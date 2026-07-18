# Contract: `GET` / `PUT /documents/{document_id}/bookmark`

**Router file**: `src/backend/app/api/reader.py` (cùng file với reader — cùng module M6, LDMS-020)
**Owner**: Khoa Nguyễn — LDMS-020.
**Auth**: **bắt buộc** đăng nhập (`get_current_user`, không optional) — US7 chỉ áp dụng cho user đã login.

## GET — đọc bookmark hiện có

```
GET /documents/{document_id}/bookmark
Authorization: Bearer <token>   # bắt buộc
```

### Response 200 — `BookmarkDetail`

```json
{
  "document_id": "5b1f2e2a-...",
  "location": "epubcfi(/6/14!/4/2/16/1:0)",
  "updated_at": "2026-07-17T10:00:00Z"
}
```

### Response 404 — chưa có bookmark nào cho `(document_id, user_sub)` này

FE coi 404 là "chưa có vị trí đã lưu" — không hiển thị lỗi, chỉ đơn giản mở sách từ đầu (không phải error state).

## PUT — lưu/ghi đè bookmark (upsert)

```
PUT /documents/{document_id}/bookmark
Authorization: Bearer <token>   # bắt buộc
Content-Type: application/json

{"location": "epubcfi(/6/14!/4/2/18/1:0)"}
```

### Response 200 — `BookmarkDetail` (sau khi lưu)

Cùng shape với GET. Upsert theo unique `(document_id, user_sub)` — gọi PUT nhiều lần chỉ ghi đè, không tạo bản ghi mới (US7 AC1/AC2).

### Response lỗi

| Status | Khi nào |
|---|---|
| 401 | Không có token / token không hợp lệ |
| 404 | `document_id` không tồn tại |
| 422 | `location` rỗng |

## Pydantic schema

```python
class BookmarkDetail(BaseModel):
    document_id: uuid.UUID
    location: str
    updated_at: datetime

class BookmarkUpdate(BaseModel):
    location: str

    @field_validator("location")
    @classmethod
    def required_text(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("must not be empty")
        return value
```

## Service function (upsert theo unique constraint)

```python
# app/services/bookmark_service.py
def get_bookmark(db: Session, document_id: uuid.UUID, user_sub: str) -> Bookmark:
    bookmark = db.scalar(
        select(Bookmark).where(Bookmark.document_id == document_id, Bookmark.user_sub == user_sub)
    )
    if bookmark is None:
        raise NotFoundError("No bookmark saved yet.")
    return bookmark

def save_bookmark(db: Session, document_id: uuid.UUID, user_sub: str, location: str) -> Bookmark:
    get_document(db, document_id)  # 404 nếu document không tồn tại
    bookmark = db.scalar(
        select(Bookmark).where(Bookmark.document_id == document_id, Bookmark.user_sub == user_sub)
    )
    if bookmark is None:
        bookmark = Bookmark(document_id=document_id, user_sub=user_sub, location=location)
        db.add(bookmark)
    else:
        bookmark.location = location
    db.commit()
    db.refresh(bookmark)
    return bookmark
```

**Bảo vệ FR-013** (không lẫn bookmark giữa các user): mọi truy vấn đều lọc theo `user_sub` lấy từ JWT của chính request (`get_current_user`), không nhận `user_sub` từ client — user A không thể đọc/ghi bookmark của user B dù biết `document_id`.
