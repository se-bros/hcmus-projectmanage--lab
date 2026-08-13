import uuid

PDF_BYTES = b"%PDF-1.4\nminimal tag test sample"


def _upload(client) -> tuple[str, dict[str, str]]:
    token = client.post("/auth/dev-token", json={"role": "editor"}).json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    response = client.post(
        "/documents",
        files={"file": ("scan.pdf", PDF_BYTES, "application/pdf")},
        headers=headers,
    )
    return response.json()["document_id"], headers


def test_add_tag_and_get_tags_ac1(api_context) -> None:
    client, _, _ = api_context
    doc_id, headers = _upload(client)

    # Initial tags should be empty
    get_res = client.get(f"/documents/{doc_id}/tags", headers=headers)
    assert get_res.status_code == 200
    assert get_res.json() == []

    # AC 1: Thêm tag cho document
    post_res = client.post(
        f"/documents/{doc_id}/tags",
        json={"name": "lich su"},
        headers=headers,
    )
    assert post_res.status_code == 200
    assert post_res.json() == ["lich su"]

    # GET /documents/{doc_id}/tags chứa tag đó
    get_res2 = client.get(f"/documents/{doc_id}/tags", headers=headers)
    assert get_res2.status_code == 200
    assert "lich su" in get_res2.json()


def test_delete_tag_ac2(api_context) -> None:
    client, _, _ = api_context
    doc_id, headers = _upload(client)

    client.post(f"/documents/{doc_id}/tags", json={"name": "toan hoc"}, headers=headers)
    client.post(f"/documents/{doc_id}/tags", json={"name": "vat ly"}, headers=headers)

    get_before = client.get(f"/documents/{doc_id}/tags", headers=headers)
    assert set(get_before.json()) == {"toan hoc", "vat ly"}

    # AC 2: Xóa tag → GET không còn tag đó trên document
    del_res = client.delete(f"/documents/{doc_id}/tags/toan hoc", headers=headers)
    assert del_res.status_code == 200
    assert del_res.json() == ["vat ly"]

    get_after = client.get(f"/documents/{doc_id}/tags", headers=headers)
    assert get_after.json() == ["vat ly"]


def test_tag_normalization_and_deduplication_ac3(api_context) -> None:
    client, _, _ = api_context
    doc_id, headers = _upload(client)

    # AC 3: Tag được normalize (lower + trim) trước khi lưu để tránh trùng lặp
    res1 = client.post(
        f"/documents/{doc_id}/tags",
        json={"name": "  PyThOn 3  "},
        headers=headers,
    )
    assert res1.status_code == 200
    assert res1.json() == ["python 3"]

    # Try adding same tag with different casing and whitespace
    res2 = client.post(
        f"/documents/{doc_id}/tags",
        json={"name": "PYTHON 3"},
        headers=headers,
    )
    assert res2.status_code == 200
    assert res2.json() == ["python 3"]


def test_empty_tag_rejected(api_context) -> None:
    client, _, _ = api_context
    doc_id, headers = _upload(client)

    res = client.post(
        f"/documents/{doc_id}/tags",
        json={"name": "   "},
        headers=headers,
    )
    assert res.status_code == 422


def test_tag_permissions(api_context, admin_headers) -> None:
    client, _, _ = api_context
    doc_id, _owner_headers = _upload(client)

    # Reader can get tags but cannot post or delete
    reader_token = client.post("/auth/dev-token", json={"role": "reader"}).json()["access_token"]
    reader_headers = {"Authorization": f"Bearer {reader_token}"}

    get_res = client.get(f"/documents/{doc_id}/tags", headers=reader_headers)
    assert get_res.status_code == 200

    post_res = client.post(
        f"/documents/{doc_id}/tags",
        json={"name": "science"},
        headers=reader_headers,
    )
    assert post_res.status_code == 403

    # Admin can add tag to any document
    admin_post = client.post(
        f"/documents/{doc_id}/tags",
        json={"name": "admin-tag"},
        headers=admin_headers,
    )
    assert admin_post.status_code == 200
    assert "admin-tag" in admin_post.json()


def test_tag_document_not_found(api_context, admin_headers) -> None:
    client, _, _ = api_context
    random_id = uuid.uuid4()

    res = client.get(f"/documents/{random_id}/tags", headers=admin_headers)
    assert res.status_code == 404

    res2 = client.post(
        f"/documents/{random_id}/tags",
        json={"name": "test"},
        headers=admin_headers,
    )
    assert res2.status_code == 404
