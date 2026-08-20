#!/usr/bin/env bash

set -Eeuo pipefail

ROOT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
COMPOSE_FILE="$ROOT_DIR/docker-compose.prod.yml"

log() {
  printf '\033[1;34m[run-prod]\033[0m %s\n' "$*"
}

success() {
  printf '\033[1;32m[run-prod] ✔ %s\033[0m\n' "$*"
}

die() {
  printf '\033[1;31m[run-prod] ✖ Error: %s\033[0m\n' "$*" >&2
  exit 1
}

require_command() {
  command -v "$1" >/dev/null 2>&1 || die "Required command not found: $1"
}

require_command docker
require_command curl

docker info >/dev/null 2>&1 || die "Docker daemon is not running."
docker compose version >/dev/null 2>&1 || die "Docker Compose plugin is not available."

# Generate SSL certs for Nginx if missing
CERT_DIR="$ROOT_DIR/src/backend/nginx/certs"
if [[ ! -f "$CERT_DIR/dev.crt" || ! -f "$CERT_DIR/dev.key" ]]; then
  log "Generating self-signed dev SSL certificate..."
  mkdir -p "$CERT_DIR"
  if command -v openssl >/dev/null 2>&1; then
    openssl req -x509 -nodes -newkey rsa:2048 \
      -keyout "$CERT_DIR/dev.key" \
      -out "$CERT_DIR/dev.crt" \
      -days 365 \
      -subj "/CN=localhost" \
      -addext "subjectAltName=DNS:localhost" >/dev/null 2>&1 || true
  fi
fi

log "Starting HCMUS-LDMS Production Stack (Web, API, Postgres, MinIO, MailHog)..."
docker compose -f "$COMPOSE_FILE" up -d --build

log "Waiting for API service healthcheck (http://localhost:8000/health)..."
api_ready=false
for _ in {1..60}; do
  if curl --fail --silent --connect-timeout 1 --max-time 2 http://localhost:8000/health >/dev/null 2>&1; then
    api_ready=true
    break
  fi
  sleep 1
done

if [[ "$api_ready" == false ]]; then
  docker compose -f "$COMPOSE_FILE" logs --tail 50 api >&2
  die "API did not become ready within 60 seconds."
fi

success "API is up and healthy!"

log "Running automatic database seeding (Users, Categories, Sample Books)..."
docker compose -f "$COMPOSE_FILE" exec -T api uv run python -m app.scripts.seed_data || log "Warning: Seed data exited with non-zero status (tables may already be populated)."

success "HCMUS-LDMS Stack is fully deployed and ready!"

echo ""
echo "======================================================================"
echo "  🚀 HCMUS-LDMS 1-CLICK PRODUCTION SYSTEM DEPLOYED SUCCESSFULLY"
echo "======================================================================"
echo "  🌐 Web Application (HTTP):    http://localhost:8080"
echo "  🔒 Web Application (HTTPS):   https://localhost:8443"
echo "  🔌 API Server (FastAPI):       http://localhost:8000"
echo "  📖 API Interactive Docs:       http://localhost:8000/docs"
echo "  📦 MinIO Object Storage UI:    http://localhost:9003  (ldms / ldms12345)"
echo "  ✉️  Mock Mail Server (MailHog): http://localhost:8025"
echo "----------------------------------------------------------------------"
echo "  🔑 DEFAULT DEMO ACCOUNTS:"
echo "     • Admin:     admin@hcmus.edu.vn     / Admin@123456"
echo "     • Librarian: librarian@hcmus.edu.vn / Librarian@123456"
echo "     • Reader:    reader@hcmus.edu.vn    / Reader@123456"
echo "======================================================================"
echo "To stop services, run: docker compose -f docker-compose.prod.yml down"
echo ""
