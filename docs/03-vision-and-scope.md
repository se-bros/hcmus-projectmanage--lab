# PROJECT VISION & SCOPE (WHAT)

## Hệ thống Quản lý Số hóa Thư viện (LibDMS)

**Thư viện hiện đại & Ban Công nghệ Thông tin**

Phiên bản 1.0 • Tháng 7/2026

## Mục lục

* [1. Glossary & Business Rules](#1-glossary--business-rules)
* [2. Feature Model & MVP](#2-feature-model--mvp)
* [3. Vision — Black-box Solution](#3-vision--black-box-solution)
* [4. Project Scope Statement](#4-project-scope-statement)
* [5. Mockup, Prototype & PoC](#5-mockup-prototype--poc)

---

## 1. Glossary & Business Rules

### Glossary

| Thuật ngữ | Định nghĩa |
| --- | --- |
| **LibDMS** | Hệ thống Quản lý Số hóa Thư viện (Library Digitization Management System). |
| **EPUB** | Định dạng sách điện tử chuẩn mã nguồn mở (.epub) hỗ trợ hiển thị linh hoạt trên nhiều loại thiết bị. |
| **OCR (Optical Character Recognition)** | Công nghệ nhận dạng ký tự quang học để chuyển dữ liệu ảnh quét sang dạng văn bản có thể tìm kiếm được. |
| **Category & Tag** | Danh mục phân loại đa cấp và thẻ nhãn gán cho tài liệu giúp gom nhóm tài liệu đa chiều. |
| **RBAC (Role-Based Access Control)** | Phân quyền truy cập dựa trên vai trò của người dùng trong hệ thống (Admin, Librarian, Reader). |
| **EPUB Reader online** | Trình đọc sách điện tử định dạng EPUB được tích hợp trực tiếp trên trình duyệt Web mà không cần cài app phụ trợ. |
| **Secure Stream API** | Cơ chế cung cấp dữ liệu tệp tin dưới dạng dòng luồng dữ liệu (streaming) được xác thực bằng JWT, tránh để lộ đường dẫn trực tiếp của tệp tin trong database. |

### Business Rules

| Quy tắc nghiệp vụ (Rule) | Nguồn tham chiếu (Source) | Mức độ biến động |
| --- | --- | --- |
| Tài liệu số hóa phải được phân loại vào ít nhất 1 Category chính | Quy trình quản lý phân mục tài liệu thư viện chuẩn | Thấp |
| Chỉ người dùng có vai trò Librarian và Admin mới được quyền thực hiện số hóa và chỉnh sửa tài liệu | Chính sách an toàn thông tin và bảo mật dữ liệu thư viện | Thấp |
| Sách điện tử bị giới hạn bản quyền chỉ được phép đọc trực tuyến thông qua EPUB Reader, chặn tải về | Luật Sở hữu trí tuệ số 50/2005/QH11 và các văn bản hướng dẫn | Trung bình |
| Thời hạn mượn sách giấy tối đa là 14 ngày, bạn đọc có thể gửi yêu cầu gia hạn trực tuyến | Quy chế hoạt động Thư viện truyền thống | Trung bình |
| Lượt mượn đọc sách số bị giới hạn số phiên truy cập đồng thời cho mỗi đầu sách (ví dụ: tối đa 5 người đọc cùng lúc cho sách có bản quyền) | Thỏa thuận mua sắm tài liệu số thư viện | Cao — tùy thuộc vào loại tài liệu |

---

## 2. Feature Model & MVP

Hệ thống **LibDMS** quản lý các nhóm chức năng chính được biểu diễn thông qua sơ đồ Feature Model dưới đây:

![Sơ đồ mô hình tính năng (Feature Model)](file:///d:/Project/hcmus-projectmanage--lab/docs/images/feature_model.svg)

Các tính năng quan trọng được xây dựng dựa trên mục tiêu của người dùng:

- **Bạn đọc (Reader):**
  - *Mục tiêu:* Tra cứu tài liệu nhanh chóng từ xa và đọc sách trực tuyến.
  - *Hành động:* Tìm kiếm toàn văn theo từ khóa, lọc theo Category/Tag, đọc sách qua EPUB Reader online, gửi yêu cầu mượn/trả sách vật lý.
- **Thủ thư (Librarian):**
  - *Mục tiêu:* Quản lý vòng đời số hóa tài liệu và nghiệp vụ thư viện hiệu quả.
  - *Hành động:* Tải lên tài liệu (PDF, hình ảnh), chạy OCR, hiệu đính text, đóng gói EPUB, phân loại danh mục, quản lý mượn/trả và xem thống kê.
- **Ban quản trị (Admin):**
  - *Mục tiêu:* Đảm bảo an toàn thông tin và quản lý người dùng tập trung.
  - *Hành động:* Quản lý tài khoản người dùng, cấu hình vai trò RBAC, sao lưu dữ liệu và giám sát hệ thống.

**Phạm vi MVP (Minimum Viable Product):**
Tập trung vào các tính năng cốt lõi để chạy thử nghiệm chu trình số hóa:
*   Đăng ký/Đăng nhập người dùng và phân quyền RBAC cơ bản.
*   Pipeline số hóa: Tải file lên → chạy OCR → xuất bản file EPUB (hỗ trợ Fixed-Layout làm mặc định).
*   Quản lý danh mục (Category) và nhãn (Tag).
*   Tìm kiếm Elasticsearch cơ bản theo metadata và text sau OCR.
*   Trình đọc sách trực tuyến EPUB Reader online cơ bản.

Các tính năng như mượn/trả sách giấy nâng cao, EPUB Reflowable tùy chọn, dashboard thống kê đồ thị biểu diễn chi tiết, tích hợp chatbot tra cứu thông minh (RAG Chatbot) và tự động co giãn Cloud sẽ được phát triển ở các giai đoạn tiếp theo.

---

## 3. Vision — Black-box Solution

### Trạng thái hiện tại (As-is)

Quy trình quản lý tài liệu tại thư viện hiện tại phụ thuộc nhiều vào thao tác thủ công, được mô tả chi tiết theo từng đối tượng tác nhân dưới đây:

#### 1. Đối với Thủ thư (Librarian) - Quy trình Nghiệp vụ Chi tiết & Vấn đề tương ứng
*   **Quy trình Nhập & Kiểm kê tài liệu:** 
    *   *Bước 1:* Thủ thư nhận sách giấy mới từ nhà cung cấp, kiểm đếm số lượng thủ công.
    *   *Bước 2:* Mở sổ đăng ký cá biệt dạng giấy (sổ kích thước lớn), dùng bút ghi tay các thông tin: số thứ tự cá biệt, tên sách, tác giả, nhà xuất bản, năm xuất bản, giá tiền.
    *   *Bước 3:* Xác định mã phân loại DDC (Dewey Decimal Classification) cho sách (ví dụ: 005.1 cho lập trình), viết tay hoặc in nhãn gáy.
    *   *Bước 4:* Sử dụng băng keo trong dán nhãn gáy lên gáy sách vật lý.
    *   *Bước 5:* Mang sách vào kho kệ, tìm vị trí kệ tương ứng với mã DDC của khoa chuyên ngành để xếp lên.
    *   *Vấn đề (Pain Point):* Quy trình nhập liệu chậm, dễ nhầm lẫn ghi chép thông tin và không có cách nào theo dõi chính xác số lượng tồn kho tức thời.
*   **Quy trình Số hóa tự phát:** 
    *   *Bước 1:* Thủ thư nhận yêu cầu số hóa tài liệu quý hiếm từ ban giám đốc.
    *   *Bước 2:* Dùng máy quét phẳng (flatbed scanner) đặt từng trang tài liệu xuống để quét sang định dạng ảnh PNG/JPEG riêng lẻ.
    *   *Bước 3:* Gom các tệp ảnh rời rạc đó thành một file PDF dạng ảnh scan thô không có text layer.
    *   *Bước 4:* Upload file PDF này lên một thư mục dùng chung (Google Drive hoặc ổ đĩa mạng máy tính thư viện) để bạn đọc tự tải về.
    *   *Vấn đề (Pain Point):* File PDF dạng ảnh scan có dung lượng rất lớn, chữ bị mờ, không thể copy/edit và hoàn toàn không thể tìm kiếm nội dung bên trong.
*   **Quy trình Cho mượn & Nhận trả sách giấy:** 
    *   *Bước 1:* Nhận phiếu mượn giấy do bạn đọc điền thông tin tại quầy.
    *   *Bước 2:* Di chuyển trực tiếp vào các hàng kệ trong kho tối để tìm cuốn sách giấy tương ứng.
    *   *Bước 3:* Ghi thông tin bạn đọc, ngày mượn và ngày phải trả vào sổ theo dõi mượn trả của thư viện.
    *   *Bước 4:* Khi bạn đọc trả sách, thủ thư nhận lại sách, lật giở từng trang để kiểm tra xem sách có bị rách, viết bậy hay ẩm mốc hay không.
    *   *Bước 5:* Ký xác nhận đã trả vào sổ tay theo dõi và mang sách xếp lại lên kệ kho vật lý.
    *   *Vấn đề (Pain Point):* Tốn nhiều thời gian đi lại tìm sách trong kho, không có hệ thống tự động cảnh báo sách quá hạn và dễ thất thoát tài liệu.

#### 2. Đối với Bạn đọc (Reader) - Quy trình Tra cứu & Tiếp cận
- **Quy trình Tìm kiếm:** Phải đến tận thư viện, sử dụng máy tính trạm cục bộ để gõ tiêu đề sách hoặc tra cứu trong tủ thẻ mục lục giấy.
  - *Vấn đề (Pain Point):* Chỉ tìm được thông tin cơ bản ngoài bìa sách (tên sách, tác giả), không thể tìm theo từ khóa chuyên môn nằm sâu trong nội dung sách.
- **Quy trình Đọc & Khai thác:** Khi tìm được sách, chỉ được đọc tại chỗ hoặc mượn về với thời hạn giới hạn. Với sách độc bản quý hiếm, bạn đọc phải ngồi chép tay các đoạn tài liệu vì thư viện cấm photocopy.
  - *Vấn đề (Pain Point):* Bị giới hạn về không gian và thời gian. Tài liệu dễ bị rách, ẩm mốc, xuống cấp cơ lý do tần suất lật giở cao.

#### 3. Đối với Quản trị viên (Admin) - Quản lý hệ thống
- **Quy trình Quản lý tài khoản:** Thư viện không có hệ thống tài khoản số tập trung cho bạn đọc ngoài, việc cấp thẻ thư viện giấy thực hiện hoàn toàn thủ công.
  - *Vấn đề (Pain Point):* Khó kiểm soát quyền truy cập và phân vai người dùng rõ ràng trong khai thác tài nguyên số.

---

### Trạng thái tương lai (To-be)

Hệ thống **LibDMS** chuyển đổi các quy trình thủ công sang chu trình số hóa tự động với trạng thái vận hành hiện đại, mô tả chi tiết theo từng tác nhân:

#### 1. Đối với Thủ thư (Librarian) - Quy trình Số hóa & Vận hành Số Chi tiết
*   **Quy trình Số hóa khép kín tự động:** 
    *   *Bước 1:* Đăng nhập admin dashboard của LibDMS bằng tài khoản được cấp quyền.
    *   *Bước 2:* Kéo thả file PDF scan hoặc thư mục chứa ảnh (PNG/JPEG) của tài liệu vào vùng tải lên.
    *   *Bước 3:* Nhập các trường metadata chuẩn hóa (tiêu đề, tác giả, nhà xuất bản, năm) và chọn Category đa cấp, gán nhãn tags tự do.
    *   *Bước 4:* Cấu hình quyền truy cập (mặc định cho phép đọc online qua EPUB Reader, chặn download).
    *   *Bước 5:* Click nút "Bắt đầu số hóa". Hệ thống tự động đẩy tệp vào Queue để chạy OCR trích xuất văn bản tiếng Việt và đóng gói sang định dạng EPUB.
    *   *Bước 6:* Khi hệ thống chuyển trạng thái tài liệu sang `Ready for Correction`, thủ thư mở giao diện hiệu đính (Correction Dashboard). Màn hình hiển thị song song ảnh gốc và văn bản OCR. Thủ thư sửa nhanh các lỗi chính tả nhận dạng sai, định dạng tiêu đề, sau đó bấm "Xác nhận & Xuất bản".
    *   *Trạng thái hệ thống (State):* Tài liệu trải qua các trạng thái có cấu trúc: `Uploaded` (Tải lên) → `Processing` (Đang OCR/EPUB) → `Ready for Correction` (Chờ hiệu đính) → `Published` (Đã xuất bản).
*   **Quy trình Phê duyệt Mượn/Trả trực tuyến:** 
    *   *Bước 1:* Thủ thư vào mục "Yêu cầu mượn/trả" trên portal.
    *   *Bước 2:* Duyệt các đăng ký mượn sách giấy từ bạn đọc (trạng thái `Requested`). Hệ thống tự động kiểm tra lượng tồn kho vật lý.
    *   *Bước 3:* Thủ thư xác nhận chuẩn bị sách tại quầy và click "Duyệt cho mượn". Hệ thống tự động chuyển trạng thái mượn sang `Borrowed` và tính toán ngày quá hạn.
    *   *Bước 4:* Khi bạn đọc mang sách giấy trả, thủ thư quét mã vạch (barcode/QR) trên sách để mở nhanh bản ghi, bấm "Xác nhận đã trả". Hệ thống tự động chuyển trạng thái sang `Returned` và cộng lại số lượng tồn kho.
    *   *Trạng thái hệ thống (State):* Trạng thái mượn sách được quản lý động: `Requested` (Đăng ký mượn) → `Borrowed` (Đang mượn) → `Returned` (Đã trả) hoặc `Overdue` (Quá hạn).
*   **Quy trình Theo dõi Thống kê:**
    *   *Bước 1:* Thủ thư truy cập tab "Thống kê" để xem biểu đồ lượt đọc online và lượt mượn sách giấy.
    *   *Bước 2:* Lọc danh sách bạn đọc nợ sách quá hạn (`Overdue`), click nút "Gửi nhắc nhở" để hệ thống tự động gửi email/SMS thông báo.

#### 2. Đối với Bạn đọc (Reader) - Tra cứu & Đọc sách trực tuyến
- **Quy trình Tra cứu thông minh:** Bạn đọc đăng nhập portal từ xa, gõ từ khóa tự do trên thanh tìm kiếm Elasticsearch.
  - *Trạng thái hệ thống (State):* Hệ thống trả về kết quả tìm kiếm toàn văn chính xác tới từng trang sách kèm theo các bộ lọc Category/Tag thời gian thực.
- **Quy trình Đọc sách trực tuyến bảo mật:** Bạn đọc mở trình đọc EPUB Reader online tích hợp trên web để đọc trực tiếp.
  - *Trạng thái hệ thống (State):* Tài nguyên được phân phối an toàn thông qua Secure Stream API (phát luồng dữ liệu trực tiếp có xác thực JWT). Trình duyệt của bạn đọc bị giới hạn không cho phép chuột phải sao chép text, tắt phím tắt in ấn và ẩn hoàn toàn đường dẫn tải tệp gốc để bảo vệ bản quyền.
- **Quy trình Hỏi đáp thông minh:** Sử dụng khung chat Chatbot RAG tích hợp để đặt câu hỏi về nội dung sách.
  - *Trạng thái hệ thống (State):* Chatbot gọi API ngôn ngữ lớn (LLM), kết hợp dữ liệu vector trích xuất từ văn bản đã OCR để phản hồi câu trả lời kèm trích dẫn nguồn trang sách cụ thể.

#### 3. Đối với Quản trị viên (Admin) - Quản lý & Giám sát Cloud
- **Quy trình Quản lý Tài khoản & Phân quyền:** Quản trị viên quản lý danh sách người dùng và gán vai trò RBAC (Admin, Librarian, Reader) trên admin dashboard.
  - *Trạng thái hệ thống (State):* Quyền truy cập API được kiểm soát chặt chẽ ở cấp độ token JWT và các policy phân quyền trên FastAPI backend.
- **Quy trình Giám sát & Báo cáo:** Xem biểu đồ trực quan về dung lượng lưu trữ cloud, băng thông sử dụng và hiệu suất số hóa.
  - *Trạng thái hệ thống (State):* Các chỉ số hạ tầng và tần suất mượn đọc được log liên tục phục vụ tối ưu hóa chi phí vận hành Cloud.

---

## 4. Project Scope Statement

### Deliverables (Các kết quả bàn giao)

*   Mã nguồn ứng dụng LibDMS (Next.js frontend, FastAPI backend, Dockerfiles).
*   Môi trường hạ tầng Cloud (Terraform script / ARM templates cho AWS/Azure).
*   Hệ thống OCR Engine (Tesseract) và EPUB Converter (Calibre/Pandoc wrapper) đóng gói container.
*   Tài liệu thiết kế kiến trúc hệ thống và mô hình dữ liệu.
*   Tài liệu hướng dẫn vận hành số hóa dành cho thủ thư và hướng dẫn tra cứu dành cho bạn đọc.

### Project Exclusions (Phạm vi loại trừ)

*   Thiết bị quét tài liệu (scanners), máy tính trạm của thủ thư.
*   Nhân sự thực hiện quét tài liệu vật lý sang file ảnh.
*   Hệ thống so khớp đạo văn chuyên dụng (Turnitin/DoIT).

### Constraints (Các ràng buộc)

*   **Chất lượng OCR:** Độ chính xác OCR tiếng Việt phụ thuộc nhiều vào độ phân giải ảnh quét và độ sạch của tài liệu gốc (tài liệu chữ viết tay không nằm trong phạm vi hỗ trợ OCR chính xác).
*   **Chi phí hạ tầng:** Giới hạn ngân sách chạy máy chủ ảo GPU (nếu dùng OCR nâng cao) và dung lượng lưu trữ Cloud.

### Yêu cầu phi chức năng (Non-Functional Requirements)

*   **Hiệu năng:** Thời gian tìm kiếm toàn văn Elasticsearch dưới **2 giây** với cơ sở dữ liệu dưới 50.000 tài liệu.
*   **Độ sẵn sàng (Reliability):** Uptime SLA đạt tối thiểu **99.9%** trên môi trường Production Cloud.
*   **Bảo mật:**
    *   Truyền dữ liệu bắt buộc qua HTTPS (TLS 1.3).
    *   Mã hóa tệp tin lưu trữ tĩnh trên Cloud (Encryption at Rest).
    *   Sử dụng Secure Stream API kết hợp Token xác thực JWT hết hạn ngắn.
    *   Chặn chuột phải copy text và tắt tính năng in mặc định trên EPUB Reader trực tuyến.

---

## 5. Mockup, Prototype & PoC

### Giai đoạn Prototype (Luồng giao diện)

*   **Giao diện Dashboard Số hóa:** Mockup quy trình tải file lên → chạy OCR hiển thị thanh tiến độ (%) → màn hình biên tập so sánh ảnh gốc và text OCR để thủ thư hiệu chỉnh → đóng gói EPUB.
*   **Giao diện Trình đọc EPUB:** Thử nghiệm giao diện đọc sách online thích ứng trên di động và PC, kiểm tra các nút tăng giảm font size, chế độ đọc ban đêm (Dark Mode).

### Giai đoạn PoC (Proof of Concept - Kiểm chứng công nghệ)

*   **Độ chính xác OCR Tesseract:** Thử nghiệm chạy OCR tiếng Việt trên 50 trang tài liệu mẫu có độ mờ, font chữ khác nhau để cấu hình thông số tiền xử lý ảnh (binarization, denoising) đạt tỷ lệ chính xác cao nhất trước khi viết code backend.
*   **Độ mượt mà của EPUB Reader online:** Thử nghiệm render file EPUB Fixed-layout dung lượng lớn (chứa nhiều hình ảnh) trên trình duyệt Safari/Chrome của điện thoại phân khúc thấp để tối ưu hóa bộ nhớ đệm (caching).
