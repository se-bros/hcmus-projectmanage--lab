"""M2 OCR — background jobs, status, page text, and page previews."""

import uuid
from collections.abc import Iterator

from fastapi import APIRouter, BackgroundTasks, Depends, Query, status
from fastapi.responses import StreamingResponse

from app.api.dependencies import DbSession
from app.core.config import settings
from app.core.exceptions import NotFoundError
from app.core.security import require_roles
from app.core.storage import minio_client
from app.schemas.document import OcrDashboardItem, OcrJobAccepted, OcrJobDetail, PageSummary
from app.services.ocr_service import (
    create_ocr_job,
    get_page,
    latest_ocr_job,
    list_latest_ocr_jobs,
    list_pages,
)
from app.workers.ocr import run_ocr_job

router = APIRouter(prefix="/documents", tags=["ocr"])
dashboard_router = APIRouter(prefix="/ocr", tags=["ocr"])


def _job_detail(job_id: uuid.UUID, job: object) -> OcrJobDetail:
    return OcrJobDetail(
        job_id=job_id,
        attempt=job.attempt,
        status=job.status,
        error_message=job.error_message,
        created_at=job.created_at,
        updated_at=job.updated_at,
    )


@dashboard_router.get("/jobs", response_model=list[OcrDashboardItem])
def read_ocr_dashboard(
    db: DbSession,
    limit: int = Query(default=100, ge=1, le=200),
) -> list[OcrDashboardItem]:
    return [
        OcrDashboardItem(
            document_id=document.id,
            original_filename=document.original_filename,
            document_status=document.status,
            job_id=job.id if job else None,
            attempt=job.attempt if job else None,
            ocr_status=job.status if job else None,
            error_message=job.error_message if job else None,
            created_at=document.created_at,
            updated_at=job.updated_at if job else None,
        )
        for document, job in list_latest_ocr_jobs(db, limit)
    ]


@router.post(
    "/{document_id}/ocr",
    response_model=OcrJobAccepted,
    status_code=status.HTTP_202_ACCEPTED,
    dependencies=[Depends(require_roles("editor", "admin"))],
)
def start_ocr(
    document_id: uuid.UUID,
    background_tasks: BackgroundTasks,
    db: DbSession,
) -> OcrJobAccepted:
    job = create_ocr_job(db, document_id)
    background_tasks.add_task(run_ocr_job, job.id)
    return OcrJobAccepted(job_id=job.id, attempt=job.attempt, status=job.status)


@router.get("/{document_id}/ocr", response_model=OcrJobDetail)
def read_ocr_status(document_id: uuid.UUID, db: DbSession) -> OcrJobDetail:
    job = latest_ocr_job(db, document_id)
    return _job_detail(job.id, job)


@router.get("/{document_id}/pages", response_model=list[PageSummary])
def read_pages(document_id: uuid.UUID, db: DbSession) -> list[PageSummary]:
    return [
        PageSummary(
            page_number=page.page_number,
            text_content=page.text_content,
            has_image=page.image_object_key is not None,
        )
        for page in list_pages(db, document_id)
    ]


@router.get("/{document_id}/pages/{page_number}/image")
def read_page_image(
    document_id: uuid.UUID,
    page_number: int,
    db: DbSession,
) -> StreamingResponse:
    page = get_page(db, document_id, page_number)
    if page.image_object_key is None:
        raise NotFoundError("Page image not found.")
    response = minio_client.get_object(settings.minio_bucket, page.image_object_key)

    def stream() -> Iterator[bytes]:
        try:
            if hasattr(response, "stream"):
                yield from response.stream(32 * 1024)
            else:
                while chunk := response.read(32 * 1024):
                    yield chunk
        finally:
            if hasattr(response, "close"):
                response.close()
            if hasattr(response, "release_conn"):
                response.release_conn()

    return StreamingResponse(stream(), media_type="image/png")
