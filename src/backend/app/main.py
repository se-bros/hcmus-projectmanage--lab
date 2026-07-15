import logging
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqlalchemy import text

from app.api import auth, documents, editor, health, metadata, ocr, publish, reader, search
from app.core.config import settings
from app.core.exceptions import register_exception_handlers
from app.core.logging import configure_logging
from app.core.storage import ensure_bucket_exists
from app.db.session import engine
from app.middleware.cors import setup_cors

configure_logging()
logger = logging.getLogger("app")


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    logger.info("Starting HCMUS-LDMS API (env=%s)", settings.app_env)

    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
    except Exception:
        logger.exception("Database unreachable at startup — check DATABASE_URL / postgres service")
        raise

    try:
        ensure_bucket_exists()
    except Exception:
        logger.exception("MinIO unreachable at startup — check MINIO_* env vars / minio service")
        raise

    logger.info("Startup checks passed (DB + MinIO reachable, bucket=%r)", settings.minio_bucket)

    yield

    logger.info("Shutting down HCMUS-LDMS API")
    engine.dispose()


app = FastAPI(title="HCMUS-LDMS API", lifespan=lifespan)

setup_cors(app)
register_exception_handlers(app)


# Sample
app.include_router(health.router)
app.include_router(auth.router)
app.include_router(documents.router)
app.include_router(ocr.router)
app.include_router(editor.router)
app.include_router(metadata.router)
app.include_router(publish.router)
app.include_router(reader.router)
app.include_router(search.router)
