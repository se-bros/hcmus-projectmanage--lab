# ĐỀ CƯƠNG ÔN TẬP — NGƯỜI 3: KIẾN TRÚC, POC & BẢN MẪU PROTOTYPE

- **Phạm vi phụ trách:** **Câu 5, Câu 6, Câu 7**
- **Tài liệu tham chiếu chính trong dự án:**
  - [`docs/02-planning/02-architecture.md`](../../docs/02-planning/02-architecture.md)
  - Ảnh giao diện hệ thống trong [`docs/assets/images/`](../../docs/assets/images/)
  - Mã nguồn chạy local trong [`src/`](../../src/)
- **Bản in cần nộp kèm khi thi:** Bản in Sơ đồ Kiến trúc hệ thống và Ảnh chụp màn hình Prototype (Editor split-screen + Reader).

---

## CÂU 5: KIẾN TRÚC PHẦN MỀM (SOFTWARE ARCHITECTURE)

> **Câu hỏi chính:** Trình bày quá trình hình thành và phương pháp đánh giá tài liệu Kiến trúc phần mềm của nhóm.

### 1. Dàn ý trả lời 4 câu hỏi vàng:
* **WHAT (Là gì?):** Là tài liệu đặc tả cấu trúc mức cao của hệ thống, các quyết định công nghệ (Tech Stack Choices), mô hình dữ liệu (Data Models), phân chia tầng (Layered Architecture) và các cơ chế bảo mật (Signed URL, RBAC).
* **HOW (Cách nhóm thực hiện):**
  1. *Lựa chọn Tech Stack:*
     - **Backend:** FastAPI (Python 3.11, quản lý bằng `uv`) — hiệu năng cao, hỗ trợ Async background task xử lý OCR.
     - **Frontend:** React 19 + TypeScript + Vite — phản hồi nhanh, modular component.
     - **Lưu trữ:** MinIO Object Storage (lưu PDF scan và EPUB xuất bản), PostgreSQL (Metadata, Full-text Search FTS).
     - **Core Engines:** Tesseract OCR `vie+eng`, Pandoc chuyển đổi Markdown sang EPUB, Poppler render PDF preview.
  2. *Mô hình Kiến trúc:* Áp dụng mô hình **4+1 Architectural Views** (Logical, Process, Development, Physical + Use Cases).
  3. *Thiết kế Bảo mật:* DRM Reader bảo vệ bản quyền — EPUB không mở public link, mà sinh **MinIO Signed URL có hiệu lực 15 phút** cho độc giả.
* **WHY (Tại sao cần làm?):** Đảm bảo hệ thống vận hành đúng yêu cầu phi chức năng (hiệu năng, mở rộng, bảo mật), tránh việc code chắp vá không kiểm soát.
* **EVIDENCE (Minh chứng dự án):** File `02-architecture.md` mã tài liệu `HCMUS-LDMS-07`, sơ đồ kiến trúc `docs/assets/images/system_architecture.svg`.

---

## CÂU 6: CHỨNG MINH Ý TƯỞNG (PROOF OF CONCEPT — POC)

> **Câu hỏi chính:** Trình bày quá trình hình thành và phương pháp đánh giá sản phẩm Chứng minh ý tưởng (PoC) của nhóm.

### 1. Dàn ý trả lời 4 câu hỏi vàng:
* **WHAT (Là gì?):** Là một bản cài đặt thử nghiệm tối giản nhằm kiểm chứng tính khả thi của công nghệ và chứng minh **bài toán khó nhất** trong dự án có thể giải quyết được trước khi bắt tay vào code toàn bộ hệ thống.
* **HOW (Cách nhóm thực hiện):**
  1. *Xác định bài toán khó nhất:* Xử lý OCR tiếng Việt từ file scan chất lượng kém và tự động đóng gói sang chuẩn EPUB 3.0 mà không làm treo Web API.
  2. *Triển khai PoC 1 (Pipeline OCR):* Tích hợp FastAPI BackgroundTasks + Tesseract OCR `vie+eng` + Poppler, thử nghiệm nhận dạng tài liệu 2 trang mẫu [`samples/two-page.pdf`](../../samples/two-page.pdf).
  3. *Triển khai PoC 2 (DRM Reader):* Kết hợp Epub.js + MinIO Presigned URL 15 phút, chứng minh độc giả đọc mượt mà nhưng không lấy được link tải trực tiếp.
* **WHY (Tại sao cần làm?):** "Fail fast, learn fast" — khử bỏ các rủi ro kỹ thuật lớn nhất ngay từ giai đoạn đầu, tránh lãng phí công sức code giao diện khi công nghệ nền tảng chưa thông suốt.
* **EVIDENCE (Minh chứng dự án):** Mục 5 & 6 trong `02-architecture.md`, kịch bản curl test mẫu chạy thành công trong `README.md`.

---

## CÂU 7: BẢN MẪU (PROTOTYPE)

> **Câu hỏi chính:** Trình bày quá trình hình thành và phương pháp đánh giá sản phẩm Bản mẫu (Prototype) của nhóm.

### 1. Dàn ý trả lời 4 câu hỏi vàng:
* **WHAT (Là gì?):** Là bản dựng giao diện trực quan cho phép người dùng và thủ thư trải nghiệm luồng nghiệp vụ cốt lõi trước khi hoàn thiện 100% tính năng phụ.
* **HOW (Cách nhóm thực hiện):**
  1. *Màn hình Quản trị & Upload (`/documents`):* Cho phép kéo thả file scan PDF, hiển thị tiến độ OCR nền.
  2. *Màn hình Biên tập Split-screen (`/documents/:id`):* Chia đôi màn hình — bên trái hiển thị ảnh scan gốc theo từng trang, bên phải là textarea sửa lỗi chính tả OCR, đồng bộ cuộn và chuyển trang.
  3. *Màn hình Đọc sách (`/reader`):* Đọc sách EPUB responsive với Epub.js, tùy chỉnh font chữ, cỡ chữ, chế độ sáng/tối.
  4. *Đánh giá Prototype:* Cho thủ thư dùng thử trực tiếp để lấy phản hồi về độ tiện dụng của giao diện Split-screen.
* **WHY (Tại sao cần làm?):** Giúp người dùng hình dung rõ ràng sản phẩm, phát hiện sớm các bất tiện trong trải nghiệm UX trước khi đóng băng thiết kế.
* **EVIDENCE (Minh chứng dự án):** Mã nguồn frontend React chạy thực tế tại `http://localhost:5173/documents` và `/reader`.
