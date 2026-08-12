# Implementation Plan: Highlight và ghi chú khi đọc sách (LDMS-021)

**Branch**: `003-highlight-and-notes` | **Date**: 2026-08-12 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/003-highlight-and-notes/spec.md`

## Summary

Cho phép độc giả đã đăng nhập bôi đen một đoạn văn trong trình đọc EPUB, đánh dấu đoạn đó, gắn một ghi chú tùy chọn, và xóa khi không cần. Dữ liệu riêng tư theo cặp `(document_id, user_sub)` — mở rộng đúng khuôn mẫu LDMS-020 (Bookmark) đã có sẵn.

**Cách tiếp cận kỹ thuật**: một bảng `highlights` mới lưu vùng đánh dấu dưới dạng **EPUB CFI range** (cùng họ định vị mà `bookmarks.location` đang dùng), kèm bản sao đoạn text đã chọn và ghi chú. Phía client dùng API sẵn có của epub.js — `rendition.on('selected')` để bắt vùng chọn và `rendition.annotations.add('highlight', ...)` để tô — nên không cần thêm thư viện nào. Bốn endpoint CRUD thuần, không có tác vụ nặng, không đụng tới đường đọc file gốc.

Ba quyết định từ `/speckit.clarify` định hình thiết kế:
- **FR-004** (chồng lấn tự do) → bảng **không** có unique constraint trên vùng; mỗi highlight là một bản ghi độc lập.
- **FR-005b** (một highlight nằm gọn trong một chương) → epub.js render mỗi spine item trong một iframe riêng nên vùng chọn của trình duyệt **không thể** vắt qua chương; ràng buộc được thoả về mặt cấu trúc, vẫn kiểm lại ở server.
- **FR-011** (giữ bản ghi khi vị trí hỏng) → **không** thêm cột trạng thái vào DB; việc một CFI còn dựng lại được hay không là thuộc tính của bản EPUB *hiện tại*, chỉ client mới biết, nên phân loại xảy ra ở client lúc render.

## Technical Context

**Language/Version**: Python 3.11 (backend, quản lý bằng `uv`) · TypeScript 5.x + React 18 (frontend, Vite)
**Primary Dependencies**: FastAPI, SQLAlchemy 2.0 (`Mapped`/`mapped_column`), Alembic, Pydantic v2 · epubjs 0.3.93, react-router — **không thêm dependency mới ở cả hai phía**
**Storage**: PostgreSQL 16 — một bảng mới `highlights`. Không đụng MinIO.
**Testing**: `pytest` với SQLite in-memory qua fixture `api_context` (`src/backend/tests/conftest.py`) · Vitest + Testing Library cho frontend
**Target Platform**: Web (Docker Compose, trình duyệt desktop)
**Project Type**: Web application — frontend + backend tách thư mục
**Performance Goals**: SC-005 thao tác tạo highlight hoàn tất < 3s · SC-006 tải kèm 50 highlight không làm chậm thời điểm đọc được sách quá 1s
**Constraints**: Ghi chú ≤ 2.000 ký tự (FR-009) · highlight nằm trong một chương (FR-005b) · dữ liệu cô lập theo `user_sub` (FR-012) · không tự động re-anchor (FR-011c)
**Scale/Scope**: 4 endpoint mới, 1 bảng mới, 1 migration (kèm merge — xem bên dưới), 1 trang FE sửa + 2 component mới. Ước lượng ~50 highlight/document là ngưỡng thiết kế.

**Ràng buộc phát sinh — đồ thị Alembic đang có hai head.** `20260717_0007_bookmarks` và `20260721_0006_users` cùng có `down_revision = "20260716_0005"`, tạo hai nhánh song song kết thúc ở `20260717_0007` và `20260721_0008`. Đây là nợ kỹ thuật có sẵn từ trước, không do feature này gây ra, nhưng nó chặn việc thêm migration mới: `alembic upgrade head` sẽ báo "multiple heads". Xem `research.md` mục R5 để biết cách xử lý đã chọn.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-checked after Phase 1 design.*

Đối chiếu từng nguyên tắc trong `.specify/memory/constitution.md` (v1.2.0):

| Nguyên tắc | Kết quả | Ghi chú |
| :--- | :--- | :--- |
| **I. Layering** | ✅ PASS | Tách đúng `models/highlight.py` → `schemas/highlight.py` → `services/highlight_service.py` → `api/highlights.py`, một file cho mỗi entity theo đúng mục Development Workflow. FE tách `services/api.ts` (gọi API) khỏi `components/` (UI). |
| **II. Clear Contracts** | ✅ PASS | Đây là story pick chính thức đủ AC nên áp dụng đầy đủ: mọi endpoint có schema Pydantic trong `schemas/highlight.py`, mọi lỗi ném qua `AppError` (`NotFoundError`/`ValidationError`/`UnauthorizedError`), không dùng `JSONResponse` thủ công. |
| **III. Test & Lint** | ✅ PASS | Story đủ AC → chạy `ruff format`/`ruff check`/`pytest` và `npm run format`/`npm run lint` trước khi mở PR vào `develop`. CI (`.github/workflows/ci.yml`) gate PR nên đằng nào cũng bắt buộc. |
| **IV. File Security** | ✅ PASS — có lưu ý | Feature **không** mở thêm đường truy cập file: không endpoint tải file mới, không object key mới, đường đọc EPUB vẫn nguyên Signed URL 15 phút qua `reader_service.get_reader_content`. Xem lưu ý bên dưới về `selected_text`. |
| **V. Background Work** | ✅ PASS (N/A) | Toàn bộ thao tác là CRUD một bản ghi, không OCR/Pandoc, không tác vụ nặng — không cần `BackgroundTasks`. |

**Lưu ý cho Nguyên tắc IV (đã xử lý trong thiết kế, không phải vi phạm):** cột `selected_text` (FR-003) lưu một bản sao nội dung sách trong DB — về nguyên tắc đây là một kênh chứa nội dung có bản quyền nằm *ngoài* đường Signed URL. Rủi ro được chặn bằng bốn biện pháp, xem `data-model.md` và `contracts/highlights-api.md`:
1. Giới hạn `selected_text` ≤ 5.000 ký tự/bản ghi, từ chối ở tầng schema — không thể dùng để mirror cả cuốn sách.
2. Chỉ đọc lại được bởi đúng user đã tạo (FR-012); không có endpoint nào trả highlight của người khác.
3. Chỉ chứa đúng phần độc giả tự bôi đen trên nội dung mà họ **đã** có quyền đọc — không mở rộng quyền sẵn có.
4. **Cổng kiểm document**: mọi endpoint chạy `ensure_readable(...)`, và đường tạo kiểm thêm `status == "published"` — endpoint highlights không được vòng qua cổng kiểm mà `reader_service.get_reader_content` đang áp cho đường đọc. Thiếu bước này thì một reader đã đăng nhập có thể gọi thẳng API để ghi `selected_text` của document `draft` họ không có quyền đọc, và biện pháp 3 mất hiệu lực. Kiểm `published` **chỉ** áp cho đường tạo — chi tiết và lý do ở `contracts/highlights-api.md`.

**Kết quả: PASS, không có vi phạm** → mục Complexity Tracking để trống.

**Re-check sau Phase 1**: thiết kế ở `data-model.md` / `contracts/` giữ nguyên 5 kết quả trên. Điểm duy nhất đáng nhắc lại là quyết định truy vấn DB thẳng trong service (`select()`) thay vì thêm `repositories/highlight_repository.py` — đây là **bám theo tiền lệ `bookmark_service.py`** đang chạy trong `develop`, và Nguyên tắc I ưu tiên "match existing style". Không tính là vi phạm; nếu sau này team thống nhất chuẩn hoá repository layer thì làm đồng loạt cho cả M6 chứ không lệch riêng feature này.

## Project Structure

### Documentation (this feature)

```text
specs/003-highlight-and-notes/
├── plan.md              # File này
├── research.md          # Phase 0 — 6 quyết định kỹ thuật
├── data-model.md        # Phase 1 — bảng highlights
├── quickstart.md        # Phase 1 — cách chạy & kiểm thử tay
├── contracts/
│   └── highlights-api.md   # Phase 1 — 4 endpoint + schema
└── tasks.md             # Do /speckit.tasks sinh ra — KHÔNG tạo ở bước này
```

### Source Code (repository root)

```text
src/backend/
├── app/
│   ├── api/
│   │   └── highlights.py              # MỚI — 4 endpoint CRUD
│   ├── models/
│   │   ├── highlight.py               # MỚI — bảng highlights
│   │   └── __init__.py                # SỬA — export Highlight (bắt buộc cho Alembic autogenerate)
│   ├── schemas/
│   │   └── highlight.py               # MỚI — HighlightCreate/NoteUpdate/HighlightDetail
│   ├── services/
│   │   └── highlight_service.py       # MỚI — nghiệp vụ + lọc theo user_sub
│   ├── db/migrations/versions/
│   │   ├── 20260812_0009_merge_heads.py    # MỚI — gộp 2 head có sẵn (xem R5)
│   │   └── 20260812_0010_highlights.py     # MỚI — tạo bảng highlights
│   └── main.py                        # SỬA — include_router(highlights.router)
└── tests/
    └── api/
        └── test_highlights.py         # MỚI — phủ AC 1/2/3 + cô lập user + ràng buộc chương

src/frontend/
└── src/
    ├── services/
    │   └── api.ts                     # SỬA — type Highlight + 4 hàm gọi API
    ├── components/
    │   ├── HighlightPopover.tsx       # MỚI — menu nổi khi bôi đen + ô nhập ghi chú
    │   ├── HighlightPopover.test.tsx  # MỚI
    │   ├── HighlightSidebar.tsx       # MỚI — danh sách highlight + nhóm "không định vị được"
    │   └── HighlightSidebar.test.tsx  # MỚI
    ├── pages/
    │   ├── ReaderPage.tsx             # SỬA — nối epub.js annotations + 2 component trên
    │   └── ReaderPage.test.tsx        # MỚI (hiện chưa có test cho trang này)
    └── index.css                      # SỬA — style highlight, mix-blend-mode cho vùng chồng lấn
```

**Structure Decision**: Giữ nguyên cấu trúc web app hai thư mục `src/backend` + `src/frontend` đã có, phân lớp theo kỹ thuật đúng Nguyên tắc I. Feature này là phần mở rộng của Module M6 (Reader) nên mọi file mới nằm cạnh file M6 sẵn có. Router tách thành `api/highlights.py` thay vì nhồi vào `api/reader.py` để không biến file M6 thành file gom tất cả — nhất quán với cách `api/` đang tách theo từng nhóm nghiệp vụ (`auth`, `editor`, `metadata`, `publish`…).

Hai điểm cần biết trước khi code:
- `src/frontend/src/services/documents.ts` là client thời fixture của spec `001`, **không** phải client thật đang chạy. Client thật là `services/api.ts`. Không đụng vào `documents.ts`.
- Hiện **chưa có** `tests/api/test_reader.py` — nhánh bookmark/reader chưa có test ở tầng API. Feature này thêm `test_highlights.py` cho phần của mình; việc bổ sung test cho bookmark nằm ngoài phạm vi, chỉ nêu ra để team biết.

## Complexity Tracking

> Constitution Check đạt toàn bộ, không có vi phạm cần biện minh. Bảng này để trống.
