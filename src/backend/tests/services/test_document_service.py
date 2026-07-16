from io import BytesIO

import pytest
from fastapi import UploadFile
from sqlalchemy import create_engine, func, select
from sqlalchemy.orm import Session
from starlette.datastructures import Headers

from app.core.config import settings
from app.db.base import Base
from app.models.document import Document
from app.models.ocr_job import OcrJob
from app.services.document_service import upload_document
from tests.fakes import InMemoryStorage


def _pdf_upload() -> UploadFile:
    return UploadFile(
        filename="sample.pdf",
        file=BytesIO(b"%PDF-1.7 sample scan"),
        headers=Headers({"content-type": "application/pdf"}),
    )


def test_upload_streams_file_and_commits_document_with_job() -> None:
    engine = create_engine("sqlite://")
    Base.metadata.create_all(engine)
    storage = InMemoryStorage()

    with Session(engine) as db:
        document, job = upload_document(db, _pdf_upload(), storage)
        assert document.original_filename == "sample.pdf"
        assert document.status == "ocr_pending"
        assert job.document_id == document.id
        assert storage.uploads[0]["bucket_name"] == settings.minio_bucket
        assert storage.uploads[0]["object_name"] == document.object_key
        assert storage.uploads[0]["content_type"] == "application/pdf"
        assert storage.uploads[0]["body"] == b"%PDF-1.7 sample scan"
    engine.dispose()


def test_database_failure_rolls_back_minio_object(monkeypatch) -> None:
    engine = create_engine("sqlite://")
    Base.metadata.create_all(engine)
    storage = InMemoryStorage()

    with Session(engine) as db:
        monkeypatch.setattr(db, "commit", lambda: (_ for _ in ()).throw(RuntimeError("db down")))
        with pytest.raises(RuntimeError, match="db down"):
            upload_document(db, _pdf_upload(), storage)
        assert len(storage.removed) == 1
        assert storage.objects == {}

    with Session(engine) as db:
        assert db.scalar(select(func.count()).select_from(Document)) == 0
        assert db.scalar(select(func.count()).select_from(OcrJob)) == 0
    engine.dispose()
