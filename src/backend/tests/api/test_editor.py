import uuid

import jwt as pyjwt

from app.core.config import settings
from app.models.document import Document
from app.models.page import Page


def _document_with_page(
    testing_session, owner_id: uuid.UUID | None = None
) -> tuple[uuid.UUID, int]:
    document_id = uuid.uuid4()
    with testing_session() as db:
        db.add(
            Document(
                id=document_id,
                original_filename="scan.pdf",
                object_key=f"documents/{document_id}/scan.pdf",
                content_type="application/pdf",
                status="ocr_completed",
                owner_id=owner_id,
            )
        )
        db.add(
            Page(
                id=uuid.uuid4(),
                document_id=document_id,
                page_number=1,
                text_content="Original OCR text",
                image_object_key="previews/page-1.png",
            )
        )
        db.commit()
    return document_id, 1


def test_get_and_update_page_text_persists(api_context, admin_headers) -> None:
    client, testing_session, _ = api_context
    document_id, page_number = _document_with_page(testing_session)

    detail = client.get(f"/documents/{document_id}/pages/{page_number}")
    assert detail.status_code == 200
    assert detail.json() == {
        "page_number": 1,
        "text_content": "Original OCR text",
        "has_image": True,
    }

    updated = client.put(
        f"/documents/{document_id}/pages/{page_number}",
        json={"text_content": "Corrected text"},
        headers=admin_headers,
    )
    assert updated.status_code == 200
    assert updated.json()["text_content"] == "Corrected text"
    assert client.get(f"/documents/{document_id}/pages/1").json()["text_content"] == (
        "Corrected text"
    )


def test_page_update_allows_empty_text(api_context, admin_headers) -> None:
    client, testing_session, _ = api_context
    document_id, page_number = _document_with_page(testing_session)
    response = client.put(
        f"/documents/{document_id}/pages/{page_number}",
        json={"text_content": ""},
        headers=admin_headers,
    )
    assert response.status_code == 200
    assert response.json()["text_content"] == ""


def test_page_update_rejected_for_reader_role(api_context) -> None:
    client, testing_session, _ = api_context
    document_id, page_number = _document_with_page(testing_session)
    token = client.post("/auth/dev-token", json={"role": "reader"}).json()["access_token"]
    response = client.put(
        f"/documents/{document_id}/pages/{page_number}",
        json={"text_content": "text"},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 403


def test_page_update_rejected_for_editor_who_does_not_own_document(
    api_context, editor_headers
) -> None:
    client, testing_session, _ = api_context
    document_id, page_number = _document_with_page(testing_session)
    response = client.put(
        f"/documents/{document_id}/pages/{page_number}",
        json={"text_content": "text"},
        headers=editor_headers,
    )
    assert response.status_code == 403


def test_page_update_allowed_for_editor_who_owns_document(api_context, editor_headers) -> None:
    client, testing_session, _ = api_context
    owner_sub = pyjwt.decode(
        editor_headers["Authorization"].split(" ", 1)[1],
        settings.jwt_secret,
        algorithms=[settings.jwt_algorithm],
    )["sub"]
    document_id, page_number = _document_with_page(testing_session, owner_id=uuid.UUID(owner_sub))

    response = client.put(
        f"/documents/{document_id}/pages/{page_number}",
        json={"text_content": "Owner edit"},
        headers=editor_headers,
    )
    assert response.status_code == 200
    assert response.json()["text_content"] == "Owner edit"


def test_missing_document_or_page_returns_clear_404(api_context, admin_headers) -> None:
    client, testing_session, _ = api_context
    document_id, _ = _document_with_page(testing_session)

    missing_page = client.get(f"/documents/{document_id}/pages/99")
    assert missing_page.status_code == 404
    assert missing_page.json() == {"detail": "Page not found."}
    assert (
        client.put(
            f"/documents/{document_id}/pages/99",
            json={"text_content": "text"},
            headers=admin_headers,
        ).status_code
        == 404
    )

    missing_document = client.get(f"/documents/{uuid.uuid4()}/pages/1")
    assert missing_document.status_code == 404
    assert missing_document.json() == {"detail": "Document not found."}
