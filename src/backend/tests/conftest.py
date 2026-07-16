import os
from collections.abc import Generator

os.environ.setdefault("DATABASE_URL", "postgresql+psycopg://test:test@localhost:5432/test")
os.environ.setdefault("MINIO_ENDPOINT", "localhost:9000")
os.environ.setdefault("MINIO_ACCESS_KEY", "test")
os.environ.setdefault("MINIO_SECRET_KEY", "test")

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.pool import StaticPool

from app.api import documents, ocr, publish
from app.db.base import Base
from app.db.session import get_db
from app.main import app
from app.services import document_service
from tests.fakes import InMemoryStorage


@pytest.fixture
def api_context(monkeypatch):
    engine = create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    Base.metadata.create_all(engine)
    testing_session = sessionmaker(bind=engine, expire_on_commit=False)
    storage = InMemoryStorage()

    def override_get_db() -> Generator[Session, None, None]:
        with testing_session() as db:
            yield db

    def no_background_work(job_id) -> None:
        pass

    app.dependency_overrides[get_db] = override_get_db
    monkeypatch.setattr(document_service, "minio_client", storage)
    monkeypatch.setattr(documents, "run_ocr_job", no_background_work)
    monkeypatch.setattr(ocr, "run_ocr_job", no_background_work)
    monkeypatch.setattr(ocr, "minio_client", storage)
    monkeypatch.setattr(publish, "run_publish_job", no_background_work)

    try:
        yield TestClient(app), testing_session, storage
    finally:
        app.dependency_overrides.clear()
        engine.dispose()
