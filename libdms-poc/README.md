# LibDMS POC — Proof of Concept

> Skeleton đơn giản chứng minh luồng nghiệp vụ số hóa: **Upload ảnh/PDF → Lưu BYTEA vào PostgreSQL & Chạy OCR tiếng Việt → Hiển thị kết quả & Cho phép tải file từ DB**

## Cấu trúc

```
libdms-poc/
├── backend/          # FastAPI (Python 3.11) + psycopg2
│   ├── main.py       # API routes (kết nối PostgreSQL, upload, download, list)
│   ├── ocr_service.py # Tesseract OCR wrapper
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/         # Next.js 14
│   ├── pages/index.js # UI upload + hiển thị kết quả
│   ├── package.json
│   └── Dockerfile
└── docker-compose.yml
```

## Chạy POC

```bash
# Từ thư mục libdms-poc/
docker compose up --build
```

Sau khi build xong:
- **Giao diện:** http://localhost:3000
- **API Swagger:** http://localhost:8000/docs
- **PostgreSQL Database:** Khởi chạy ở port `5432` bên trong cụm docker.

## API Endpoints

| Method | Endpoint | Mô tả |
|--------|----------|-------|
| `GET` | `/` | Health check |
| `POST` | `/documents/upload` | Upload file và lưu trực tiếp dạng nhị phân (`BYTEA`) vào PostgreSQL, chạy OCR |
| `GET` | `/documents/{id}` | Lấy kết quả OCR và metadata theo ID |
| `GET` | `/documents/{id}/download` | Tải lại file nhị phân gốc trực tiếp từ PostgreSQL |
| `GET` | `/documents` | Liệt kê tất cả tài liệu đã số hóa |

## Công nghệ

- **Backend:** FastAPI + Uvicorn + Tesseract OCR (`vie.traineddata`) + PyMuPDF + psycopg2
- **Database / File Storage:** PostgreSQL (Sử dụng bảng `documents` với cột `file_data BYTEA` để lưu trữ tệp tin nhị phân gốc)
- **Frontend:** Next.js 14 + React 18 + Axios
- **Containerization:** Docker Compose

