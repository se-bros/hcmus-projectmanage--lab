# Contract: `GET /search`

**Router file**: `src/backend/app/api/search.py` (thêm vào router đã có, prefix `/search`)
**Owner**: Khoa Nguyễn — chuẩn bị cho LDMS-015/016 (chỉ phần khung Search placeholder, chưa phải PostgreSQL FTS thật).

## Request

```
GET /search?q={keyword}
```

| Query param | Type | Bắt buộc | Ghi chú |
|---|---|---|---|
| `q` | `str` | có | Từ khóa tìm kiếm. Rỗng/whitespace-only → xem quy tắc dưới (US3 AC3). |

## Quy tắc xử lý `q` rỗng (US3 AC3)

`q` rỗng hoặc chỉ khoảng trắng → trả về mảng rỗng `[]` với HTTP 200 (nhất quán, không phải lỗi) — khớp với convention đã ghi trong `docs/07-product-backlog.md` LDMS-015 AC3 ("trả lỗi hoặc mảng rỗng, convention nhất quán"); chọn mảng rỗng để đơn giản hơn cho FE (không cần try/catch riêng).

## Response 200 — `list[SearchResult]`

```json
[
  {
    "document_id": "doc-1",
    "title": "Giáo trình Giải tích 1",
    "snippet": "...Chương 1. Giới hạn và liên tục..."
  }
]
```

Không khớp gì → `[]` (US3 AC2).

## Pydantic schema (tham chiếu `data-model.md#searchresult`)

```python
class SearchResult(BaseModel):
    document_id: str
    title: str
    snippet: str
```

## Matching logic

Xem `research.md` — Decision: Search matching logic (substring match không phân biệt hoa/thường trên `DocumentContent.text`, snippet cắt quanh vị trí khớp đầu tiên).
