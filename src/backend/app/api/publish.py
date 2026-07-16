"""M5 Publish EPUB — background publishing and metadata gate."""

import uuid

from fastapi import APIRouter, BackgroundTasks, status

from app.api.dependencies import DbSession
from app.schemas.document import PublishJobAccepted, PublishJobDetail
from app.services.publish_service import create_publish_job, latest_publish_job
from app.workers.publish import run_publish_job

router = APIRouter(prefix="/documents", tags=["publish"])


@router.post(
    "/{document_id}/publish",
    response_model=PublishJobAccepted,
    status_code=status.HTTP_202_ACCEPTED,
)
def publish_document(
    document_id: uuid.UUID,
    background_tasks: BackgroundTasks,
    db: DbSession,
) -> PublishJobAccepted:
    job = create_publish_job(db, document_id)
    background_tasks.add_task(run_publish_job, job.id)
    return PublishJobAccepted(publish_job_id=job.id, attempt=job.attempt, status=job.status)


@router.get("/{document_id}/publish", response_model=PublishJobDetail)
def read_publish_status(document_id: uuid.UUID, db: DbSession) -> PublishJobDetail:
    job = latest_publish_job(db, document_id)
    return PublishJobDetail(
        publish_job_id=job.id,
        attempt=job.attempt,
        status=job.status,
        error_message=job.error_message,
        created_at=job.created_at,
        updated_at=job.updated_at,
    )
