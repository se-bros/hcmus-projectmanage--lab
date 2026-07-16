import uuid

PDF_BYTES = b"%PDF-1.4\nminimal sample"


def _create(client, name: str, parent_id: str | None = None):
    return client.post("/categories", json={"name": name, "parent_id": parent_id})


def _upload(client) -> tuple[str, dict[str, str]]:
    token = client.post("/auth/dev-token", json={"role": "editor"}).json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    document_id = client.post(
        "/documents",
        files={"file": ("scan.pdf", PDF_BYTES, "application/pdf")},
        headers=headers,
    ).json()["document_id"]
    return document_id, headers


def test_create_parent_child_and_read_two_level_tree(api_context) -> None:
    client, _, _ = api_context
    parent = _create(client, "  Science  ")
    assert parent.status_code == 201
    assert parent.json()["name"] == "Science"

    child = _create(client, " Physics ", parent.json()["id"])
    assert child.status_code == 201
    assert child.json()["parent_id"] == parent.json()["id"]

    tree = client.get("/categories")
    assert tree.status_code == 200
    assert tree.json()[0]["name"] == "Science"
    assert [(item["name"], item["parent_id"]) for item in tree.json()[0]["children"]] == [
        ("Physics", parent.json()["id"])
    ]


def test_category_name_parent_and_depth_validation(api_context) -> None:
    client, _, _ = api_context
    blank = _create(client, "   ")
    assert blank.status_code == 422
    assert blank.json()["detail"][0]["loc"][-1] == "name"

    missing = _create(client, "Child", str(uuid.uuid4()))
    assert missing.status_code == 404
    assert missing.json() == {"detail": "Parent category not found."}

    root = _create(client, "Root").json()
    child = _create(client, "Child", root["id"]).json()
    too_deep = _create(client, "Grandchild", child["id"])
    assert too_deep.status_code == 422
    assert too_deep.json() == {"detail": "Categories are limited to two levels."}


def test_rename_and_delete_category(api_context) -> None:
    client, _, _ = api_context
    category = _create(client, "Old").json()

    renamed = client.patch(f"/categories/{category['id']}", json={"name": "  New  "})
    assert renamed.status_code == 200
    assert renamed.json()["name"] == "New"
    assert client.delete(f"/categories/{category['id']}").status_code == 204
    assert client.get("/categories").json() == []

    missing_id = uuid.uuid4()
    assert client.patch(f"/categories/{missing_id}", json={"name": "New"}).status_code == 404
    assert client.delete(f"/categories/{missing_id}").status_code == 404


def test_delete_rejects_categories_with_children_or_documents(api_context) -> None:
    client, _, _ = api_context
    parent = _create(client, "Parent").json()
    child = _create(client, "Child", parent["id"]).json()

    has_children = client.delete(f"/categories/{parent['id']}")
    assert has_children.status_code == 409
    assert "children" in has_children.json()["detail"]

    document_id, headers = _upload(client)
    assigned = client.put(
        f"/documents/{document_id}/metadata",
        json={"title": "Title", "author": "Author", "category_id": child["id"]},
    )
    assert assigned.status_code == 200
    assert assigned.json()["category_id"] == child["id"]
    assert (
        client.get(f"/documents/{document_id}", headers=headers).json()["category_id"]
        == child["id"]
    )

    in_use = client.delete(f"/categories/{child['id']}")
    assert in_use.status_code == 409
    assert "documents" in in_use.json()["detail"]


def test_assigning_unknown_category_returns_clear_404(api_context) -> None:
    client, _, _ = api_context
    document_id, _headers = _upload(client)
    response = client.put(
        f"/documents/{document_id}/metadata",
        json={"title": "Title", "author": "Author", "category_id": str(uuid.uuid4())},
    )
    assert response.status_code == 404
    assert response.json() == {"detail": "Category not found."}
