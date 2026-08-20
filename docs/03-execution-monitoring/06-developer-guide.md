# HƯỚNG DẪN CÀI ĐẶT VÀ PHÁT TRIỂN CHO LẬP TRÌNH VIÊN

## Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS (HCMUS-LDMS)

### THÔNG TIN TÀI LIỆU (DOCUMENT CONTROL)

| Trường thông tin (Field)                   | Nội dung đặc tả (Description)                                      |
| :----------------------------------------- | :----------------------------------------------------------------- |
| **Mã tài liệu (Document ID)**              | `HCMUS-LDMS-DEVGUIDE`                                              |
| **Tên tài liệu (Document Title)**          | Hướng dẫn Cài đặt và Phát triển (Developer Guide)                  |
| **Dự án (Project Name)**                   | HCMUS-LDMS                                                         |
| **Đơn vị soạn thảo (Author/Organization)** | Nhóm Phát triển Dự án HCMUS-LDMS                                   |
| **Cấp độ bảo mật (Security Class)**        | Internal                                                           |
| **Trạng thái tài liệu (Status)**           | Active — khớp README và scripts hiện có                            |

### LỊCH SỬ PHIÊN BẢN (REVISION HISTORY)

| Phiên bản (Version) | Ngày phát hành (Date) | Mô tả thay đổi (Description of Change)                                      | Người thực hiện (Author) |
| :-----------------: | :-------------------: | :-------------------------------------------------------------------------- | :----------------------: |
|         1.0         |      20/08/2026       | Tách hướng dẫn dev từ root README; bổ sung CI local checklist và nhánh Git. |    Nguyễn Tuấn Anh     |

---

## 1. Mục đích

Tài liệu giúp thành viên mới (hoặc máy mới) **cài công cụ, biên dịch/chạy mã nguồn, chạy kiểm thử**, và **mở PR đúng cổng CI**. Nội dung bám đúng những gì repo đã hỗ trợ — không mô tả pipeline deploy VMware tự động (xem [07-deployment-guide.md](./07-deployment-guide.md)).

---

## 2. Yêu cầu công cụ

| Công cụ | Phiên bản tối thiểu | Ghi chú |
| ------- | ------------------- | ------- |
| Docker + Docker Compose plugin | Docker 24.x khuyến nghị | Bắt buộc cho Postgres, MinIO, API image |
| Node.js | 20+ | Frontend Vite/React |
| npm | Đi kèm Node 20 | Dùng `npm ci` / `npm install` |
| [uv](https://docs.astral.sh/uv/) | Latest ổn định | Quản lý Python 3.11 backend |
| Git | 2.x | Nhánh theo GitFlow |
| curl | Có sẵn hầu hết OS | Health check trong `scripts/run.sh` |

Tùy chọn:

- `openssl` — tạo cert self-signed cho profile `prod` (`scripts/generate-dev-cert.sh`).

---

## 3. Lấy mã nguồn và cấu hình

```bash
git clone <URL-repo-nhóm>
cd hcmus-projectmanage--lab

# Backend env
cp src/backend/.env.example src/backend/.env
# Chỉnh JWT_SECRET, Google OAuth (nếu không dùng mock auth), v.v.
```

Kiểm tra file `.env` không commit secret thật lên Git.

---

## 4. Chạy môi trường phát triển

### 4.1 Một lệnh (khuyến nghị)

Từ thư mục gốc repo:

```bash
./scripts/run.sh
```

Script sẽ:

1. `docker compose up -d --build` (API + PostgreSQL + MinIO) theo `src/backend/docker-compose.yml`.
2. Chờ `GET http://localhost:8000/health` tối đa ~60 giây.
3. Chạy `alembic upgrade head` trong container API.
4. Chạy frontend `npm run dev` (cài `npm ci` nếu lockfile mới hơn `node_modules`).

Dừng bằng `Ctrl+C` (script dừng frontend và `compose down`).

### 4.2 Chạy tách bước (debug)

```bash
# Backend stack
cd src/backend
cp .env.example .env   # nếu chưa có
docker compose up -d --build
docker compose exec api uv run --no-dev alembic upgrade head

# Frontend (terminal khác)
cd src/frontend
npm ci
npm run dev
```

### 4.3 Cổng dịch vụ (dev)

| Service | URL |
| ------- | --- |
| Frontend (Vite) | http://localhost:5173 |
| API | http://localhost:8000 |
| PostgreSQL (host) | localhost:**5434** |
| MinIO API (host) | localhost:**9002** |
| MinIO Console | localhost:**9003** |

> Cổng map ra host khác cổng trong container để tránh đụng Postgres/MinIO local khác.

---

## 5. Biên dịch và kiểm tra chất lượng (giống CI)

Trước khi mở PR, chạy cùng tập lệnh với `.github/workflows/ci.yml`:

### 5.1 Backend

```bash
cd src/backend
uv sync
uv run ruff format --check .
uv run ruff check .
uv run pytest
```

Sửa format:

```bash
uv run ruff format .
```

### 5.2 Frontend

```bash
cd src/frontend
npm ci
npm run lint
npm run build
npm test
```

### 5.3 Ý nghĩa từng bước

| Bước | Mục đích |
| ---- | -------- |
| Ruff format/check | Thống nhất style Python; chặn merge nếu lệch |
| Pytest | ~141 test API/service/worker/core |
| ESLint + `npm run build` | Type/lint + bundle production FE |
| Vitest | Regression UI/component |

CI cũng chạy các bước trên khi mở PR vào `main` / `develop`, hoặc push các nhánh `main`, `develop`, `release/**`, `hotfix/**`.

---

## 6. Migration cơ sở dữ liệu

Mọi thay đổi schema phải qua **Alembic**:

```bash
cd src/backend
# Tạo revision (máy có kết nối DB / trong container)
docker compose exec api uv run --no-dev alembic revision --autogenerate -m "mo_ta_ngan"

# Áp dụng
docker compose exec api uv run --no-dev alembic upgrade head
```

Import model mới vào `app/db/migrations/env.py` nếu autogenerate không nhận diện. Chi tiết thêm trong root README.

**Bắt buộc** `upgrade head` trước khi gọi API upload tài liệu trên môi trường mới.

---

## 7. Nhánh Git và quy trình PR

Theo [`02-architecture.md`](../02-planning/02-architecture.md) §8.2 (GitFlow):

| Nhánh | Mục đích |
| ----- | -------- |
| `feature/*` | Tính năng từ `develop` |
| `develop` | Tích hợp sprint |
| `release/*` | Chuẩn bị phát hành / UAT |
| `main` | Ổn định nhất |
| `hotfix/*` | Sửa khẩn từ `main` |

Checklist trước khi nhờ review:

1. AC story đã tự kiểm trên UI/API.
2. Test liên quan đã thêm/cập nhật.
3. Các lệnh mục 5 xanh local.
4. PR description nêu story ID / thay đổi.
5. Sau merge: ghi log effort vào [`02-project-log.md`](./02-project-log.md) nếu story Done (DoD).

Khi **push lên `main`**, job CI `notify` gửi email Brevo tới danh sách `.github/ci-notify-recipients.txt` (cần secret `BREVO_*` trên GitHub).

---

## 8. Xác thực khi dev

- Mặc định Compose có thể bật `ENABLE_MOCK_AUTH` / endpoint dev-token để lấy JWT theo role (`editor`, `admin`, `reader`) — dùng trong test và demo local.
- Google OAuth: cấu hình `GOOGLE_CLIENT_ID`, `GOOGLE_CLIENT_SECRET`, `GOOGLE_REDIRECT_URI`, `GOOGLE_ALLOWED_DOMAINS` trong `.env`.

Chi tiết luồng auth xem root README mục xác thực.

---

## 9. Cấu trúc thư mục liên quan dev

```
hcmus-projectmanage--lab/
├── scripts/run.sh                 # One-shot dev stack
├── .github/workflows/ci.yml       # Cổng CI
├── src/backend/                   # FastAPI, Dockerfile, compose, alembic, tests/
├── src/frontend/                  # React + Vite + Vitest
└── samples/                       # PDF mẫu không bản quyền cho smoke OCR
```

---

## 10. Sự cố thường gặp

| Triệu chứng | Hướng xử lý |
| ----------- | ----------- |
| `run.sh` báo API không ready trong 60s | `docker compose -f src/backend/docker-compose.yml logs --tail 80 api` |
| Pytest fail liên quan DB | Đảm bảo không phụ thuộc Postgres thật; kiểm tra fixture `api_context` |
| Frontend port 5173 bận | Tắt process cũ; `run.sh` cố gắng `fuser -k 5173/tcp` nếu có `fuser` |
| OCR không chạy | Image API phải build đủ Tesseract/Poppler/Pandoc; xem Dockerfile backend |
| Migration chưa chạy | `docker compose exec api uv run --no-dev alembic upgrade head` |

---

## 11. Tài liệu liên quan

- Root [`README.md`](../../README.md) — nghiệp vụ API, OCR, bảo mật Signed URL.
- [`07-deployment-guide.md`](./07-deployment-guide.md) — triển khai prod-like / vận hành.
- [`09-test-plan.md`](../02-planning/09-test-plan.md) — chiến lược kiểm thử.
