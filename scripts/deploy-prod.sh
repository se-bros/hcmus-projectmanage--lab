#!/usr/bin/env bash
# Prod-like deploy: Docker Compose profile "prod" + health check + Alembic.
# Continuous Delivery thủ công — không phải CD tự động lên VMware.

set -Eeuo pipefail

ROOT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
BACKEND_DIR="$ROOT_DIR/src/backend"
CERT_DIR="$BACKEND_DIR/nginx/certs"
COMPOSE=(
  docker compose
  --project-directory "$BACKEND_DIR"
  --file "$BACKEND_DIR/docker-compose.yml"
  --profile prod
)

log() {
  printf '[deploy-prod] %s\n' "$*"
}

die() {
  printf '[deploy-prod] Error: %s\n' "$*" >&2
  exit 1
}

require_command() {
  command -v "$1" >/dev/null 2>&1 || die "Required command not found: $1"
}

require_command docker
require_command curl

docker info >/dev/null 2>&1 || die "Docker daemon is not available."
docker compose version >/dev/null 2>&1 || die "Docker Compose plugin is not available."

if [[ ! -f "$BACKEND_DIR/docker-compose.yml" ]]; then
  die "Missing Compose file: $BACKEND_DIR/docker-compose.yml"
fi

if [[ ! -f "$BACKEND_DIR/.env" ]]; then
  if [[ -f "$BACKEND_DIR/.env.example" ]]; then
    log "No .env found — copying from .env.example (review secrets before real use)."
    cp "$BACKEND_DIR/.env.example" "$BACKEND_DIR/.env"
  else
    die "Missing $BACKEND_DIR/.env (and no .env.example to copy)."
  fi
fi

if [[ ! -f "$CERT_DIR/dev.crt" || ! -f "$CERT_DIR/dev.key" ]]; then
  log "TLS cert missing — generating self-signed cert for local demo..."
  "$ROOT_DIR/scripts/generate-dev-cert.sh"
fi

log "Building and starting stack with Compose profile 'prod'..."
"${COMPOSE[@]}" up -d --build

log "Waiting for API health check at http://localhost:8000/health ..."
api_ready=false
for _ in {1..90}; do
  if curl --fail --silent --connect-timeout 1 --max-time 2 \
    http://localhost:8000/health >/dev/null; then
    api_ready=true
    break
  fi
  sleep 1
done

if [[ "$api_ready" == false ]]; then
  log "Health check failed — recent logs:"
  "${COMPOSE[@]}" logs --tail 80 api >&2 || true
  "${COMPOSE[@]}" logs --tail 40 nginx >&2 || true
  die "API did not become ready within 90 seconds. Stack left running for inspection; run: cd src/backend && docker compose --profile prod down"
fi

log "Applying database migrations (alembic upgrade head)..."
"${COMPOSE[@]}" exec -T api uv run --no-dev alembic upgrade head

log "Deploy succeeded (prod-like local)."
log "  HTTPS (Nginx): https://localhost:8443"
log "  HTTP  (Nginx): http://localhost:8080"
log "  API health:    http://localhost:8000/health"
log "Self-signed TLS is for demo only. Rollback: compose --profile prod down, git checkout previous tag, re-run this script."
