# Implementation Plan: Tìm kiếm toàn văn & Trải nghiệm đọc sách EPUB

**Branch**: `002-search-reader-experience` | **Date**: 2026-07-17 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `specs/002-search-reader-experience/spec.md`

## Summary

Thay 2 endpoint fixture-backed (`/reader/{id}`, `/search`) bằng dữ liệu thật: đọc EPUB qua MinIO Signed URL (15 phút), tìm kiếm toàn văn PostgreSQL FTS trên title/author/nội dung OCR, snippet kết quả, tùy chỉnh giao diện đọc (font/theme, lưu local), và bookmark vị trí đọc theo user. Danh sách tài liệu (LDMS-026) gần như đã xong ở `/documents` (`DocumentsPage.tsx` + `GET /ocr/jobs`) — chỉ thiếu 1 nhánh điều hướng (published → Reader). Route `/reader/:documentId` và `/search` đã tồn tại dưới dạng file component (từ `001-reader-search-placeholder`) nhưng **chưa được đăng ký trong `App.tsx`** — sẽ được viết lại phần lớn nội dung (Epub.js thay vì text thô) và đăng ký route.

## Technical Context

**Language/Version**: Python 3.11 (`uv`) cho backend; TypeScript 6 + React 19 (Vite 8) cho frontend.
**Primary Dependencies**: Backend — FastAPI, SQLAlchemy, Alembic, `minio` SDK (`presigned_get_object` cho Signed URL), PyJWT (đã có). Frontend — React 19, `react-router` (đã có); **cần thêm `epubjs`** (chưa có trong `package.json`) để render EPUB thật thay cho text thô.
**Storage**: PostgreSQL 16 (bảng `documents`, `pages` đã có; thêm bảng mới `bookmarks`) + MinIO (EPUB đã được `publish` worker ghi vào `epub_object_key`, xem `app/workers/publish.py` — đã hoạt động, không cần thay đổi pipeline xuất bản).
**Testing**: `uv run pytest` — test suite chạy trên **SQLite in-memory** (`tests/conftest.py: create_engine("sqlite://")`, dùng `Base.metadata.create_all`, **không chạy qua Alembic**). Điều này ràng buộc cách viết Search: xem `research.md` mục "Dialect-aware FTS".
**Target Platform**: Web (SPA qua Vite dev server / Nginx); backend Docker Compose (API + Postgres + MinIO).
**Project Type**: Web application (`src/frontend` + `src/backend`, đã có sẵn).
**Performance Goals**: Tìm kiếm phản hồi < 3 giây (mục tiêu kiến trúc `docs/06-architecture.md` §2.1) — dễ đạt ở quy mô vài chục document của MVP, kể cả không có index (index vẫn được thêm để đúng tinh thần kiến trúc "GIN index tích hợp sẵn").
**Constraints**: Không thêm Elasticsearch/Celery/Redis. Signed URL bắt buộc `expires_in` mặc định 15 phút (Constitution Principle IV — non-negotiable). Không có bảng `User` trong DB — danh tính người dùng là JWT `sub` claim (xem `app/core/security.py`); Bookmark dùng `user_sub` thay vì `user_id` FK.
**Scale/Scope**: 1 model mới (`Bookmark`), 2 migration mới, ~5 endpoint mới/sửa (reader, bookmark GET+PUT, search), 1 dependency FE mới (`epubjs`), 2 route FE mới đăng ký (`/reader/:documentId`, `/search`), 1 sửa nhỏ điều hướng ở `DocumentsPage.tsx`.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-checked after Phase 1 design.*

| Principle | Trạng thái | Ghi chú |
|---|---|---|
| I. Layering | **PASS** | Code mới đi đúng 3 lớp đã có: `api/reader.py`, `api/search.py` (router) → `services/reader_service.py`, `services/search_service.py`, `services/bookmark_service.py` (nghiệp vụ) → `models/bookmark.py` + truy vấn trực tiếp qua SQLAlchemy (giống pattern đã dùng ở `publish_service.py`, không bắt buộc phải có Repository riêng cho mọi thứ). |
| II. Clear Contracts khi story được pick chính thức | **PASS — áp dụng đầy đủ, không miễn trừ** | Đây là bước "pick chính thức" (đủ AC), không còn là scaffold. Mọi endpoint mới dùng `response_model` Pydantic (`ReaderContent`, `BookmarkDetail`, `BookmarkUpdate`) và raise `NotFoundError`/`ValidationError`/`ForbiddenError` từ `core/exceptions.py`, không tự trả `JSONResponse` rải rác. |
| III. Test & Lint | **PASS** | `tasks.md` không thêm task viết test mới cho reader/bookmark/search (không được `spec.md`/user yêu cầu tường minh) — chỉ có 1 task Polish (T029) chạy lại toàn bộ `uv run ruff format .`, `uv run ruff check .`, `uv run pytest`, `npm run format`, `npm run lint`, `npm run build`, `npm test` trên code/test hiện có. CI (`.github/workflows/ci.yml`) vẫn tự động gate các lệnh này trên mọi PR vào `develop`/`main` bất kể có test mới hay không — xem Constitution v1.2.0 Principle III "CI enforcement note". |
| IV. File Security — non-negotiable | **PASS — đây chính là trọng tâm của feature này** | EPUB **không** serve qua route công khai trực tiếp: `GET /documents/{id}/reader` trả về MinIO Signed URL (`presigned_get_object`, `expires_in=900s`) sau khi `ensure_readable()` (RBAC `is_public`/token) đã pass. FE không có control tải file gốc. README sẽ ghi nhận residual risk (US5/FR-009) — xem `tasks.md` sau. |
| V. Heavy work chạy nền | **PASS — không áp dụng** | Không có OCR/EPUB compile mới trong scope này (EPUB đã được `publish` worker tạo sẵn ở LDMS-007, đã xong). Truy vấn search và tạo Signed URL đều là tác vụ nhanh, chạy đồng bộ trong request bình thường, không cần `BackgroundTasks`. |

**Kết luận**: Không có vi phạm nào cần biện minh trong Complexity Tracking.

## Project Structure

### Documentation (this feature)

```text
specs/002-search-reader-experience/
├── plan.md              # This file
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output
├── quickstart.md        # Phase 1 output
├── contracts/            # Phase 1 output
│   ├── get-reader.md
│   ├── get-search.md
│   └── bookmark.md
└── tasks.md              # Phase 2 output (/speckit.tasks — not created here)
```

### Source Code (repository root)

```text
src/backend/
├── app/
│   ├── models/
│   │   └── bookmark.py                 # [NEW] Bookmark(document_id, user_sub, location, updated_at)
│   ├── db/migrations/versions/
│   │   ├── 20260717_0006_search_indexes.py   # [NEW] GIN functional index (Postgres-only, op.execute thô) — tạo trước vì US3 (P3) đi trước US7 (P7)
│   │   └── 20260717_0007_bookmarks.py        # [NEW] tạo bảng bookmarks (unique document_id+user_sub), down_revision=0006
│   ├── schemas/
│   │   └── document.py                 # [MODIFY] thêm ReaderContent, BookmarkDetail, BookmarkUpdate; SearchResult.document_id → uuid.UUID; xoá docstring "Fixture-backed placeholder"
│   ├── services/
│   │   ├── document_service.py         # [MODIFY] chuyển `_ensure_readable` từ api/documents.py sang đây thành `ensure_readable()` dùng chung
│   │   ├── reader_service.py           # [NEW] get_reader_content(): validate published+epub, ensure_readable, mint Signed URL
│   │   ├── search_service.py           # [NEW] search_documents(): dialect-aware FTS (Postgres thật / SQLite fallback cho test)
│   │   └── bookmark_service.py         # [NEW] get_bookmark(), save_bookmark() (upsert theo document_id+user_sub)
│   ├── core/
│   │   └── storage.py                  # [MODIFY] thêm get_presigned_url(object_key, expires_seconds=900)
│   └── api/
│       ├── documents.py                # [MODIFY] dùng `ensure_readable` từ document_service thay vì hàm private cục bộ
│       ├── reader.py                   # [MODIFY] thay fixture bằng GET /documents/{id}/reader thật + GET/PUT /documents/{id}/bookmark
│       └── search.py                   # [MODIFY] thay fixture bằng search_service thật, áp RBAC filter
│
├── app/fixtures/documents.py            # [ORPHANED sau feature này — xem Complexity Tracking / báo cáo cuối, KHÔNG xoá]

src/frontend/
├── package.json                        # [MODIFY] thêm dependency "epubjs"
├── src/
│   ├── App.tsx                          # [MODIFY] đăng ký route "/reader/:documentId", "/search"; thêm nav link "Tìm kiếm"
│   ├── pages/
│   │   ├── DocumentsPage.tsx            # [MODIFY] Link tới document → "/reader/:id" nếu document_status === "published", giữ nguyên "/documents/:id" cho trạng thái khác (LDMS-026 AC2)
│   │   ├── ReaderPage.tsx               # [MODIFY — viết lại phần lớn] Epub.js render qua Signed URL, control cỡ chữ/theme (localStorage), bookmark restore/save khi rời trang, error states (US1 AC2/AC3)
│   │   └── SearchPage.tsx               # [MODIFY — nhỏ] đổi nguồn import sang services/api.ts (auth-aware), giữ nguyên UI/logic hiện có (contract SearchResult không đổi field)
│   └── services/
│       └── api.ts                       # [MODIFY] thêm getReaderContent(), getBookmark(), saveBookmark(), searchDocuments()
│
├── src/pages/DocumentListPage.tsx       # [ORPHANED — pre-existing, không wire vào App.tsx từ trước, không đụng tới]
└── src/services/documents.ts            # [ORPHANED sau feature này — chỉ còn được dùng bởi DocumentListPage.tsx, KHÔNG đụng tới]
```

**Structure Decision**: Không tạo cấu trúc thư mục mới — tiếp tục 3-lớp `api/ → services/ → models/` đã thiết lập. `reader.py` đã được scaffold sẵn đúng scope này từ trước (docstring "LDMS-008, LDMS-014, LDMS-019, LDMS-020" — chỉ thiếu LDMS-020 trong docstring cũ, sẽ cập nhật). Danh sách tài liệu (LDMS-026) **không cần endpoint mới** — `GET /ocr/jobs` (`list_latest_ocr_jobs`, đã có, join `Document` outer với `OcrJob` mới nhất) đã trả đủ toàn bộ document + status + created_at; chỉ thiếu nhánh điều hướng ở FE. Hai file component đặt tên đúng route đã được scaffold ở `001-reader-search-placeholder` (`ReaderPage.tsx`, `SearchPage.tsx`) nhưng **chưa từng được đăng ký trong `App.tsx`** — feature này viết lại nội dung và đăng ký route, thay vì tạo file mới trùng lặp. `DocumentListPage.tsx` + `services/documents.ts` là code còn sót lại không liên quan (không wire, không phải do feature này tạo ra) — giữ nguyên, không xoá, không sửa.

## Complexity Tracking

*Không có vi phạm Constitution nào cần biện minh — bảng để trống.*

**Lưu ý dọn dẹp (không phải vi phạm Constitution, chỉ để người review biết)**: Sau feature này, `app/fixtures/documents.py` không còn được import bởi bất kỳ router nào (cả `reader.py` và `search.py` đều chuyển sang dữ liệu thật) — trở thành dead code. Theo quy tắc "không xoá file trừ khi được yêu cầu", file này được giữ nguyên; người review có thể xoá thủ công nếu đồng ý đây thực sự không còn cần thiết.
