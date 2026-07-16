# Contract: `GET /reader/{document_id}`

**Router file**: `src/backend/app/api/reader.py` (thêm vào router đã có, chưa có prefix — route đầy đủ là `/reader/{document_id}`)
**Owner**: Khoa Nguyễn — chuẩn bị cho LDMS-008 (chỉ phần đọc text placeholder, chưa phải Epub.js/MinIO Signed URL thật).

## Request

```
GET /reader/{document_id}
```

| Path param | Type | Ghi chú |
|---|---|---|
| `document_id` | `str` | Khớp `Document.id` trong fixture (US2 AC1/AC2). |

## Response 200 — `DocumentContent`

```json
{
  "document_id": "doc-1",
  "text": "Chương 1. Giới hạn và liên tục...\n\n(nội dung fixture rút gọn)"
}
```

## Response 404 — không tìm thấy (US2 AC2)

```json
{
  "detail": "Document 'doc-999' not found"
}
```

Dùng `HTTPException(status_code=404, detail=...)` chuẩn FastAPI — chưa cần đi qua `AppError` hierarchy (`core/exceptions.py`) vì Principle II constitution miễn trừ cho endpoint scaffold/placeholder chưa pick chính thức; sẽ chuyển sang `AppError` khi LDMS-008 được pick đủ AC.

## Pydantic schema

```python
class DocumentContent(BaseModel):
    document_id: str
    text: str
```
