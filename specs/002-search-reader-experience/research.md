# Phase 0 Research: Tìm kiếm toàn văn & Trải nghiệm đọc sách EPUB

## 1. Signed URL cho EPUB (LDMS-014 / Constitution Principle IV)

**Decision**: Thêm `get_presigned_url(object_key, expires_seconds=900)` vào `app/core/storage.py`, dùng `minio_client.presigned_get_object(bucket, object_name, expires=timedelta(seconds=expires_seconds))`. Endpoint mới `GET /documents/{id}/reader` trả JSON `{document_id, title, author, epub_url, expires_in}` — FE (Epub.js) fetch bytes EPUB trực tiếp từ `epub_url` (MinIO), không qua backend proxy.

**Rationale**: Backlog LDMS-014 AC2 yêu cầu cụ thể "MinIO Signed URL", không phải chỉ "route có auth". Endpoint `/documents/{id}/source` hiện tại (proxy stream qua backend) phục vụ mục đích khác (Split-screen Editor đọc file scan gốc, LDMS-017) — không tái sử dụng cho EPUB vì đó không phải luồng đọc sách công khai cho độc giả.

**Alternatives considered**:
- Proxy stream EPUB qua backend giống `/source` — bị loại vì không khớp literal AC "Signed URL", và tốn băng thông backend không cần thiết cho file có thể serve thẳng từ object storage.
- Presigned URL không giới hạn thời gian / thời gian dài hơn — bị loại, Constitution Principle IV cố định 15 phút.

## 2. Danh tính người dùng cho Bookmark

**Decision**: `Bookmark.user_sub: str` (JWT `sub` claim), không phải `user_id` FK — vì hệ thống **không có bảng `User`** trong DB (`app/models/` không có `user.py`; định danh chỉ tồn tại trong JWT — xem `app/core/security.py::AuthenticatedUser`). Unique constraint `(document_id, user_sub)`.

**Rationale**: Nhất quán với cách hệ thống đã xử lý identity ở mọi nơi khác (RBAC, role check đều dựa JWT claims, không query DB user). Thêm bảng `User` chỉ để FK cho Bookmark là over-engineering ngoài phạm vi story này.

**Lưu ý vận hành**: Ở `AUTH_MODE=mock`, mỗi lần gọi `/auth/dev-token` sinh `sub` là **UUID ngẫu nhiên mới** (xem `app/api/auth.py`) — nghĩa là bookmark chỉ "nhớ" được trong cùng một phiên token (FE lưu token vào `localStorage`, không tự xin token mới liên tục). Đây là giới hạn có sẵn của cơ chế Mock Auth, không phải bug của feature này.

## 3. Định dạng vị trí đọc (Bookmark location)

**Decision**: `location: str` lưu nguyên văn **EPUB CFI** (Canonical Fragment Identifier) do Epub.js sinh ra qua `rendition.currentLocation()` — backend coi đây là chuỗi mờ (opaque), chỉ lưu/trả lại y nguyên, không parse.

**Rationale**: Epub.js có sẵn API `rendition.display(cfi)` để nhảy thẳng tới vị trí — không cần backend hiểu cấu trúc CFI. Tránh phát minh lại định dạng vị trí riêng (ví dụ số trang) vốn không khớp với cách Epub.js quản lý vị trí đọc responsive (không có khái niệm "trang" cố định).

**Alternatives considered**: Lưu % tiến độ đọc (progress percentage) — bị loại vì kém chính xác hơn CFI khi nhảy lại đúng vị trí (yêu cầu SC-004/US7 AC2 "nhảy về đúng vị trí").

## 4. Thời điểm lưu Bookmark

**Decision** (đã chốt qua `/speckit.clarify`): chỉ lưu **một lần khi rời/đóng Reader** (React `useEffect` cleanup + `beforeunload`), không tự động lưu định kỳ trong lúc đọc.

**Rationale**: Đơn giản, đủ cho hầu hết trường hợp thực tế; lưu định kỳ cần debounce + xử lý race condition, vượt quá effort cho phép của story Should-have này.

## 5. Tìm kiếm toàn văn — dialect-aware FTS (quyết định quan trọng nhất)

**Vấn đề phát hiện được**: `tests/conftest.py` chạy toàn bộ test suite trên **SQLite in-memory** (`create_engine("sqlite://")`, dùng `Base.metadata.create_all()` — **không chạy qua Alembic**, và `.github/workflows/ci.yml` không có service Postgres nào). SQLite không có `to_tsvector`/`plainto_tsquery`/`ts_headline`. Nếu viết thẳng SQL Postgres FTS, toàn bộ test cho Search sẽ không chạy được trong CI hiện tại.

**Decision**: `search_service.search_documents(db, q)` **branch theo dialect**:
- `db.bind.dialect.name == "postgresql"` (production/Docker Compose thật): dùng `func.to_tsvector('simple', ...)`, `func.plainto_tsquery('simple', q)`, `func.ts_headline('simple', text_content, plainto_tsquery(...))` cho snippet.
- Dialect khác (SQLite — chỉ xảy ra trong test suite hiện tại): fallback bằng so khớp `LIKE`/Python substring (case-insensitive) trên `title`/`author`/`Page.text_content`, và cắt snippet thủ công quanh vị trí khớp đầu tiên (logic tương tự bản fixture cũ ở `001-reader-search-placeholder`, giữ lại đúng chỗ này thay vì xoá hẳn).

Text search config dùng `'simple'` (không stem) thay vì `'english'` — vì nội dung OCR là tiếng Việt, Postgres không có dictionary tiếng Việt built-in; `'simple'` tách từ theo khoảng trắng/dấu câu mà không "stem" sai sang tiếng Anh.

**Rationale**: Giữ đúng kiến trúc đã chọn (`docs/06-architecture.md` §4.2: PostgreSQL FTS cho production) mà vẫn test được trên hạ tầng test hiện tại của repo, không phải thêm Postgres service vào CI (thay đổi lớn, ngoài phạm vi 1 feature). Fallback chỉ tồn tại vì giới hạn test, không phải đường chạy thật ở production (production luôn dùng Postgres theo `docker-compose.yml`).

**Alternatives considered**:
- Thêm Postgres service vào `.github/workflows/ci.yml` để test thật trên Postgres — cân nhắc nhưng bị loại cho feature này: thay đổi CI ảnh hưởng toàn team, nằm ngoài scope 1 feature, nên đề xuất làm riêng (ví dụ ticket kỹ thuật hạ tầng test) nếu team muốn test FTS thật 1:1.
- Mock toàn bộ `search_service` trong test (giống cách `minio_client` được monkeypatch) — bị loại vì sẽ không kiểm chứng được logic khớp từ khóa/snippet thật, chỉ test được phần routing/schema.
- Index GIN được thêm bằng `op.execute()` thô trong migration (không khai báo qua `Index()` trong model) để tránh việc `Base.metadata.create_all()` (chạy trong test) cố tạo index Postgres-only trên SQLite và lỗi.

## 6. Danh sách tài liệu (LDMS-026) — tái sử dụng thay vì tạo endpoint mới

**Decision**: Không tạo `GET /documents` (list). `GET /ocr/jobs` (`list_latest_ocr_jobs`, đã có sẵn ở `ocr_service.py`) đã outer-join toàn bộ `Document` với OCR job mới nhất, trả `document_status`, `created_at` — đúng những gì LDMS-026 AC1/AC3/AC4 cần, và `DocumentsPage.tsx` đã hiển thị đúng bảng/empty-state/link upload. Chỉ còn thiếu AC2 (điều hướng theo trạng thái) — sửa 1 dòng logic điều hướng trong `DocumentsPage.tsx`.

**Rationale**: Tránh 2 nguồn sự thật (2 "document list") khác nhau cho cùng một khái niệm; endpoint `/ocr/jobs` tuy đặt tên theo M2 (OCR dashboard) nhưng dữ liệu trả về đã đủ tổng quát cho mục đích danh sách chung.

**Lưu ý phạm vi**: file `DocumentListPage.tsx` + `services/documents.ts::getDocuments` (từ `001-reader-search-placeholder`) là bản scaffold cũ, **chưa từng được đăng ký route** trong `App.tsx` — không liên quan tới quyết định này, giữ nguyên không đụng tới (xem `plan.md` Project Structure).

## 7. Tùy chỉnh giao diện đọc (LDMS-019) — theming qua Epub.js

**Decision**: Dùng API theming có sẵn của Epub.js: `rendition.themes.register('light', {...})` / `register('dark', {...})`, `rendition.themes.select(theme)`, và `rendition.themes.fontSize('Npx')` cho cỡ chữ. State `{fontSize, theme}` lưu trực tiếp trong component `ReaderPage.tsx` (`useState` + ghi `localStorage` mỗi lần đổi, đọc lại khi mount) — không cần Context/global state vì chỉ dùng trong 1 trang.

**Rationale**: Epub.js render nội dung EPUB trong `<iframe>` riêng — CSS thông thường của trang cha không thể xuyên vào để đổi màu chữ/nền bên trong, bắt buộc phải dùng theming API riêng của thư viện. Giữ state cục bộ component (không Context) đúng tinh thần "no abstractions for single-use code".
