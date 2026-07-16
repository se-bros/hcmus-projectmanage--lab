from io import BytesIO
from typing import BinaryIO, cast

from fastapi import UploadFile
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from starlette.datastructures import Headers

from app.core.config import settings
from app.db.base import Base
from app.services.document_service import upload_document


class RecordingStorage:
    def __init__(self) -> None:
        self.upload: dict[str, object] = {}

    def put_object(self, **kwargs: object) -> None:
        data = cast(BinaryIO, kwargs["data"])
        self.upload = {**kwargs, "body": data.read()}


def test_upload_streams_file_to_minio_and_persists_document() -> None:
    engine = create_engine("sqlite://")
    Base.metadata.create_all(engine)
    storage = RecordingStorage()
    body = b"%PDF-1.7 sample scan"
    upload = UploadFile(
        filename="sample.pdf",
        file=BytesIO(body),
        headers=Headers({"content-type": "application/pdf"}),
    )

    with Session(engine) as db:
        document = upload_document(db, upload, storage)  # type: ignore[arg-type]

        assert document.original_filename == "sample.pdf"
        assert document.status == "uploaded"
        assert document.object_key == f"documents/{document.id}/sample.pdf"
        assert storage.upload["bucket_name"] == settings.minio_bucket
        assert storage.upload["object_name"] == document.object_key
        assert storage.upload["length"] == len(body)
        assert storage.upload["content_type"] == "application/pdf"
        assert storage.upload["body"] == body
