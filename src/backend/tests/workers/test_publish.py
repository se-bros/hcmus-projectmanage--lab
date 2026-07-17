import uuid
import zipfile
from pathlib import Path

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.db.base import Base
from app.models.document import Document
from app.models.page import Page
from app.models.publish_job import PublishJob
from app.workers import publish
from tests.fakes import InMemoryStorage


def _database():
    engine = create_engine(
        "sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool
    )
    Base.metadata.create_all(engine)
    return engine, sessionmaker(bind=engine, expire_on_commit=False)


def _seed_publish_job(session_factory) -> tuple[uuid.UUID, uuid.UUID]:
    with session_factory() as db:
        document_id = uuid.uuid4()
        document = Document(
            id=document_id,
            original_filename="book.pdf",
            object_key=f"documents/{document_id}/book.pdf",
            content_type="application/pdf",
            status="ocr_completed",
            title="Thư viện HCMUS",
            author="Nhóm LDMS",
        )
        db.add(document)
        db.flush()
        db.add_all(
            [
                Page(
                    id=uuid.uuid4(),
                    document_id=document_id,
                    page_number=2,
                    text_content="Nội dung trang hai.",
                ),
                Page(
                    id=uuid.uuid4(),
                    document_id=document_id,
                    page_number=1,
                    text_content="Nội dung trang một.",
                ),
            ]
        )
        job = PublishJob(id=uuid.uuid4(), document_id=document_id, attempt=1, status="pending")
        db.add(job)
        db.commit()
        return document_id, job.id


def _write_epub(path: Path, title: str, author: str, page_texts: list[str]) -> None:
    container = """<?xml version="1.0"?>
<container xmlns="urn:oasis:names:tc:opendocument:xmlns:container" version="1.0">
  <rootfiles><rootfile full-path="OEBPS/content.opf"
    media-type="application/oebps-package+xml"/></rootfiles>
</container>"""
    opf = f"""<?xml version="1.0" encoding="UTF-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="id">
  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
    <dc:identifier id="id">urn:uuid:{uuid.uuid4()}</dc:identifier>
    <dc:title>{title}</dc:title><dc:creator>{author}</dc:creator>
    <dc:language>vi</dc:language>
  </metadata>
  <manifest><item id="body" href="body.xhtml" media-type="application/xhtml+xml"/></manifest>
  <spine><itemref idref="body"/></spine>
</package>"""
    body = """<?xml version="1.0" encoding="UTF-8"?>
<html xmlns="http://www.w3.org/1999/xhtml"><body>{}</body></html>""".format(
        "".join(f"<section><p>{text}</p></section>" for text in page_texts)
    )
    with zipfile.ZipFile(path, "w") as archive:
        archive.writestr("mimetype", "application/epub+zip", compress_type=zipfile.ZIP_STORED)
        archive.writestr("META-INF/container.xml", container)
        archive.writestr("OEBPS/content.opf", opf)
        archive.writestr("OEBPS/body.xhtml", body)


def test_publish_worker_uploads_valid_epub_and_preserves_page_order(monkeypatch) -> None:
    engine, session_factory = _database()
    storage = InMemoryStorage()
    document_id, job_id = _seed_publish_job(session_factory)

    def fake_pandoc(source: Path, output: Path, title: str, author: str) -> None:
        _write_epub(
            output,
            title,
            author,
            ["Nội dung trang một.", "Nội dung trang hai."],
        )

    monkeypatch.setattr(publish, "_create_epub", fake_pandoc)
    publish.run_publish_job(job_id, session_factory, storage)

    with session_factory() as db:
        document = db.get(Document, document_id)
        job = db.get(PublishJob, job_id)
        assert job.status == "completed"
        assert document.status == "published"
        assert document.epub_object_key == f"documents/{document_id}/epub/{job_id}.epub"
        epub_bytes = storage.objects[document.epub_object_key]
        assert epub_bytes.startswith(b"PK")
    engine.dispose()


def test_publish_worker_failure_keeps_previous_epub(monkeypatch) -> None:
    engine, session_factory = _database()
    storage = InMemoryStorage()
    document_id, job_id = _seed_publish_job(session_factory)
    with session_factory() as db:
        db.get(Document, document_id).epub_object_key = "documents/old.epub"
        db.commit()

    def fail_pandoc(*args, **kwargs) -> None:
        raise RuntimeError("pandoc failed")

    monkeypatch.setattr(publish, "_create_epub", fail_pandoc)
    publish.run_publish_job(job_id, session_factory, storage)

    with session_factory() as db:
        document = db.get(Document, document_id)
        job = db.get(PublishJob, job_id)
        assert job.status == "failed"
        assert job.error_message == "pandoc failed"
        assert document.status == "publish_failed"
        assert document.epub_object_key == "documents/old.epub"
    engine.dispose()


def test_epub_validation_rejects_reversed_page_order(tmp_path: Path) -> None:
    epub_path = tmp_path / "reversed.epub"
    _write_epub(
        epub_path,
        "Thư viện HCMUS",
        "Nhóm LDMS",
        ["Nội dung trang hai.", "Nội dung trang một."],
    )
    pages = [
        Page(page_number=1, text_content="Nội dung trang một."),
        Page(page_number=2, text_content="Nội dung trang hai."),
    ]
    with pytest.raises(RuntimeError, match="page 2 in order"):
        publish.validate_epub(epub_path, "Thư viện HCMUS", "Nhóm LDMS", pages)
