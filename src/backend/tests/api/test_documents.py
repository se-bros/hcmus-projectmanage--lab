from collections.abc import Generator
from typing import BinaryIO, cast

from fastapi.testclient import TestClient
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.pool import StaticPool

from app.db.base import Base
from app.db.session import get_db
from app.main import app
from app.models.document import Document
from app.services import document_service


class InMemoryStorage:
    def put_object(self, **kwargs: object) -> None:
        data = cast(BinaryIO, kwargs["data"])
        data.read()


def test_upload_then_get_document_metadata(monkeypatch) -> None:
    engine = create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    Base.metadata.create_all(engine)
    testing_session = sessionmaker(bind=engine)

    def override_get_db() -> Generator[Session, None, None]:
        with testing_session() as db:
            yield db

    app.dependency_overrides[get_db] = override_get_db
    monkeypatch.setattr(document_service, "minio_client", InMemoryStorage())

    try:
        client = TestClient(app)
        upload_response = client.post(
            "/documents",
            files={"file": ("scan.pdf", b"%PDF sample", "application/pdf")},
        )

        assert upload_response.status_code == 201
        document_id = upload_response.json()["document_id"]

        with testing_session() as db:
            persisted = db.scalar(select(Document))
            assert persisted is not None
            assert str(persisted.id) == document_id
            assert persisted.original_filename == "scan.pdf"
            assert persisted.object_key == f"documents/{document_id}/scan.pdf"
            assert persisted.status == "uploaded"

        detail_response = client.get(f"/documents/{document_id}")

        assert detail_response.status_code == 200
        detail = detail_response.json()
        assert detail["id"] == document_id
        assert detail["original_filename"] == "scan.pdf"
        assert detail["status"] == "uploaded"
        assert detail["created_at"]
    finally:
        app.dependency_overrides.clear()
        engine.dispose()
