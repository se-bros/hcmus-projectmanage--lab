import logging
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from app.api import auth, documents, editor, health, metadata, ocr, publish, reader, search
from app.core.config import settings
from app.core.exceptions import register_exception_handlers
from app.core.logging import configure_logging
from app.core.storage import ensure_bucket_exists
from app.db.session import engine
from app.middleware.cors import setup_cors
from app.workers.ocr import recover_interrupted_ocr_jobs
from app.workers.publish import recover_interrupted_publish_jobs

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

    try:
        recovered_ocr = recover_interrupted_ocr_jobs()
        recovered_publish = recover_interrupted_publish_jobs()
        if recovered_ocr or recovered_publish:
            logger.warning(
                "Marked interrupted jobs failed (ocr=%d, publish=%d)",
                recovered_ocr,
                recovered_publish,
            )
    except SQLAlchemyError:
        # A brand-new environment applies Alembic immediately after the first health check.
        logger.warning("Job recovery skipped because migrations are not applied yet")

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
app.include_router(ocr.dashboard_router)
app.include_router(editor.router)
app.include_router(metadata.router)
app.include_router(metadata.category_router)
app.include_router(publish.router)
app.include_router(reader.router)
app.include_router(search.router)
