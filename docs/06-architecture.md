# ARCHITECTURE (HOW)

## Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS

**Trường Đại học Khoa học Tự nhiên, ĐHQG-HCM (HCMUS) — Thư viện & Phòng Công nghệ Thông tin**

Phiên bản 1.0 • Tháng 7/2026

## Mục lục

* [1. Phong cách Kiến trúc](#1-phong-cách-kiến-trúc)
* [2. Ngăn xếp Công nghệ](#2-ngăn-xếp-công-nghệ)
* [3. Phương án Bảo mật, Sao lưu & Khôi phục Thảm họa (Backup & Disaster Recovery)](#3-phương-án-bảo-mật-sao-lưu--khôi-phục-thảm-họa-backup--disaster-recovery)
* [4. Quy trình Nghiệp vụ & Vận hành Chi tiết](#4-quy-trình-nghiệp-vụ--vận-hành-chi-tiết)

---

## 1. Phong cách Kiến trúc

![Mô hình kiến trúc hệ thống (System Architecture)](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/hcmus-projectmanage--lab/docs/images/system_architecture.svg)

**Lựa chọn: Kiến trúc ứng dụng web tự xây dựng (custom-built) theo mô hình Modular Monolith sử dụng React 18 ở frontend và FastAPI (Python 3.11) ở backend, kết hợp các công cụ xử lý file offline (Tesseract OCR, Pandoc) và các dịch vụ vệ tinh (MinIO, Elasticsearch, Keycloak SSO).**

| Lý do chọn | Giải thích |
| --- | --- |
| **Không sử dụng DSpace** | DSpace là hệ thống lưu trữ học thuật tĩnh (PDF/Metadata) cho khóa luận/luận văn, không hỗ trợ luồng nghiệp vụ tương tác phức tạp như: chạy OCR động, biên tập sửa lỗi chính tả trực tuyến song song với ảnh quét, và tự động đóng gói sách EPUB. Việc tự viết web app custom giúp tối ưu hóa luồng nghiệp vụ đặc thù này. |
| **Không chọn microservices** | Đội ngũ kỹ thuật Phòng CNTT của trường mỏng (3-4 kỹ sư kiêm nhiệm). Kiến trúc Modular Monolith trên FastAPI giúp đơn giản hóa khâu kiểm thử, triển khai và bảo trì, đồng thời dễ dàng chuyển đổi sang microservices ở pha sau nếu hệ thống phình to. |
| **Xử lý tác vụ bất đồng bộ (FastAPI & Celery)** | Các tác vụ nặng như chạy OCR trên tệp scan 300 trang và compile EPUB thông qua Pandoc tốn nhiều thời gian và tài nguyên CPU. FastAPI tích hợp Background Tasks giúp API không bị nghẽn (non-blocking) trong khi thực hiện xử lý. |
| **Tách riêng Elasticsearch & MinIO** | Đảm bảo hiệu năng truy tìm sách tức thì ( Elasticsearch full-text search) và khả năng lưu trữ hàng triệu file scan/EPUB an toàn trên hệ thống đối tượng (MinIO) tách biệt với máy chủ chạy code logic. |

---

## 2. Ngăn xếp Công nghệ

| Thành phần | Lựa chọn cụ thể | Lý do & Phiên bản |
| :--- | :--- | :--- |
| **Frontend UI** | **React 18** & **TypeScript** | Thư viện phổ biến giúp xây dựng giao diện Single Page Application (SPA) mượt mà, hỗ trợ tốt các thành phần UI phức tạp như trình chỉnh sửa văn bản WYSIWYG và trình xem PDF/EPUB. |
| **Web Reader** | **Epub.js** | Thư viện JavaScript nguồn mở tốt nhất hiện tại giúp hiển thị sách EPUB responsive trực tiếp trên trình duyệt, hỗ trợ bookmark, ghi chú và tùy chỉnh chế độ đọc (font, cỡ chữ, màu nền). |
| **Backend API** | **FastAPI (Python 3.11)** | Framework API hiệu năng cực cao, hỗ trợ lập trình bất đồng bộ (async/await) lý tưởng cho các tác vụ I/O nặng và xử lý tệp tin. Tự động sinh tài liệu API (Swagger UI). |
| **Web Server / Proxy** | **Nginx 1.24+** | Nginx đóng vai trò Web Server phục vụ static files của React, Reverse Proxy chuyển hướng các yêu cầu API đến FastAPI, và xử lý mã hóa bảo mật SSL/TLS 1.3. |
| **Cơ sở dữ liệu** | **PostgreSQL 16** | Hệ quản trị cơ sở dữ liệu quan hệ mạnh mẽ, lưu trữ thông tin người dùng, phân quyền (RBAC), cây danh mục (Category), thẻ (Tag) và siêu dữ liệu (Metadata) sách. |
| **OCR Engine** | **Tesseract OCR (CLI)** | Bộ nhận dạng ký tự quang học mã nguồn mở cài đặt cục bộ trên server backend, cấu hình gói ngôn ngữ tiếng Việt (`vie`), hỗ trợ trích xuất văn bản tiếng Việt chính xác cao. |
| **EPUB Compiler** | **Pandoc** & **Calibre CLI** | Bộ công cụ chuyển đổi tài liệu mạnh mẽ giúp tự động biên dịch văn bản (sau khi thủ thư sửa lỗi chính tả) sang định dạng EPUB 3 chuẩn chỉnh chỉ bằng lệnh CLI. |
| **Tìm kiếm toàn văn** | **Elasticsearch 8.x** | Công cụ tìm kiếm phân tán mạnh mẽ, dùng để lập chỉ mục toàn bộ văn bản sách EPUB và metadata, hỗ trợ tìm kiếm mờ (fuzzy search) và lọc đa chiều. |
| **Lưu trữ đối tượng** | **MinIO (On-premise)** | Hệ thống Object Storage tương thích S3 lưu trữ tệp tin PDF scan gốc và tệp EPUB thành phẩm. Hỗ trợ sinh đường dẫn bảo mật Signed URL. |
| **Xác thực & SSO** | **Keycloak 24.x** kết nối **LDAP/AD** | Quản lý định danh và phiên đăng nhập tập trung của trường. Đồng bộ phân quyền người dùng (RBAC) với LDAP/Active Directory có sẵn của HCMUS. |
| **Hạ tầng triển khai** | **Docker & Docker Compose** | Đóng gói toàn bộ các service thành container độc lập giúp dễ dàng triển khai trên hệ thống ảo hóa vật lý (VMware) sẵn có của phòng máy chủ trường. |
| **Dịch vụ AI (Giai đoạn 3)** | **Qdrant Vector DB** & **FastAPI** | Dùng để lưu trữ embeddings phục vụ tìm kiếm ngữ nghĩa (Semantic Search) và RAG hỏi đáp thông minh trên sách học trình ở giai đoạn nâng cao. |
| **Công cụ Sao lưu** | **PgBackRest** & **Restic** | PgBackRest tự động backup gia tăng PostgreSQL hàng ngày. Restic mã hóa và sao lưu MinIO bucket sang máy chủ dự phòng off-site. |

---

## 3. Phương án Bảo mật, Sao lưu & Khôi phục Thảm họa (Backup & Disaster Recovery)

### 3.1. Chiến lược Sao lưu (Backup Strategy)
*   **PostgreSQL Backup:** PgBackRest tự động chạy sao lưu gia tăng (incremental) vào lúc 02:00 AM mỗi ngày và sao lưu toàn phần (full backup) vào tối Chủ nhật hàng tuần. Bản sao lưu được mã hóa AES-256 trước khi đẩy sang máy chủ lưu trữ độc lập.
*   **MinIO Storage Backup:** Sử dụng Restic đồng bộ hóa và mã hóa toàn bộ dữ liệu PDF gốc và EPUB hàng đêm sang hệ thống NAS lưu trữ dự phòng của phòng CNTT trường.
*   **Thời gian lưu trữ:** Bản sao lưu ngày được giữ trong 30 ngày, bản sao lưu tuần được giữ trong 12 tuần và bản sao lưu tháng được giữ trong 12 tháng.

### 3.2. Chỉ số phục hồi (DR Targets)
*   **RPO (Recovery Point Objective):** Tối đa **24 giờ** (không mất quá 1 ngày làm việc số hóa của thủ thư).
*   **RTO (Recovery Time Objective):** Tối đa **4 giờ** (thời gian khôi phục toàn bộ hệ thống từ bản backup gần nhất khi xảy ra lỗi phần cứng vật lý nghiêm trọng).

### 3.3. Các lớp bảo mật (Security Layers)
*   **Mã hóa truyền tải:** Sử dụng SSL/TLS 1.3 cho toàn bộ kết nối HTTPS. Thiết lập tiêu đề bảo mật HSTS.
*   **Bảo mật dữ liệu tệp tin:** Không cho phép độc giả truy cập trực tiếp file EPUB trên MinIO. Khi độc giả nhấn đọc sách, backend FastAPI kiểm tra phân quyền và sinh một **Signed URL** giới hạn hiệu lực trong **15 phút**.
*   **Chống cào dữ liệu (Anti-scraping):** Trình xem Epub.js được cấu hình vô hiệu hóa phím chuột phải, phím tắt chụp màn hình, chặn in ấn và không hiển thị tùy chọn download file gốc nhằm bảo vệ bản quyền số của nhà xuất bản.

---

## 4. Quy trình Nghiệp vụ & Vận hành Chi tiết

Sơ đồ tuần tự mô tả chi tiết quy trình số hóa sách, biên tập, xuất bản và đọc sách bảo mật của độc giả trên hệ thống HCMUS-LDMS:

![Sơ đồ Tuần tự Số hóa và Đọc EPUB](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/hcmus-projectmanage--lab/docs/images/submission_workflow.svg)

### 4.1. Quy trình Số hóa & Xuất bản (Thành viên Thư viện)
1.  **Chụp quét tài liệu (Scan/Capture):** Thủ thư dùng máy quét chuyên dụng chụp giáo trình giấy thành PDF chất lượng cao (300 DPI, thẳng dòng).
2.  **Tải lên & Khai báo (Upload & Metadata Init):** Thủ thư đăng nhập Editor/Librarian dashboard, tải file PDF lên và nhập siêu dữ liệu cơ bản chuẩn Dublin Core.
3.  **OCR Nhận dạng chữ (Auto OCR):** Hệ thống đẩy PDF vào hàng đợi chạy OCR Tesseract để trích xuất văn bản thô tiếng Việt.
4.  **Hiệu chỉnh văn bản (Online Text Editing):** Biên tập viên sử dụng giao diện Split-screen để soát sửa lỗi chính tả văn bản thô, gán cấp đề mục (H1, H2, H3) và chèn ảnh minh họa.
5.  **Gắn phân loại & Phân quyền (RBAC Configuration):** Biên tập viên chọn Danh mục (Category), gắn các nhãn Thẻ (Tag), và cấu hình quyền truy cập (Public/Internal/Restricted).
6.  **Đóng gói & Xuất bản (EPUB Compilation):** Biên tập viên bấm "Xuất bản". Hệ thống gọi Pandoc/Calibre CLI biên dịch văn bản thành EPUB 3.0, lưu trữ file EPUB vào MinIO Storage, lưu metadata vào PostgreSQL và index toàn văn sang Elasticsearch.

### 4.2. Quy trình Tìm kiếm & Đọc sách (Độc giả / Học sinh)
1.  **Đăng nhập & Xác thực (Access & Login):** Học sinh truy cập Web Portal và đăng nhập tài khoản trường qua Keycloak SSO.
2.  **Tìm kiếm & Lọc (Search & Filter):** Học sinh nhập từ khóa tìm kiếm toàn văn Elasticsearch để truy vấn nội dung bên trong sách EPUB, kết hợp bộ lọc Category và Tag để lọc kết quả.
3.  **Xác thực quyền đọc (Secure File Load):** Khi học sinh chọn đọc sách, hệ thống kiểm tra phân quyền RBAC. Nếu được phép, backend gọi MinIO sinh Signed URL bảo mật có hiệu lực 15 phút.
4.  **Đọc sách responsive (Web EPUB Reader):** Trình xem Epub.js hiển thị sách responsive thích ứng mọi màn hình di động, hỗ trợ: tăng/giảm cỡ chữ, thay đổi font, chuyển nền vàng bảo vệ mắt hoặc Dark mode, đánh dấu trang (Bookmark), tô sáng và ghi chú (Highlight & Note).
5.  **Trích dẫn tự động (Auto Citation):** Học sinh click "Trích dẫn" để hệ thống tự động xuất mẫu trích dẫn APA/IEEE kèm link định danh sách phục vụ viết bài.

