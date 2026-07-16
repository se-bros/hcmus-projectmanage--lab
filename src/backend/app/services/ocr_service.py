import uuid

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.exceptions import ConflictError, NotFoundError
from app.models.document import Document
from app.models.ocr_job import OcrJob
from app.models.page import Page

ACTIVE_OCR_STATUSES = {"pending", "processing"}


def _document_or_404(db: Session, document_id: uuid.UUID) -> Document:
    document = db.get(Document, document_id)
    if document is None:
        raise NotFoundError("Document not found.")
    return document


def latest_ocr_job(db: Session, document_id: uuid.UUID) -> OcrJob:
    _document_or_404(db, document_id)
    job = db.scalar(
        select(OcrJob)
        .where(OcrJob.document_id == document_id)
        .order_by(OcrJob.attempt.desc(), OcrJob.created_at.desc())
        .limit(1)
    )
    if job is None:
        raise NotFoundError("OCR job not found.")
    return job


def create_ocr_job(db: Session, document_id: uuid.UUID) -> OcrJob:
    document = db.scalar(select(Document).where(Document.id == document_id).with_for_update())
    if document is None:
        raise NotFoundError("Document not found.")
    latest = db.scalar(
        select(OcrJob)
        .where(OcrJob.document_id == document_id)
        .order_by(OcrJob.attempt.desc(), OcrJob.created_at.desc())
        .limit(1)
    )
    if latest is not None and latest.status in ACTIVE_OCR_STATUSES | {"completed"}:
        raise ConflictError(f"OCR job is already {latest.status}.")

    job = OcrJob(
        id=uuid.uuid4(),
        document_id=document_id,
        attempt=(latest.attempt + 1) if latest else 1,
        status="pending",
    )
    document.status = "ocr_pending"
    db.add(job)
    db.commit()
    db.refresh(job)
    return job


def list_pages(db: Session, document_id: uuid.UUID) -> list[Page]:
    _document_or_404(db, document_id)
    return list(
        db.scalars(select(Page).where(Page.document_id == document_id).order_by(Page.page_number))
    )


def get_page(db: Session, document_id: uuid.UUID, page_number: int) -> Page:
    _document_or_404(db, document_id)
    page = db.scalar(
        select(Page).where(
            Page.document_id == document_id,
            Page.page_number == page_number,
        )
    )
    if page is None:
        raise NotFoundError("Page not found.")
    return page


def list_latest_ocr_jobs(db: Session, limit: int = 100) -> list[tuple[Document, OcrJob | None]]:
    latest_job_id = (
        select(OcrJob.id)
        .where(OcrJob.document_id == Document.id)
        .order_by(OcrJob.attempt.desc(), OcrJob.created_at.desc())
        .limit(1)
        .correlate(Document)
        .scalar_subquery()
    )
    rows = db.execute(
        select(Document, OcrJob)
        .outerjoin(OcrJob, OcrJob.id == latest_job_id)
        .order_by(Document.created_at.desc())
        .limit(limit)
    )
    return [(document, job) for document, job in rows]
