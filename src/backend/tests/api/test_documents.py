import uuid

import pytest
from sqlalchemy import func, select

from app.models.document import Document
from app.models.ocr_job import OcrJob

PDF_BYTES = b"%PDF-1.4\nminimal sample"


def test_upload_creates_document_and_pending_ocr_job(api_context) -> None:
    client, testing_session, storage = api_context
    response = client.post(
        "/documents",
        files={"file": ("scan.pdf", PDF_BYTES, "application/pdf")},
    )

    assert response.status_code == 201
    document_id = response.json()["document_id"]
    with testing_session() as db:
        document = db.get(Document, uuid.UUID(document_id))
        job = db.scalar(select(OcrJob))
        assert document is not None
        assert document.original_filename == "scan.pdf"
        assert document.content_type == "application/pdf"
        assert document.status == "ocr_pending"
        assert job is not None
        assert job.document_id == document.id
        assert job.attempt == 1
        assert job.status == "pending"
        assert storage.objects[document.object_key] == PDF_BYTES

    detail = client.get(f"/documents/{document_id}")
    assert detail.status_code == 200
    assert detail.json()["status"] == "ocr_pending"
    assert detail.json()["title"] is None


@pytest.mark.parametrize(
    ("filename", "body", "content_type"),
    [
        ("malware.exe", b"MZ", "application/octet-stream"),
        ("wrong.pdf", b"%PDF-1.4", "image/png"),
        ("fake.png", b"not a png", "image/png"),
        ("fake.jpg", b"not a jpeg", "image/jpeg"),
    ],
)
def test_invalid_upload_returns_422_without_side_effects(
    api_context, filename: str, body: bytes, content_type: str
) -> None:
    client, testing_session, storage = api_context
    response = client.post(
        "/documents",
        files={"file": (filename, body, content_type)},
    )

    assert response.status_code == 422
    with testing_session() as db:
        assert db.scalar(select(func.count()).select_from(Document)) == 0
        assert db.scalar(select(func.count()).select_from(OcrJob)) == 0
    assert storage.objects == {}


def test_source_read_back_and_not_found(api_context) -> None:
    client, _, _ = api_context
    upload = client.post("/documents", files={"file": ("scan.pdf", PDF_BYTES, "application/pdf")})
    document_id = upload.json()["document_id"]

    source = client.get(f"/documents/{document_id}/source")
    assert source.status_code == 200
    assert source.content == PDF_BYTES
    assert source.headers["content-type"] == "application/pdf"

    missing_id = uuid.uuid4()
    missing = client.get(f"/documents/{missing_id}")
    assert missing.status_code == 404
    assert missing.json() == {"detail": "Document not found."}
    assert client.get(f"/documents/{missing_id}/source").status_code == 404
