# Quickstart: Tìm kiếm toàn văn & Trải nghiệm đọc sách EPUB

Các bước tối thiểu để chạy và kiểm chứng feature này cục bộ, sau khi code đã được implement theo `plan.md`/`tasks.md`.

## 1. Backend

```bash
cd src/backend
uv sync
uv run alembic upgrade head        # áp 2 migration mới: bookmarks, search_indexes
docker compose up -d postgres minio # nếu chưa chạy sẵn
uv run uvicorn app.main:app --reload
```

## 2. Tạo dữ liệu thật để test (thay vì fixture)

1. Lấy dev token editor: `POST /auth/dev-token {"role": "editor"}`.
2. Upload 1 document: `POST /documents` (multipart PDF) → nhận `document_id`.
3. Chờ OCR job chạy xong (`GET /documents/{id}/ocr`, `status == "completed"`) hoặc sửa trực tiếp trang qua `PUT /documents/{id}/pages/{n}`.
4. Cập nhật metadata bắt buộc: `PUT /documents/{id}/metadata` (`title`, `author`).
5. Publish: `POST /documents/{id}/publish` (nếu route đặt tên khác, xem `api/publish.py`) → chờ `status == "published"`, `epub_object_key` có giá trị.

## 3. Kiểm chứng Reader (US1/US5)

```bash
curl http://localhost:8000/documents/{id}/reader
# → {"epub_url": "http://minio:9000/...", "expires_in": 900, ...}
curl -I "<epub_url>"                      # 200 trong 15 phút đầu
sleep 900 && curl -I "<epub_url>"         # 403/expired sau 15 phút — US5 AC3
```

Mở FE `http://localhost:5173/reader/{id}` — xác nhận: EPUB render được, không có nút "Tải EPUB", đổi cỡ chữ/Dark mode hoạt động, reload giữ preference (US6).

## 4. Kiểm chứng Search (US3/US4)

```bash
curl "http://localhost:8000/search?q=<từ khoá có trong title>"
curl "http://localhost:8000/search?q=<từ khoá chỉ có trong nội dung OCR>"
curl "http://localhost:8000/search?q=   "   # → []
```

Mở FE `http://localhost:5173/search` — nhập từ khoá, xác nhận snippet có highlight, click kết quả mở đúng Reader.

## 5. Kiểm chứng Document List (LDMS-026, US2)

Mở FE `http://localhost:5173/documents` — document `published` phải điều hướng sang `/reader/{id}` khi click, các trạng thái khác vẫn sang `/documents/{id}` (editor).

## 6. Kiểm chứng Bookmark (US7)

1. Đăng nhập user A (`/auth/dev-token`), mở Reader, cuộn tới 1 vị trí, điều hướng rời trang (không dùng lại tab để tránh mất `beforeunload`).
2. Mở lại `/reader/{id}` cùng user A → phải nhảy về đúng vị trí.
3. Đăng nhập user B (dev-token khác) mở cùng `{id}` → không thấy vị trí của A (mặc định từ đầu sách).

## 7. Test tự động

```bash
cd src/backend && uv run pytest
cd src/frontend && npm test
```

Lưu ý: test Search chạy trên SQLite (nhánh fallback trong `search_service.py`, xem `research.md` mục 5) — không kiểm chứng trực tiếp `to_tsvector`/`ts_headline` thật, chỉ kiểm chứng logic khớp từ khoá/snippet/RBAC filter tương đương.
