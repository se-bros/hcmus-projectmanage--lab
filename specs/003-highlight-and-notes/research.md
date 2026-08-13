# Phase 0 — Research: Highlight và ghi chú (LDMS-021)

Sáu điểm cần chốt trước khi thiết kế. Mỗi mục ghi Quyết định / Lý do / Phương án đã loại.

---

## R1 — Định dạng lưu vị trí vùng đánh dấu

**Quyết định**: Lưu một chuỗi **EPUB CFI range** duy nhất trong cột `cfi_range` (kiểu `Text`), ví dụ `epubcfi(/6/14[chap03]!/4/2,/1:12,/3:28)`.

**Lý do**:
- Cùng họ định vị mà LDMS-020 đã dùng cho `bookmarks.location` (giá trị lấy từ `location.start.cfi` trong `ReaderPage.tsx:64`), nên không phát minh hệ toạ độ thứ hai trong cùng module M6 — đúng Assumption đã chốt trong spec.
- epub.js sinh sẵn chuỗi này: sự kiện `rendition.on('selected', (cfiRange, contents) => …)` trả thẳng CFI range của vùng bôi đen, và `rendition.annotations.add('highlight', cfiRange, …)` nhận lại đúng chuỗi đó để tô. Không cần code chuyển đổi.
- CFI range mã hoá cả spine item (chương) lẫn offset trong text node, nên bám theo cấu trúc tài liệu chứ không theo số trang — thoả FR-014 (đổi cỡ chữ không làm lệch highlight) và FR-005a.

**Đã loại**:
- *Offset ký tự tuyệt đối trong text đã OCR*: đơn giản hơn nhưng gắn chặt vào text OCR chứ không phải EPUB đang đọc; đổi bản OCR là lệch toàn bộ, và không có đường ánh xạ ngược sang DOM để tô màu.
- *XPath + offset tự chế*: tương đương CFI nhưng phải tự viết code dựng lại vùng chọn, trong khi epub.js đã làm sẵn.

---

## R2 — Cơ chế tô màu và xử lý vùng chồng lấn (FR-004)

**Quyết định**: Dùng `rendition.annotations.add('highlight', cfiRange, { id }, onClick, className, styles)` của epub.js, mỗi bản ghi một annotation độc lập. Vùng chồng lấn hiển thị đậm hơn bằng CSS `mix-blend-mode: multiply` trên lớp SVG mà epub.js sinh ra.

**Lý do**:
- epub.js vẽ annotation thành các `<rect>` SVG nằm chồng lên nội dung, nhiều annotation cùng vùng cùng tồn tại được — đúng ngữ nghĩa "tồn tại song song, không gộp" của FR-004, không cần tự tính toán hình học vùng giao.
- `mix-blend-mode: multiply` cho phần giao tự nhiên đậm hơn mà không cần biết có bao nhiêu lớp chồng lên nhau.
- Tham số `onClick` cho phép gắn handler theo từng annotation → mở đúng highlight người dùng bấm vào.

**Rủi ro đã nhận diện**: khi nhiều highlight chồng khít nhau, cú bấm chỉ trúng annotation nằm trên cùng — người dùng không chọn được cái bên dưới. Đây chính là bullet Edge Case đã ghi trong spec. **Cách xử lý**: `HighlightSidebar` là đường truy cập chính thức và luôn đầy đủ — mọi highlight đều thao tác được từ danh sách bên cạnh, bấm trực tiếp trên sách chỉ là lối tắt tiện tay. Không phụ thuộc vào việc bấm trúng.

**Đã loại**:
- *Tự bọc `<mark>` vào DOM của iframe*: phải tự cắt text node, vỡ ngay khi hai vùng chồng nhau (một node thuộc hai mark), và bị epub.js ghi đè mỗi lần re-render.
- *Gộp vùng chồng lấn thành một*: đã bị loại ở bước `/speckit.clarify`.

---

## R3 — Bảo đảm một highlight nằm gọn trong một chương (FR-005b)

**Quyết định**: Dựa vào ràng buộc cấu trúc của epub.js ở client, **cộng thêm** một lần kiểm ở server bằng cách so sánh phần spine step giữa hai đầu của CFI range.

**Lý do**:
- `ReaderPage.tsx` đang render với `flow: 'scrolled-doc'` (dòng 56). Ở chế độ này epub.js render **mỗi spine item trong một iframe riêng**. Selection của trình duyệt không vượt qua được ranh giới iframe, nên trên thực tế người dùng không tạo nổi vùng chọn vắt hai chương — FR-005b được thoả về mặt cấu trúc, không cần chặn thủ công ở UI.
- Vẫn kiểm ở server vì API là bề mặt công khai: client khác (hoặc curl) có thể gửi CFI range vắt chương. CFI range có dạng `epubcfi(<phần chung>,<đầu>,<cuối>)` — nếu phần chung đã chứa dấu `!` (đã vào trong spine item) thì hai đầu chắc chắn cùng một chương. Ngược lại là vắt chương → `ValidationError`.
- Kiểm ở server rẻ (thao tác chuỗi thuần), không cần parse EPUB.

**Đã loại**:
- *Chỉ tin client*: vi phạm nguyên tắc không tin input từ client, và FR-005b được viết là ràng buộc của hệ thống chứ không phải của giao diện.
- *Parse file EPUB ở server để xác thực CFI trỏ đúng chỗ*: phải tải EPUB từ MinIO trên mỗi lần tạo highlight — chậm, tốn, và kéo đường truy cập file vào một luồng vốn không cần đụng tới file (đi ngược tinh thần Nguyên tắc IV).

---

## R4 — Phát hiện highlight "không còn định vị được" (FR-011)

**Quyết định**: Phân loại ở **client, lúc render**, không lưu cột trạng thái nào trong DB. Khi mở Reader, với mỗi highlight thử `rendition.annotations.add(...)` trong `try/catch` (kèm kiểm `book.spine.get(cfiRange)` trả về `null`); bản nào không dựng được thì đẩy vào nhóm "Đánh dấu không còn định vị được" của sidebar, hiển thị bằng `selected_text` đã lưu.

**Lý do**:
- "CFI này còn trỏ đúng chỗ không" là thuộc tính của **bản EPUB đang mở**, không phải của bản ghi. Cùng một highlight có thể hỏng trên bản mới rồi lại đúng nếu thủ thư rollback — lưu thành cột trong DB là lưu một sự thật sẽ hết hạn.
- Không cần cột mới → không cần job quét lại toàn bộ highlight mỗi lần một document được publish lại.
- `selected_text` (FR-003) đã có sẵn chính là để hiển thị trong tình huống này, không cần thêm dữ liệu gì.

**Đã loại**:
- *Cột `is_orphaned` cập nhật khi re-publish*: cần hook vào `publish_service` để quét và cập nhật hàng loạt highlight của mọi user — thêm phụ thuộc chéo giữa M5 (Publish) và M6 (Reader) cho một story ưu tiên Could.
- *Lưu `epub_object_key` lúc tạo rồi so sánh*: phát hiện được "sách đã đổi bản" nhưng không phát hiện được "CFI cụ thể này có còn đúng không" — publish lại mà cấu trúc chương không đổi thì phần lớn highlight vẫn dùng tốt, cách này sẽ báo hỏng oan toàn bộ.

---

## R5 — Alembic đang có hai head (chặn migration mới)

**Quyết định**: Thêm **hai** revision: một `merge` revision gộp hai head có sẵn, rồi migration tạo bảng `highlights` nối sau nó.

```python
# 20260812_0009_merge_heads.py
revision = "20260812_0009"
down_revision = ("20260717_0007", "20260721_0008")   # tuple = merge
# upgrade()/downgrade() để trống — merge revision không đổi schema

# 20260812_0010_highlights.py
revision = "20260812_0010"
down_revision = "20260812_0009"
```

**Lý do**:
- Đồ thị hiện tại phân nhánh tại `20260716_0005`: nhánh `20260717_0006 → 0007` (search + bookmarks) và nhánh `20260721_0006 → 0007 → 0008` (users + owner + profile). Hai head cùng tồn tại nên `alembic upgrade head` báo lỗi "multiple heads"; không gộp thì migration mới không có chỗ neo hợp lệ.
- Merge revision là cơ chế chính thức của Alembic cho đúng tình huống này (`alembic merge`), không sửa schema nên rủi ro bằng không và không đụng vào lịch sử migration của người khác.
- Tách riêng khỏi migration `highlights` để diff đọc được rõ: một revision dọn đồ thị, một revision thêm bảng.

**Đây là nợ có sẵn, không do feature này gây ra** — nêu rõ trong mô tả PR để reviewer không nhầm là thay đổi ngoài phạm vi. Nếu team muốn xử lý ở một PR riêng thì làm trước, feature này chỉ cần đổi `down_revision` của `20260812_0010` trỏ vào head mới.

**Đã loại**:
- *Nối thẳng vào một trong hai head*: tạo ra head thứ ba, làm vấn đề nặng thêm.
- *Sửa `down_revision` của migration cũ để duỗi thành chuỗi thẳng*: viết lại lịch sử migration đã chạy trên máy người khác và có thể đã chạy trên môi trường chung — sai lệch giữa `alembic_version` và file.

---

## R6 — Hình dạng API và cách chống rò rỉ dữ liệu chéo user (FR-012)

**Quyết định**: 4 endpoint lồng dưới document, mọi truy vấn **bắt buộc** kèm điều kiện `user_sub` lấy từ JWT của chính request; truy cập bản ghi của người khác trả **404**, không phải 403.

```
GET    /documents/{document_id}/highlights
POST   /documents/{document_id}/highlights
PATCH  /documents/{document_id}/highlights/{highlight_id}
DELETE /documents/{document_id}/highlights/{highlight_id}
```

**Lý do**:
- Lồng dưới `/documents/{id}` khớp với `bookmark` đang có (`/documents/{document_id}/bookmark`) và làm quyền sở hữu document trở thành điều kiện tự nhiên trên đường đi.
- `PATCH` riêng cho ghi chú vì FR-007 chỉ cho sửa ghi chú — vùng đánh dấu là bất biến sau khi tạo (muốn đổi vùng thì xóa và tạo lại). `PATCH` diễn đạt đúng "sửa một phần" hơn `PUT`.
- **404 thay vì 403** khi đụng bản ghi của người khác: 403 vô tình xác nhận "highlight id này có tồn tại", rò rỉ thông tin. 404 khiến "không tồn tại" và "không phải của bạn" không phân biệt được từ bên ngoài. Cách làm: điều kiện `user_sub` nằm ngay trong `WHERE` của câu `select`, không phải một lần kiểm `if` sau khi đã lấy được bản ghi — quên `if` thì lộ, quên `WHERE` thì không tìm thấy gì cả, nên hướng lỗi an toàn hơn.

**Đã loại**:
- *`/highlights?document_id=…` phẳng ở gốc*: mất ràng buộc document trên đường đi, phải tự kiểm thủ công.
- *Trả 403 cho bản ghi của người khác*: xem trên.
- *Một endpoint `PUT` thay cả bản ghi*: cho phép client đổi `cfi_range`, mở ra tình huống vùng đánh dấu lệch khỏi `selected_text` đã lưu — không AC nào yêu cầu.
