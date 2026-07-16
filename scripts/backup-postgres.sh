#!/usr/bin/env bash
set -Eeuo pipefail

ROOT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
BACKEND_DIR="$ROOT_DIR/src/backend"
BACKUP_DIR="${LDMS_BACKUP_DIR:-$ROOT_DIR/.backups/postgres}"
RETENTION_DAYS="${LDMS_BACKUP_RETENTION_DAYS:-30}"
TIMESTAMP="$(date +%Y%m%d-%H%M%S)"

mkdir -p "$BACKUP_DIR"

# shellcheck disable=SC1091
source "$BACKEND_DIR/.env"

docker compose --project-directory "$BACKEND_DIR" --file "$BACKEND_DIR/docker-compose.yml" \
  exec -T postgres pg_dump -U "${POSTGRES_USER:-ldms}" -Fc "${POSTGRES_DB:-ldms}" \
  > "$BACKUP_DIR/ldms-$TIMESTAMP.dump"

echo "Backup written to $BACKUP_DIR/ldms-$TIMESTAMP.dump"

find "$BACKUP_DIR" -name '*.dump' -mtime "+$RETENTION_DAYS" -print -delete
