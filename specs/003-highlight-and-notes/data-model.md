# Phase 1 — Data Model: Highlight và ghi chú (LDMS-021)

Một bảng mới. Không sửa bảng nào đang có.

---

## Bảng `highlights`

Model: `src/backend/app/models/highlight.py` · bám theo đúng khuôn `models/bookmark.py`.

| Cột | Kiểu | Ràng buộc | Nguồn |
| :--- | :--- | :--- | :--- |
| `id` | `Uuid` | PK, mặc định `uuid.uuid4` | — |
| `document_id` | `Uuid` | FK → `documents.id`, `ondelete="CASCADE"`, có index | FR-002, FR-013 |
| `user_sub` | `String(255)` | NOT NULL, có index | FR-002, FR-012 |
| `cfi_range` | `Text` | NOT NULL | FR-002 (R1) |
| `selected_text` | `Text` | NOT NULL | FR-003 |
| `note` | `Text` | **NULL được** | FR-007 |
| `created_at` | `DateTime(timezone=True)` | `server_default=now()` | — |
| `updated_at` | `DateTime(timezone=True)` | `server_default=now()`, `onupdate=now()` | — |

### Index

```python
__table_args__ = (Index("ix_highlights_document_user", "document_id", "user_sub"),)
```

Index tổ hợp `(document_id, user_sub)` phục vụ truy vấn nóng duy nhất của feature: "lấy mọi highlight của user X trên document Y" — chạy mỗi lần mở Reader, là đường ảnh hưởng trực tiếp tới SC-006.

### KHÔNG có unique constraint

Khác hẳn `bookmarks` (vốn có `UniqueConstraint("document_id", "user_sub")` vì mỗi user chỉ có một vị trí đọc dở), bảng này **cố ý không** ràng buộc unique:

- Một user có **nhiều** highlight trên cùng một document (FR-006).
- Hai highlight được phép **trùng vùng hoặc chồng lấn** (FR-004) — kể cả trùng khít `cfi_range`.

Đây là điểm dễ bị "sửa nhầm cho giống bookmark" khi review; ràng buộc unique ở đây sẽ phá vỡ FR-004.

---

## Quy tắc kiểm tra dữ liệu

Đặt ở tầng schema Pydantic (`schemas/highlight.py`), ném `ValidationError` (422) kèm thông báo tiếng Việt — theo tiền lệ `BookmarkUpdate.required_text`.

| # | Quy tắc | Áp dụng cho | FR |
| :--- | :--- | :--- | :--- |
| V1 | `selected_text` sau khi `.strip()` không được rỗng | tạo | FR-005 |
| V2 | `selected_text` ≤ **5.000** ký tự | tạo | Nguyên tắc IV (xem dưới) |
| V3 | `cfi_range` không rỗng và bắt đầu bằng `epubcfi(` | tạo | R1 |
| V4 | `cfi_range` phải nằm trong một chương: phần chung trước dấu `,` đầu tiên phải chứa `!` | tạo | FR-005b |
| V5 | `note` ≤ **2.000** ký tự, báo lỗi kèm số ký tự hiện tại | tạo, sửa ghi chú | FR-009 |
| V6 | `note` rỗng/toàn khoảng trắng → chuẩn hoá thành `NULL` (gỡ ghi chú, giữ highlight) | sửa ghi chú | FR-007 |

**Về V2** — giới hạn 5.000 ký tự cho `selected_text` là biện pháp thuộc Nguyên tắc IV đã nêu ở Constitution Check: cột này chứa nội dung sách có bản quyền nằm ngoài đường Signed URL, nên phải chặn khả năng dùng API highlight để dựng dần một bản sao cuốn sách trong DB. 5.000 ký tự tương đương vài trang — thừa sức cho mọi thao tác đánh dấu thật, nhưng không đủ để mirror sách.

---

## Quan hệ

```
documents (1) ──< (N) highlights
                      │
                      └── note: cột nullable trên chính bản ghi, KHÔNG phải bảng riêng
```

**Ghi chú không tách bảng.** Spec đã chốt mỗi highlight có nhiều nhất một ghi chú (Assumptions), nên `note` là một cột nullable. Hệ quả trực tiếp: xóa highlight thì ghi chú biến mất theo trong cùng một thao tác, thoả US3 scenario 3 ("không để lại bản ghi mồ côi") mà không cần cascade thứ hai.

**Xóa document → xóa highlight** qua `ondelete="CASCADE"` ở tầng DB (FR-013), cùng cách `bookmarks` đang làm.

**Không có FK sang bảng `users`.** `user_sub` là một `String` giữ giá trị `sub` trong JWT, đúng như `bookmarks.user_sub`. Bám theo tiền lệ để M6 nhất quán; đổi sang FK là việc phải làm đồng loạt cho cả bookmark lẫn highlight ở một PR riêng.

---

## Mapping sang trạng thái ở client

Bảng này **không** có cột nào mô tả việc highlight còn dựng lại được hay không — theo quyết định R4. Client tự phân loại lúc render:

| Nhóm ở UI | Cách xác định | Hiển thị |
| :--- | :--- | :--- |
| Dựng được | `rendition.annotations.add(...)` thành công | Tô trên trang sách + hiện trong sidebar |
| Không định vị được | `book.spine.get(cfi_range)` trả `null`, hoặc `annotations.add` ném lỗi | Chỉ hiện ở nhóm riêng trong sidebar, dùng `selected_text` (FR-011, FR-011a) |

Cùng một bản ghi có thể rơi vào nhóm khác nhau ở hai thời điểm nếu document được xuất bản lại — đó chính là lý do trạng thái này không được lưu xuống DB.

---

## Migration

Hai file, theo quyết định R5 (đã xác nhận bằng `uv run alembic heads`: tồn tại hai head `20260717_0007` và `20260721_0008`).

**`20260812_0009_merge_heads.py`** — gộp hai head, `upgrade()`/`downgrade()` để trống:

```python
revision: str = "20260812_0009"
down_revision: tuple[str, str] = ("20260717_0007", "20260721_0008")
```

**`20260812_0010_highlights.py`** — tạo bảng:

```python
revision: str = "20260812_0010"
down_revision: str | None = "20260812_0009"
```

`upgrade()` tạo bảng `highlights` với đủ cột ở trên, `ForeignKeyConstraint(["document_id"], ["documents.id"], ondelete="CASCADE")`, index `ix_highlights_document_id`, `ix_highlights_user_sub`, `ix_highlights_document_user`. `downgrade()` drop index rồi drop bảng — đối xứng với `20260717_0007_bookmarks.py`.

**Bắt buộc**: thêm `from app.models.highlight import Highlight` vào `app/models/__init__.py` và vào `__all__`. `app/db/migrations/env.py` import `from app import models`, nên model không được export ở đó sẽ vô hình với `--autogenerate` (đúng quy định trong mục Development Workflow của constitution).
