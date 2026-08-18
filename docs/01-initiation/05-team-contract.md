# HỢP ĐỒNG NHÓM (TEAM CONTRACT)

## Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS (HCMUS-LDMS)

### THÔNG TIN TÀI LIỆU (DOCUMENT CONTROL)

| Trường thông tin (Field)                   | Nội dung đặc tả (Description)        |
| :----------------------------------------- | :----------------------------------- |
| **Mã tài liệu (Document ID)**              | `HCMUS-LDMS-TCT`                     |
| **Tên tài liệu (Document Title)**          | Hợp đồng Nhóm (Team Contract)        |
| **Dự án (Project Name)**                   | HCMUS-LDMS                           |
| **Đơn vị soạn thảo (Author/Organization)** | Nhóm Phát triển Dự án HCMUS-LDMS     |
| **Người xem xét (Reviewer)**               | Toàn bộ thành viên nhóm              |
| **Người phê duyệt (Approver)**             | Toàn bộ thành viên nhóm (đồng thuận) |
| **Cấp độ bảo mật (Security Class)**        | Internal (Nội bộ nhóm)               |
| **Trạng thái tài liệu (Status)**           | Active (Có hiệu lực)                 |

### LỊCH SỬ PHIÊN BẢN (REVISION HISTORY)

| Phiên bản (Version) | Ngày phát hành (Date) | Mô tả thay đổi (Description of Change)                                                                | Người thực hiện (Author) |
| :-----------------: | :-------------------: | :---------------------------------------------------------------------------------------------------- | :----------------------: |
|         1.0         |      24/07/2026       | Khởi tạo Hợp đồng Nhóm chính thức, bao gồm phân vai, quy tắc giao tiếp, quy trình AI và kỷ luật nhóm. |    Ân Tiến Nguyên An     |

---

## Mục lục

- [1. Mục đích Hợp đồng Nhóm](#1-mục-đích-hợp-đồng-nhóm)
- [2. Thông tin thành viên và Mục tiêu](#2-thông-tin-thành-viên-và-mục-tiêu)
  - [2.1. Danh sách thành viên](#21-danh-sách-thành-viên)
  - [2.2. Mục tiêu chung của nhóm](#22-mục-tiêu-chung-của-nhóm)
  - [2.3. Mục tiêu cá nhân](#23-mục-tiêu-cá-nhân)
- [3. Phân vai và Trách nhiệm (Roles & Responsibilities)](#3-phân-vai-và-trách-nhiệm-roles-responsibilities)
  - [3.1. Ma trận phân vai và Trách nhiệm](#31-ma-trận-phân-vai-và-trách-nhiệm)
  - [3.2. Nguyên tắc phân công công việc](#32-nguyên-tắc-phân-công-công-việc)
- [4. Phương pháp làm việc (Work Methodology)](#4-phương-pháp-làm-việc-work-methodology)
  - [4.1. Kanban và WIP Limit](#41-kanban-và-wip-limit)
  - [4.2. Định nghĩa Hoàn thành (Definition of Done — DoD)](#42-định-nghĩa-hoàn-thành-definition-of-done-dod)
  - [4.3. Đo lường Throughput và Forecast](#43-đo-lường-throughput-và-forecast)
- [5. Quy tắc Giao tiếp (Communication Norms)](#5-quy-tắc-giao-tiếp-communication-norms)
  - [5.1. Kênh giao tiếp chính thức](#51-kênh-giao-tiếp-chính-thức)
  - [5.2. Lịch họp nhóm](#52-lịch-họp-nhóm)
  - [5.3. Quy tắc phản hồi](#53-quy-tắc-phản-hồi)
- [6. Quy trình sử dụng AI Coding Assistants](#6-quy-trình-sử-dụng-ai-coding-assistants)
  - [6.1. AI Tools được phép sử dụng](#61-ai-tools-được-phép-sử-dụng)
  - [6.2. Quy tắc sử dụng AI](#62-quy-tắc-sử-dụng-ai)
  - [6.3. Ghi nhận Session Log](#63-ghi-nhận-session-log)
- [7. Quản lý mã nguồn (Source Control)](#7-quản-lý-mã-nguồn-source-control)
- [8. Triết lý Quản trị & Giải quyết Xung đột (Theory Y & Policy-based Resolution)](#8-triết-lý-quản-trị-giải-quyết-xung-đột-theory-y-policy-based-resolution)
  - [8.1. Triết lý Quản trị Lý thuyết Y (Theory Y Principles)](#81-triết-lý-quản-trị-lý-thuyết-y-theory-y-principles)
  - [8.2. Chính sách Thiết lập Sớm để Phòng ngừa Xung đột (Proactive Policies)](#82-chính-sách-thiết-lập-sớm-để-phòng-ngừa-xung-đột-proactive-policies)
  - [8.3. Quy trình Giải quyết Bất đồng Kỹ thuật & Nghiệp vụ](#83-quy-trình-giải-quyết-bất-đồng-kỹ-thuật-nghiệp-vụ)
- [9. Cam kết và Kỷ luật (Accountability & Consequences)](#9-cam-kết-và-kỷ-luật-accountability-consequences)
  - [9.1. Cam kết chung](#91-cam-kết-chung)
  - [9.2. Xử lý vi phạm](#92-xử-lý-vi-phạm)
- [10. Điều khoản sửa đổi](#10-điều-khoản-sửa-đổi)
- [11. Chữ ký cam kết (Signatures)](#11-chữ-ký-cam-kết-signatures)

---
## 1. Mục đích Hợp đồng Nhóm

Hợp đồng Nhóm (Team Contract) là thỏa thuận nội bộ giữa tất cả thành viên nhóm phát triển dự án **HCMUS-LDMS**, nhằm:

- Thiết lập **kỳ vọng chung** về chất lượng công việc, tiến độ và trách nhiệm cá nhân.
- Xây dựng **quy tắc giao tiếp** rõ ràng để phối hợp hiệu quả.
- Thống nhất **phương pháp làm việc** (Kanban, DoD, throughput) và **quy trình sử dụng AI**.
- Định nghĩa **cơ chế giải quyết xung đột** khi phát sinh bất đồng kỹ thuật hoặc tiến độ.
- Tạo nền tảng **kỷ luật nhóm** đảm bảo dự án được hoàn thành đúng cam kết trong SOW.

> **Tài liệu sống (Living Document):** Hợp đồng này có thể được điều chỉnh khi nhóm nhận thấy quy trình không phù hợp. Mọi sửa đổi phải được sự đồng thuận của toàn bộ thành viên (mục 10).

---

## 2. Thông tin thành viên và Mục tiêu

### 2.1. Danh sách thành viên

| #   | Họ và tên             | MSSV     | Email liên hệ                 | Vai trò chính              |
| --- | :-------------------- | :------- | :---------------------------- | :------------------------- |
| 1   | Ngô Nguyễn Thế Khoa   | 23127065 | 23127065@student.hcmus.edu.vn | Frontend Developer         |
| 2   | Mạch Quốc Tấn         | 23127115 | 23127115@student.hcmus.edu.vn | Backend Developer          |
| 3   | Nguyễn Quang Thái     | 23127116 | 23127116@student.hcmus.edu.vn | Devops / QA                |
| 4   | Ân Tiến Nguyên An     | 23127148 | 23127148@student.hcmus.edu.vn | Project Manager            |
| 5   | Nguyễn Tuấn Anh       | 23127152 | 23127152@student.hcmus.edu.vn | DevOps / Backend Developer |
| 6   | Nguyễn Lê Hồ Anh Khoa | 23127211 | 23127211@student.hcmus.edu.vn | Frontend Developer         |

### 2.2. Mục tiêu chung của nhóm

1. Hoàn thành toàn bộ **16 Must-have User Stories** trước tuần 12 (MVP go-live).
2. Bàn giao đầy đủ sản phẩm theo cam kết SOW (tài liệu 10).
3. Đạt điểm cao trong môn học Quản lý Dự án thông qua chất lượng tài liệu và sản phẩm phần mềm.
4. Mỗi thành viên đều có đóng góp thực tế, được ghi nhận qua `../03-execution-monitoring/02-project-log.md`.

### 2.3. Mục tiêu cá nhân

Mỗi thành viên cam kết theo đuổi ít nhất **1 mục tiêu phát triển cá nhân** trong quá trình thực hiện dự án:

| Thành viên            | Vai trò chính              | Mục tiêu cá nhân                                                                                            |
| :-------------------- | :------------------------- | :---------------------------------------------------------------------------------------------------------- |
| Ngô Nguyễn Thế Khoa   | Frontend Developer         | Thành thạo xây dựng UI React TypeScript, thiết kế giao diện Split-screen Editor và nâng cao trải nghiệm UX. |
| Mạch Quốc Tấn         | Project Manager            | Nâng cao kỹ năng quản lý dự án, theo dõi tiến độ Kanban/Throughput và điều phối nhóm hiệu quả.              |
| Nguyễn Quang Thái     | Devops / QA                | Làm chủ quy trình kiểm thử phần mềm (UAT/unit test), giám sát chất lượng và hỗ trợ vận hành Docker.         |
| Ân Tiến Nguyên An     | Backend Developer / SA     | Làm chủ việc thiết kế kiến trúc Backend FastAPI, xử lý tác vụ OCR/Pandoc bất đồng bộ và tối ưu CSDL.        |
| Nguyễn Tuấn Anh       | DevOps / Backend Developer | Thành thạo quản trị Docker Compose, cấu hình hệ thống xác thực (Google OAuth/JWT) và CI/CD.                 |
| Nguyễn Lê Hồ Anh Khoa | Frontend Developer         | Nâng cao kỹ năng React, làm chủ tích hợp thư viện Epub.js Reader và tùy biến giao diện đọc sách.            |

---

## 3. Phân vai và Trách nhiệm (Roles & Responsibilities)

### 3.1. Ma trận phân vai và Trách nhiệm

#### A. Phân vai theo chức danh kỹ thuật

| Vai trò                          | Trách nhiệm chính                                                                                                                      | Thành viên phụ trách                       |
| :------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------- |
| **Project Manager (PM)**         | Lập kế hoạch, theo dõi tiến độ throughput, kiểm soát rủi ro, điều phối nhóm, tổng hợp báo cáo Weekly Review, duy trì `../03-execution-monitoring/02-project-log.md`. | Mạch Quốc Tấn                              |
| **Solution Architect (SA) / BE** | Thiết kế kiến trúc Modular Monolith, lập trình API FastAPI, tích hợp OCR/Pandoc, review code chất lượng và phê duyệt Pull Request.     | Ân Tiến Nguyên An                          |
| **Backend Developer**            | Phát triển các API nghiệp vụ FastAPI, truy vấn PostgreSQL Full-Text Search và thiết lập lưu trữ MinIO.                                 | Ân Tiến Nguyên An, Nguyễn Tuấn Anh         |
| **Frontend Developer**           | Lập trình UI React (Dashboard, Split-screen Editor, Reader), tích hợp Epub.js và xử lý state management.                               | Ngô Nguyễn Thế Khoa, Nguyễn Lê Hồ Anh Khoa |
| **DevOps / System Admin**        | Quản trị Docker Compose (3 services), cấu hình CI/CD, thiết lập Google OAuth 2.0 / Mock JWT, quản lý môi trường Staging/Production.    | Nguyễn Tuấn Anh, Nguyễn Quang Thái         |
| **QA / Tester**                  | Xây dựng test scenario, thực hiện kiểm thử chức năng (UAT), viết test case và kiểm soát tiêu chí nghiệm thu Acceptance Criteria.       | Nguyễn Quang Thái                          |

#### B. Ma trận RACI nội bộ nhóm theo Gói công việc WBS

- **R** (Responsible): Thành viên trực tiếp thực hiện công việc.
- **A** (Accountable): Thành viên chịu trách nhiệm duyệt và giải trình cuối cùng (**duy nhất 1 người/gói công việc**).
- **C** (Consulted): Thành viên tham gia đóng góp ý kiến chuyên môn.
- **I** (Informed): Thành viên nhận thông tin tiến độ/kết quả.

| Gói công việc WBS                  | Ngô N. T. Khoa (`23127065`) | Mạch Quốc Tấn (`23127115`) | N. Quang Thái (`23127116`) | Ân T. N. An (`23127148`) | N. Tuấn Anh (`23127152`) | N. L. H. A. Khoa (`23127211`) |
| :--------------------------------- | :-------------------------: | :------------------------: | :------------------------: | :----------------------: | :----------------------: | :---------------------------: |
| **WP1 — Khảo sát & Bản quyền**     |              R              |         **A** / R          |             C              |            R             |            C             |               R               |
| **WP2 — Cơ sở dữ liệu & Backend**  |              I              |             C              |             I              |        **A** / R         |            R             |               I               |
| **WP3 — Giao diện UI & Trình đọc** |          **A** / R          |             I              |             C              |            C             |            I             |               R               |
| **WP4 — Số hóa & Xử lý OCR/EPUB**  |              C              |             C              |             I              |        **A** / R         |            R             |               C               |
| **WP5 — Kiểm thử, QA & UAT**       |              R              |             I              |         **A** / R          |            C             |            C             |               R               |
| **WP6 — Triển khai & Vận hành**    |              I              |             C              |             R              |            C             |        **A** / R         |               I               |

### 3.2. Nguyên tắc phân công công việc

1. **Phân công theo Module:** Mỗi User Story thuộc một Module (M0–M8). PM phân công story cho thành viên có chuyên môn phù hợp với module đó.
2. **Ownership rõ ràng:** Mỗi story khi được kéo vào _In Progress_ phải có đúng **1 người chịu trách nhiệm** (owner). Không có story "vô chủ".
3. **Hỗ trợ chéo:** Khi một thành viên bị block (chờ dependency hoặc gặp khó khăn kỹ thuật), các thành viên khác có trách nhiệm hỗ trợ khi được yêu cầu.
4. **Không chồng chéo:** Hai người không được làm cùng một story trừ khi PM chỉ định rõ pair-programming.

---

## 4. Phương pháp làm việc (Work Methodology)

### 4.1. Kanban và WIP Limit

Nhóm áp dụng phương pháp **Kanban** với các quy tắc:

- **Board Kanban:** Sử dụng GitHub Projects (hoặc công cụ tương đương) với các cột: `Backlog` → `Ready` → `In Progress` → `Review` → `Done`.
- **WIP Limit:** Mỗi thành viên chỉ được giữ tối đa **1 card** ở trạng thái _In Progress_ tại bất kỳ thời điểm nào.
- **Definition of Ready (DoR):** Card chỉ được kéo vào _In Progress_ khi:
  - Có ID (LDMS-xxx) và Acceptance Criteria rõ ràng.
  - Tất cả `depends_on` đã ở trạng thái Done.
  - Size là S (≤ 1 ngày) hoặc M (≤ 2 ngày). Card quá lớn phải tách nhỏ trước.

### 4.2. Định nghĩa Hoàn thành (Definition of Done — DoD)

Một User Story chỉ được coi là **Done** khi đáp ứng đủ **5 tiêu chí**:

| #   | Tiêu chí DoD   | Mô tả chi tiết                                                              |
| --- | :------------- | :-------------------------------------------------------------------------- |
| 1   | **AC pass**    | Toàn bộ Acceptance Criteria của card đã kiểm tra đạt.                       |
| 2   | **Code merge** | Mã nguồn merge vào nhánh chính qua Pull Request (self-review checklist OK). |
| 3   | **Chạy local** | Chạy được trên môi trường local (`docker compose up` + `npm run dev`).      |
| 4   | **README**     | Endpoint hoặc trang mới có ghi trong README module.                         |
| 5   | **Log effort** | Ghi nhận thời gian thực hiện và token AI vào `../03-execution-monitoring/02-project-log.md`.              |

### 4.3. Đo lường Throughput và Forecast

- **Throughput (T):** Số User Story **Done** (deploy + AC pass) trong 1 tuần.
- **Forecast:** `Dev weeks ≈ N(stories còn lại) / T`. Báo cáo dạng **khoảng** (optimistic – pessimistic) vì các story có độ khó khác nhau.
- **Cập nhật:** PM tính toán và báo cáo throughput mỗi cuối tuần trong Weekly Review.

---

## 5. Quy tắc Giao tiếp (Communication Norms)

### 5.1. Kênh giao tiếp chính thức

| Kênh                  | Mục đích sử dụng                                                   | Thời gian phản hồi tối đa |
| :-------------------- | :----------------------------------------------------------------- | :------------------------ |
| **Messenger/Discord** | Trao đổi nhanh hàng ngày, thông báo khẩn cấp, chia sẻ link/file.   | **12 giờ**                |
| **GitHub Issues**     | Thảo luận kỹ thuật gắn liền với story/code, review PR.             | **24 giờ**                |
| **Google Meet**       | Họp nhóm trực tuyến (Daily Standup, Weekly Review).                | Theo lịch                 |
| **Email**             | Giao tiếp chính thức với giảng viên hoặc bên liên quan ngoài nhóm. | **24 giờ**                |

### 5.2. Lịch họp nhóm

| Loại họp                      | Tần suất           | Thời lượng | Nội dung chính                                                                      |
| :---------------------------- | :----------------- | :--------- | :---------------------------------------------------------------------------------- |
| **Daily Standup**             | Hàng ngày (online) | 15 phút    | Mỗi người báo: Hôm qua làm gì? Hôm nay làm gì? Có bị block không?                   |
| **Weekly Review**             | Cuối tuần          | 30–45 phút | Đếm story Done, tính throughput, forecast tuần tới, cập nhật rủi ro.                |
| **Gating Review (Phase-end)** | Cuối mỗi giai đoạn | 60 phút    | Tổng kết giai đoạn, trình bày cho giảng viên/stakeholder, xin phê duyệt chuyển pha. |

### 5.3. Quy tắc phản hồi

1. **Tin nhắn khẩn cấp** (hệ thống sập, lỗi bảo mật, deadline trong 24h): Phản hồi trong vòng **2 giờ**.
2. **Tin nhắn thường**: Phản hồi trong vòng **12 giờ**.
3. **Pull Request review**: Phản hồi (approve hoặc request changes) trong vòng **24 giờ**.
4. **Không phản hồi = đồng ý:** Nếu quá thời gian phản hồi mà không có ý kiến, coi như đồng ý với đề xuất.

---

## 6. Quy trình sử dụng AI Coding Assistants

### 6.1. AI Tools được phép sử dụng

| AI Tool         | Mục đích sử dụng chính                                                                   |
| :-------------- | :--------------------------------------------------------------------------------------- |
| **Claude**      | Phân tích tài liệu spec, thiết kế kiến trúc, lên kế hoạch và đề xuất giải pháp kỹ thuật. |
| **Antigravity** | Agentic AI coding assistant cho pair programming, sinh mã nguồn, refactor và debug sâu.  |
| **Cursor**      | IDE AI hỗ trợ autocomplete mã nguồn, chỉnh sửa code đa file và phát triển tính năng.     |

### 6.2. Quy tắc sử dụng AI

1. **AI là công cụ, không phải tác giả:** Mọi mã nguồn do AI sinh ra phải được thành viên nhóm **đọc hiểu, review và kiểm tra** trước khi merge. Thành viên phải có khả năng giải thích được code cho giảng viên.
2. **Không chạy code AI mù quáng:** Luôn kiểm tra Acceptance Criteria và chạy local trước khi đánh dấu Done.
3. **Tối ưu token:** Sử dụng AI có mục đích rõ ràng (prompt cụ thể, context đầy đủ). Không chat lan man tiêu hao token vô ích.
4. **Hạn mức ngân sách:** Tổng chi phí AI Tools của cả nhóm không vượt quá **5.000.000 VNĐ** (theo SOW mục 7).
5. **Công bằng:** Mọi thành viên đều có quyền sử dụng AI. Không có thành viên nào bị cấm sử dụng hoặc độc quyền công cụ AI.

### 6.3. Ghi nhận Session Log

Sau **mỗi phiên làm việc** với AI Coding Assistant, thành viên **bắt buộc** ghi nhận một dòng log vào file `../03-execution-monitoring/02-project-log.md` với các trường:

| Trường           | Bắt buộc | Mô tả                                          |
| :--------------- | :------: | :--------------------------------------------- |
| Ngày hoàn thành  |        | Ngày kết thúc session.                         |
| Dev              |        | Tên thành viên thực hiện.                      |
| Story ID         |        | Mã các stories hoàn thành trong session.       |
| Tên Story        |        | Mô tả ngắn gọn công việc đã làm.               |
| Thời gian làm    |        | Tổng thời gian thực tế (giờ hoặc phút).        |
| Token AI đã dùng |        | Số token AI tiêu thụ trong session.            |
| Ghi chú          |        | Model AI sử dụng và ghi chú đặc biệt (nếu có). |

> **Vi phạm:** Không ghi session log sẽ bị tính là vi phạm kỷ luật nhóm (mục 9.2).

---

## 7. Quản lý mã nguồn (Source Control)

Nhóm áp dụng mô hình **GitFlow** để điều phối mã nguồn:

| Nhánh       | Vai trò                                                                                  | Quyền merge                   |
| :---------- | :--------------------------------------------------------------------------------------- | :---------------------------- |
| `main`      | Mã nguồn ổn định, chạy trên Production. Mỗi lần merge đánh tag phiên bản (vd. `v1.0.0`). | Chỉ SA/PM phê duyệt PR.       |
| `develop`   | Nhánh tích hợp chính. Tất cả feature merge vào đây sau khi review.                       | Self-review + 1 approve khác. |
| `feature/*` | Phát triển tính năng riêng lẻ (vd. `feature/ocr-integration`). Tạo từ `develop`.         | Tự tạo, merge sau khi review. |
| `release/*` | Chuẩn bị phát hành (vd. `release/v1.0-MVP`). Fix lỗi cuối trước khi merge vào `main`.    | SA/PM phê duyệt.              |
| `hotfix/*`  | Sửa lỗi khẩn cấp từ `main`. Merge đồng thời vào `main` và `develop`.                     | SA/PM phê duyệt.              |

**Quy tắc commit:**

- Viết commit message theo convention: `type(scope): description` (vd. `feat(ocr): add Tesseract pipeline`).
- Không commit trực tiếp lên `main` hoặc `develop`.
- Không commit secret keys, API tokens hoặc file `.env` vào repository.

---

## 8. Triết lý Quản trị & Giải quyết Xung đột (Theory Y & Policy-based Resolution)

Nhóm thống nhất áp dụng **Lý thuyết Y của Douglas McGregor (Theory Y)** làm triết lý quản trị và giải quyết xung đột xuyên suốt dự án. Nhóm tin tưởng rằng mỗi thành viên đều là người siêng năng, có tinh thần trách nhiệm cao, tự giác và khao khát hoàn thành công việc với chất lượng tốt nhất.

### 8.1. Triết lý Quản trị Lý thuyết Y (Theory Y Principles)

1. **Tự chọn Task (Self-Selection):**
   - Thành viên chủ động kéo card từ cột `Ready` sang `In Progress` trên Kanban Board dựa theo thế mạnh, mong muốn phát triển cá nhân và năng lực bản thân, thay vì chờ PM phân công cứng nhắc.
2. **Tự báo cáo Trạng thái (Self-Reporting & Autonomy):**
   - Thành viên tự chịu trách nhiệm cập nhật trạng thái công việc (WIP), chủ động ghi nhận effort/token vào `../03-execution-monitoring/02-project-log.md` sau mỗi phiên làm việc, và tự báo cáo các nút thắt (blocker) tại các buổi Daily Standup.
3. **Phát huy Năng lực Tự quản (Self-Direction):**
   - Nhóm tạo không gian sáng tạo kỹ thuật cho từng cá nhân, coi sai sót nhỏ là cơ hội học tập và hoàn thiện, không áp đặt tâm lý quản lý vi mô (micromanagement) hay nghi ngờ thái độ làm việc của thành viên.

### 8.2. Chính sách Thiết lập Sớm để Phòng ngừa Xung đột (Proactive Policies)

Để ngăn chặn xung đột từ sớm thay vì chờ sự cố xảy ra mới giải quyết, nhóm thiết lập các **Chính sách Tiền lệ (Policies)** bắt buộc tuân thủ:

- **Policy 1 — Minh bạch Tiến độ & Nhật ký (Log Policy):** Mọi công việc và phiên dùng AI phải được log vào `../03-execution-monitoring/02-project-log.md` trong vòng 12h. Việc minh bạch giúp loại bỏ rủi ro nghi ngờ đóng góp của nhau.
- **Policy 2 — Độc lập Branch & Code Review (Git Policy):** 100% code mới phải qua Pull Request và có ít nhất 1 thành viên review. Không tự ý sửa code của người khác trên branch cá nhân.
- **Policy 3 — Quy tắc Đặt lịch & Báo bận (Availability Policy):** Thành viên bận việc đột xuất hoặc có lịch thi cử phải thông báo lên nhóm Zalo/Discord trước tối thiểu **24 giờ** để nhóm chủ động hỗ trợ.

### 8.3. Quy trình Giải quyết Bất đồng Kỹ thuật & Nghiệp vụ

Khi xuất hiện xung đột quan điểm (kỹ thuật, kiến trúc hoặc ưu tiên feature), nhóm giải quyết theo quy trình Lý thuyết Y tôn trọng sự chủ động:

1. **Thảo luận dựa trên Dữ liệu & Empirical Evidence (Data-driven Discussion):**
   - Các bên trình bày giải pháp dựa trên minh chứng kỹ thuật (benchmark, kết quả PoC, best practices) trên tinh thần xây dựng, hướng tới mục tiêu chung của dự án.
2. **Thử nghiệm đối chứng (PoC Comparison):**
   - Nếu có 2 giải pháp kỹ thuật bất đồng, cho phép 2 bên tạo branch PoC nhỏ để đo lường thực tế (hiệu năng, dòng code) rồi nhóm cùng chọn giải pháp tốt nhất.
3. **Biểu quyết Dân chủ (Team Consensus):**
   - Nếu vẫn chưa đạt đồng thuận, tiến hành biểu quyết nhóm (quá bán ≥ 4/6). Phương án được chọn sẽ nhận được sự ủng hộ 100% của toàn nhóm với cam kết _"Disagree and Commit"_.
4. **Tham vấn Giảng viên / Mentor:**
   - Chỉ leo thang nhờ Giảng viên hướng dẫn tư vấn khi gặp các bế tắc về định hướng kiến trúc lớn không thể tự quyết định. Quyết định của giảng viên là quyết định cuối cùng.

---

## 9. Cam kết và Kỷ luật (Accountability & Consequences)

### 9.1. Cam kết chung

Tất cả thành viên cam kết:

1. **Hoàn thành công việc đúng hạn:** Mỗi story được giao phải hoàn thành trong thời gian size quy định (S ≤ 1 ngày, M ≤ 2 ngày). Nếu dự kiến trễ, phải báo PM **trước** deadline.
2. **Tham gia đầy đủ các buổi họp:** Daily Standup, Weekly Review và Gating Review. Vắng mặt phải báo trước ≥ 12 giờ.
3. **Ghi nhận session log:** Bắt buộc ghi vào `../03-execution-monitoring/02-project-log.md` sau mỗi phiên làm việc với AI.
4. **Code quality:** Mã nguồn phải pass self-review checklist trước khi tạo Pull Request.
5. **Tôn trọng lẫn nhau:** Giao tiếp chuyên nghiệp, không gây ảnh hưởng tiêu cực đến tinh thần nhóm.
6. **Trung thực:** Không khai gian thời gian, token AI hoặc mạo nhận công việc của người khác.

### 9.2. Xử lý vi phạm

|  Mức vi phạm   | Hành vi                                                                                        | Hậu quả                                                                           |
| :------------: | :--------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------- |
|    **Nhẹ**     | Trễ phản hồi tin nhắn quá thời gian quy định, quên ghi session log 1 lần.                      | PM nhắc nhở trực tiếp. Thành viên bổ sung ngay.                                   |
| **Trung bình** | Vắng họp không báo trước, trễ deadline story mà không thông báo, quên ghi session log ≥ 2 lần. | PM ghi nhận trong biên bản. Thành viên giải trình trước nhóm trong Weekly Review. |
|    **Nặng**    | Không hoàn thành công việc liên tục (≥ 3 stories liên tiếp), không hợp tác, gian lận.          | Báo cáo giảng viên. Ghi nhận vào đánh giá đóng góp cá nhân cuối kỳ.               |

---

## 10. Điều khoản sửa đổi

- Hợp đồng Nhóm là **tài liệu sống** — có thể được sửa đổi khi cần thiết.
- Mọi sửa đổi phải được **đề xuất trong buổi Weekly Review** và **biểu quyết đồng thuận** (≥ 4/6 thành viên đồng ý).
- Phiên bản mới phải được ghi nhận trong bảng Lịch sử Phiên bản và tất cả thành viên ký lại xác nhận.

---

## 11. Chữ ký cam kết (Signatures)

Bằng việc ký xác nhận dưới đây, tôi cam kết tuân thủ toàn bộ nội dung của Hợp đồng Nhóm phiên bản 1.0 và chấp nhận các hậu quả khi vi phạm.

| #   | Họ và tên             | MSSV     | Chữ ký | Ngày ký |
| --- | :-------------------- | :------- | :----: | :-----: |
| 1   | Ngô Nguyễn Thế Khoa   | 23127065 |        |         |
| 2   | Mạch Quốc Tấn         | 23127115 |        |         |
| 3   | Nguyễn Quang Thái     | 23127116 |        |         |
| 4   | Ân Tiến Nguyên An     | 23127148 |        |         |
| 5   | Nguyễn Tuấn Anh       | 23127152 |        |         |
| 6   | Nguyễn Lê Hồ Anh Khoa | 23127211 |        |         |

---
