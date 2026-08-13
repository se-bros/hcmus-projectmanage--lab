import uuid

from sqlalchemy import func, select

from app.models.document import Document
from app.models.highlight import Highlight

CFI = "epubcfi(/6/14[chap03]!/4/2,/1:12,/3:28)"
CFI_OTHER = "epubcfi(/6/14[chap03]!/4/2,/1:20,/3:40)"
CFI_CROSS_CHAPTER = "epubcfi(/6,/14!/4/2/1:0,/16!/4/2/1:9)"


def _document(status: str = "published") -> Document:
    document_id = uuid.uuid4()
    return Document(
        id=document_id,
        original_filename="scan.pdf",
        object_key=f"documents/{document_id}/scan.pdf",
        content_type="application/pdf",
        status=status,
        title="A Book",
        author="An Author",
        epub_object_key=f"documents/{document_id}/book.epub",
    )


def _create_document(testing_session, status: str = "published") -> uuid.UUID:
    with testing_session() as db:
        document = _document(status=status)
        db.add(document)
        db.commit()
        return document.id


def _payload(cfi: str = CFI, text: str = "đoạn văn mẫu", note: str | None = None) -> dict:
    return {"cfi_range": cfi, "selected_text": text, "note": note}


def test_create_then_list_returns_highlight(api_context, reader_headers) -> None:
    """T1 — AC 1: tạo highlight rồi đọc lại thấy đúng vùng và text đã chọn."""
    client, testing_session, _ = api_context
    document_id = _create_document(testing_session)

    created = client.post(
        f"/documents/{document_id}/highlights", json=_payload(), headers=reader_headers
    )
    assert created.status_code == 201
    assert created.json()["cfi_range"] == CFI
    assert created.json()["selected_text"] == "đoạn văn mẫu"
    assert created.json()["note"] is None
    assert "user_sub" not in created.json()

    listed = client.get(f"/documents/{document_id}/highlights", headers=reader_headers)
    assert listed.status_code == 200
    assert [item["cfi_range"] for item in listed.json()] == [CFI]


def test_list_is_empty_before_any_highlight(api_context, reader_headers) -> None:
    """T2 — chưa có highlight nào là trạng thái bình thường, không phải 404."""
    client, testing_session, _ = api_context
    document_id = _create_document(testing_session)

    response = client.get(f"/documents/{document_id}/highlights", headers=reader_headers)
    assert response.status_code == 200
    assert response.json() == []


def test_overlapping_highlights_both_persist(api_context, reader_headers) -> None:
    """T13 — FR-004: vùng chồng lấn tạo bản ghi độc lập, KHÔNG gộp, KHÔNG chặn.

    Chống hồi quy cho quyết định "không UniqueConstraint" ở data-model.md: thêm
    ràng buộc unique cho giống bookmarks sẽ làm test này đỏ.
    """
    client, testing_session, _ = api_context
    document_id = _create_document(testing_session)

    first = client.post(
        f"/documents/{document_id}/highlights", json=_payload(), headers=reader_headers
    )
    second = client.post(
        f"/documents/{document_id}/highlights",
        json=_payload(cfi=CFI_OTHER),
        headers=reader_headers,
    )
    assert first.status_code == 201
    assert second.status_code == 201
    assert first.json()["id"] != second.json()["id"]

    listed = client.get(f"/documents/{document_id}/highlights", headers=reader_headers)
    assert len(listed.json()) == 2


def test_identical_range_creates_separate_record(api_context, reader_headers) -> None:
    """T13 (biến thể) — trùng khít cùng một vùng vẫn ra hai bản ghi."""
    client, testing_session, _ = api_context
    document_id = _create_document(testing_session)

    client.post(f"/documents/{document_id}/highlights", json=_payload(), headers=reader_headers)
    duplicate = client.post(
        f"/documents/{document_id}/highlights", json=_payload(), headers=reader_headers
    )
    assert duplicate.status_code == 201

    listed = client.get(f"/documents/{document_id}/highlights", headers=reader_headers)
    assert len(listed.json()) == 2


def test_deleting_document_removes_highlights(api_context, reader_headers) -> None:
    """T14 — FR-013: xóa tài liệu thì highlight bị dọn theo."""
    client, testing_session, _ = api_context
    document_id = _create_document(testing_session)
    client.post(f"/documents/{document_id}/highlights", json=_payload(), headers=reader_headers)

    with testing_session() as db:
        assert db.scalar(select(func.count()).select_from(Highlight)) == 1
        db.delete(db.get(Document, document_id))
        db.commit()
        assert db.scalar(select(func.count()).select_from(Highlight)) == 0


def test_other_user_cannot_see_highlights(
    api_context, reader_headers, second_reader_headers
) -> None:
    """T7 — FR-012: highlight của user A không lộ sang user B."""
    client, testing_session, _ = api_context
    document_id = _create_document(testing_session)
    client.post(f"/documents/{document_id}/highlights", json=_payload(), headers=reader_headers)

    listed = client.get(f"/documents/{document_id}/highlights", headers=second_reader_headers)
    assert listed.status_code == 200
    assert listed.json() == []


def test_anonymous_cannot_create_highlight(api_context) -> None:
    """T9 — FR-015: chưa đăng nhập thì không tạo được."""
    client, testing_session, _ = api_context
    document_id = _create_document(testing_session)

    response = client.post(f"/documents/{document_id}/highlights", json=_payload())
    assert response.status_code == 401

    with testing_session() as db:
        assert db.scalar(select(func.count()).select_from(Highlight)) == 0


def test_blank_selection_is_rejected(api_context, reader_headers) -> None:
    """T10 — FR-005: vùng chọn rỗng/toàn khoảng trắng không tạo bản ghi rác."""
    client, testing_session, _ = api_context
    document_id = _create_document(testing_session)

    response = client.post(
        f"/documents/{document_id}/highlights",
        json=_payload(text="   \n  "),
        headers=reader_headers,
    )
    assert response.status_code == 422

    with testing_session() as db:
        assert db.scalar(select(func.count()).select_from(Highlight)) == 0


def test_cross_chapter_range_is_rejected(api_context, reader_headers) -> None:
    """T11 — FR-005b: vùng chọn vắt qua ranh giới chương bị từ chối."""
    client, testing_session, _ = api_context
    document_id = _create_document(testing_session)

    response = client.post(
        f"/documents/{document_id}/highlights",
        json=_payload(cfi=CFI_CROSS_CHAPTER),
        headers=reader_headers,
    )
    assert response.status_code == 422
    assert "cùng một chương" in response.json()["detail"]

    with testing_session() as db:
        assert db.scalar(select(func.count()).select_from(Highlight)) == 0


def test_cannot_create_highlight_on_draft_document(api_context, reader_headers) -> None:
    """T15 — FR-001: chỉ đánh dấu được trên tài liệu đã xuất bản."""
    client, testing_session, _ = api_context
    document_id = _create_document(testing_session, status="draft")

    response = client.post(
        f"/documents/{document_id}/highlights", json=_payload(), headers=reader_headers
    )
    assert response.status_code == 422
    assert response.json()["detail"] == "Tài liệu chưa được xuất bản."

    with testing_session() as db:
        assert db.scalar(select(func.count()).select_from(Highlight)) == 0


def test_existing_highlights_readable_after_unpublish(api_context, reader_headers) -> None:
    """T16 — cặp đôi của T15: kiểm `published` CHỈ áp cho đường tạo.

    Gỡ xuất bản tài liệu không được khoá độc giả khỏi ghi chú của chính họ —
    đó đúng là kiểu mất dữ liệu mà FR-011 sinh ra để chặn. Nếu ai đó "sửa cho
    nhất quán" bằng cách áp `published` cho cả 4 endpoint, test này sẽ đỏ.
    (Nhánh xóa của T16 nằm ở test_delete_works_after_unpublish, thuộc US3.)
    """
    client, testing_session, _ = api_context
    document_id = _create_document(testing_session)
    client.post(f"/documents/{document_id}/highlights", json=_payload(), headers=reader_headers)

    with testing_session() as db:
        db.get(Document, document_id).status = "draft"
        db.commit()

    listed = client.get(f"/documents/{document_id}/highlights", headers=reader_headers)
    assert listed.status_code == 200
    assert len(listed.json()) == 1


def test_create_on_missing_document_returns_404(api_context, reader_headers) -> None:
    client, _, _ = api_context
    response = client.post(
        f"/documents/{uuid.uuid4()}/highlights", json=_payload(), headers=reader_headers
    )
    assert response.status_code == 404


def _create_highlight(client, document_id, headers, note: str | None = None) -> str:
    response = client.post(
        f"/documents/{document_id}/highlights", json=_payload(note=note), headers=headers
    )
    assert response.status_code == 201
    return response.json()["id"]


def test_note_survives_reload(api_context, reader_headers) -> None:
    """T3 — AC 2: ghi chú gắn lúc tạo, đọc lại còn nguyên văn."""
    client, testing_session, _ = api_context
    document_id = _create_document(testing_session)
    _create_highlight(client, document_id, reader_headers, note="Trích cho phần mở đầu")

    listed = client.get(f"/documents/{document_id}/highlights", headers=reader_headers)
    assert listed.json()[0]["note"] == "Trích cho phần mở đầu"


def test_note_can_be_edited(api_context, reader_headers) -> None:
    """T4 — FR-007: nội dung mới thay nội dung cũ."""
    client, testing_session, _ = api_context
    document_id = _create_document(testing_session)
    highlight_id = _create_highlight(client, document_id, reader_headers, note="bản nháp")

    updated = client.patch(
        f"/documents/{document_id}/highlights/{highlight_id}",
        json={"note": "bản đã sửa"},
        headers=reader_headers,
    )
    assert updated.status_code == 200
    assert updated.json()["note"] == "bản đã sửa"

    listed = client.get(f"/documents/{document_id}/highlights", headers=reader_headers)
    assert listed.json()[0]["note"] == "bản đã sửa"


def test_clearing_note_keeps_the_highlight(api_context, reader_headers) -> None:
    """T5 — FR-007: gỡ ghi chú KHÔNG được xóa luôn highlight."""
    client, testing_session, _ = api_context
    document_id = _create_document(testing_session)
    highlight_id = _create_highlight(client, document_id, reader_headers, note="sẽ gỡ")

    cleared = client.patch(
        f"/documents/{document_id}/highlights/{highlight_id}",
        json={"note": "   "},
        headers=reader_headers,
    )
    assert cleared.status_code == 200
    assert cleared.json()["note"] is None

    listed = client.get(f"/documents/{document_id}/highlights", headers=reader_headers)
    assert len(listed.json()) == 1
    assert listed.json()[0]["note"] is None


def test_note_longer_than_limit_is_rejected(api_context, reader_headers) -> None:
    """T12 — FR-009: vượt 2.000 ký tự thì báo lỗi kèm số ký tự, không cắt cụt."""
    client, testing_session, _ = api_context
    document_id = _create_document(testing_session)
    highlight_id = _create_highlight(client, document_id, reader_headers, note="ngắn")

    response = client.patch(
        f"/documents/{document_id}/highlights/{highlight_id}",
        json={"note": "a" * 2001},
        headers=reader_headers,
    )
    assert response.status_code == 422
    assert "2001/2000" in response.json()["detail"]

    listed = client.get(f"/documents/{document_id}/highlights", headers=reader_headers)
    assert listed.json()[0]["note"] == "ngắn"


def test_other_user_cannot_edit_note(api_context, reader_headers, second_reader_headers) -> None:
    """T8 (nhánh PATCH) — FR-012: 404 chứ không phải 403, để không xác nhận id có tồn tại."""
    client, testing_session, _ = api_context
    document_id = _create_document(testing_session)
    highlight_id = _create_highlight(client, document_id, reader_headers, note="của user A")

    response = client.patch(
        f"/documents/{document_id}/highlights/{highlight_id}",
        json={"note": "user B chen vào"},
        headers=second_reader_headers,
    )
    assert response.status_code == 404

    listed = client.get(f"/documents/{document_id}/highlights", headers=reader_headers)
    assert listed.json()[0]["note"] == "của user A"


def test_overlapping_highlights_keep_separate_notes(api_context, reader_headers) -> None:
    """US2 scenario 8 — hai highlight chồng lấn không lẫn ghi chú của nhau."""
    client, testing_session, _ = api_context
    document_id = _create_document(testing_session)
    outer = _create_highlight(client, document_id, reader_headers, note="ghi chú ngoài")
    inner = client.post(
        f"/documents/{document_id}/highlights",
        json=_payload(cfi=CFI_OTHER, note="ghi chú trong"),
        headers=reader_headers,
    ).json()["id"]

    listed = {
        item["id"]: item["note"]
        for item in client.get(
            f"/documents/{document_id}/highlights", headers=reader_headers
        ).json()
    }
    assert listed[outer] == "ghi chú ngoài"
    assert listed[inner] == "ghi chú trong"


def test_delete_removes_highlight_permanently(api_context, reader_headers) -> None:
    """T6 — AC 3: xóa rồi thì không quay lại sau khi tải lại."""
    client, testing_session, _ = api_context
    document_id = _create_document(testing_session)
    highlight_id = _create_highlight(client, document_id, reader_headers, note="sẽ bị xóa")

    deleted = client.delete(
        f"/documents/{document_id}/highlights/{highlight_id}", headers=reader_headers
    )
    assert deleted.status_code == 204

    listed = client.get(f"/documents/{document_id}/highlights", headers=reader_headers)
    assert listed.json() == []


def test_delete_leaves_overlapping_highlight_intact(api_context, reader_headers) -> None:
    """US3 scenario 7 — FR-004: xóa cái ngoài, cái chồng lấn bên trong còn nguyên."""
    client, testing_session, _ = api_context
    document_id = _create_document(testing_session)
    outer = _create_highlight(client, document_id, reader_headers, note="ngoài")
    inner = client.post(
        f"/documents/{document_id}/highlights",
        json=_payload(cfi=CFI_OTHER, note="trong"),
        headers=reader_headers,
    ).json()["id"]

    client.delete(f"/documents/{document_id}/highlights/{outer}", headers=reader_headers)

    listed = client.get(f"/documents/{document_id}/highlights", headers=reader_headers).json()
    assert [item["id"] for item in listed] == [inner]
    assert listed[0]["note"] == "trong"


def test_other_user_cannot_delete_highlight(
    api_context, reader_headers, second_reader_headers
) -> None:
    """T8 (nhánh DELETE) — FR-012."""
    client, testing_session, _ = api_context
    document_id = _create_document(testing_session)
    highlight_id = _create_highlight(client, document_id, reader_headers)

    response = client.delete(
        f"/documents/{document_id}/highlights/{highlight_id}", headers=second_reader_headers
    )
    assert response.status_code == 404

    listed = client.get(f"/documents/{document_id}/highlights", headers=reader_headers)
    assert len(listed.json()) == 1


def test_acting_on_already_deleted_highlight_returns_404(api_context, reader_headers) -> None:
    """T17 — edge case "đã bị xóa ở tab khác": bản ghi của CHÍNH user, đã biến mất."""
    client, testing_session, _ = api_context
    document_id = _create_document(testing_session)
    highlight_id = _create_highlight(client, document_id, reader_headers)
    client.delete(f"/documents/{document_id}/highlights/{highlight_id}", headers=reader_headers)

    second_delete = client.delete(
        f"/documents/{document_id}/highlights/{highlight_id}", headers=reader_headers
    )
    patch_after_delete = client.patch(
        f"/documents/{document_id}/highlights/{highlight_id}",
        json={"note": "gõ ở tab cũ"},
        headers=reader_headers,
    )
    assert second_delete.status_code == 404
    assert patch_after_delete.status_code == 404


def test_delete_works_after_unpublish(api_context, reader_headers) -> None:
    """T16 (nhánh xóa) — gỡ xuất bản không được khoá độc giả khỏi bản ghi của họ."""
    client, testing_session, _ = api_context
    document_id = _create_document(testing_session)
    highlight_id = _create_highlight(client, document_id, reader_headers)

    with testing_session() as db:
        db.get(Document, document_id).status = "draft"
        db.commit()

    response = client.delete(
        f"/documents/{document_id}/highlights/{highlight_id}", headers=reader_headers
    )
    assert response.status_code == 204
