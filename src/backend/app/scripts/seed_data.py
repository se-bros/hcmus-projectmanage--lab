"""Seed initial sample data for HCMUS-LDMS development & evaluation.

Creates default users (admin, librarian, reader), categories, tags,
and sample published documents with full text pages for search & reader demo.
"""

import io
import logging
import uuid
import zipfile

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.security import hash_password
from app.core.storage import ensure_bucket_exists, minio_client, settings
from app.db.session import SessionLocal
from app.models.category import Category
from app.models.document import Document
from app.models.document_tag import DocumentTag
from app.models.page import Page
from app.models.user import User

logging.basicConfig(level=logging.INFO, format="[seed] %(message)s")
logger = logging.getLogger("seed")


def create_minimal_epub_bytes(title: str, author: str) -> bytes:
    """Generate a valid minimal EPUB in memory for testing reader."""
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("mimetype", "application/epub+zip", compress_type=zipfile.ZIP_STORED)
        z.writestr(
            "META-INF/container.xml",
            """<?xml version="1.0" encoding="UTF-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
  <rootfiles>
    <rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>
  </rootfiles>
</container>""",
        )
        z.writestr(
            "OEBPS/content.opf",
            f"""<?xml version="1.0" encoding="UTF-8"?>
<package xmlns="http://www.idpf.org/2007/opf" unique-identifier="BookId" version="3.0">
  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
    <dc:title>{title}</dc:title>
    <dc:creator>{author}</dc:creator>
    <dc:language>vi</dc:language>
    <dc:identifier id="BookId">urn:uuid:{uuid.uuid4()}</dc:identifier>
    <meta property="dcterms:modified">2026-08-20T00:00:00Z</meta>
  </metadata>
  <manifest>
    <item id="chapter1" href="chapter1.xhtml" media-type="application/xhtml+xml"/>
  </manifest>
  <spine>
    <itemref idref="chapter1"/>
  </spine>
</package>""",
        )
        z.writestr(
            "OEBPS/chapter1.xhtml",
            f"""<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <title>{title}</title>
</head>
<body>
  <h1>{title}</h1>
  <p>Tác giả: {author}</p>
  <hr/>
  <p>Chào mừng bạn đến với tài liệu số hóa thư viện Đại học Khoa học Tự nhiên ĐHQG-HCM.</p>
  <p>Hệ thống hỗ trợ đọc trực tuyến, đánh dấu (bookmark), ghi chú và highlight nội dung sách.</p>
</body>
</html>""",
        )
    return buf.getvalue()


def seed_users(db: Session) -> dict[str, User]:
    users_data = [
        {
            "email": "admin@hcmus.edu.vn",
            "username": "Quản Trị Viên (Admin)",
            "password": "Admin@123456",
            "role": "admin",
        },
        {
            "email": "librarian@hcmus.edu.vn",
            "username": "Thủ Thư (Librarian)",
            "password": "Librarian@123456",
            "role": "librarian",
        },
        {
            "email": "reader@hcmus.edu.vn",
            "username": "Sinh Viên / Độc Giả",
            "password": "Reader@123456",
            "role": "reader",
        },
    ]

    users_map = {}
    for item in users_data:
        user = db.scalar(select(User).where(User.email == item["email"]))
        if not user:
            user = User(
                id=uuid.uuid4(),
                email=item["email"],
                username=item["username"],
                password_hash=hash_password(item["password"]),
                role=item["role"],
                auth_provider="local",
            )
            db.add(user)
            db.commit()
            db.refresh(user)
            logger.info("Created user: %s (%s)", item["email"], item["role"])
        else:
            user.role = item["role"]
            user.username = item["username"]
            user.password_hash = hash_password(item["password"])
            db.commit()
            db.refresh(user)
            logger.info("Updated existing user: %s (%s)", item["email"], item["role"])
        users_map[item["role"]] = user
    return users_map


def seed_categories(db: Session) -> dict[str, Category]:
    names = [
        "Khoa học Máy tính",
        "Công nghệ Phần mềm",
        "Hệ thống Thông tin",
        "Trí tuệ Nhân tạo & Khoa học Dữ liệu",
    ]
    cat_map = {}
    for name in names:
        cat = db.scalar(select(Category).where(Category.name == name))
        if not cat:
            cat = Category(id=uuid.uuid4(), name=name)
            db.add(cat)
            db.commit()
            db.refresh(cat)
            logger.info("Created category: %s", name)
        cat_map[name] = cat
    return cat_map


def seed_documents(db: Session, admin_user: User, cat_map: dict[str, Category]) -> None:
    try:
        ensure_bucket_exists()
    except Exception as e:
        logger.warning("Could not connect to MinIO for seeding files: %s", e)

    docs_data = [
        {
            "title": "Kiến trúc Hệ thống Số hóa Thư viện HCMUS-LDMS",
            "author": "Nhóm Kỹ thuật Phòng CNTT HCMUS",
            "shelf_location": "Kệ A1 - Tầng 2 Thư viện Trung tâm",
            "category": "Công nghệ Phần mềm",
            "tags": ["Architecture", "FastAPI", "React", "DevOps"],
            "pages": [
                (1, "Chương 1: Giới thiệu hệ thống HCMUS-LDMS và giải pháp số hóa toàn diện."),
                (
                    2,
                    "Chương 2: Kiến trúc Modular Monolith và triển khai CI/CD trên môi trường ảo"
                    " hóa.",
                ),
                (
                    3,
                    "Chương 3: Quy trình OCR tiếng Việt, bảo mật RBAC và tích hợp Google OAuth"
                    " 2.0.",
                ),
            ],
        },
        {
            "title": "Cẩm nang Kỹ thuật DevOps & Cloud-Native Deployment",
            "author": "Đội ngũ Kỹ sư Phần mềm",
            "shelf_location": "Kệ B3 - Khu vực Tham khảo",
            "category": "Khoa học Máy tính",
            "tags": ["DevOps", "Docker", "Kubernetes", "CI-CD"],
            "pages": [
                (1, "Phần 1: Nguyên lý Continuous Integration & Continuous Delivery tự động."),
                (
                    2,
                    "Phần 2: Thiết lập Docker Compose đa môi trường và giám sát"
                    " Prometheus/Grafana.",
                ),
                (
                    3,
                    "Phần 3: Chiến lược triển khai Zero-downtime Rolling Update & Canary trên"
                    " Kubernetes.",
                ),
            ],
        },
    ]

    for item in docs_data:
        doc = db.scalar(select(Document).where(Document.title == item["title"]))
        if not doc:
            doc_id = uuid.uuid4()
            obj_key = f"documents/{doc_id}/original.pdf"
            epub_key = f"documents/{doc_id}/book.epub"

            try:
                pdf_bytes = b"%PDF-1.4 Mock PDF content for seeding demo"
                minio_client.put_object(
                    settings.minio_bucket,
                    obj_key,
                    io.BytesIO(pdf_bytes),
                    length=len(pdf_bytes),
                    content_type="application/pdf",
                )
                epub_bytes = create_minimal_epub_bytes(item["title"], item["author"])
                minio_client.put_object(
                    settings.minio_bucket,
                    epub_key,
                    io.BytesIO(epub_bytes),
                    length=len(epub_bytes),
                    content_type="application/epub+zip",
                )
            except Exception as e:
                logger.warning("Skipped MinIO upload for %s: %s", item["title"], e)

            doc = Document(
                id=doc_id,
                title=item["title"],
                author=item["author"],
                original_filename=f"{item['title']}.pdf",
                object_key=obj_key,
                epub_object_key=epub_key,
                content_type="application/pdf",
                status="published",
                is_public=True,
                shelf_location=item["shelf_location"],
                category_id=cat_map[item["category"]].id if item["category"] in cat_map else None,
                owner_id=admin_user.id,
            )
            db.add(doc)
            db.commit()
            db.refresh(doc)

            for page_num, text_content in item["pages"]:
                page = Page(
                    id=uuid.uuid4(),
                    document_id=doc.id,
                    page_number=page_num,
                    text_content=text_content,
                )
                db.add(page)

            for tag_name in item["tags"]:
                tag = DocumentTag(
                    id=uuid.uuid4(),
                    document_id=doc.id,
                    name=tag_name,
                )
                db.add(tag)

            db.commit()
            logger.info("Created sample document: %s (id=%s)", item["title"], doc.id)
        else:
            logger.info("Sample document already exists: %s", item["title"])


def main() -> None:
    logger.info("Starting HCMUS-LDMS database seeding...")
    db = SessionLocal()
    try:
        users = seed_users(db)
        categories = seed_categories(db)
        seed_documents(db, users["admin"], categories)
        logger.info("Database seeding completed successfully!")
    except Exception:
        logger.exception("Error during database seeding")
        db.rollback()
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
