# ARCHITECTURE (HOW)

## Kho Lưu trữ Số Khóa luận Tốt nghiệp HCMUS

**Trường Đại học Khoa học Tự nhiên, ĐHQG-HCM (HCMUS) — Thư viện & Phòng Công nghệ Thông tin**

Phiên bản 1.0 • Tháng 7/2026

## Mục lục

* [1. Phong cách Kiến trúc](#1-phong-cách-kiến-trúc)
* [2. Ngăn xếp Công nghệ](#2-ngăn-xếp-công-nghệ)
* [3. Phương án Bảo mật, Sao lưu & Khôi phục Thảm họa (Backup & Disaster Recovery)](#3-phương-án-bảo-mật-sao-lưu--khôi-phục-thảm-họa-backup--disaster-recovery)
* [4. Quy trình Nghiệp vụ & Vận hành Chi tiết](#4-quy-trình-nghiệp-vụ--vận-hành-chi-tiết)

---

## 1. Phong cách Kiến trúc

![Mô hình kiến trúc hệ thống (System Architecture)](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/docs/images/system_architecture.svg)

**Lựa chọn: Modular monolith trên nền tảng mã nguồn mở DSpace 7.x/8.0 (sử dụng Angular frontend và Java REST API backend), kết hợp dịch vụ tìm kiếm Solr/Elasticsearch tách rời và cổng dịch vụ AI/RAG vệ tinh (triển khai ở giai đoạn sau).**

| Lý do chọn                                         | Giải thích                                                                                                                                                                                                                                    |
| -------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Không chọn xây mới (build from scratch)            | Nền tảng mã nguồn mở đã kiểm chứng rộng rãi trong ngành thư viện số, có sẵn mô hình dữ liệu Dublin Core, quản lý phân quyền, workflow duyệt xuất bản — rút ngắn thời gian phát triển và giảm rủi ro kỹ thuật so với tự thiết kế từ đầu.       |
| Không chọn microservices ngay từ MVP               | Đội ngũ vận hành nhỏ (nội bộ CNTT, không có đội SRE chuyên trách); khối lượng nghiệp vụ ở MVP không đòi hỏi mở rộng độc lập theo từng service; kiến trúc phân tán sẽ tăng chi phí vận hành/giám sát không cần thiết ở giai đoạn này.          |
| Tách riêng lớp tìm kiếm (Elasticsearch/OpenSearch) | Tìm kiếm toàn văn là năng lực lõi của MVP, cần hiệu năng và khả năng mở rộng độc lập với phần lõi repository — tách thành dịch vụ riêng nhưng vẫn nằm trong cùng hệ thống, không phải microservice độc lập theo nghĩa vận hành riêng đội ngũ. |
| Tách riêng lớp AI/RAG (giai đoạn sau, tùy chọn)    | Chỉ triển khai khi có ngân sách/nhu cầu xác nhận (Giai đoạn 3); tách thành dịch vụ độc lập để không ảnh hưởng đến độ ổn định của repository lõi khi thử nghiệm công nghệ mới (embedding, vector search).                                      |
| Giải quyết bài toán bảo trì/tích hợp               | Nền tảng mã nguồn mở có cộng đồng hỗ trợ dài hạn, giảm phụ thuộc vào một nhà cung cấp duy nhất (không vendor lock-in nặng); hỗ trợ chuẩn tích hợp phổ biến (SSO/LDAP, OAI-PMH) để kết nối với hệ thống quản lý đào tạo hiện có của trường.    |

## 2. Ngăn xếp Công nghệ

| Thành phần | Lựa chọn cụ thể | Lý do & Phiên bản |
| :--- | :--- | :--- |
| **Nền tảng lõi (repository)** | **DSpace 7.x/8.0** | Nền tảng mã nguồn mở phổ biến và ổn định nhất thế giới dành cho thư viện số học thuật, hỗ trợ sẵn chuẩn Dublin Core, quản lý phân quyền, workflow duyệt và tích hợp định danh Handle ID. |
| **Frontend** | **Angular 16+** (custom) | DSpace 7.x/8.0 sử dụng Angular làm giao diện mặc định. Đội ngũ phát triển tùy biến theme Angular bằng HTML5, CSS3 (Sass) và Bootstrap để đồng bộ nhận diện thương hiệu HCMUS. |
| **Backend API Server** | **Java 17 (Spring Boot)** | DSpace core chạy trên nền Spring Boot, cung cấp hệ thống REST API mạnh mẽ, bảo mật và kế thừa toàn bộ logic nghiệp vụ lưu trữ học thuật của DSpace. |
| **Web Server / Proxy** | **Nginx 1.24+** & **Tomcat 10** | Nginx đóng vai trò Web Server phục vụ Angular static files, Reverse Proxy chuyển hướng request đến Apache Tomcat 10 container (chạy backend API), và xử lý SSL/TLS 1.3. |
| **Cơ sở dữ liệu** | **PostgreSQL 16** | Hệ quản trị cơ sở dữ liệu quan hệ mạnh mẽ, được tối ưu sẵn cho DSpace, hỗ trợ tốt kiểu dữ liệu JSON và cho phép tích hợp tiện ích mở rộng `pgvector` cho nhu cầu AI ở giai đoạn sau. |
| **Tìm kiếm & Chỉ mục** | **Solr 9.x** & **Elasticsearch 8.x** | Solr 9.x được tích hợp sẵn làm công cụ tìm kiếm và thống kê mặc định của DSpace. Elasticsearch 8.x được triển khai tách rời như một dịch vụ vệ tinh để cung cấp tính năng tìm kiếm toàn văn (full-text search) nâng cao với hiệu năng cao hơn. |
| **Xác thực & SSO** | **Keycloak 24.x** kết nối **LDAP/Active Directory** | Keycloak làm Identity Provider (IdP) quản lý phiên đăng nhập tập trung (SSO) qua OIDC/SAML2, cấu hình đồng bộ trực tiếp với máy chủ LDAP/Active Directory sẵn có của HCMUS. |
| **Lưu trữ tệp (Storage)** | **MinIO (On-premise Object Storage)** | Giải pháp lưu trữ đối tượng tương thích S3 chạy cục bộ (on-premise) trên hạ tầng máy chủ của trường, hỗ trợ mã hóa tĩnh (encryption at rest) và phân quyền truy cập thông qua Signed URL bảo mật. |
| **Dịch vụ AI/RAG (Giai đoạn sau)** | • **Python 3.11** (FastAPI/LangChain)<br>• **Qdrant** (Vector DB)<br>• Embedding **BAAI/bge-m3**<br>• LLM **Llama-3-8B-Instruct** | Triển khai như một dịch vụ vệ tinh (Microservice độc lập) kết nối qua API với DSpace lõi. Qdrant lưu trữ vector biểu diễn. Sử dụng mô hình nguồn mở Llama-3-8B chạy GPU cục bộ để tránh rò rỉ dữ liệu học thuật ra bên ngoài. |
| **Hạ tầng triển khai** | **Docker & Docker Compose**, **VMware/Proxmox VMs** | Sử dụng Docker để đóng gói toàn bộ các dịch vụ (Tomcat, Angular, Nginx, PostgreSQL, Solr, MinIO, Keycloak). Chạy trên hệ thống ảo hóa của phòng máy chủ trường để tối ưu hóa tài nguyên phần cứng. |
| **Công cụ Sao lưu & DR** | **PgBackRest** (cho DB) và **Restic** (cho MinIO storage) | PgBackRest hỗ trợ backup gia tăng (incremental backup) tự động hàng ngày. Restic hỗ trợ backup và mã hóa file PDF sang máy chủ backup độc lập ngoài mạng chính của trường (off-site backup). |

## 3. Phương án Bảo mật, Sao lưu & Khôi phục Thảm họa (Backup & Disaster Recovery)

Để giải quyết bài toán độ tin cậy và cam kết mức độ dịch vụ (SLA 99.5%), hệ thống thiết lập các chính sách bảo mật và khôi phục dữ liệu chi tiết sau:

### 3.1. Chiến lược Sao lưu (Backup Strategy)
*   **Sao lưu cơ sở dữ liệu (PostgreSQL):** Thực hiện sao lưu gia tăng (incremental backup) tự động hàng ngày lúc 01:00 AM và sao lưu toàn phần (full backup) vào mỗi Chủ nhật. File backup được mã hóa AES-256.
*   **Sao lưu tệp tin số hóa (Object Storage):** Áp dụng cơ chế đồng bộ hóa thời gian thực (real-time replication) sang một vùng lưu trữ thứ cấp độc lập (off-site storage) nằm ngoài hệ thống mạng chính của trường để tránh rủi ro mất mát dữ liệu do ransomware.
*   **Thời gian lưu trữ bản sao lưu:** Giữ tối thiểu 30 bản sao lưu ngày gần nhất và 12 bản sao lưu tháng gần nhất.

### 3.2. Chỉ số phục hồi & Khôi phục thảm họa (Disaster Recovery)
*   **RPO (Recovery Point Objective):** Tối đa **24 giờ** (đảm bảo mất mát dữ liệu không vượt quá lượng công việc của 1 ngày trong trường hợp xấu nhất).
*   **RTO (Recovery Time Objective):** Tối đa **4 giờ** (thời gian phục dựng lại toàn bộ hệ thống từ bản sao lưu gần nhất khi xảy ra thảm họa phần cứng).
*   **Kịch bản diễn tập:** Tổ chức diễn tập khôi phục hệ thống (mock disaster recovery) định kỳ 6 tháng một lần do Phòng CNTT chủ trì.

### 3.3. Các lớp bảo mật (Security Layers)
*   **Mã hóa truyền tải:** Bắt buộc sử dụng giao thức HTTPS (TLS 1.3) cho toàn bộ phiên truy cập.
*   **Mã hóa lưu trữ:** File PDF lưu trữ trong Object Storage được mã hóa tĩnh (encryption at rest).
*   **Xác thực và Phân quyền:**
    *   Sinh viên và cán bộ đăng nhập qua **Keycloak SSO** (OIDC/SAML2) kết nối với hệ thống LDAP/Active Directory của trường để đồng bộ tài khoản.
    *   Hệ thống kiểm soát quyền đọc tệp tin PDF trực tiếp ở mức ứng dụng DSpace. Link tải file từ **MinIO** được sinh tự động dưới dạng Signed URL có thời hạn hiệu lực tối đa 15 phút để ngăn chặn hành vi tải tệp hàng loạt bất hợp pháp.

---

## 4. Quy trình Nghiệp vụ & Vận hành Chi tiết

Sơ đồ tuần tự (Sequence Diagram) dưới đây mô tả chi tiết sự tương tác giữa các tác nhân và hệ thống trong quy trình nộp, duyệt và xuất bản khóa luận tốt nghiệp:

![Sơ đồ Tuần tự Nộp & Duyệt Khóa luận](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/docs/images/submission_workflow.svg)

1. **Sinh viên** truy cập cổng thông tin và đăng nhập qua hệ thống **Keycloak SSO** kết nối **LDAP/Active Directory** tập trung của trường.
2. Sau khi xác thực thành công, sinh viên tải lên tệp tin khóa luận (PDF) và nhập dữ liệu mô tả (**Metadata Dublin Core**), đồng thời thực hiện ký cam kết bản quyền số (**Consent Form**).
3. Hệ thống lưu trữ thông tin ở trạng thái bản nháp và lưu tệp tin PDF an toàn vào **MinIO Object Storage**.
4. Hệ thống thông báo cho **Thủ thư** để thực hiện kiểm duyệt.
5. Thủ thư truy cập dashboard quản trị để rà soát chất lượng metadata và file PDF.
6. Nếu hợp lệ, thủ thư duyệt và cấu hình mức độ truy cập (Public/Internal/Embargo). Hệ thống cập nhật trạng thái xuất bản, đồng thời gửi thông tin sang **Elasticsearch 8.x** để lập chỉ mục toàn văn. Hệ thống gán mã định danh bền vững (**Handle ID**) và tự động gửi email xác nhận kèm link truy cập cho sinh viên.
7. Nếu không hợp lệ (lỗi metadata hoặc sai định dạng), thủ thư từ chối bài nộp và hệ thống tự động gửi email yêu cầu sinh viên sửa đổi, cập nhật lại qua cổng thông tin.

