# Contract: `GET /search`

**Router file**: `src/backend/app/api/search.py` (thay fixture bằng `search_service.search_documents`)
**Owner**: Khoa Nguyễn — LDMS-015, LDMS-016.
**Auth**: optional user — kết quả lọc theo RBAC giống `ensure_readable` (chỉ trả document `is_public=true` cho guest; user đã đăng nhập thấy cả document private).

## Request

```
GET /search?q=<keyword>
Authorization: Bearer <token>   # optional
```

| Query param | Type | Ghi chú |
|---|---|---|
| `q` | `str = ""` | Rỗng/whitespace → trả `[]` ngay, không query DB (US3 AC3, Assumption đã chốt ở spec) |

## Response 200 — `list[SearchResult]`

```json
[
  {
    "document_id": "5b1f2e2a-...",
    "title": "Giáo trình Giải tích 1",
    "snippet": "...giới hạn của một dãy số được định nghĩa là..."
  }
]
```

Khớp cả `title`/`author` (US3 AC1) và `Page.text_content` (US3 AC2, full-text thật qua Postgres). Không lỗi 5xx với truy vấn hợp lệ (US3 AC4).

## Pydantic schema

```python
class SearchResult(BaseModel):
    document_id: uuid.UUID   # trước là str (fixture) — đổi để khớp Document.id thật
    title: str
    snippet: str
```

## Service function (dialect-aware — xem `research.md` mục 5)

```python
# app/services/search_service.py
def search_documents(
    db: Session, q: str, user: AuthenticatedUser | None
) -> list[SearchResult]:
    keyword = q.strip()
    if not keyword:
        return []
    if db.bind.dialect.name == "postgresql":
        return _search_postgres_fts(db, keyword, user)
    return _search_fallback_like(db, keyword, user)  # SQLite — chỉ dùng trong test suite
```

`_search_postgres_fts`: `to_tsvector('simple', title || ' ' || author)` cho Document, `to_tsvector('simple', text_content)` cho Page (join), match bằng `plainto_tsquery('simple', keyword)`, snippet bằng `ts_headline('simple', text_content, plainto_tsquery(...))`.
`_search_fallback_like`: `LIKE`/substring case-insensitive trên title/author/text_content + cắt snippet thủ công quanh vị trí khớp đầu (logic tương tự bản fixture cũ).

Cả 2 nhánh đều áp RBAC filter: `Document.is_public == True` khi `user is None`, không lọc gì thêm khi có user (khớp `ensure_readable` hiện tại).
