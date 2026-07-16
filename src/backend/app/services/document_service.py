import uuid
from pathlib import PurePath

from fastapi import UploadFile
from minio import Minio
from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.storage import minio_client
from app.models.document import Document
from app.repositories.document_repository import DocumentRepository


def upload_document(
    db: Session,
    file: UploadFile,
    storage_client: Minio | None = None,
) -> Document:
    document_id = uuid.uuid4()
    original_filename = PurePath(file.filename or "scan").name
    object_key = f"documents/{document_id}/{original_filename}"

    file.file.seek(0, 2)
    length = file.file.tell()
    file.file.seek(0)

    client = storage_client or minio_client
    client.put_object(
        bucket_name=settings.minio_bucket,
        object_name=object_key,
        data=file.file,
        length=length,
        content_type=file.content_type or "application/octet-stream",
    )

    return DocumentRepository(db).create(
        document_id=document_id,
        original_filename=original_filename,
        object_key=object_key,
    )


def get_document(db: Session, document_id: uuid.UUID) -> Document | None:
    return DocumentRepository(db).get(document_id)
