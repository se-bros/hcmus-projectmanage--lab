# Feature Specification: Tìm kiếm toàn văn & Trải nghiệm đọc sách EPUB (LDMS-008, 014, 015, 016, 019, 020, 026)

**Feature Branch**: `002-search-reader-experience`
**Created**: 2026-07-17
**Status**: Draft
**Input**: User description: "Hoàn thiện Tìm kiếm toàn văn và trải nghiệm đọc sách EPUB: LDMS-008 đọc EPUB trên web, LDMS-014 giảm rủi ro tải file gốc qua Signed URL, LDMS-015 tìm kiếm toàn văn PostgreSQL FTS, LDMS-016 snippet kết quả và mở reader, LDMS-019 tùy chỉnh giao diện đọc (font/màu nền), LDMS-020 đánh dấu trang đọc dở, LDMS-026 danh sách tài liệu hoàn thiện đủ AC" (bảng phân công Ngày 3–9, `docs/plan.md` mục 4, hàng "Khoa Nguyễn — Epic C").

**Bối cảnh**: Đây là bước "chính thức pick" (đủ AC) của Epic C — Search & Reader UX, tiếp nối bản scaffold fixture đã dựng ở `001-reader-search-placeholder`. Feature này thay dữ liệu giả bằng dữ liệu thật (PostgreSQL FTS, MinIO Signed URL, EPUB thật do LDMS-007 xuất bản), theo đúng cấu trúc route đã có sẵn (`/reader/:documentId`, `/search`) để không phải đổi lại FE structure.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Đọc sách EPUB đã xuất bản (Priority: P1)

Là độc giả đã đăng nhập, tôi muốn mở một tài liệu đã xuất bản (published) và đọc nội dung EPUB thật của nó ngay trên trình duyệt, để không cần phần mềm đọc sách riêng.

**Why this priority**: Đây là giá trị cốt lõi nhất của toàn hệ thống LDMS — nếu không đọc được sách thật thì tìm kiếm, snippet, bookmark hay tùy chỉnh giao diện đều vô nghĩa. Story này độc lập hoàn toàn với tìm kiếm (có thể mở thẳng qua `document_id`).

**Independent Test**: Có một document `status = published` kèm EPUB đã sinh (từ LDMS-007) → mở `/reader/:documentId` trực tiếp bằng URL (không qua search/list) → nội dung EPUB hiển thị đọc được. Test độc lập với LDMS-015/016/019/020.

**Acceptance Scenarios**:

1. **Given** document đã `published` và có EPUB, **When** độc giả mở trang Reader với đúng `document_id`, **Then** nội dung EPUB được render đầy đủ, đọc được trên trình duyệt.
2. **Given** document chưa publish hoặc không có EPUB, **When** mở trang Reader, **Then** hiển thị thông báo lỗi rõ ràng ("chưa xuất bản"/"không có bản đọc"), không phải màn trắng.
3. **Given** `document_id` không tồn tại, **When** mở trang Reader, **Then** hiển thị thông báo "không tìm thấy tài liệu".

---

### User Story 2 - Danh sách tài liệu hoàn thiện (Priority: P2)

Là biên tập viên/độc giả, tôi muốn xem danh sách đầy đủ các tài liệu (tên, trạng thái, ngày tạo) với đủ các trạng thái biên/rỗng, để biết tài liệu nào có thể mở đọc hoặc cần thao tác tiếp.

**Why this priority**: Là điểm vào chính để tới được User Story 1 khi độc giả duyệt thay vì gõ thẳng URL. Không phụ thuộc Search/Reader thật, có thể hoàn thiện song song.

**Independent Test**: Có ≥ 1 document thật trong hệ thống (không phải fixture) → mở trang danh sách → thấy bảng/list đúng dữ liệu thật; xóa hết document → thấy empty state. Test độc lập với Reader/Search.

**Acceptance Scenarios**:

1. **Given** có ≥ 1 document, **When** mở trang danh sách, **Then** thấy bảng/list với tên, status, ngày tạo cho từng tài liệu (dữ liệu thật, không còn fixture).
2. **Given** đang ở danh sách, **When** click vào một document, **Then** điều hướng đúng: sang trang editor nếu chưa xuất bản, sang trang Reader nếu đã `published`.
3. **Given** không có document nào, **When** mở trang danh sách, **Then** hiển thị empty state ("Chưa có tài liệu"), không màn trắng/lỗi.
4. **Given** đang ở trang danh sách, **When** nhìn thấy trang, **Then** có nút/link dẫn tới flow tải lên tài liệu mới.

---

### User Story 3 - Tìm kiếm toàn văn (Priority: P3)

Là độc giả, tôi muốn nhập từ khóa và tìm được đúng tài liệu chứa từ khóa đó trong tiêu đề, tác giả hoặc nội dung đã OCR, để không phải duyệt thủ công toàn bộ danh sách.

**Why this priority**: Giá trị tìm kiếm phụ thuộc vào có dữ liệu OCR/metadata thật (do LDMS-004, LDMS-011 cung cấp) nhưng độc lập với việc Reader đã render EPUB hay chưa — search chỉ cần trả đúng danh sách document khớp.

**Independent Test**: Seed từ khóa xuất hiện trong title của 1 document và trong nội dung OCR của 1 document khác → gọi tìm kiếm với từng từ khóa → cả hai đều được tìm thấy đúng. Test độc lập, chưa cần mở Reader.

**Acceptance Scenarios**:

1. **Given** tiêu đề document chứa từ khóa, **When** tìm kiếm với từ khóa đó, **Then** kết quả trả về có document đó.
2. **Given** từ khóa chỉ xuất hiện trong nội dung trang (không có trong title), **When** tìm kiếm, **Then** vẫn tìm thấy đúng document (full-text search thật trên dữ liệu OCR).
3. **Given** từ khóa để trống hoặc chỉ khoảng trắng, **When** submit tìm kiếm, **Then** hệ thống trả lỗi hoặc mảng rỗng theo một convention nhất quán (không crash).
4. **Given** một truy vấn tìm kiếm thông thường, **When** submit, **Then** không gây lỗi server.

---

### User Story 4 - Snippet kết quả và mở đúng Reader (Priority: P4)

Là độc giả, tôi muốn thấy đoạn trích (snippet) chứa từ khóa ngay trong kết quả tìm kiếm và bấm vào để mở thẳng sách đó, để đánh giá độ liên quan trước khi mở đọc toàn bộ.

**Why this priority**: Xây trên cả User Story 1 (Reader thật) và User Story 3 (Search thật) — chỉ có giá trị đầy đủ khi hai story trên đã hoạt động, nên xếp sau.

**Independent Test**: Với một kết quả tìm kiếm đã biết chứa từ khóa X → xác nhận `snippet` trả về có chứa X → click vào kết quả → xác nhận điều hướng đúng `document_id` sang Reader (US1).

**Acceptance Scenarios**:

1. **Given** một kết quả tìm kiếm khớp, **When** xem kết quả, **Then** mỗi hit có kèm `snippet` (đoạn text ngắn liên quan tới query).
2. **Given** snippet được trả về, **When** kiểm tra nội dung, **Then** snippet chứa từ khóa đã tìm.
3. **Given** danh sách kết quả tìm kiếm, **When** click vào một hit, **Then** mở đúng Reader của document tương ứng.

---

### User Story 5 - Giảm rủi ro tải file gốc khi đọc (Priority: P5)

Là độc giả, tôi muốn đọc sách mà không có cách nào dễ dàng tải file EPUB gốc về máy, để bảo vệ bản quyền tài liệu thư viện.

**Why this priority**: Là yêu cầu bảo mật bắt buộc (Constitution Principle IV) nhưng phụ thuộc Reader thật (US1) đã hoạt động trước — không tự đứng một mình được vì cần có luồng đọc thật để áp Signed URL lên.

**Independent Test**: Mở Reader một document đã publish → kiểm tra UI không có control "Download"/"Tải sách" trỏ file gốc; lấy Signed URL đã cấp, đợi hết hạn (15 phút) rồi gọi lại URL cũ → bị từ chối.

**Acceptance Scenarios**:

1. **Given** đang ở trang Reader, **When** quan sát UI, **Then** không có control nào tải trực tiếp file EPUB gốc.
2. **Given** Reader cần tải nội dung EPUB, **When** backend phục vụ file, **Then** dùng MinIO Signed URL với `expires_in` mặc định 15 phút.
3. **Given** một Signed URL đã hết hạn, **When** fetch trực tiếp URL đó, **Then** bị từ chối, không đọc được EPUB.
4. **Given** rủi ro tồn dư (screenshot, DevTools) không thể chặn hoàn toàn bằng kỹ thuật, **When** hoàn thành story, **Then** README ghi nhận rõ các rủi ro này.

---

### User Story 6 - Tùy chỉnh giao diện đọc (Priority: P6)

Là độc giả, tôi muốn chỉnh cỡ chữ và chuyển Light/Dark mode khi đọc, để đọc thoải mái hơn theo sở thích/điều kiện ánh sáng.

**Why this priority**: Cải thiện trải nghiệm (Should, không phải Must), phụ thuộc Reader thật (US1) đã render được nội dung để có gì đó mà tùy chỉnh.

**Independent Test**: Mở Reader, tăng/giảm cỡ chữ và chuyển Dark mode → quan sát thay đổi ngay trên UI; reload lại cùng trình duyệt → xác nhận preference được giữ nguyên (không phụ thuộc US3/US4/US5).

**Acceptance Scenarios**:

1. **Given** đang ở Reader, **When** dùng control tăng/giảm cỡ chữ, **Then** font-size thay đổi tương ứng.
2. **Given** đang ở Reader, **When** chuyển Light/Dark mode, **Then** màu nền/chữ đổi tương ứng và nội dung vẫn đọc được rõ ràng.
3. **Given** đã tùy chỉnh cỡ chữ/theme, **When** reload trang trên cùng trình duyệt, **Then** preference cũ được giữ nguyên (lưu local).

---

### User Story 7 - Đánh dấu trang đọc dở (Priority: P7)

Là độc giả đã đăng nhập, tôi muốn hệ thống tự nhớ vị trí tôi đang đọc dở của một tài liệu, để lần sau mở lại không phải tìm lại từ đầu.

**Why this priority**: Giá trị gia tăng thấp nhất trong nhóm Must/Should của scope này — cần cả đăng nhập thật (LDMS-009) và Reader thật (US1) đã sẵn sàng, và không chặn các luồng khác nếu chưa xong.

**Independent Test**: Đăng nhập user A, mở document, cuộn tới một vị trí, đóng Reader; mở lại → nhảy về đúng vị trí. Đăng nhập user B mở cùng document → không thấy vị trí của A.

**Acceptance Scenarios**:

1. **Given** user đã login đang đọc một document, **When** rời khỏi/đóng Reader, **Then** vị trí đọc được lưu lại gắn với `(user_id, document_id)`.
2. **Given** đã có bookmark lưu trước đó, **When** mở lại Reader cùng user + cùng document, **Then** nhảy về đúng vị trí đã lưu.
3. **Given** một user khác mở cùng document đó, **When** vào Reader, **Then** không nhận vị trí bookmark của user trước — mỗi user có bookmark riêng.

---

### Edge Cases

- Document chưa `published` hoặc thiếu EPUB → Reader báo lỗi rõ ràng, không màn trắng (US1 AC2).
- `document_id` không tồn tại/sai định dạng → thông báo "không tìm thấy" (US1 AC3).
- Danh sách tài liệu rỗng → empty state, không lỗi (US2 AC3).
- Từ khóa tìm kiếm rỗng/toàn khoảng trắng → xử lý nhất quán, không crash (US3 AC3).
- Từ khóa không khớp document nào → trả kết quả rỗng có UI xử lý riêng, không lỗi.
- Signed URL hết hạn (>15 phút) → truy cập trực tiếp URL cũ bị từ chối (US5 AC3).
- Hai user khác nhau đọc cùng một document → bookmark không lẫn giữa hai user (US7 AC3).
- Reload trang sau khi đổi font-size/theme → preference vẫn giữ nguyên trên cùng trình duyệt (US6 AC3); nhưng đổi sang trình duyệt/máy khác thì preference không tự đồng bộ (lưu local, ngoài phạm vi story này).
- Reader cố tình chặn download nhưng người dùng vẫn có thể chụp màn hình/dùng DevTools để lấy nội dung — residual risk được ghi nhận trong README, không phải bug cần fix (US5 AC4).

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST cho phép độc giả mở một document `published` kèm EPUB thật và đọc nội dung ngay trên trình duyệt qua `document_id` (US1).
- **FR-002**: System MUST hiển thị thông báo lỗi rõ ràng (không màn trắng) khi document chưa publish, thiếu EPUB, hoặc `document_id` không tồn tại (US1).
- **FR-003**: FE MUST hiển thị danh sách tài liệu từ dữ liệu thật (không còn fixture), gồm tên/status/ngày tạo, với empty state khi rỗng và link tới flow upload (US2).
- **FR-004**: Click vào một document trong danh sách MUST điều hướng đúng theo trạng thái: editor nếu chưa xuất bản, Reader nếu đã `published` (US2).
- **FR-005**: System MUST cung cấp tìm kiếm toàn văn thật (PostgreSQL FTS) khớp cả tiêu đề/tác giả và nội dung OCR đã lập chỉ mục, không còn là bộ lọc fixture (US3).
- **FR-006**: System MUST xử lý từ khóa rỗng/whitespace theo một convention nhất quán (lỗi hoặc mảng rỗng) và không để lỗi server với truy vấn hợp lệ (US3).
- **FR-007**: Mỗi kết quả tìm kiếm MUST kèm một đoạn `snippet` chứa từ khóa liên quan, và click vào kết quả MUST mở đúng Reader của document đó (US4).
- **FR-008**: Reader UI MUST NOT cung cấp control tải trực tiếp file EPUB gốc; nội dung EPUB MUST được phục vụ qua MinIO Signed URL với thời hạn mặc định 15 phút, và URL hết hạn MUST bị từ chối khi truy cập lại (US5) — theo Constitution Principle IV.
- **FR-009**: README MUST ghi nhận rủi ro tồn dư về chống tải lậu (screenshot, DevTools) không thể loại bỏ hoàn toàn bằng kỹ thuật (US5).
- **FR-010**: Reader MUST cho phép độc giả tăng/giảm cỡ chữ và chuyển Light/Dark mode, giữ nguyên nội dung đọc được rõ ràng ở mọi chế độ (US6).
- **FR-011**: Reader preference (cỡ chữ, theme) MUST được lưu lại (local, theo trình duyệt) và áp dụng lại khi reload cùng trình duyệt (US6).
- **FR-012**: System MUST lưu vị trí đọc dở của một user cho một document theo cặp `(user_id, document_id)`, và khôi phục đúng vị trí khi user đó mở lại cùng document (US7). Việc lưu chỉ cần xảy ra một lần khi user rời/đóng Reader (điều hướng đi hoặc đóng tab) — không yêu cầu tự động lưu định kỳ trong lúc đang đọc; mất tiến độ do trình duyệt crash/mất điện giữa phiên đọc là rủi ro chấp nhận được, ngoài phạm vi story này.
- **FR-013**: Bookmark của một user MUST không hiển thị/áp dụng cho user khác mở cùng document (US7).

*Ghi chú phạm vi (không phải NEEDS CLARIFICATION):*
- Route FE (`/reader/:documentId`, `/search`, danh sách tài liệu) đã tồn tại từ `001-reader-search-placeholder` — feature này thay nguồn dữ liệu từ fixture sang thật, không đổi cấu trúc route/trang.
- Auth/RBAC nền tảng (LDMS-009/010) được giả định đã sẵn sàng khi US1/US5/US7 triển khai — feature này dùng, không xây lại cơ chế đăng nhập/phân quyền.
- EPUB thật (LDMS-007/Pandoc) và OCR/metadata thật (LDMS-004/011) là input đầu vào cần có trước khi US1/US3 kiểm thử được với dữ liệu thật — nếu chưa sẵn sàng, có thể kiểm thử tạm với 1 document mẫu đã publish thủ công.

### Key Entities *(include if feature involves data)*

- **Document**: tài liệu thư viện — `id`, tiêu đề, tác giả, `status` (draft/published), ngày tạo. Nguồn dữ liệu thật từ PostgreSQL (không còn fixture).
- **EpubAsset**: file EPUB đã biên dịch gắn với một Document đã publish, lưu trên MinIO, truy cập qua Signed URL có thời hạn.
- **SearchHit**: kết quả tìm kiếm — tham chiếu tới Document, kèm `snippet` (đoạn text khớp từ khóa).
- **ReaderPreference**: tùy chọn hiển thị của độc giả — cỡ chữ, theme (light/dark), lưu theo trình duyệt (local), không gắn với tài khoản.
- **Bookmark**: vị trí đọc dở — gắn với cặp `(user_id, document_id)`, lưu vị trí đọc gần nhất.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Độc giả có quyền đọc mở được một document đã publish và thấy nội dung EPUB thật hiển thị đầy đủ, không qua fixture giả lập.
- **SC-002**: Tìm kiếm với từ khóa chỉ xuất hiện trong nội dung OCR (không phải title) vẫn trả về đúng tài liệu — phản hồi dưới 3 giây theo mục tiêu kiến trúc (`docs/06-architecture.md` §2.1).
- **SC-003**: 100% các trường hợp Signed URL đã hết hạn (>15 phút) không thể dùng lại để truy cập nội dung EPUB gốc.
- **SC-004**: Độc giả quay lại một document đang đọc dở thấy đúng vị trí đã dừng ở lần mở trước, và không nhìn thấy vị trí đọc của người dùng khác.
- **SC-005**: Danh sách tài liệu và kết quả tìm kiếm đều xử lý đúng cả hai trạng thái có dữ liệu và rỗng — không có màn trắng hoặc lỗi console chưa xử lý ở bất kỳ trạng thái nào trong Edge Cases.
- **SC-006**: Tùy chỉnh cỡ chữ/theme của Reader được giữ nguyên sau khi tải lại trang trên cùng trình duyệt.

## Assumptions

- Feature này là bước "pick chính thức" (đủ AC) theo Constitution — khác với `001-reader-search-placeholder` (scaffold fixture); route/cấu trúc trang FE giữ nguyên, chỉ thay nguồn dữ liệu.
- LDMS-009 (Mock JWT + roles) và LDMS-010 (RBAC kiểm soát truy cập tài liệu) được coi là đã sẵn sàng để US1/US5/US7 dùng — feature này không tự triển khai lại đăng nhập/phân quyền.
- LDMS-007 (đóng gói EPUB qua Pandoc), LDMS-004 (kết quả OCR theo trang) và LDMS-011 (metadata bắt buộc) là input cần có trước để US1/US3 có dữ liệu thật kiểm thử — đây là các story do thành viên khác trong nhóm phụ trách theo `docs/plan.md`.
- Với US3 (Search) AC3 "trả lỗi hoặc mảng rỗng" — chọn quy ước trả mảng rỗng cho từ khóa rỗng/whitespace, nhất quán với cách xử lý "không có kết quả" (không coi là lỗi 4xx), theo đúng backlog cho phép cả hai lựa chọn.
- ReaderPreference (US6) lưu theo trình duyệt (localStorage-tương-đương), không đồng bộ giữa các thiết bị/trình duyệt khác nhau của cùng user — nằm ngoài phạm vi story này.
- Vị trí đọc (Bookmark, US7) chỉ cần đủ chi tiết để nhảy lại đúng vị trí trong Reader — không yêu cầu định dạng cụ thể (ví dụ CFI hay số trang), việc này thuộc quyết định kỹ thuật ở `/speckit.plan`.
