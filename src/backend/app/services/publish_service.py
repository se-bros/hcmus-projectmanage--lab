import uuid

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.exceptions import ConflictError, NotFoundError, ValidationError
from app.models.document import Document
from app.models.page import Page
from app.models.publish_job import PublishJob

ACTIVE_PUBLISH_STATUSES = {"pending", "publishing"}


def validate_publishable(db: Session, document: Document) -> list[Page]:
    missing_fields = [
        field for field in ("title", "author") if not (getattr(document, field, None) or "").strip()
    ]
    if missing_fields:
        raise ValidationError(
            {
                "message": "Required metadata is missing.",
                "missing_fields": missing_fields,
            }
        )

    pages = list(
        db.scalars(select(Page).where(Page.document_id == document.id).order_by(Page.page_number))
    )
    missing_page_numbers = [page.page_number for page in pages if not page.text_content.strip()]
    if not pages or missing_page_numbers:
        raise ValidationError(
            {
                "message": "Every document page must contain text before publishing.",
                "missing_page_numbers": missing_page_numbers,
                "has_pages": bool(pages),
            }
        )
    return pages


def create_publish_job(db: Session, document_id: uuid.UUID) -> PublishJob:
    document = db.scalar(select(Document).where(Document.id == document_id).with_for_update())
    if document is None:
        raise NotFoundError("Document not found.")
    validate_publishable(db, document)

    latest = db.scalar(
        select(PublishJob)
        .where(PublishJob.document_id == document_id)
        .order_by(PublishJob.attempt.desc(), PublishJob.created_at.desc())
        .limit(1)
    )
    if latest is not None and latest.status in ACTIVE_PUBLISH_STATUSES:
        raise ConflictError(f"Publish job is already {latest.status}.")

    job = PublishJob(
        id=uuid.uuid4(),
        document_id=document_id,
        attempt=(latest.attempt + 1) if latest else 1,
        status="pending",
    )
    db.add(job)
    db.commit()
    db.refresh(job)
    return job


def latest_publish_job(db: Session, document_id: uuid.UUID) -> PublishJob:
    if db.get(Document, document_id) is None:
        raise NotFoundError("Document not found.")
    job = db.scalar(
        select(PublishJob)
        .where(PublishJob.document_id == document_id)
        .order_by(PublishJob.attempt.desc(), PublishJob.created_at.desc())
        .limit(1)
    )
    if job is None:
        raise NotFoundError("Publish job not found.")
    return job
