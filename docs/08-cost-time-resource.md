# KẾ HOẠCH CHI PHÍ, TIẾN ĐỘ & NGUỒN LỰC DỰ ÁN (COST, TIME & RESOURCE PLAN)

## Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS (HCMUS-LDMS)

**Trường Đại học Khoa học Tự nhiên, ĐHQG-HCM (HCMUS) — Thư viện & Phòng Công nghệ Thông tin**

Phiên bản 1.0 • Tháng 7/2026

## Mục lục

* [1. Kế hoạch Thời gian & Tiến độ (Time & Schedule Plan)](#1-kế-hoạch-thời-gian--tiến-độ-time--schedule-plan)
* [2. Dự toán Chi phí & Ngân sách (Cost & Budget Plan)](#2-dự-toán-chi-phí--ngân-sách-cost--budget-plan)
* [3. Kế hoạch Phân bổ Nguồn lực (Resource Plan)](#3-kế-hoạch-phân-bổ-nguồn-lực-resource-plan)

---

## 1. Kế hoạch Thời gian & Tiến độ (Time & Schedule Plan)

Dự án có tổng thời gian thực hiện dự kiến là **20 tuần**, chia làm 4 giai đoạn lớn theo mô hình Gating chặt chẽ để kiểm soát chất lượng và rủi ro đầu tư.

### 1.1. Lộ trình Triển khai 4 Giai đoạn (Roadmap)
1.  **Giai đoạn 0: Chuẩn bị & Khảo sát (Tuần 1 - Tuần 2):** Khảo sát chi tiết hiện trạng sách, chốt quy chế bản quyền và lấy báo giá thiết bị scan.
2.  **Giai đoạn 1: Xây dựng MVP Thí điểm (Tuần 3 - Tuần 12):** Thiết kế kiến trúc, lập trình UI, tích hợp OCR/EPUB và số hóa thí điểm 500 cuốn sách ngành Công nghệ thông tin.
3.  **Giai đoạn 2: Số hóa Diện rộng (Tuần 13 - Tuần 18):** Chuyển giao quy trình cho thư viện, tuyển CTV sinh viên và số hóa hàng loạt 2.000 giáo trình cốt lõi tiếp theo.
4.  **Giai đoạn 3: Nghiệm thu & Chuyển giao (Tuần 19 - Tuần 20):** Kiểm thử nghiệm thu toàn diện (UAT), bàn giao hệ thống và chính thức go-live toàn trường.

### 1.2. Phân rã Công việc (Work Breakdown Structure - WBS)
Tiến độ được theo dõi qua 6 Gói công việc (Work Packages - WP):
*   **WP1 — Khảo sát & Bản quyền (Tuần 1-3):** Thực hiện 15-20 cuộc phỏng vấn sinh viên, chốt quy chế bản quyền và hoàn thiện biểu mẫu consent giảng viên.
*   **WP2 — Cơ sở dữ liệu & Backend (Tuần 4-7):** Thiết lập cơ sở dữ liệu PostgreSQL, cài đặt MinIO Object Storage, cấu hình Keycloak SSO và tích hợp Tesseract OCR/Pandoc.
*   **WP3 — Giao diện & Trình đọc (Tuần 6-10):** Phát triển Portal tìm kiếm React, thiết kế Split-screen chỉnh sửa OCR và tích hợp thư viện Epub.js cho Web Reader.
*   **WP4 — Số hóa tài liệu (Tuần 11-17):** Tiến hành scan sách cứng, chạy OCR, thủ thư/sinh viên hiệu chỉnh chính tả, đóng gói EPUB và index Elasticsearch.
*   **WP5 — Kiểm thử & Nghiệm thu (Tuần 18-19):** Chạy kiểm thử tự động, đánh giá bảo mật (Pentest) và lấy ý kiến UAT từ thủ thư và độc giả.
*   **WP6 — Triển khai & Vận hành (Tuần 20):** Triển khai Docker production trên server trường, đào tạo cán bộ thư viện và truyền thông ra mắt.

### 1.3. Đường Găng Tiến độ (Critical Path) & Các Cột mốc (Milestones)
*   **Đường găng dự án (Critical Path):** Nằm tại **WP4 (Số hóa tài liệu)**. Khâu scan sách và sửa lỗi chính tả OCR thô chiếm thời gian dài nhất và phụ thuộc lớn vào năng suất của thủ thư và sinh viên CTV. Sự chậm trễ ở WP4 sẽ trực tiếp kéo lùi ngày bàn giao dự án.
*   **Mốc M1 (Tuần 3):** Hoàn thành quy chế pháp lý bản quyền và chốt phương án mua máy quét.
*   **Mốc M2 (Tuần 12):** Hoàn thành phát triển phần mềm MVP, thử nghiệm thành công trên 500 cuốn sách thí điểm.
*   **Mốc M3 (Tuần 19):** Hoàn tất nghiệm thu UAT toàn trường, sẵn sàng triển khai chính thức.

---

## 2. Dự toán Chi phí & Ngân sách (Cost & Budget Plan)

Tổng ngân sách đầu tư ban đầu ước tính từ **$45.000 đến $85.000**, phân bổ chi tiết cho CapEx (Chi phí đầu tư ban đầu) và OpEx (Chi phí vận hành hàng năm).

### 2.1. Chi phí Đầu tư Ban đầu (CapEx Breakdown)
*   **Thiết bị phần cứng (Scanners & Server):** **$15.000 – $35.000**
    *   02 máy quét sách chuyên dụng chữ V bảo vệ gáy sách.
    *   Thiết bị nâng cấp RAM/SSD cho cụm máy chủ ảo hóa VMware hiện có của trường.
*   **Phát triển phần mềm (Software Development):** **$20.000 – $35.000**
    *   Chi phí nhân sự lập trình (4 kỹ sư phòng CNTT làm việc kiêm nhiệm 50% thời gian trong 20 tuần).
    *   Tích hợp và cấu hình Keycloak, Elasticsearch, PostgreSQL.
*   **Số hóa & Hiệu chỉnh dữ liệu (Data Digitization):** **$5.000 – $10.000**
    *   Học bổng/chi phí hỗ trợ sinh viên CTV tham gia sửa lỗi chính tả OCR thô trong 7 tuần (khoảng 10-15 sinh viên xoay ca).
*   **Chi phí dự phòng rủi ro phát sinh (Contingency - 15%):** **$5.000 – $10.000**

### 2.2. Chi phí Vận hành Hàng năm (OpEx Breakdown)
*   **Bảo trì hệ thống & Hỗ trợ kỹ thuật:** **$3.000 – $6.000 / năm**
    *   Lương hỗ trợ kỹ thuật định kỳ cho kỹ sư vận hành.
*   **Khấu hao thiết bị & Điện năng:** **$2.000 – $4.000 / năm**
*   **Dự phòng phí OCR thương mại (Google Cloud Vision):** **$1.000 – $3.000 / năm** (Dành riêng cho xử lý các tài liệu cũ nát, chất lượng in cực kém).
*   **Tên miền & Chứng chỉ bảo mật SSL:** **$200 – $400 / năm**

### 2.3. Hiệu quả Kinh tế & Điểm Hòa vốn (Cost Avoidance & ROI)
*   **Mô hình Cost Avoidance:** Dự án giúp trường thu hồi **60-70% diện tích kho kệ** sách cũ tại cơ sở Nguyễn Văn Cừ để cải tạo thành phòng tự học thông minh, tiết kiệm chi phí thuê/xây dựng cơ sở vật chất mới (tránh được khoảng $15.000/năm). Đồng thời giảm **85% thời gian thủ thư** xử lý tìm kiếm và giao nhận sách giấy trực tiếp.
*   **Thời gian hoàn vốn (Payback Period):** Dự kiến từ **1.6 đến 2.8 năm** sau khi go-live dựa trên việc cắt giảm chi phí bảo quản sách giấy vật lý, tiết kiệm nhân công thủ thư và giá trị thu hồi không gian kho bãi vật chất.

---

## 3. Kế hoạch Phân bổ Nguồn lực (Resource Plan)

### 3.1. Phân bổ Nhân sự (Human Resources)
Dự án tận dụng tối đa nguồn lực nội bộ sẵn có của HCMUS kết hợp với sinh viên cộng tác viên:

1.  **Nhóm Kỹ thuật (Phòng CNTT HCMUS - Kiêm nhiệm 50%):**
    *   *Project Manager / Solution Architect (01 người):* Quản lý tiến độ, thiết kế cấu trúc hệ thống và tích hợp bảo mật.
    *   *Backend Developer (01 người):* Lập trình FastAPI, cấu hình MinIO, Keycloak, PostgreSQL.
    *   *Frontend Developer (01 người):* Lập trình cổng thông tin React, tích hợp Epub.js.
    *   *DevOps / System Administrator (01 người):* Cài đặt Elasticsearch, CI/CD Docker, thiết lập backup PgBackRest/Restic.
2.  **Nhóm Nghiệp vụ & Vận hành (Thư viện HCMUS):**
    *   *Thủ thư Quản lý (02 người):* Phụ trách quét sách cứng, kiểm duyệt chất lượng file EPUB cuối cùng, phân loại Category/Tag.
    *   *Cộng tác viên Sinh viên (10-15 người làm việc theo ca):* Soát lỗi chính tả chữ OCR thô trên giao diện Split-screen dưới sự hướng dẫn của thủ thư.

### 3.2. Trang thiết bị & Hạ tầng Vật lý
*   **Văn phòng số hóa:** Bố trí 01 phòng làm việc yên tĩnh tại Thư viện cơ sở Nguyễn Văn Cừ, trang bị sẵn máy điều hòa nhiệt độ ổn định để vận hành 02 máy quét sách.
*   **Hạ tầng máy chủ (Server):** Sử dụng hệ thống máy chủ vật lý hiện có của Phòng CNTT, phân vùng 03 máy chủ ảo hóa VM chạy CentOS để thiết lập 3 môi trường: Dev, Staging, và Production.

### 3.3. Ma trận Phân bổ Trách nhiệm (RACI Matrix)

| Gói công việc (WP) | BGH (Sponsor) | Trưởng phòng CNTT (PM/SA) | Đội Kỹ thuật (Dev/DevOps) | Giám đốc Thư viện (Client) | Thủ thư (User) | Sinh viên CTV |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **WP1: Khảo sát & Bản quyền** | I | A | C | R | R | C |
| **WP2: Backend & DB** | I | A | R | I | I | - |
| **WP3: UI & Trình đọc** | I | A | R | C | R | - |
| **WP4: Số hóa tài liệu** | I | I | C | A | R | R |
| **WP5: Kiểm thử & UAT** | I | A | R | C | R | C |
| **WP6: Triển khai & Vận hành**| I | A | R | R | R | - |

*Chú thích:* **R (Responsible):** Người trực tiếp thực hiện; **A (Accountable):** Người chịu trách nhiệm phê duyệt cuối cùng; **C (Consulted):** Người được tham vấn ý kiến; **I (Informed):** Người được nhận thông tin thông báo.
