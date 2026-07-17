import uuid

from sqlalchemy import func, select

from app.models.document import Document
from app.models.page import Page
from app.models.publish_job import PublishJob


def _document(title: str | None = "A Book", author: str | None = "An Author") -> Document:
    document_id = uuid.uuid4()
    return Document(
        id=document_id,
        original_filename="scan.pdf",
        object_key=f"documents/{document_id}/scan.pdf",
        content_type="application/pdf",
        status="ocr_completed",
        title=title,
        author=author,
    )


def test_publish_reports_all_missing_metadata_without_creating_job(
    api_context, editor_headers
) -> None:
    client, testing_session, _ = api_context
    with testing_session() as db:
        document = _document(title="  ", author=None)
        db.add(document)
        db.add(Page(id=uuid.uuid4(), document_id=document.id, page_number=1, text_content="text"))
        db.commit()
        document_id = document.id

    response = client.post(f"/documents/{document_id}/publish", headers=editor_headers)
    assert response.status_code == 422
    assert response.json()["detail"] == {
        "message": "Required metadata is missing.",
        "missing_fields": ["title", "author"],
    }
    with testing_session() as db:
        assert db.scalar(select(func.count()).select_from(PublishJob)) == 0
        assert db.get(Document, document_id).status == "ocr_completed"


def test_publish_rejects_missing_or_blank_pages(api_context, editor_headers) -> None:
    client, testing_session, _ = api_context
    with testing_session() as db:
        document = _document()
        db.add(document)
        db.commit()
        document_id = document.id
    no_pages = client.post(f"/documents/{document_id}/publish", headers=editor_headers)
    assert no_pages.status_code == 422
    assert no_pages.json()["detail"]["has_pages"] is False

    with testing_session() as db:
        db.add(Page(id=uuid.uuid4(), document_id=document_id, page_number=1, text_content="  "))
        db.commit()
    blank_page = client.post(f"/documents/{document_id}/publish", headers=editor_headers)
    assert blank_page.status_code == 422
    assert blank_page.json()["detail"]["missing_page_numbers"] == [1]


def test_publish_creates_pending_job_and_rejects_active_duplicate(
    api_context, editor_headers
) -> None:
    client, testing_session, _ = api_context
    with testing_session() as db:
        document = _document()
        db.add(document)
        db.add_all(
            [
                Page(
                    id=uuid.uuid4(),
                    document_id=document.id,
                    page_number=number,
                    text_content=text,
                )
                for number, text in [(2, "Second"), (1, "First")]
            ]
        )
        db.commit()
        document_id = document.id

    response = client.post(f"/documents/{document_id}/publish", headers=editor_headers)
    assert response.status_code == 202
    assert response.json()["attempt"] == 1
    assert response.json()["status"] == "pending"
    status_response = client.get(f"/documents/{document_id}/publish")
    assert status_response.json()["publish_job_id"] == response.json()["publish_job_id"]
    assert (
        client.post(f"/documents/{document_id}/publish", headers=editor_headers).status_code == 409
    )


def test_publish_rejected_for_reader_role(api_context) -> None:
    client, testing_session, _ = api_context
    with testing_session() as db:
        document = _document()
        db.add(document)
        db.commit()
        document_id = document.id
    token = client.post("/auth/dev-token", json={"role": "reader"}).json()["access_token"]

    response = client.post(
        f"/documents/{document_id}/publish", headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 403


def test_publish_rejected_without_token(api_context) -> None:
    client, testing_session, _ = api_context
    with testing_session() as db:
        document = _document()
        db.add(document)
        db.commit()
        document_id = document.id

    assert client.post(f"/documents/{document_id}/publish").status_code == 401
