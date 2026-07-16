#!/usr/bin/env bash
set -Eeuo pipefail

ROOT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
BACKEND_DIR="$ROOT_DIR/src/backend"
BACKUP_DIR="${LDMS_BACKUP_DIR:-$ROOT_DIR/.backups/minio}"

mkdir -p "$BACKUP_DIR"

# shellcheck disable=SC1091
source "$BACKEND_DIR/.env"

MINIO_CONTAINER="$(docker compose --project-directory "$BACKEND_DIR" \
  --file "$BACKEND_DIR/docker-compose.yml" ps -q minio)"

docker run --rm --network "container:$MINIO_CONTAINER" \
  -v "$BACKUP_DIR:/backup" \
  --entrypoint sh \
  minio/mc:latest \
  -c "mc alias set src http://localhost:9000 '${MINIO_ROOT_USER:-ldms}' '${MINIO_ROOT_PASSWORD:-ldms12345}' \
    && mc mirror --overwrite src/${MINIO_BUCKET:-ldms} /backup"

echo "Mirrored MinIO bucket ${MINIO_BUCKET:-ldms} to $BACKUP_DIR"
