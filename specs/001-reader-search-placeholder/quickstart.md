# Quickstart: Reader/Search Placeholder & Document List

Không cần Docker/Postgres/MinIO chạy — toàn bộ dữ liệu là fixture in-memory.

## Backend

```bash
cd src/backend
uv run fastapi dev app/main.py
```

Kiểm tra nhanh 3 endpoint:

```bash
curl http://localhost:8000/documents
curl http://localhost:8000/reader/doc-1
curl "http://localhost:8000/search?q=giới hạn"
```

## Frontend

```bash
cd src/frontend
npm install    # sau khi thêm react-router-dom vào package.json
npm run dev
```

Mở trình duyệt:
1. `http://localhost:5173/` — Document List, phải thấy ≥ 2 tài liệu fixture.
2. Click một tài liệu → điều hướng sang `/reader/:documentId`, thấy nội dung text.
3. `http://localhost:5173/search` — nhập từ khóa có trong fixture → thấy kết quả; click kết quả → mở đúng Reader.

## Xác nhận Edge Cases (theo spec)

- Mở `/reader/khong-ton-tai` → thấy thông báo "không tìm thấy tài liệu", không phải màn trắng.
- Search với từ khóa không khớp gì → "không có kết quả".
- Search để trống rồi submit → không lỗi (trả rỗng).
