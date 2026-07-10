# PROJECT CHARTER (WHO)

## Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS

**Trường Đại học Khoa học Tự nhiên, ĐHQG-HCM (HCMUS) — Thư viện & Phòng Công nghệ Thông tin**

Phiên bản 1.0 • Tháng 7/2026

## Mục lục

* [1. Tổng quan & Phạm vi](#1-tổng-quan--phạm-vi)
* [2. Stakeholder Analysis](#2-stakeholder-analysis)
* [3. Cơ sở Vật chất & Nguồn lực](#3-cơ-sở-vật-chất--nguồn-lực)
* [4. Ma trận Trách nhiệm (RACI)](#4-ma-trận-trách-nhiệm-raci)
* [5. Lộ trình (Roadmap)](#5-lộ-trình-roadmap)
* [6. Tiêu chí Thành công & KPI](#6-tiêu-chí-thành-công--kpi)
* [7. Phương pháp luận & Quy tắc Làm việc](#7-phương-pháp-luận--quy-tắc-làm-việc)
* [8. Chữ ký (Signatures)](#8-chữ-ký-signatures)

---

## 1. Tổng quan & Phạm vi

**Bối cảnh:** Thư viện HCMUS hiện lưu trữ lượng lớn giáo trình và tài liệu tham khảo dưới dạng sách giấy. Việc này gây ra tình trạng quá tải kho lưu trữ vật lý, rủi ro rách hỏng tài liệu do tần suất mượn đọc cao, và độc giả từ xa không thể tiếp cận. Đồng thời, các tài liệu PDF scan hiện tại chỉ là ảnh chụp tĩnh, cực kỳ khó đọc trên điện thoại di động do không responsive. Dự án xây dựng ứng dụng web **HCMUS-LDMS** tự xây dựng để tự động hóa luồng số hóa khép kín: quét sách giấy -> OCR trích xuất chữ -> biên tập hiệu chỉnh -> đóng gói thành file EPUB responsive, giúp lưu trữ, phân loại và phục vụ đọc sách trực tuyến bảo mật.

**Phạm vi (tóm tắt):** MVP gồm luồng số hóa PDF/Ảnh quét, chạy OCR Tesseract, biên tập trực tuyến, đóng gói EPUB bằng Pandoc, quản lý Category & Tag, phân quyền người dùng (RBAC), tìm kiếm toàn văn Elasticsearch và tích hợp trình xem Web EPUB Reader (Epub.js) bảo mật. Thí điểm số hóa 500 cuốn sách ngành CNTT trước khi nhân rộng toàn trường. Các tính năng AI/RAG là tùy chọn giai đoạn 3.

**Ma trận Tác nhân, Trách nhiệm và Tác động Trước - Sau (Stakeholder Responsibility & Impact Matrix):**

| Tác nhân / Vai trò | Trách nhiệm trong dự án | Tác động TRƯỚC khi có hệ thống (Before / As-is) | Tác động SAU khi có hệ thống (After / To-be) |
| :--- | :--- | :--- | :--- |
| **Ban Giám hiệu**<br>*(Sponsor)* | • Phê duyệt chủ trương đầu tư, ngân sách mua sắm máy quét sách chuyên dụng và phần cứng server.<br>• Ban hành Quy chế quản lý học liệu số nội bộ của nhà trường. | • Thiếu công cụ đo lường hiệu quả chuyển đổi số thư viện học liệu.<br>• Chịu áp lực ngân sách lớn cho việc xây dựng thêm kho vật lý chứa sách mới.<br>• Nguy cơ thất thoát nguồn tài nguyên tri thức quý giá do rách hỏng sách. | • Đạt chỉ số chuyển đổi số xuất sắc cấp ĐHQG-HCM.<br>• Tối ưu hóa hiệu quả sử dụng mặt bằng và hạ tầng CNTT sẵn có của trường.<br>• Bảo tồn vĩnh viễn học liệu số an toàn. |
| **Ban Giám đốc Thư viện**<br>*(Client - Nghiệp vụ)* | • Chủ trì xây dựng yêu cầu nghiệp vụ, cấu hình cây Danh mục (Category) và hệ thống Tag.<br>• Quản trị quy trình số hóa và tiếp nhận bàn giao hệ thống để vận hành dài hạn. | • Đau đầu giải quyết tình trạng thiếu kệ lưu trữ sách giáo trình cũ.<br>• Chi phí bảo quản vật lý sách giấy (điều hòa, diệt mối mọt) lớn.<br>• Khó khăn phục vụ mượn sách cho độc giả cơ sở Thủ Đức và người học từ xa. | • Giải phóng hơn 60% diện tích kệ sách giấy tại cơ sở Quận 5 để làm phòng tự học thông minh.<br>• Làm chủ quy trình số hóa hiện đại khép kín.<br>• Chủ động chia sẻ và kiểm soát học liệu số an toàn, đúng bản quyền. |
| **Thủ thư / Biên tập viên**<br>*(User Nghiệp vụ)* | • Thực hiện scan tài liệu giấy, tải file scan lên hệ thống.<br>• Hiệu chỉnh lỗi chính tả OCR, đóng gói EPUB, phân loại Category/Tag và cấu hình mức truy cập. | • Mất hàng trăm giờ lao động thủ công mỗi kỳ để sắp xếp sách cứng, phục vụ mượn trả và ghi sổ theo dõi.<br>• Thao tác quét sách cũ chỉ ra file PDF ảnh tĩnh thô sơ, chất lượng đọc kém.<br>• Khó kiểm soát rách hỏng trang sách của độc giả. | • Toàn bộ nghiệp vụ biên tập và xuất bản chuyển sang môi trường số trực quan.<br>• Công cụ hỗ trợ OCR tiếng Việt và đóng gói EPUB tự động giảm 85% thao tác thủ công.<br>• Công việc nhẹ nhàng hơn, tập trung vào nâng cao dịch vụ số. |
| **Trưởng phòng CNTT**<br>*(Client - Kỹ thuật / PM)* | • Điều phối nhóm kỹ thuật thiết kế kiến trúc, phát triển phần mềm custom (React, FastAPI).<br>• Cấu hình server lưu trữ MinIO, Keycloak, Elasticsearch và sao lưu tự động. | • Quản lý hạ tầng máy chủ thư viện phân tán, chắp vá, hiệu năng kém.<br>• Không kiểm soát được an toàn thông tin khi sinh viên tự ý tải file scan chia sẻ lên mạng.<br>• Rủi ro mất mát dữ liệu do thiếu hệ thống backup chuẩn. | • Quản trị hệ thống web app hiện đại, bảo mật cao thông qua Keycloak SSO và Signed URL.<br>• Hệ thống backup tự động MinIO/PostgreSQL ổn định.<br>• Tối ưu hóa hiệu năng hạ tầng máy chủ ảo của trường. |
| **Kỹ sư Kỹ thuật Phòng CNTT**<br>*(Dev & DevOps Team)* | • Lập trình Frontend React (Epub.js) và Backend FastAPI (Python).<br>• Tích hợp Tesseract OCR và Pandoc; cấu hình Elasticsearch lập chỉ mục.<br>• Thiết lập môi trường Dev/Staging/Production. | • Thường xuyên phải bảo trì các trang web cũ lỗi thời viết bằng PHP/ASP.NET khó nâng cấp.<br>• Thiếu cơ hội tiếp cận các dự án xử lý bất đồng bộ tải file nặng, OCR và công nghệ tìm kiếm toàn văn. | • Làm chủ các công nghệ hiện đại (FastAPI, React TypeScript, MinIO, Elasticsearch, Keycloak).<br>• Nhàn nhã trong khâu vận hành nhờ quy trình CI/CD và kiến trúc Modular Monolith chuẩn hóa. |
| **Giáo vụ khoa / Giảng viên**<br>*(Bên liên quan nghiệp vụ)* | • Hỗ trợ Thư viện chọn lọc danh mục giáo trình cốt lõi để ưu tiên số hóa thí điểm.<br>• Gửi liên kết sách số EPUB vào đề cương chi tiết môn học cho sinh viên. | • Khó khăn khi giới thiệu sách tham khảo cho sinh viên vì thư viện chỉ có 1-2 cuốn sách giấy độc bản.<br>• Chất lượng học tập của sinh viên giảm sút do thiếu tài liệu học tập chính thống. | • Giảng viên dễ dàng nhúng liên kết tài liệu trực tuyến vào bài giảng LMS.<br>• Bảo đảm 100% sinh viên trong lớp đều có thể tiếp cận giáo trình đồng thời. |
| **Bộ phận Pháp chế & Lưu trữ**<br>*(Tư vấn bản quyền)* | • Thẩm định quy chế số hóa sách nội bộ tuân thủ Khoản 1 Điều 25 Luật SHTT.<br>• Kiểm soát và hướng dẫn việc thiết lập các phân mức truy cập (Public/Internal/Restricted). | • Lo ngại rủi ro pháp lý cao bị kiện bản quyền khi thư viện tự ý scan sách giấy phân phối cho sinh viên.<br>• Quy trình kiểm soát bản quyền tài liệu số lỏng lẻo. | • Triệt tiêu hoàn toàn rủi ro pháp lý nhờ cơ chế phân quyền RBAC và hệ thống đọc sách web viewer bảo mật chống download.<br>• Quy chế số hóa được pháp lý hóa rõ ràng, minh bạch. |
| **Sinh viên / Độc giả**<br>*(Người sử dụng cuối)* | • Tra cứu tài liệu, lọc danh mục/tag và đọc sách EPUB trực tuyến trên cổng thông tin Web Portal. | • Tốn chi phí mua sách giáo trình giấy in đắt đỏ hoặc di chuyển xa về cơ sở Quận 5 để đọc tại chỗ.<br>• Trải nghiệm ức chế khi đọc file PDF scan chữ siêu nhỏ trên smartphone.<br>• Đề tài nghiên cứu bị gián đoạn nếu sách giấy bị người khác mượn mất. | • Đọc giáo trình miễn phí 24/7 từ xa qua Internet.<br>• Trải nghiệm đọc EPUB responsive mượt mà trên di động (co giãn chữ, đổi màu nền).<br>• Tìm kiếm thông tin tức thời dưới 3 giây phục vụ làm bài tập, nghiên cứu. |

---

## 2. Stakeholder Analysis

### Stakeholder Register

| Tên/Nhóm | Vai trò | External/Internal | Mối quan tâm chính (Vested Interest) | Power | Interest |
| --- | --- | --- | --- | --- | --- |
| Ban Giám hiệu | Sponsor | Internal | Tiến độ chuyển đổi số trường, hiệu quả chi phí CapEx | Cao | Trung bình |
| Ban GĐ Thư viện | Client (Nhiệp vụ) | Internal | Số hóa học liệu giáo trình, giải phóng kho bãi, bảo mật sách | Cao | Cao |
| Phòng CNTT | Client (Kỹ thuật) | Internal | Chất lượng phần mềm custom, bảo mật hạ tầng Keycloak/MinIO | Cao | Cao |
| Giáo vụ / Giảng viên | Bên liên quan | Internal | Sinh viên có sách học tập môn học đầy đủ | Trung bình | Cao |
| Pháp chế & Lưu trữ | Tư vấn kiểm soát | Internal | Tuân thủ Luật SHTT về giới hạn quyền tác giả số hóa sách | Cao | Trung bình |
| Sinh viên / Độc giả | User cuối | Internal | Trải nghiệm đọc EPUB responsive trên mobile mượt mà | Thấp | Cao |

### Power/Interest Grid

*   **Power cao, Interest cao (Quản lý sát sao):** Ban Giám đốc Thư viện, Phòng Công nghệ Thông tin.
*   **Power cao, Interest trung bình (Giữ hài lòng):** Ban Giám hiệu, Bộ phận Pháp chế & Lưu trữ (cần tham vấn pháp lý sớm từ Giai đoạn 0).
*   **Power trung bình/thấp, Interest cao (Giữ thông tin):** Giảng viên/Giáo vụ khoa, Sinh viên/Độc giả.

---

## 3. Cơ sở Vật chất & Nguồn lực

| Hạng mục | Nội dung chi tiết |
| --- | --- |
| **Thiết bị Scan** | 02 máy quét sách chuyên dụng dạng chữ V (Book Scanner) lắp đặt tại phòng số hóa thư viện Quận 5. |
| **Hạ tầng Kỹ thuật** | 01 máy chủ vật lý on-premise của trường cài đặt Docker Compose chạy các service: PostgreSQL 16, MinIO, Keycloak, Elasticsearch 8.x, FastAPI Backend và Web Server Nginx. |
| **Nhân sự Phát triển** | 04 kỹ sư Phòng CNTT (01 PM/SA kiêm nhiệm 50% thời gian, 02 Web Dev 50%, 01 DevOps 50%) làm việc trong 3 tháng phát triển cốt lõi. |
| **Nhân sự Số hóa & Biên tập** | 02 cán bộ thư viện phụ trách nghiệp vụ + 05 sinh viên cộng tác viên bán thời gian quét sách và chỉnh sửa lỗi văn bản OCR. |

---

## 4. Ma trận Trách nhiệm (RACI)

*   **R** (Responsible): Người thực hiện.
*   **A** (Accountable): Người chịu trách nhiệm cuối cùng.
*   **C** (Consulted): Người được tham vấn.
*   **I** (Informed): Người nhận thông tin.

| Gói công việc (WBS) | Thư viện | Phòng CNTT | Giáo vụ Khoa | Pháp chế | Ban Giám hiệu | Độc giả |
| --- | :---: | :---: | :---: | :---: | :---: | :---: |
| **WP1 — Khảo sát & Bản quyền** | **A** / R | R | C | C | I | - |
| **WP2 — Thiết lập Backend & DB** | C | **A** / R | - | - | I | - |
| **WP3 — Phát triển UI & OCR/EPUB** | C | **A** / R | - | - | I | C |
| **WP4 — Số hóa tài liệu** | **A** / R | C | C | C | I | - |
| **WP5 — Kiểm thử & Nghiệm thu** | R | **A** / R | - | - | I | C |
| **WP6 — Triển khai & Vận hành** | **A** / R | R | C | - | I | I |

---

## 5. Lộ trình (Roadmap)

Sơ đồ lộ trình chi tiết và mốc bàn giao:

![Sơ đồ lộ trình triển khai (Project Roadmap)](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/hcmus-projectmanage--lab/docs/images/project_roadmap.svg)

### Bảng thời gian chi tiết theo gói công việc (Phương án MVP cuốn chiếu):

![Biểu đồ tiến độ Gantt (Project Timeline Gantt Chart)](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/hcmus-projectmanage--lab/docs/images/project_timeline.svg)

*   **Critical Path:** Khâu **Số hóa tài liệu (WP4)** gồm quét sách và hiệu chỉnh lỗi văn bản OCR là đường găng giới hạn tiến độ bàn giao sách EPUB. Số hóa chạy song song với lập trình phần mềm để cung cấp dữ liệu thử nghiệm sớm.
*   **Mốc quan trọng (Milestones):**
    *   *Milestone 1 (Tuần 4):* Chốt Quy chế số hóa bản quyền & Thiết kế Mockup giao diện.
    *   *Milestone 2 (Tuần 12):* Hoàn thành UAT phần mềm và số hóa xong 500 cuốn giáo trình CNTT.
    *   *Milestone 3 (Tuần 16):* Go-live chính thức hệ thống HCMUS-LDMS toàn trường.

---

## 6. Tiêu chí Thành công & KPI

1.  **Tỷ lệ số hóa:** Đạt tối thiểu **90%** giáo trình tự viết của trường được đóng gói sang EPUB thành công trong vòng 12 tháng kể từ go-live.
2.  **Độ chính xác OCR:** Tỷ lệ nhận dạng từ tiếng Việt chính xác đạt **85%** trở lên trước khi biên tập viên hiệu chỉnh thủ công.
3.  **Tốc độ tra cứu:** Phản hồi kết quả tìm kiếm Elasticsearch dưới **3 giây** cho mỗi truy vấn tìm kiếm toàn văn.
4.  **Tần suất tương tác:** Đạt tối thiểu **10.000 lượt đọc sách/tháng** của sinh viên sau 6 tháng vận hành.
5.  **Bảo mật thông tin:** **0** sự cố rò rỉ file EPUB gốc từ hệ thống lưu trữ ra ngoài môi trường Internet tự do.

---

## 7. Phương pháp luận & Quy tắc Làm việc

*   **Phương pháp luận:** Áp dụng mô hình **Lai (Hybrid)** - quản lý vòng đời dự án theo mô hình gating chặt chẽ (Giai đoạn 0 đến 3) để Ban Giám hiệu kiểm soát chi phí đầu tư từng mốc lớn, kết hợp quy trình phát triển phần mềm lặp **Scrum (Sprint 2 tuần)** trong gói WP3 để đội kỹ thuật phản ứng linh hoạt với các phản hồi UAT thực tế của thủ thư và sinh viên.
*   **Quy tắc phối hợp:**
    *   Họp nhóm kỹ thuật ngắn (Daily Standup) hàng ngày trực tuyến (15 phút).
    *   Họp bàn giao Sprint (Sprint Review & Planning) cuối mỗi 2 tuần giữa Phòng CNTT và Thư viện.
    *   Báo cáo tiến độ bằng văn bản gửi Ban Giám hiệu cuối mỗi Giai đoạn để nghiệm thu chốt chuyển pha (Gating Approval).

---

## 8. Chữ ký (Signatures)

| Vai trò | Họ tên | Chữ ký | Ngày |
| --- | --- | --- | --- |
| Đại diện Ban Giám hiệu (Sponsor) | | | |
| Đại diện Thư viện (Client) | | | |
| Đại diện Phòng CNTT (Client) | | | |
| Đại diện Bộ phận Pháp chế & Lưu trữ | | | |
