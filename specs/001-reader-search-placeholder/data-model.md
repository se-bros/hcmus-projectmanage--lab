# Data Model: Reader/Search Placeholder & Document List

Toàn bộ entity dưới đây là **fixture in-memory** (Python module `app/fixtures/documents.py`), không phải bảng PostgreSQL — sẽ được thay bằng model SQLAlchemy thật khi LDMS-002/026 được pick chính thức (xem `plan.md` Structure Decision).

## Document (fixture)

Đại diện một tài liệu trong danh sách.

| Field | Type | Bắt buộc | Ghi chú |
|---|---|---|---|
| `id` | `str` | có | Định danh duy nhất, dùng làm `document_id` trong route `/reader/:documentId`. |
| `title` | `str` | có | Tên hiển thị trong Document List. |
| `status` | `Literal["draft", "published"]` | có | Hiển thị cột status trong danh sách (US1 AC1). |
| `created_at` | `date` (ISO 8601 string trong response) | có | Hiển thị cột ngày tạo. |

**Validation rules**: `id` duy nhất trong toàn bộ fixture list (không enforce runtime vì dữ liệu tĩnh do dev kiểm soát).

## DocumentContent (fixture)

Nội dung text thô gắn với một `Document`, dùng cho Reader placeholder và Search.

| Field | Type | Bắt buộc | Ghi chú |
|---|---|---|---|
| `document_id` | `str` | có | Khóa ngoại logic tới `Document.id`. |
| `text` | `str` | có | Nội dung text thô hiển thị trong Reader (US2 AC1) và được Search quét qua (US3). |

**Quan hệ**: 1 `Document` — 1 `DocumentContent` (1-1, khóa là `document_id`). Không phải mọi `Document` bắt buộc có `DocumentContent` (US2 AC2: `document_id` không có content → "không tìm thấy").

## SearchResult (response-only, không lưu trữ)

Kết quả trả về từ `GET /search`, dựng từ `Document` + `DocumentContent` tại thời điểm query — không phải entity lưu trữ riêng.

| Field | Type | Ghi chú |
|---|---|---|
| `document_id` | `str` | Trỏ tới `Document.id`, dùng để FE điều hướng sang `/reader/:documentId`. |
| `title` | `str` | Copy từ `Document.title` để hiển thị trong danh sách kết quả mà không cần gọi thêm API. |
| `snippet` | `str` | Đoạn text ngắn quanh vị trí khớp từ khóa đầu tiên trong `DocumentContent.text` (xem `research.md` — Search matching logic). |

## Fixture seed tối thiểu

Để thỏa mãn mọi Acceptance Scenario trong spec (kể cả edge case), fixture cần tối thiểu:
- ≥ 2 `Document` (để US1 AC1 có gì đó hiển thị, và có ít nhất 1 document **không** có `DocumentContent` để test US2 AC2).
- ≥ 1 `DocumentContent` chứa một từ khóa xác định trước (dùng để test US3 AC1), và đảm bảo có từ khóa chắc chắn không khớp gì (test US3 AC2).
