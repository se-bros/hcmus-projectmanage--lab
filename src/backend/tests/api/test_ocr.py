import uuid

from sqlalchemy import select

from app.models.document import Document
from app.models.ocr_job import OcrJob
from app.models.page import Page


def _document() -> Document:
    document_id = uuid.uuid4()
    return Document(
        id=document_id,
        original_filename="scan.png",
        object_key=f"documents/{document_id}/scan.png",
        content_type="image/png",
        status="ocr_failed",
    )


def test_get_failed_job_and_retry_creates_next_attempt(api_context) -> None:
    client, testing_session, _ = api_context
    with testing_session() as db:
        document = _document()
        failed_job = OcrJob(
            id=uuid.uuid4(),
            document_id=document.id,
            attempt=1,
            status="failed",
            error_message="tesseract timed out",
        )
        db.add_all([document, failed_job])
        db.commit()
        document_id = document.id

    status_response = client.get(f"/documents/{document_id}/ocr")
    assert status_response.status_code == 200
    assert status_response.json()["status"] == "failed"
    assert status_response.json()["error_message"] == "tesseract timed out"

    retry = client.post(f"/documents/{document_id}/ocr")
    assert retry.status_code == 202
    assert retry.json()["attempt"] == 2
    assert retry.json()["status"] == "pending"
    with testing_session() as db:
        jobs = list(
            db.scalars(
                select(OcrJob).where(OcrJob.document_id == document_id).order_by(OcrJob.attempt)
            )
        )
        assert [job.status for job in jobs] == ["failed", "pending"]
        assert db.get(Document, document_id).status == "ocr_pending"

    duplicate = client.post(f"/documents/{document_id}/ocr")
    assert duplicate.status_code == 409


def test_completed_job_cannot_be_restarted(api_context) -> None:
    client, testing_session, _ = api_context
    with testing_session() as db:
        document = _document()
        document.status = "ocr_completed"
        db.add(document)
        db.add(OcrJob(id=uuid.uuid4(), document_id=document.id, attempt=1, status="completed"))
        db.commit()
        document_id = document.id
    response = client.post(f"/documents/{document_id}/ocr")
    assert response.status_code == 409
    assert "completed" in response.json()["detail"]


def test_pages_are_ordered_and_preview_is_streamed(api_context) -> None:
    client, testing_session, storage = api_context
    with testing_session() as db:
        document = _document()
        document.status = "ocr_completed"
        db.add(document)
        db.flush()
        for number, text in [(2, "Second page"), (1, "First page")]:
            key = f"documents/{document.id}/pages/{number}.png"
            storage.objects[key] = f"png-{number}".encode()
            db.add(
                Page(
                    id=uuid.uuid4(),
                    document_id=document.id,
                    page_number=number,
                    text_content=text,
                    image_object_key=key,
                )
            )
        db.commit()
        document_id = document.id

    pages = client.get(f"/documents/{document_id}/pages")
    assert pages.status_code == 200
    assert [page["page_number"] for page in pages.json()] == [1, 2]
    assert pages.json()[0] == {
        "page_number": 1,
        "text_content": "First page",
        "has_image": True,
    }
    preview = client.get(f"/documents/{document_id}/pages/2/image")
    assert preview.status_code == 200
    assert preview.content == b"png-2"
    assert preview.headers["content-type"] == "image/png"
    assert client.get(f"/documents/{document_id}/pages/3/image").status_code == 404


def test_pages_are_empty_before_ocr_completes(api_context) -> None:
    client, testing_session, _ = api_context
    with testing_session() as db:
        document = _document()
        document.status = "ocr_processing"
        db.add(document)
        db.commit()
        document_id = document.id
    assert client.get(f"/documents/{document_id}/pages").json() == []


def test_dashboard_returns_latest_job_per_document(api_context) -> None:
    client, testing_session, _ = api_context
    with testing_session() as db:
        failed_document = _document()
        processing_document = _document()
        no_job_document = _document()
        db.add_all([failed_document, processing_document, no_job_document])
        db.flush()
        db.add_all(
            [
                OcrJob(
                    id=uuid.uuid4(),
                    document_id=failed_document.id,
                    attempt=1,
                    status="failed",
                    error_message="old error",
                ),
                OcrJob(
                    id=uuid.uuid4(),
                    document_id=failed_document.id,
                    attempt=2,
                    status="failed",
                    error_message="latest error",
                ),
                OcrJob(
                    id=uuid.uuid4(),
                    document_id=processing_document.id,
                    attempt=1,
                    status="processing",
                ),
            ]
        )
        db.commit()

    response = client.get("/ocr/jobs")
    assert response.status_code == 200
    items = {item["document_id"]: item for item in response.json()}
    assert len(items) == 3
    assert items[str(failed_document.id)]["attempt"] == 2
    assert items[str(failed_document.id)]["error_message"] == "latest error"
    assert items[str(processing_document.id)]["ocr_status"] == "processing"
    assert items[str(no_job_document.id)]["job_id"] is None
    assert client.get("/ocr/jobs?limit=0").status_code == 422
