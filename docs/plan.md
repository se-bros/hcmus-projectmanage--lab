# KẾ HOẠCH SPRINT 1 — PHÂN CÔNG CÔNG VIỆC

## Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS (HCMUS-LDMS)

### THÔNG TIN TÀI LIỆU (DOCUMENT CONTROL)

| Trường thông tin (Field) | Nội dung đặc tả (Description) |
| :--- | :--- |
| **Mã tài liệu (Document ID)** | `HCMUS-LDMS-SPR1` |
| **Tên tài liệu (Document Title)** | Kế hoạch Sprint 1 — Phân công công việc theo Epic |
| **Dự án (Project Name)** | HCMUS-LDMS |
| **Nguồn backlog** | `docs/07-product-backlog.md` (mọi story tham chiếu dưới đây được pick trực tiếp từ đó) |
| **Nhóm phát triển** | Thái, Tuấn Anh, Khoa Ngô, Khoa Nguyễn (4 kỹ sư fullstack) |
| **Trạng thái tài liệu (Status)** | Ready for Sprint |

---

## 1. Tổng quan Sprint

* **Thời lượng:** 9 ngày.
* **Mốc 1 (Ngày 1–2, 17/07):** Bản chạy được đơn giản — luồng cơ bản đi xuyên suốt (upload → xem tài liệu), **chưa cần đạt đủ Acceptance Criteria (AC)**.
* **Mốc 2 (Ngày 3–9, 24/07):** Hoàn thiện đủ AC/DoD cho toàn bộ story từ backlog.
* **Scope:** 16 story **Must-have** + 1 story **Should-have** (LDMS-018, được kéo sớm vào sprint để cân bằng effort giữa 4 người) = **17 story / 22 story tổng của scope tuần này** *(xem mục 5 — 6 story Should còn lại cũng được xếp lịch nếu còn dư effort)*.
* **Quy tắc làm việc:** Mỗi người tự triển khai **cả API (FastAPI) lẫn UI (React)** cho story của mình — không tách riêng người code BE / người code FE. WIP = 1 card/người theo đúng quy tắc Kanban của backlog (§1.1).

---

## 2. Phân công Epic

| Người | Thiên hướng | Epic / Cụm đảm nhiệm | Story pick từ backlog |
| :--- | :--- | :--- | :--- |
| **Tuấn Anh** | Backend | **Epic D + Epic A** — Platform & Identity | LDMS-001, LDMS-009, LDMS-010, LDMS-018 |
| **Khoa Ngô** | Backend | **Epic B (nhánh Pipeline)** — Digitization & Publish | LDMS-002, LDMS-003, LDMS-004, LDMS-007, LDMS-022, LDMS-013 |
| **Thái** | Frontend | **Epic B (nhánh Editorial)** — Biên tập & Metadata | LDMS-005, LDMS-006, LDMS-011, LDMS-012, LDMS-017 |
| **Khoa Nguyễn** | Frontend | **Epic C** — Search & Reader UX | LDMS-008, LDMS-014, LDMS-015, LDMS-016, LDMS-019, LDMS-020, LDMS-026 |


---

## 3. Mốc 1 — Ngày 1–2: Bản chạy được đơn giản

Ngày 1: thống nhất data model tối thiểu (`Document`, `Page`, `User`, `Category`) và cấu trúc thư mục monorepo `/frontend`, `/backend` theo `06-architecture.md` (§7.1–7.2).

| Người | Story pick (bản rút gọn) | Việc làm cụ thể |
| :--- | :--- | :--- |
| **Tuấn Anh** | **LDMS-001** (rút gọn — chỉ cần AC 1+2) | setup codebase, `docker-compose` cho API + PostgreSQL + MinIO; `GET /health` trả 200. Đây là việc chặn cả nhóm, làm trước tiên. |
| **Khoa Ngô** | **LDMS-002** (rút gọn — AC 1+3, bỏ qua AC lỗi/edge-case) | Endpoint upload lưu file vào MinIO + form upload React tối giản, tự code cả 2 lớp. |
| **Thái** | Chuẩn bị cho **LDMS-006** (chưa chính thức pick, chỉ dựng khung) | Scaffold khung FE dùng chung (routing, layout) + màn Editor dựng trên **dữ liệu giả (fixture text)**, vì LDMS-005/006 thật còn phụ thuộc LDMS-004 chưa xong. |
| **Khoa Nguyễn** | Chuẩn bị cho **LDMS-008** và **LDMS-026** | Trang Reader/Search placeholder đọc text thô từ fixture; danh sách tài liệu tạm thời gọi `GET /documents`. |

**Kết quả cuối Ngày 2:** đóng gói service được → upload file → thấy trong danh sách → mở xem text (giả lập). Luồng chạy xuyên suốt, chưa cần đủ AC.

---

## 4. Mốc 2 — Ngày 3–9: Hoàn thiện AC/DoD

### Tuấn Anh — Epic D + A (Platform & Identity)

| Ngày | Story | Module / Size / MoSCoW | depends_on |
| :---: | :--- | :--- | :--- |
| 3 | **LDMS-001** hoàn thiện đủ AC (AC 3, 4: `.env.example`, xử lý lỗi thiếu env) | M0 · M · Must | — |
| 3–4 | **LDMS-009** Đăng nhập dev (Mock JWT + roles) | M8 · M · Must | LDMS-001 |
| 5 | **LDMS-010** Kiểm soát quyền truy cập tài liệu | M1+M8 · S · Must | LDMS-002, LDMS-009 |
| 6–7 | **LDMS-018** Đăng nhập Google OAuth 2.0 | M8 · M · Should | LDMS-009 |
| 8–9 | Hạ tầng bổ sung (không phải story backlog, nhưng thuộc phạm vi Platform theo `06-architecture.md` §4.2, §5, §8.2): Nginx reverse-proxy + SSL, CI/CD theo GitFlow, script backup PgBackRest/Restic. Buffer hỗ trợ Khoa Ngô nếu pipeline trễ. | — | — |

### Khoa Ngô — Epic B nhánh Pipeline (Digitization & Publish)

| Ngày | Story | Module / Size / MoSCoW | depends_on |
| :---: | :--- | :--- | :--- |
| 3–4 | **LDMS-003** Hàng đợi OCR và trạng thái job (tích hợp Tesseract thật, thay bản giả lập Ngày 1–2) | M2 · M · Must | LDMS-002 |
| 5–6 | **LDMS-004** Kết quả OCR theo từng trang | M2 · M · Must | LDMS-003 |
| 7–8 | **LDMS-007** Đóng gói & xuất EPUB (Pandoc) | M5 · M · Must | LDMS-005 (Thái) |
| 9 | **LDMS-022** UI trạng thái OCR + retry | M2 · S · Should | LDMS-003 |
| 9 | **LDMS-013** Chặn xuất bản khi thiếu metadata | M4+M5 · S · Must | LDMS-007, LDMS-011 (Thái) |


### Thái — Epic B nhánh Editorial (Biên tập & Metadata)

| Ngày | Story | Module / Size / MoSCoW | depends_on |
| :---: | :--- | :--- | :--- |
| 3 | **LDMS-011** Gán metadata bắt buộc (không phụ thuộc pipeline, làm sớm) | M4 · S · Must | LDMS-002 |
| 4–5 | **LDMS-012** Quản lý Category (2 cấp) | M4 · M · Must | LDMS-011 |
| 6 | **LDMS-005** API đọc và cập nhật text trang (tích hợp thật khi LDMS-004 xong) | M3 · S · Must | LDMS-004 (Khoa Ngô) |
| 7–8 | **LDMS-006** UI biên tập text (nối API thật vào khung đã dựng sẵn Ngày 1–2 — nhanh hơn vì đã chuẩn bị trước) | M3 · M · Must | LDMS-005 |
| 9 | **LDMS-017** Biên tập Split-screen (ảnh + text) | M3 · M · Should | LDMS-006 |

### Khoa Nguyễn — Epic C (Search & Reader UX)

| Ngày | Story | Module / Size / MoSCoW | depends_on |
| :---: | :--- | :--- | :--- |
| 3–4 | **LDMS-019** Tùy chỉnh giao diện đọc sách (không phụ thuộc EPUB thật, làm sớm trên khung Reader placeholder) | M6 · S · Should | LDMS-008 |
| 5–6 | **LDMS-015** Tìm kiếm toàn văn (PostgreSQL FTS) | M7 · M · Must | LDMS-004 (Khoa Ngô), LDMS-011 (Thái) |
| 7 | **LDMS-016** Snippet kết quả và mở reader + **LDMS-020** Đánh dấu trang (Bookmark) | M7 · S · Must / M6 · M · Should | LDMS-015, LDMS-008 / LDMS-009 (Tuấn Anh), LDMS-008 |
| 8–9 | **LDMS-008** Đọc sách EPUB trên web + **LDMS-014** Giảm rủi ro tải file gốc khi đọc + **LDMS-026** Danh sách tài liệu (hoàn thiện đủ AC) | M6 · M · Must / M6 · M · Should / M1+M3 · M · Must | LDMS-007 (Khoa Ngô) / LDMS-008, LDMS-010 (Tuấn Anh) / LDMS-002, LDMS-006 (Thái) |

---
