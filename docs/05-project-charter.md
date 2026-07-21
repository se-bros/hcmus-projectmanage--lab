# ĐIỀU LỆ DỰ ÁN (PROJECT CHARTER)

## Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS (HCMUS-LDMS)

### THÔNG TIN TÀI LIỆU (DOCUMENT CONTROL)

| Trường thông tin (Field)                   | Nội dung đặc tả (Description)                |
| :----------------------------------------- | :------------------------------------------- |
| **Mã tài liệu (Document ID)**              | `HCMUS-LDMS-PCH`                             |
| **Tên tài liệu (Document Title)**          | Điều lệ dự án (Project Charter)              |
| **Dự án (Project Name)**                   | HCMUS-LDMS                                   |
| **Đơn vị soạn thảo (Author/Organization)** | Thư viện & Phòng Công nghệ Thông tin - HCMUS |
| **Người xem xét (Reviewer)**               | Trưởng phòng CNTT & Giám đốc Thư viện        |
| **Người phê duyệt (Approver)**             | Ban Giám hiệu Trường ĐH Khoa học Tự nhiên    |
| **Cấp độ bảo mật (Security Class)**        | Internal (Nội bộ trường)                     |
| **Trạng thái tài liệu (Status)**           | Under Review (Đang thẩm định)                |

### LỊCH SỬ PHIÊN BẢN (REVISION HISTORY)

| Phiên bản (Version) | Ngày phát hành (Date) | Mô tả thay đổi (Description of Change)                                                                                                                                                | Người thực hiện (Author) |
| :-----------------: | :-------------------: | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :----------------------: |
|         1.0         |      09/07/2026       | Khởi tạo dự thảo điều lệ dự án ban đầu (v1.0).                                                                                                                                        |      Mạch Quốc Tấn       |
|         2.0         |      14/07/2026       | Chuẩn hóa, tích hợp RACI/WBS từ Proposal, bổ sung Project Checklist.                                                                                                                  |      Mạch Quốc Tấn       |
|         3.0         |      15/07/2026       | Đồng bộ hóa với Product Backlog mới: Google OAuth 2.0 (thay Keycloak SSO), PostgreSQL FTS (thay Elasticsearch) và BackgroundTasks (thay Celery). Cập nhật KPIs và Checklist kỹ thuật. |     Nhóm phát triển      |

---

## Mục lục

- [1. Tuyên bố ủy quyền chính thức](#1-tuyên-bố-ủy-quyền-chính-thức)
- [2. Danh sách kiểm tra dự án (Project Checklist)](#2-danh-sách-kiểm-tra-dự-án-project-checklist)
- [3. Cơ cấu quản lý và Quản trị dự án (Governance)](#3-cơ-cấu-quản-lý-và-quản-trị-dự-án-governance)
- [4. Cơ sở vật chất và Tài nguyên được ủy quyền](#4-cơ-sở-vật-chất-và-tài-nguyên-được-ủy-quyền)
- [5. Phân tích các bên liên quan và Tác động (Stakeholder Analysis)](#5-phân-tích-các-bên-liên-quan-và-tác-động-stakeholder-analysis)
- [6. Ma trận trách nhiệm (RACI Matrix)](#6-ma-trận-trách-nhiệm-raci-matrix)
- [7. Cấu trúc phân rã công việc (WBS) và Tiến độ](#7-cấu-trúc-phân-rã-công-việc-wbs-và-tiến-độ)
- [8. Tiêu chí thành công và Chỉ số KPIs](#8-tiêu-chí-thành-công-và-chỉ-số-kpis)
- [9. Phương pháp luận và Quy tắc phối hợp làm việc](#9-phương-pháp-luận-và-quy-tắc-phối-hợp-làm-việc)
- [10. Các giả định, Ràng buộc và Quy chế kiểm soát thay đổi](#10-các-giả-định-ràng-buộc-và-quy-chế-kiểm-soát-thay-đổi)
- [11. Chữ ký phê duyệt (Signatures)](#11-chữ-ký-phê-duyệt-signatures)

---

## 1. Tuyên bố ủy quyền chính thức

Ban Giám hiệu Trường Đại học Khoa học Tự nhiên, ĐHQG-HCM chính thức phê duyệt thành lập dự án **Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS (HCMUS-LDMS)**. Điều lệ dự án này trao quyền chính thức cho Trưởng phòng Công nghệ Thông tin làm Quản lý Dự án (PM) đại diện nhà trường điều phối nguồn lực, mua sắm thiết bị scan chuyên dụng chữ V, sử dụng hạ tầng ảo hóa máy chủ VMware sẵn có và phối hợp chặt chẽ với Ban Giám đốc Thư viện để triển khai dự án theo đúng kế hoạch.

## 2. Danh sách kiểm tra dự án (Project Checklist)

- **Tại sao cần dự án này? (Why):** Kho tài liệu giấy tại cơ sở Quận 5 quá tải và xuống cấp vật lý; sinh viên ở cơ sở Thủ Đức khó tiếp cận; định dạng PDF scan cũ không hỗ trợ đọc responsive trên di động.
- **Những vấn đề cần giải quyết? (What):** Tự động hóa quy trình chuyển đổi sách giấy thành sách điện tử responsive; nâng cao tốc độ tra cứu và bảo mật bản quyền số tài liệu của trường.
- **Các sản phẩm bàn giao chính? (Deliverables):** Web Portal đọc sách; Admin Dashboard biên tập OCR; File EPUB 3.0 của 500 cuốn sách CNTT; hạ tầng CSDL PostgreSQL, MinIO Storage; tài liệu cẩm nang hướng dẫn sử dụng.
- **Chúng ta sẽ giải quyết vấn đề như thế nào? (How):**
  - _Khía cạnh kỹ thuật:_ Tự xây dựng phần mềm custom (React 18 + FastAPI + PostgreSQL + MinIO), xác thực qua Google OAuth 2.0 / Mock Auth, tìm kiếm qua PostgreSQL FTS, chạy OCR Tesseract cục bộ qua FastAPI BackgroundTasks kết hợp công cụ đóng gói Pandoc.
  - _Khía cạnh quản lý:_ Áp dụng mô hình Hybrid. Quản lý tiến độ tổng thể bằng Gating Checkpoints; phát triển phần mềm theo Kanban (WIP = 1 card/người), đo throughput thực tế hàng tuần để forecast tiến độ. Tuyển sinh viên làm CTV bán thời gian hiệu chỉnh OCR đổi điểm rèn luyện.
- **Khi nào hoàn thành dự án? (When):** Tổng thời gian thực hiện dự kiến là **20 tuần**; go-live phiên bản MVP cuốn chiếu tại tuần 12 phục vụ khai giảng năm học mới 2026.

## 3. Cơ cấu quản lý và Quản trị dự án (Governance)

- **Sponsor (Ban Giám hiệu trường):** Chịu trách nhiệm tối cao phê duyệt ngân sách CapEx/OpEx và ban hành quy chế hoạt động của thư viện số.
- **Client - Nghiệp vụ (Ban Giám đốc Thư viện):** Phụ trách định nghĩa yêu cầu nghiệp vụ, cây danh mục tài liệu; chịu trách nhiệm pháp lý kiểm duyệt chất lượng sách xuất bản; quản lý nhân lực quét sách và sinh viên CTV.
- **Project Manager - PM (Trưởng phòng CNTT):** Lập kế hoạch, theo dõi tiến độ đường găng, kiểm soát rủi ro, chịu trách nhiệm chất lượng kỹ thuật, điều phối nhóm phát triển.
- **Technical Lead (Kỹ sư trưởng phòng CNTT):** Thiết kế kiến trúc Modular Monolith, thiết kế CSDL PostgreSQL (lưu trữ & FTS) và chịu trách nhiệm cấu hình bảo mật Google OAuth/MinIO.
- **Nhóm phát triển phần mềm (Dev & DevOps Team):** 4 kỹ sư Phòng CNTT chịu trách nhiệm code React Frontend và FastAPI Backend, viết API và deploy Docker Compose (API, Postgres, MinIO).

## 4. Cơ sở vật chất và Tài nguyên được ủy quyền

- **Ngân sách được cấp:** Phê duyệt tổng ngân sách đầu tư một lần CapEx trị giá **75.000.000 VNĐ – 95.000.000 VNĐ** và OpEx định kỳ **15.000.000 VNĐ – 30.000.000 VNĐ / năm**.
- **Thiết bị scan:** Cấp kinh phí mua sắm 02 máy quét sách chuyên dụng dạng chữ V bảo vệ gáy sách giấy.
- **Hạ tầng máy chủ:** Phân vùng 3 máy chủ ảo hóa VMware vSphere chạy trong phòng máy chủ của trường phục vụ môi trường Dev, Staging và Production.
- **Nhân sự được huy động:** 2 cán bộ Thư viện phụ trách biên tập; 4 kỹ sư CNTT (phân bổ 50% thời gian kiêm nhiệm); 10-15 sinh viên CTV bán thời gian làm việc theo ca.

## 5. Phân tích các bên liên quan và Tác động (Stakeholder Analysis)

### 5.1. Ma trận Tác nhân và Tác động As-is vs To-be

| Vai trò / Tác nhân      | Mối quan tâm chính                                                                | Trước khi có hệ thống (As-is)                                                       | Sau khi có hệ thống (To-be)                                                                   |
| :---------------------- | :-------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------- |
| **Ban Giám hiệu**       | Đạt chỉ số chuyển đổi số trường, kiểm soát tốt CapEx.                             | Thiếu dữ liệu học liệu số báo cáo ĐHQG; tốn chi phí mở rộng kho bãi.                | Đạt chỉ tiêu chuyển đổi số giáo dục; tối ưu hóa diện tích kho Quận 5.                         |
| **Ban GĐ Thư viện**     | Nâng cao tỷ lệ tự phục vụ của sinh viên; bảo quản sách giấy; kiểm soát bản quyền. | Tốn nhiều chi phí bảo quản sách giấy; khó chia sẻ tài liệu do sợ vi phạm bản quyền. | Thu hồi 60% mặt bằng kho kệ làm phòng tự học; kiểm soát bản quyền qua Signed URL.             |
| **Thủ thư / Editor**    | Giao diện biên tập tiện lợi; giảm công sức kiểm kê, mượn trả thủ công.            | Tốn thời gian mượn trả giấy; file scan PDF ảnh tĩnh chất lượng kém, khó đọc.        | Quy trình số hóa tự động hóa 85% khâu đóng gói; sửa lỗi OCR trên giao diện chia đôi tiện lợi. |
| **Độc giả (Sinh viên)** | Trải nghiệm đọc EPUB responsive mượt mà trên mobile; tra cứu nhanh 24/7.          | Di chuyển 15km từ Thủ Đức về Quận 5; chép tay tài liệu độc bản; file PDF khó đọc.   | Đọc trực tuyến responsive 24/7 từ xa; tra cứu từ khóa qua PostgreSQL FTS dưới 3 giây.         |

### 5.2. Bản đồ Stakeholder (Power/Interest Grid)

- _Power cao, Interest cao (Quản trị sát sao):_ Ban Giám đốc Thư viện, Trưởng phòng CNTT (PM).
- _Power cao, Interest trung bình (Giữ hài lòng):_ Ban Giám hiệu (Sponsor), Bộ phận Pháp chế.
- _Power thấp, Interest cao (Thông báo đầy đủ):_ Giảng viên, Sinh viên trường.

## 6. Ma trận trách nhiệm (RACI Matrix)

- **R** (Responsible): Thực hiện. | **A** (Accountable): Phê duyệt cuối cùng. | **C** (Consulted): Tham vấn. | **I** (Informed): Nhận thông tin.

| Gói công việc WBS                  | Thư viện  | Phòng CNTT | Giáo vụ Khoa | Bộ phận Pháp chế | Ban Giám hiệu | Độc giả |
| :--------------------------------- | :-------: | :--------: | :----------: | :--------------: | :-----------: | :-----: |
| **WP1 — Khảo sát & Bản quyền**     | **A** / R |     R      |      C       |        C         |       I       |    -    |
| **WP2 — Thiết lập Backend & DB**   |     C     | **A** / R  |      -       |        -         |       I       |    -    |
| **WP3 — Phát triển UI & OCR/EPUB** |     C     | **A** / R  |      -       |        -         |       I       |    C    |
| **WP4 — Số hóa tài liệu**          | **A** / R |     C      |      C       |        C         |       I       |    -    |
| **WP5 — Kiểm thử & UAT**           |     R     | **A** / R  |      -       |        -         |       I       |    C    |
| **WP6 — Triển khai & Vận hành**    | **A** / R |     R      |      C       |        -         |       I       |    I    |

## 7. Cấu trúc phân rã công việc (WBS) và Tiến độ

Hệ thống được thiết kế triển khai trong **20 tuần** với phương án cuốn chiếu MVP:

- **WP1 — Khảo sát & Bản quyền (Tuần 1–3):** Phỏng vấn độc giả; hoàn thiện quy chế bản quyền số hóa nội bộ; thiết kế mockup UI.
- **WP2 — Cơ sở dữ liệu & Backend (Tuần 4–7):** Thiết lập hạ tầng ảo hóa VMware; cài đặt PostgreSQL, MinIO và phát triển các API CRUD, RBAC, Mock Auth.
- **WP3 — Giao diện & Trình đọc (Tuần 8–11):** Code React Frontend; tích hợp Epub.js, Tesseract OCR, Pandoc; cấu hình PostgreSQL FTS.
- **WP4 — Số hóa tài liệu (Tuần 12–17) [Đường găng - Critical Path]:** Quét sách giấy; chạy OCR background; biên tập Split-screen; đóng gói EPUB. Số hóa thí điểm 500 cuốn sách CNTT đưa vào sử dụng ở tuần 12.
- **WP5 — Kiểm thử & UAT (Tuần 18–19):** Pentest bảo mật Signed URL; nghiệm thu UAT với thủ thư và sinh viên mẫu.
- **WP6 — Triển khai & Vận hành (Tuần 20):** Triển khai production Docker Compose (API + Postgres + MinIO); đào tạo cán bộ; truyền thông ra mắt.

## 8. Tiêu chí thành công và Chỉ số KPIs

1. **Tỷ lệ học liệu số hóa:** Đạt tối thiểu **90%** số lượng giáo trình cốt lõi tự soạn của giảng viên trường được số hóa sang EPUB 3.0 responsive trong vòng 12 tháng.
2. **Hiệu năng tìm kiếm:** Thời gian phản hồi của PostgreSQL FTS dưới **3 giây** cho truy vấn tìm kiếm toàn văn ở điều kiện bình thường.
3. **Độ chính xác OCR:** Tỷ lệ nhận dạng ký tự tiếng Việt (CAR) trung bình đạt tối thiểu **85%** trước khi biên tập viên soát lỗi chính tả.
4. **An toàn bảo mật:** Hạn chế tối đa sự cố rò rỉ hoặc tải lậu file EPUB gốc ra ngoài hệ thống.
5. **Độ hài lòng người dùng:** Đạt tối thiểu **85%** sinh viên đánh giá tích cực về trải nghiệm đọc trực tuyến.

## 9. Phương pháp luận và Quy tắc phối hợp làm việc

- **Phương pháp luận quản lý:** Áp dụng mô hình **Hybrid (Lai)**. Tiến độ vĩ mô được quản lý chặt chẽ theo mô hình Gating kết thúc giai đoạn để kiểm soát ngân sách; việc phát triển phần mềm nghiệp vụ áp dụng **Kanban** (WIP = 1 card / người hoặc / agent), đo **throughput** (số story Done mỗi tuần) để forecast tiến độ thực tế, giúp linh hoạt cho nhóm kỹ sư kiêm nhiệm 50%.
- **Quy tắc phối hợp:**
  - Họp tiến độ kỹ thuật ngắn (Daily Standup) hàng ngày trực tuyến (15 phút).
  - Họp sơ kết hàng tuần (Weekly Review): đếm story Done, cập nhật throughput, forecast tuần còn lại — giữa nhóm kỹ thuật và Thư viện.
  - Họp bàn giao chốt cổng kiểm soát giai đoạn (Gating Review) gửi Ban Giám hiệu phê duyệt chuyển pha.

## 10. Các giả định, Ràng buộc và Quy chế kiểm soát thay đổi

- **Giả định:** Khoản 1 Điều 25 Luật SHTT Việt Nam cho phép thư viện trường số hóa phục vụ học tập nội bộ phi thương mại; giảng viên cam kết hỗ trợ ký consent đồng ý chia sẻ bản quyền.
- **Ràng buộc:** Tài nguyên máy chủ ảo hóa VMware bị giới hạn RAM/CPU; đội kỹ sư CNTT chỉ kiêm nhiệm 50% thời gian làm việc cho dự án.
- **Quy chế kiểm soát thay đổi (Change Control):** Mọi yêu cầu thay đổi về phạm vi hoặc ngân sách vượt quá 5% phải được làm thành tờ trình đề xuất bằng văn bản, có chữ ký xác nhận của PM (Trưởng phòng CNTT) và Giám đốc Thư viện trước khi trình Đại diện Ban Giám hiệu ký phê duyệt chính thức.

## 11. Chữ ký phê duyệt (Signatures)

| Vai trò                                    | Họ và tên | Chữ ký | Ngày ký |
| :----------------------------------------- | :-------- | :----: | :-----: |
| **Đại diện Ban Giám hiệu (Sponsor)**       |           |        |         |
| **Đại diện Thư viện (Client - Nghiệp vụ)** |           |        |         |
| **Đại diện Phòng CNTT (Project Manager)**  |           |        |         |
| **Đại diện Bộ phận Pháp chế & Lưu trữ**    |           |        |         |
