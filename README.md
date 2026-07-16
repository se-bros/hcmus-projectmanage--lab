# HCMUS-LDMS

Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS.

## Yêu cầu

- Docker & Docker Compose
- Node.js 20+
- [uv](https://docs.astral.sh/uv/) (Python package manager)

## Chạy local

Chạy toàn bộ PostgreSQL, MinIO, API và frontend bằng một lệnh:

```bash
./scripts/run.sh
```

Nhấn `Ctrl+C` để dừng. Script chỉ tự động dừng Compose nếu chính nó đã khởi tạo
các container; các service Compose có sẵn sẽ được giữ nguyên.

Hoặc chạy từng phần thủ công:

```bash
# Backend + PostgreSQL + MinIO
cd src/backend
cp .env.example .env
docker compose up -d --build
docker compose exec api uv run --no-dev alembic upgrade head

# Frontend (chạy riêng, không nằm trong compose)
cd src/frontend
npm install
npm run dev
```

| Service | URL |
| --- | --- |
| Frontend (Vite dev server) | http://localhost:5173 |
| API | http://localhost:8000 |
| PostgreSQL | localhost:5434 |
| MinIO API | localhost:9002 |
| MinIO Console UI | localhost:9003 |

> Cổng PostgreSQL/MinIO được map ra ngoài container ở các số khác mặc định 5434, 9002, 9003

Migration phải được áp dụng bằng `alembic upgrade head` trước khi gọi API upload tài liệu.

## Luồng số hóa và xuất bản

Backend chỉ nhận PDF, JPG/JPEG và PNG khi extension, `Content-Type` và magic bytes cùng khớp.
Upload trả ngay `document_id`, tự tạo OCR job nền, render preview PNG theo trang và nhận dạng với
Tesseract `vie+eng`. Docker image đã chứa Tesseract, Poppler và Pandoc.

Các endpoint chính:

| Method | Endpoint | Kết quả |
| --- | --- | --- |
| `POST` | `/documents` | Lưu source, tạo OCR job, trả `201 {document_id}` |
| `GET` | `/documents/{id}/source` | Stream bytes source gốc |
| `POST` | `/documents/{id}/ocr` | Retry job failed, trả job mới với HTTP 202 |
| `GET` | `/documents/{id}/ocr` | Job mới nhất, attempt, status và lỗi |
| `GET` | `/documents/{id}/pages` | Text theo `page_number` tăng dần |
| `GET` | `/documents/{id}/pages/{n}` | Đọc text và trạng thái preview của một trang |
| `PUT` | `/documents/{id}/pages/{n}` | Lưu `{ "text_content": "..." }`, kể cả chuỗi rỗng |
| `GET` | `/documents/{id}/pages/{n}/image` | Preview PNG của trang |
| `PUT` | `/documents/{id}/metadata` | Lưu title, author, shelf location và category |
| `POST` | `/categories` | Tạo category cấp 1 hoặc cấp 2 bằng `parent_id` |
| `GET` | `/categories` | Trả cây category hai cấp với mảng `children` |
| `PATCH` | `/categories/{id}` | Đổi tên category |
| `DELETE` | `/categories/{id}` | Xóa category không có con và chưa được sử dụng |
| `GET` | `/ocr/jobs` | Job OCR mới nhất của từng document cho dashboard |
| `POST` | `/documents/{id}/publish` | Kiểm tra metadata/page text và tạo publish job |
| `GET` | `/documents/{id}/publish` | Publish job mới nhất |

Các trạng thái document gồm `ocr_pending`, `ocr_processing`, `ocr_completed`, `ocr_failed`,
`publishing`, `published` và `publish_failed`. Job `pending`/`processing` bị gián đoạn bởi API
restart được đánh dấu `failed` để người dùng retry, thay vì treo vô thời hạn.

### Chạy lại Acceptance Criteria OCR

Repo có sample tự sinh, không dùng nội dung có bản quyền tại [`samples/`](samples/README.md).
Sau khi chạy `./scripts/run.sh`, mở terminal khác:

```bash
curl -fsS -F file=@samples/two-page.pdf http://localhost:8000/documents

# Thay DOCUMENT_ID bằng id vừa nhận; polling đến completed
curl -fsS http://localhost:8000/documents/DOCUMENT_ID/ocr
curl -fsS http://localhost:8000/documents/DOCUMENT_ID/pages
curl -fsS -o /tmp/page-1.png \
  http://localhost:8000/documents/DOCUMENT_ID/pages/1/image
```

PDF phải trả hai page không trùng số, theo thứ tự `1, 2`; PNG trả một page. UI tại
`http://localhost:5173` tự polling mỗi 2 giây, hiện lỗi worker và cung cấp nút **Thử lại OCR**.
Dashboard tại `http://localhost:5173/dashboard` tổng hợp số job theo trạng thái, thời điểm cập nhật,
error message và cho phép retry trực tiếp từng tài liệu lỗi.

Trang `http://localhost:5173/documents` hiển thị kho tài liệu scan với tìm kiếm và bộ lọc trạng
thái. Chọn một tài liệu sẽ mở `/documents/{document_id}`, nơi có form metadata/category và editor
split-screen. Ảnh preview và textarea OCR chuyển trang đồng bộ; editor hiển thị trạng thái đang
lưu/đã lưu/lỗi và hỏi xác nhận trước khi bỏ nội dung chưa lưu. Trang thiếu preview vẫn có
placeholder và textarea hoạt động bình thường. Quản trị cây hai cấp tại
`http://localhost:5173/categories`; RBAC sẽ được nối sau khi LDMS-009/010 cung cấp dependency xác
thực.

Publish yêu cầu `Document.title`, `Document.author` và text không rỗng trên mọi page. Có thể chạy
smoke flow metadata/category/editor hoàn toàn qua API:

```bash
# Tạo category cha rồi category con; thay các ID từ response vào lệnh sau
curl -fsS -X POST http://localhost:8000/categories \
  -H 'Content-Type: application/json' \
  -d '{"name":"Khoa học","parent_id":null}'
curl -fsS -X POST http://localhost:8000/categories \
  -H 'Content-Type: application/json' \
  -d '{"name":"Vật lý","parent_id":"PARENT_CATEGORY_ID"}'

curl -fsS -X PUT http://localhost:8000/documents/DOCUMENT_ID/metadata \
  -H 'Content-Type: application/json' \
  -d '{"title":"OCR Sample","author":"HCMUS LDMS","shelf_location":"A-12","category_id":"CHILD_CATEGORY_ID"}'
curl -fsS http://localhost:8000/documents/DOCUMENT_ID/pages/1
curl -fsS -X PUT http://localhost:8000/documents/DOCUMENT_ID/pages/1 \
  -H 'Content-Type: application/json' \
  -d '{"text_content":"Corrected OCR page text"}'
curl -fsS http://localhost:8000/documents/DOCUMENT_ID/pages/1
curl -fsS -X POST http://localhost:8000/documents/DOCUMENT_ID/publish
curl -fsS http://localhost:8000/documents/DOCUMENT_ID/publish
```

Reload `/documents/DOCUMENT_ID` sau lệnh PUT phải thấy text đã sửa. Thử title/author chỉ chứa
whitespace phải nhận `422` chỉ rõ field; gán category UUID không tồn tại phải nhận `404`; xóa
category có con hoặc đang được document dùng phải nhận `409`.

Publish thành công lưu EPUB ở key
`documents/{document_id}/epub/{publish_job_id}.epub`. Worker kiểm tra ZIP/container, title,
author và thứ tự text trong spine trước khi cập nhật document thành `published`.

## Cấu trúc thư mục

```
src/
├── frontend/                  # React 19 + TypeScript, khởi tạo bằng `npm create vite`
│   └── src/{components,pages,services,context,utils}
└── backend/                   # FastAPI, quản lý bằng uv
    ├── docker-compose.yml     # API + PostgreSQL + MinIO
    ├── alembic.ini            # Config Alembic — url thật lấy từ .env, không sửa ở đây
    ├── .env.example
    ├── app/
    │   ├── main.py             # App factory — wiring only, không chứa business logic
    │   ├── core/
    │   │   ├── config.py       # Settings (đọc .env qua pydantic-settings)
    │   │   ├── security.py     # JWT/OAuth helpers — chưa implement (LDMS-009/018)
    │   │   ├── logging.py      # configure_logging()
    │   │   └── exceptions.py   # AppError hierarchy + exception handler dùng chung
    │   ├── db/
    │   │   ├── base.py         # Declarative Base dùng chung cho models
    │   │   ├── session.py      # engine + get_db dependency
    │   │   └── migrations/     # Alembic (env.py đã trỏ vào Base.metadata + settings)
    │   ├── api/                 # 1 router/module nghiệp vụ, xem bảng bên dưới
    │   │   └── dependencies.py  # Dependency dùng chung giữa các router (DbSession, ...)
    │   ├── middleware/          # Custom middleware (vd. CORS setup) — cors.py
    │   ├── models/              # Document, OCR/Page và PublishJob models
    │   ├── repositories/        # Data-access layer trên models
    │   ├── schemas/             # Request/response schemas
    │   ├── services/            # Upload, OCR và publish business rules
    │   ├── workers/             # FastAPI BackgroundTasks cho OCR/EPUB
    │   └── utils/               # Helper dùng chung khi có
    └── tests/
        ├── conftest.py
        └── api/                 # Test theo từng router
```

Quy ước:
- Model/schema/service/repository cũng tách 1 file/entity hoặc module tương ứng (vd. `models/document.py`, `repositories/document_repository.py`, `services/ocr.py`) — tránh dồn hết vào 1 file dùng chung.
- Lỗi nghiệp vụ raise bằng các exception trong `core/exceptions.py` (`NotFoundError`, `ConflictError`, ...) thay vì tự trả `JSONResponse` — handler dùng chung đã đăng ký sẵn trong `main.py`.
- Migration: `uv run alembic revision --autogenerate -m "..."` rồi `uv run alembic upgrade head` (cần import model mới vào `app/db/migrations/env.py` để autogenerate nhận diện).
- Format trước khi commit: `uv run ruff format .` (backend), `npm run format` (frontend).
- Lint: `uv run ruff check .` (backend), `npm run lint` (frontend).
- Test backend: `uv run pytest`.
- Regression frontend: `npm test && npm run lint && npm run build`.
- Kiểm tra migration PostgreSQL: `cd src/backend && docker compose exec api uv run --no-dev alembic upgrade head`.
- Nhánh Git theo GitFlow (`feature/*` → `develop` → `release/*` → `main`), xem `docs/06-architecture.md` §8.2.

## Tài liệu liên quan

- `docs/07-product-backlog.md` — backlog & AC
- `docs/06-architecture.md` — kiến trúc & tech stack
- `docs/09-plan.md` — phân công
