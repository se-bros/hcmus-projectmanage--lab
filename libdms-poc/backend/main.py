from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from ocr_service import extract_text
import uuid, os, psycopg2, time

app = FastAPI(title="LibDMS POC API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

DATABASE_URL = os.environ.get("DATABASE_URL", "postgresql://postgres:postgres@db:5432/libdms")

def get_db_connection():
    # Thử kết nối nhiều lần đề phòng db khởi động chậm hơn backend
    for _ in range(10):
        try:
            conn = psycopg2.connect(DATABASE_URL)
            return conn
        except psycopg2.OperationalError:
            time.sleep(2)
    raise Exception("Không thể kết nối đến PostgreSQL")

@app.on_event("startup")
def startup_db():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS documents (
            id VARCHAR(36) PRIMARY KEY,
            filename VARCHAR(255),
            file_data BYTEA,
            status VARCHAR(50),
            extracted_text TEXT
        );
    """)
    conn.commit()
    cur.close()
    conn.close()

@app.get("/")
def health_check():
    return {"status": "ok", "service": "LibDMS POC Backend (PostgreSQL Storage)"}

@app.post("/documents/upload")
async def upload_document(file: UploadFile = File(...)):
    """Nhận file, chạy OCR, lưu tệp nhị phân gốc trực tiếp vào PostgreSQL (BYTEA)."""
    allowed_types = {"image/png", "image/jpeg", "image/jpg", "application/pdf"}
    if file.content_type not in allowed_types:
        raise HTTPException(
            status_code=400,
            detail=f"Định dạng không hỗ trợ: {file.content_type}. Chỉ chấp nhận PNG, JPEG, PDF."
        )

    doc_id = str(uuid.uuid4())
    ext = os.path.splitext(file.filename)[1]
    
    # Đọc dữ liệu file
    file_bytes = await file.read()
    
    # Ghi tạm ra đĩa để thư viện OCR đọc
    temp_path = f"/tmp/{doc_id}{ext}"
    os.makedirs("/tmp", exist_ok=True)
    with open(temp_path, "wb") as f:
        f.write(file_bytes)
        
    try:
        # Chạy OCR
        text = extract_text(temp_path)
    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)

    # Lưu file data và kết quả OCR trực tiếp vào PostgreSQL
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO documents (id, filename, file_data, status, extracted_text) VALUES (%s, %s, %s, %s, %s)",
        (doc_id, file.filename, psycopg2.Binary(file_bytes), "done", text)
    )
    conn.commit()
    cur.close()
    conn.close()

    return {"id": doc_id, "filename": file.filename, "status": "done"}

@app.get("/documents/{doc_id}")
def get_document(doc_id: str):
    """Trả về kết quả OCR và metadata của tài liệu từ PostgreSQL."""
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, filename, status, extracted_text FROM documents WHERE id = %s", (doc_id,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    
    if not row:
        raise HTTPException(status_code=404, detail="Không tìm thấy tài liệu.")
        
    return {
        "id": row[0],
        "filename": row[1],
        "status": row[2],
        "text": row[3]
    }

@app.get("/documents/{doc_id}/download")
def download_document(doc_id: str):
    """Tải lại file gốc được lưu trữ dưới dạng BYTEA trong PostgreSQL."""
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT filename, file_data FROM documents WHERE id = %s", (doc_id,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    
    if not row:
        raise HTTPException(status_code=404, detail="Không tìm thấy tài liệu.")
        
    filename, file_bytes = row[0], row[1]
    
    # Trả về file nhị phân trực tiếp từ database
    media_type = "application/pdf" if filename.lower().endswith(".pdf") else "image/png"
    return Response(
        content=bytes(file_bytes),
        media_type=media_type,
        headers={"Content-Disposition": f"attachment; filename={filename}"}
    )

@app.get("/documents")
def list_documents():
    """Liệt kê danh sách tài liệu từ PostgreSQL."""
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, filename, status, extracted_text FROM documents")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    
    return [
        {"id": r[0], "filename": r[1], "status": r[2], "text": r[3]}
        for r in rows
    ]
