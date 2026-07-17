# YÊU CẦU NGHIỆP VỤ VÀ SỔ TAY PRODUCT BACKLOG

## Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS (HCMUS-LDMS)

### THÔNG TIN TÀI LIỆU (DOCUMENT CONTROL)

| Trường thông tin (Field)                   | Nội dung đặc tả (Description)                     |
| :----------------------------------------- | :------------------------------------------------ |
| **Mã tài liệu (Document ID)**              | `HCMUS-LDMS-PBL`                                  |
| **Tên tài liệu (Document Title)**          | Sổ tay Product Backlog (Product Backlog Document) |
| **Dự án (Project Name)**                   | HCMUS-LDMS                                        |
| **Đơn vị soạn thảo (Author/Organization)** | Nhóm Phát triển Dự án HCMUS-LDMS                  |
| **Người xem xét (Reviewer)**               | Trưởng phòng CNTT & Giám đốc Thư viện             |
| **Người phê duyệt (Approver)**             | Ban Giám hiệu Trường ĐH Khoa học Tự nhiên         |
| **Cấp độ bảo mật (Security Class)**        | Internal (Nội bộ trường)                          |
| **Trạng thái tài liệu (Status)**           | Ready for Implementation                          |

### LỊCH SỬ PHIÊN BẢN (REVISION HISTORY)

| Phiên bản (Version) | Ngày phát hành (Date) | Mô tả thay đổi (Description of Change)                                                                                                                                                                                                                   | Người thực hiện (Author) |
| :-----------------: | :-------------------: | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------: |
|         1.0         |      11/07/2026       | Khởi tạo dự thảo Product Backlog ban đầu (v1.0).                                                                                                                                                                                                         |      Mạch Quốc Tấn       |
|         2.0         |      14/07/2026       | Chuẩn hóa định dạng User Story, bổ sung kịch bản AC, DoD, Sprint mapping.                                                                                                                                                                                |      Mạch Quốc Tấn       |
|         3.0         |      15/07/2026       | Cập nhật nội dung: Kanban, cắt nhỏ story, gom module cho agent, DoD Pilot, thứ tự implement & đo throughput (giữ khung mục lục).                                                                                                                         |     Nhóm phát triển      |
|         3.1         |      15/07/2026       | Siết Acceptance Criteria toàn bộ 25 stories (điều kiện lỗi, verify được, GWT nơi cần).                                                                                                                                                                   |     Nhóm phát triển      |
|         4.0         |      15/07/2026       | Tái thiết kế backlog phù hợp đồ án sinh viên: đơn giản tech stack (Google OAuth thay Keycloak, Postgres FTS thay Elasticsearch, BackgroundTasks thay Celery/Redis), nhẹ AC (bỏ GWT bắt buộc, bỏ ép HTTP status code), giữ MoSCoW/Size/Kanban/throughput. |     Nhóm phát triển      |

---

## Mục lục

- [1. Định nghĩa Hoàn thành và Quy tắc tổ chức](#1-định-nghĩa-hoàn-thành-và-quy-tắc-tổ-chức)
  - [1.1. Quy tắc Kanban và Forecast](#11-quy-tắc-kanban-và-forecast)
  - [1.2. Định nghĩa Hoàn thành (Definition of Done - DoD)](#12-định-nghĩa-hoàn-thành-definition-of-done---dod)
  - [1.3. Thang đo độ ưu tiên MoSCoW](#13-thang-đo-độ-ưu-tiên-moscow)
- [2. Chi tiết Product Backlog — User Story & Acceptance Criteria](#2-chi-tiết-product-backlog--user-story--acceptance-criteria)
  - [EPIC D — Nền tảng triển khai (Platform)](#epic-d--nền-tảng-triển-khai-platform)
  - [EPIC A — Xác thực & Phân quyền (Identity & Access)](#epic-a--xác-thực--phân-quyền-identity--access)
  - [EPIC B — Số hóa & Xuất bản (Digitization & Publish)](#epic-b--số-hóa--xuất-bản-digitization--publish)
  - [EPIC C — Tra cứu & Đọc sách (Search & Reader UX)](#epic-c--tra-cứu--đọc-sách-search--reader-ux)
- [3. Bản đồ triển khai (Implementation Map)](#3-bản-đồ-triển-khai-implementation-map)

---

## 1. Định nghĩa Hoàn thành và Quy tắc tổ chức

### 1.1. Quy tắc Kanban và Forecast

Nhóm phát triển áp dụng **Kanban**: làm **từng card backlog** (WIP = 1 card / người), gom theo **module** (M0–M8, xem `06-architecture.md`).

**Definition of Ready (DoR):** Card chỉ được kéo vào _In Progress_ khi có ID, AC rõ ràng, `depends_on` đã Done (nếu có), size S hoặc M (≤ 2 ngày). Card quá to phải tách trước.

**Forecast:** Thời gian dev được dự báo sau khi đo **số user story Done mỗi tuần** (deploy + AC pass), không dùng Story Point để nhân lịch. Công thức: Dev weeks ≈ N(còn lại) / T, với T = story Done/tuần. Báo cáo dạng **khoảng**.

**Size (thay cho Story Point):** S ≤ 1 ngày, M ≤ 2 ngày. Không dùng tổng SP để ra số tuần.

### 1.2. Định nghĩa Hoàn thành (Definition of Done - DoD)

Một User Story chỉ được coi là hoàn thành (`Done`) khi đáp ứng đủ các tiêu chí sau:

1. **AC pass:** Toàn bộ Acceptance Criteria của card đã kiểm tra đạt.
2. **Code merge:** Mã nguồn merge vào nhánh chính qua Pull Request (self-review checklist OK).
3. **Chạy local:** Chạy được trên môi trường local (`docker compose up` + `npm run dev`).
4. **README:** Endpoint hoặc trang mới có ghi trong README module.
5. **Log effort:** Ghi nhận thời gian thực hiện và token AI (nếu có) phục vụ báo cáo throughput.

> Chỉ đếm throughput T = số story **Done** trong 7 ngày theo DoD trên.

### 1.3. Thang đo độ ưu tiên MoSCoW

- **Must-have (M):** Bắt buộc cho luồng E2E hoạt động được — 16 stories.
- **Should-have (S):** Nâng cao trải nghiệm, làm sau khi Must xong — 7 stories.
- **Could-have (C):** Làm nếu còn thời gian — 3 stories. Cắt bỏ không ảnh hưởng luồng chính.

---

## 2. Chi tiết Product Backlog — User Story & Acceptance Criteria

Mỗi story có: **ID** (`LDMS-xxx`), **Module**, **Size**, **depends_on**, **MoSCoW**, **AC**.

**Module:** M0 Platform · M1 Documents & Storage · M2 OCR · M3 Editor · M4 Metadata · M5 Publish EPUB · M6 Reader · M7 Search · M8 Identity.

**Lưu ý tech stack (so với `06-architecture.md`):**

- **Auth MVP:** Mock JWT → Google OAuth 2.0 (thay Keycloak, không cần self-host).
- **Search MVP:** PostgreSQL Full-Text Search (thay Elasticsearch, không cần service riêng).
- **Queue MVP:** FastAPI BackgroundTasks (thay Celery + Redis, bớt 2 services).
- **DRM:** MinIO Signed URL 15 phút (giữ nguyên).
- **Compose MVP:** 3 services — API + PostgreSQL + MinIO.

---

### EPIC D — Nền tảng triển khai (Platform)

#### LDMS-001: Bootstrap môi trường monorepo + Docker Compose

- **User Story:** Là lập trình viên, tôi muốn một lệnh khởi động API + DB + storage thống nhất để cả nhóm implement cùng một môi trường.
- **Module:** M0 | **Size:** M | **Độ ưu tiên:** Must | **depends_on:** —
- **Tiêu chí chấp nhận (Acceptance Criteria):**
  - **AC 1:** Repo mới clone, chạy lệnh start trong README (compose hoặc script), trong ≤ 5 phút các service **API + PostgreSQL + MinIO** ở trạng thái healthy/up.
  - **AC 2:** `GET /health` trả HTTP 200 với body có tín hiệu sống (vd. `{"status":"ok"}`).
  - **AC 3:** Có `.env.example` liệt kê biến bắt buộc (DB URL, S3 endpoint/key…); README ghi port API và FE.
  - **AC 4:** Thiếu biến env bắt buộc → service fail với log/message rõ, không treo im lặng.

---

### EPIC A — Xác thực & Phân quyền (Identity & Access)

#### LDMS-009: Đăng nhập dev (Mock JWT + roles)

- **User Story:** Là lập trình viên, tôi muốn có endpoint cấp JWT nhanh với role tùy chọn để test phân quyền trong môi trường dev mà không cần setup auth thật.
- **Module:** M8 | **Size:** M | **Độ ưu tiên:** Must | **depends_on:** LDMS-001
- **Tiêu chí chấp nhận (Acceptance Criteria):**
  - **AC 1:** Gọi endpoint cấp token (vd. `POST /auth/dev-token`) với role `reader` | `editor` | `admin`, nhận JWT hợp lệ (decode được `sub` và `role`).
  - **AC 2:** Gọi API ghi (upload / publish) với token `reader` → bị từ chối. Gọi với token `editor` hoặc `admin` → không bị từ chối vì quyền.
  - **AC 3:** Gọi API ghi mà không gửi token → bị từ chối.
  - **AC 4:** README: flag bật/tắt mock auth + ví dụ `curl` lấy token từng role.

#### LDMS-018: Đăng nhập Google OAuth 2.0

- **User Story:** Là sinh viên/giảng viên, tôi muốn đăng nhập bằng tài khoản Google trường (`@hcmus.edu.vn`) để hệ thống xác nhận danh tính mà không cần tạo tài khoản riêng.
- **Module:** M8 | **Size:** M | **Độ ưu tiên:** Should | **depends_on:** LDMS-009
- **Tiêu chí chấp nhận (Acceptance Criteria):**
  - **AC 1:** Mở `/login` và chọn đăng nhập Google → redirect tới Google OAuth consent screen (client_id cấu hình bằng env).
  - **AC 2:** Đăng nhập Google thành công → callback về app → session/JWT có identity + role được gán (vd. email `@hcmus.edu.vn` → role `reader`).
  - **AC 3:** Khi bật Google OAuth, mock dev-token bị tắt (gọi → trả lỗi hoặc không tồn tại).
  - **AC 4:** Client secret chỉ lấy từ env, `git grep` không thấy secret hardcode trong repo.

#### LDMS-010: Kiểm soát quyền truy cập tài liệu

- **User Story:** Là sinh viên, tôi chỉ muốn nhìn thấy và đọc các tài liệu mà tôi được phép tiếp cận.
- **Module:** M1 + M8 | **Size:** S | **Độ ưu tiên:** Must | **depends_on:** LDMS-002, LDMS-009
- **Tiêu chí chấp nhận (Acceptance Criteria):**
  - **AC 1:** Document có field `is_public` (boolean). Giá trị mặc định là `false`.
  - **AC 2:** Document `is_public = true` → guest (không token) có thể đọc được.
  - **AC 3:** Document `is_public = false` và request không có token hợp lệ → không đọc được (ẩn khỏi list hoặc trả lỗi).
  - **AC 4:** Có kịch bản test (manual curl hoặc script) với guest vs user đã login, kết quả khớp AC 2–3.

---

### EPIC B — Số hóa & Xuất bản (Digitization & Publish)

#### LDMS-002: Tải lên tệp scan gốc

- **User Story:** Là thủ thư, tôi muốn tải lên tệp PDF hoặc ảnh scan sách giấy gốc để hệ thống bắt đầu xử lý luồng số hóa.
- **Module:** M1 | **Size:** M | **Độ ưu tiên:** Must | **depends_on:** LDMS-001
- **Tiêu chí chấp nhận (Acceptance Criteria):**
  - **AC 1:** Upload file `.pdf` / `.jpg` / `.png` hợp lệ → trả thành công với `document_id`.
  - **AC 2:** Upload file type không hỗ trợ (vd. `.exe`, `.docx`) → trả lỗi rõ ràng, không tạo document.
  - **AC 3:** `GET /documents/{id}` trả `id`, `original_filename`, `status` (vd. `uploaded`), `created_at`.
  - **AC 4:** File nằm trên MinIO storage, có thể đọc lại bytes theo `document_id`.
  - **AC 5:** `GET /documents/{id}` với id không tồn tại → trả lỗi "không tìm thấy".

#### LDMS-003: Hàng đợi OCR và trạng thái job

- **User Story:** Là thủ thư, tôi muốn hệ thống chạy OCR nền và tôi theo dõi được trạng thái xử lý.
- **Module:** M2 | **Size:** M | **Độ ưu tiên:** Must | **depends_on:** LDMS-002
- **Tiêu chí chấp nhận (Acceptance Criteria):**
  - **AC 1:** Kích hoạt OCR cho document đã upload (auto hoặc `POST .../ocr`) → tạo job với status ban đầu `pending`.
  - **AC 2:** Job trải qua `processing` rồi kết thúc `completed` hoặc `failed` (quan sát qua GET status).
  - **AC 3:** API kích hoạt OCR trả về nhanh (không chờ OCR xong trong cùng HTTP request).
  - **AC 4:** Job `failed` → GET status có `error_message` không rỗng.

#### LDMS-004: Kết quả OCR theo từng trang

- **User Story:** Là thủ thư, tôi muốn nhận văn bản OCR tách theo từng trang sách để biên tập.
- **Module:** M2 | **Size:** M | **Độ ưu tiên:** Must | **depends_on:** LDMS-003
- **Tiêu chí chấp nhận (Acceptance Criteria):**
  - **AC 1:** OCR job `completed` trên file mẫu → `GET /documents/{id}/pages` trả ≥ 1 page với `page_number` (bắt đầu từ 1) và `text_content`.
  - **AC 2:** PDF mẫu nhiều trang → OCR xong → số page ≥ 2, `page_number` không trùng.
  - **AC 3:** Repo có `samples/` (PDF và/hoặc ảnh) + README mô tả lệnh chạy AC lặp lại.
  - **AC 4:** Document chưa OCR xong → GET pages trả kết quả rõ ràng (mảng rỗng, lỗi, hoặc status) — không lỗi server.

#### LDMS-005: API đọc và cập nhật text trang

- **User Story:** Là biên tập viên, tôi muốn đọc và sửa text một trang qua API.
- **Module:** M3 | **Size:** S | **Độ ưu tiên:** Must | **depends_on:** LDMS-004
- **Tiêu chí chấp nhận (Acceptance Criteria):**
  - **AC 1:** `GET .../pages/{n}` trả `text_content` + `page_number` cho page tồn tại.
  - **AC 2:** `PUT`/`PATCH` với `text_content` mới → GET lại → nội dung đã cập nhật.
  - **AC 3:** `page_number` không tồn tại → trả lỗi "không tìm thấy".

#### LDMS-006: UI biên tập text tối thiểu

- **User Story:** Là biên tập viên, tôi muốn sửa text OCR trên giao diện và lưu lại.
- **Module:** M3 | **Size:** M | **Độ ưu tiên:** Must | **depends_on:** LDMS-005
- **Tiêu chí chấp nhận (Acceptance Criteria):**
  - **AC 1:** Document có ≥ 1 page → mở màn editor → thấy danh sách/chỉ số trang chọn được.
  - **AC 2:** Sửa text và bấm Lưu → request thành công → F5/reload vẫn còn text đã sửa.
  - **AC 3:** UI có trạng thái lưu (saving / saved / error) quan sát được.

#### LDMS-017: Biên tập Split-screen (ảnh + text)

- **User Story:** Là biên tập viên, tôi muốn so sánh ảnh scan và văn bản OCR song song để hiệu chỉnh nhanh.
- **Module:** M3 | **Size:** M | **Độ ưu tiên:** Should | **depends_on:** LDMS-006
- **Tiêu chí chấp nhận (Acceptance Criteria):**
  - **AC 1:** Mở split-screen → vùng trái = preview ảnh/PDF page, vùng phải = editor text cùng page.
  - **AC 2:** Đổi sang page khác → cả hai vùng đồng bộ theo page mới.
  - **AC 3:** Chưa có image page → vùng trái hiển thị placeholder; vùng phải vẫn edit/lưu text được.

#### LDMS-026: Danh sách tài liệu (Document List UI)

- **User Story:** Là biên tập viên, tôi muốn xem danh sách tài liệu đã tải lên để biết trạng thái và thao tác tiếp.
- **Module:** M1 + M3 | **Size:** M | **Độ ưu tiên:** Must | **depends_on:** LDMS-002, LDMS-006
- **Tiêu chí chấp nhận (Acceptance Criteria):**
  - **AC 1:** Có ≥ 1 document → mở trang danh sách → thấy bảng/list với tên, status, ngày tạo.
  - **AC 2:** Click vào document → mở đúng trang editor hoặc reader tùy trạng thái.
  - **AC 3:** Không có document nào → UI hiển thị empty state ("Chưa có tài liệu"), không màn trắng/lỗi.
  - **AC 4:** Trang có nút/link upload dẫn đến flow tải lên.

#### LDMS-011: Gán siêu dữ liệu bắt buộc

- **User Story:** Là thủ thư, tôi muốn nhập thông tin mô tả sách để độc giả tra cứu và để được phép xuất bản.
- **Module:** M4 | **Size:** S | **Độ ưu tiên:** Must | **depends_on:** LDMS-002
- **Tiêu chí chấp nhận (Acceptance Criteria):**
  - **AC 1:** Lưu metadata hợp lệ (`title`, `author`, và optional `shelf_location`) → GET document trả đúng các field đó.
  - **AC 2:** `title` hoặc `author` rỗng/whitespace → trả lỗi chỉ rõ field thiếu.
  - **AC 3:** `shelf_location` bỏ trống → vẫn lưu được các field khác.

#### LDMS-012: Quản lý Category (2 cấp)

- **User Story:** Là admin, tôi muốn cấu hình cây danh mục để tổ chức tài liệu.
- **Module:** M4 | **Size:** M | **Độ ưu tiên:** Must | **depends_on:** LDMS-011
- **Tiêu chí chấp nhận (Acceptance Criteria):**
  - **AC 1:** Tạo category **parent** và category **con** (`parent_id`) thành công; GET tree/list thể hiện quan hệ 2 cấp.
  - **AC 2:** Gán `category_id` cho document → GET document thấy category đã gán.
  - **AC 3:** Category id không tồn tại → gán vào document trả lỗi rõ ràng.
  - **AC 4:** Xóa/cập nhật tên category hoạt động — không lỗi server.

#### LDMS-007: Đóng gói & xuất EPUB

- **User Story:** Là thủ thư, tôi muốn đóng gói nội dung đã biên tập thành file EPUB để độc giả đọc trực tuyến.
- **Module:** M5 | **Size:** M | **Độ ưu tiên:** Must | **depends_on:** LDMS-005
- **Tiêu chí chấp nhận (Acceptance Criteria):**
  - **AC 1:** Document có ≥ 1 page có text → `POST .../publish` → tạo file EPUB trên storage, status → `published`.
  - **AC 2:** Thứ tự nội dung EPUB theo `page_number` tăng dần.
  - **AC 3:** File EPUB mở được bằng Epub.js hoặc ebook viewer (thấy text đã put vào page).
  - **AC 4:** Document không có page/text → publish trả lỗi rõ ràng, status không thành `published`.

#### LDMS-013: Chặn xuất bản khi thiếu metadata

- **User Story:** Là thủ thư, tôi không muốn xuất bản nhầm sách thiếu thông tin bắt buộc.
- **Module:** M4 + M5 | **Size:** S | **Độ ưu tiên:** Must | **depends_on:** LDMS-007, LDMS-011
- **Tiêu chí chấp nhận (Acceptance Criteria):**
  - **AC 1:** Thiếu `title` hoặc `author` → publish trả lỗi và **không** tạo EPUB.
  - **AC 2:** Đủ metadata + có page text → publish thành công.
  - **AC 3:** Message lỗi chỉ rõ field metadata nào thiếu.

#### LDMS-022: UI trạng thái OCR + retry

- **User Story:** Là biên tập viên, tôi muốn thấy job OCR lỗi và chạy lại được.
- **Module:** M2 | **Size:** S | **Độ ưu tiên:** Should | **depends_on:** LDMS-003
- **Tiêu chí chấp nhận (Acceptance Criteria):**
  - **AC 1:** Mở chi tiết document → thấy state job hiện tại (`pending` / `processing` / `completed` / `failed`).
  - **AC 2:** State `failed` → bấm Retry → tạo job mới, state chuyển khỏi `failed`.
  - **AC 3:** Khi `failed`, UI vẫn hiển thị `error_message`.

#### LDMS-023: Tags

- **User Story:** Là thủ thư, tôi muốn gắn tag linh hoạt cho tài liệu.
- **Module:** M4 | **Size:** S | **Độ ưu tiên:** Could | **depends_on:** LDMS-012
- **Tiêu chí chấp nhận (Acceptance Criteria):**
  - **AC 1:** Thêm tag cho document → GET document/tags chứa tag đó.
  - **AC 2:** Xóa tag → GET không còn tag đó trên document.
  - **AC 3:** Tag được normalize (lower + trim) trước khi lưu để tránh trùng lặp.

---

### EPIC C — Tra cứu & Đọc sách (Search & Reader UX)

#### LDMS-008: Đọc sách EPUB trên web (tối thiểu)

- **User Story:** Là độc giả, tôi muốn mở sách EPUB trên trình duyệt sau khi biên tập viên xuất bản.
- **Module:** M6 | **Size:** M | **Độ ưu tiên:** Must | **depends_on:** LDMS-007
- **Tiêu chí chấp nhận (Acceptance Criteria):**
  - **AC 1:** Document `published` có EPUB → mở reader với `document_id` → Epub.js render được nội dung.
  - **AC 2:** Document chưa publish / không có EPUB → UI message lỗi rõ ràng, không màn trắng.
  - **AC 3:** `document_id` sai → thông báo "không tìm thấy".

#### LDMS-014: Giảm rủi ro tải file gốc khi đọc

- **User Story:** Là độc giả, tôi muốn đọc sách mà hệ thống không khuyến khích tải file EPUB gốc về máy.
- **Module:** M6 | **Size:** M | **Độ ưu tiên:** Should | **depends_on:** LDMS-008, LDMS-010
- **Tiêu chí chấp nhận (Acceptance Criteria):**
  - **AC 1:** Trên UI reader **không** có control "Download EPUB" / "Tải sách" trỏ file gốc.
  - **AC 2:** EPUB được serve qua MinIO Signed URL có `expires_in` mặc định **15 phút**.
  - **AC 3:** URL đã hết hạn → fetch trực tiếp URL cũ → bị từ chối (không đọc được EPUB).
  - **AC 4:** README mục Security: ghi nhận residual risk (screenshot, DevTools).

#### LDMS-015: Tìm kiếm toàn văn (PostgreSQL FTS)

- **User Story:** Là độc giả, tôi muốn tìm sách theo từ khóa trong tiêu đề/tác giả/nội dung đã OCR.
- **Module:** M7 | **Size:** M | **Độ ưu tiên:** Must | **depends_on:** LDMS-004, LDMS-011
- **Tiêu chí chấp nhận (Acceptance Criteria):**
  - **AC 1:** Document title chứa từ khóa → `GET /search?q=...` → kết quả có document đó.
  - **AC 2:** Từ khóa chỉ có trong `text_content` page (không có trong title) → search vẫn tìm thấy document (full-text).
  - **AC 3:** `q` rỗng hoặc chỉ whitespace → trả lỗi hoặc mảng rỗng (convention nhất quán).
  - **AC 4:** Query bình thường không gây lỗi server.

#### LDMS-016: Snippet kết quả và mở reader

- **User Story:** Là độc giả, tôi muốn thấy đoạn trích chứa từ khóa và mở đúng sách để đọc.
- **Module:** M7 | **Size:** S | **Độ ưu tiên:** Must | **depends_on:** LDMS-015, LDMS-008
- **Tiêu chí chấp nhận (Acceptance Criteria):**
  - **AC 1:** Mỗi hit trong response/UI có `snippet` (đoạn text ngắn) liên quan query.
  - **AC 2:** Snippet chứa từ khóa tìm kiếm (kiểm bằng fixture).
  - **AC 3:** Click hit → mở reader đúng document đó.

#### LDMS-019: Tùy chỉnh giao diện đọc sách

- **User Story:** Là độc giả, tôi muốn chỉnh cỡ chữ và màu nền khi đọc.
- **Module:** M6 | **Size:** S | **Độ ưu tiên:** Should | **depends_on:** LDMS-008
- **Tiêu chí chấp nhận (Acceptance Criteria):**
  - **AC 1:** Control tăng/giảm cỡ chữ hoạt động (quan sát font-size thay đổi).
  - **AC 2:** Chuyển được Light và Dark mode; màu nền/chữ đổi tương ứng, vẫn đọc được text.
  - **AC 3:** Preference giữ khi reload cùng browser (localStorage).

#### LDMS-020: Đánh dấu trang (Bookmark)

- **User Story:** Là độc giả, tôi muốn hệ thống nhớ vị trí đọc dở.
- **Module:** M6 | **Size:** M | **Độ ưu tiên:** Should | **depends_on:** LDMS-009, LDMS-008
- **Tiêu chí chấp nhận (Acceptance Criteria):**
  - **AC 1:** User đã login + document đang đọc → lưu bookmark → API/DB có bản ghi theo `(user_id, document_id)` với vị trí đọc.
  - **AC 2:** Đóng và mở lại reader cùng user/document → nhảy về vị trí đã lưu.
  - **AC 3:** User khác mở cùng document → không nhận bookmark của user trước.

#### LDMS-021: Highlight và ghi chú

- **User Story:** Là độc giả, tôi muốn highlight đoạn văn và gắn ghi chú.
- **Module:** M6 | **Size:** M | **Độ ưu tiên:** Could | **depends_on:** LDMS-020
- **Tiêu chí chấp nhận (Acceptance Criteria):**
  - **AC 1:** Chọn đoạn text trên reader → tạo highlight → đoạn được đánh dấu và persist theo user+document.
  - **AC 2:** Có thể gắn ghi chú text; GET lại còn ghi chú.
  - **AC 3:** Xóa highlight → không còn trên UI sau reload.

#### LDMS-024: Trích dẫn tự động (Citation)

- **User Story:** Là độc giả, tôi muốn sinh chuỗi trích dẫn APA/IEEE từ metadata sách.
- **Module:** M4 | **Size:** S | **Độ ưu tiên:** Could | **depends_on:** LDMS-011
- **Tiêu chí chấp nhận (Acceptance Criteria):**
  - **AC 1:** Document có `title` + `author` → gọi citation API hoặc bấm nút UI → trả chuỗi APA và IEEE.
  - **AC 2:** Chuỗi chứa title và author đã lưu (không hardcode).
  - **AC 3:** Thiếu title/author → trả lỗi hoặc chuỗi ghi "thiếu metadata" — không lỗi server.

#### LDMS-025: Tìm kiếm Elasticsearch nâng cao

- **User Story:** Là độc giả, tôi muốn tìm kiếm mượt hơn (fuzzy, scale) khi Postgres FTS không đủ.
- **Module:** M7 | **Size:** M | **Độ ưu tiên:** Could | **depends_on:** LDMS-015
- **Tiêu chí chấp nhận (Acceptance Criteria):**
  - **AC 1:** Elasticsearch up + document đã publish/OCR → index pipeline chạy → document searchable qua ES.
  - **AC 2:** `GET /search?q=...` trả kết quả từ ES khi feature flag bật.
  - **AC 3:** ES down → fallback Postgres FTS hoặc trả lỗi rõ ràng — không treo.

---

## 3. Bản đồ triển khai (Implementation Map)

> **Cách đọc:** Nhóm làm **từng story theo Order**. Cuối mỗi **7 ngày**, đếm story **Done** → throughput T → forecast N/T tuần. MoSCoW cho biết cắt gì nếu trễ: Must → Should → Could.

### Giai đoạn 1 — Nền tảng & Luồng dữ liệu

Mục tiêu: _API chạy được, upload file, OCR trả text theo trang._

| Order |    ID    | Epic | Module | Size | MoSCoW | Tóm tắt                     | depends_on |
| :---: | :------: | :--: | :----: | :--: | :----: | :-------------------------- | :--------- |
|   1   | LDMS-001 |  D   |   M0   |  M   |  Must  | Compose 3 services + health | —          |
|   2   | LDMS-002 |  B   |   M1   |  M   |  Must  | Upload PDF/ảnh              | 001        |
|   3   | LDMS-003 |  B   |   M2   |  M   |  Must  | OCR background + status     | 002        |
|   4   | LDMS-004 |  B   |   M2   |  M   |  Must  | Text theo trang             | 003        |
|   5   | LDMS-005 |  B   |   M3   |  S   |  Must  | API sửa text trang          | 004        |

### Giai đoạn 2 — Biên tập & Xuất bản

Mục tiêu: _Sửa text trên UI, gán metadata, xuất EPUB, mở reader._

| Order |    ID    | Epic | Module | Size | MoSCoW | Tóm tắt               | depends_on |
| :---: | :------: | :--: | :----: | :--: | :----: | :-------------------- | :--------- |
|   6   | LDMS-006 |  B   |   M3   |  M   |  Must  | UI sửa text           | 005        |
|   7   | LDMS-011 |  B   |   M4   |  S   |  Must  | Metadata bắt buộc     | 002        |
|   8   | LDMS-007 |  B   |   M5   |  M   |  Must  | Xuất EPUB             | 005        |
|   9   | LDMS-013 |  B   | M4/M5  |  S   |  Must  | Publish gate metadata | 007, 011   |
|  10   | LDMS-008 |  C   |   M6   |  M   |  Must  | Reader mở EPUB        | 007        |

### Giai đoạn 3 — Xác thực & Tra cứu

Mục tiêu: _Đăng nhập, phân quyền, tìm kiếm, danh sách tài liệu._

| Order |    ID    | Epic | Module | Size | MoSCoW | Tóm tắt               | depends_on |
| :---: | :------: | :--: | :----: | :--: | :----: | :-------------------- | :--------- |
|  11   | LDMS-009 |  A   |   M8   |  M   |  Must  | Mock JWT + roles      | 001        |
|  12   | LDMS-010 |  A   | M1/M8  |  S   |  Must  | Access control        | 002, 009   |
|  13   | LDMS-012 |  B   |   M4   |  M   |  Must  | Category 2 cấp        | 011        |
|  14   | LDMS-015 |  C   |   M7   |  M   |  Must  | Search Postgres FTS   | 004, 011   |
|  15   | LDMS-016 |  C   |   M7   |  S   |  Must  | Snippet + link reader | 015, 008   |
|  16   | LDMS-026 |  B   | M1/M3  |  M   |  Must  | Document List UI      | 002, 006   |

### Giai đoạn 4 — Nâng cao trải nghiệm

Mục tiêu: _Split-screen, signed URL, Google OAuth, tùy chỉnh reader._

| Order |    ID    | Epic | Module | Size | MoSCoW | Tóm tắt                  | depends_on |
| :---: | :------: | :--: | :----: | :--: | :----: | :----------------------- | :--------- |
|  17   | LDMS-017 |  B   |   M3   |  M   | Should | Split-screen             | 006        |
|  18   | LDMS-014 |  C   |   M6   |  M   | Should | Signed URL + no download | 008, 010   |
|  19   | LDMS-018 |  A   |   M8   |  M   | Should | Google OAuth 2.0         | 009        |
|  20   | LDMS-019 |  C   |   M6   |  S   | Should | Reader font/nền          | 008        |
|  21   | LDMS-022 |  B   |   M2   |  S   | Should | OCR status + retry UI    | 003        |
|  22   | LDMS-020 |  C   |   M6   |  M   | Should | Bookmark                 | 009, 008   |

### Giai đoạn 5 — Hoàn thiện

Mục tiêu: _Tags, highlight, citation, search nâng cao._

| Order |    ID    | Epic | Module | Size | MoSCoW | Tóm tắt           | depends_on |
| :---: | :------: | :--: | :----: | :--: | :----: | :---------------- | :--------- |
|  23   | LDMS-023 |  B   |   M4   |  S   | Could  | Tags              | 012        |
|  24   | LDMS-021 |  C   |   M6   |  M   | Could  | Highlight + note  | 020        |
|  25   | LDMS-024 |  C   |   M4   |  S   | Could  | Citation APA/IEEE | 011        |
|  26   | LDMS-025 |  C   |   M7   |  M   | Could  | Elasticsearch     | 015        |

### Tham chiếu Epic → stories

- **Epic D (Platform):** LDMS-001
- **Epic A (Identity):** LDMS-009, LDMS-010, LDMS-018
- **Epic B (Digitize/Publish):** LDMS-002…007, LDMS-011…013, LDMS-017, LDMS-022, LDMS-023, LDMS-026
- **Epic C (Search/Reader):** LDMS-008, LDMS-014…016, LDMS-019…021, LDMS-024, LDMS-025

### Tổng backlog

**Tổng = 26 stories:** Must (16) · Should (7) · Could (3).

---

_Hết Product Backlog. Architecture & design: `docs/06-architecture.md`._
