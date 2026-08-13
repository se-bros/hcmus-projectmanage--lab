---
description: "Task list for LDMS-021 — Highlight và ghi chú"
---

# Tasks: Highlight và ghi chú khi đọc sách (LDMS-021)

**Input**: Design documents from `/specs/003-highlight-and-notes/`
**Prerequisites**: `plan.md`, `spec.md`, `research.md`, `data-model.md`, `contracts/highlights-api.md`, `quickstart.md`

**Tests**: **CÓ**. Không phải mặc định của lệnh, mà vì `contracts/highlights-api.md` liệt kê rõ 14 contract test bắt buộc (T1–T14), và đây là story pick chính thức đủ AC nên Nguyên tắc III của constitution áp dụng đầy đủ — CI (`.github/workflows/ci.yml`) gate PR vào `develop` bất kể sao.

**Organization**: Nhóm theo user story để mỗi story giao được độc lập.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: chạy song song được (khác file, không phụ thuộc nhau)
- **[Story]**: US1 / US2 / US3

## Path Conventions

Web app hai thư mục: `src/backend/app/…` và `src/frontend/src/…` — theo mục Project Structure của `plan.md`.

---

## Phase 1: Setup

**Purpose**: Gỡ vật cản duy nhất trước khi làm được bất cứ việc gì với DB.

Feature này **không thêm dependency nào** ở cả frontend lẫn backend (epub.js đã có sẵn `annotations` API), và DB/auth/routing/test harness đều đã dựng từ các story trước. Nên Setup chỉ còn đúng một việc:

- [x] **T001** Tạo merge revision `src/backend/app/db/migrations/versions/20260812_0009_merge_heads.py` với `down_revision = ("20260717_0007", "20260721_0008")`, `upgrade()`/`downgrade()` để trống. Xác minh: `cd src/backend && uv run alembic heads` chỉ còn **một** head. Hiện đang có hai (đã xác nhận bằng lệnh này) nên `alembic upgrade head` đang báo lỗi — xem `research.md` R5.

**Checkpoint**: `alembic upgrade head` chạy được.

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Bảng, schema chung, khung service/router và fixture test — dùng chung cho cả 3 story.

**⚠️ CRITICAL**: Không story nào bắt đầu được trước khi phase này xong.

- [x] **T002** [P] Tạo model `Highlight` trong `src/backend/app/models/highlight.py` theo `data-model.md`: `id`, `document_id` (FK CASCADE, index), `user_sub` (index), `cfi_range`, `selected_text`, `note` (nullable), `created_at`, `updated_at`, cộng `Index("ix_highlights_document_user", "document_id", "user_sub")`. **KHÔNG** thêm `UniqueConstraint` — vùng chồng lấn phải tạo được (FR-004).
- [x] **T003** Export `Highlight` trong `src/backend/app/models/__init__.py` (import + thêm vào `__all__`). Bắt buộc, nếu không Alembic `--autogenerate` sẽ không thấy model. *(phụ thuộc T002)*
- [x] **T004** Tạo migration `src/backend/app/db/migrations/versions/20260812_0010_highlights.py`, `down_revision = "20260812_0009"`, đối xứng với `20260717_0007_bookmarks.py`. Xác minh: `uv run alembic upgrade head` rồi `\d highlights` thấy đúng index và FK CASCADE, không có unique constraint. *(phụ thuộc T001, T003)*
- [x] **T005** [P] Tạo `src/backend/app/schemas/highlight.py` với hằng `MAX_NOTE_LENGTH = 2000`, `MAX_SELECTED_TEXT_LENGTH = 5000` và schema `HighlightDetail` (không có trường `user_sub` — xem `contracts/highlights-api.md`).
- [x] **T006** [P] Tạo `src/backend/app/services/highlight_service.py` với helper dùng chung `_get_owned_highlight(db, document_id, highlight_id, user_sub)`: đặt điều kiện `user_sub` **trong mệnh đề `WHERE`** của `select()`, không tìm thấy thì `raise NotFoundError("Không tìm thấy đánh dấu.")`. Đây là điểm chốt của FR-012 — tuyệt đối không lấy bản ghi trước rồi mới `if` kiểm chủ sở hữu.
- [x] **T007** Tạo khung router `src/backend/app/api/highlights.py`: `APIRouter(prefix="/documents", tags=["highlights"])`, mọi endpoint dùng `Depends(get_current_user)` (**không** `get_optional_user` — FR-015). *(phụ thuộc T005, T006)*
- [x] **T008** Đăng ký `highlights.router` trong `src/backend/app/main.py` cạnh các router M6 hiện có. *(phụ thuộc T007)*
- [x] **T009** [P] Thêm fixture `reader_headers` và `second_reader_headers` vào `src/backend/tests/conftest.py` (hiện mới có `editor_headers`/`admin_headers`). Lưu ý `POST /auth/dev-token` sinh `sub` ngẫu nhiên mỗi lần gọi, nên hai fixture này tự nhiên là hai user khác nhau — đúng thứ cần cho test cô lập.
- [x] **T010** [P] Thêm type `Highlight` vào `src/frontend/src/services/api.ts` (`id`, `document_id`, `cfi_range`, `selected_text`, `note`, `created_at`, `updated_at`). **Không** đụng `src/frontend/src/services/documents.ts` — đó là client thời fixture đã chết.

**Checkpoint**: Bảng tồn tại, router đã mount (`/docs` thấy nhóm `highlights`), fixture test sẵn sàng. Ba story có thể chạy song song từ đây.

---

## Phase 3: User Story 1 — Tạo highlight cho đoạn văn đang đọc (P1) 🎯 MVP

**Goal**: Độc giả bôi đen một đoạn → đánh dấu → đoạn được tô ngay và còn nguyên sau khi reload.

**Independent Test**: Đăng nhập, mở `/reader/<id>` của một document đã publish, bôi đen và tạo highlight → tô ngay; F5 → còn đúng chỗ. Không cần chức năng ghi chú hay xóa.

### Tests for User Story 1

- [x] **T011** [P] [US1] `src/backend/tests/api/test_highlights.py` — luồng thuận: **T1** POST rồi GET trả đúng `cfi_range`/`selected_text`, **T2** GET khi chưa có gì trả `200` + mảng rỗng, **T13** hai highlight chồng lấn đều tạo được và GET trả 2 bản ghi, **T14** xóa document thì highlight bị xóa theo. T13 là test chống hồi quy cho quyết định "không unique constraint" — ai thêm ràng buộc unique cho giống `bookmarks` sẽ làm nó đỏ.
- [x] **T012** [P] [US1] `src/backend/tests/api/test_highlights.py` — nhánh từ chối: **T7** user B không thấy highlight của A, **T9** POST không token trả `401`, **T10** `selected_text` toàn khoảng trắng trả `422`, **T11** `cfi_range` vắt chương trả `422`, **T15** POST lên document `draft` trả `422` và không tạo bản ghi, **T16** highlight đã có vẫn GET/DELETE được sau khi document bị gỡ xuất bản. T15 và T16 phải cùng tồn tại — chỉ có T15 thì rất dễ bị "sửa cho nhất quán" thành áp `published` cho cả 4 endpoint, và khoá độc giả khỏi ghi chú của chính họ.

### Implementation for User Story 1

- [x] **T013** [US1] Thêm `HighlightCreate` vào `src/backend/app/schemas/highlight.py` với validator **V1** (`selected_text` strip không rỗng), **V2** (≤ 5.000 ký tự), **V3** (bắt đầu bằng `epubcfi(`), **V4** (phần chung trước dấu `,` đầu tiên phải chứa `!` → cùng một chương). Thông báo lỗi tiếng Việt theo bảng trong `contracts/highlights-api.md`.
- [x] **T014** [US1] Thêm `list_highlights` và `create_highlight` vào `src/backend/app/services/highlight_service.py`. **Cổng kiểm document (FR-001)**: cả hai hàm gọi `ensure_readable(get_document(db, document_id), user)`; riêng `create_highlight` kiểm thêm `if document.status != "published": raise ValidationError("Tài liệu chưa được xuất bản.")`. **Không** áp `published` cho đường đọc/sửa/xóa — highlight đã có phải sống sót khi document bị gỡ xuất bản, nếu không một vòng re-publish sẽ khoá độc giả khỏi ghi chú của chính họ. Xem bảng "Cổng kiểm document" trong `contracts/highlights-api.md`.
- [x] **T015** [US1] Thêm `GET` và `POST /documents/{document_id}/highlights` vào `src/backend/app/api/highlights.py` (POST trả `201`). *(phụ thuộc T013, T014)*
- [x] **T016** [P] [US1] Thêm `getHighlights(documentId)` và `createHighlight(documentId, payload)` vào `src/frontend/src/services/api.ts`.
- [x] **T017** [P] [US1] Tạo `src/frontend/src/components/HighlightPopover.tsx` — menu nổi hiện khi có vùng chọn, ở story này chỉ cần nút "Đánh dấu".
- [x] **T018** [US1] Nối vào `src/frontend/src/pages/ReaderPage.tsx`: bắt `rendition.on('selected', (cfiRange, contents) => …)` để mở popover và lấy `selected_text` từ `contents.window.getSelection()`; sau khi tạo thì `rendition.annotations.add('highlight', cfiRange, { id }, onClick, className, styles)`. Khi mở sách, gọi `getHighlights` rồi add lần lượt. *(phụ thuộc T016, T017)*
- [x] **T019** [US1] Tạo `src/frontend/src/components/HighlightSidebar.tsx` — danh sách mọi highlight, **tách hai nhóm**: dựng được, và "Đánh dấu không còn định vị được" (FR-011). Phân loại tại chỗ bằng `book.spine.get(cfi_range)` trả `null` hoặc `annotations.add` ném lỗi (`research.md` R4), hiển thị nhóm hỏng bằng `selected_text`. Sidebar là đường thao tác **chính thức và luôn đầy đủ** — bấm trực tiếp trên sách chỉ là lối tắt, vì khi nhiều vùng chồng khít thì cú bấm chỉ trúng annotation trên cùng. *(phụ thuộc T018)*
- [x] **T020** [P] [US1] Thêm style highlight vào `src/frontend/src/index.css`, gồm `mix-blend-mode: multiply` để phần giao của các vùng chồng lấn tự đậm hơn (FR-004), và style cho nhóm "không định vị được".
- [x] **T021** [P] [US1] Test FE: `HighlightPopover.test.tsx` (hiện popover khi có selection) và `ReaderPage.test.tsx` (chưa tồn tại — tạo mới; mock `services/api` và epub.js rendition, kiểm gọi `annotations.add` đúng số lần theo số highlight trả về).

**Checkpoint**: AC 1 xong. Đây là **mốc MVP** — dừng ở đây vẫn giao được giá trị thật: độc giả đánh dấu được đoạn quan trọng và thấy lại sau khi mở lại sách.

---

## Phase 4: User Story 2 — Gắn ghi chú vào highlight (P2)

**Goal**: Viết/sửa/gỡ ghi chú trên một highlight, đọc lại còn nguyên văn.

**Independent Test**: Trên một highlight đã có, nhập ghi chú → lưu → F5 → mở lại highlight đó → ghi chú hiện đúng. Không cần chức năng xóa highlight.

### Tests for User Story 2

- [x] **T022** [P] [US2] Bổ sung vào `src/backend/tests/api/test_highlights.py`: **T3** POST kèm note rồi GET thấy nguyên văn, **T4** PATCH đổi note thì nội dung mới thay cũ, **T5** PATCH `note: null` thì note về `null` nhưng highlight vẫn còn, **T12** note 2.001 ký tự trả `422` kèm số ký tự.

### Implementation for User Story 2

- [x] **T023** [US2] Thêm `HighlightNoteUpdate` vào `src/backend/app/schemas/highlight.py` với **V5** (≤ 2.000 ký tự, lỗi kèm số ký tự hiện tại) và **V6** (rỗng/toàn khoảng trắng → chuẩn hoá `NULL`). Áp V5 cho cả trường `note` của `HighlightCreate`.
- [x] **T024** [US2] Thêm `update_note` vào `src/backend/app/services/highlight_service.py`, dùng lại `_get_owned_highlight` từ T006.
- [x] **T025** [US2] Thêm `PATCH /documents/{document_id}/highlights/{highlight_id}` vào `src/backend/app/api/highlights.py`. Chỉ sửa ghi chú — `cfi_range` bất biến (`research.md` R6). *(phụ thuộc T023, T024)*
- [x] **T026** [P] [US2] Thêm `updateHighlightNote(documentId, highlightId, note)` vào `src/frontend/src/services/api.ts`.
- [x] **T027** [US2] Thêm ô nhập ghi chú vào `src/frontend/src/components/HighlightPopover.tsx` và `HighlightSidebar.tsx`: hiện "chưa có ghi chú" khi trống (US2 scenario 3), đếm ký tự còn lại khi gần 2.000 (FR-009), giữ nguyên nội dung đang gõ khi server trả `422` để người dùng tự cắt ngắn. *(phụ thuộc T026)*
- [x] **T028** [US2] Hiện ghi chú cho cả highlight trong nhóm "không còn định vị được" ở `HighlightSidebar.tsx` (FR-011a) — đây là lý do tồn tại của quyết định giữ bản ghi thay vì xóa. *(phụ thuộc T027)*
- [x] **T029** [P] [US2] Test FE: sửa/gỡ ghi chú, hiện cảnh báo khi vượt 2.000 ký tự, và hai highlight chồng lấn hiện đúng ghi chú của từng cái (US2 scenario 8).

**Checkpoint**: AC 1 + AC 2 xong, mỗi cái vẫn kiểm độc lập được.

---

## Phase 5: User Story 3 — Xóa highlight không cần nữa (P3)

**Goal**: Xóa một highlight; nó biến mất ngay và không quay lại sau reload.

**Independent Test**: Tạo highlight → xóa → mất ngay → F5 → vẫn không có. Chỉ cần chức năng tạo của US1.

### Tests for User Story 3

- [x] **T030** [P] [US3] Bổ sung vào `src/backend/tests/api/test_highlights.py`: **T6** DELETE rồi GET không còn trong danh sách, **T8** user B gọi PATCH/DELETE lên highlight của A trả `404` và bản ghi của A còn nguyên (`404` chứ không phải `403` — `403` gián tiếp xác nhận id đó có tồn tại), **T17** PATCH/DELETE lên highlight của **chính mình** đã bị xóa trước đó trả `404`, không lỗi hệ thống (edge case "highlight đã bị xóa ở tab khác" — khác T8 ở chỗ đây là bản ghi của chính user, không phải của người khác).

### Implementation for User Story 3

- [x] **T031** [US3] Thêm `delete_highlight` vào `src/backend/app/services/highlight_service.py`, dùng lại `_get_owned_highlight`.
- [x] **T032** [US3] Thêm `DELETE /documents/{document_id}/highlights/{highlight_id}` trả `204` không body vào `src/backend/app/api/highlights.py`. *(phụ thuộc T031)*
- [x] **T033** [P] [US3] Thêm `deleteHighlight(documentId, highlightId)` vào `src/frontend/src/services/api.ts`.
- [x] **T034** [US3] Thêm thao tác xóa vào `HighlightPopover.tsx` và `HighlightSidebar.tsx`; gọi `rendition.annotations.remove(cfiRange, 'highlight')` để gỡ khỏi trang ngay. Xóa được **cả** bản ghi trong nhóm "không còn định vị được" (FR-011b) — nhóm này không có annotation để gỡ nên chỉ cập nhật danh sách. *(phụ thuộc T033)*
- [x] **T035** [P] [US3] Test FE: xóa highlight ngoài thì highlight chồng lấn bên trong còn nguyên kèm ghi chú (US3 scenario 7), và xóa được bản ghi trong nhóm hỏng.

**Checkpoint**: Cả 3 AC xong, mỗi story vẫn độc lập kiểm được.

---

## Phase 6: Polish & Cross-Cutting

- [ ] **T036** Chạy kịch bản FR-011 ở `quickstart.md` §4: tạo highlight + ghi chú, publish lại document để sinh EPUB có cấu trúc chương khác, mở lại Reader. Kỳ vọng **SC-008**: đếm số bản ghi trước và sau bằng nhau — không mất bản ghi nào, ghi chú còn nguyên trong nhóm "không định vị được". Đây là hành vi không có test tự động nào phủ được (cần EPUB thật), nên phải kiểm tay.
- [ ] **T037** Kiểm hai tiêu chí hiệu năng: **SC-006** — tạo 50 highlight trên một document, đo thời điểm sách đọc được so với khi không có highlight nào, chênh lệch phải < 1s (nếu trượt, nghi can đầu tiên là số lần gọi `annotations.add` lúc mở sách ở T018); **SC-005** — đo từ lúc thả chuột hết vùng chọn tới lúc thấy đoạn được tô, phải < 3s và không rời khỏi trang đang đọc.
- [ ] **T040** Kiểm **FR-014 + FR-005a** theo `quickstart.md` §4 bước 6: tạo một highlight trải qua nhiều trang trong cùng một chương, rồi bấm `A+`/`A−` đổi cỡ chữ để nội dung dàn lại trang — highlight phải bám đúng đoạn văn cũ, không trôi sang đoạn khác (US1 scenario 9). Đây là điểm dễ vỡ nhất của feature: CFI range gặp text reflow thì hoặc đúng, hoặc hỏng thầm lặng mà không báo lỗi gì. Không test tự động nào phủ được vì cần EPUB thật render trong trình duyệt.
- [x] **T038** Chạy đủ gate trước khi mở PR: `cd src/backend && uv run ruff format . && uv run ruff check . && uv run pytest`; `cd src/frontend && npm run format && npm run lint && npm test`.
- [ ] **T039** Trong mô tả PR, nêu rõ merge revision ở T001 là **dọn nợ có sẵn** (`20260717_0007` và `20260721_0008` cùng tách nhánh từ `20260716_0005` từ trước feature này), để reviewer không nhầm là thay đổi ngoài phạm vi.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (T001)**: không phụ thuộc gì, làm đầu tiên — chặn mọi việc liên quan migration.
- **Foundational (T002–T010)**: phụ thuộc T001 (riêng T004). **Chặn cả 3 story.**
- **US1 (T011–T021)**: sau Foundational. Không phụ thuộc story nào khác.
- **US2 (T022–T029)**: sau Foundational. Về mặt code độc lập với US1, nhưng để **kiểm** thủ công thì cần một highlight có sẵn (do US1 tạo, hoặc bằng `curl` như `quickstart.md` §3).
- **US3 (T030–T035)**: sau Foundational. Cùng ghi chú như US2. Riêng T034 đụng chung file với T027 (`HighlightPopover.tsx`, `HighlightSidebar.tsx`) → nếu US2 và US3 chạy song song thì hai file này phải phối hợp, đây là điểm xung đột file duy nhất giữa các story.
- **Polish (T036–T039)**: sau khi các story cần giao đã xong.

### Within Each User Story

Test viết trước và phải **đỏ** trước khi code → schema → service → endpoint → client FE → UI. Backend xong trước FE trong cùng story vì FE gọi thẳng endpoint thật.

### Parallel Opportunities

- Foundational: T002, T005, T006, T009, T010 chạy song song được (khác file). T003 → T004 và T007 → T008 là chuỗi.
- Trong US1: T011 ∥ T012 (viết test), rồi T016 ∥ T017 ∥ T020 sau khi backend xong.
- Ba story chạy song song được nếu đủ người, **trừ** lưu ý xung đột file T027/T034 ở trên.

---

## Implementation Strategy

### MVP trước (chỉ US1)

1. T001 → `alembic upgrade head` chạy được.
2. T002–T010 → nền sẵn sàng.
3. T011–T021 → US1 xong.
4. **DỪNG VÀ KIỂM**: chạy `quickstart.md` §4 bước 1–2 và bước 5 (chồng lấn), 6 (đổi cỡ chữ).
5. Demo được: độc giả đánh dấu và thấy lại sau reload.

### Giao tăng dần

US1 (AC 1) → kiểm → demo · US2 (AC 2) → kiểm → demo · US3 (AC 3) → kiểm → demo. Mỗi bước thêm giá trị mà không phá bước trước.

### Nếu chia người

Sau Foundational: một người US1 (nặng nhất, 11 task, chứa toàn bộ phần epub.js khó), một người US2 + US3 (cùng đụng `HighlightPopover.tsx`/`HighlightSidebar.tsx` nên gộp cho một người là gọn nhất, tránh đúng điểm xung đột file duy nhất).

---

## Notes

- `[P]` = khác file, không phụ thuộc nhau.
- Commit sau mỗi task hoặc mỗi nhóm hợp lý.
- Ba cái bẫy đã biết, nhắc lại cho khỏi mất thời gian debug:
  - `POST /auth/dev-token` sinh `sub` **ngẫu nhiên mỗi lần gọi** — gọi lại là thành user khác và highlight "biến mất". Lưu token dùng lại (`quickstart.md` §3).
  - Bảng `highlights` **cố ý không** có unique constraint, khác `bookmarks`. Thêm vào là phá FR-004; T013 sẽ bắt được.
  - Kiểm `status == "published"` **cố ý chỉ** áp cho đường tạo, không áp cho đọc/sửa/xóa. Trông như thiếu sót nhưng là có chủ ý: áp cho cả 4 endpoint sẽ khoá độc giả khỏi ghi chú của chính họ mỗi khi thủ thư gỡ xuất bản tài liệu. T16 sẽ bắt được.
