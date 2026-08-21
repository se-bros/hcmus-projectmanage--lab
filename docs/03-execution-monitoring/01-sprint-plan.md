# BIÊN BẢN HỌP NHÓM & KẾ HOẠCH PHÂN CÔNG SPRINT 1
## (MEETING MINUTES & SPRINT 1 PLANNING RECORD)
### Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS (HCMUS-LDMS)

---

### BẢNG LỊCH SỬ THAY ĐỔI TÀI LIỆU (DOCUMENT REVISION HISTORY)

| Phiên bản (Version) | Ngày (Date) | Tác giả (Author) | Mô tả thay đổi (Description) |
| :---: | :---: | :---: | :--- |
| `1.0` | 14/07/2026 | Nguyễn Tuấn Anh (Thư ký) | Soạn thảo kế hoạch phân công Sprint 1 theo Backlog. |
| `1.1` | 20/08/2026 | Mạch Quốc Tấn (PM) | Chuẩn hóa định dạng Biên bản họp nhóm chính thức phục vụ hồ sơ đồ án và vấn đáp. |

---

### THÔNG TIN TÀI LIỆU (DOCUMENT CONTROL)

| Trường thông tin (Field) | Nội dung đặc tả (Description) |
| :--- | :--- |
| **Mã tài liệu (Document ID):** | `HCMUS-LDMS-MM01` / `HCMUS-LDMS-SPR1` |
| **Tên tài liệu (Document Title):** | Biên bản Họp Nhóm & Kế hoạch Phân công Phát triển Sprint 1 |
| **Dự án (Project Name):** | Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS (HCMUS-LDMS) |
| **Nguồn Backlog tham chiếu:** | [`docs/02-planning/03-product-backlog.md`](../02-planning/03-product-backlog.md) |
| **Thời gian họp:** | 19:30 – 21:45, Thứ Ba ngày 14/07/2026 |
| **Địa điểm:** | Kênh voice Discord server `SE Bros` kết hợp Google Meet |
| **Chủ trì cuộc họp (Chair):** | **Mạch Quốc Tấn** (Project Manager) |
| **Thư ký cuộc họp (Secretary):** | **Nguyễn Tuấn Anh** (DevOps / QA Lead) |
| **Thành viên tham dự:** | Đầy đủ 6/6 thành viên (*Mạch Quốc Tấn, Nguyễn Tuấn Anh, Khoa Ngô, Nguyễn Trường Thái, Khoa Nguyễn, Nguyễn Đức An*) |

---

## 1. Nội dung & Diễn biến Cuộc họp (Meeting Agenda & Decisions)

### 1.1. Mục tiêu Sprint 1
- Toàn bộ nhóm thống nhất mục tiêu hoàn thành **16 User Stories Must-have** và kéo sớm **1 Story Should-have** (`LDMS-018`: Google OAuth) để cân bằng khối lượng công việc giữa các thành viên.
- Thời lượng Sprint: **9 ngày** (từ 15/07/2026 đến 24/07/2026).
- Chia làm 2 mốc kiểm soát rõ ràng:
  - **Mốc 1 (Ngày 1–2, 17/07):** Ra mắt bản chạy tối thiểu (PoC) xuyên suốt luồng: *Tải lên file scan $\rightarrow$ OCR $\rightarrow$ Xem tài liệu placeholder*.
  - **Mốc 2 (Ngày 3–9, 24/07):** Hoàn thiện $100\%$ tiêu chí Definition of Done (DoD) và Acceptance Criteria (AC) cho toàn bộ 17 User Stories.

### 1.2. Thống nhất Quy chế Vận hành Kỹ thuật & Quản trị
1. **Cơ chế Kanban & Giới hạn WIP:** Áp dụng nguyên tắc **WIP Limit = 1 card/người** trên Trello Board. Mỗi thành viên tự chủ động kéo task theo thế mạnh cá nhân (Triết lý Lý thuyết Y).
2. **Quy chuẩn Fullstack:** Mỗi thành viên chịu trách nhiệm từ đầu đến cuối (End-to-End) cho story của mình (viết cả Backend FastAPI, Frontend React, Schema Pydantic và Test).
3. **Chính sách Review Pull Request (Policy 2):** $100\%$ code phải qua Pull Request, tự động pass linter Ruff + Pytest trên CI, và có ít nhất 1 thành viên review độc lập trước khi merge.
4. **Daily Standup:** Họp nhanh 15 phút mỗi ngày lúc 21:00 trên Discord để rà soát blocker.

---

## 2. Bảng Phân công Trách nhiệm theo Epic (Epic Allocation)

| Thành viên | Thiên hướng | Epic / Cụm module đảm nhiệm | Phạm vi User Stories từ Backlog |
| :--- | :--- | :--- | :--- |
| **Tuấn Anh** | Backend / DevOps | **Epic D + Epic A** — Platform & Identity | `LDMS-001`, `LDMS-009`, `LDMS-010`, `LDMS-018` |
| **Khoa Ngô** | Backend / AI | **Epic B (nhánh Pipeline)** — Digitization & Publish | `LDMS-002`, `LDMS-003`, `LDMS-004`, `LDMS-007`, `LDMS-022`, `LDMS-013` |
| **Thái** | Frontend / UI | **Epic B (nhánh Editorial)** — Biên tập & Metadata | `LDMS-005`, `LDMS-006`, `LDMS-011`, `LDMS-012`, `LDMS-017` |
| **Khoa Nguyễn** | Frontend / UX | **Epic C** — Search & Reader UX | `LDMS-008`, `LDMS-014`, `LDMS-015`, `LDMS-016`, `LDMS-019`, `LDMS-020`, `LDMS-026` |
| **Mạch Quốc Tấn** | PM / Backend | Quản trị dự án, điều phối Sprint, Review Kiến trúc & Rủi ro | `LDMS-RSK`, `LDMS-QMP`, `LDMS-TCT`, Quản lý RAID Log |
| **Nguyễn Đức An** | Solution Architect | Thiết kế Kiến trúc Monorepo, Database Schema & Giám sát CI/CD | `LDMS-ARCH`, `LDMS-FTS`, Review Database Migration |

---

## 3. Kế hoạch Thực thi Chi tiết Từng Mốc

### 3.1. Mốc 1 — Ngày 1–2 (15/07 – 17/07): Bản chạy tối thiểu (PoC)

Thống nhất Data Model tối thiểu (`Document`, `Page`, `User`, `Category`) và cấu trúc monorepo `/frontend`, `/backend`.

| Thành viên | Story đảm nhiệm (Bản rút gọn) | Công việc cụ thể |
| :--- | :--- | :--- |
| **Tuấn Anh** | **LDMS-001** (Setup môi trường) | Cấu hình Monorepo, Docker Compose cho FastAPI, PostgreSQL 16, MinIO; Endpoint `GET /health` trả 200. |
| **Khoa Ngô** | **LDMS-002** (Upload file scan) | Endpoint upload file PDF vào MinIO và form React kéo thả tối giản. |
| **Thái** | Chuẩn bị **LDMS-006** (Editor UI) | Dựng khung giao diện chung (Routing, Navbar) và Editor trên dữ liệu giả (Fixture text). |
| **Khoa Nguyễn** | Chuẩn bị **LDMS-008** & **LDMS-026** | Placeholder màn hình Reader và Search đọc text thô từ fixture mock. |

---

### 3.2. Mốc 2 — Ngày 3–9 (18/07 – 24/07): Hoàn thiện 100% Acceptance Criteria & DoD

#### A. Tuấn Anh — Epic D + A (Platform & Identity)
| Ngày | Mã Story | Nội dung công việc | Module / Size / MoSCoW | Phụ thuộc (depends_on) |
| :---: | :--- | :--- | :--- | :--- |
| 3 | **LDMS-001** | Hoàn thiện đủ AC (AC 3, 4: `.env.example`, xử lý thiếu env) | M0 · M · Must | — |
| 3–4 | **LDMS-009** | Đăng nhập môi trường dev (Mock JWT + phân quyền roles) | M8 · M · Must | LDMS-001 |
| 5 | **LDMS-010** | Kiểm soát quyền truy cập tài liệu theo role | M1+M8 · S · Must | LDMS-002, LDMS-009 |
| 6–7 | **LDMS-018** | Đăng nhập Google OAuth 2.0 | M8 · M · Should | LDMS-009 |
| 8–9 | Hạ tầng CI/CD | Nginx reverse-proxy + SSL, CI/CD GitFlow, backup PgBackRest | Hạ tầng | — |

#### B. Khoa Ngô — Epic B nhánh Pipeline (Digitization & Publish)
| Ngày | Mã Story | Nội dung công việc | Module / Size / MoSCoW | Phụ thuộc (depends_on) |
| :---: | :--- | :--- | :--- | :--- |
| 3–4 | **LDMS-003** | Hàng đợi OCR và trạng thái job (Tesseract OCR thực tế) | M2 · M · Must | LDMS-002 |
| 5–6 | **LDMS-004** | Trả kết quả OCR theo từng trang | M2 · M · Must | LDMS-003 |
| 7–8 | **LDMS-007** | Đóng gói và xuất bản file EPUB qua Pandoc | M5 · M · Must | LDMS-005 (Thái) |
| 9 | **LDMS-022** | Giao diện theo dõi trạng thái OCR và nút bấm Retry | M2 · S · Should | LDMS-003 |
| 9 | **LDMS-013** | Chặn xuất bản khi tài liệu chưa đủ metadata bắt buộc | M4+M5 · S · Must | LDMS-007, LDMS-011 |

#### C. Thái — Epic B nhánh Editorial (Biên tập & Metadata)
| Ngày | Mã Story | Nội dung công việc | Module / Size / MoSCoW | Phụ thuộc (depends_on) |
| :---: | :--- | :--- | :--- | :--- |
| 3 | **LDMS-011** | Gán metadata bắt buộc cho tài liệu (Tiêu đề, Tác giả) | M4 · S · Must | LDMS-002 |
| 4–5 | **LDMS-012** | Quản lý danh mục tài liệu Category 2 cấp | M4 · M · Must | LDMS-011 |
| 6 | **LDMS-005** | API đọc và cập nhật văn bản từng trang sau OCR | M3 · S · Must | LDMS-004 (Khoa Ngô) |
| 7–8 | **LDMS-006** | UI biên tập văn bản (Split Editor nối API thật) | M3 · M · Must | LDMS-005 |
| 9 | **LDMS-017** | Biên tập Split-screen đối soát ảnh gốc và text OCR | M3 · M · Should | LDMS-006 |

#### D. Khoa Nguyễn — Epic C (Search & Reader UX)
| Ngày | Mã Story | Nội dung công việc | Module / Size / MoSCoW | Phụ thuộc (depends_on) |
| :---: | :--- | :--- | :--- | :--- |
| 3–4 | **LDMS-019** | Tùy chỉnh giao diện đọc sách (Font, cỡ chữ, Dark/Light) | M6 · S · Should | LDMS-008 |
| 5–6 | **LDMS-015** | Tìm kiếm toàn văn tiếng Việt (PostgreSQL FTS) | M7 · M · Must | LDMS-004, LDMS-011 |
| 7 | **LDMS-016** + **020** | Snippet kết quả tìm kiếm + Đánh dấu trang (Bookmark) | M7+M6 · M · Must/Should | LDMS-015, LDMS-008 |
| 8–9 | **LDMS-008** + **014** | Đọc sách EPUB trên Web + Bảo mật DRM Signed URL 15 phút | M6 · M · Must/Should | LDMS-007, LDMS-010 |

---

## 4. Biểu quyết & Kết luận Cuộc họp

- **Kết quả biểu quyết:** **$6/6$ thành viên đồng thuận $100\%$** với Kế hoạch phân công Sprint 1 và Quy chế kỹ thuật.
- Cuộc họp kết thúc vào lúc 21:45 cùng ngày. Kế hoạch này có hiệu lực thực thi ngay lập tức.

<br>

| THƯ KÝ CUỘC HỌP | CHỦ TRÌ CUỘC HỌP / PROJECT MANAGER |
| :---: | :---: |
| *(Đã ký điện tử)* | *(Đã ký điện tử)* |
| <br><br>**Nguyễn Tuấn Anh** | <br><br>**Mạch Quốc Tấn** |

<br>

| ĐẠI DIỆN BACKEND LEAD | ĐẠI DIỆN FRONTEND LEAD | ĐẠI DIỆN KIẾN TRÚC SƯ |
| :---: | :---: | :---: |
| *(Đã ký)* | *(Đã ký)* | *(Đã ký)* |
| **Ngô Đặng Đăng Khoa** | **Nguyễn Trường Thái** | **Nguyễn Đức An** |
