---
description: "Task list template for feature implementation"
---

# Tasks: Reader/Search Placeholder & Document List (prep cho LDMS-008, LDMS-026)

**Input**: Design documents from `specs/001-reader-search-placeholder/` (spec.md, plan.md, research.md, data-model.md, contracts/, quickstart.md)
**Prerequisites**: plan.md, spec.md

**Tests**: Không có task test — theo `constitution.md` Principle III, test/lint gate bị hoãn tới khi story được pick chính thức (đây là scaffold trên fixture). Người dùng cũng không yêu cầu thêm test khi chạy `/speckit.tasks`.

**Organization**: Tasks nhóm theo user story để mỗi story implement/test/demo độc lập được, đúng thứ tự P1 → P2 → P3 trong spec.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Có thể làm song song (khác file, không phụ thuộc nhau)
- **[Story]**: US1 = Document List, US2 = Reader placeholder, US3 = Search placeholder

## Path Conventions

Web application đã có sẵn: `src/backend/app/`, `src/frontend/src/` (xem `plan.md` — Project Structure).

---

## Phase 1: Setup

**Purpose**: Chuẩn bị dependency còn thiếu và khung schema dùng chung.

- [x] T001 [P] Thêm `react-router-dom` (^6) vào `src/frontend/package.json` dependencies, chạy `npm install` trong `src/frontend` (quyết định tại `research.md` — dự án chưa có routing lib nào).
- [x] T002 [P] Tạo `src/backend/app/schemas/document.py` với 3 Pydantic model theo `contracts/`: `DocumentSummary`, `DocumentContent`, `SearchResult` (field/type theo `data-model.md`).

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Dữ liệu fixture + API client dùng chung cho cả 3 user story.

**⚠️ CRITICAL**: Không story nào bắt đầu được trước khi phase này xong.

- [x] T003 Tạo `src/backend/app/fixtures/documents.py`: seed ≥ 2 `Document` (một document **không** có `DocumentContent`, để test US2 AC2) và dict nội dung text theo `document_id`, đảm bảo có sẵn 1 từ khóa chắc chắn khớp và 1 từ khóa chắc chắn không khớp (phục vụ US3 AC1/AC2) — theo "Fixture seed tối thiểu" trong `data-model.md`. Phụ thuộc T002 (dùng schema để type dữ liệu fixture nếu cần).
- [x] T004 [P] Bọc `<BrowserRouter>` quanh `<App />` trong `src/frontend/src/main.tsx`.
- [x] T005 [P] Tạo `src/frontend/src/services/documents.ts` với 3 hàm gọi API: `getDocuments()`, `getDocumentContent(documentId)`, `searchDocuments(query)` — dùng `fetch`, trả kiểu dữ liệu khớp `contracts/` (không dùng `any`). **Quan trọng**: `fetch` không tự throw khi server trả 4xx/5xx — mỗi hàm phải kiểm tra `response.ok` và `throw` (kèm status/`detail` từ body) khi không ok, để `ReaderPage.tsx` (T011) bắt được lỗi 404 đúng theo `contracts/get-reader-document.md`.

**Checkpoint**: Fixture + routing wrapper + API client sẵn sàng — bắt đầu implement từng story.

---

## Phase 3: User Story 1 - Xem danh sách tài liệu (Priority: P1) 🎯 MVP

**Goal**: Mở `/` thấy danh sách tài liệu (từ fixture qua `GET /documents`), click một dòng điều hướng sang Reader.

**Independent Test**: Seed fixture ≥ 1 document, mở `/`, xác nhận bảng/list hiển thị đúng tên/status/ngày tạo (US1 AC1); mảng rỗng → trạng thái rỗng, không lỗi (US1 AC3).

- [x] T006 [US1] Implement `GET /documents` trong `src/backend/app/api/documents.py`: đọc từ `app/fixtures/documents.py`, trả `list[DocumentSummary]` theo `contracts/get-documents.md`. Phụ thuộc T002, T003.
- [x] T007 [US1] Tạo `src/frontend/src/pages/DocumentListPage.tsx`: gọi `getDocuments()`, render bảng (tên, status, ngày tạo), xử lý trạng thái rỗng (US1 AC3) và trạng thái lỗi gọi API (Edge Case). Phụ thuộc T005.
- [x] T008 [US1] Trong `src/frontend/src/App.tsx`: dựng `<Routes>` với route mặc định `/` → `DocumentListPage`. Phụ thuộc T004, T007.
- [x] T009 [US1] Trong `DocumentListPage.tsx`, mỗi dòng dùng `<Link to={`/reader/${id}`}>` để điều hướng sang Reader (US1 AC2). Phụ thuộc T007.

**Checkpoint**: Document List chạy độc lập được (Reader/Search phía sau chưa cần tồn tại để test riêng US1, dù click sẽ 404 route cho tới khi US2 xong).

---

## Phase 4: User Story 2 - Đọc thử nội dung tài liệu (Priority: P2)

**Goal**: Mở `/reader/:documentId` thấy nội dung text thô của tài liệu, hoặc thông báo "không tìm thấy" nếu sai id.

**Independent Test**: Mở thẳng URL `/reader/<id-có-trong-fixture>` (không cần qua Document List) và xác nhận nội dung đúng (US2 AC1); mở `/reader/<id-không-tồn-tại>` → thông báo rõ ràng (US2 AC2).

- [x] T010 [US2] Implement `GET /reader/{document_id}` trong `src/backend/app/api/reader.py`: đọc fixture, trả `DocumentContent` hoặc `HTTPException(404)` theo `contracts/get-reader-document.md`. Phụ thuộc T002, T003.
- [x] T011 [US2] Tạo `src/frontend/src/pages/ReaderPage.tsx`: lấy `documentId` từ route param (`useParams`), gọi `getDocumentContent`, hiển thị `text`; bắt lỗi 404 → hiển thị "không tìm thấy tài liệu" (US2 AC2). Phụ thuộc T005.
- [x] T012 [US2] Thêm route `/reader/:documentId` → `ReaderPage` trong `src/frontend/src/App.tsx`. Phụ thuộc T008 (cùng file `App.tsx`, làm sau T008), T011.

**Checkpoint**: Document List + Reader chạy được cùng nhau — đây là luồng demo chính của Ngày 2 (`docs/plan.md`).

---

## Phase 5: User Story 3 - Tìm kiếm thử trên dữ liệu giả (Priority: P3)

**Goal**: Mở `/search`, nhập từ khóa, thấy danh sách tài liệu khớp (kèm snippet), click kết quả mở đúng Reader.

**Independent Test**: Mở thẳng `/search`, nhập từ khóa có trong fixture → thấy kết quả (US3 AC1); từ khóa không khớp → "không có kết quả" (US3 AC2); submit rỗng → không lỗi (US3 AC3). Độc lập với US1/US2 (chỉ cần US2 tồn tại để link kết quả hoạt động, nhưng test search tự thân không phụ thuộc US1).

- [x] T013 [US3] Implement `GET /search?q=` trong `src/backend/app/api/search.py`: `q` rỗng/whitespace → trả `[]`; ngược lại substring match trên `DocumentContent.text` (không phân biệt hoa/thường), trả `list[SearchResult]` kèm snippet, theo `contracts/get-search.md`. Phụ thuộc T002, T003.
- [x] T014 [US3] Tạo `src/frontend/src/pages/SearchPage.tsx`: ô input + submit, gọi `searchDocuments(query)`, hiển thị danh sách kết quả (title + snippet) hoặc "không có kết quả"; mỗi kết quả là `<Link to={`/reader/${document_id}`}>`. Phụ thuộc T005.
- [x] T015 [US3] Thêm route `/search` → `SearchPage` trong `src/frontend/src/App.tsx`. Phụ thuộc T012 (cùng file, làm sau T012), T014.

**Checkpoint**: Cả 3 story hoạt động độc lập và cùng nhau — toàn bộ luồng "danh sách / đọc / tìm kiếm" trên fixture đã demo được.

---

## Phase 6: Polish

**Purpose**: Yêu cầu universal từ `AGENTS.md`/`CLAUDE.md` (áp dụng mọi thay đổi, không phải gate "trước khi merge develop" của constitution).

- [x] T016 Chạy `uv run ruff format .` và `uv run ruff check .` trong `src/backend`; sửa mọi lỗi liên quan tới các file đã đổi (T002, T003, T006, T010, T013).
- [x] T017 Chạy `npm run format` và `npm run lint` trong `src/frontend`; sửa mọi lỗi liên quan tới các file đã đổi (T001, T004, T005, T007-T009, T011-T012, T014-T015).
- [x] T018 Chạy thủ công các bước trong `quickstart.md` (bao gồm phần "Xác nhận Edge Cases") để xác nhận toàn bộ Acceptance Scenarios trong `spec.md` đạt.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: Không phụ thuộc gì — làm ngay.
- **Foundational (Phase 2)**: Phụ thuộc Setup — **chặn** toàn bộ user story.
- **User Stories (Phase 3-5)**: Đều phụ thuộc Foundational xong. Có thể làm song song bởi nhiều dev nếu tách phần backend (T006/T010/T013 khác file nhau), nhưng phần sửa `App.tsx` (T008, T012, T015) phải làm **tuần tự** vì cùng 1 file.
- **Polish (Phase 6)**: Phụ thuộc tất cả story đã chọn triển khai xong.

### User Story Dependencies

- **US1 (P1)**: Không phụ thuộc US2/US3 để tự chạy (chỉ có link sang `/reader/:id` sẽ 404 cho tới khi US2 xong — chấp nhận được cho MVP checkpoint đầu tiên).
- **US2 (P2)**: Độc lập test được qua URL trực tiếp, không cần US1.
- **US3 (P3)**: Độc lập test được qua URL trực tiếp; cần US2 tồn tại để link kết quả thực sự hữu ích khi demo full luồng (không chặn việc tự test US3).

### Parallel Opportunities

- T001 và T002 chạy song song (khác hệ thống: FE dependency vs BE schema).
- T004 và T005 chạy song song sau T001 (khác file).
- Backend implementation của 3 story (T006, T010, T013) có thể làm song song bởi các dev khác nhau — khác file, đều chỉ phụ thuộc T002+T003.
- Frontend page component của 3 story (T007, T011, T014) có thể làm song song — khác file.
- Việc sửa `App.tsx` (T008 → T012 → T015) **không** song song được — cùng file, phải theo đúng thứ tự đó.

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Hoàn thành Phase 1: Setup (T001-T002)
2. Hoàn thành Phase 2: Foundational (T003-T005) — **bắt buộc trước mọi story**
3. Hoàn thành Phase 3: User Story 1 (T006-T009)
4. **Dừng lại và kiểm chứng**: mở `/`, xác nhận Document List hoạt động độc lập
5. Đây đã là MVP demo được cho "thấy trong danh sách" — phần "mở xem text" cần thêm US2

### Incremental Delivery

1. Setup + Foundational xong → nền tảng sẵn sàng
2. Thêm US1 → test độc lập → demo Document List
3. Thêm US2 → test độc lập → demo cả "danh sách → click → đọc" (đúng luồng cuối Ngày 2 trong `docs/plan.md`)
4. Thêm US3 → test độc lập → demo thêm Search
5. Phase 6 Polish (lint/format + quickstart validation) trước khi coi feature "xong" theo Definition of Done

---

## Notes

- Đây là scaffold trên fixture (constitution MVP Phase Note) — không có task DB migration, không có task auth/RBAC.
- `App.tsx` là điểm nghẽn tuần tự duy nhất giữa 3 story (T008/T012/T015) — nếu nhiều người làm song song, cần merge/rebase cẩn thận ở file này.
- Không đánh dấu task nào có test — nếu sau này quyết định thêm test khi story được pick chính thức, bổ sung task test theo `AGENTS.md` (backend: `uv run pytest`; không có test FE trong stack hiện tại).
