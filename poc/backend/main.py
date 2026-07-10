from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import psycopg2
import os
import time

app = FastAPI(title="HCMUS-LDMS API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

DB_URL = os.getenv("DATABASE_URL", "postgresql://ldms:ldms@db:5432/ldms")


def get_conn():
    return psycopg2.connect(DB_URL)


def wait_for_db(retries=10, delay=2):
    for i in range(retries):
        try:
            conn = get_conn()
            conn.close()
            print("DB ready!")
            return
        except Exception as e:
            print(f"Waiting for DB ({i+1}/{retries})... {e}")
            time.sleep(delay)
    raise RuntimeError("Cannot connect to DB")


def init_db():
    wait_for_db()
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id TEXT PRIMARY KEY,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            publisher TEXT,
            year INTEGER,
            category TEXT,
            tags TEXT,
            access TEXT DEFAULT 'Internal',
            cover TEXT,
            description TEXT,
            pages INTEGER,
            ocr_accuracy REAL,
            content TEXT
        )
    """)
    # Seed one sample book if table is empty
    cur.execute("SELECT COUNT(*) FROM books")
    if cur.fetchone()[0] == 0:
        cur.execute("""
            INSERT INTO books VALUES (
                'b001',
                'Cấu trúc Dữ liệu và Giải thuật',
                'Nguyễn Văn An',
                'NXB ĐHQG-HCM',
                2022,
                'Khoa học Máy tính',
                '#GiaoTrinh,#CTDL,#Algorithm,#CS101',
                'Internal',
                '🖥️',
                'Giáo trình cơ bản về cấu trúc dữ liệu: mảng, danh sách liên kết, cây nhị phân, đồ thị và các giải thuật sắp xếp, tìm kiếm nền tảng.',
                324,
                94.2,
                '<h1>Chương 2: Các Giải thuật Tìm kiếm</h1><p>Trong chương này, chúng ta sẽ khảo sát các giải thuật tìm kiếm cơ bản và nâng cao.</p><h2>2.1. Tìm kiếm Tuyến tính (Linear Search)</h2><p>Tìm kiếm tuyến tính là giải thuật đơn giản nhất. Duyệt qua tất cả các phần tử từ đầu đến cuối.</p><pre><code>def linear_search(arr, target):\n    for i in range(len(arr)):\n        if arr[i] == target:\n            return i\n    return -1</code></pre><p><strong>Độ phức tạp:</strong> O(n) trong trường hợp xấu nhất.</p><h2>2.2. Tìm kiếm Nhị phân (Binary Search)</h2><p>Yêu cầu danh sách đã sắp xếp. Chia đôi không gian tìm kiếm trong mỗi bước.</p><pre><code>def binary_search(arr, target):\n    left, right = 0, len(arr) - 1\n    while left <= right:\n        mid = (left + right) // 2\n        if arr[mid] == target:\n            return mid\n        elif arr[mid] &lt; target:\n            left = mid + 1\n        else:\n            right = mid - 1\n    return -1</code></pre><p><strong>Độ phức tạp:</strong> O(log n).</p><h2>2.3. So sánh các Giải thuật</h2><table><tr><th>Giải thuật</th><th>Tốt nhất</th><th>Xấu nhất</th><th>Yêu cầu</th></tr><tr><td>Linear Search</td><td>O(1)</td><td>O(n)</td><td>Không cần sắp xếp</td></tr><tr><td>Binary Search</td><td>O(1)</td><td>O(log n)</td><td>Phải sắp xếp trước</td></tr></table>'
            )
        """)
        print("Seeded sample book into DB.")
    conn.commit()
    cur.close()
    conn.close()


# ─── Models ───────────────────────────────────────────────────────
class Book(BaseModel):
    id: str
    title: str
    author: str
    publisher: Optional[str] = None
    year: Optional[int] = None
    category: Optional[str] = None
    tags: list[str] = []
    access: str = "Internal"
    cover: str = "📖"
    description: Optional[str] = None
    pages: Optional[int] = None
    ocr_accuracy: Optional[float] = None
    content: Optional[str] = None


def row_to_book(row) -> dict:
    return {
        "id": row[0],
        "title": row[1],
        "author": row[2],
        "publisher": row[3],
        "year": row[4],
        "category": row[5],
        "tags": row[6].split(",") if row[6] else [],
        "access": row[7],
        "cover": row[8],
        "description": row[9],
        "pages": row[10],
        "ocr_accuracy": row[11],
        "content": row[12],
    }


# ─── Routes ───────────────────────────────────────────────────────
@app.on_event("startup")
def startup():
    init_db()


@app.get("/")
def root():
    return {"status": "ok", "service": "HCMUS-LDMS API"}


@app.get("/api/books")
def list_books(q: Optional[str] = None, category: Optional[str] = None):
    conn = get_conn()
    cur = conn.cursor()
    sql = "SELECT * FROM books WHERE 1=1"
    params = []
    if category:
        sql += " AND category = %s"
        params.append(category)
    if q:
        sql += " AND (title ILIKE %s OR author ILIKE %s OR description ILIKE %s OR content ILIKE %s)"
        params.extend([f"%{q}%"] * 4)
    cur.execute(sql, params)
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [row_to_book(r) for r in rows]


@app.get("/api/books/{book_id}")
def get_book(book_id: str):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM books WHERE id = %s", (book_id,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    if not row:
        raise HTTPException(status_code=404, detail="Book not found")
    return row_to_book(row)


@app.post("/api/books", status_code=201)
def create_book(book: Book):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO books VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        ON CONFLICT (id) DO UPDATE SET
            title=EXCLUDED.title, author=EXCLUDED.author,
            content=EXCLUDED.content, access=EXCLUDED.access
    """, (
        book.id, book.title, book.author, book.publisher, book.year,
        book.category, ",".join(book.tags), book.access, book.cover,
        book.description, book.pages, book.ocr_accuracy, book.content,
    ))
    conn.commit()
    cur.close()
    conn.close()
    return {"status": "published", "id": book.id}
