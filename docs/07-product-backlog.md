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
| **Trạng thái tài liệu (Status)** | Under Review (Đang thẩm định) |

### LỊCH SỬ PHIÊN BẢN (REVISION HISTORY)

| Phiên bản (Version) | Ngày phát hành (Date) | Mô tả thay đổi (Description of Change) | Người thực hiện (Author) |
| :---: | :---: | :--- | :---: |
| 1.0 | 11/07/2026 | Khởi tạo dự thảo Product Backlog ban đầu (v1.0). | Mạch Quốc Tấn |
| 2.0 | 14/07/2026 | Chuẩn hóa định dạng User Story, bổ sung kịch bản AC, DoD, Sprint mapping. | Mạch Quốc Tấn |

---

## Mục lục

* [1. Định nghĩa Hoàn thành và Quy tắc tổ chức](#1-định-nghĩa-hoàn-thành-và-quy-tắc-tổ-chức)
    * [1.1. Định nghĩa Hoàn thành (Definition of Done - DoD)](#11-định-nghĩa-hoàn-thành-definition-of-done---dod)
    * [1.2. Thang đo độ ưu tiên MoSCoW](#12-thang-đo-độ-ưu-tiên-moscow)
* [2. Chi tiết Product Backlog — User Story & Acceptance Criteria](#2-chi-tiết-product-backlog-user-story--acceptance-criteria)
    * [EPIC A — Xác thực & Phân quyền bảo mật (Security & Identity)](#epic-a-xác-thực--phân-quyền-bảo-mật-security--identity)
    * [EPIC B — Số hóa & Xuất bản (Digitization & Publish)](#epic-b-số-hóa--xuất-bản-digitization--publish)
    * [EPIC C — Tra cứu & Đọc sách (Search & Reader UX)](#epic-c-tra-cứu--đọc-sách-search--reader-ux)
* [3. Bản đồ phân bổ Sprint (Sprint Mapping)](#3-bản-đồ-phân-bổ-sprint-sprint-mapping)

---

## 1. Định nghĩa Hoàn thành và Quy tắc tổ chức

### 1.1. Định nghĩa Hoàn thành (Definition of Done - DoD)
Một User Story chỉ được coi là hoàn thành (`Done`) và sẵn sàng bàn giao trong Sprint Review khi đáp ứng đủ các tiêu chí:

1. **Code Quality:** Không còn lỗi cảnh báo nghiêm trọng từ ESLint/PyLint; mã nguồn đã được merge vào nhánh `main` qua Pull Request có tối thiểu 01 kỹ sư khác review.
2. **Testing:** Unit test bao phủ dòng code tối thiểu đạt 80%. Vượt qua tất cả các ca kiểm thử chức năng tự động (Integration Test).
3. **Deployment:** Được deploy thành công lên môi trường Staging qua quy trình CI/CD tự động.
4. **Security:** Không chứa mật khẩu cứng (hardcoded credentials); API được bảo mật bằng JWT và xác thực phân quyền qua Keycloak.
5. **Documentation:** API Swagger được cập nhật đầy đủ; mã nguồn được comment rõ ràng.

### 1.2. Thang đo độ ưu tiên MoSCoW
* **Must-have (M):** Bắt buộc phải hoàn thành trong MVP (Sprint 1 đến Sprint 3).
* **Should-have (S):** Cần thiết để tối ưu hóa trải nghiệm người dùng, hoàn thành trong MVP (Sprint 4).
* **Could-have (C):** Bổ sung nếu dư thời gian (Sprint 5).
* **Won't-have (W):** Tính năng hoãn lại sang giai đoạn sau (AI/RAG, Chống đạo văn).

---

## 2. Chi tiết Product Backlog — User Story & Acceptance Criteria

### EPIC A — Xác thực & Phân quyền bảo mật (Security & Identity)

#### US00: Đăng nhập SSO hệ thống
* **User Story:** Là độc giả (sinh viên/giảng viên/thủ thư), tôi muốn đăng nhập bằng tài khoản email HCMUS thông qua Keycloak SSO để hệ thống tự động xác nhận vai trò và cấp quyền truy cập giao diện phù hợp.
* **Story Points:** 5 | **Độ ưu tiên:** Must
* **Tiêu chí chấp nhận (Acceptance Criteria):**
  * **AC 1 (Given-When-Then):** **Given** người dùng truy cập trang `/login`, **When** người dùng click nút "Đăng nhập với tài khoản HCMUS", **Then** hệ thống chuyển hướng thành công đến trang đăng nhập Keycloak SSO của trường.
  * **AC 2:** Sau khi xác thực đúng tài khoản, Keycloak trả về JWT Token chứa các thông tin cá nhân và mảng vai trò `roles` (student / faculty / editor / admin).
  * **AC 3:** Hệ thống tự động phân phối giao diện: vai trò `editor`/`librarian` truy cập vào Dashboard Quản lý; vai trò `student`/`faculty` truy cập Web Portal đọc sách; khách vãng lai (Guest) chỉ có quyền đọc tài liệu Public.
  * **AC 4:** JWT token có thời hạn 60 phút, hệ thống tự động refresh token ngầm khi còn hoạt động hoặc yêu cầu đăng nhập lại an toàn khi hết phiên.

#### US00b: Kiểm soát quyền truy cập tài liệu
* **User Story:** Là sinh viên, tôi chỉ muốn nhìn thấy và đọc các tài liệu mà tôi được phép tiếp cận để bảo đảm tính tuân thủ pháp lý về bản quyền của nhà trường.
* **Story Points:** 3 | **Độ ưu tiên:** Must
* **Tiêu chí chấp nhận (Acceptance Criteria):**
  * **AC 1:** Tài liệu được đánh nhãn truy cập `Restricted` sẽ không xuất hiện trong kết quả tìm kiếm và danh mục của tài khoản sinh viên thường.
  * **AC 2:** Tài liệu `Internal` chỉ hiển thị đối với người dùng đã đăng nhập thành công tài khoản trường; bị chặn hoàn toàn đối với khách vãng lai (Guest).
  * **AC 3:** Tài liệu `Public` cho phép hiển thị và đọc trực tuyến đối với tất cả người dùng (không yêu cầu đăng nhập).

---

### EPIC B — Số hóa & Xuất bản (Digitization & Publish)

#### US01: Tải lên tệp scan gốc
* **User Story:** Là thủ thư, tôi muốn tải lên tệp PDF hoặc ảnh scan sách giấy gốc để hệ thống bắt đầu xử lý luồng số hóa tự động.
* **Story Points:** 3 | **Độ ưu tiên:** Must
* **Tiêu chí chấp nhận (Acceptance Criteria):**
  * **AC 1:** Giao diện hỗ trợ kéo thả tệp tin hoặc chọn từ thiết bị.
  * **AC 2:** Chỉ chấp nhận định dạng tệp `.pdf`, `.jpg`, `.png` và giới hạn dung lượng tải lên tối đa là **100 MB**.
  * **AC 3:** Hiển thị thanh tiến trình upload theo thời gian thực (0% - 100%).
  * **AC 4:** Tệp tin tải lên được lưu trữ tự động vào MinIO Object Storage tại đường dẫn: `bucket-library/raw_scans/YYYYMMDD/[ID]_[filename]`.

#### US02: Tự động chạy OCR nhận dạng ký tự
* **User Story:** Là thủ thư, tôi muốn hệ thống tự động chạy nhận dạng ký tự quang học đối với tệp ảnh quét vừa tải lên để tôi không phải nhập liệu lại văn bản thủ công.
* **Story Points:** 5 | **Độ ưu tiên:** Must
* **Tiêu chí chấp nhận (Acceptance Criteria):**
  * **AC 1:** Tiến trình OCR Tesseract tự động kích hoạt sau khi tệp tin upload thành công lên MinIO.
  * **AC 2:** Độ chính xác nhận dạng ký tự tiếng Việt (CAR) đạt ≥ **85%** đối với bản in rõ nét (300 DPI).
  * **AC 3:** Tác vụ chạy bất đồng bộ qua Celery/Redis; giao diện dashboard hiển thị trạng thái xử lý theo thời gian thực (Pending -> Processing -> Completed / Failed).
  * **AC 4:** Kết quả OCR text thô được phân tách theo từng trang sách tương ứng với ảnh scan gốc.

#### US03: Biên tập & Hiệu chỉnh văn bản OCR
* **User Story:** Là biên tập viên, tôi muốn so sánh ảnh scan gốc và văn bản OCR song song trên giao diện để tôi hiệu chỉnh nhanh các lỗi chính tả của máy nhận dạng.
* **Story Points:** 8 | **Độ ưu tiên:** Must
* **Tiêu chí chấp nhận (Acceptance Criteria):**
  * **AC 1:** Giao diện Split-screen: Bên trái là ảnh trang scan gốc (hỗ trợ zoom, rotate); bên phải là trình soạn thảo văn bản.
  * **AC 2:** Trình soạn thảo hỗ trợ gán cấu trúc Heading (H1, H2, H3) và định dạng văn bản cơ bản (in đậm, in nghiêng, danh sách).
  * **AC 3:** Hỗ trợ tính năng "Cắt ảnh" trực tiếp từ ảnh scan bên trái để nhúng nhanh làm hình minh họa trong văn bản bên phải.
  * **AC 4:** Tự động lưu nháp (Auto-save) mỗi **30 giây** vào PostgreSQL để chống mất dữ liệu khi rớt mạng.

#### US04: Gán siêu dữ liệu Dublin Core
* **User Story:** Là thủ thư, tôi muốn nhập thông tin Dublin Core và danh mục của sách để độc giả tra cứu dễ dàng.
* **Story Points:** 2 | **Độ ưu tiên:** Must
* **Tiêu chí chấp nhận (Acceptance Criteria):**
  * **AC 1:** Form nhập liệu yêu cầu bắt buộc các trường: Tên sách, Tác giả, Danh mục (Category), Quyền truy cập (Access Level).
  * **AC 2:** Danh mục (Category) được chọn từ cây danh mục có sẵn; các thẻ phân loại (Tags) cho phép nhập tự do có gợi ý tự động (Autocomplete).
  * **AC 3:** Nút "Xuất bản" bị vô hiệu hóa nếu các trường bắt buộc để trống.

#### US05: Đóng gói & Xuất bản EPUB 3.0
* **User Story:** Là thủ thư, tôi muốn đóng gói nội dung đã biên tập thành file EPUB và phát hành để độc giả có thể đọc trực tuyến responsive.
* **Story Points:** 5 | **Độ ưu tiên:** Must
* **Tiêu chí chấp nhận (Acceptance Criteria):**
  * **AC 1:** Khi nhấn nút "Đóng gói & Xuất bản", hệ thống sử dụng Pandoc biên dịch text đã biên tập sang định dạng EPUB 3.0.
  * **AC 2:** File EPUB sinh ra phải vượt qua kiểm định của công cụ `epubcheck` (0 lỗi nghiêm trọng).
  * **AC 3:** File được lưu vào MinIO: `bucket-library/epub/[ID].epub` và tự động lập chỉ mục văn bản toàn văn vào Elasticsearch.

#### US06: Quản lý Danh mục & Tag (Admin)
* **User Story:** Là admin, tôi muốn cấu hình cây danh mục môn học và tag để tổ chức tài liệu một cách khoa học.
* **Story Points:** 3 | **Độ ưu tiên:** Must
* **Tiêu chí chấp nhận (Acceptance Criteria):**
  * **AC 1:** Admin quản lý cây danh mục (Category) hỗ trợ phân cấp tối thiểu 2 cấp.
  * **AC 2:** Ngăn chặn tạo trùng tên danh mục hoặc tag (bỏ qua khoảng trắng và không phân biệt hoa thường).

---

### EPIC C — Tra cứu & Đọc sách (Search & Reader UX)

#### US07: Tìm kiếm toàn văn Elasticsearch và Vị trí vật lý
* **User Story:** Là độc giả, tôi muốn tìm kiếm từ khóa trong nội dung sách và xem thông tin vị trí kệ sách giấy tương ứng để tôi có thể đến mượn trực tiếp tại thư viện khi cần.
* **Story Points:** 8 | **Độ ưu tiên:** Must
* **Tiêu chí chấp nhận (Acceptance Criteria):**
  * **AC 1:** Trả kết quả tìm kiếm toàn văn dưới **3 giây** với tải trọng 500 người dùng đồng thời.
  * **AC 2:** Hỗ trợ Fuzzy Search (gõ tiếng Việt không dấu vẫn tìm ra kết quả có dấu tương ứng).
  * **AC 3:** Kết quả hiển thị snippet chứa từ khóa tìm kiếm và từ khóa được highlight bôi đậm.
  * **AC 4:** Kết quả hiển thị rõ thông tin vị trí vật lý của sách giấy tại kho (ví dụ: Kệ 12 - Tầng 2 - Cơ sở Quận 5).

#### US08: Đọc sách trực tuyến bảo mật
* **User Story:** Là độc giả, tôi muốn đọc sách EPUB mượt mà trên trình duyệt mà không thể tải tệp gốc về máy để bảo đảm an toàn bản quyền cho tác giả.
* **Story Points:** 8 | **Độ ưu tiên:** Must
* **Tiêu chí chấp nhận (Acceptance Criteria):**
  * **AC 1:** Trình đọc web sử dụng Epub.js kết xuất sách dạng HTML chia trang, không tải tệp EPUB gốc về client.
  * **AC 2:** Gọi tài nguyên bằng Signed URL MinIO với thời gian hết hạn là **15 phút**.
  * **AC 3:** Chặn chuột phải, chặn phím tắt copy (`Ctrl+C`), chặn in ấn (`Ctrl+P`) đối với tài liệu Internal/Restricted.

#### US09: Tùy chỉnh giao diện đọc sách (Reader Customization)
* **User Story:** Là độc giả, tôi muốn điều chỉnh cỡ chữ, font chữ và màu nền để bảo vệ mắt khi đọc sách ban đêm.
* **Story Points:** 3 | **Độ ưu tiên:** Should
* **Tiêu chí chấp nhận (Acceptance Criteria):**
  * **AC 1:** Cho phép co giãn phông chữ từ **80% đến 200%**.
  * **AC 2:** Chọn font chữ: Serif, Sans-serif, và OpenDyslexic.
  * **AC 3:** Hỗ trợ 3 chế độ màu nền: Light, Sepia, và Dark mode.

#### US10: Đánh dấu trang (Bookmark) & Highlight
* **User Story:** Là độc giả, tôi muốn đánh dấu trang đang đọc dở và highlight các đoạn văn hay để tiện ôn tập sau này.
* **Story Points:** 5 | **Độ ưu tiên:** Should
* **Tiêu chí chấp nhận (Acceptance Criteria):**
  * **AC 1:** Tự động lưu vị trí đọc (CFI pointer) sau mỗi 30 giây vào PostgreSQL.
  * **AC 2:** Hỗ trợ bôi đen đoạn văn để lưu highlight (chọn màu Vàng/Hồng/Xanh) và đính kèm ghi chú.

#### US11: Trích dẫn tự động (Citation Generator)
* **User Story:** Là độc giả, tôi muốn sinh trích dẫn chuẩn APA hoặc IEEE của cuốn sách để chèn nhanh vào báo cáo khoa học.
* **Story Points:** 2 | **Độ ưu tiên:** Could
* **Tiêu chí chấp nhận (Acceptance Criteria):**
  * **AC 1:** Nút "Trích dẫn" tự động trích xuất metadata Dublin Core thành chuỗi trích dẫn chuẩn APA 7th và IEEE.

---

## 3. Bản đồ phân bổ Sprint (Sprint Mapping)

Quy trình phát triển phần mềm MVP kéo dài **10 tuần**, chia làm 5 Sprint (mỗi Sprint 2 tuần):

* **Sprint 1 (Tuần 3–4):**
  * *Mục tiêu:* Đăng nhập SSO Keycloak, Upload file scan và Pipeline OCR thô.
  * *User Stories:* US00, US00b, US01, US02.
* **Sprint 2 (Tuần 5–6):**
  * *Mục tiêu:* Màn hình biên tập Split-screen, Form Metadata và Đóng gói EPUB bằng Pandoc.
  * *User Stories:* US03, US04, US05.
* **Sprint 3 (Tuần 7–8):**
  * *Mục tiêu:* Quản lý Category/Tag, Elasticsearch full-text search và Trình đọc Web Reader bảo mật.
  * *User Stories:* US06, US07, US08.
* **Sprint 4 (Tuần 9–10):**
  * *Mục tiêu:* Tùy chỉnh UI Reader (font/nền), Bookmark tự động và Highlight/Ghi chú.
  * *User Stories:* US09, US10.
* **Sprint 5 (Tuần 11–12):**
  * *Mục tiêu:* Trích dẫn tự động, kiểm thử sửa lỗi hệ thống và nghiệm thu UAT phần mềm.
  * *User Stories:* US11.
