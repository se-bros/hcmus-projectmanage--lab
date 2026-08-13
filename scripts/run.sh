#!/usr/bin/env bash

set -Eeuo pipefail

ROOT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
BACKEND_DIR="$ROOT_DIR/src/backend"
FRONTEND_DIR="$ROOT_DIR/src/frontend"
COMPOSE=(
  docker compose
  --project-directory "$BACKEND_DIR"
  --file "$BACKEND_DIR/docker-compose.yml"
)

FRONTEND_PID=""

log() {
  printf '[run] %s\n' "$*"
}

die() {
  printf '[run] Error: %s\n' "$*" >&2
  exit 1
}

require_command() {
  command -v "$1" >/dev/null 2>&1 || die "Required command not found: $1"
}

stop_running_services() {
  log "Stopping any existing containers for this project..."
  "${COMPOSE[@]}" down --remove-orphans >/dev/null 2>&1 || true
}

cleanup() {
  local exit_code=$?
  trap - EXIT INT TERM
  set +e

  if [[ -n "$FRONTEND_PID" ]] && kill -0 "$FRONTEND_PID" 2>/dev/null; then
    log "Stopping frontend..."
    kill -TERM "$FRONTEND_PID" 2>/dev/null
    wait "$FRONTEND_PID" 2>/dev/null
  fi

  if command -v fuser >/dev/null 2>&1; then
    fuser -k 5173/tcp >/dev/null 2>&1 || true
  fi

  log "Stopping API, PostgreSQL, and MinIO..."
  "${COMPOSE[@]}" down

  exit "$exit_code"
}

trap cleanup EXIT
trap 'exit 130' INT
trap 'exit 143' TERM

require_command docker
require_command npm
require_command curl

docker info >/dev/null 2>&1 || die "Docker daemon is not available."
docker compose version >/dev/null 2>&1 || die "Docker Compose plugin is not available."

if [[ ! -f "$BACKEND_DIR/docker-compose.yml" ]]; then
  die "Missing backend Compose file: $BACKEND_DIR/docker-compose.yml"
fi
if [[ ! -f "$FRONTEND_DIR/package-lock.json" ]]; then
  die "Missing frontend lockfile: $FRONTEND_DIR/package-lock.json"
fi

if [[ ! -f "$FRONTEND_DIR/node_modules/.package-lock.json" ]] || \
  [[ "$FRONTEND_DIR/package-lock.json" -nt "$FRONTEND_DIR/node_modules/.package-lock.json" ]]; then
  log "Installing frontend dependencies from package-lock.json..."
  (cd "$FRONTEND_DIR" && npm ci)
fi

stop_running_services

log "Starting API, PostgreSQL, and MinIO..."
"${COMPOSE[@]}" up -d --build

log "Waiting for the API health check..."
api_ready=false
for _ in {1..60}; do
  if curl --fail --silent --connect-timeout 1 --max-time 2 \
    http://localhost:8000/health >/dev/null; then
    api_ready=true
    break
  fi
  sleep 1
done

if [[ "$api_ready" == false ]]; then
  "${COMPOSE[@]}" logs --tail 80 api >&2
  die "API did not become ready within 60 seconds."
fi

log "Applying database migrations..."
"${COMPOSE[@]}" exec -T api uv run --no-dev alembic upgrade head

log "Services are ready:"
log "  Frontend:      http://localhost:5173"
log "  API:           http://localhost:8000"
log "  MinIO console: http://localhost:9003"
log "Press Ctrl+C to stop."

(
  cd "$FRONTEND_DIR"
  exec npm run dev -- --host 0.0.0.0 --strictPort
) &
FRONTEND_PID=$!

wait "$FRONTEND_PID"
