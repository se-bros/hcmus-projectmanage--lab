# YÊU CẦU NGHIỆP VỤ VÀ SỔ TAY PRODUCT BACKLOG

## Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS (HCMUS-LDMS)

### THÔNG TIN TÀI LIỆU (DOCUMENT CONTROL)

| Trường thông tin (Field) | Nội dung đặc tả (Description) |
| :--- | :--- |
| **Mã tài liệu (Document ID)** | `HCMUS-LDMS-PBL` |
| **Tên tài liệu (Document Title)** | Sổ tay Product Backlog (Product Backlog Document) |
| **Dự án (Project Name)** | HCMUS-LDMS |
| **Đơn vị soạn thảo (Author/Organization)** | Nhóm Phát triển Dự án HCMUS-LDMS |
| **Người xem xét (Reviewer)** | Trưởng phòng CNTT & Giám đốc Thư viện |
| **Người phê duyệt (Approver)** | Ban Giám hiệu Trường ĐH Khoa học Tự nhiên |
| **Cấp độ bảo mật (Security Class)** | Internal (Nội bộ trường) |
| **Trạng thái tài liệu (Status)** | Ready for Pilot Implementation |

### LỊCH SỬ PHIÊN BẢN (REVISION HISTORY)

| Phiên bản (Version) | Ngày phát hành (Date) | Mô tả thay đổi (Description of Change) | Người thực hiện (Author) |
| :---: | :---: | :--- | :---: |
| 1.0 | 11/07/2026 | Khởi tạo dự thảo Product Backlog ban đầu (v1.0). | Mạch Quốc Tấn |
| 2.0 | 14/07/2026 | Chuẩn hóa định dạng User Story, bổ sung kịch bản AC, DoD, Sprint mapping. | Mạch Quốc Tấn |
| 3.0 | 15/07/2026 | Cập nhật nội dung: Kanban, cắt nhỏ story, gom module cho agent, DoD Pilot, thứ tự implement & đo throughput (giữ khung mục lục). | Nhóm phát triển |
| 3.1 | 15/07/2026 | Siết Acceptance Criteria toàn bộ 25 stories (điều kiện lỗi, verify được, GWT nơi cần). | Nhóm phát triển |

---

## Mục lục

* [1. Định nghĩa Hoàn thành và Quy tắc tổ chức](#1-định-nghĩa-hoàn-thành-và-quy-tắc-tổ-chức)
    * [1.1. Định nghĩa Hoàn thành (Definition of Done - DoD)](#11-định-nghĩa-hoàn-thành-definition-of-done---dod)
    * [1.2. Thang đo độ ưu tiên MoSCoW](#12-thang-đo-độ-ưu-tiên-moscow)
* [2. Chi tiết Product Backlog — User Story & Acceptance Criteria](#2-chi-tiết-product-backlog-user-story--acceptance-criteria)
    * [EPIC A — Xác thực & Phân quyền bảo mật (Security & Identity)](#epic-a-xác-thực--phân-quyền-bảo-mật-security--identity)
    * [EPIC B — Số hóa & Xuất bản (Digitization & Publish)](#epic-b-số-hóa--xuất-bản-digitization--publish)
    * [EPIC C — Tra cứu & Đọc sách (Search & Reader UX)](#epic-c-tra-cứu--đọc-sách-search--reader-ux)
    * [EPIC D — Nền tảng triển khai (Platform — Technical)](#epic-d-nền-tảng-triển-khai-platform--technical)
* [3. Bản đồ phân bổ Sprint (Sprint Mapping)](#3-bản-đồ-phân-bổ-sprint-sprint-mapping)

---

## 1. Định nghĩa Hoàn thành và Quy tắc tổ chức

Nhóm phát triển áp dụng **Kanban**: làm **từng card backlog** (WIP = 1 card / người hoặc / agent), gom theo **module** (M0–M8, xem `06-architecture.md`). Thời gian dev được forecast sau khi đo **số user story Done mỗi tuần** (deploy + AC), không dùng Story Point để nhân lịch.

**Definition of Ready (DoR):** Card chỉ được kéo vào *In Progress* khi có ID, AC test được, `depends_on` đã Done (nếu có), size S hoặc M (≤ 2 ngày). Card quá to phải tách trước.

**Chuẩn AC (bắt buộc khi review/PR):** Mỗi story có đủ AC để dev/agent **tự kiểm pass/fail** — gồm: hành vi đúng (happy path), ít nhất một **trường hợp lỗi/biên** nếu story đụng API/UI, và cách **verify** (HTTP status, UI quan sát được, hoặc lệnh). PR phải checklist từng AC: Pass / Fail / N/A.

**Giao agent:** một phiên chỉ implement **một** ID; prompt kèm **toàn bộ AC** + module + dependency; không “tiện thể” làm card khác; không Done nếu còn AC Fail.

### 1.1. Định nghĩa Hoàn thành (Definition of Done - DoD)

Một User Story chỉ được coi là hoàn thành (`Done`) khi đáp ứng đủ các tiêu chí sau (theo giai đoạn):

**DoD-Pilot** (tuần đo throughput / implement sớm):

1. **AC:** Toàn bộ Acceptance Criteria của card đã pass.
2. **Code Quality:** Không hardcode secret; mã nguồn merge vào nhánh chính qua Pull Request (có review hoặc self-review checklist có ghi log).
3. **Deployment:** Chạy được trên môi trường thống nhất (`docker compose` hoặc script dev tương đương trong repo).
4. **Documentation:** Endpoint mới ghi tối thiểu trong OpenAPI/Swagger hoặc README module; PR liệt kê AC pass/fail.
5. **Đo lường:** Ghi nhận thời gian thực hiện (và token AI nếu có) phục vụ forecast — schema log sẽ chuẩn hóa bằng skill team.

**DoD-Release** (trước demo / UAT — bổ sung thêm):

1. CI xanh; deploy staging nếu đã có.
2. Không còn cảnh báo lint nghiêm trọng (ESLint/PyLint) trên phần đụng tới.
3. Test tự động cho path chính của story (khi đã có khung test).
4. API Swagger cập nhật đầy đủ.

> Chỉ đếm throughput \(T\) = số story **Done** trong 7 ngày theo **cùng một** mức DoD (tuần pilot: DoD-Pilot).

### 1.2. Thang đo độ ưu tiên MoSCoW

* **Must-have (M):** Bắt buộc cho lát mỏng E2E (thin slice) và MVP dùng được — tương ứng hàng **P0–P1**, làm theo thứ tự ở mục 3.
* **Should-have (S):** Tối ưu UX / vận hành sau khi thin slice đã xong (**P2**).
* **Could-have (C):** Làm nếu còn throughput (**P3**).
* **Won't-have (W):** Hoãn: AI/RAG, chống đạo văn, load test 500 user như AC story, “chặn copy tuyệt đối”.

**Size (thay cho Story Point khi forecast):** S ≤ 1 ngày, M ≤ 2 ngày. Không dùng tổng SP để ra số tuần. Forecast: \( \text{Dev weeks} \approx N_{\text{còn lại}} / T \) với \(T\) = story Done/tuần; báo cáo dạng **khoảng**; có thể nhờ LLM phản biện danh sách còn lại (không thay số đo thật).

**Client time vs Dev time:** mốc Proposal (client) và dự báo từ throughput (dev) là hai con số; nếu dev > client → cắt scope, không bịa \(T\).

---

## 2. Chi tiết Product Backlog — User Story & Acceptance Criteria

Mỗi story có: **ID** (`LDMS-xxx`), **Module**, **Size**, **depends_on**, **MoSCoW**, **AC**. Chi tiết API/state: `06-architecture.md`.

**Module (gom cho agent):** M0 Platform · M1 Documents & Storage · M2 OCR · M3 Editor · M4 Metadata · M5 Publish EPUB · M6 Reader · M7 Search · M8 Identity.

---

### EPIC D — Nền tảng triển khai (Platform — Technical)

> Technical enabler — làm trước để team/agent chung một môi trường. (Bổ sung epic kỹ thuật; không đổi các epic nghiệp vụ A–C.)

#### LDMS-001: Bootstrap môi trường monorepo + Docker Compose
* **User Story:** Là lập trình viên, tôi muốn một lệnh khởi động API + DB + storage thống nhất để cả nhóm implement cùng một môi trường.
* **Module:** M0 | **Size:** M | **Độ ưu tiên:** Must (P0) | **depends_on:** —
* **Tiêu chí chấp nhận (Acceptance Criteria):**
  * **AC 1:** Given repo mới clone, When chạy lệnh start trong README (compose hoặc script), Then trong ≤ 5 phút các service **API + PostgreSQL + S3 storage (MinIO)** ở trạng thái healthy/up.
  * **AC 2:** `GET /health` (hoặc `/api/health`) trả **HTTP 200** và body có tín hiệu sống (vd. `{"status":"ok"}` hoặc tương đương).
  * **AC 3:** Có `.env.example` liệt kê biến bắt buộc (DB URL, S3 endpoint/access key/secret key…); README ghi **port** API và FE.
  * **AC 4:** Frontend skeleton: `npm install && npm run dev` (hoặc lệnh tương đương) chạy được **hoặc** README nêu rõ lệnh + screenshot/log mẫu.
  * **AC 5 (lỗi):** Thiếu biến env bắt buộc → service fail với log/message rõ, không “treo im lặng”.
* **Out of scope:** Keycloak, Elasticsearch, CI đầy đủ.

---

### EPIC A — Xác thực & Phân quyền bảo mật (Security & Identity)

#### LDMS-009: Đăng nhập dev (Mock JWT + roles)
* **User Story:** Là độc giả/biên tập viên, tôi muốn đăng nhập môi trường dev với vai trò rõ ràng để hệ thống cấp quyền giao diện và API phù hợp (trước khi gắn SSO trường).
* **Module:** M8 | **Size:** M | **Độ ưu tiên:** Must (P1) | **depends_on:** LDMS-001
* **Ghi chú:** Có thể làm song song sau LDMS-001 nếu đủ người. **Thin slice P0 cho phép localhost không auth.**
* **Tiêu chí chấp nhận (Acceptance Criteria):**
  * **AC 1:** Given auth dev bật, When gọi endpoint cấp token (vd. `POST /auth/dev-token`) với role `reader`|`editor`|`admin`, Then nhận JWT hợp lệ (decode được `sub`/`role` hoặc claim tương đương).
  * **AC 2:** Given token `reader`, When gọi API ghi (upload / OCR / publish), Then **401/403**.
  * **AC 3:** Given token `editor` hoặc `admin`, When gọi cùng API ghi, Then **không** bị từ chối vì thiếu quyền (có thể 4xx vì lý do khác, không phải authz).
  * **AC 4:** Given không gửi token (auth bật), When gọi API ghi, Then **401**.
  * **AC 5:** README: flag bật/tắt mock auth + ví dụ `curl` lấy token từng role.
* **Out of scope:** Keycloak/LDAP thật (xem LDMS-018).

#### LDMS-018: Đăng nhập SSO Keycloak (OIDC)
* **User Story:** Là độc giả (sinh viên/giảng viên/thủ thư), tôi muốn đăng nhập bằng tài khoản trường qua OIDC/Keycloak để hệ thống xác nhận vai trò thật.
* **Module:** M8 | **Size:** M | **Độ ưu tiên:** Must (P1, khi có env) | **depends_on:** LDMS-009
* **Tiêu chí chấp nhận (Acceptance Criteria):**
  * **AC 1:** Given user chưa đăng nhập, When mở `/login` và chọn đăng nhập HCMUS, Then browser redirect tới IdP OIDC/Keycloak (URL cấu hình được bằng env).
  * **AC 2:** Given đăng nhập IdP thành công, When callback về app, Then session/JWT có identity + roles; app map được ít nhất một role nghiệp vụ (`reader` / `editor` / `admin` hoặc tương đương đã document).
  * **AC 3:** Given `AUTH_MODE=oidc` (hoặc flag tương đương), When app chạy, Then **mock dev-token bị tắt** (gọi dev-token → 404/403/disabled).
  * **AC 4:** Client secret/issuer chỉ lấy từ env/secret store; `git grep` không thấy secret production hardcode trong repo.
  * **AC 5:** Given access token hết hạn, When gọi API được bảo vệ, Then 401 và UI yêu cầu đăng nhập lại **hoặc** refresh thành công (chọn một, ghi README).
* **Out of scope:** Tự host Keycloak production HA.

#### LDMS-010: Kiểm soát quyền truy cập tài liệu
* **User Story:** Là sinh viên, tôi chỉ muốn nhìn thấy và đọc các tài liệu mà tôi được phép tiếp cận.
* **Module:** M1 + M8 | **Size:** S | **Độ ưu tiên:** Must (P1) | **depends_on:** LDMS-002, LDMS-009
* **Tiêu chí chấp nhận (Acceptance Criteria):**
  * **AC 1:** Document lưu `access_level` ∈ {`public`, `internal`, `restricted`}; giá trị khác khi create/update → **400**.
  * **AC 2:** Given document `restricted` và user role không đủ quyền, When `GET` list/search/get/read-url, Then **không** trả nội dung (ẩn khỏi list **hoặc** 403 — chọn một, ghi OpenAPI).
  * **AC 3:** Given document `internal` và request **không** auth, When get/list/search, Then không đọc được nội dung (401/403/ẩn).
  * **AC 4:** Given document `public`, When guest (không token) gọi get/read theo policy guest, Then đọc được (200).
  * **AC 5:** Có kịch bản kiểm thử (manual `curl` hoặc test) với **≥ 2 role** khác nhau; kết quả khớp AC 2–4.

---

### EPIC B — Số hóa & Xuất bản (Digitization & Publish)

#### LDMS-002: Tải lên tệp scan gốc
* **User Story:** Là thủ thư, tôi muốn tải lên tệp PDF hoặc ảnh scan sách giấy gốc để hệ thống bắt đầu xử lý luồng số hóa.
* **Module:** M1 | **Size:** M | **Độ ưu tiên:** Must (P0) | **depends_on:** LDMS-001
* **Tiêu chí chấp nhận (Acceptance Criteria):**
  * **AC 1:** Given file `.pdf` / `.jpg` / `.png` hợp lệ, When `POST` upload, Then **201/200** và body có `document_id`.
  * **AC 2:** Given file type không hỗ trợ (vd. `.exe` / `.docx`), When upload, Then **4xx** + message rõ (không tạo document orphan).
  * **AC 3:** Given file &gt; giới hạn (mặc định **100 MB**, cấu hình được), When upload, Then **413** hoặc 400 tương đương; không lưu file dở.
  * **AC 4:** `GET /documents/{id}` trả `id`, `original_filename`, `status=uploaded` (hoặc enum tương đương), `created_at`.
  * **AC 5:** File nằm trên storage; có API/dev path đọc lại bytes theo `document_id` (smoke test so hash/size).
  * **AC 6:** Given `document_id` không tồn tại, When GET, Then **404**.
* **Out of scope:** OCR, thanh progress UI bắt buộc (có thể bổ sung sau).

#### LDMS-003: Hàng đợi OCR và trạng thái job
* **User Story:** Là thủ thư, tôi muốn hệ thống chạy OCR nền và tôi theo dõi được trạng thái xử lý.
* **Module:** M2 | **Size:** M | **Độ ưu tiên:** Must (P0) | **depends_on:** LDMS-002
* **Tiêu chí chấp nhận (Acceptance Criteria):**
  * **AC 1:** Given document đã upload, When kích hoạt OCR (auto sau upload **hoặc** `POST .../ocr`), Then tạo job với `status=pending` (hoặc chuyển nhanh sang `processing`).
  * **AC 2:** Job trải qua `processing` rồi kết thúc `completed` **hoặc** `failed` (quan sát qua GET status).
  * **AC 3:** `POST` kích hoạt OCR trả về **nhanh** (thường &lt; 5s) — không chờ OCR xong toàn bộ tài liệu trong một HTTP request đồng bộ.
  * **AC 4:** Given job `failed`, When GET status, Then có `error_message` không rỗng.
  * **AC 5:** Given `document_id` không tồn tại, When enqueue OCR, Then **404**.
* **Out of scope:** Ngưỡng CAR ≥ 85% (metric chất lượng/PoC, **không** phải điều kiện Done story).

#### LDMS-004: Kết quả OCR theo từng trang
* **User Story:** Là thủ thư, tôi muốn nhận văn bản OCR tách theo từng trang sách để biên tập.
* **Module:** M2 | **Size:** M | **Độ ưu tiên:** Must (P0) | **depends_on:** LDMS-003
* **Tiêu chí chấp nhận (Acceptance Criteria):**
  * **AC 1:** Given OCR job `completed` trên file mẫu repo, When `GET /documents/{id}/pages`, Then có ≥ 1 page với `page_number` bắt đầu từ **1** và field `text_content` (string, có thể rỗng nếu trang trống nhưng field phải có).
  * **AC 2:** Given PDF mẫu nhiều trang (hoặc fixture), When OCR xong, Then số page ≥ 2 và `page_number` không trùng.
  * **AC 3:** Given ảnh đơn trang, When OCR xong, Then đúng **1** page (hoặc document rõ policy nếu tool split khác — ghi README).
  * **AC 4:** Repo có `samples/` (PDF và/hoặc ảnh) + README/PR mô tả lệnh chạy AC lặp lại.
  * **AC 5:** Given document chưa OCR xong, When GET pages, Then **409/404/[]** theo convention đã chọn (ghi OpenAPI) — không 500.
* **Out of scope:** Đánh giá % ký tự đúng (CAR).

#### LDMS-005: API đọc và cập nhật text trang
* **User Story:** Là biên tập viên, tôi muốn đọc và sửa text một trang qua API trước khi có UI đầy đủ.
* **Module:** M3 | **Size:** S | **Độ ưu tiên:** Must (P0) | **depends_on:** LDMS-004
* **Tiêu chí chấp nhận (Acceptance Criteria):**
  * **AC 1:** Given page tồn tại, When `GET .../pages/{n}`, Then **200** + `text_content` + `page_number`.
  * **AC 2:** Given `PUT`/`PATCH` body `{"text_content":"hello-ac"}`, When GET lại, Then `text_content` = `hello-ac`.
  * **AC 3:** Given `page_number` không tồn tại, When GET hoặc PUT, Then **404**.
  * **AC 4:** Given body thiếu `text_content` (hoặc null không hợp lệ), When PUT, Then **422/400**.

#### LDMS-006: UI biên tập text tối thiểu
* **User Story:** Là biên tập viên, tôi muốn sửa text OCR trên giao diện và lưu lại.
* **Module:** M3 | **Size:** M | **Độ ưu tiên:** Must (P0) | **depends_on:** LDMS-005
* **Tiêu chí chấp nhận (Acceptance Criteria):**
  * **AC 1:** Given document có ≥ 1 page, When mở màn editor, Then thấy danh sách/chỉ số trang chọn được.
  * **AC 2:** Given sửa text và bấm Lưu, When request thành công, Then UI báo saved; F5/reload vẫn còn text đã sửa.
  * **AC 3:** UI có trạng thái **saving / saved / error** (quan sát được).
  * **AC 4:** Given API lưu trả lỗi (simulate tắt API hoặc 500), When bấm Lưu, Then UI ở trạng thái error và **không** báo saved giả.

#### LDMS-017: Biên tập Split-screen (ảnh + text)
* **User Story:** Là biên tập viên, tôi muốn so sánh ảnh scan và văn bản OCR song song để hiệu chỉnh nhanh.
* **Module:** M3 | **Size:** M | **Độ ưu tiên:** Must (P1) | **depends_on:** LDMS-006
* **Tiêu chí chấp nhận (Acceptance Criteria):**
  * **AC 1:** Given đang ở page N, When mở split-screen, Then **cùng page N**: vùng trái = preview ảnh/PDF page (nếu có), vùng phải = editor text page N.
  * **AC 2:** Đổi sang page M → cả hai vùng (hoặc editor + label) theo page M, không lệch page.
  * **AC 3:** Given chưa có image page, When mở split-screen, Then vùng trái placeholder có message; vùng phải **vẫn edit/lưu text** được.
  * **AC 4:** PR mô tả limitation nếu preview chưa đủ (zoom/rotate không bắt buộc P1).
* **Out of scope (tách sau nếu cần):** crop ảnh nhúng, toolbar heading đầy đủ, autosave 30s.

#### LDMS-026: Danh sách tài liệu (Document List UI)
* **User Story:** Là biên tập viên, tôi muốn xem danh sách tài liệu đã tải lên để biết trạng thái và thao tác tiếp (sửa text, xuất bản, mở reader).
* **Module:** M1 + M3 | **Size:** M | **Độ ưu tiên:** Must (P1) | **depends_on:** LDMS-002, LDMS-006
* **Tiêu chí chấp nhận (Acceptance Criteria):**
  * **AC 1:** Given có ≥ 1 document trong hệ thống, When mở trang danh sách, Then thấy bảng/list documents với: `title` (hoặc `original_filename`), `status`, `created_at`.
  * **AC 2:** Given document có `status=uploaded`/`ocr_completed`/`published`, When nhìn list, Then trạng thái hiển thị rõ (label/badge/icon) — không cần phải gọi API chi tiết từng document.
  * **AC 3:** Given click vào document, When điều hướng, Then mở đúng trang editor (LDMS-006) **hoặc** reader (LDMS-008) tuỳ trạng thái.
  * **AC 4:** Given không có document nào, When mở trang, Then UI hiển thị empty state ("Chưa có tài liệu") — không màn trắng/lỗi.
  * **AC 5:** Trang có nút/link upload dẫn đến flow tải lên (hoặc tích hợp form upload tối thiểu).

#### LDMS-011: Gán siêu dữ liệu bắt buộc
* **User Story:** Là thủ thư, tôi muốn nhập thông tin mô tả sách để độc giả tra cứu và để được phép xuất bản.
* **Module:** M4 | **Size:** S | **Độ ưu tiên:** Must (P1) | **depends_on:** LDMS-002
* **Tiêu chí chấp nhận (Acceptance Criteria):**
  * **AC 1:** Given PATCH/PUT metadata hợp lệ, When lưu `title`, `author`, `access_level` (và optional `shelf_location`), Then GET document trả đúng các field đó.
  * **AC 2:** Given `title` hoặc `author` rỗng/whitespace khi endpoint yêu cầu bắt buộc, When lưu, Then **400/422** + chỉ rõ field lỗi.
  * **AC 3:** Given `access_level` không thuộc enum, When lưu, Then **400/422**.
  * **AC 4:** `shelf_location` optional: bỏ trống vẫn lưu được các field khác.

#### LDMS-012: Quản lý Category (2 cấp)
* **User Story:** Là admin, tôi muốn cấu hình cây danh mục để tổ chức tài liệu.
* **Module:** M4 | **Size:** M | **Độ ưu tiên:** Must (P1) | **depends_on:** LDMS-011
* **Tiêu chí chấp nhận (Acceptance Criteria):**
  * **AC 1:** Tạo category **parent** và category **con** (`parent_id`) thành công; GET tree/list thể hiện quan hệ 2 cấp.
  * **AC 2:** Gán `category_id` cho document; GET document thấy category đã gán.
  * **AC 3:** Given tên trùng sau normalize (trim + case-insensitive) trong cùng không gian đặt tên, When tạo, Then **409/400**.
  * **AC 4:** Given category id không tồn tại, When gán vào document, Then **400/404**.
  * **AC 5:** Xóa/cập nhật tên category hoạt động (hoặc soft-delete có document) — hành vi ghi rõ OpenAPI; không 500.

#### LDMS-007: Đóng gói & xuất EPUB
* **User Story:** Là thủ thư, tôi muốn đóng gói nội dung đã biên tập thành file EPUB để độc giả đọc trực tuyến.
* **Module:** M5 | **Size:** M | **Độ ưu tiên:** Must (P0) | **depends_on:** LDMS-005
* **Tiêu chí chấp nhận (Acceptance Criteria):**
  * **AC 1:** Given document có ≥ 1 page có text, When `POST .../publish`, Then tạo file EPUB trên storage và response/job thành công.
  * **AC 2:** Document sau publish có `epub_storage_key` (hoặc tương đương) và `status` ∈ {`published`, `epub_ready`} theo enum architecture.
  * **AC 3:** Thứ tự nội dung EPUB theo `page_number` tăng dần (kiểm bằng mở file hoặc extract text chapter/page).
  * **AC 4:** File mở được bằng Epub.js hoặc ebook viewer (smoke: thấy text đã put vào page).
  * **AC 5:** Given document **không** có page/text, When publish, Then **400** + message rõ; status không thành published.
  * **AC 6:** Given publish fail giữa chừng (nếu mô phỏng được), Then `publish_failed` hoặc job `failed` + error_message — không để status published giả.
* **Out of scope:** Index Elasticsearch trong cùng card; epubcheck bắt buộc (khuyến nghị).

#### LDMS-013: Chặn xuất bản khi thiếu metadata
* **User Story:** Là thủ thư, tôi không muốn xuất bản nhầm sách thiếu thông tin bắt buộc.
* **Module:** M4 + M5 | **Size:** S | **Độ ưu tiên:** Must (P1) | **depends_on:** LDMS-007, LDMS-011
* **Tiêu chí chấp nhận (Acceptance Criteria):**
  * **AC 1:** Given thiếu `title` (null/rỗng), When publish, Then **400** và **không** tạo EPUB mới / không chuyển published.
  * **AC 2:** Tương tự lần lượt thiếu `author` hoặc `access_level` → **400**.
  * **AC 3:** Given đủ `title` + `author` + `access_level` và có page text, When publish, Then thành công như LDMS-007.
  * **AC 4:** Message lỗi chỉ rõ field metadata nào thiếu (để UI hiển thị).

#### LDMS-022: UI trạng thái OCR + retry
* **User Story:** Là biên tập viên, tôi muốn thấy job OCR lỗi và chạy lại được.
* **Module:** M2 | **Size:** S | **Độ ưu tiên:** Should (P2) | **depends_on:** LDMS-003
* **Tiêu chí chấp nhận (Acceptance Criteria):**
  * **AC 1:** Given document đang/đã OCR, When mở chi tiết document, Then thấy state job hiện tại (`pending`/`processing`/`completed`/`failed`) — UI hoặc trang dev tối thiểu.
  * **AC 2:** Given state `failed`, When bấm Retry, Then tạo job mới (id khác hoặc attempt tăng) và state chuyển khỏi `failed` về `pending`/`processing`.
  * **AC 3:** Given state `completed` hoặc `processing`, When Retry (nếu cho phép), Then hành vi đã định nghĩa (chặn 409 **hoặc** cho re-OCR) và ghi OpenAPI/UI.
  * **AC 4:** Khi `failed`, UI/API vẫn show `error_message` (không chỉ mã lỗi chung).

#### LDMS-023: Tags + autocomplete
* **User Story:** Là thủ thư, tôi muốn gắn tag linh hoạt cho tài liệu.
* **Module:** M4 | **Size:** S | **Độ ưu tiên:** Should (P2) | **depends_on:** LDMS-012
* **Tiêu chí chấp nhận (Acceptance Criteria):**
  * **AC 1:** Given document, When thêm tag `"machine-learning"`, Then GET document/tags chứa tag đó.
  * **AC 2:** Xóa tag → GET không còn tag đó trên document.
  * **AC 3:** Autocomplete: gõ prefix trả gợi ý từ tag đã có (ít nhất match prefix).
  * **AC 4:** `"ML"` và `" ml "` (sau normalize) không tạo hai tag trùng nghĩa — policy normalize (lower/trim) được document và có test.

---

### EPIC C — Tra cứu & Đọc sách (Search & Reader UX)

#### LDMS-008: Đọc sách EPUB trên web (tối thiểu)
* **User Story:** Là độc giả, tôi muốn mở sách EPUB trên trình duyệt sau khi biên tập viên xuất bản.
* **Module:** M6 | **Size:** M | **Độ ưu tiên:** Must (P0) | **depends_on:** LDMS-007
* **Tiêu chí chấp nhận (Acceptance Criteria):**
  * **AC 1:** Given document `published` có EPUB, When mở reader với `document_id`, Then FE lấy được nội dung EPUB (blob URL / signed URL / proxy) **không** 404.
  * **AC 2:** Epub.js (hoặc lib tương đương) render được **ít nhất** phần đầu nội dung có text đã biết từ fixture.
  * **AC 3:** Given document chưa publish / không có EPUB, When mở reader, Then UI message lỗi rõ (tiếng Việt hoặc i18n key), **không** màn trắng / uncaught exception.
  * **AC 4:** Given `document_id` sai, When mở reader, Then 404/message “không tìm thấy”.

#### LDMS-014: Giảm rủi ro tải file gốc khi đọc
* **User Story:** Là độc giả, tôi muốn đọc sách mà hệ thống không khuyến khích tải file EPUB gốc về máy.
* **Module:** M6 | **Size:** M | **Độ ưu tiên:** Must (P1) | **depends_on:** LDMS-008, LDMS-010
* **Tiêu chí chấp nhận (Acceptance Criteria):**
  * **AC 1:** Trên UI reader **không** có control “Download EPUB” / “Tải sách” trỏ file gốc.
  * **AC 2:** Given S3 storage (MinIO) + signed URL, When `GET read-url`, Then response có `expires_in` (hoặc `expires_at`); mặc định cấu hình **15 phút** (± clock skew document).
  * **AC 3:** Given URL đã hết hạn, When fetch trực tiếp URL cũ, Then **403/401/denied** (không đọc được EPUB).
  * **AC 4:** README mục Security: residual risk (screenshot, DevTools) — **cấm** wording “chống sao chép tuyệt đối”.
* **Out of scope:** Chặn Ctrl+C / PrintScreen như yêu cầu bảo mật.

#### LDMS-015: Tìm kiếm metadata và full-text tối thiểu
* **User Story:** Là độc giả, tôi muốn tìm sách theo từ khóa trong tiêu đề/tác giả/nội dung đã OCR.
* **Module:** M7 | **Size:** M | **Độ ưu tiên:** Must (P1) | **depends_on:** LDMS-004, LDMS-011
* **Tiêu chí chấp nhận (Acceptance Criteria):**
  * **AC 1:** Given document title chứa từ khóa unique `XYZTEST`, When `GET /search?q=XYZTEST`, Then hit có `document_id` đó.
  * **AC 2:** Given chỉ có trong `text_content` page (không có trong title), When search từ khóa đó, Then vẫn hit document (full-text).
  * **AC 3:** Given auth bật và document `restricted` với user không đủ quyền, When search, Then document đó **không** có trong kết quả.
  * **AC 4:** Given `q` rỗng hoặc chỉ whitespace, When search, Then **400** **hoặc** `[]` — một convention, ghi OpenAPI.
  * **AC 5:** Không 500 trên query bình thường; lỗi server phải log được.
* **Out of scope:** 500 concurrent &lt; 3s; Elasticsearch (LDMS-025).

#### LDMS-016: Snippet kết quả và mở reader
* **User Story:** Là độc giả, tôi muốn thấy đoạn trích chứa từ khóa và mở đúng sách để đọc.
* **Module:** M7 | **Size:** S | **Độ ưu tiên:** Must (P1) | **depends_on:** LDMS-015, LDMS-008
* **Tiêu chí chấp nhận (Acceptance Criteria):**
  * **AC 1:** Mỗi hit trong response/UI có field `snippet` (hoặc tương đương) độ dài giới hạn (vd. ≤ 300 ký tự) và liên quan query.
  * **AC 2:** Snippet chứa từ khóa (hoặc dạng stem/highlight) — kiểm bằng fixture.
  * **AC 3:** Given click hit / follow `reader_url` hoặc `document_id`, When điều hướng, Then mở reader **đúng** document đó (so `document_id`).
  * **AC 4:** Hit không có quyền → không xuất hiện (kế thừa LDMS-015); không deep-link lọt read nếu 403.

#### LDMS-019: Tùy chỉnh giao diện đọc sách
* **User Story:** Là độc giả, tôi muốn chỉnh cỡ chữ và màu nền khi đọc.
* **Module:** M6 | **Size:** S | **Độ ưu tiên:** Should (P2) | **depends_on:** LDMS-008
* **Tiêu chí chấp nhận (Acceptance Criteria):**
  * **AC 1:** Control tăng/giảm cỡ chữ hoạt động trong khoảng **80%–200%** (quan sát CSS/font-size hoặc UI label).
  * **AC 2:** Chuyển được **Light** và **Dark** (Sepia optional); màu nền/chữ đổi tương ứng, vẫn đọc được text.
  * **AC 3:** Chọn được font **Serif** và **Sans-serif** (OpenDyslexic optional).
  * **AC 4:** Preference giữ khi reload reader **cùng browser** (localStorage/user setting) — nếu chưa persist user server, ghi rõ client-only.

#### LDMS-020: Đánh dấu trang (Bookmark)
* **User Story:** Là độc giả, tôi muốn hệ thống nhớ vị trí đọc dở.
* **Module:** M6 | **Size:** M | **Độ ưu tiên:** Should (P2) | **depends_on:** LDMS-009, LDMS-008
* **Tiêu chí chấp nhận (Acceptance Criteria):**
  * **AC 1:** Given user đã login + document đang đọc, When lưu bookmark (auto hoặc nút), Then API/DB có bản ghi theo `(user_id, document_id)` với vị trí (CFI hoặc page/offset).
  * **AC 2:** Given đã có bookmark, When đóng và mở lại reader cùng user/document, Then nhảy về vị trí đã lưu (sai số chấp nhận document nếu CFI xấp xỉ).
  * **AC 3:** Given user B, When mở cùng document, Then **không** nhận bookmark của user A.
  * **AC 4:** Given chưa login (nếu auth bắt buộc), When lưu bookmark, Then 401 hoặc disable control.

#### LDMS-021: Highlight và ghi chú
* **User Story:** Là độc giả, tôi muốn highlight đoạn văn và gắn ghi chú.
* **Module:** M6 | **Size:** M | **Độ ưu tiên:** Should (P2) | **depends_on:** LDMS-020
* **Tiêu chí chấp nhận (Acceptance Criteria):**
  * **AC 1:** Given chọn một đoạn text trên reader, When tạo highlight, Then đoạn được đánh dấu (ít nhất **1** màu) và persist theo user+document.
  * **AC 2:** Có thể gắn `note` text optional; GET lại còn note.
  * **AC 3:** Xóa highlight → không còn trên UI sau reload.
  * **AC 4:** User khác không thấy highlight của user hiện tại.
  * **AC 5:** Given payload note quá dài (nếu có max), When tạo, Then 400 — max length ghi OpenAPI.

#### LDMS-024: Trích dẫn tự động (Citation)
* **User Story:** Là độc giả, tôi muốn sinh chuỗi trích dẫn APA/IEEE từ metadata sách.
* **Module:** M4 | **Size:** S | **Độ ưu tiên:** Could (P3) | **depends_on:** LDMS-011
* **Tiêu chí chấp nhận (Acceptance Criteria):**
  * **AC 1:** Given document có `title` + `author`, When gọi citation API hoặc bấm nút UI, Then trả **hai** chuỗi: APA 7th-ish và IEEE-ish (format ổn định, có test fixture).
  * **AC 2:** Chuỗi chứa title và author đã lưu (không hardcode một cuốn mẫu duy nhất).
  * **AC 3:** Given thiếu title/author, When citation, Then 400 hoặc chuỗi ghi “thiếu metadata” — không 500.
  * **AC 4:** Năm xuất bản optional: có field thì xuất hiện trong citation; không có thì format vẫn hợp lệ theo rule đã chọn.

#### LDMS-025: Tìm kiếm Elasticsearch nâng cao
* **User Story:** Là độc giả, tôi muốn tìm kiếm mượt hơn (fuzzy, scale) khi Postgres FTS không đủ.
* **Module:** M7 | **Size:** M | **Độ ưu tiên:** Could (P3) | **depends_on:** LDMS-015
* **Tiêu chí chấp nhận (Acceptance Criteria):**
  * **AC 1:** Given ES up + document đã publish/OCR, When index pipeline chạy, Then document searchable qua ES (prove bằng search hit).
  * **AC 2:** `GET /search?q=` (hoặc endpoint ES mode) trả kết quả từ ES khi feature flag bật.
  * **AC 3:** Có **ít nhất 1** test case fuzzy/không dấu (fixture + expected hit) nếu bật analyzer tiếng Việt; nếu chưa bật, PR ghi rõ “not enabled” và AC 3 = N/A có lý do.
  * **AC 4:** Given ES down, When search, Then fallback FTS **hoặc** 503 rõ ràng — không treo/500 mơ hồ.
* **Out of scope:** Bắt buộc cho MVP; không chặn thin slice.

---

## 3. Bản đồ phân bổ Sprint (Sprint Mapping)

> **Cách đọc mục này (Kanban):** Nhóm **không** cố định sprint 2 tuần kiểu Scrum. “Sprint” dưới đây = **lô giao hàng / hàng ưu tiên**. Làm **từng story theo Order**. Cuối mỗi **7 ngày**, đếm story **Done** (= deploy + AC theo DoD đang dùng) → throughput \(T\) → forecast \(N/T\) tuần (khoảng).

### 3.1. Lô P0 — Thin vertical slice (làm trước, mục tiêu đo \(T\) tuần đầu)

Mục tiêu: *Upload → OCR theo trang → sửa text → EPUB → đọc web.*

| Order | ID | Epic | Module | Size | Tóm tắt |
| :---: | :---: | :---: | :---: | :---: | :--- |
| 1 | LDMS-001 | D | M0 | M | Compose + health |
| 2 | LDMS-002 | B | M1 | M | Upload + Document |
| 3 | LDMS-003 | B | M2 | M | Job OCR + state |
| 4 | LDMS-004 | B | M2 | M | Text theo trang |
| 5 | LDMS-005 | B | M3 | S | API sửa text trang |
| 6 | LDMS-006 | B | M3 | M | UI sửa text |
| 7 | LDMS-007 | B | M5 | M | Xuất EPUB |
| 8 | LDMS-008 | C | M6 | M | Reader mở EPUB |

**Tổng backlog = 26 stories** (`LDMS-001` … `LDMS-026`).  
**\(N_{P0} = 8\)** · **\(N_{P1} = 11\)** · **\(N_{P2} = 5\)** · **\(N_{P3} = 2\)**.  
Sau tuần 1 / xong P0: chốt \(T\), forecast \(N_{\text{còn}}/T\) (khoảng).

### 3.2. Lô P1 — MVP bổ sung

| Order | ID | Epic | Module | Size | Tóm tắt |
| :---: | :---: | :---: | :---: | :---: | :--- |
| 9 | LDMS-009 | A | M8 | M | Mock JWT + roles |
| 10 | LDMS-010 | A | M1/M8 | S | Access level |
| 11 | LDMS-011 | B | M4 | S | Metadata bắt buộc |
| 12 | LDMS-012 | B | M4 | M | Category 2 cấp |
| 13 | LDMS-013 | B | M4/M5 | S | Publish gate metadata |
| 14 | LDMS-014 | C | M6 | M | Read URL hạn + no download |
| 15 | LDMS-015 | C | M7 | M | Search FTS tối thiểu |
| 16 | LDMS-016 | C | M7 | S | Snippet + link reader |
| 17 | LDMS-017 | B | M3 | M | Split-screen |
| 18 | LDMS-018 | A | M8 | M | Keycloak/OIDC thật |
| 19 | LDMS-026 | B | M1/M3 | M | Document List UI |

### 3.3. Lô P2 — Should

| Order | ID | Size | Tóm tắt |
| :---: | :---: | :---: | :--- |
| 20 | LDMS-019 | S | Reader font/nền |
| 21 | LDMS-020 | M | Bookmark |
| 22 | LDMS-021 | M | Highlight + note |
| 23 | LDMS-022 | S | OCR status + retry UI |
| 24 | LDMS-023 | S | Tags |

### 3.4. Lô P3 — Could

| Order | ID | Size | Tóm tắt |
| :---: | :---: | :---: | :--- |
| 25 | LDMS-024 | S | Citation APA/IEEE |
| 26 | LDMS-025 | M | Elasticsearch |

### 3.5. Tham chiếu mapping cũ (Epic → stories)

* **Epic D (Platform):** LDMS-001  
* **Epic A (Security):** LDMS-009, LDMS-010, LDMS-018  
* **Epic B (Digitize/Publish):** LDMS-002…007, LDMS-011…013, LDMS-017, LDMS-022, LDMS-023, LDMS-026  
* **Epic C (Search/Reader):** LDMS-008, LDMS-014…016, LDMS-019…021, LDMS-024, LDMS-025  

### 3.6. Prompt khung cho agent

```text
Implement ONLY card {ID}: {Title}
Module: {M#} | Size: {S|M} | depends_on: {ids already Done}
AC: (paste from this document)
Architecture: docs/06-architecture.md (module + API/state if needed)
DoD: DoD-Pilot
Do not implement other backlog items.
```

---

*Hết Product Backlog. Architecture & design: `docs/06-architecture.md`.*
