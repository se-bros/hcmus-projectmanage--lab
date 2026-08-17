# PHÁT BIỂU CÔNG VIỆC (STATEMENT OF WORK — SOW)

## Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS (HCMUS-LDMS)

### THÔNG TIN TÀI LIỆU (DOCUMENT CONTROL)

| Trường thông tin (Field)                   | Nội dung đặc tả (Description)             |
| :----------------------------------------- | :---------------------------------------- |
| **Mã tài liệu (Document ID)**              | `HCMUS-LDMS-SOW`                          |
| **Tên tài liệu (Document Title)**          | Phát biểu Công việc (Statement of Work)   |
| **Dự án (Project Name)**                   | HCMUS-LDMS                                |
| **Đơn vị soạn thảo (Author/Organization)** | Nhóm Phát triển Dự án HCMUS-LDMS          |
| **Người xem xét (Reviewer)**               | Trưởng phòng CNTT & Giám đốc Thư viện     |
| **Người phê duyệt (Approver)**             | Ban Giám hiệu Trường ĐH Khoa học Tự nhiên |
| **Cấp độ bảo mật (Security Class)**        | Internal (Nội bộ trường)                  |
| **Trạng thái tài liệu (Status)**           | Pending Approval (Chờ phê duyệt)          |

### LỊCH SỬ PHIÊN BẢN (REVISION HISTORY)

| Phiên bản (Version) | Ngày phát hành (Date) | Mô tả thay đổi (Description of Change)                                                                                                | Người thực hiện (Author) |
| :-----------------: | :-------------------: | :------------------------------------------------------------------------------------------------------------------------------------ | :----------------------: |
|         1.0         |      24/07/2026       | Khởi tạo tài liệu SOW chính thức, phản ánh tech stack đơn giản hóa (Google OAuth 2.0, PostgreSQL FTS, BackgroundTasks) và vai trò AI. |    Ân Tiến Nguyên An     |

---

## Mục lục



---

## 1. Mục đích và Ý nghĩa tài liệu

Tài liệu **Phát biểu Công việc (Statement of Work — SOW)** là văn bản pháp lý đánh dấu sự kết thúc của giai đoạn **Project Planning** trong vòng đời dự án HCMUS-LDMS. Khi SOW được ký duyệt bởi tất cả các bên liên quan, dự án chính thức chuyển sang giai đoạn **Project Execution**.

SOW ghi nhận sự đồng thuận cuối cùng giữa **Bên yêu cầu** (Client — Ban Giám đốc Thư viện và Ban Giám hiệu) và **Bên thực hiện** (Nhóm phát triển — Phòng CNTT / Nhóm sinh viên) về:

- **Phạm vi công việc** cụ thể sẽ được thực hiện và các hạng mục loại trừ.
- **Ngăn xếp công nghệ** đã thống nhất sau quá trình đơn giản hóa.
- **Thời gian**, **chi phí** và **nguồn lực** được cam kết phân bổ.
- **Quy chế kiểm soát thay đổi** khi phạm vi dự án bị điều chỉnh.
- **Vai trò của AI Coding Assistants** trong quy trình phát triển phần mềm.

> **Lưu ý quan trọng:** Mọi thay đổi về phạm vi (scope) sau khi SOW được ký duyệt sẽ kéo theo thay đổi liên động về tính năng (features), ngăn xếp công nghệ (tech stack), thời gian (timeline) và chi phí (cost). Các thay đổi này bắt buộc phải được xử lý qua Quy chế Kiểm soát Thay đổi (mục 10).

---

## 2. Các bên tham gia Hợp đồng

| Vai trò                                        | Đơn vị / Cá nhân đại diện                        | Trách nhiệm trong SOW                                                                          |
| :--------------------------------------------- | :----------------------------------------------- | :--------------------------------------------------------------------------------------------- |
| **Bên A — Nhà tài trợ (Sponsor)**              | Ban Giám hiệu Trường ĐH Khoa học Tự nhiên        | Phê duyệt chủ trương, cấp ngân sách CapEx/OpEx và ký duyệt SOW.                                |
| **Bên B — Chủ trì nghiệp vụ (Client)**         | Ban Giám đốc Thư viện HCMUS                      | Xác nhận yêu cầu nghiệp vụ, phạm vi tài liệu số hóa và nghiệm thu sản phẩm bàn giao.           |
| **Bên C — Nhóm phát triển (Development Team)** | Phòng Công nghệ Thông tin / Nhóm sinh viên dự án | Thực hiện phát triển phần mềm, triển khai hệ thống và bàn giao sản phẩm theo đúng cam kết SOW. |
| **Cố vấn Pháp lý**                             | Bộ phận Pháp chế & Lưu trữ của trường            | Thẩm định quy chế bản quyền số hóa nội bộ, đảm bảo tuân thủ Luật Sở hữu trí tuệ Việt Nam.      |

---

## 3. Phạm vi công việc (Scope of Work)

### 3.1. Phạm vi bao gồm (In-Scope)

Nhóm phát triển cam kết thực hiện các hạng mục công việc sau trong phạm vi SOW này:

**A. Phát triển phần mềm hệ thống HCMUS-LDMS:**

| #   | Nhóm tính năng                             | Mô tả chi tiết                                                                                                                  | Backlog tham chiếu           |
| --- | :----------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------ | :--------------------------- |
| 1   | **Nền tảng & Hạ tầng (Platform)**          | Monorepo + Docker Compose (3 services: API + PostgreSQL + MinIO), health check endpoint, `.env.example`.                        | LDMS-001                     |
| 2   | **Xác thực & Phân quyền (Identity)**       | Mock JWT + roles (dev), Google OAuth 2.0 (`@hcmus.edu.vn`), RBAC kiểm soát quyền truy cập tài liệu (`is_public`).               | LDMS-009, 010, 018           |
| 3   | **Tải lên & Quản lý tài liệu (Documents)** | Upload PDF/ảnh scan lên MinIO, danh sách tài liệu (Document List UI), trạng thái vòng đời tài liệu.                             | LDMS-002, 026                |
| 4   | **OCR tự động (Digitization)**             | Hàng đợi OCR bất đồng bộ qua FastAPI BackgroundTasks, Tesseract OCR tiếng Việt, kết quả theo từng trang, UI trạng thái + retry. | LDMS-003, 004, 022           |
| 5   | **Biên tập nội dung (Editor)**             | API đọc/cập nhật text trang, UI biên tập tối thiểu, giao diện Split-screen (ảnh gốc + text OCR).                                | LDMS-005, 006, 017           |
| 6   | **Metadata & Phân loại (Cataloging)**      | Gán siêu dữ liệu bắt buộc (title, author), Category 2 cấp, Tags tùy chọn, chặn xuất bản khi thiếu metadata.                     | LDMS-011, 012, 013, 023      |
| 7   | **Đóng gói & Xuất bản EPUB (Publishing)**  | Biên dịch Pandoc sang EPUB 3.0 reflowable, lưu trữ MinIO, cập nhật PostgreSQL FTS.                                              | LDMS-007                     |
| 8   | **Tra cứu toàn văn (Search)**              | PostgreSQL Full-Text Search (`tsvector`/`tsquery` + GIN index), snippet kết quả, liên kết mở reader.                            | LDMS-015, 016                |
| 9   | **Trình đọc sách (Reader)**                | Epub.js Web Reader bảo mật, MinIO Signed URL 15 phút (DRM), tùy chỉnh font/nền, bookmark vị trí đọc, highlight & ghi chú.       | LDMS-008, 014, 019, 020, 021 |
| 10  | **Trích dẫn & Nâng cao**                   | Citation tự động APA/IEEE, Elasticsearch nâng cao (nếu còn thời gian).                                                          | LDMS-024, 025                |

**Tổng cộng: 26 User Stories** — 16 Must-have · 7 Should-have · 3 Could-have (theo thang MoSCoW).

**B. Số hóa tài liệu thí điểm:**

- Số hóa thí điểm **500 cuốn giáo trình CNTT** sang EPUB 3.0 trong giai đoạn MVP.

**C. Tài liệu và Đào tạo:**

- Bộ tài liệu thiết kế kiến trúc, API Swagger tự động.
- Cẩm nang hướng dẫn sử dụng cho thủ thư và độc giả.
- Tổ chức tối thiểu 02 buổi tập huấn vận hành.

### 3.2. Phạm vi loại trừ (Out-of-Scope)

Các hạng mục sau **không nằm** trong phạm vi cam kết của SOW này:

- Tích hợp hệ thống chống đạo văn (Turnitin hoặc tương đương).
- Số hóa hồ sơ hành chính, học bạ, tài liệu nhân sự của trường.
- Phát triển ứng dụng di động native (iOS/Android).
- Tính năng tìm kiếm AI/RAG (trí tuệ nhân tạo ngữ nghĩa) — hoãn sang giai đoạn sau.
- Thanh lý hoặc vận chuyển sách giấy cũ ra khỏi thư viện.
- Mua sắm bản quyền phần mềm thương mại (Adobe, ABBYY).

---

## 4. Ngăn xếp công nghệ thống nhất (Agreed Technology Stack)

### 4.1. Tech Stack chính thức (MVP)

Sau quá trình đánh giá tính khả thi và đơn giản hóa tech stack (ghi nhận tại commit `1d76700e`), các bên thống nhất sử dụng ngăn xếp công nghệ sau cho phiên bản MVP:

| Thành phần          | Công nghệ thống nhất          | Thay thế cho (trước đó) | Lý do thay đổi                                                                           |
| :------------------ | :---------------------------- | :---------------------- | :--------------------------------------------------------------------------------------- |
| **Xác thực (MVP)**  | Google OAuth 2.0 / Mock Auth  | Keycloak SSO            | Sinh viên/GV đã có Gmail HCMUS; không cần self-host server xác thực riêng.               |
| **Tìm kiếm (MVP)**  | PostgreSQL Full-Text Search   | Elasticsearch           | Tích hợp sẵn trong PostgreSQL 16, không cần thêm service; đủ tốt cho vài nghìn tài liệu. |
| **Xử lý nền (MVP)** | FastAPI BackgroundTasks       | Celery + Redis          | Giảm 2 services trong Docker Compose; đơn giản hóa vận hành cho nhóm nhỏ.                |
| **Frontend**        | React 18 + TypeScript         | —                       | Giữ nguyên.                                                                              |
| **Backend**         | FastAPI (Python 3.11)         | —                       | Giữ nguyên.                                                                              |
| **CSDL**            | PostgreSQL 16                 | —                       | Giữ nguyên (vừa lưu trữ vừa FTS).                                                        |
| **Lưu trữ file**    | MinIO (On-premise, S3-compat) | —                       | Giữ nguyên.                                                                              |
| **OCR Engine**      | Tesseract OCR 5.3+ (vie)      | —                       | Giữ nguyên.                                                                              |
| **EPUB Compiler**   | Pandoc + Calibre CLI          | —                       | Giữ nguyên.                                                                              |
| **Web Reader**      | Epub.js 0.3+                  | —                       | Giữ nguyên.                                                                              |
| **Triển khai**      | Docker + Docker Compose       | —                       | Giữ nguyên (3 services: API + PostgreSQL + MinIO).                                       |
| **DRM**             | MinIO Signed URL (15 phút)    | —                       | Giữ nguyên.                                                                              |

### 4.2. Lý do đơn giản hóa Tech Stack

Quyết định đơn giản hóa tech stack xuất phát từ nguyên tắc **cân bằng nguồn lực — phạm vi — thời gian**:

1. **Nguồn lực giới hạn:** Nhóm phát triển gồm 6 sinh viên, không có kinh nghiệm vận hành Keycloak hoặc Elasticsearch cluster ở quy mô production.
2. **Thời gian chặt:** Dự án phải bàn giao MVP trong vòng 12 tuần.
3. **Chi phí tối ưu:** Giảm từ 5–6 services Docker xuống 3 services, tiết kiệm RAM/CPU trên hạ tầng VMware ảo hóa.

### 4.3. Roadmap công nghệ mở rộng

Các công nghệ dưới đây được ghi nhận là **roadmap mở rộng**, chỉ triển khai khi dự án chuyển sang giai đoạn vận hành diện rộng và được phê duyệt bổ sung ngân sách:

| Công nghệ                | Điều kiện kích hoạt                                              |
| :----------------------- | :--------------------------------------------------------------- |
| **Keycloak OIDC + LDAP** | Khi triển khai toàn trường, cần liên kết Active Directory.       |
| **Elasticsearch**        | Khi kho tài liệu vượt 10.000 documents (LDMS-025 trong backlog). |
| **Celery + Redis**       | Khi cần xử lý hàng trăm job OCR song song.                       |

---

## 5. Sản phẩm bàn giao (Deliverables)

| #   | Sản phẩm bàn giao                              | Định dạng / Đặc tả                                    | Thời điểm bàn giao |
| --- | :--------------------------------------------- | :---------------------------------------------------- | :----------------- |
| 1   | Mã nguồn Frontend React (TypeScript)           | Repository Git, chạy được qua `npm run dev`.          | Tuần 12 (MVP)      |
| 2   | Mã nguồn Backend FastAPI (Python)              | Repository Git, chạy được qua `docker compose up`.    | Tuần 12 (MVP)      |
| 3   | Bộ cài đặt Docker Compose                      | File `docker-compose.yml` (API + PostgreSQL + MinIO). | Tuần 12 (MVP)      |
| 4   | Kho 500 giáo trình CNTT số hóa EPUB 3.0        | File EPUB trên MinIO, metadata trên PostgreSQL.       | Tuần 17            |
| 5   | Tài liệu API Swagger UI                        | Tự động sinh từ FastAPI (`/docs`).                    | Tuần 12 (MVP)      |
| 6   | Bộ tài liệu dự án (01–10)                      | File Markdown + PDF, lưu trữ trong thư mục `docs/`.   | Liên tục           |
| 7   | Cẩm nang hướng dẫn sử dụng (thủ thư + độc giả) | File PDF, video hướng dẫn.                            | Tuần 19            |
| 8   | Báo cáo kiểm thử nghiệm thu (UAT Report)       | File Markdown/PDF.                                    | Tuần 19            |

---

## 6. Tiến độ và Các mốc thời gian (Schedule & Milestones)

Dự án được thực hiện trong **20 tuần**, chia thành 4 giai đoạn với các chốt kiểm soát (Gating Checkpoints):

| Giai đoạn | Tên giai đoạn            | Tuần       | Mốc kiểm soát (Milestone)                                                       |
| :-------: | :----------------------- | :--------- | :------------------------------------------------------------------------------ |
|     0     | Khảo sát & Bản quyền     | Tuần 1–2   | **M0:** Quy chế bản quyền số hóa nội bộ được phê duyệt.                         |
|     1     | Xây dựng MVP & Thí điểm  | Tuần 3–12  | **M1:** MVP go-live — 16 Must-have stories Done, 500 cuốn sách số hóa thí điểm. |
|     2     | Số hóa Diện rộng         | Tuần 13–18 | **M2:** 2.000 cuốn giáo trình cốt lõi được số hóa bổ sung.                      |
|     3     | Nghiệm thu & Chuyển giao | Tuần 19–20 | **M3:** UAT pass, pentest bảo mật, go-live toàn trường.                         |

**Phương pháp đo tiến độ:** Throughput-based Forecast — đếm số User Story **Done** (deploy + AC pass) mỗi tuần, dùng công thức `Dev weeks ≈ N(còn lại) / T` để dự báo thời gian hoàn thành.

---

## 7. Chi phí và Ngân sách thống nhất (Agreed Cost & Budget)

### 7.1. Tổng ngân sách đầu tư một lần (CapEx)

| Hạng mục                        |        Khoảng giá (VNĐ)        | Ghi chú chi tiết thù lao / lương nhân lực |
| :------------------------------ | :----------------------------: | :---------------------------------------- |
| Số hóa & Biên tập EPUB (CTV SV) |    30.000.000 – 40.000.000     | Thù lao CTV sinh viên: 30.000 VNĐ/giờ (hoặc 12.000 VNĐ/cuốn 200 trang đã sửa lỗi OCR). |
| Phát triển phần mềm (Nhóm Dev)  |    25.000.000 – 35.000.000     | Phụ cấp khoán nỗ lực cho 6 thành viên nhóm Dev (trung bình 4.5 - 6 triệu VNĐ/người/dự án). |
| Phụ cấp Cán bộ Thư viện         |     4.000.000 – 6.000.000      | Phụ cấp kiêm nhiệm kiểm duyệt cho 02 thủ thư (1.000.000 VNĐ/người/tháng x 3 tháng). |
| Thiết bị scan & Server          |    10.000.000 – 12.000.000     | 02 máy quét chữ V + RAM/SSD nâng cấp server VMware. |
| Đào tạo & Triển khai            |     2.000.000 – 4.000.000      | Tài liệu, video hướng dẫn và tập huấn cán bộ. |
| **Chi phí AI Tools (hạn mức)**  |        **≤ 5.000.000**         | Hạn mức chi trả API/Token AI (Claude, Antigravity, v.v.). |
| Dự phòng rủi ro (~15%)          |     5.000.000 – 10.000.000     | Phát sinh ngoài dự kiến. |
| **TỔNG CAPEX**                  | **≈ 77.000.000 – 106.000.000** | |

### 7.2. Chi phí vận hành định kỳ (OpEx/năm)

| Hạng mục                  |     Khoảng giá (VNĐ/năm)      |
| :------------------------ | :---------------------------: |
| Hạ tầng Server & Cloud    |     4.000.000 – 8.000.000     |
| Bảo trì phần mềm          |    6.000.000 – 12.000.000     |
| Dịch vụ Cloud OCR bổ sung |     3.000.000 – 6.000.000     |
| Số hóa bổ sung hàng năm   |     2.000.000 – 4.000.000     |
| **TỔNG OPEX / NĂM**       | **≈ 15.000.000 – 30.000.000** |

> **Cam kết ngân sách:** Tổng chi phí CapEx + OpEx năm đầu tiên bắt buộc nằm dưới **100.000.000 VNĐ** theo giới hạn tài chính của nhà trường.

---

## 8. Nguồn lực nhân sự và Vai trò AI Assistants

### 8.1. Nhân sự dự án và Cơ chế Thù lao / Lương

#### A. Nhóm Phát triển Dự án (Bên A - Kỹ sư CNTT / Sinh viên Dev)

| #   | Họ và tên             | MSSV     | Email liên hệ                 | Vai trò trong dự án        | Phân bổ thời gian | Mức phụ cấp khoán (VNĐ) |
| --- | :-------------------- | :------- | :---------------------------- | :------------------------- | :---------------- | :---------------------- |
| 1   | Mạch Quốc Tấn         | 23127115 | 23127115@student.hcmus.edu.vn | Project Manager            | Kiêm nhiệm (50%)  | 6.000.000 VNĐ           |
| 2   | Ân Tiến Nguyên An     | 23127148 | 23127148@student.hcmus.edu.vn | Backend Developer (Lead)   | Kiêm nhiệm (50%)  | 5.500.000 VNĐ           |
| 3   | Ngô Nguyễn Thế Khoa   | 23127065 | 23127065@student.hcmus.edu.vn | Frontend Developer (Lead)  | Kiêm nhiệm (50%)  | 5.500.000 VNĐ           |
| 4   | Nguyễn Tuấn Anh       | 23127152 | 23127152@student.hcmus.edu.vn | DevOps / Backend Developer | Kiêm nhiệm (50%)  | 5.000.000 VNĐ           |
| 5   | Nguyễn Quang Thái     | 23127116 | 23127116@student.hcmus.edu.vn | DevOps / QA                | Kiêm nhiệm (50%)  | 4.500.000 VNĐ           |
| 6   | Nguyễn Lê Hồ Anh Khoa | 23127211 | 23127211@student.hcmus.edu.vn | Frontend Developer         | Kiêm nhiệm (50%)  | 4.500.000 VNĐ           |

#### B. Nhân sự Vận hành Thư viện & Cộng tác viên (Bên B - Thư viện HCMUS)

- **Cán bộ Thủ thư (Kiểm duyệt):** 02 người — Phụ cấp kiêm nhiệm kiểm duyệt chất lượng sách & thẩm định bản quyền **1.000.000 VNĐ/tháng/người** (trong 3 tháng cao điểm).
- **Sinh viên CTV (Scan & OCR):** 10–15 người — Thù lao **30.000 VNĐ/giờ** (hoặc khoán **12.000 VNĐ/cuốn 200 trang** đã nghiệm thu không lỗi chính tả OCR).



### 8.2. Vai trò của AI Coding Assistants

Các bên thống nhất rằng nhóm phát triển được phép sử dụng các **AI Coding Assistants** chính (bao gồm **Claude**, **Antigravity**, **Cursor** và các công cụ tương đương) trong quá trình phát triển phần mềm, với các điều kiện:

1. **Minh bạch chi phí:** Mọi phiên làm việc với AI phải ghi nhận số token tiêu thụ, model sử dụng và thời gian vào file `../03-execution-monitoring/02-project-log.md`.
2. **Hạn mức ngân sách AI:** Tổng chi phí AI Tools không vượt quá **5.000.000 VNĐ** trong toàn bộ vòng đời dự án (thuộc hạng mục CapEx).
3. **Kiểm soát chất lượng:** Mọi mã nguồn do AI sinh ra đều phải được con người review, kiểm tra Acceptance Criteria và deploy thành công trước khi tính là Done.
4. **Bản quyền mã nguồn:** Mã nguồn do AI hỗ trợ sinh ra thuộc sở hữu trí tuệ của dự án HCMUS-LDMS, tuân theo giấy phép mã nguồn mở được chọn cho dự án.

---

## 9. Tiêu chí nghiệm thu (Acceptance Criteria)

Dự án được coi là **nghiệm thu thành công** khi đáp ứng đủ các tiêu chí sau:

| #   | Tiêu chí nghiệm thu                                                                            | Ngưỡng chấp nhận     |
| --- | :--------------------------------------------------------------------------------------------- | :------------------- |
| 1   | Toàn bộ **16 User Stories Must-have** đạt trạng thái Done (deploy + Acceptance Criteria pass). | 100% Must-have Done  |
| 2   | Thời gian phản hồi tìm kiếm toàn văn PostgreSQL FTS.                                           | ≤ 3 giây             |
| 3   | Tỷ lệ nhận dạng ký tự OCR tiếng Việt trung bình trên sách in rõ nét (từ 2010).                 | ≥ 85% CAR            |
| 4   | Signed URL MinIO hết hạn sau thời gian quy định, fetch lại bị từ chối.                         | Hết hạn sau 15 phút  |
| 5   | Không hiển thị nút tải file EPUB gốc trên giao diện reader.                                    | Kiểm tra UI          |
| 6   | Hệ thống chạy ổn định trên Docker Compose (3 services healthy) sau `docker compose up`.        | ≤ 5 phút khởi động   |
| 7   | Kho 500 cuốn sách CNTT số hóa thành EPUB 3.0, đọc được trên Epub.js Web Reader.                | ≥ 500 cuốn           |
| 8   | Tất cả sản phẩm bàn giao (mục 5) được chuyển giao đầy đủ cho Bên B.                            | Ký biên bản bàn giao |

---

## 10. Quy chế Kiểm soát Thay đổi (Change Control)

### 10.1. Nguyên tắc liên động Scope–Feature–Resource

Khi phạm vi dự án (Scope) thay đổi, các yếu tố sau sẽ bị ảnh hưởng liên động và phải được đánh giá lại:

```
   Scope thay đổi
       │
       ├── Features (thêm/bớt User Stories)
       ├── Tech Stack (thêm/bớt công nghệ)
       ├── Timeline (kéo dài/rút ngắn)
       └── Cost (tăng/giảm ngân sách)
```

**Ví dụ minh họa thực tế:** Khi nhóm quyết định đưa Keycloak SSO ra khỏi phạm vi MVP và thay bằng Google OAuth 2.0 (commit `1d76700e`), các thay đổi liên động đã xảy ra:

| Yếu tố         | Trước thay đổi                    | Sau thay đổi                                |
| :------------- | :-------------------------------- | :------------------------------------------ |
| **Feature**    | LDMS-009: Keycloak SSO + LDAP     | LDMS-009: Mock JWT → LDMS-018: Google OAuth |
| **Tech Stack** | 5–6 Docker services (có Keycloak) | 3 Docker services (không có Keycloak)       |
| **Timeline**   | Cần 2 tuần setup Keycloak         | Tiết kiệm 2 tuần                            |
| **Cost**       | Cần server riêng cho Keycloak     | Không phát sinh chi phí server thêm         |

### 10.2. Quy trình xử lý yêu cầu thay đổi

1. **Bất kỳ bên nào** phát hiện nhu cầu thay đổi → lập **Phiếu yêu cầu thay đổi (Change Request — CR)** bằng văn bản.
2. PM đánh giá tác động liên động (Scope → Features → Tech → Time → Cost) và trình bày cho các bên.
3. **Thay đổi nhỏ** (≤ 5% ngân sách hoặc ≤ 1 tuần tiến độ): PM và Giám đốc Thư viện cùng ký duyệt.
4. **Thay đổi lớn** (> 5% ngân sách hoặc > 1 tuần tiến độ): Phải có chữ ký phê duyệt của đại diện Ban Giám hiệu.
5. CR được phê duyệt → cập nhật SOW (phiên bản mới) → cập nhật Product Backlog → tiếp tục phát triển.

---

## 11. Các giả định và Ràng buộc

### 11.1. Giả định (Assumptions)

- Khoản 1 Điều 25 Luật SHTT Việt Nam cho phép thư viện trường số hóa tài liệu phục vụ học tập nội bộ phi thương mại.
- Giảng viên nhà trường sẵn sàng ký cam kết đồng ý chia sẻ bản quyền giáo trình tự soạn lên hệ thống.
- Hạ tầng VMware vSphere của trường đủ tài nguyên phân vùng 3 máy chủ ảo hóa (Dev, Staging, Production).
- Tỷ lệ nhận dạng OCR Tesseract đạt tối thiểu 85% trên sách in rõ nét từ năm 2010.
- Nhóm phát triển có quyền sử dụng AI Coding Assistants và chi phí nằm trong hạn mức CapEx.

### 11.2. Ràng buộc (Constraints)

- Tài nguyên máy chủ ảo hóa VMware bị giới hạn RAM/CPU, dùng chung với các dịch vụ khác của trường.
- Nhóm phát triển 6 thành viên sinh viên, làm việc kiêm nhiệm (không phải full-time).
- Tổng ngân sách CapEx + OpEx năm đầu tiên không vượt 100.000.000 VNĐ.
- Tiến độ phụ thuộc năng suất scan/OCR của con người (đường găng WP4).

---

## 12. Quản lý rủi ro liên quan đến nguồn lực

Khi các vấn đề nguồn lực (thời gian, chi phí, công nghệ, nhân sự) không khớp với kế hoạch ban đầu, nhóm phát triển cam kết xử lý theo quy trình sau:

| Loại bất đồng nguồn lực    | Biện pháp xử lý thống nhất                                                                                                         |
| :------------------------- | :--------------------------------------------------------------------------------------------------------------------------------- |
| **Thời gian bị thiếu**     | Cắt bỏ User Stories theo thứ tự MoSCoW ngược: Could → Should. Không cắt Must-have.                                                 |
| **Chi phí vượt hạn mức**   | Dừng các hạng mục Could-have, chuyển ngân sách dự phòng 15% vào hạng mục thiếu hụt. Nếu vẫn thiếu → lập CR trình Ban Giám hiệu.    |
| **Công nghệ gặp trở ngại** | Chuyển sang phương án dự phòng trong roadmap (ví dụ: PostgreSQL FTS thay Elasticsearch). Nếu không có phương án dự phòng → lập CR. |
| **Nhân sự thiếu hụt**      | Phân bổ lại task giữa các thành viên. Nếu nghiêm trọng → PM đề xuất tuyển thêm CTV hoặc giảm scope qua CR.                         |
| **AI Tools bị giới hạn**   | Chuyển sang model rẻ hơn hoặc viết code thủ công. Chi phí AI không được vượt hạn mức 5.000.000 VNĐ.                                |

---

## 13. Chữ ký phê duyệt (Signatures)

Bằng việc ký xác nhận dưới đây, các bên đồng ý với toàn bộ nội dung của Phát biểu Công việc (SOW) phiên bản 1.0 và cam kết thực hiện theo đúng các điều khoản đã nêu.

| Vai trò                                         | Họ và tên | Chữ ký | Ngày ký |
| :---------------------------------------------- | :-------- | :----: | :-----: |
| **Đại diện Ban Giám hiệu (Sponsor — Bên A)**    |           |        |         |
| **Đại diện Thư viện (Client — Bên B)**          |           |        |         |
| **Đại diện Nhóm phát triển (Dev Team — Bên C)** |           |        |         |
| **Đại diện Bộ phận Pháp chế & Lưu trữ**         |           |        |         |

---

> **Ghi chú pháp lý:** Tài liệu SOW này có hiệu lực kể từ ngày ký cuối cùng của tất cả các bên. Mọi sửa đổi phải tuân theo Quy chế Kiểm soát Thay đổi (mục 10) và được ghi nhận bằng phiên bản mới.
