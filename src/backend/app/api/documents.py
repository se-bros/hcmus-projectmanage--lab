"""M1 Documents & Storage — upload, detail, and source read-back endpoints."""

import uuid
from typing import Annotated
from urllib.parse import quote

from fastapi import APIRouter, BackgroundTasks, Depends, File, UploadFile, status
from fastapi.responses import StreamingResponse

from app.api.dependencies import DbSession
from app.core.exceptions import UnauthorizedError
from app.core.security import AuthenticatedUser, get_optional_user, require_roles
from app.models.document import Document
from app.schemas.document import DocumentDetail, DocumentUploadResponse
from app.services.document_service import get_document, open_document_source, upload_document
from app.workers.ocr import run_ocr_job

router = APIRouter(prefix="/documents", tags=["documents"])


@router.post(
    "",
    response_model=DocumentUploadResponse,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(require_roles("editor", "admin"))],
)
def create_document(
    background_tasks: BackgroundTasks,
    db: DbSession,
    file: UploadFile = File(...),
) -> DocumentUploadResponse:
    document, job = upload_document(db, file)
    background_tasks.add_task(run_ocr_job, job.id)
    return DocumentUploadResponse(document_id=document.id)


def _ensure_readable(document: Document, user: AuthenticatedUser | None) -> Document:
    if not document.is_public and user is None:
        raise UnauthorizedError("Authentication required to access this document.")
    return document


@router.get("/{document_id}", response_model=DocumentDetail)
def read_document(
    document_id: uuid.UUID,
    db: DbSession,
    user: Annotated[AuthenticatedUser | None, Depends(get_optional_user)],
) -> Document:
    return _ensure_readable(get_document(db, document_id), user)


@router.get("/{document_id}/source")
def read_document_source(
    document_id: uuid.UUID,
    db: DbSession,
    user: Annotated[AuthenticatedUser | None, Depends(get_optional_user)],
) -> StreamingResponse:
    _ensure_readable(get_document(db, document_id), user)
    document, source = open_document_source(db, document_id)
    filename = quote(document.original_filename)
    return StreamingResponse(
        source,
        media_type=document.content_type,
        headers={"Content-Disposition": f"inline; filename*=UTF-8''{filename}"},
    )
