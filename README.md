# HCMUS-LDMS

Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS.

## Yêu cầu

- Docker & Docker Compose
- Node.js 20+
- [uv](https://docs.astral.sh/uv/) (Python package manager)

## Chạy local

```bash
# Backend + PostgreSQL + MinIO
cd src/backend
cp .env.example .env
docker compose up -d --build

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
    │   ├── models/              # SQLAlchemy models — trống, thêm khi có story cần DB
    │   ├── repositories/        # Data-access layer trên models — trống, thêm khi cần
    │   ├── schemas/             # Pydantic schemas — trống, thêm khi có story cần
    │   ├── services/            # Business logic (OCR, EPUB, search) — trống, thêm khi cần
    │   ├── workers/             # FastAPI BackgroundTasks jobs — trống, thêm khi cần
    │   └── utils/               # Helper functions dùng chung — trống, thêm khi cần
    └── tests/
        ├── conftest.py
        └── api/                 # Test theo từng router
```

Các thư mục `models/`, `repositories/`, `schemas/`, `services/`, `workers/`, `utils/` hiện chỉ có `.gitkeep` — để trống vì chưa có story nào cần đến; thêm file thật vào khi cần

Quy ước:
- Model/schema/service/repository cũng tách 1 file/entity hoặc module tương ứng (vd. `models/document.py`, `repositories/document_repository.py`, `services/ocr.py`) — tránh dồn hết vào 1 file dùng chung.
- Lỗi nghiệp vụ raise bằng các exception trong `core/exceptions.py` (`NotFoundError`, `ConflictError`, ...) thay vì tự trả `JSONResponse` — handler dùng chung đã đăng ký sẵn trong `main.py`.
- Migration: `uv run alembic revision --autogenerate -m "..."` rồi `uv run alembic upgrade head` (cần import model mới vào `app/db/migrations/env.py` để autogenerate nhận diện).
- Format trước khi commit: `uv run ruff format .` (backend), `npm run format` (frontend).
- Lint: `uv run ruff check .` (backend), `npm run lint` (frontend).
- Test backend: `uv run pytest`.
- Nhánh Git theo GitFlow (`feature/*` → `develop` → `release/*` → `main`), xem `docs/06-architecture.md` §8.2.

## Tài liệu liên quan

- `docs/07-product-backlog.md` — backlog & AC
- `docs/06-architecture.md` — kiến trúc & tech stack
- `docs/09-plan.md` — phân công
