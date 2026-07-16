import logging
import tempfile
import uuid
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path
from typing import Protocol

import pytesseract
from pdf2image import convert_from_path
from PIL import Image
from sqlalchemy import delete, select
from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.storage import minio_client
from app.db.session import SessionLocal
from app.models.ocr_job import OcrJob
from app.models.page import Page

logger = logging.getLogger(__name__)


class StorageClient(Protocol):
    def get_object(self, bucket_name: str, object_name: str) -> object: ...

    def put_object(self, **kwargs: object) -> object: ...


@dataclass(frozen=True)
class ProcessedPage:
    page_number: int
    text_content: str
    preview_path: Path


def _download_source(client: StorageClient, object_key: str, destination: Path) -> None:
    response = client.get_object(settings.minio_bucket, object_key)
    try:
        with destination.open("wb") as output:
            if hasattr(response, "stream"):
                for chunk in response.stream(32 * 1024):
                    output.write(chunk)
            else:
                while chunk := response.read(32 * 1024):
                    output.write(chunk)
    finally:
        if hasattr(response, "close"):
            response.close()
        if hasattr(response, "release_conn"):
            response.release_conn()


def _process_source(source_path: Path, content_type: str, workdir: Path) -> list[ProcessedPage]:
    if content_type == "application/pdf":
        images = convert_from_path(
            source_path,
            dpi=settings.ocr_dpi,
            fmt="png",
            output_folder=workdir,
            timeout=settings.pdf_render_timeout_seconds,
        )
    else:
        with Image.open(source_path) as source_image:
            images = [source_image.convert("RGB")]

    pages: list[ProcessedPage] = []
    try:
        for page_number, image in enumerate(images, start=1):
            preview_path = workdir / f"page-{page_number}.png"
            image.save(preview_path, format="PNG")
            text = pytesseract.image_to_string(
                image,
                lang=settings.ocr_language,
                timeout=settings.ocr_timeout_seconds,
            )
            pages.append(ProcessedPage(page_number, text, preview_path))
    finally:
        for image in images:
            image.close()
    if not pages:
        raise RuntimeError("OCR source did not produce any pages.")
    return pages


def _mark_failed(
    job_id: uuid.UUID,
    message: str,
    session_factory: Callable[[], Session],
) -> None:
    with session_factory() as db:
        job = db.get(OcrJob, job_id)
        if job is None:
            return
        job.status = "failed"
        job.error_message = message[:4000]
        job.document.status = "ocr_failed"
        db.commit()


def run_ocr_job(
    job_id: uuid.UUID,
    session_factory: Callable[[], Session] = SessionLocal,
    storage_client: StorageClient | None = None,
) -> None:
    client = storage_client or minio_client
    try:
        with session_factory() as db:
            job = db.get(OcrJob, job_id)
            if job is None or job.status != "pending":
                return
            job.status = "processing"
            job.error_message = None
            job.document.status = "ocr_processing"
            db.commit()
            document_id = job.document_id
            object_key = job.document.object_key
            content_type = job.document.content_type

        with tempfile.TemporaryDirectory(prefix=f"ocr-{job_id}-") as temporary_directory:
            workdir = Path(temporary_directory)
            source_path = workdir / f"source{Path(object_key).suffix.lower()}"
            _download_source(client, object_key, source_path)
            processed_pages = _process_source(source_path, content_type, workdir)

            page_values: list[tuple[ProcessedPage, str]] = []
            for page in processed_pages:
                image_object_key = f"documents/{document_id}/pages/{page.page_number}.png"
                with page.preview_path.open("rb") as preview:
                    client.put_object(
                        bucket_name=settings.minio_bucket,
                        object_name=image_object_key,
                        data=preview,
                        length=page.preview_path.stat().st_size,
                        content_type="image/png",
                    )
                page_values.append((page, image_object_key))

            with session_factory() as db:
                job = db.get(OcrJob, job_id)
                if job is None or job.status != "processing":
                    return
                db.execute(delete(Page).where(Page.document_id == document_id))
                db.flush()
                for page, image_object_key in page_values:
                    db.add(
                        Page(
                            id=uuid.uuid4(),
                            document_id=document_id,
                            page_number=page.page_number,
                            text_content=page.text_content,
                            image_object_key=image_object_key,
                        )
                    )
                job.status = "completed"
                job.error_message = None
                job.document.status = "ocr_completed"
                db.commit()
    except Exception as exc:
        logger.exception("OCR job %s failed", job_id)
        try:
            _mark_failed(job_id, str(exc) or exc.__class__.__name__, session_factory)
        except Exception:
            logger.exception("Could not persist failure for OCR job %s", job_id)


def recover_interrupted_ocr_jobs(session_factory: Callable[[], Session] = SessionLocal) -> int:
    with session_factory() as db:
        jobs = list(db.scalars(select(OcrJob).where(OcrJob.status.in_(("pending", "processing")))))
        for job in jobs:
            job.status = "failed"
            job.error_message = "OCR interrupted by API restart; retry the job."
            job.document.status = "ocr_failed"
        db.commit()
        return len(jobs)
