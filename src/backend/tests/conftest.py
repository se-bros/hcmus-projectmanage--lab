import os
from collections.abc import Generator

os.environ.setdefault("DATABASE_URL", "postgresql+psycopg://test:test@localhost:5432/test")
os.environ.setdefault("MINIO_ENDPOINT", "localhost:9000")
os.environ.setdefault("MINIO_ACCESS_KEY", "test")
os.environ.setdefault("MINIO_SECRET_KEY", "test")
os.environ.setdefault("JWT_SECRET", "test-secret-do-not-use-in-prod-min-32-bytes")

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, event
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

    @event.listens_for(engine, "connect")
    def enforce_foreign_keys(dbapi_connection, connection_record) -> None:
        """SQLite bỏ qua ON DELETE CASCADE trừ khi bật pragma này, nên nếu không
        có nó thì ràng buộc FK trong test lỏng hơn PostgreSQL thật."""
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON")
        cursor.close()

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


@pytest.fixture
def editor_headers(api_context) -> dict[str, str]:
    client, _, _ = api_context
    token = client.post("/auth/dev-token", json={"role": "editor"}).json()["access_token"]
    return {"Authorization": f"Bearer {token}"}


@pytest.fixture
def admin_headers(api_context) -> dict[str, str]:
    client, _, _ = api_context
    token = client.post("/auth/dev-token", json={"role": "admin"}).json()["access_token"]
    return {"Authorization": f"Bearer {token}"}


@pytest.fixture
def reader_headers(api_context) -> dict[str, str]:
    client, _, _ = api_context
    token = client.post("/auth/dev-token", json={"role": "reader"}).json()["access_token"]
    return {"Authorization": f"Bearer {token}"}


@pytest.fixture
def second_reader_headers(api_context) -> dict[str, str]:
    """User thứ hai — `/auth/dev-token` sinh `sub` ngẫu nhiên mỗi lần gọi nên
    fixture này tự nhiên là một user khác `reader_headers`."""
    client, _, _ = api_context
    token = client.post("/auth/dev-token", json={"role": "reader"}).json()["access_token"]
    return {"Authorization": f"Bearer {token}"}
