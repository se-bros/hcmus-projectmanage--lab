# Phase 1 Data Model: Tìm kiếm toàn văn & Trải nghiệm đọc sách EPUB

## Entity mới: Bookmark

Bảng mới `bookmarks` — vị trí đọc dở của một user cho một document (US7 / FR-012, FR-013).

| Field | Type | Ràng buộc | Ghi chú |
|---|---|---|---|
| `id` | UUID | PK, `default=uuid.uuid4` | |
| `document_id` | UUID | FK → `documents.id`, `ondelete="CASCADE"`, index | Xoá document → xoá bookmark liên quan |
| `user_sub` | String(255) | index, not null | JWT `sub` claim — xem `research.md` mục 2. Không FK vì không có bảng `User`. |
| `location` | Text | not null | EPUB CFI string, opaque với backend — xem `research.md` mục 3 |
| `created_at` | DateTime(timezone=True) | `server_default=func.now()` | |
| `updated_at` | DateTime(timezone=True) | `server_default=func.now()`, `onupdate=func.now()` | |

**Unique constraint**: `(document_id, user_sub)` — mỗi user chỉ có 1 bookmark/document (upsert, không lưu lịch sử vị trí cũ) → thoả FR-013 "một user khác không nhận bookmark của user trước" bằng thiết kế (query luôn lọc theo `user_sub` của chính request).

**SQLAlchemy sketch** (`app/models/bookmark.py`):

```python
class Bookmark(Base):
    __tablename__ = "bookmarks"
    __table_args__ = (UniqueConstraint("document_id", "user_sub"),)

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    document_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("documents.id", ondelete="CASCADE"), index=True
    )
    user_sub: Mapped[str] = mapped_column(String(255), index=True)
    location: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )
```

Phải import vào `app/models/__init__.py` và đảm bảo `app/db/migrations/env.py` thấy được (đã import `from app import models  # noqa: F401` — tự động bao phủ model mới, không cần sửa `env.py`).

## Entity hiện có — dùng lại, không đổi schema DB

- **Document** (`app/models/document.py`): dùng các field có sẵn — `status` (phải `== "published"` để đọc được), `epub_object_key`, `title`, `author`, `is_public`. Không thêm cột mới.
- **Page** (`app/models/page.py`): dùng `text_content` làm nguồn full-text search nội dung OCR.

## Response DTOs mới (không phải bảng DB — `app/schemas/document.py`)

### ReaderContent (US1/US5 — `GET /documents/{id}/reader`)

| Field | Type | Ghi chú |
|---|---|---|
| `document_id` | UUID | |
| `title` | str | |
| `author` | str \| None | |
| `epub_url` | str | MinIO Signed URL, hết hạn sau `expires_in` giây |
| `expires_in` | int | Luôn `900` (15 phút, Constitution Principle IV) |

### BookmarkDetail / BookmarkUpdate (US7 — `GET`/`PUT /documents/{id}/bookmark`)

`BookmarkDetail`: `document_id: UUID`, `location: str`, `updated_at: datetime`.
`BookmarkUpdate` (request body của PUT): `location: str` (không rỗng).

### SearchResult (US3/US4 — sửa nhẹ, giữ nguyên tên field)

| Field | Type | Đổi so với bản fixture |
|---|---|---|
| `document_id` | **uuid.UUID** (trước là `str`) | Khớp kiểu thật của `Document.id` |
| `title` | str | không đổi |
| `snippet` | str | không đổi — nội dung sinh bởi `ts_headline` (Postgres) hoặc cắt thủ công (SQLite fallback), không đổi format trả về cho FE |

FE `SearchResult.document_id: string` trong `services/documents.ts`/TS không cần đổi — UUID vẫn serialize thành string qua JSON, tương thích ngược hoàn toàn.

## Validation rules tổng hợp (từ Functional Requirements)

- `GET /documents/{id}/reader`: 404 nếu document không tồn tại; lỗi rõ ràng (400/409-style qua `ValidationError`/`NotFoundError`) nếu `status != "published"` hoặc `epub_object_key is None`; 401 nếu private + không có token hợp lệ (dùng lại `ensure_readable`).
- `PUT /documents/{id}/bookmark`: bắt buộc đăng nhập (`get_current_user`, không phải optional); `location` không được rỗng.
- `GET /search?q=`: `q` rỗng/whitespace → trả `[]` (theo Assumption đã chốt ở spec, không phải lỗi 4xx).
