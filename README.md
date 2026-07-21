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
`http://localhost:5173/categories`; backend RBAC/`is_public` guard (LDMS-009/010, xem mục "Xác
thực & Phân quyền" bên dưới) đã sẵn sàng — các trang FE hiện chưa gắn `Authorization` header vào
những call này, sẽ nối khi module tương ứng cập nhật.

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

## Xác thực & Phân quyền (LDMS-009, LDMS-010, LDMS-018)

Hệ thống hỗ trợ song song 2 cách đăng nhập, dùng chung một bảng `users` và một
tập role (`reader` | `editor` | `admin`): đăng ký/đăng nhập bằng email+mật khẩu,
và đăng nhập Google OAuth. Tài khoản mới (dù tạo qua cách nào) đều mặc định
role `reader`; nâng quyền lên `editor`/`admin` hiện là thao tác thủ công trên
DB (`UPDATE users SET role = 'editor' WHERE email = '...'`).

`ENABLE_MOCK_AUTH` trong `.env` (mặc định `true`) bật/tắt endpoint dev-token
dùng riêng cho test RBAC nhanh, độc lập với đăng nhập thật:

```bash
curl -fsS -X POST http://localhost:8000/auth/dev-token -H 'Content-Type: application/json' \
  -d '{"role":"editor"}'
curl -fsS -X POST http://localhost:8000/auth/dev-token -H 'Content-Type: application/json' \
  -d '{"role":"reader"}'
curl -fsS -X POST http://localhost:8000/auth/dev-token -H 'Content-Type: application/json' \
  -d '{"role":"admin"}'
```

Đăng ký / đăng nhập bằng email + mật khẩu (mặc định nhận mọi domain email —
xem `GOOGLE_ALLOWED_DOMAINS` bên dưới; mật khẩu tối thiểu 8 ký tự):

```bash
curl -fsS -X POST http://localhost:8000/auth/register -H 'Content-Type: application/json' \
  -d '{"email":"student@hcmus.edu.vn","password":"supersecret"}'
curl -fsS -X POST http://localhost:8000/auth/login -H 'Content-Type: application/json' \
  -d '{"email":"student@hcmus.edu.vn","password":"supersecret"}'
curl -fsS -X POST http://localhost:8000/auth/logout
```

`POST /auth/logout` không giữ trạng thái phía server — trả `204`, việc "đăng
xuất" thực tế là FE xoá token khỏi `localStorage`.

Gắn token vào header `Authorization: Bearer <token>`. RBAC theo role:

* **`reader`**: chỉ đọc. Mọi endpoint ghi (`POST /documents`, `POST
  .../ocr`, `PUT .../metadata`, `PUT .../pages/{n}`, `POST /documents/{id}/publish`,
  `POST/PATCH/DELETE /categories`) trả `403`.
* **`editor`**: `POST /documents` (upload) và `POST .../ocr` (chạy/chạy lại
  OCR) cho phép trên mọi document. `PUT .../metadata` và `PUT .../pages/{n}`
  chỉ cho phép trên document do chính editor đó upload (`document.owner_id`
  khớp `sub` trong JWT) — document của người khác trả `403` giống hệt
  reader. `/categories` (tạo/sửa/xoá) vẫn `403` với editor.
* **`admin`**: full access mọi endpoint, không bị ràng buộc ownership.

Không có token (guest) → `401` trên mọi endpoint ghi. `GET /categories` là
ngoại lệ luôn mở, không cần token, vì đây chỉ là dữ liệu tham chiếu cho
dropdown category trong metadata form.

Document được set `owner_id` = `sub` của người upload tại thời điểm tạo;
document tạo trước khi có field này có `owner_id = NULL` nên chỉ `admin` sửa
được.

Document có field `is_public` (mặc định `false`). Guest (không token) chỉ đọc
được document `is_public = true`; ngược lại `GET /documents/{id}` và
`.../source` trả `401`. Đặt một document thành public để test thủ công:

```bash
docker compose exec postgres psql -U ldms -d ldms \
  -c "UPDATE documents SET is_public = true WHERE id = 'DOCUMENT_ID';"
```

### Google OAuth 2.0 (LDMS-018)

Đặt `GOOGLE_CLIENT_ID`, `GOOGLE_CLIENT_SECRET`,
`GOOGLE_REDIRECT_URI=http://localhost:8000/auth/callback/google` trong `.env`
(lấy từ [Google Cloud Console](https://console.cloud.google.com/apis/credentials)
— thêm redirect URI trên vào danh sách Authorized redirect URIs của OAuth
Client) để bật `/auth/login/google`. Không cần tắt gì khác — Google OAuth và
đăng nhập email/mật khẩu luôn chạy song song; thiếu 1 trong 3 biến trên thì
`/auth/login/google` trả `404`.

Luồng: mở `http://localhost:5173/login` → bấm "Đăng nhập với Google" → consent screen Google →
callback về BE → BE tìm hoặc tạo user theo email (role mặc định `reader` nếu
là user mới) → redirect FE tới `/auth/callback?token=...` → FE lưu token vào
`localStorage`.

`GOOGLE_ALLOWED_DOMAINS` (JSON array trong `.env`) giới hạn domain email được
phép — áp dụng cho cả Google login lẫn đăng ký email/mật khẩu. Mặc định `[]`
(rỗng) = **không giới hạn**, mọi email public (gmail.com, ...) đều đăng
ký/đăng nhập được. Đặt vd. `["hcmus.edu.vn","clc.fitus.edu.vn"]` nếu muốn chỉ
chấp nhận email trường — email ngoài danh sách bị từ chối với `403`.

Nếu một email đã đăng ký bằng mật khẩu trước đó đăng nhập lại bằng Google (hoặc
ngược lại), hệ thống dùng lại đúng identity/role cũ — không tạo user trùng.

**Bảo mật:** `GOOGLE_CLIENT_SECRET`/`JWT_SECRET` chỉ đọc từ `.env` (gitignored),
không hardcode trong repo.

### Hồ sơ cá nhân & Yêu cầu nâng quyền

`GET /auth/me` trả profile (`email`, `username`, `role`, `auth_provider`,
`has_password`); `PATCH /auth/me` đổi `username`; `POST /auth/change-password`
đổi mật khẩu (`current_password` bắt buộc nếu tài khoản đã có mật khẩu —
tài khoản Google-only chưa có mật khẩu thì bỏ qua field này). Tài khoản đăng
nhập qua `/auth/dev-token` (mock) không có bản ghi `users` thật nên `GET
/auth/me` trả profile "tổng hợp" từ JWT (`username = null`, `has_password =
false`), còn `PATCH /auth/me`/`change-password` trả `404`.

`POST /role-requests` cho phép role `reader` gửi yêu cầu nâng lên `editor`
(chặn nếu đã có request `pending`). `GET /role-requests/me` xem request gần
nhất của chính mình. `GET /role-requests` (admin) liệt kê tất cả; `POST
/role-requests/{id}/approve` hoặc `.../decline` (admin) quyết định — approve
sẽ cập nhật `role` của user đó ngay trong DB, nhưng JWT cũ của họ vẫn giữ role
cũ cho tới lần đăng nhập kế tiếp (giới hạn cố hữu của JWT stateless, giống
hành vi role Google hiện tại).

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
    │   │   ├── security.py     # JWT issuance/verification + RBAC dependencies (LDMS-009/018)
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

## Triển khai kiểu production-like (Nginx + TLS, buffer §8.2)

Compose có thêm service `nginx` (profile `prod`) đóng gói FE build tĩnh + reverse proxy `/api` →
backend, TLS 1.2/1.3 với cert self-signed cho demo local:

```bash
./scripts/generate-dev-cert.sh
cd src/backend && docker compose --profile prod up -d --build
# https://localhost:8443
```

Không ảnh hưởng luồng dev mặc định (`docker compose up` không có `--profile prod` giữ nguyên 3
service API + PostgreSQL + MinIO theo LDMS-001 AC1). Cert self-signed chỉ phục vụ demo — production
thật trên VMware cần CA cert hợp lệ, xem `docs/06-architecture.md` §5.1.

## Sao lưu dữ liệu (buffer §5.2)

`./scripts/backup-postgres.sh` chạy `pg_dump -Fc` (định dạng nén, khôi phục bằng `pg_restore`) và
dọn bản backup cũ hơn `LDMS_BACKUP_RETENTION_DAYS` (mặc định 30 ngày).
`./scripts/backup-minio.sh` chạy `mc mirror` đồng bộ toàn bộ bucket sang thư mục cục bộ (đại diện
cho vị trí lưu trữ off-site). Cả hai ghi vào `.backups/` (gitignored) hoặc `$LDMS_BACKUP_DIR` nếu
đặt biến môi trường trỏ tới NAS/máy chủ dự phòng thật.

Đây là bản MVP thay thế PgBackRest/Restic — cùng tinh thần đơn giản hóa tech stack như Postgres
FTS thay Elasticsearch (`docs/07-product-backlog.md`). Roadmap khi triển khai thật trên VMware:
PgBackRest (incremental + AES-256) và Restic (encrypted off-site sync), xem
`docs/06-architecture.md` §5.2.

## Bảo mật đọc sách (LDMS-014)

File EPUB thành phẩm **không** được phục vụ qua URL công khai/trực tiếp. Khi độc giả mở Reader,
backend kiểm tra RBAC (`is_public` hoặc token hợp lệ) rồi mới sinh một **MinIO Signed URL** có hiệu
lực **15 phút** (`GET /documents/{id}/reader`, xem `app/services/reader_service.py`). Trình đọc
Epub.js dùng URL tạm thời này để tải nội dung; UI không có nút tải file EPUB gốc.

**Rủi ro tồn dư (residual risk)** — không thể loại bỏ hoàn toàn bằng kỹ thuật, chấp nhận ở phạm vi MVP:

- Trong 15 phút hiệu lực, người dùng có thể lấy Signed URL từ tab Network của DevTools và tải file.
- Người dùng luôn có thể chụp màn hình từng trang đang hiển thị.

Đây là cơ chế **giảm rủi ro**, không phải chống sao chép tuyệt đối — đúng tinh thần
`docs/06-architecture.md` §5.1.

## Tài liệu liên quan

- `docs/07-product-backlog.md` — backlog & AC
- `docs/06-architecture.md` — kiến trúc & tech stack
- `docs/09-plan.md` — phân công
