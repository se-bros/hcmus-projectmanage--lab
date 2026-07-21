import uuid

import jwt as pyjwt
import pytest
from sqlalchemy import func, select

from app.core.config import settings
from app.models.document import Document
from app.models.ocr_job import OcrJob

PDF_BYTES = b"%PDF-1.4\nminimal sample"


def test_upload_creates_document_and_pending_ocr_job(api_context, editor_headers) -> None:
    client, testing_session, storage = api_context
    response = client.post(
        "/documents",
        files={"file": ("scan.pdf", PDF_BYTES, "application/pdf")},
        headers=editor_headers,
    )

    assert response.status_code == 201
    document_id = response.json()["document_id"]
    uploader_sub = pyjwt.decode(
        editor_headers["Authorization"].split(" ", 1)[1],
        settings.jwt_secret,
        algorithms=[settings.jwt_algorithm],
    )["sub"]
    with testing_session() as db:
        document = db.get(Document, uuid.UUID(document_id))
        job = db.scalar(select(OcrJob))
        assert document is not None
        assert document.original_filename == "scan.pdf"
        assert document.content_type == "application/pdf"
        assert document.status == "ocr_pending"
        assert document.is_public is False
        assert str(document.owner_id) == uploader_sub
        assert job is not None
        assert job.document_id == document.id
        assert job.attempt == 1
        assert job.status == "pending"
        assert storage.objects[document.object_key] == PDF_BYTES

    detail = client.get(f"/documents/{document_id}", headers=editor_headers)
    assert detail.status_code == 200
    assert detail.json()["status"] == "ocr_pending"
    assert detail.json()["content_type"] == "application/pdf"
    assert detail.json()["title"] is None
    assert detail.json()["is_public"] is False


def test_upload_rejected_without_token(api_context) -> None:
    client, _, _ = api_context
    response = client.post("/documents", files={"file": ("scan.pdf", PDF_BYTES, "application/pdf")})
    assert response.status_code == 401


def test_upload_rejected_for_reader_role(api_context) -> None:
    client, _, _ = api_context
    token = client.post("/auth/dev-token", json={"role": "reader"}).json()["access_token"]
    response = client.post(
        "/documents",
        files={"file": ("scan.pdf", PDF_BYTES, "application/pdf")},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 403


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
    api_context, editor_headers, filename: str, body: bytes, content_type: str
) -> None:
    client, testing_session, storage = api_context
    response = client.post(
        "/documents",
        files={"file": (filename, body, content_type)},
        headers=editor_headers,
    )

    assert response.status_code == 422
    with testing_session() as db:
        assert db.scalar(select(func.count()).select_from(Document)) == 0
        assert db.scalar(select(func.count()).select_from(OcrJob)) == 0
    assert storage.objects == {}


def test_source_read_back_and_not_found(api_context, editor_headers) -> None:
    client, _, _ = api_context
    upload = client.post(
        "/documents",
        files={"file": ("scan.pdf", PDF_BYTES, "application/pdf")},
        headers=editor_headers,
    )
    document_id = upload.json()["document_id"]

    source = client.get(f"/documents/{document_id}/source", headers=editor_headers)
    assert source.status_code == 200
    assert source.content == PDF_BYTES
    assert source.headers["content-type"] == "application/pdf"

    missing_id = uuid.uuid4()
    missing = client.get(f"/documents/{missing_id}")
    assert missing.status_code == 404
    assert missing.json() == {"detail": "Document not found."}
    assert client.get(f"/documents/{missing_id}/source").status_code == 404


def test_private_document_hidden_from_guest(api_context, editor_headers) -> None:
    client, _, _ = api_context
    upload = client.post(
        "/documents",
        files={"file": ("scan.pdf", PDF_BYTES, "application/pdf")},
        headers=editor_headers,
    )
    document_id = upload.json()["document_id"]

    guest_detail = client.get(f"/documents/{document_id}")
    assert guest_detail.status_code == 401
    guest_source = client.get(f"/documents/{document_id}/source")
    assert guest_source.status_code == 401

    reader_token = client.post("/auth/dev-token", json={"role": "reader"}).json()["access_token"]
    reader_headers = {"Authorization": f"Bearer {reader_token}"}
    reader_detail = client.get(f"/documents/{document_id}", headers=reader_headers)
    assert reader_detail.status_code == 200


def test_public_document_readable_by_guest(api_context, editor_headers) -> None:
    client, testing_session, _ = api_context
    upload = client.post(
        "/documents",
        files={"file": ("scan.pdf", PDF_BYTES, "application/pdf")},
        headers=editor_headers,
    )
    document_id = upload.json()["document_id"]
    with testing_session() as db:
        document = db.get(Document, uuid.UUID(document_id))
        document.is_public = True
        db.commit()

    guest_detail = client.get(f"/documents/{document_id}")
    assert guest_detail.status_code == 200
    assert guest_detail.json()["is_public"] is True

    guest_source = client.get(f"/documents/{document_id}/source")
    assert guest_source.status_code == 200
    assert guest_source.content == PDF_BYTES
