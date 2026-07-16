"""M1 Documents & Storage — LDMS-002 Day 1 upload and detail endpoints."""

import uuid

from fastapi import APIRouter, File, UploadFile, status

from app.api.dependencies import DbSession
from app.models.document import Document
from app.schemas.document import DocumentDetail, DocumentUploadResponse
from app.services.document_service import get_document, upload_document

router = APIRouter(prefix="/documents", tags=["documents"])


@router.post("", response_model=DocumentUploadResponse, status_code=status.HTTP_201_CREATED)
def create_document(db: DbSession, file: UploadFile = File(...)) -> DocumentUploadResponse:
    document = upload_document(db, file)
    return DocumentUploadResponse(document_id=document.id)


@router.get("/{document_id}", response_model=DocumentDetail)
def read_document(document_id: uuid.UUID, db: DbSession) -> Document | None:
    return get_document(db, document_id)
