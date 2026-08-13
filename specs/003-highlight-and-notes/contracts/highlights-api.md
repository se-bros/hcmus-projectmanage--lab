# Phase 1 — API Contract: Highlights (LDMS-021)

Router: `src/backend/app/api/highlights.py` · Schema: `src/backend/app/schemas/highlight.py`

```python
router = APIRouter(prefix="/documents", tags=["highlights"])
```

Đăng ký trong `app/main.py` cạnh các router M6 hiện có.

**Mọi endpoint đều yêu cầu đăng nhập** — `Depends(get_current_user)`, không dùng `get_optional_user`. Độc giả ẩn danh nhận **401** (FR-015). Đây là điểm khác `GET /documents/{id}/reader` (cho phép khách xem document public).

---

## Cổng kiểm document — bắt buộc trước mọi thao tác

FR-001 giới hạn feature ở **tài liệu đã xuất bản**, và spec ghi rõ "document chưa xuất bản → chức năng highlight không khả dụng". Endpoint highlights **không được** tự ý bỏ qua cổng kiểm mà `reader_service.get_reader_content` đang áp cho đường đọc — nếu bỏ, một reader đã đăng nhập có thể gọi thẳng API để tạo highlight trên document `draft` của người khác, ghi `selected_text` (nội dung sách có bản quyền) vào DB cho tài liệu họ không có quyền đọc. Cùng lập luận với `research.md` R3: API là bề mặt công khai, không tin client.

Áp dụng **không đồng nhất** giữa các endpoint, có chủ ý:

| Kiểm | POST (tạo) | GET / PATCH / DELETE |
| :--- | :---: | :---: |
| `ensure_readable(document, user)` — quyền xem | ✅ | ✅ |
| `document.status == "published"` | ✅ | ❌ **cố ý bỏ** |

**Vì sao chỉ POST kiểm `published`**: tạo highlight đòi hỏi một bề mặt đọc thật đang mở, nên bắt buộc document phải đã xuất bản. Nhưng đọc/sửa/xóa highlight **đã có** phải sống sót qua việc document bị gỡ xuất bản — nếu không, một vòng re-publish sẽ khoá độc giả khỏi chính ghi chú của họ, đúng cái hỏng mà FR-011 sinh ra để chặn. Nhất quán: dữ liệu của người dùng không biến mất vì thao tác của thủ thư.

```python
document = ensure_readable(get_document(db, document_id), user)
# chỉ ở đường tạo:
if document.status != "published":
    raise ValidationError("Tài liệu chưa được xuất bản.")
```

Thông báo lỗi dùng lại nguyên văn của `reader_service` để độc giả thấy cùng một câu ở cả hai đường.

---

## Schema Pydantic

```python
MAX_NOTE_LENGTH = 2000
MAX_SELECTED_TEXT_LENGTH = 5000


class HighlightCreate(BaseModel):
    cfi_range: str
    selected_text: str
    note: str | None = None
    # validator: V1, V2, V3, V4, V5 (xem data-model.md)


class HighlightNoteUpdate(BaseModel):
    note: str | None
    # validator: V5, V6


class HighlightDetail(BaseModel):
    id: uuid.UUID
    document_id: uuid.UUID
    cfi_range: str
    selected_text: str
    note: str | None
    created_at: datetime
    updated_at: datetime
```

`HighlightDetail` **không** trả `user_sub`: client luôn chỉ nhận highlight của chính mình nên trường đó không mang thông tin, và không trả ra thì không có đường rò định danh user sang response.

---

## `GET /documents/{document_id}/highlights`

Lấy toàn bộ highlight của user hiện tại trên một document.

**Response `200`** — `list[HighlightDetail]`, sắp xếp theo `created_at` tăng dần.

```json
[
  {
    "id": "3f2b…",
    "document_id": "9a1c…",
    "cfi_range": "epubcfi(/6/14[chap03]!/4/2,/1:12,/3:28)",
    "selected_text": "Thư viện số là hạ tầng tri thức của đại học.",
    "note": "Trích cho phần mở đầu tiểu luận",
    "created_at": "2026-08-12T09:15:00Z",
    "updated_at": "2026-08-12T09:20:00Z"
  }
]
```

- Chưa có highlight nào → `200` với mảng rỗng `[]`, **không** phải 404. Đây là trạng thái bình thường của mọi document mới mở, khác `GET /bookmark` (404 khi chưa có) vì bookmark là một giá trị đơn còn đây là tập hợp.
- Document không tồn tại → `404`.
- Chưa đăng nhập → `401`.

Response này là đầu vào cho việc phân loại "dựng được / không định vị được" ở client (R4) — server trả tất, client tự phân nhóm.

---

## `POST /documents/{document_id}/highlights`

Tạo một highlight, kèm ghi chú ngay từ đầu nếu muốn.

**Request** — `HighlightCreate`:

```json
{
  "cfi_range": "epubcfi(/6/14[chap03]!/4/2,/1:12,/3:28)",
  "selected_text": "Thư viện số là hạ tầng tri thức của đại học.",
  "note": null
}
```

**Response `201`** — `HighlightDetail`.

| Tình huống | Mã | Thông báo |
| :--- | :--- | :--- |
| `selected_text` rỗng/toàn khoảng trắng (V1) | `422` | "Vùng chọn không có nội dung." |
| `selected_text` > 5.000 ký tự (V2) | `422` | "Đoạn chọn quá dài (tối đa 5.000 ký tự)." |
| `cfi_range` sai định dạng (V3) | `422` | "Vị trí đánh dấu không hợp lệ." |
| `cfi_range` vắt qua chương (V4) | `422` | "Chỉ đánh dấu được trong cùng một chương." |
| `note` > 2.000 ký tự (V5) | `422` | "Ghi chú quá dài (N/2.000 ký tự)." |
| Document chưa xuất bản (`status != "published"`) | `422` | "Tài liệu chưa được xuất bản." |
| Document không tồn tại | `404` | — |
| Không có quyền xem document (`ensure_readable`) | `401` | — |
| Chưa đăng nhập | `401` | — |

**Không** kiểm trùng với highlight đã có — vùng chồng lấn hoặc trùng khít đều tạo bản ghi mới (FR-004). Không có đường trả `409` ở endpoint này.

---

## `PATCH /documents/{document_id}/highlights/{highlight_id}`

Sửa hoặc gỡ ghi chú. Vùng đánh dấu bất biến (R6).

**Request** — `HighlightNoteUpdate`:

```json
{ "note": "Đối chiếu với chương 5" }
```

Gỡ ghi chú mà giữ highlight: gửi `{"note": null}` hoặc `{"note": "   "}` → chuẩn hoá về `NULL` (V6, FR-007).

**Response `200`** — `HighlightDetail` sau khi cập nhật.

| Tình huống | Mã |
| :--- | :--- |
| `note` > 2.000 ký tự | `422` kèm số ký tự hiện tại |
| Highlight không tồn tại **hoặc thuộc user khác** | `404` |
| Chưa đăng nhập | `401` |

---

## `DELETE /documents/{document_id}/highlights/{highlight_id}`

**Response `204`**, không có body. Ghi chú gắn kèm mất theo (cùng bản ghi).

| Tình huống | Mã |
| :--- | :--- |
| Highlight không tồn tại **hoặc thuộc user khác** | `404` |
| Chưa đăng nhập | `401` |

Xóa một highlight không đụng tới highlight nào chồng lấn với nó (FR-004, US3 scenario 7). Xóa được cả bản ghi đang ở nhóm "không định vị được" (FR-011b) — server không phân biệt hai nhóm này nên điều đó tự đúng.

---

## Quy tắc cô lập user — bắt buộc với cả 4 endpoint

Điều kiện `user_sub` phải nằm **trong mệnh đề `WHERE`**, không phải một lần kiểm sau khi đã lấy bản ghi:

```python
# ĐÚNG
highlight = db.scalar(
    select(Highlight).where(
        Highlight.id == highlight_id,
        Highlight.document_id == document_id,
        Highlight.user_sub == user_sub,
    )
)
if highlight is None:
    raise NotFoundError("Không tìm thấy đánh dấu.")

# SAI — lấy trước rồi mới kiểm, quên một nhánh là lộ dữ liệu user khác
highlight = db.get(Highlight, highlight_id)
if highlight.user_sub != user_sub:
    raise ForbiddenError(...)
```

Hướng lỗi của cách đúng an toàn hơn: quên điều kiện trong `WHERE` thì truy vấn không trả về gì, còn quên câu `if` thì rò dữ liệu.

Trả `404` (không phải `403`) cho bản ghi của người khác — `403` gián tiếp xác nhận id đó có tồn tại (R6).

---

## Contract test cần có

`src/backend/tests/api/test_highlights.py`, dùng fixture `api_context` sẵn có. Cần thêm một fixture `reader_headers` (hiện `conftest.py` mới có `editor_headers`/`admin_headers`) và một fixture cho user thứ hai để kiểm cô lập.

| # | Tình huống | Kỳ vọng | AC/FR |
| :--- | :--- | :--- | :--- |
| T1 | POST rồi GET | Highlight trả về đúng `cfi_range` + `selected_text` | AC 1 |
| T2 | GET khi chưa có gì | `200`, mảng rỗng | — |
| T3 | POST kèm note rồi GET | Note còn nguyên văn | AC 2 |
| T4 | PATCH đổi note | Nội dung mới thay nội dung cũ | FR-007 |
| T5 | PATCH `note: null` | Note về `null`, highlight vẫn còn | FR-007 |
| T6 | DELETE rồi GET | Không còn trong danh sách | AC 3 |
| T7 | User B GET document của A | Không thấy highlight của A | FR-012 |
| T8 | User B PATCH/DELETE highlight của A | `404`, bản ghi của A còn nguyên | FR-012 |
| T9 | POST không kèm token | `401` | FR-015 |
| T10 | POST `selected_text` toàn khoảng trắng | `422` | FR-005 |
| T11 | POST `cfi_range` vắt chương | `422` | FR-005b |
| T12 | POST/PATCH note 2.001 ký tự | `422` kèm số ký tự | FR-009 |
| T13 | POST hai highlight chồng lấn | Cả hai tạo được, GET trả 2 bản ghi | FR-004 |
| T14 | Xóa document | Highlight bị xóa theo | FR-013 |
| T15 | POST lên document `draft` | `422` "Tài liệu chưa được xuất bản.", không tạo bản ghi | FR-001 |
| T16 | GET/DELETE highlight đã có sau khi document bị gỡ xuất bản | Vẫn đọc và xóa được | FR-011 (xem bảng cổng kiểm) |
| T17 | PATCH/DELETE lên highlight của **chính mình** đã bị xóa trước đó | `404`, không lỗi hệ thống | Edge case "xóa ở tab khác" |

T13 là test chống hồi quy cho quyết định "không unique constraint" ở `data-model.md` — nếu ai đó thêm ràng buộc unique cho giống `bookmarks`, T13 đỏ ngay.

T15 và T16 là một cặp và phải cùng tồn tại: T15 ghim "không tạo được trên document chưa xuất bản", T16 ghim "nhưng bản ghi đã có thì không mất khi document bị gỡ xuất bản". Chỉ có T15 thì rất dễ bị sửa thành áp `published` cho cả 4 endpoint và khoá độc giả khỏi ghi chú của chính họ.
