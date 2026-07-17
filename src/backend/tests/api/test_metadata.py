import uuid

PDF_BYTES = b"%PDF-1.4\nminimal sample"


def _upload(client) -> tuple[str, dict[str, str]]:
    token = client.post("/auth/dev-token", json={"role": "editor"}).json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    response = client.post(
        "/documents",
        files={"file": ("scan.pdf", PDF_BYTES, "application/pdf")},
        headers=headers,
    )
    return response.json()["document_id"], headers


def test_metadata_is_trimmed_saved_and_returned_by_document_detail(api_context) -> None:
    client, _, _ = api_context
    document_id, headers = _upload(client)

    response = client.put(
        f"/documents/{document_id}/metadata",
        json={
            "title": "  A title  ",
            "author": "  An author ",
            "shelf_location": "  A-12 ",
            "category_id": None,
        },
    )

    assert response.status_code == 200
    assert response.json()["title"] == "A title"
    assert response.json()["author"] == "An author"
    assert response.json()["shelf_location"] == "A-12"
    assert response.json()["category_id"] is None
    assert (
        client.get(f"/documents/{document_id}", headers=headers).json()["shelf_location"] == "A-12"
    )


def test_optional_metadata_can_be_null_or_blank(api_context) -> None:
    client, _, _ = api_context
    document_id, _headers = _upload(client)

    response = client.put(
        f"/documents/{document_id}/metadata",
        json={"title": "Title", "author": "Author", "shelf_location": "   "},
    )

    assert response.status_code == 200
    assert response.json()["shelf_location"] is None
    assert response.json()["category_id"] is None


def test_required_metadata_reports_each_blank_field(api_context) -> None:
    client, _, _ = api_context
    document_id, _headers = _upload(client)

    response = client.put(
        f"/documents/{document_id}/metadata",
        json={"title": "   ", "author": "\t"},
    )

    assert response.status_code == 422
    fields = {error["loc"][-1] for error in response.json()["detail"]}
    assert fields == {"title", "author"}


def test_metadata_document_not_found(api_context) -> None:
    client, _, _ = api_context
    response = client.put(
        f"/documents/{uuid.uuid4()}/metadata",
        json={"title": "Title", "author": "Author"},
    )
    assert response.status_code == 404
    assert response.json() == {"detail": "Document not found."}
