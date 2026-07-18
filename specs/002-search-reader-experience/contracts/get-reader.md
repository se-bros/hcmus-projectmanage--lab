# Contract: `GET /documents/{document_id}/reader`

**Router file**: `src/backend/app/api/reader.py` (sửa route cũ `/reader/{document_id}` → chuyển vào prefix `/documents`, khớp convention của `documents.py`/`ocr.py`)
**Owner**: Khoa Nguyễn — LDMS-008, LDMS-014.
**Auth**: optional user (`get_optional_user`) — cho phép guest đọc document `is_public=true`; bắt buộc token hợp lệ nếu `is_public=false` (dùng lại `ensure_readable`, xem `document_service.py`).

## Request

```
GET /documents/{document_id}/reader
Authorization: Bearer <token>   # optional nếu document is_public
```

| Path param | Type | Ghi chú |
|---|---|---|
| `document_id` | `uuid.UUID` | |

## Response 200 — `ReaderContent`

```json
{
  "document_id": "5b1f2e2a-...",
  "title": "Giáo trình Giải tích 1",
  "author": "Nguyễn Văn A",
  "epub_url": "http://minio:9000/ldms/documents/.../epub/....epub?X-Amz-Signature=...",
  "expires_in": 900
}
```

`epub_url` là MinIO Signed URL (`presigned_get_object`, `expires_seconds=900`) — FE (Epub.js) fetch trực tiếp từ URL này, **không** qua backend proxy (US1/FR-001, US5/FR-008 — Constitution Principle IV).

## Response lỗi

| Status | Khi nào | AppError |
|---|---|---|
| 401 | `is_public=false` và không có token hợp lệ | `UnauthorizedError` (dùng lại `ensure_readable`) |
| 404 | `document_id` không tồn tại | `NotFoundError` (US1 AC3) |
| 422 | Document tồn tại nhưng `status != "published"` hoặc thiếu `epub_object_key` | `ValidationError` — message rõ ràng kiểu "Tài liệu chưa được xuất bản." / "Không tìm thấy bản đọc EPUB." (US1 AC2) |

## Pydantic schema

```python
class ReaderContent(BaseModel):
    document_id: uuid.UUID
    title: str
    author: str | None
    epub_url: str
    expires_in: int
```

## Service function

```python
# app/services/reader_service.py
def get_reader_content(
    db: Session, document_id: uuid.UUID, user: AuthenticatedUser | None
) -> ReaderContent:
    document = ensure_readable(get_document(db, document_id), user)  # 401/404
    if document.status != "published":
        raise ValidationError("Tài liệu chưa được xuất bản.")
    if document.epub_object_key is None:
        raise ValidationError("Không tìm thấy bản đọc EPUB.")
    url = get_presigned_url(document.epub_object_key, expires_seconds=900)
    return ReaderContent(
        document_id=document.id, title=document.title or document.original_filename,
        author=document.author, epub_url=url, expires_in=900,
    )
```
