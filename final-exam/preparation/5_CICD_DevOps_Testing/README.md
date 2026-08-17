# ĐỀ CƯƠNG ÔN TẬP — NGƯỜI 5: CI/CD, DEVOPS & KẾ HOẠCH KIỂM THỬ

- **Phạm vi phụ trách:** **Câu 13, Câu 14, Câu 15, Câu 20**
- **Tài liệu tham chiếu chính trong dự án:**
  - [`docs/02-planning/02-architecture.md`](../../docs/02-planning/02-architecture.md) (Mục 8.2: GitFlow & Deploy)
  - File cấu hình `docker-compose.yml`, Dockerfile trong [`src/backend/`](../../src/backend/)
  - Bộ test suite trong [`src/backend/tests/`](../../src/backend/tests/)
- **Hạn chót hoàn thành đề cương (Bước 1):** **20:00, Thứ Năm (20/08/2026)**
- **Bản in cần nộp kèm khi thi:** Bản in Sơ đồ Luồng GitFlow/CI/CD, File `docker-compose.yml` (profile `prod`) và Kết quả chạy test `pytest`.

---

## CÂU 13: MÔ HÌNH TÍCH HỢP LIÊN TỤC (CONTINUOUS INTEGRATION — CI)

> **Câu hỏi chính:** Vẽ và giải thích mô hình tích hợp liên tục (CI) của nhóm. Ghi chú trên mô hình các công cụ nhóm đã dùng.

### 1. Dàn ý trả lời & Sơ đồ:
* **Mô hình luồng CI của nhóm:**
```
[Dev Workspace] ──(git push)──> [GitHub Repository]
       │                                │ (Trigger Workflow)
       ▼                                ▼
[Linting: Ruff / ESLint] ──> [Format check: Prettier] ──> [Automated Tests: Pytest / Vitest]
                                                                  │
                                                          (All Passed )
                                                                  ▼
                                                      [Allow Merge Pull Request]
```
* **Giải thích:** Mỗi khi dev tạo PR vào nhánh `develop`, hệ thống CI tự động kích hoạt kiểm tra chất lượng: Linting backend (`ruff check`), frontend (`npm run lint`), format code và chạy toàn bộ Unit test backend (`pytest`). Nếu có bất kỳ test nào fail, PR bị chặn merge.
* **Công cụ nhóm sử dụng:** Git, GitHub Actions, Ruff (Python linter), ESLint, Pytest, Docker build validator.

---

## CÂU 14: MÔ HÌNH CHUYỂN GIAO LIÊN TỤC (CONTINUOUS DELIVERY — CD)

> **Câu hỏi chính:** Vẽ và giải thích mô hình chuyển giao liên tục (CD) của nhóm. Ghi chú trên mô hình các công cụ nhóm đã dùng.

### 1. Dàn ý trả lời & Sơ đồ:
* **Mô hình luồng CD của nhóm:**
```
[Merged into 'main'] ──> [Build Production Images] ──> [Run Database Migrations]
                                │ (alembic upgrade head)
                                ▼
[Deploy Production Containers: API + PostgreSQL + MinIO + Nginx Reverse Proxy (TLS 1.3)]
                                │
                                ▼
                [Health Check: GET /health -> 200 OK]
```
* **Giải thích:** Khi code được merge vào nhánh `main`, hệ thống tự động build Docker image chứa toàn bộ dependency (Tesseract, Pandoc, Poppler), chạy migration database tự động (`alembic upgrade head`), và khởi chạy profile `prod` với Nginx đóng gói web tĩnh và cấp phát chứng chỉ TLS an toàn.

---

## CÂU 15: MÔ HÌNH DEVOPS

> **Câu hỏi chính:** Vẽ và giải thích mô hình DevOps của nhóm. Ghi chú trên mô hình các công cụ nhóm đã dùng.

### 1. Dàn ý trả lời & Sơ đồ:
* **Vòng lặp DevOps 8 giai đoạn:**
  1. **Plan:** GitHub Issues, Kanban Backlog (`03-product-backlog.md`).
  2. **Code:** VS Code, Cursor, Antigravity AI, Claude Code.
  3. **Build:** uv (Python packaging), Vite (Frontend bundling), Docker.
  4. **Test:** Pytest, Vitest, Playwright (UI testing).
  5. **Release:** Git tag releases (`v1.0.0-MVP`).
  6. **Deploy:** Docker Compose (Service API, DB, MinIO, Nginx).
  7. **Operate:** MinIO Console UI (quản trị object storage), Port 5434 PostgreSQL.
  8. **Monitor & Backup:** Scripts sao lưu tự động `scripts/backup-postgres.sh` (pg_dump nén) và `scripts/backup-minio.sh` (mc mirror đồng bộ).

---

## CÂU 20: KẾ HOẠCH KIỂM THỬ (TEST PLAN)

> **Câu hỏi chính:** Trình bày quá trình hình thành và phương pháp đánh giá tài liệu Kế hoạch kiểm thử của nhóm.

### 1. Dàn ý trả lời:
* **WHAT:** Kế hoạch bao quát các cấp độ kiểm thử: Unit Test (các hàm tiện ích, parser), Integration Test (API Router + Database Session + MinIO mock), Security Test (xác thực JWT, RBAC 403 forbidden, signed URL expiry 15 phút), và Smoke Test.
* **HOW:** Viết test song song cùng quá trình sinh mã bằng AI, sử dụng `pytest` với fixtures độc lập, kiểm tra mọi trường hợp biên (tải file sai extension, upload file lỗi, sửa text page rỗng, trùng lặp category).
* **EVIDENCE:** 100% test pass khi chạy `uv run pytest` và `npm test` trước khi đóng gói bản nộp.
