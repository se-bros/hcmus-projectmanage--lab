---
description: "Task list for Tìm kiếm toàn văn & Trải nghiệm đọc sách EPUB"
---

# Tasks: Tìm kiếm toàn văn & Trải nghiệm đọc sách EPUB

**Input**: Design documents from `specs/002-search-reader-experience/`
**Prerequisites**: `plan.md`, `spec.md`, `research.md`, `data-model.md`, `contracts/`, `quickstart.md` (all present)

**Tests**: Không có task viết test riêng — spec/`` của feature này không yêu cầu tường minh. Việc chạy `uv run pytest`/`npm test` như một gate trước khi merge (Constitution Principle III + CI) được gộp vào 1 task ở Phase Polish thay vì tách theo từng story.

**Organization**: Task nhóm theo User Story (P1→P7, khớp thứ tự trong `spec.md`) để mỗi story implement/test độc lập được.

## Format: `[ID] [P?] [Story] Description`

---

## Phase 1: Setup

- [x] T001 [P] Thêm dependency `epubjs` vào `src/frontend/package.json`, chạy `npm install` trong `src/frontend` (cần cho US1/US6/US7 — Epub.js render + theming + CFI bookmark).

*Không có task setup nào khác — dự án đã có sẵn cấu trúc `src/backend`/`src/frontend`, DB/MinIO/Auth đã hoạt động.*

---

## Phase 2: Foundational (Blocking Prerequisites)

**⚠️ CRITICAL**: Phải xong trước khi bắt đầu US1 và US3.

- [x] T002 Chuyển hàm `_ensure_readable` (hiện private trong `src/backend/app/api/documents.py`) thành `ensure_readable(document, user)` công khai trong `src/backend/app/services/document_service.py`; cập nhật `documents.py` để import và gọi hàm này thay vì định nghĩa cục bộ. Không đổi hành vi — test hiện có ở `tests/api/test_documents.py` phải pass nguyên trạng.

**Checkpoint**: `ensure_readable` sẵn sàng dùng chung cho US1 (reader) và US3 (search RBAC filter).

---

## Phase 3: User Story 1 - Đọc sách EPUB đã xuất bản (Priority: P1) 🎯 MVP

**Goal**: Độc giả mở `/reader/:documentId` và đọc được nội dung EPUB thật (không còn text thô từ fixture), qua MinIO Signed URL.

**Independent Test**: Publish 1 document thật (theo `quickstart.md` §2) → mở `/reader/{id}` trực tiếp bằng URL → EPUB render đọc được; document chưa publish hoặc `id` sai → thấy lỗi rõ ràng, không màn trắng.

### Implementation

- [x] T003 [P] [US1] Thêm `get_presigned_url(object_key, expires_seconds=900)` vào `src/backend/app/core/storage.py` (dùng `minio_client.presigned_get_object`, xem `contracts/get-reader.md`).
- [x] T004 [P] [US1] Trong `src/backend/app/schemas/document.py`: thêm `ReaderContent` (document_id, title, author, epub_url, expires_in); xoá `DocumentContent` (chỉ còn được dùng bởi route fixture sẽ bị thay ở T006 — orphan do chính thay đổi này tạo ra).
- [x] T005 [US1] Tạo `src/backend/app/services/reader_service.py::get_reader_content()` — validate `status == "published"` + `epub_object_key` tồn tại, gọi `ensure_readable` (T002), mint Signed URL (T003) (phụ thuộc T003, T004).
- [x] T006 [US1] Viết lại `src/backend/app/api/reader.py`: đổi router sang `prefix="/documents"`, thay route fixture `GET /reader/{document_id}` bằng `GET /documents/{document_id}/reader` gọi `reader_service.get_reader_content` (T005); xoá import `app.fixtures.documents.DOCUMENT_CONTENTS` khỏi file này (giữ nguyên `app/fixtures/documents.py` — `search.py` vẫn dùng tới Phase 5).
- [x] T007 [P] [US1] Thêm `getReaderContent(documentId)` vào `src/frontend/src/services/api.ts` (auth-aware, dùng `request()` có sẵn).
- [x] T008 [US1] Viết lại `src/frontend/src/pages/ReaderPage.tsx`: gọi `getReaderContent` (T007), render qua `epubjs` (`ePub(epub_url).renderTo(...)`), xử lý lỗi "chưa xuất bản"/"không có bản đọc"/"không tìm thấy" (US1 AC2/AC3); bỏ hẳn logic hiển thị text thô cũ.
- [x] T009 [US1] Đăng ký route `/reader/:documentId` → `ReaderPage` trong `src/frontend/src/App.tsx` (route này chưa từng tồn tại trong app thật).

**Checkpoint**: US1 hoạt động độc lập — mở thẳng URL Reader với 1 document đã publish là đọc được.

---

## Phase 4: User Story 2 - Danh sách tài liệu hoàn thiện (Priority: P2)

**Goal**: Danh sách tài liệu điều hướng đúng theo trạng thái (LDMS-026 AC2) — AC1/AC3/AC4 **đã có sẵn** từ `DocumentsPage.tsx` + `GET /ocr/jobs`, không cần việc gì thêm (xem `research.md` mục 6).

**Independent Test**: Danh sách có 1 document `published` và 1 document trạng thái khác → click document published mở `/reader/:id`, click document còn lại vẫn mở `/documents/:id` (editor).

### Implementation

- [x] T010 [US2] Trong `src/frontend/src/pages/DocumentsPage.tsx`, sửa `Link to` của mỗi document card: `` `/reader/${item.document_id}` `` khi `item.document_status === 'published'`, giữ nguyên `` `/documents/${item.document_id}` `` cho các trạng thái khác.

**Checkpoint**: US2 hoàn thiện — phụ thuộc route `/reader/:documentId` đã đăng ký ở T009 (US1) để không rơi vào catch-all `*` redirect.

---

## Phase 5: User Story 3 - Tìm kiếm toàn văn (Priority: P3)

**Goal**: `GET /search` trả kết quả thật từ PostgreSQL FTS trên title/author/nội dung OCR, thay fixture.

**Independent Test**: Seed từ khoá trong title 1 document và trong `Page.text_content` của document khác → tìm cả hai đều ra đúng kết quả; `q` rỗng → `[]`; query hợp lệ không lỗi server.

### Implementation

- [x] T011 [P] [US3] Thêm migration `src/backend/app/db/migrations/versions/20260717_0006_search_indexes.py` — GIN functional index Postgres-only qua `op.execute()` thô trên `to_tsvector('simple', ...)` của `documents(title, author)` và `pages(text_content)` (không khai báo qua SQLAlchemy `Index()` — xem `research.md` mục 5 lý do).
- [x] T012 [P] [US3] Trong `src/backend/app/schemas/document.py`: đổi `SearchResult.document_id` từ `str` sang `uuid.UUID`; xoá docstring "Fixture-backed placeholder".
- [x] T013 [US3] Tạo `src/backend/app/services/search_service.py::search_documents()` — dialect-aware: `_search_postgres_fts` (to_tsvector/plainto_tsquery/ts_headline) khi `db.bind.dialect.name == "postgresql"`, `_search_fallback_like` (LIKE + snippet thủ công) khi khác; áp filter `is_public` khi `user is None` (phụ thuộc T012, T002).
- [x] T014 [US3] Viết lại `src/backend/app/api/search.py`: gọi `search_service.search_documents` (T013) thay fixture; xoá import `app.fixtures.documents` khỏi file này.
- [x] T015 [P] [US3] Thêm `searchDocuments(query)` vào `src/frontend/src/services/api.ts` (auth-aware).
- [x] T016 [US3] Sửa `src/frontend/src/pages/SearchPage.tsx`: đổi import `searchDocuments`/`SearchResult` từ `services/documents.ts` sang `services/api.ts` (T015) — UI/logic highlight giữ nguyên, không đổi.
- [x] T017 [US3] Đăng ký route `/search` → `SearchPage` trong `src/frontend/src/App.tsx`; thêm nav link "Tìm kiếm".

**Checkpoint**: US3 hoạt động độc lập — tìm kiếm ra đúng document theo cả title lẫn nội dung OCR.

---

## Phase 6: User Story 4 - Snippet kết quả và mở đúng Reader (Priority: P4)

**Goal**: Xác nhận mỗi kết quả tìm kiếm có snippet đúng và click mở đúng Reader — phần lớn đã được tạo ra bởi US3 (snippet là 1 phần của cùng câu query FTS) và UI có sẵn từ bản scaffold cũ (`highlightSnippet`, `Link to="/reader/:id"` trong `SearchPage.tsx`).

**Independent Test**: Với 1 kết quả tìm kiếm đã biết chứa từ khoá X → `snippet` chứa X; click kết quả → mở đúng `/reader/{document_id}` tương ứng.

### Implementation

- [x] T018 [US4] Kiểm tra thủ công theo `quickstart.md` §4: `snippet` trả về từ T013/T014 hiển thị đúng có highlight trong `SearchPage.tsx`, click kết quả điều hướng đúng document — sửa lại nếu phát hiện lệch (không kỳ vọng có thay đổi code nếu US3 đã đúng). *Đã sửa: strip markup `<b>`/`</b>` mặc định của `ts_headline` trong `search_service.py` để không lọt tag thô vào snippet — FE tự highlight qua `highlightSnippet`.*

**Checkpoint**: US4 xác nhận xong — không có phần backend/frontend mới ngoài T018.

---

## Phase 7: User Story 5 - Giảm rủi ro tải file gốc khi đọc (Priority: P5)

**Goal**: Không có control tải EPUB gốc trên UI; residual risk được ghi nhận. Cơ chế Signed URL 15 phút đã được triển khai đầy đủ ở US1 (T003, T005, T006) — story này chỉ bổ sung phần còn thiếu.

**Independent Test**: Ở trang Reader không thấy nút "Tải EPUB"/"Download"; README có mục Security nói rõ residual risk.

### Implementation

- [x] T019 [US5] Rà lại `src/frontend/src/pages/ReaderPage.tsx` (viết ở T008) — xác nhận không có control nào trỏ tới tải file EPUB gốc; xoá nếu vô tình có. *Đã xác nhận: ReaderPage chỉ truyền Signed URL cho epubjs, không có nút Download nào.*
- [x] T020 [US5] Thêm mục "## Bảo mật đọc sách (LDMS-014)" vào `README.md` (repo root) ghi nhận: EPUB chỉ qua Signed URL 15 phút; residual risk (screenshot, DevTools) không thể chặn hoàn toàn bằng kỹ thuật.

**Checkpoint**: US5 hoàn thiện.

---

## Phase 8: User Story 6 - Tùy chỉnh giao diện đọc (Priority: P6)

**Goal**: Tăng/giảm cỡ chữ, chuyển Light/Dark mode trong Reader, giữ preference qua `localStorage`.

**Independent Test**: Mở Reader (từ US1), đổi cỡ chữ/theme → thấy đổi ngay; reload cùng trình duyệt → preference giữ nguyên.

### Implementation

- [x] T021 [US6] Trong `src/frontend/src/pages/ReaderPage.tsx` (đã có từ T008): thêm control cỡ chữ +/- và toggle Light/Dark dùng `rendition.themes.register()/select()/fontSize()` (Epub.js theming API — CSS thường không xuyên được vào iframe nội dung EPUB, xem `research.md` mục 7); đọc/ghi `{fontSize, theme}` vào `localStorage` khi mount/đổi.

**Checkpoint**: US6 hoàn thiện.

---

## Phase 9: User Story 7 - Đánh dấu trang đọc dở (Priority: P7)

**Goal**: Lưu và khôi phục vị trí đọc (CFI) theo `(document_id, user_sub)`, chỉ lưu khi rời/đóng Reader (đã chốt qua `/speckit.clarify`).

**Independent Test**: User A đọc, cuộn tới 1 vị trí, rời trang; mở lại → nhảy đúng vị trí. User B mở cùng document → không thấy vị trí của A.

### Implementation

- [x] T022 [P] [US7] Tạo `src/backend/app/models/bookmark.py::Bookmark` (document_id FK CASCADE, user_sub, location, created_at, updated_at, unique `(document_id, user_sub)`) theo `data-model.md`. *Đã import vào `app/models/__init__.py` để `create_all`/migrations thấy được.*
- [x] T023 [US7] Thêm migration `src/backend/app/db/migrations/versions/20260717_0007_bookmarks.py` (`down_revision = "20260717_0006"`) — tạo bảng `bookmarks` khớp model T022.
- [x] T024 [P] [US7] Trong `src/backend/app/schemas/document.py`: thêm `BookmarkDetail` (document_id, location, updated_at) và `BookmarkUpdate` (location, validator không rỗng).
- [x] T025 [US7] Tạo `src/backend/app/services/bookmark_service.py::get_bookmark()`/`save_bookmark()` (upsert theo `(document_id, user_sub)`, phụ thuộc T022, T024).
- [x] T026 [US7] Thêm `GET`/`PUT /documents/{document_id}/bookmark` vào `src/backend/app/api/reader.py` — `GET`/`PUT` đều yêu cầu `get_current_user` (bắt buộc đăng nhập, không optional); gọi `bookmark_service` (T025).
- [x] T027 [P] [US7] Thêm `getBookmark(documentId)`/`saveBookmark(documentId, location)` vào `src/frontend/src/services/api.ts`.
- [x] T028 [US7] Trong `src/frontend/src/pages/ReaderPage.tsx` (đã có từ T008/T021): khi mount, gọi `getBookmark` (T027) và `rendition.display(location)` nếu có (404/401 → mở từ đầu, không phải lỗi); khi unmount, gọi `saveBookmark` với CFI hiện tại theo dõi qua event `relocated` (chỉ khi user đã đăng nhập — kiểm token localStorage).

**Checkpoint**: Tất cả 7 user story hoạt động độc lập và cùng nhau.

---

## Phase 10: Polish

- [x] T029 Chạy full verification: `uv run ruff format .`, `uv run ruff check .`, `uv run pytest` (backend); `npm run format`, `npm run lint`, `npm run build`, `npm test` (frontend) — bắt buộc trước khi merge theo Constitution Principle III + CI (`.github/workflows/ci.yml`); đi qua từng bước `quickstart.md` thủ công 1 lần. *Kết quả: backend ruff sạch + 53 pytest pass; frontend oxlint exit 0 (1 warning có sẵn ở `AuthContext.tsx`, không phải file của feature này), `tsc -b && vite build` pass, 14 vitest pass. Kiểm chứng runtime `quickstart.md` (cần Postgres+MinIO+EPUB thật) chưa chạy trong môi trường này — để lại cho người triển khai theo `quickstart.md`.*

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: không phụ thuộc gì — chạy ngay.
- **Foundational (Phase 2)**: phụ thuộc Setup xong (thực ra độc lập với T001, có thể chạy song song) — **chặn US1 và US3**.
- **US1 (Phase 3, P1 — MVP)**: phụ thuộc Foundational (T002). Không phụ thuộc story khác.
- **US2 (Phase 4, P2)**: phụ thuộc route `/reader/:documentId` đã đăng ký ở **US1/T009** (nếu không, click sẽ rơi vào catch-all redirect).
- **US3 (Phase 5, P3)**: phụ thuộc Foundational (T002, dùng lại RBAC rule cho filter). Không phụ thuộc US1/US2 về code, nhưng UI đầy đủ (kết quả click mở Reader) cần US1 đã xong.
- **US4 (Phase 6, P4)**: phụ thuộc US1 (Reader hoạt động) + US3 (search + snippet) đã xong — chủ yếu là task xác nhận, không code mới.
- **US5 (Phase 7, P5)**: phụ thuộc US1 (Signed URL + ReaderPage đã tồn tại để audit).
- **US6 (Phase 8, P6)**: phụ thuộc US1 (cần `rendition` instance đã dựng ở `ReaderPage.tsx`).
- **US7 (Phase 9, P7)**: phụ thuộc US1 (cùng lý do US6) + migration T011 (US3) vì `down_revision` của T023 chain sau `20260717_0006`.
- **Polish (Phase 10)**: sau tất cả story muốn merge.

### Parallel Opportunities

```bash
# Trong US1 (Phase 3) — 2 việc độc lập file, chạy song song:
Task: "T003 get_presigned_url trong core/storage.py"
Task: "T007 getReaderContent() trong services/api.ts"

# Trong US3 (Phase 5) — 2 việc độc lập file:
Task: "T011 migration search_indexes"
Task: "T012 SearchResult schema update"

# Trong US7 (Phase 9) — 3 việc độc lập file:
Task: "T022 Bookmark model"
Task: "T024 BookmarkDetail/BookmarkUpdate schema"
Task: "T027 getBookmark/saveBookmark trong services/api.ts"
```

---

## Implementation Strategy

### MVP First (User Story 1)

1. Phase 1 (Setup) → Phase 2 (Foundational) → Phase 3 (US1).
2. **DỪNG và kiểm chứng**: publish 1 document thật, mở `/reader/{id}` trực tiếp, đọc được EPUB thật qua Signed URL. Đây là MVP checkpoint của feature này.

### Incremental Delivery

Tiếp theo theo đúng thứ tự ưu tiên P2→P7 (mỗi phase đều có Checkpoint riêng ở trên): US2 (điều hướng danh sách) → US3 (search thật) → US4 (xác nhận snippet) → US5 (audit + README) → US6 (customize) → US7 (bookmark) → Polish (T029, gate trước khi merge `develop`).

Vì hầu hết hạ tầng (DB, Auth, EPUB publish pipeline) đã có sẵn từ các story khác trong sprint, feature này không cần chiến lược "nhiều dev song song trên nhiều story" — khối lượng việc còn lại vừa đủ cho 1 người (Khoa Nguyễn, đúng phân công `docs/plan.md`) đi tuần tự P1→P7.
