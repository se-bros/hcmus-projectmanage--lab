# Feature Specification: Reader/Search Placeholder & Document List (prep cho LDMS-008, LDMS-026)

**Feature Branch**: `001-reader-search-placeholder`  
**Created**: 2026-07-16  
**Status**: Draft  
**Input**: User description: "Chuẩn bị cho LDMS-008 và LDMS-026 | Trang Reader/Search placeholder đọc text thô từ fixture; danh sách tài liệu tạm thời gọi `GET /documents`."

**Bối cảnh (không phải yêu cầu implementation nhưng cần để hiểu scope)**: Đây là việc **dựng khung** (scaffold) cho Ngày 1–2 của sprint MVP (`docs/plan.md` mục 3, hàng "Khoa Nguyễn"), **chưa phải** là pick chính thức LDMS-008 (Đọc EPUB — cần LDMS-007 xong) hay LDMS-026 (Document List đủ AC — cần LDMS-002/006 xong). Mục tiêu là có một luồng **click-through demo được** (danh sách → mở đọc) chạy trên dữ liệu giả (fixture), theo đúng tinh thần Constitution "MVP Phase Note": ưu tiên luồng end-to-end chạy được trước, AC đầy đủ và test làm sau khi story được pick chính thức.

## User Scenarios & Testing *(mandatory)*

<!--
  IMPORTANT: User stories should be PRIORITIZED as user journeys ordered by importance.
  Each user story/journey must be INDEPENDENTLY TESTABLE - meaning if you implement just ONE of them,
  you should still have a viable MVP (Minimum Viable Product) that delivers value.
  
  Assign priorities (P1, P2, P3, etc.) to each story, where P1 is the most critical.
  Think of each story as a standalone slice of functionality that can be:
  - Developed independently
  - Tested independently
  - Deployed independently
  - Demonstrated to users independently
-->

### User Story 1 - Xem danh sách tài liệu (Priority: P1)

Là biên tập viên/độc giả, tôi muốn mở trang danh sách tài liệu để thấy các tài liệu đã có trong hệ thống (tên, trạng thái, ngày tạo) và chọn một tài liệu để mở đọc.

**Why this priority**: Đây là điểm vào của toàn bộ luồng demo Ngày 2 ("đóng gói → upload → thấy trong danh sách → mở xem"). Không có danh sách thì không có gì để bấm vào Reader/Search cả — phải làm trước.

**Independent Test**: Gọi `GET /documents` (backend trả về dữ liệu fixture tạm thời, chưa cần nối MinIO/DB thật) và render ra bảng/list trên FE. Test độc lập được bằng cách seed vài bản ghi fixture rồi mở trang, không phụ thuộc Reader/Search.

**Acceptance Scenarios**:

1. **Given** `GET /documents` trả về ≥ 1 tài liệu (fixture), **When** mở trang danh sách, **Then** thấy bảng/list hiển thị tên, status, ngày tạo cho từng tài liệu.
2. **Given** đang ở trang danh sách, **When** click vào một tài liệu, **Then** điều hướng sang trang Reader placeholder với đúng `document_id`.
3. **Given** `GET /documents` trả về mảng rỗng, **When** mở trang danh sách, **Then** hiển thị trạng thái rỗng rõ ràng (không phải màn trắng/lỗi).

---

### User Story 2 - Đọc thử nội dung tài liệu (Reader placeholder) (Priority: P2)

Là độc giả, tôi muốn mở một tài liệu từ danh sách và thấy nội dung text thô của nó (dữ liệu giả từ fixture), để hình dung trải nghiệm đọc trước khi luồng OCR/EPUB thật (LDMS-007/008) sẵn sàng.

**Why this priority**: Là bước kế tiếp tự nhiên sau danh sách, dựng khung UI/route cho LDMS-019 (tùy chỉnh giao diện đọc) làm sớm mà không cần chờ EPUB thật, đúng như `docs/plan.md` dòng LDMS-019 "không phụ thuộc EPUB thật, làm sớm trên khung Reader placeholder".

**Independent Test**: Mở trực tiếp URL Reader với một `document_id` có trong fixture text và xác nhận nội dung text hiển thị đúng, không cần đi qua trang danh sách.

**Acceptance Scenarios**:

1. **Given** `document_id` có trong fixture text, **When** mở trang Reader, **Then** hiển thị nội dung text thô tương ứng.
2. **Given** `document_id` không tồn tại trong fixture, **When** mở trang Reader, **Then** hiển thị thông báo "không tìm thấy tài liệu", không phải màn trắng hay lỗi console không xử lý.

---

### User Story 3 - Tìm kiếm thử trên dữ liệu giả (Search placeholder) (Priority: P3)

Là độc giả, tôi muốn nhập từ khóa vào ô tìm kiếm và thấy các tài liệu fixture có chứa từ khóa đó, để dựng khung UI Search trước khi Postgres FTS thật (LDMS-015) sẵn sàng.

**Why this priority**: Giá trị thấp hơn 2 story trên vì Search thật (LDMS-015/016) phụ thuộc LDMS-004/011 chưa xong; ở đây chỉ cần khung UI + lọc naive trên fixture để không chặn thiết kế UI sau này.

**Independent Test**: Nhập một từ khóa có/không xuất hiện trong fixture text và xác nhận kết quả lọc đúng, độc lập với danh sách tài liệu và Reader.

**Acceptance Scenarios**:

1. **Given** từ khóa xuất hiện trong ≥ 1 fixture, **When** submit tìm kiếm, **Then** thấy danh sách kết quả khớp, mỗi kết quả bấm vào mở được Reader placeholder của tài liệu đó.
2. **Given** từ khóa không khớp fixture nào, **When** submit tìm kiếm, **Then** hiển thị "không có kết quả", không lỗi.
3. **Given** ô tìm kiếm để trống hoặc chỉ khoảng trắng, **When** submit, **Then** hệ thống xử lý nhất quán (trả rỗng hoặc không submit) — không crash.

### Edge Cases

- `GET /documents` lỗi/không phản hồi (backend down) → FE hiển thị lỗi thân thiện, không màn trắng.
- `document_id` trong URL Reader sai định dạng hoặc không tồn tại trong fixture → thông báo rõ ràng (US2, AC2).
- Danh sách tài liệu rỗng (chưa upload gì) → trạng thái rỗng, không lỗi (US1, AC3).
- Từ khóa tìm kiếm rỗng/toàn khoảng trắng → xử lý nhất quán, không lỗi server/console (US3, AC3).
- Đây là placeholder: không cần xử lý phân trang, không cần auth/RBAC thật ở bước này (RBAC thật sẽ áp dụng khi LDMS-026/008 được pick chính thức với đủ AC).

## Requirements *(mandatory)*

<!--
  ACTION REQUIRED: The content in this section represents placeholders.
  Fill them out with the right functional requirements.
-->

### Functional Requirements

- **FR-001**: Backend MUST expose `GET /documents` trả về danh sách tài liệu (tên, status, ngày tạo, id) — nguồn dữ liệu là fixture tĩnh cho bước này, chưa cần nối PostgreSQL/MinIO thật.
- **FR-002**: FE MUST có trang Document List gọi `GET /documents` và render bảng/list; mỗi dòng dẫn tới trang Reader placeholder theo `document_id`.
- **FR-003**: FE MUST có trang Reader placeholder nhận `document_id`, hiển thị nội dung text thô đọc từ fixture (không phải EPUB thật — Epub.js/MinIO signed URL sẽ vào ở LDMS-008 chính thức).
- **FR-004**: Backend MUST expose một endpoint tạm `GET /search?q=<keyword>` trả về danh sách tài liệu fixture có nội dung khớp từ khóa (không cần Postgres FTS thật — vẫn là fixture-backed, kiến trúc gần giống LDMS-015 thật sau này để đỡ phải viết lại). FE MUST có trang Search placeholder gọi endpoint này và hiển thị kết quả.
- **FR-005**: System MUST xử lý 3 trạng thái rỗng/lỗi mà không crash: danh sách rỗng, document_id không tồn tại, từ khóa không khớp (xem Edge Cases).
- **FR-006**: Routing FE MUST tách thành 2 route độc lập — `/reader/:documentId` (Reader placeholder) và `/search` (Search placeholder, kết quả dẫn sang `/reader/:documentId` khi click) — không gộp chung 1 trang, để mỗi trang test/triển khai độc lập được và path không đổi khi LDMS-008/026 chính thức implement đầy đủ.

*Ghi chú phạm vi (không phải NEEDS CLARIFICATION — đã xác nhận qua `docs/plan.md`/constitution MVP note):*
- Chưa cần auth/RBAC thật ở bước này.
- Chưa cần phân trang, sort, filter nâng cao cho Document List.
- Chưa cần snippet/highlight thật cho Search (đó là LDMS-016).

### Key Entities *(include if feature involves data)*

- **Document (fixture)**: đại diện một tài liệu — `id`, `name`/`title`, `status` (ví dụ: draft/published), `created_at`. Nguồn: file fixture tĩnh trong backend, không phải bảng DB thật ở bước này.
- **DocumentContent (fixture)**: nội dung text thô gắn với một `document_id`, dùng để Reader placeholder hiển thị và Search placeholder lọc theo từ khóa.

## Success Criteria *(mandatory)*

<!--
  ACTION REQUIRED: Define measurable success criteria.
  These must be technology-agnostic and measurable.
-->

### Measurable Outcomes

- **SC-001**: Người demo có thể đi hết luồng "mở danh sách → click tài liệu → thấy nội dung text" trong dưới 10 giây, không gặp lỗi console/màn trắng.
- **SC-002**: Cả 3 trạng thái rỗng/lỗi trong Edge Cases đều có UI xử lý riêng (không phải màn trắng) — verify bằng cách set fixture rỗng / document_id sai / từ khóa không khớp.
- **SC-003**: Khi LDMS-008/LDMS-026 được pick chính thức, việc thay fixture bằng dữ liệu thật (API/DB) không yêu cầu đổi route hoặc cấu trúc trang FE — chỉ đổi nguồn dữ liệu.

## Assumptions

- Đây là scaffolding, không phải story chính thức — không cần đủ AC như mô tả đầy đủ của LDMS-008 (Epub.js, MinIO signed URL) hay LDMS-026 (đủ AC1-AC3 trong `docs/07-product-backlog.md`); các AC đó sẽ được implement khi story được pick chính thức (Ngày 8-9 theo `docs/plan.md`).
- `GET /documents` ở bước này do chính feature này cung cấp dưới dạng fixture-backed endpoint (chưa phải endpoint thật của LDMS-002 do Khoa Ngô làm) — sẽ được thay thế/hợp nhất khi LDMS-002/026 chính thức triển khai.
- Không cần bảo mật file (Principle IV constitution) ở bước placeholder này vì chưa serve file gốc/EPUB thật qua signed URL — nguyên tắc này áp dụng khi Reader thật (LDMS-008/014) triển khai.
- Fixture text/document list là dữ liệu tĩnh trong repo (ví dụ JSON hoặc module Python), không cần seed DB.
