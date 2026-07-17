# KẾ HOẠCH CHI PHÍ, TIẾN ĐỘ & PHÂN BỔ NGUỒN LỰC DỰ ÁN

## Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS (HCMUS-LDMS)

### THÔNG TIN TÀI LIỆU (DOCUMENT CONTROL)

| Trường thông tin (Field)                   | Nội dung đặc tả (Description)                                              |
| :----------------------------------------- | :------------------------------------------------------------------------- |
| **Mã tài liệu (Document ID)**              | `HCMUS-LDMS-CTR`                                                           |
| **Tên tài liệu (Document Title)**          | Kế hoạch Chi phí, Tiến độ & Phân bổ Nguồn lực (Cost, Time & Resource Plan) |
| **Dự án (Project Name)**                   | HCMUS-LDMS                                                                 |
| **Đơn vị soạn thảo (Author/Organization)** | Thư viện & Phòng Công nghệ Thông tin - HCMUS                               |
| **Người xem xét (Reviewer)**               | Trưởng phòng CNTT & Giám đốc Thư viện                                      |
| **Người phê duyệt (Approver)**             | Ban Giám hiệu Trường ĐH Khoa học Tự nhiên                                  |
| **Cấp độ bảo mật (Security Class)**        | Internal (Nội bộ trường)                                                   |
| **Trạng thái tài liệu (Status)**           | Under Review (Đang thẩm định)                                              |

### LỊCH SỬ PHIÊN BẢN (REVISION HISTORY)

| Phiên bản (Version) | Ngày phát hành (Date) | Mô tả thay đổi (Description of Change)                                         | Người thực hiện (Author) |
| :-----------------: | :-------------------: | :----------------------------------------------------------------------------- | :----------------------: |
|         1.0         |      12/07/2026       | Khởi tạo dự thảo kế hoạch chi phí, tiến độ ban đầu (v1.0).                     |      Mạch Quốc Tấn       |
|         2.0         |      14/07/2026       | Trình bày LaTeX công thức UCP & COCOMO II, chi tiết hóa WBS và chuyển đổi VNĐ. |      Mạch Quốc Tấn       |

---

## Mục lục

- [1. Kế hoạch thời gian và Tiến độ thực hiện (Time & Schedule Plan)](#1-kế-hoạch-thời-gian-và-tiến-độ-thực-hiện-time--schedule-plan)
  - [1.1. Lộ trình triển khai 4 Giai đoạn](#11-lộ-trình-triển-khai-4-giai-đoạn)
  - [1.2. Phân rã gói công việc (WBS) và Đường găng (Critical Path)](#12-phân-rã-gói-công-việc-wbs-và-đường-găng-critical-path)
- [2. Phương pháp luận ước lượng nỗ lực phần mềm (Estimation)](#2-phương-pháp-luận-ước-lượng-nỗ-lực-phần-mềm-estimation)
  - [2.1. Phương pháp Điểm trường hợp sử dụng (Use Case Points - UCP)](#21-phương-pháp-điểm-trường-hợp-sử-dụng-use-case-points---ucp)
  - [2.2. Phương pháp COCOMO II (Early Design Model)](#22-phương-pháp-cocomo-ii-early-design-model)
  - [2.3. Đối chiếu và Kết luận nỗ lực thực tế](#23-đối-chiếu-và-kết-luận-nỗ-lực-thực-tế)
- [3. Dự toán chi phí và Phân bổ ngân sách dự án (Cost & Budget Plan)](#3-dự-toán-chi-phí-và-phân-bổ-ngân-sách-dự-án-cost--budget-plan)
  - [3.1. Dự toán chi phí đầu tư ban đầu (CapEx)](#31-dự-toán-chi-phí-đầu-tư-ban-đầu-capex)
  - [3.2. Dự toán chi phí vận hành định kỳ (OpEx)](#32-dự-toán-chi-phí-vận-hành-định-kỳ-opex)
- [4. Kế hoạch phân bổ nguồn lực nhân sự và Thiết bị](#4-kế-hoạch-phân-bổ-nguồn-lực-nhân-sự-và-thiết-bi)
- [5. Kế hoạch Giám sát & Báo cáo Tình trạng Dự án (Monitoring & Status Reporting)](#5-kế-hoạch-giám-sát--báo-cáo-tình-trạng-dự-án-monitoring--status-reporting)

---

## 1. Kế hoạch thời gian và Tiến độ thực hiện (Time & Schedule Plan)

Dự án HCMUS-LDMS được hoạch định thực hiện trong vòng **20 tuần** (5 tháng), chia làm 4 giai đoạn lớn kết hợp kiểm soát chốt cổng (Gating Checkpoints):

### 1.1. Lộ trình triển khai 4 Giai đoạn

- **Giai đoạn 0 — Khảo sát & Bản quyền (Tuần 1–2):** Nghiên cứu pháp lý, ký cam kết đồng ý của tác giả, khảo sát thực tế sách giấy và lấy báo giá thiết bị scan.
- **Giai đoạn 1 — Xây dựng MVP & Thí điểm (Tuần 3–12):** Phát triển phần mềm, tích hợp Google OAuth 2.0 / Mock Auth, MinIO, OCR, Pandoc, PostgreSQL FTS. Số hóa thí điểm 500 cuốn sách ngành CNTT đưa vào sử dụng ở tuần 12.
- **Giai đoạn 2 — Số hóa Diện rộng (Tuần 13–18):** Bàn giao quy trình số hóa, tuyển sinh viên CTV và tiến hành số hóa hàng loạt 2.000 giáo trình cốt lõi tiếp theo của các khoa khác.
- **Giai đoạn 3 — Nghiệm thu & Chuyển giao (Tuần 19–20):** Kiểm thử nghiệm thu (UAT), pentest bảo mật, đào tạo cán bộ thư viện và go-live toàn trường.

### 1.2. Phân rã gói công việc (WBS) và Đường găng (Critical Path)

- **WP1 — Khảo sát & Bản quyền (Tuần 1–3):** Phỏng vấn độc giả; hoàn thành quy chế số hóa.
- **WP2 — Cơ sở dữ liệu & Backend (Tuần 4–7):** Cấu hình ảo hóa VMware; cài đặt PostgreSQL, MinIO, và phát triển Mock Auth / Google OAuth 2.0.
- **WP3 — Giao diện & Trình đọc (Tuần 8–11):** Code React UI; tích hợp Epub.js, Tesseract, Pandoc và PostgreSQL FTS.
- **WP4 — Số hóa tài liệu (Tuần 12–17) [Đường găng - Critical Path]:** Quét sách giấy; chạy OCR; biên tập Split-screen; đóng gói EPUB. Khâu scan sách và soát sửa lỗi chính tả chiếm thời gian dài nhất và phụ thuộc lớn vào năng suất của con người. Sự chậm trễ ở WP4 sẽ trực tiếp kéo lùi ngày bàn giao dự án.
- **WP5 — Kiểm thử & UAT (Tuần 18–19):** Pentest bảo mật; nghiệm thu UAT với thủ thư và sinh viên mẫu.
- **WP6 — Triển khai & Vận hành (Tuần 20):** Triển khai Docker Compose; đào tạo cán bộ; truyền thông ra mắt.

## 2. Ước lượng nỗ lực phát triển (Effort Estimation)

Để lập kế hoạch nhân sự và tiến độ một cách khoa học, Phòng CNTT đã thực hiện ước lượng nỗ lực phát triển (effort estimation) thông qua việc đối chuẩn giữa hai phương pháp: **Use Case Points (UCP)** (tiếp cận theo độ phức tạp tính năng) và **COCOMO II** (tiếp cận theo quy mô dòng lệnh).

### 2.1. Tóm tắt kết quả ước lượng theo Use Case Points (UCP)

Phương pháp này phân tích độ phức tạp dựa trên các tác nhân (Actors) và các kịch bản nghiệp vụ (Use Cases) của hệ thống:

* **Phân tích tác nhân (Actors Weight):** Hệ thống tương tác với 3 tác nhân hệ thống (Google OAuth, MinIO, PostgreSQL API) và 4 nhóm người dùng trực tiếp (Độc giả, Thủ thư, Biên tập viên, Quản trị viên). Tổng trọng số tác nhân (UAW) là **15**.
* **Phân tích ca sử dụng (Use Cases Weight):** Dựa trên 14 Use Cases nghiệp vụ cốt lõi từ Product Backlog (phân bổ thành 6 Use Cases đơn giản, 4 Use Cases trung bình và 4 Use Cases phức tạp). Tổng trọng số Use Case (UUCW) là **130**.
* **Hệ số điều chỉnh kỹ thuật & môi trường (TCF & ECF):**
  * Hệ số kỹ thuật (TCF = 1.13): Đánh giá cao tính bảo mật (Signed URL, DRM), hiệu năng tìm kiếm toàn văn dưới 3 giây và tính phân tán nhẹ.
  * Hệ số môi trường (ECF = 0.785): Tận dụng năng lực của đội ngũ kỹ sư Phòng CNTT quen thuộc với React/FastAPI/Docker, nhưng tính đến rủi ro nhân sự kiêm nhiệm 50%.
* **Kết quả:** Điểm Use Case điều chỉnh đạt **129 UCP**. Với năng suất trung bình 20 người-giờ/UCP, tổng nỗ lực lý thuyết là **16.1 Người-Tháng (Person-Months - PM)**.
* **Điều chỉnh thực tế:** Nhờ tận dụng tối đa kiến trúc Modular Monolith và khả năng tái sử dụng cấu hình sẵn có của PostgreSQL, MinIO (tiết kiệm ~40% nỗ lực viết mới), nỗ lực thực tế được tối ưu hóa xuống còn **10 PM** (tương đương **5 tháng** làm việc của đội ngũ kỹ sư).

### 2.2. Đối chuẩn bằng phương pháp COCOMO II

Để kiểm chứng tính thực tế của phương pháp UCP, chúng tôi đối chuẩn với mô hình COCOMO II (Early Design Model):

* **Quy mô dòng lệnh (Size):** Dự kiến hệ thống viết mới khoảng **8.5 KLOC** (8.500 dòng mã nguồn React và FastAPI).
* **Mức độ tái sử dụng (Reuse):** Tích hợp sâu các dịch vụ mã nguồn mở (MinIO Storage, PostgreSQL FTS, Google OAuth) giúp giảm khối lượng code viết mới thực tế xuống còn **3.5 KLOC**.
* **Kết quả nỗ lực:** Mô hình COCOMO II cho kết quả nỗ lực thực tế viết mới là **10.4 PM**.

### 2.3. Kết luận nỗ lực và Phân bổ thời gian

Kết quả đối chuẩn giữa hai phương pháp độc lập cho thấy độ tin cậy rất cao:
* Theo UCP (đã tối ưu hóa): **10.0 PM**
* Theo COCOMO II (đã tối ưu hóa): **10.4 PM**

**Quyết định chọn:** Ban dự án thống nhất chọn hạn mức **10.5 PM** làm cơ sở hoạch định nhân sự.
* Với đội ngũ **4 kỹ sư kiêm nhiệm 50% thời gian** (tương đương sức lao động của 2 nhân sự full-time), thời gian phát triển phần mềm cốt lõi sẽ kéo dài:
  $$\text{Thời gian phát triển thực tế} = \frac{10.5 \text{ PM}}{2 \text{ nhân sự}} = 5.25 \text{ tháng } (\approx 21 \text{ tuần})$$
* Để khớp với thời hạn **20 tuần** go-live của nhà trường, nhóm sẽ áp dụng quy trình phát triển song song (Parallel Development) giữa Frontend và Backend từ tuần thứ 4 đến tuần thứ 11, đồng thời tuyển sinh viên CTV tham gia số hóa cuốn chiếu ngay khi hoàn thành phiên bản MVP ở tuần 12.

---

## 3. Dự toán chi phí và Phân bổ ngân sách dự án (Cost & Budget Plan)

### 3.1. Dự toán chi phí đầu tư ban đầu (CapEx)

Tổng chi phí CapEx dao động từ **75.000.000 VNĐ – 95.000.000 VNĐ**:

- **Số hóa dữ liệu & Biên tập EPUB:** 30.000.000 VNĐ – 40.000.000 VNĐ (thuê sinh viên CTV scan và sửa lỗi OCR cho ~10.000 cuốn sách).
- **Phát triển phần mềm:** 25.000.000 VNĐ – 35.000.000 VNĐ (chi phí nhân lực 4 kỹ sư Phòng CNTT tự phát triển).
- **Hạ tầng thiết bị:** 10.000.000 VNĐ – 12.000.000 VNĐ (02 máy scan chuyên dụng chữ V và nâng cấp cụm máy chủ ảo hóa VMware).
- **Đào tạo & Triển khai:** 5.000.000 VNĐ – 8.000.000 VNĐ (tài liệu hướng dẫn, video, tập huấn).
- **Dự phòng rủi ro phát sinh (15%):** 5.000.000 VNĐ – 10.000.000 VNĐ.

### 3.2. Dự toán chi phí vận hành định kỳ (OpEx)

Tổng chi phí OpEx hàng năm duy trì từ năm thứ 2 ước tính **15.000.000 VNĐ – 30.000.000 VNĐ / năm**:

- **Hạ tầng máy chủ ảo hóa:** 4.000.000 VNĐ – 8.000.000 VNĐ / năm (điện, mạng băng thông cao, bảo quản).
- **Bảo trì & Hỗ trợ kỹ thuật:** 6.000.000 VNĐ – 12.000.000 VNĐ / năm (vá lỗi bảo mật, nâng cấp thư viện).
- **API OCR dự phòng (Cloud OCR):** 3.000.000 VNĐ – 6.000.000 VNĐ / năm (dùng khi gặp tài liệu quá mờ).
- **Số hóa bổ sung sách mới:** 2.000.000 VNĐ – 4.000.000 VNĐ / năm.

---

## 4. Kế hoạch phân bổ nguồn lực nhân sự và Thiết bị

### 4.1. Phân bổ nhân sự (Human Resources)

- **Project Manager / Solution Architect (01 người):** Điều phối tiến độ, thiết kế kiến trúc hệ thống, quản lý rủi ro và tích hợp Google OAuth 2.0.
- **Backend Developer (01 người):** Lập trình các API FastAPI, tích hợp module OCR Tesseract và đóng gói Pandoc EPUB.
- **Frontend Developer (01 người):** Lập trình UI React Portal, tích hợp trình đọc Epub.js.
- **DevOps / System Admin (01 người):** Quản trị CSDL PostgreSQL, cài đặt MinIO, Docker Compose và thiết lập CI/CD.
- **Thủ thư (02 người):** Vận hành máy scan chữ V, kiểm duyệt chất lượng sách xuất bản.
- **Sinh viên CTV (10-15 người):** Sửa lỗi chính tả OCR thô trực tuyến trên màn hình Split-screen.

### 4.2. Phân bổ thiết bị & Server ảo hóa

- **Thiết bị scan:** 02 máy quét sách chữ V lắp đặt tại phòng số hóa thư viện.
- **Phân vùng máy chủ ảo hóa VMware:**
  - `VM-Dev:` 4 vCPU, 8 GB RAM, 100 GB SSD (môi trường lập trình).
  - `VM-Staging:` 4 vCPU, 16 GB RAM, 200 GB SSD (môi trường kiểm thử và UAT).
  - `VM-Production:` 8 vCPU, 32 GB RAM, 2 TB HDD + 500 GB SSD (vận hành chính thức, chứa tệp EPUB và cơ sở dữ liệu PostgreSQL FTS).

## 5. Kế hoạch Giám sát & Báo cáo Tình trạng Dự án (Monitoring & Status Reporting)

Để quản lý tiến độ và kiểm soát hiệu quả của dự án phát triển phần mềm với sự trợ giúp của AI Coding Assistants, hệ thống giám sát định kỳ (Project Monitoring and Control) được thiết lập thông qua các chỉ số sau:

### 5.1. Bộ chỉ số Giám sát & Đo lường (Monitoring Metrics)

- **Throughput (T):** Đo lường số lượng User Story chuyển trạng thái sang `Done` (đáp ứng đủ Definition of Done) trong **mỗi 7 ngày**. Dùng công thức forecast: Dev weeks ≈ N (story còn lại) / T.
- **Thời gian chu kỳ (Cycle Time):** Đo lường thời gian từ lúc kéo card vào _In Progress_ đến khi card đạt `Done` (deploy + AC pass). Mục tiêu giữ cycle time trung bình dưới **3 ngày** đối với card size M.
- **Tốc độ xử lý của AI Assistant (AI Productivity Factor):** Theo dõi hiệu suất sinh mã nguồn của các AI Coding Assistants (Claude Code, Copilot) nhằm cân bằng tốc độ phát triển và tốc độ review của kỹ sư (tránh tình trạng sinh code quá nhanh gây quá tải khâu thẩm định).
- **Số lượng Token sử dụng & Chi phí API:** Giám sát lượng token tiêu thụ hàng tuần và chi phí sử dụng API của các AI Assistant ở background, đảm bảo tổng chi phí API phát triển luôn nằm trong hạn mức **5.000.000 VNĐ** (đã dự toán trong CapEx).

### 5.2. Quy chế Báo cáo định kỳ (Status Reporting)

- **Báo cáo Weekly Review (Mỗi tuần):** PM tổng hợp báo cáo gửi Ban Giám đốc Thư viện và Trưởng phòng CNTT về: throughput tuần (số story Done), cycle time trung bình, tổng chi phí thực tế đã chi, và các rủi ro phát sinh.
- **Báo cáo Chốt cổng Giai đoạn (Phase-Gating Report):** Báo cáo thẩm định chi tiết được gửi lên Ban Giám hiệu trường tại các chốt kiểm soát (cuối tuần 2, tuần 12, tuần 18) để phê duyệt giải ngân ngân sách CapEx cuốn chiếu và cho phép dự án chuyển sang giai đoạn tiếp theo.
