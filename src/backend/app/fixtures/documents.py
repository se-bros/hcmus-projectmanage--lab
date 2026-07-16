"""Fixture tĩnh cho placeholder LDMS-026/008/015 — sẽ thay bằng DB thật khi
story được pick chính thức. Xem specs/001-reader-search-placeholder/data-model.md.

Seed cố ý bao gồm:
- doc-3 KHÔNG có nội dung → test Reader 404 (US2 AC2).
- từ khóa chắc chắn khớp ("giới hạn", "vòng lặp") và không khớp (bất kỳ chuỗi
  không xuất hiện) → test Search (US3 AC1/AC2).
"""

from datetime import date

from app.schemas.document import DocumentSummary

DOCUMENTS: list[DocumentSummary] = [
    DocumentSummary(
        id="doc-1",
        title="Giáo trình Giải tích 1",
        status="published",
        created_at=date(2026, 7, 10),
    ),
    DocumentSummary(
        id="doc-2",
        title="Nhập môn Lập trình",
        status="published",
        created_at=date(2026, 7, 12),
    ),
    DocumentSummary(
        id="doc-3",
        title="Bản thảo chưa biên tập",
        status="draft",
        created_at=date(2026, 7, 15),
    ),
]

DOCUMENT_CONTENTS: dict[str, str] = {
    "doc-1": (
        "Chương 1. Giới hạn và liên tục.\n\n"
        "Khái niệm giới hạn của hàm số là nền tảng của giải tích. "
        "Một hàm số liên tục tại một điểm nếu giới hạn tại điểm đó bằng giá trị hàm số."
    ),
    "doc-2": (
        "Chương 1. Biến, kiểu dữ liệu và vòng lặp.\n\n"
        "Vòng lặp cho phép lặp lại một khối lệnh nhiều lần. "
        "Biến dùng để lưu trữ giá trị trong quá trình chạy chương trình."
    ),
}
