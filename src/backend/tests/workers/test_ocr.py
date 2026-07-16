import uuid
from pathlib import Path

from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.db.base import Base
from app.models.document import Document
from app.models.ocr_job import OcrJob
from app.models.page import Page
from app.workers import ocr
from tests.fakes import InMemoryStorage


def _database():
    engine = create_engine(
        "sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool
    )
    Base.metadata.create_all(engine)
    return engine, sessionmaker(bind=engine, expire_on_commit=False)


def _seed_job(session_factory, storage: InMemoryStorage) -> tuple[uuid.UUID, uuid.UUID]:
    with session_factory() as db:
        document_id = uuid.uuid4()
        key = f"documents/{document_id}/scan.png"
        storage.objects[key] = b"source image"
        document = Document(
            id=document_id,
            original_filename="scan.png",
            object_key=key,
            content_type="image/png",
            status="ocr_pending",
        )
        job = OcrJob(id=uuid.uuid4(), document_id=document_id, attempt=1, status="pending")
        db.add_all([document, job])
        db.commit()
        return document_id, job.id


def test_worker_completes_and_replaces_pages_atomically(monkeypatch) -> None:
    engine, session_factory = _database()
    storage = InMemoryStorage()
    document_id, job_id = _seed_job(session_factory, storage)
    with session_factory() as db:
        db.add(
            Page(
                id=uuid.uuid4(),
                document_id=document_id,
                page_number=99,
                text_content="stale",
            )
        )
        db.commit()

    def fake_process(source_path: Path, content_type: str, workdir: Path):
        first = workdir / "first.png"
        second = workdir / "second.png"
        first.write_bytes(b"preview one")
        second.write_bytes(b"preview two")
        return [
            ocr.ProcessedPage(1, "Xin chào", first),
            ocr.ProcessedPage(2, "Library", second),
        ]

    monkeypatch.setattr(ocr, "_process_source", fake_process)
    ocr.run_ocr_job(job_id, session_factory, storage)

    with session_factory() as db:
        job = db.get(OcrJob, job_id)
        pages = list(db.scalars(select(Page).order_by(Page.page_number)))
        assert job.status == "completed"
        assert job.error_message is None
        assert job.document.status == "ocr_completed"
        assert [(page.page_number, page.text_content) for page in pages] == [
            (1, "Xin chào"),
            (2, "Library"),
        ]
        assert all(page.image_object_key for page in pages)
    assert storage.objects[f"documents/{document_id}/pages/1.png"] == b"preview one"
    engine.dispose()


def test_worker_failure_records_error_and_keeps_existing_pages(monkeypatch) -> None:
    engine, session_factory = _database()
    storage = InMemoryStorage()
    document_id, job_id = _seed_job(session_factory, storage)
    with session_factory() as db:
        db.add(
            Page(
                id=uuid.uuid4(),
                document_id=document_id,
                page_number=1,
                text_content="existing edit",
            )
        )
        db.commit()

    def fail_processing(*args, **kwargs):
        raise TimeoutError("tesseract timed out")

    monkeypatch.setattr(ocr, "_process_source", fail_processing)
    ocr.run_ocr_job(job_id, session_factory, storage)

    with session_factory() as db:
        job = db.get(OcrJob, job_id)
        pages = list(db.scalars(select(Page)))
        assert job.status == "failed"
        assert job.error_message == "tesseract timed out"
        assert job.document.status == "ocr_failed"
        assert [page.text_content for page in pages] == ["existing edit"]
    engine.dispose()


def test_restart_recovery_marks_active_jobs_failed() -> None:
    engine, session_factory = _database()
    storage = InMemoryStorage()
    _, first_job_id = _seed_job(session_factory, storage)
    with session_factory() as db:
        first = db.get(OcrJob, first_job_id)
        first.status = "processing"
        db.commit()

    assert ocr.recover_interrupted_ocr_jobs(session_factory) == 1
    with session_factory() as db:
        job = db.get(OcrJob, first_job_id)
        assert job.status == "failed"
        assert "restart" in job.error_message
        assert job.document.status == "ocr_failed"
    engine.dispose()
