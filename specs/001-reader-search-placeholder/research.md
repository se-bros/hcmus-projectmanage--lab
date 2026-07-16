# Phase 0 Research: Reader/Search Placeholder & Document List

## Decision: Thư viện routing frontend

**Decision**: Dùng `react-router-dom` (v6+), thêm vào `src/frontend/package.json`.

**Rationale**: Dự án hiện chưa có route nào (`App.tsx` chỉ là trang Vite mẫu, chưa có concept "trang"). `react-router-dom` là thư viện routing tiêu chuẩn cho React SPA, được chính `docs/06-architecture.md` ngầm giả định khi mô tả `pages/` (Dashboard, Editor, Reader) là các "trang" riêng biệt. Đây là lần đầu dự án cần routing nên phải quyết định ở đây thay vì để ngỏ.

**Alternatives considered**:
- Tự viết state-based "page switcher" (không dùng URL) — bị loại vì US2 yêu cầu mở thẳng URL Reader với `document_id` độc lập (Acceptance Scenario US2.1), cần URL thật có tham số.
- TanStack Router — mạnh hơn nhưng nặng hơn nhu cầu hiện tại (3 route tĩnh), không cần type-safe routing phức tạp cho placeholder.

## Decision: Nguồn dữ liệu fixture

**Decision**: Một module Python duy nhất `app/fixtures/documents.py` chứa list dict/dataclass cho danh sách document + nội dung text theo `document_id`, import trực tiếp vào 3 router (`documents.py`, `reader.py`, `search.py`).

**Rationale**: Constitution cho phép scaffold trên fixture; gom fixture vào 1 module để 3 router dùng chung tránh lặp dữ liệu giả ở nhiều nơi, và khi LDMS-002/026 thật thay bằng DB, chỉ cần đổi import trong router sang gọi `services`/`repositories` mà không đổi response schema.

**Alternatives considered**:
- File JSON tĩnh đọc từ đĩa — bị loại vì thêm I/O không cần thiết cho dữ liệu chỉ vài bản ghi, và Python module dễ type-check hơn (khớp "No `any`" trong Definition of Done).

## Decision: Search matching logic

**Decision**: So khớp substring không phân biệt hoa/thường (`keyword.lower() in content.lower()`) trên nội dung fixture, trả về document có match kèm 1 đoạn snippet ngắn quanh vị trí khớp đầu tiên.

**Rationale**: Spec US3 chỉ yêu cầu "lọc theo từ khóa", không yêu cầu ranking/relevance (đó là LDMS-015 PostgreSQL FTS thật). Substring match là đủ để demo UI Search mà không giả vờ có full-text search thật.

**Alternatives considered**:
- Regex/fuzzy match — over-engineering cho placeholder, không có yêu cầu tương ứng trong spec.

## Đã xác nhận từ `/speckit.clarify` (không cần research lại)

- Search xử lý ở backend qua `GET /search?q=` (không phải client-side filter).
- Reader và Search là 2 route độc lập (`/reader/:documentId`, `/search`), không gộp 1 trang.

Không còn mục nào `NEEDS CLARIFICATION` sau bước này.
