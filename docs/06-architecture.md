# ARCHITECTURE (HOW)

## Hệ thống Quản lý Số hóa Thư viện (LibDMS)

**Thư viện hiện đại & Ban Công nghệ Thông tin**

Phiên bản 1.0 • Tháng 7/2026

## Mục lục

* [1. Phong cách Kiến trúc](#1-phong-cách-kiến-trúc)
* [2. Ngăn xếp Công nghệ](#2-ngăn-xếp-công-nghệ)
* [3. Phương án Bảo mật, Sao lưu & Khôi phục Thảm họa (Backup & Disaster Recovery)](#3-phương-án-bảo-mật-sao-lưu--khôi-phục-thảm-họa-backup--disaster-recovery)
* [4. Quy trình Nghiệp vụ & Vận hành Chi tiết](#4-quy-trình-nghiệp-vụ--vận-hành-chi-tiết)

---

## 1. Phong cách Kiến trúc

Hệ thống **LibDMS** sử dụng phong cách kiến trúc **Custom Containerized Service Architecture (Kiến trúc Dịch vụ đóng gói Container)**. Kiến trúc này được thiết kế để phân rã các tác vụ xử lý nặng như OCR và đóng gói EPUB ra khỏi máy chủ xử lý API chính, đảm bảo tính sẵn sàng và hiệu năng cao nhất trên môi trường Cloud (AWS/Azure).

![Mô hình kiến trúc hệ thống (System Architecture)](file:///d:/Project/hcmus-projectmanage--lab/docs/images/system_architecture.svg)

| Thành phần kiến trúc | Lý do lựa chọn |
| --- | --- |
| **Decoupled Frontend & Backend** | Tách biệt hoàn toàn Next.js frontend và FastAPI backend. Giúp đội ngũ lập trình có thể làm việc song song, tối ưu hóa giao diện đọc sách trên di động và dễ dàng triển khai CDN toàn cầu. |
| **Worker-based OCR & Converter** | Tác vụ chạy nhận dạng văn bản (Tesseract OCR) và chuyển đổi định dạng (Calibre/Pandoc) ngốn rất nhiều CPU/RAM. Các tác vụ này được đưa vào các Worker chạy container độc lập, giao tiếp qua hàng đợi thông báo (Message Queue) để tránh làm nghẽn API server chính khi có hàng chục thủ thư số hóa tài liệu cùng lúc. |
| **Tách biệt tầng tìm kiếm (Elasticsearch)** | Lập chỉ mục toàn văn văn bản sau OCR và lưu trữ độc lập trên Elasticsearch Cluster, đảm bảo các truy vấn tìm kiếm của hàng ngàn bạn đọc cùng lúc phản hồi dưới 2 giây mà không ảnh hưởng tới cơ sở dữ liệu chính PostgreSQL. |
| **Object Storage cho tài nguyên tệp** | Toàn bộ tệp ảnh thô tải lên và file EPUB sinh ra được lưu trữ trực tiếp trên AWS S3 Storage. Giúp hệ thống không bị giới hạn bộ nhớ vật lý của máy chủ web và dễ dàng co giãn. |

---

## 2. Ngăn xếp Công nghệ

| Thành phần | Lựa chọn cụ thể | Ghi chú & Phiên bản |
| :--- | :--- | :--- |
| **Frontend Portal** | **Next.js 14+ (React 18)** | Hỗ trợ Server-Side Rendering (SSR) tối ưu hóa SEO cho cổng tra cứu công khai, UI sử dụng CSS Modules/Tailwind CSS thiết kế Responsive cho Mobile/Tablet/PC. |
| **EPUB Reader Component** | **Epub.js** | Thư viện JavaScript mạnh mẽ dùng để render sách EPUB trực tiếp trên trình duyệt, hỗ trợ bookmark, tùy biến theme đọc sách. |
| **Backend API Server** | **FastAPI (Python 3.11)** | Framework API hiệu năng cao dựa trên Python, hỗ trợ async/await tự nhiên, tự động sinh tài liệu Swagger/OpenAPI, và tích hợp hoàn hảo với các thư viện AI/RAG (LangChain, LlamaIndex). |
| **Database chính** | **PostgreSQL 16** | Cơ sở dữ liệu quan hệ mạnh mẽ lưu trữ Metadata tài liệu, tài khoản người dùng, phân quyền RBAC và lịch sử mượn/trả sách. |
| **Search Engine** | **Elasticsearch 8.x** | Công cụ tìm kiếm toàn văn tốc độ cao hỗ trợ phân tích ngôn ngữ tiếng Việt (Vietnamese Analyzer) để lập chỉ mục chính xác. |
| **File Storage** | **AWS S3 Storage** | Dịch vụ lưu trữ đối tượng đám mây của Amazon Web Services để lưu trữ an toàn các tệp tin EPUB và ảnh quét thô gốc. |
| **OCR Engine** | **Tesseract OCR v5** | Công cụ nhận dạng ký tự quang học nguồn mở tốt nhất, cài đặt gói ngôn ngữ tiếng Việt (`vie.traineddata`) để quét tài liệu thô. |
| **EPUB Converter** | **Calibre CLI (ebook-convert) / Pandoc** | Các công cụ chuyển đổi dòng lệnh mạnh mẽ để đóng gói tệp tin HTML/Text sau OCR thành file `.epub` chuẩn. |
| **Chatbot AI/RAG Engine** | **LangChain & LlamaIndex (Python)** | Framework xử lý RAG kết nối Elasticsearch (Vector search) và LLMs (OpenAI/Ollama/Groq) để hỗ trợ hỏi đáp trực tuyến dựa trên văn bản sách đã OCR. |
| **Môi trường triển khai** | **Docker, Docker Compose, Kubernetes** | Toàn bộ các dịch vụ được đóng gói thành Docker Images, chạy Docker Compose ở môi trường Staging/Dev và deploy lên AWS EKS hoặc Azure AKS ở môi trường Production. |
| **CI/CD Pipeline** | **GitHub Actions / GitLab CI** | Tự động chạy test, build Docker image và deploy lên Kubernetes Cluster khi có commit code mới. |

---

## 3. Phương án Bảo mật, Sao lưu & Khôi phục Thảm họa (Backup & Disaster Recovery)

### 3.1. Chiến lược Bảo mật (Security Strategy)

*   **Mã hóa truyền tải:** Bắt buộc sử dụng HTTPS (TLS 1.3) cho toàn bộ request.
*   **Bảo mật tệp tin tài liệu:** 
    *   File EPUB gốc lưu trữ trên Cloud Storage (S3) được cấu hình ở chế độ Private (không thể truy cập công khai).
    *   Khi bạn đọc mở sách, backend LibDMS kiểm tra quyền truy cập (mức độ RBAC) rồi sinh ra **Signed URL** có thời hạn hiệu lực tối đa 15 phút.
    *   Trình đọc EPUB Reader trên Next.js frontend chặn chuột phải (ngăn sao chép text), ẩn tính năng in ấn mặc định của trình duyệt và không hiển thị nút tải file về.
*   **Xác thực và Phân quyền:**
    *   Hệ thống sử dụng cơ chế xác thực **JWT (JSON Web Token)** đính kèm cookie bảo mật (`httpOnly`, `secure`, `sameSite`).
    *   Phân quyền RBAC (Admin, Librarian, Reader) được kiểm tra ở cả tầng frontend (chặn điều hướng) và backend (API Guards).

### 3.2. Sao lưu và Khôi phục dữ liệu (Backup & DR)

*   **Sao lưu Database:** Sử dụng công cụ tự động snapshot hàng ngày của dịch vụ đám mây (như AWS RDS backup) hoặc chạy PgBackRest sao lưu tự động lúc 02:00 AM, giữ tối thiểu 30 bản backup gần nhất.
*   **Sao lưu File Storage:** Cấu hình **Cross-Region Replication (CRR)** trên AWS S3 để tự động đồng bộ tệp tin EPUB sang một Region vật lý độc lập khác nhằm đề phòng thảm họa mất trung tâm dữ liệu.
*   **Chỉ số khôi phục thảm họa:**
    *   *RPO (Recovery Point Objective):* Dưới 24 giờ (đảm bảo mất dữ liệu tối đa trong 1 ngày làm việc).
    *   *RTO (Recovery Time Objective):* Dưới 4 giờ (hệ thống phục hồi hoạt động hoàn toàn từ bản backup cloud gần nhất khi xảy ra thảm họa phần cứng).

---

## 4. Quy trình Nghiệp vụ & Vận hành Chi tiết

Sơ đồ tuần tự dưới đây mô tả quá trình số hóa tài liệu từ đầu vào thô sang EPUB và lưu trữ trên LibDMS:

![Sơ đồ Tuần tự Số hóa Tài liệu](file:///d:/Project/hcmus-projectmanage--lab/docs/images/submission_workflow.svg)

1.  **Librarian** truy cập admin dashboard, thực hiện tải lên tệp tin thô (PDF scan, PNG, JPEG) và nhập Metadata cơ bản (tiêu đề, tác giả, category, tags).
2.  Backend LibDMS tiếp nhận file, lưu tệp gốc vào **AWS S3 Storage**, tạo bản ghi tài liệu ở trạng thái "Processing" trong **PostgreSQL**.
3.  Backend gửi một message chứa thông tin file vào hàng đợi (Message Queue).
4.  **OCR & Converter Worker** nhận message, tải ảnh từ Storage xuống, gọi **Tesseract OCR** để trích xuất text tiếng Việt.
5.  Worker sắp xếp cấu trúc text, gọi **Calibre/Pandoc** đóng gói thành file EPUB. File EPUB mới sinh được upload ngược lại lên **Storage**.
6.  Worker cập nhật trạng thái tài liệu thành "Completed", đồng thời gửi text sau OCR sang **Elasticsearch** để lập chỉ mục tìm kiếm toàn văn.
7.  Hệ thống gửi thông báo cho thủ thư kiểm duyệt. Thủ thư có thể mở trang hiệu đính (Correction Dashboard) để chỉnh sửa lỗi chính tả phát sinh do OCR trước khi cho phép xuất bản chính thức tới bạn đọc.
