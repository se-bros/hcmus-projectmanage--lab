# Contract: `GET /documents`

**Router file**: `src/backend/app/api/documents.py` (thêm vào router đã có, prefix `/documents`)
**Owner**: Khoa Nguyễn (theo docstring hiện tại của file) — chuẩn bị cho LDMS-026.

## Request

Không có query param hay body ở bước placeholder này (phân trang/filter nâng cao ngoài phạm vi — xem spec FR ghi chú phạm vi).

```
GET /documents
```

## Response 200 — `list[DocumentSummary]`

```json
[
  {
    "id": "doc-1",
    "title": "Giáo trình Giải tích 1",
    "status": "published",
    "created_at": "2026-07-10"
  },
  {
    "id": "doc-2",
    "title": "Bản thảo chưa biên tập",
    "status": "draft",
    "created_at": "2026-07-15"
  }
]
```

Mảng rỗng `[]` là response hợp lệ (US1 AC3 — FE phải tự xử lý trạng thái rỗng, backend không cần trả lỗi).

## Pydantic schema (tham chiếu `data-model.md#document-fixture`)

```python
class DocumentSummary(BaseModel):
    id: str
    title: str
    status: Literal["draft", "published"]
    created_at: date
```

## Lỗi

Không có input để validate → không có response lỗi 4xx dự kiến ở endpoint này trong phạm vi placeholder.
