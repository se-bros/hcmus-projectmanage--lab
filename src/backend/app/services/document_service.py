import logging
import uuid
from collections.abc import Iterator
from pathlib import PurePath
from typing import Protocol

from fastapi import UploadFile
from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.exceptions import NotFoundError, ValidationError
from app.core.storage import minio_client
from app.models.document import Document
from app.models.ocr_job import OcrJob
from app.repositories.document_repository import DocumentRepository

logger = logging.getLogger(__name__)


class StorageClient(Protocol):
    def put_object(self, **kwargs: object) -> object: ...

    def get_object(self, bucket_name: str, object_name: str) -> object: ...

    def remove_object(self, bucket_name: str, object_name: str) -> object: ...


ALLOWED_UPLOADS = {
    ".pdf": ("application/pdf", lambda header: header.startswith(b"%PDF-")),
    ".jpg": ("image/jpeg", lambda header: header.startswith(b"\xff\xd8\xff")),
    ".jpeg": ("image/jpeg", lambda header: header.startswith(b"\xff\xd8\xff")),
    ".png": ("image/png", lambda header: header.startswith(b"\x89PNG\r\n\x1a\n")),
}


def _validate_upload(file: UploadFile) -> tuple[str, str, int]:
    original_filename = PurePath(file.filename or "").name
    extension = PurePath(original_filename).suffix.lower()
    if extension not in ALLOWED_UPLOADS:
        raise ValidationError("Unsupported file extension. Allowed: PDF, JPG, JPEG, PNG.")

    expected_mime, has_valid_magic = ALLOWED_UPLOADS[extension]
    actual_mime = (file.content_type or "").split(";", 1)[0].strip().lower()
    if actual_mime != expected_mime:
        raise ValidationError(
            f"Content-Type {actual_mime or 'missing'} does not match {extension} ({expected_mime})."
        )

    file.file.seek(0)
    header = file.file.read(16)
    if not has_valid_magic(header):
        raise ValidationError(f"File content does not match the {extension} format.")

    file.file.seek(0, 2)
    length = file.file.tell()
    file.file.seek(0)
    if length == 0:
        raise ValidationError("Uploaded file is empty.")
    return original_filename, expected_mime, length


def upload_document(
    db: Session,
    file: UploadFile,
    storage_client: StorageClient | None = None,
) -> tuple[Document, OcrJob]:
    original_filename, content_type, length = _validate_upload(file)
    document_id = uuid.uuid4()
    object_key = f"documents/{document_id}/{original_filename}"
    client = storage_client or minio_client

    client.put_object(
        bucket_name=settings.minio_bucket,
        object_name=object_key,
        data=file.file,
        length=length,
        content_type=content_type,
    )

    try:
        document = DocumentRepository(db).create(
            document_id=document_id,
            original_filename=original_filename,
            object_key=object_key,
            content_type=content_type,
            status="ocr_pending",
        )
        job = OcrJob(id=uuid.uuid4(), document_id=document_id, attempt=1, status="pending")
        db.add(job)
        db.commit()
    except Exception:
        db.rollback()
        try:
            client.remove_object(settings.minio_bucket, object_key)
        except Exception:
            logger.exception("Could not roll back MinIO object %s", object_key)
        raise
    db.refresh(document)
    db.refresh(job)
    return document, job


def get_document(db: Session, document_id: uuid.UUID) -> Document:
    document = DocumentRepository(db).get(document_id)
    if document is None:
        raise NotFoundError("Document not found.")
    return document


def open_document_source(
    db: Session,
    document_id: uuid.UUID,
    storage_client: StorageClient | None = None,
) -> tuple[Document, Iterator[bytes]]:
    document = get_document(db, document_id)
    response = (storage_client or minio_client).get_object(
        settings.minio_bucket, document.object_key
    )

    def stream() -> Iterator[bytes]:
        try:
            if hasattr(response, "stream"):
                yield from response.stream(32 * 1024)
            else:
                reader = response
                while chunk := reader.read(32 * 1024):
                    yield chunk
        finally:
            if hasattr(response, "close"):
                response.close()
            if hasattr(response, "release_conn"):
                response.release_conn()

    return document, stream()
