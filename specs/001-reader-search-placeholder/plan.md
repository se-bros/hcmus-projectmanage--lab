# Implementation Plan: Reader/Search Placeholder & Document List (prep cho LDMS-008, LDMS-026)

**Branch**: `001-reader-search-placeholder` | **Date**: 2026-07-16 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `specs/001-reader-search-placeholder/spec.md`

## Summary

Dựng khung 2 trang FE (Document List, Reader placeholder) + 1 trang FE Search placeholder, cùng 3 endpoint backend fixture-backed (`GET /documents`, `GET /reader/{document_id}`, `GET /search`) để có một luồng click-through demo được (danh sách → click → đọc / tìm kiếm → click → đọc) trong Ngày 1-2 của sprint MVP, không phụ thuộc DB/MinIO/OCR thật. Dữ liệu nguồn là fixture tĩnh trong backend.

## Technical Context

**Language/Version**: Python 3.11 (`uv`) cho backend; TypeScript 6 + React 19 (Vite 8) cho frontend.
**Primary Dependencies**: Backend — FastAPI (đã có `app/api/documents.py`, `app/api/reader.py`, `app/api/search.py` dạng router rỗng, đã được `app/main.py` include sẵn); Pydantic cho response schema. Frontend — React 19; **cần thêm `react-router-dom`** (chưa có trong `package.json`, dự án chưa có routing lib nào) để dựng 2 route `/reader/:documentId` và `/search` cộng route danh sách mặc định `/`.
**Storage**: Không dùng PostgreSQL/MinIO ở bước này — dữ liệu là fixture tĩnh (module Python) trong backend, trả thẳng qua API. Việc này khớp với `constitution.md` Principle I/II (chấp nhận scaffold trên fixture khi story chưa được pick chính thức).
**Testing**: `uv run pytest` có sẵn (`tests/api/test_health.py` làm mẫu) — theo Principle III của constitution, test không bắt buộc ở bước scaffolding fixture, nên feature này **không** viết test mới, trừ khi review sau này yêu cầu.
**Target Platform**: Web (SPA phục vụ qua Vite dev server / Nginx theo `docs/06-architecture.md` §6); backend chạy trong Docker Compose (API + Postgres + MinIO) nhưng feature này không cần Postgres/MinIO chạy được vẫn hoạt động vì dùng fixture.
**Project Type**: Web application (frontend `src/frontend` + backend `src/backend`, đã có sẵn theo cấu trúc `docs/06-architecture.md` §7).
**Performance Goals**: Không áp dụng ở mức đo lường (đây là placeholder nội bộ, không phải luồng production) — chỉ cần phản hồi tức thời vì toàn bộ là in-memory fixture.
**Constraints**: Không được thêm Elasticsearch/Celery/Redis (constitution: "Do not silently add ... roadmap items"). Không cần auth/RBAC thật ở bước này (đã ghi trong spec Assumptions) — nhưng cũng không được serve file gốc/EPUB thật qua route này (Principle IV không áp dụng vì chưa chạm file thật).
**Scale/Scope**: 3 endpoint backend, 3 trang/route frontend, 1 module fixture dữ liệu dùng chung. Không có migration DB.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-checked after Phase 1 design.*

| Principle | Trạng thái | Ghi chú |
|---|---|---|
| I. Layering (định hướng, không cứng nhắc khi MVP) | **PASS (miễn trừ scaffold)** | Đây là dựng khung trên fixture, một người code cả 2 lớp — constitution cho phép. Vẫn tổ chức đúng thư mục `api/` cho router, không nhét business logic linh tinh. |
| II. Clear Contracts khi story được pick chính thức | **PASS (miễn trừ)** | LDMS-008/026 chưa được pick chính thức (full AC) — đây chỉ là scaffold đọc fixture, không có Pydantic schema đầy đủ là chấp nhận được, nhưng vẫn dùng `response_model` cơ bản cho rõ ràng (xem `contracts/`). |
| III. Test & Lint bắt buộc trước khi merge `develop` | **PASS (miễn trừ khi scaffold fixture)** | Không viết test mới cho fixture endpoints; **vẫn chạy** `uv run ruff format .`, `uv run ruff check .` (backend) và `npm run format`, `npm run lint` (frontend) trước khi coi task hoàn thành, vì đây là yêu cầu universal của `AGENTS.md`/`CLAUDE.md`, tách biệt với gate "trước khi merge develop" của constitution. |
| IV. File Security non-negotiable | **PASS — không áp dụng** | Feature này không serve file gốc/EPUB thật, không tạo Signed URL nào. Không vi phạm vì không chạm vào phạm vi của principle này. |
| V. Heavy work chạy background | **PASS — không áp dụng** | Không có OCR/EPUB compile trong scope này; tất cả endpoint đọc fixture in-memory, đồng bộ, cực nhanh. |

**Kết luận**: Không có vi phạm nào cần biện minh trong Complexity Tracking.

## Project Structure

### Documentation (this feature)

```text
specs/001-reader-search-placeholder/
├── plan.md              # This file
├── research.md          # Phase 0 output
├── data-model.md         # Phase 1 output
├── quickstart.md        # Phase 1 output
├── contracts/           # Phase 1 output
│   ├── get-documents.md
│   ├── get-reader-document.md
│   └── get-search.md
└── tasks.md             # Phase 2 output (/speckit.tasks — not created here)
```

### Source Code (repository root)

```text
src/backend/
├── app/
│   ├── api/
│   │   ├── documents.py      # [MODIFY] thêm GET /documents (fixture list)
│   │   ├── reader.py         # [MODIFY] thêm GET /reader/{document_id} (fixture content)
│   │   └── search.py         # [MODIFY] thêm GET /search?q= (fixture filter)
│   ├── schemas/
│   │   └── document.py       # [NEW] Pydantic: DocumentSummary, DocumentContent, SearchResult
│   └── fixtures/
│       └── documents.py      # [NEW] dữ liệu fixture tĩnh: danh sách document + nội dung text

src/frontend/
├── package.json               # [MODIFY] thêm dependency react-router-dom
├── src/
│   ├── main.tsx                # [MODIFY] bọc BrowserRouter
│   ├── App.tsx                 # [MODIFY] khai báo <Routes> cho 3 trang
│   ├── pages/
│   │   ├── DocumentListPage.tsx   # [NEW] route "/"
│   │   ├── ReaderPage.tsx         # [NEW] route "/reader/:documentId"
│   │   └── SearchPage.tsx         # [NEW] route "/search"
│   └── services/
│       └── documents.ts           # [NEW] hàm gọi GET /documents, /reader/{id}, /search
```

**Structure Decision**: Web application 2 thư mục (`src/backend`, `src/frontend`) đã có sẵn theo `docs/06-architecture.md` §7 — không tạo cấu trúc mới. Backend chỉ **thêm code vào router rỗng đã tồn tại** (`documents.py`, `reader.py`, `search.py`) thay vì tạo file mới, đúng ranh giới module đã được scaffold sẵn theo owner (`Khoa Nguyễn` — xem docstring đầu mỗi file). Fixture data tách thành `app/fixtures/documents.py` riêng (không lẫn vào `api/`) để dễ thay bằng truy vấn DB thật sau này mà không đổi router. Frontend thêm `pages/*.tsx` theo đúng layering đã định trong kiến trúc (`components/`, `pages/`, `services/`), và cần bổ sung `react-router-dom` — quyết định này được ghi lại ở `research.md`.

## Complexity Tracking

*Không có vi phạm nào cần biện minh — bảng để trống.*
