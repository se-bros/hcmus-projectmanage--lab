# KẾ HOẠCH CHI PHÍ, TIẾN ĐỘ & PHÂN BỔ NGUỒN LỰC DỰ ÁN

## Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS (HCMUS-LDMS)

### THÔNG TIN TÀI LIỆU (DOCUMENT CONTROL)

| Trường thông tin (Field) | Nội dung đặc tả (Description) |
| :--- | :--- |
| **Mã tài liệu (Document ID)** | `HCMUS-LDMS-CTR` |
| **Tên tài liệu (Document Title)** | Kế hoạch Chi phí, Tiến độ & Phân bổ Nguồn lực (Cost, Time & Resource Plan) |
| **Dự án (Project Name)** | HCMUS-LDMS |
| **Đơn vị soạn thảo (Author/Organization)** | Thư viện & Phòng Công nghệ Thông tin - HCMUS |
| **Người xem xét (Reviewer)** | Trưởng phòng CNTT & Giám đốc Thư viện |
| **Người phê duyệt (Approver)** | Ban Giám hiệu Trường ĐH Khoa học Tự nhiên |
| **Cấp độ bảo mật (Security Class)** | Internal (Nội bộ trường) |
| **Trạng thái tài liệu (Status)** | Under Review (Đang thẩm định) |

### LỊCH SỬ PHIÊN BẢN (REVISION HISTORY)

| Phiên bản (Version) | Ngày phát hành (Date) | Mô tả thay đổi (Description of Change) | Người thực hiện (Author) |
| :---: | :---: | :--- | :---: |
| 1.0 | 12/07/2026 | Khởi tạo dự thảo kế hoạch chi phí, tiến độ ban đầu (v1.0). | Mạch Quốc Tấn |
| 2.0 | 14/07/2026 | Trình bày LaTeX công thức UCP & COCOMO II, chi tiết hóa WBS và chuyển đổi VNĐ. | Mạch Quốc Tấn |
| 3.0 | 17/07/2026 | Bổ sung phần Monitoring & Reporting (mục 5): bộ chỉ số giám sát, cơ chế session logging, snapshot tiến độ tuần 1 với dữ liệu thực tế, quy chế báo cáo 3 cấp. | Mạch Quốc Tấn |

---

## Mục lục

* [1. Kế hoạch thời gian và Tiến độ thực hiện (Time & Schedule Plan)](#1-kế-hoạch-thời-gian-và-tiến-độ-thực-hiện-time--schedule-plan)
    * [1.1. Lộ trình triển khai 4 Giai đoạn](#11-lộ-trình-triển-khai-4-giai-đoạn)
    * [1.2. Phân rã gói công việc (WBS) và Đường găng (Critical Path)](#12-phân-rã-gói-công-việc-wbs-và-đường-găng-critical-path)
* [2. Phương pháp luận ước lượng nỗ lực phần mềm (Estimation)](#2-phương-pháp-luận-ước-lượng-nỗ-lực-phần-mềm-estimation)
    * [2.1. Phương pháp Điểm trường hợp sử dụng (Use Case Points - UCP)](#21-phương-pháp-điểm-trường-hợp-sử-dụng-use-case-points---ucp)
    * [2.2. Phương pháp COCOMO II (Early Design Model)](#22-phương-pháp-cocomo-ii-early-design-model)
    * [2.3. Đối chiếu và Kết luận nỗ lực thực tế](#23-đối-chiếu-và-kết-luận-nỗ-lực-thực-tế)
* [3. Dự toán chi phí và Phân bổ ngân sách dự án (Cost & Budget Plan)](#3-dự-toán-chi-phí-và-phân-bổ-ngân-sách-dự-án-cost--budget-plan)
    * [3.1. Dự toán chi phí đầu tư ban đầu (CapEx)](#31-dự-toán-chi-phí-đầu-tư-ban-đầu-capex)
    * [3.2. Dự toán chi phí vận hành định kỳ (OpEx)](#32-dự-toán-chi-phí-vận-hành-định-kỳ-opex)
* [4. Kế hoạch phân bổ nguồn lực nhân sự và Thiết bị](#4-kế-hoạch-phân-bổ-nguồn-lực-nhân-sự-và-thiết-bi)
* [5. Kế hoạch Giám sát & Báo cáo Tình trạng Dự án (Monitoring & Status Reporting)](#5-kế-hoạch-giám-sát--báo-cáo-tình-trạng-dự-án-monitoring--status-reporting)
    * [5.1. Bộ chỉ số Giám sát & Đo lường (Monitoring Metrics)](#51-bộ-chỉ-số-giám-sát--đo-lường-monitoring-metrics)
    * [5.2. Cơ chế thu thập Metrics từ AI Session (Session Logging)](#52-cơ-chế-thu-thập-metrics-từ-ai-session-session-logging)
    * [5.3. Snapshot tiến độ thực tế — Tuần 1 (16–17/07/2026)](#53-snapshot-tiến-độ-thực-tế--tuần-1-1617072026)
    * [5.4. Quy chế Báo cáo định kỳ (Status Reporting)](#54-quy-chế-báo-cáo-định-kỳ-status-reporting)

---

## 1. Kế hoạch thời gian và Tiến độ thực hiện (Time & Schedule Plan)

Dự án HCMUS-LDMS được hoạch định thực hiện trong vòng **20 tuần** (5 tháng), chia làm 4 giai đoạn lớn kết hợp kiểm soát chốt cổng (Gating Checkpoints):

### 1.1. Lộ trình triển khai 4 Giai đoạn
* **Giai đoạn 0 — Khảo sát & Bản quyền (Tuần 1–2):** Nghiên cứu pháp lý, ký cam kết đồng ý của tác giả, khảo sát thực tế sách giấy và lấy báo giá thiết bị scan.
* **Giai đoạn 1 — Xây dựng MVP & Thí điểm (Tuần 3–12):** Phát triển phần mềm, tích hợp Keycloak, MinIO, OCR, Pandoc, Elasticsearch. Số hóa thí điểm 500 cuốn sách ngành CNTT đưa vào sử dụng ở tuần 12.
* **Giai đoạn 2 — Số hóa Diện rộng (Tuần 13–18):** Bàn giao quy trình số hóa, tuyển sinh viên CTV và tiến hành số hóa hàng loạt 2.000 giáo trình cốt lõi tiếp theo của các khoa khác.
* **Giai đoạn 3 — Nghiệm thu & Chuyển giao (Tuần 19–20):** Kiểm thử nghiệm thu (UAT), pentest bảo mật, đào tạo cán bộ thư viện và go-live toàn trường.

### 1.2. Phân rã gói công việc (WBS) và Đường găng (Critical Path)
* **WP1 — Khảo sát & Bản quyền (Tuần 1–3):** Phỏng vấn độc giả; hoàn thành quy chế số hóa.
* **WP2 — Cơ sở dữ liệu & Backend (Tuần 4–7):** Cấu hình ảo hóa VMware; cài đặt PostgreSQL, MinIO, Keycloak và code API CRUD.
* **WP3 — Giao diện & Trình đọc (Tuần 8–11):** Code React UI; tích hợp Epub.js, Tesseract, Pandoc và Elasticsearch.
* **WP4 — Số hóa tài liệu (Tuần 12–17) [Đường găng - Critical Path]:** Quét sách giấy; chạy OCR; biên tập Split-screen; đóng gói EPUB. Khâu scan sách và soát sửa lỗi chính tả chiếm thời gian dài nhất và phụ thuộc lớn vào năng suất của con người. Sự chậm trễ ở WP4 sẽ trực tiếp kéo lùi ngày bàn giao dự án.
* **WP5 — Kiểm thử & UAT (Tuần 18–19):** Pentest bảo mật; nghiệm thu UAT với thủ thư và sinh viên mẫu.
* **WP6 — Triển khai & Vận hành (Tuần 20):** Triển khai Docker Compose; đào tạo cán bộ; truyền thông ra mắt.

## 2. Phương pháp luận ước lượng nỗ lực phần mềm (Estimation)

### 2.1. Phương pháp Điểm trường hợp sử dụng (Use Case Points - UCP)

#### Bước 1: Tính trọng lượng tác nhân chưa điều chỉnh (UAW - Unadjusted Actor Weight)
Hệ thống tương tác với các tác nhân sau:

* Tác nhân đơn giản (Simple - API/Hệ thống khác): Keycloak SSO API, MinIO API, Elasticsearch API. (Trọng số: 1 mỗi tác nhân).
  * **UAW_Simple** = 3 x 1 = 3

* Tác nhân phức tạp (Complex - Người dùng qua giao diện đồ họa): Độc giả (Sinh viên/Giảng viên), Biên tập viên (Thủ thư), Quản trị viên (Admin). (Trọng số: 3 mỗi tác nhân).
  * **UAW_Complex** = 3 x 3 = 9

* **Tổng UAW:**
  * **Tổng UAW** = UAW_Simple + UAW_Complex = 3 + 9 = 12

#### Bước 2: Tính trọng lượng Use Case chưa điều chỉnh (UUCW - Unadjusted Use Case Weight)
Dựa trên đặc tả 14 Use Case nghiệp vụ từ Product Backlog:

* Use Case đơn giản (Simple - <= 3 bước giao dịch, 1 bảng CSDL): Đăng nhập SSO, Phân quyền RBAC, Upload file scan, Nhập Metadata, Quản lý Category, Sinh trích dẫn. (Trọng số: 5 mỗi Use Case).
  * **UUCW_Simple** = 6 x 5 = 30

* Use Case trung bình (Average - 4 đến 7 bước giao dịch, 2+ bảng CSDL): Tự động OCR, Tùy chỉnh UI Reader, Bookmark tự động, Phân bổ Sprint. (Trọng số: 10 mỗi Use Case).
  * **UUCW_Average** = 4 x 10 = 40

* Use Case phức tạp (Complex - > 7 bước giao dịch, 3+ bảng CSDL): Biên tập Split-screen, Tìm kiếm Elasticsearch, Trình đọc EPUB bảo mật, Ghi chú & Highlight. (Trọng số: 15 mỗi Use Case).
  * **UUCW_Complex** = 4 x 15 = 60

* **Tổng UUCW:**
  * **Tổng UUCW** = UUCW_Simple + UUCW_Average + UUCW_Complex = 30 + 40 + 60 = 130

#### Bước 3: Tính Use Case Points chưa điều chỉnh (UUCP)
> **UUCP (Chưa điều chỉnh)** = UAW + UUCW = 12 + 130 = 142 points

#### Bước 4: Tính hệ số phức tạp kỹ thuật (TCF - Technical Complexity Factor)
Đánh giá 13 yếu tố kỹ thuật (T1 -> T13), mỗi yếu tố cho điểm từ 0 (không ảnh hưởng) đến 5 (ảnh hưởng lớn):

* T1 (Hệ thống phân tán): Điểm 4 x Trọng số 2.0 = 8.0
* T2 (Hiệu năng phản hồi): Điểm 4 x Trọng số 1.0 = 4.0
* T3 (Hiệu quả người dùng cuối): Điểm 4 x Trọng số 1.0 = 4.0
* T4 (Xử lý nội bộ phức tạp): Điểm 5 x Trọng số 1.0 = 5.0
* T5 (Khả năng tái sử dụng mã nguồn): Điểm 3 x Trọng số 1.0 = 3.0
* T6 (Dễ cài đặt): Điểm 4 x Trọng số 0.5 = 2.0
* T7 (Dễ sử dụng): Điểm 4 x Trọng số 0.5 = 2.0
* T8 (Khả năng chuyển đổi nền tảng): Điểm 4 x Trọng số 2.0 = 8.0
* T9 (Dễ thay đổi): Điểm 3 x Trọng số 1.0 = 3.0
* T10 (Tính đồng thời): Điểm 4 x Trọng số 1.0 = 4.0
* T11 (Mục tiêu bảo mật đặc biệt): Điểm 5 x Trọng số 1.0 = 5.0
* T12 (Truy cập trực tiếp bên thứ ba): Điểm 2 x Trọng số 1.0 = 2.0
* T13 (Yêu cầu đào tạo người dùng): Điểm 3 x Trọng số 1.0 = 3.0
* **Tổng điểm kỹ thuật (T_Factor):** 53
* **Công thức tính TCF:**
  * **TCF** = 0.6 + (0.01 x T_Factor) = 0.6 + (0.01 x 53) = 1.13

#### Bước 5: Tính hệ số phức tạp môi trường (ECF - Environment Complexity Factor)
Đánh giá 8 yếu tố môi trường (E1 -> E8), mỗi yếu tố cho điểm từ $0$ đến 5:

* E1 (Quen thuộc với mô hình dự án): Điểm 4 x Trọng số 1.5 = 6.0
* E2 (Kinh nghiệm ứng dụng): Điểm 3 x Trọng số 0.5 = 1.5
* E3 (Kinh nghiệm OOP): Điểm 4 x Trọng số 1.0 = 4.0
* E4 (Năng lực phân tích chính): Điểm 4 x Trọng số 0.5 = 2.0
* E5 (Động lực làm việc): Điểm 5 x Trọng số 1.0 = 5.0
* E6 (Yêu cầu ổn định): Điểm 4 x Trọng số 2.0 = 8.0
* E7 (Nhân sự kiêm nhiệm/bán thời gian): Điểm 4 x Trọng số -1.0 = -4.0
* E8 (Ngôn ngữ lập trình khó): Điểm 2 x Trọng số -1.0 = -2.0
* **Tổng điểm môi trường (E_Factor):** 20.5
* **Công thức tính ECF:**
  * **ECF** = 1.4 + (-0.03 x E_Factor) = 1.4 + (-0.03 x 20.5) = 0.785

#### Bước 6: Tính Use Case Points điều chỉnh (AUCP)
> **AUCP (Đã điều chỉnh)** = UUCP x TCF x ECF = 142 x 1.13 x 0.785 ≈ 126 UCP

#### Bước 7: Tính nỗ lực thực hiện (Effort)
Sử dụng Hệ số năng suất khuyến nghị $\text{PF} = 20$ người-giờ/UCP:
> **Nỗ lực (Effort)** = 126 AUCP x 20 người-giờ/UCP = 2.520 người-giờ
Quy đổi sang Người-Tháng (Person-Months - PM, với 160 giờ làm việc/tháng):
> **Số người-tháng (PM)** = 2.520 / 160 ≈ 15.75 PM
*Điều chỉnh thực tế:* Nhóm tận dụng tối đa hạ tầng API sẵn có của Keycloak, MinIO và Elasticsearch (tái sử dụng mã nguồn 40%), nỗ lực thực tế viết mới giảm xuống còn **10 PM** (tương đương **5 tháng** làm việc của đội ngũ kỹ sư).

### 2.2. Phương pháp COCOMO II (Early Design Model)

Sử dụng mô hình COCOMO II để đối chuẩn kết quả:

* **Quy mô phần mềm:** Dự kiến phát triển viết mới khoảng **8.5 KLOC** (8.500 dòng code React và FastAPI).
* **Hệ số quy mô (Scale Factors - SF):** Đánh giá 5 yếu tố quy mô (mức độ tiền lệ, độ linh hoạt, giải quyết rủi ro, sự gắn kết nhóm, độ chín công nghệ) đạt tổng điểm B = 1.05.
* **Hệ số nhân nỗ lực (Effort Multipliers - EM):** Giả định hệ số điều chỉnh nỗ lực tích hợp $\text{EAF} = 0.95$ (do tận dụng tốt container Docker và quy trình CI/CD tự động).
* **Công thức tính nỗ lực:**
  * **Nỗ lực thô (Effort)** = 2.94 x EAF x (KLOC)^B = 2.94 x 0.95 x (8.5)^1.05 ≈ 2.793 x 9.42 ≈ 26.3 PM

* *Tính toán tái sử dụng (Reuse Adjustment):* Tích hợp MinIO, Keycloak và Elasticsearch (chiếm khoảng 60% tổng khối lượng hệ thống). Khối lượng code viết mới thực tế tương đương **3.5 KLOC**.
  * **Nỗ lực phần mềm mới (Effort_New)** = 2.793 x (3.5)^1.05 ≈ 2.793 x 3.73 ≈ 10.4 PM

### 2.3. Đối chiếu và Kết luận nỗ lực thực tế
Kết quả từ hai mô hình ước lượng độc lập hoàn toàn trùng khớp:

* **UCP:** 10.0 PM.
* **COCOMO II:** 10.4 PM.
* **Quyết định chọn:** Chọn mức nỗ lực 10.5 PM làm cơ sở hoạch định nhân sự. Với nhóm phát triển gồm 4 kỹ sư kiêm nhiệm 50% thời gian (tương đương 2 kỹ sư full-time), thời gian phát triển phần mềm cốt lõi là:
  * **Thời gian thực tế** = 10.5 PM / 2 = 5.25 tháng (≈ 21 tuần)
  *Tiến độ này hoàn toàn khả thi và khớp với lộ trình 20 tuần của dự án.*

---

## 3. Dự toán chi phí và Phân bổ ngân sách dự án (Cost & Budget Plan)

### 3.1. Dự toán chi phí đầu tư ban đầu (CapEx)
Tổng chi phí CapEx dao động từ **75.000.000 VNĐ – 95.000.000 VNĐ**:

* **Số hóa dữ liệu & Biên tập EPUB:** 30.000.000 VNĐ – 40.000.000 VNĐ (thuê sinh viên CTV scan và sửa lỗi OCR cho ~10.000 cuốn sách).
* **Phát triển phần mềm:** 25.000.000 VNĐ – 35.000.000 VNĐ (chi phí nhân lực 4 kỹ sư Phòng CNTT tự phát triển).
* **Hạ tầng thiết bị:** 10.000.000 VNĐ – 12.000.000 VNĐ (02 máy scan chuyên dụng chữ V và nâng cấp cụm máy chủ ảo hóa VMware).
* **Đào tạo & Triển khai:** 5.000.000 VNĐ – 8.000.000 VNĐ (tài liệu hướng dẫn, video, tập huấn).
* **Dự phòng rủi ro phát sinh (15%):** 5.000.000 VNĐ – 10.000.000 VNĐ.

### 3.2. Dự toán chi phí vận hành định kỳ (OpEx)
Tổng chi phí OpEx hàng năm duy trì từ năm thứ 2 ước tính **15.000.000 VNĐ – 30.000.000 VNĐ / năm**:

* **Hạ tầng máy chủ ảo hóa:** 4.000.000 VNĐ – 8.000.000 VNĐ / năm (điện, mạng băng thông cao, bảo quản).
* **Bảo trì & Hỗ trợ kỹ thuật:** 6.000.000 VNĐ – 12.000.000 VNĐ / năm (vá lỗi bảo mật, nâng cấp thư viện).
* **API OCR dự phòng (Cloud OCR):** 3.000.000 VNĐ – 6.000.000 VNĐ / năm (dùng khi gặp tài liệu quá mờ).
* **Số hóa bổ sung sách mới:** 2.000.000 VNĐ – 4.000.000 VNĐ / năm.

---

## 4. Kế hoạch phân bổ nguồn lực nhân sự và Thiết bị

### 4.1. Phân bổ nhân sự (Human Resources)
* **Project Manager / Solution Architect (01 người):** Điều phối tiến độ, thiết kế kiến trúc hệ thống, quản lý rủi ro và tích hợp Keycloak.
* **Backend Developer (01 người):** Lập trình các API FastAPI, tích hợp module OCR Tesseract và đóng gói Pandoc EPUB.
* **Frontend Developer (01 người):** Lập trình UI React Portal, tích hợp trình đọc Epub.js.
* **DevOps / System Admin (01 người):** Quản trị CSDL PostgreSQL, cài đặt Elasticsearch, MinIO, Docker Compose và thiết lập CI/CD.
* **Thủ thư (02 người):** Vận hành máy scan chữ V, kiểm duyệt chất lượng sách xuất bản.
* **Sinh viên CTV (10-15 người):** Sửa lỗi chính tả OCR thô trực tuyến trên màn hình Split-screen.

### 4.2. Phân bổ thiết bị & Server ảo hóa
* **Thiết bị scan:** 02 máy quét sách chữ V lắp đặt tại phòng số hóa thư viện.
* **Phân vùng máy chủ ảo hóa VMware:**
  * `VM-Dev:` 4 vCPU, 8 GB RAM, 100 GB SSD (môi trường lập trình).
  * `VM-Staging:` 4 vCPU, 16 GB RAM, 200 GB SSD (môi trường kiểm thử và UAT).
  * `VM-Production:` 8 vCPU, 32 GB RAM, 2 TB HDD + 500 GB SSD (vận hành chính thức, chứa tệp EPUB và Elasticsearch).

## 5. Kế hoạch Giám sát & Báo cáo Tình trạng Dự án (Monitoring & Status Reporting)

Để quản lý tiến độ và kiểm soát chi phí phát triển với sự hỗ trợ của AI Coding Assistants, dự án thiết lập hệ thống giám sát định kỳ dựa trên dữ liệu thực tế được ghi nhận tại file [`project_log.md`](../project_log.md).

### 5.1. Bộ chỉ số Giám sát & Đo lường (Monitoring Metrics)

#### A. Chỉ số tiến độ phát triển (Development Progress)

| Chỉ số | Cách đo | Mục tiêu |
| :--- | :--- | :--- |
| **Throughput (T)** | Số User Story **đã deploy và đáp ứng Acceptance Criteria** trong 1 tuần. Dùng để dự báo: Thời gian còn lại ≈ N (stories chưa Done) / T. | Đo cuối mỗi tuần; dùng khoảng (optimistic–pessimistic) vì độ khó stories không đều. |
| **Cycle Time** | Thời gian từ lúc kéo card vào *In Progress* đến khi card `Done`. | ≤ 2 ngày (size S), ≤ 3 ngày (size M). |
| **Forecast còn lại** | Dev weeks ≈ N (story còn lại) / T. | Cập nhật mỗi cuối tuần trong báo cáo Weekly Review. |
| **Tỷ lệ hoàn thành Backlog** | Số stories Done / Tổng 26 stories × 100%. | 100% Must-have hoàn thành trước tuần 12. |

#### B. Chỉ số chi phí AI & Hiệu suất (AI Cost & Productivity)

| Chỉ số | Cách đo | Mục tiêu |
| :--- | :--- | :--- |
| **Token AI tiêu thụ** | Tổng token sử dụng mỗi phiên làm việc (ghi vào `project_log.md`). | ≤ 300K tokens/session trung bình. |
| **Chi phí AI tích lũy** | Quy đổi token ra VNĐ theo bảng giá API từng model, cộng dồn theo tuần. | Tổng ≤ 5.000.000 VNĐ (hạn mức CapEx). |
| **AI Productivity Factor** | Số stories Done / Tổng token AI đã dùng (hiệu suất sử dụng AI). | Theo dõi xu hướng để phát hiện lãng phí token. |

#### C. Chỉ số rủi ro kỹ thuật (Technical Risk Indicators)

| Chỉ số | Nguồn dữ liệu | Ngưỡng cảnh báo |
| :--- | :--- | :--- |
| **Kết quả PoC 1 (OCR chạy nền)** | Kết quả kiểm chứng tích hợp Tesseract + BackgroundTasks. | OCR timeout > 60s hoặc block Event Loop → escalate. |
| **Kết quả PoC 2 (Liên thông E2E)** | Kết quả kiểm chứng luồng React → FastAPI → PostgreSQL → MinIO → Epub.js. | Bất kỳ lớp nào trong chuỗi không kết nối được → escalate. |
| **Tỷ lệ nhận dạng OCR** | Đo thủ công trên mẫu 10 trang sách in rõ nét. | < 85% → cần tiền xử lý ảnh hoặc đổi model OCR. |

---

### 5.2. Cơ chế thu thập Metrics từ AI Session (Session Logging)

Sau mỗi phiên làm việc với AI Coding Assistant (Claude Code, Copilot, v.v.), thành viên nhóm **bắt buộc** ghi nhận một dòng log vào file [`project_log.md`](../project_log.md) theo định dạng:

| Trường | Mô tả | Ví dụ |
| :--- | :--- | :--- |
| Ngày hoàn thành | Ngày kết thúc session. | `2026-07-16` |
| Dev | Tên thành viên thực hiện. | `Khoa Nguyễn` |
| Story ID | Mã các stories hoàn thành trong session. | `LDMS-008/026` |
| Tên Story | Mô tả ngắn gọn công việc đã làm. | `Reader/Search placeholder` |
| Thời gian làm | Tổng thời gian thực tế (giờ hoặc phút). | `2h` |
| Token AI đã dùng | Số token AI tiêu thụ trong session (lấy từ dashboard API hoặc ước tính từ giao diện chat). | `40.000` |
| Ghi chú | Model AI sử dụng và ghi chú đặc biệt. | `Claude Sonnet 5 (spec) + Opus 4.8 (impl)` |

PM tổng hợp dữ liệu từ file `project_log.md` mỗi cuối tuần để tính toán các chỉ số Monitoring ở mục 5.1.

---

### 5.3. Snapshot tiến độ thực tế — Tuần 1 (16–17/07/2026)

Dưới đây là dữ liệu thực tế thu thập được từ 2 ngày phát triển đầu tiên của nhóm:

#### Bảng tổng hợp tiến độ:

| Hạng mục | Giá trị thực tế | Ghi chú |
| :--- | ---: | :--- |
| Stories hoàn thành (Done) | **12 / 26** | LDMS-001, 003, 004, 007, 008, 009, 010, 013, 018, 022, 026 và Reader/Search placeholder. |
| Tỷ lệ hoàn thành Backlog | **46%** | Gần một nửa backlog trong 2 ngày đầu. |
| Tổng thời gian dev thực tế | **4 giờ 05 phút** | 4 phiên làm việc của 4 dev (Thái và Khoa Ngô ghi chung 1 dòng log). |
| Tổng token AI đã dùng | **440.000 tokens** | Hỗn hợp Claude Sonnet 5 + Claude Opus 4.8 + Claude Code. |
| Throughput tuần 1 (T) | **12 stories / tuần** | Tuần đầu thường nhanh hơn do stories nền tảng (Platform, Identity) có độ phức tạp thấp. |

#### Dự báo tiến độ (Velocity-based Forecast):

Phương pháp: Đếm số stories **đã deploy & đáp ứng Acceptance Criteria** trong 1 tuần (= Throughput T), rồi ước lượng thời gian còn lại = N (stories chưa Done) / T. Vì các stories có độ khó khác nhau, kết quả được trình bày dưới dạng **khoảng thời gian (optimistic – pessimistic)** thay vì một con số chính xác.

* **Stories còn lại:** 26 − 12 = **14 stories** (4 Must, 7 Should, 3 Could).
* **Throughput đo được (T):** 12 stories/tuần.
* **Điều chỉnh T cho stories còn lại:**
  * *Optimistic (T = 8 stories/tuần):* Stories còn lại có một số size S/M quen thuộc, giảm nhẹ so với tuần 1.
  * *Pessimistic (T = 4 stories/tuần):* Bao gồm các stories phức tạp (Biên tập Split-screen, Trình đọc EPUB bảo mật, OCR pipeline) cần nhiều thời gian hơn.
* **Thời gian dự kiến hoàn thành:**
  * *Optimistic:* 14 / 8 ≈ **1.8 tuần** → hoàn thành tuần 3.
  * *Pessimistic:* 14 / 4 ≈ **3.5 tuần** → hoàn thành tuần 5.
  * **Khoảng ước lượng: 2–4 tuần** (dự kiến hoàn thành toàn bộ Must-have trước tuần 4, Could-have trước tuần 5).

#### Phân tích chi phí AI thực tế:

| Hạng mục | Giá trị |
| :--- | ---: |
| Token đã dùng (tuần 1) | 440.000 tokens |
| Chi phí ước tính tuần 1 (hỗn hợp model) | ~300.000 VNĐ |
| Hạn mức CapEx AI Tools | 5.000.000 VNĐ |
| Tỷ lệ tiêu thụ ngân sách | **~6%** |
| Dự báo chi phí AI tổng dự án (ngoại suy) | ~1.200.000 VNĐ |

> **Nhận xét:** Tốc độ tiêu thụ ngân sách AI rất thấp (6% hạn mức sau tuần 1). Ngân sách dư có thể được điều chuyển sang mục Cloud OCR dự phòng hoặc thuê thêm AI model chất lượng cao cho các stories phức tạp còn lại.

---

### 5.4. Quy chế Báo cáo định kỳ (Status Reporting)

#### A. Báo cáo Session (Sau mỗi phiên AI)

Ngay sau khi kết thúc một phiên làm việc với AI Coding Assistant, dev ghi nhận vào `project_log.md`:
* Nội dung đã hoàn thành (Story IDs).
* Token AI đã dùng trong phiên.
* Thời gian thực tế đã bỏ ra.
* Model AI sử dụng (để PM phân tích hiệu quả từng model).

#### B. Báo cáo Weekly Review (Mỗi tuần)

PM tổng hợp từ `project_log.md` và gửi báo cáo cho Ban Giám đốc Thư viện và Trưởng phòng CNTT, gồm:
* Throughput tuần (số stories Done) và Cycle Time trung bình.
* Tổng chi phí AI tích lũy so với hạn mức CapEx.
* Forecast thời gian hoàn thành dự kiến.
* Các rủi ro phát sinh và biện pháp giảm thiểu.

#### C. Báo cáo Chốt cổng Giai đoạn (Phase-Gating Report)

Báo cáo thẩm định chi tiết gửi lên Ban Giám hiệu trường tại các chốt kiểm soát (cuối tuần 2, tuần 12, tuần 18) để phê duyệt giải ngân ngân sách CapEx cuốn chiếu và cho phép dự án chuyển sang giai đoạn tiếp theo.

