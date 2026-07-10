# PROJECT CHARTER (WHO)

## Hệ thống Quản lý Số hóa Thư viện (LibDMS)

**Thư viện hiện đại & Ban Công nghệ Thông tin**

Phiên bản 1.0 • Tháng 7/2026

## Mục lục

* [1. Tổng quan & Phạm vi](#1-tổng-quan--phạm-vi)
* [2. Stakeholder Analysis](#2-stakeholder-analysis)
* [3. Cơ sở Vật chất & Nguồn lực](#3-cơ-sở-vật-chất--nguồn-lực)
* [4. Ma trận Trách nhiệm (RACI)](#4-ma-trận-trách-nhiệm-raci)
* [5. Lộ trình (Roadmap)](#5-lộ-trình-roadmap)
* [6. Tiêu chí Thành công & KPI](#6-tiêu-chí-thành-công--kpi)
* [7. Phương pháp luận & Quy tắc Làm việc](#7-phương-pháp-luận--quy-tắc-làm-việc)

---

## 1. Tổng quan & Phạm vi

**Bối cảnh:** Thư viện truyền thống lưu giữ hàng ngàn tài liệu giấy đang đối mặt với nguy cơ ẩm mốc, rách hỏng và quá tải diện tích lưu kho. Quy trình quản lý mượn/trả thủ công tốn nhiều nhân lực, đồng thời bạn đọc gặp khó khăn khi tiếp cận tài liệu từ xa. Dự án phát triển **Hệ thống Quản lý Số hóa Thư viện (LibDMS)** nhằm tự động hóa quy trình chuyển đổi tài liệu thô (ảnh scan, PDF) sang định dạng EPUB, giúp bạn đọc tra cứu toàn văn tốc độ cao và đọc trực tuyến bảo mật trên mọi thiết bị di động (chi tiết đầy đủ tại [02-project-proposal.md](file:///d:/Project/hcmus-projectmanage--lab/docs/02-project-proposal.md) và [03-vision-and-scope.md](file:///d:/Project/hcmus-projectmanage--lab/docs/03-vision-and-scope.md)).

**Phạm vi (Tóm tắt):** Hệ thống được xây dựng trên **Custom Modern Stack (Next.js + FastAPI)** chạy containerized trên hạ tầng Cloud (AWS/Azure). 
*   *Tính năng lõi:* Đăng ký/đăng nhập, phân quyền RBAC, pipeline số hóa tự động OCR (Tesseract) sang EPUB, quản lý phân loại Category & Tag linh hoạt, tìm kiếm toàn văn Elasticsearch nâng cao.
*   *Tính năng bổ sung:* Module mượn/trả sách giấy và đăng ký đọc sách số, trình đọc EPUB Reader online trên giao diện web, dashboard thống kê báo cáo biểu đồ trực quan, và **Chatbot tra cứu tài liệu thông minh (RAG Chatbot)**.

**Ma trận Tác nhân, Trách nhiệm và Tác động Trước - Sau (Stakeholder Responsibility & Impact Matrix):**

| Tác nhân / Vai trò | Trách nhiệm trong dự án | Tác động TRƯỚC khi có hệ thống (Before / As-is) | Tác động SAU khi có hệ thống (After / To-be) |
| :--- | :--- | :--- | :--- |
| **Ban quản lý Thư viện**<br>*(Sponsor)* | • Phê duyệt chủ trương, cấp ngân sách dự án.<br>• Phê duyệt nghiệm thu go-live hệ thống. | • Không có số liệu thống kê để tối ưu chi phí mua sắm sách giấy.<br>• Đau đầu vì diện tích kho kệ vật lý ngày càng chật chội. | • Quản trị thư viện hiện đại bằng số liệu biểu đồ trực quan.<br>• Thu hồi diện tích kho bãi vật lý làm không gian sinh hoạt chung. |
| **Thủ thư trưởng**<br>*(Business Lead)* | • Đặc tả quy trình mượn/trả sách, mô hình phân loại danh mục, tags.<br>• Kiểm tra và phê duyệt chất lượng metadata tài liệu số hóa. | • Tốn nhiều thời gian kiểm kê, đối chiếu sổ sách mượn/trả thủ công.<br>• Khó khăn trong việc phát hiện sách mượn quá hạn hoặc thất thoát sách. | • Quản lý tập trung mọi tài liệu số và vật lý trên một giao diện.<br>• Hệ thống tự động theo dõi, nhắc hạn mượn và xuất báo cáo tự động. |
| **Project Manager**<br>*(PM)* | • Quản lý tiến độ, điều phối nguồn lực phát triển.<br>• Quản trị rủi ro dự án. | • Gặp khó khăn khi quản lý các nhóm nghiệp vụ thư viện và kỹ thuật tách rời. | • Quản lý dự án khoa học qua các mốc bàn giao (milestones) rõ ràng. |
| **Technical Team**<br>*(Dev & DevOps)* | • Lập trình Frontend Next.js và Backend FastAPI.<br>• Thiết lập hạ tầng Cloud AWS/Azure (Kubernetes, S3, PostgreSQL).<br>• Cấu hình Docker container cho Tesseract OCR và Elasticsearch. | • Thường xuyên phải sửa chữa các ứng dụng thư viện cũ, khó bảo trì.<br>• Thiếu công cụ số hóa tự động khép kín. | • Làm chủ công nghệ hiện đại, tự động hóa build/deploy qua CI/CD.<br>• Hệ thống chạy ổn định, dễ dàng nâng cấp bảo trì. |
| **Bạn đọc**<br>*(End User)* | • Tra cứu tài liệu, mượn/trả và đọc trực tuyến. | • Phải di chuyển trực tiếp đến thư viện, đọc bản giấy cũ nát tại phòng đọc và chép tay thủ công. | • Tra cứu toàn văn nhanh chóng, đọc sách online 24/7 từ xa qua trình đọc EPUB linh hoạt trên di động. |

---

## 2. Stakeholder Analysis

### Stakeholder Register

| Tên/Nhóm | Vai trò | External/Internal | Mối quan tâm chính (Vested Interest) | Power | Interest |
| --- | --- | --- | --- | --- | --- |
| Ban quản lý Thư viện | Sponsor | Internal | Hiệu suất đầu tư ngân sách, nâng cao chất lượng phục vụ | Cao | Trung bình |
| Thủ thư trưởng | Business Lead | Internal | Tối ưu hóa quy trình mượn/trả, độ chính xác OCR | Cao | Cao |
| Project Manager | PM | Internal | Hoàn thành dự án đúng hạn, đúng ngân sách | Cao | Cao |
| Technical Team | Devs & DevOps | Internal | Kiến trúc hệ thống ổn định, bảo mật tệp tin S3 | Cao | Cao |
| Cán bộ thư viện | Operator | Internal | Giao diện số hóa dễ dùng, giảm thiểu thao tác thủ công | Trung bình | Cao |
| Bạn đọc | End User | External | Trải nghiệm EPUB Reader tốt, tìm kiếm chính xác | Thấp | Cao |

### Power/Interest Grid

*   **Power cao / Interest cao:** Thủ thư trưởng, Technical Team, PM — **Quản lý sát sao** (Nhân sự nòng cốt thực thi dự án).
*   **Power cao / Interest thấp:** Ban quản lý Thư viện — **Giữ hài lòng** (Cần báo cáo tiến độ theo mốc giai đoạn để duy trì ngân sách).
*   **Power thấp / Interest cao:** Cán bộ thư viện, Bạn đọc — **Giữ thông tin** (Cung cấp tài liệu hướng dẫn và tập huấn sớm để tăng mức độ chấp nhận hệ thống).

---

## 3. Cơ sở Vật chất & Nguồn lực

*   **Hạ tầng kỹ thuật:** Tài khoản AWS/Azure của thư viện phục vụ triển khai môi trường Development, Staging và Production.
*   **Thiết bị chạy thử:** Máy scan tài liệu vật lý sẵn có tại thư viện để cung cấp ảnh quét mẫu cho nhóm kỹ thuật kiểm thử OCR.
*   **Nhân sự dự án:**
    *   *01 Project Manager:* Điều phối chung (30% time).
    *   *02 Lập trình viên Backend & OCR specialist:* Xây dựng API FastAPI, Tesseract OCR pipeline, Calibre EPUB converter (100% time).
    *   *01 Lập trình viên Frontend:* Xây dựng Next.js portal và EPUB Reader (100% time).
    *   *01 DevOps Engineer:* Cấu hình AWS/Azure, Docker, CI/CD và Elasticsearch (50% time).
    *   *02 Cán bộ thư viện:* Hỗ trợ khảo sát dữ liệu và kiểm thử UAT nghiệp vụ.

---

## 4. Ma trận Trách nhiệm (RACI)

*   **R** (Responsible): Người thực hiện công việc.
*   **A** (Accountable): Người chịu trách nhiệm cuối cùng.
*   **C** (Consulted): Người được tham vấn ý kiến.
*   **I** (Informed): Người nhận thông tin kết quả.

| Gói công việc (WBS) | Sponsor | PM | Thủ thư trưởng | Technical Team | Cán bộ thư viện | Bạn đọc |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **WP1 — Khảo sát & Thiết kế** | I | **A** | R | R | C | - |
| **WP2 — Hạ tầng Cloud & Core API** | I | C | - | **A** / R | - | - |
| **WP3 — Giao diện & Pipeline** | I | R | C | **A** / R | C | I |
| **WP4 — OCR & EPUB Generator** | I | C | - | **A** / R | - | - |
| **WP5 — Nghiệp vụ mượn/trả & Reader**| I | R | **A** / R | R | R | I |
| **WP6 — Kiểm thử, Triển khai Cloud** | I | C | C | **A** / R | R | C |

---

## 5. Lộ trình (Roadmap)

Dự án kéo dài **7 tháng** theo lộ trình Gantt chi tiết dưới đây:

![Biểu đồ tiến độ Gantt (Project Timeline Gantt Chart)](file:///d:/Project/hcmus-projectmanage--lab/docs/images/project_timeline.svg)

*   **Tháng 1 (Mốc M1 - Khảo sát thiết kế xong):** Hoàn thành tài liệu đặc tả nghiệp vụ, chốt thiết kế kiến trúc PostgreSQL database và mô hình phân loại danh mục/tag mẫu.
*   **Tháng 2 - 3 (Mốc M2 - Hoàn thành Core API & Portal):** Thiết lập môi trường AWS/Azure dev, viết xong Core API FastAPI (Authentication, Users, RBAC) và khung portal Next.js.
*   **Tháng 4 (Mốc M3 - Go-live MVP thí điểm):** Hoàn thành tích hợp Tesseract OCR tiếng Việt và Calibre converter. Import thử nghiệm 1.000 tài liệu mẫu.
*   **Tháng 5 - 6 (Mốc M4 - Hoàn thành tính năng nâng cao):** Tích hợp trình đọc trực tuyến EPUB Reader, module mượn/trả sách giấy, chatbot tra cứu tài liệu thông minh (RAG Chatbot) và dashboard thống kê biểu đồ.
*   **Tháng 7 (Mốc M5 - Go-live chính thức):** Hoàn thành kiểm thử UAT, cấu hình Auto-scaling trên Cloud, hoàn thành Pen-test và go-live Production chính thức.

---

## 6. Tiêu chí Thành công & KPI

1.  **KPI Số hóa:** Hoàn thành số hóa và chuyển đổi sang EPUB thành công cho tối thiểu **95%** lượng tài liệu thuộc danh mục ưu tiên trong 3 tháng đầu vận hành chính thức.
2.  **KPI Tra cứu:** Đảm bảo thời gian phản hồi tìm kiếm toàn văn luôn dưới **2 giây** với cơ sở dữ liệu lớn.
3.  **KPI Mượn/Trả:** Tự động gửi email/SMS nhắc hạn trả sách giấy với tỷ lệ chính xác **100%**.
4.  **KPI Bảo mật:** Đạt chứng nhận Pen-test bảo mật, **0** vụ việc rò rỉ nguyên file EPUB gốc từ S3 ra ngoài.
5.  **KPI Uptime:** Tính sẵn sàng của portal trực tuyến đạt tối thiểu **99.9%** (Uptime SLA).

---

## 7. Phương pháp luận & Quy tắc Làm việc

*   **Phương pháp luận:** Áp dụng mô hình **Lai (Hybrid)**:
    *   *Cấp vĩ mô (Roadmap):* Gating nghiêm ngặt qua 4 giai đoạn (Phase 0 -> Phase 3). Cuối mỗi Phase phải có cuộc họp nghiệm thu báo cáo khả thi/kết quả (Gate Review) với Sponsor để thông qua quyết định cấp ngân sách cho Phase tiếp theo.
    *   *Cấp vi mô (Phát triển kỹ thuật):* Sử dụng **Agile/Scrum** với chu kỳ sprint 2 tuần cho Technical Team để liên tục cập nhật và kiểm thử các tính năng mới dựa trên phản hồi của thủ thư.
*   **Quy tắc làm việc:**
    *   Họp Daily stand-up 15 phút (Tech team) để tháo gỡ nút thắt kỹ thuật.
    *   Họp Sprint Review & Planning cuối mỗi 2 tuần (PM, Tech Team, Thủ thư trưởng) để demo tính năng mới và lên kế hoạch sprint tiếp theo.
    *   Báo cáo trạng thái dự án gửi Sponsor định kỳ hàng tháng.
