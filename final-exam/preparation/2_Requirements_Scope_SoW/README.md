# ĐỀ CƯƠNG ÔN TẬP — NGƯỜI 2: YÊU CẦU NGHIỆP VỤ, PHẠM VI & SOW

- **Phạm vi phụ trách:** **Câu 2, Câu 4, Câu 12**
- **Tài liệu tham chiếu chính trong dự án:**
  - [`docs/02-planning/01-vision-and-scope.md`](../../../docs/02-planning/01-vision-and-scope.md)
  - [`docs/02-planning/03-product-backlog.md`](../../../docs/02-planning/03-product-backlog.md)
  - [`docs/02-planning/05-statement-of-work.md`](../../../docs/02-planning/05-statement-of-work.md)
- **Hạn chót hoàn thành đề cương (Bước 1):** **20:00, Thứ Năm (20/08/2026)**
- **Bản in cần nộp kèm khi thi:** Bản in file `01-vision-and-scope.md` và `03-product-backlog.md`.

---

## CÂU 2: VIỄN CẢNH VÀ PHẠM VI DỰ ÁN (PROJECT VISION & SCOPE)

> **Câu hỏi chính:** Trình bày quá trình hình thành và phương pháp đánh giá tài liệu Viễn cảnh và phạm vi dự án của nhóm.

### 1. Dàn ý trả lời 4 câu hỏi vàng:
* **WHAT (Là gì?):** Định nghĩa bức tranh tổng thể tương lai của sản phẩm, so sánh quy trình nghiệp vụ hiện tại (As-Is: thủ công rời rạc) với quy trình mới (To-Be: số hóa tự động hóa khép kín), phân định rõ ràng ranh giới trong phạm vi (In-Scope) và ngoài phạm vi (Out-of-Scope).
* **HOW (Cách nhóm thực hiện):**
  1. Vẽ sơ đồ luồng quy trình hiện tại: Quét thủ công $\rightarrow$ Lưu PDF ảnh $\rightarrow$ Upload Google Drive $\rightarrow$ Không tìm kiếm được nội dung bên trong sách.
  2. Thiết kế luồng quy trình tương lai (To-Be): Upload $\rightarrow$ Tesseract OCR tự động $\rightarrow$ Soát lỗi Split-screen $\rightarrow$ Biên dịch Pandoc sang EPUB $\rightarrow$ Đọc trực tiếp trên web với DRM.
  3. Phân định phạm vi: Bản MVP tập trung vào 16 stories Must-have, hoãn các tính năng phức tạp (như Audio book, AI Chatbot hỏi đáp tài liệu) sang giai đoạn sau.
* **WHY (Tại sao cần làm?):** Giúp toàn bộ nhóm và khách hàng có chung một góc nhìn (Shared Vision), tránh hiện tượng "phình phạm vi" (Scope Creep) làm trễ hạn dự án.
* **EVIDENCE (Minh chứng dự án):** Bảng so sánh 6 tiêu chí quy trình As-Is vs To-Be trong `01-vision-and-scope.md` mục 3.

---

## CÂU 4: YÊU CẦU PHẦN MỀM & PRODUCT BACKLOG

> **Câu hỏi chính:** Trình bày quá trình hình thành và phương pháp đánh giá tài liệu Yêu cầu phần mềm / Product Backlog của nhóm.

### 1. Dàn ý trả lời 4 câu hỏi vàng:
* **WHAT (Là gì?):** Là danh sách ưu tiên toàn bộ các tính năng người dùng mong muốn, được viết dưới dạng User Story chuẩn (`As a <role>, I want to <feature> so that <benefit>`) kèm theo Tiêu chí nghiệm thu (Acceptance Criteria - AC) rõ ràng và Tiêu chuẩn hoàn thành (Definition of Done - DoD).
* **HOW (Cách nhóm thực hiện):**
  1. Phân rã từ Vision & Scope thành **4 Epic lớn** và **26 User Stories** (LDMS-001 đến LDMS-026).
  2. Gắn độ ưu tiên theo phương pháp **MoSCoW**: 16 Must, 6 Should, 4 Could.
  3. Viết Acceptance Criteria chi tiết cho từng Story theo cấu trúc kịch bản kiểm thử rõ ràng.
  4. Đặt ra quy tắc **DoD 5 tiêu chí**: Code clean & test pass, tích hợp local docker, không lỗi bảo mật, review chéo 1 approve, ghi nhật ký log token/effort.
* **WHY (Tại sao cần làm?):** Là kim chỉ nam cho các Sprint, là cơ sở để dev lấy việc, test kiểm thử và PM nghiệm thu bàn giao.
* **EVIDENCE (Minh chứng dự án):** File `03-product-backlog.md` mã tài liệu `HCMUS-LDMS-08` dài 26 User Stories chuẩn mực.

---

## CÂU 12: PHÁT BIỂU CÔNG VIỆC (STATEMENT OF WORK — SOW)

> **Câu hỏi chính:** Trình bày quá trình hình thành và phương pháp đánh giá tài liệu Phát biểu công việc (SoW) của nhóm.

### 1. Dàn ý trả lời 4 câu hỏi vàng:
* **WHAT (Là gì?):** Là hợp đồng kỹ thuật và cam kết pháp lý giữa Đội ngũ phát triển và Đơn vị thụ hưởng (Thư viện trường), xác định rõ ràng: Phạm vi sản phẩm bàn giao (Deliverables), Lịch trình bàn giao, Chi phí thống nhất, và Quy chế kiểm soát thay đổi (Change Control).
* **HOW (Cách nhóm thực hiện):**
  1. Thiết lập **Nguyên tắc liên động Tam giác ràng buộc (Scope–Feature–Resource)**: Nếu khách hàng yêu cầu thêm tính năng mới, bắt buộc phải tăng thêm thời gian/ngân sách hoặc cắt giảm tính năng tương đương.
  2. Thiết lập quy trình 4 bước xử lý Change Request (Gửi yêu cầu $\rightarrow$ Đánh giá tác động $\rightarrow$ Phê duyệt $\rightarrow$ Cập nhật hợp đồng).
  3. Thống nhất danh mục 6 gói sản phẩm bàn giao (Deliverables) cụ thể.
* **WHY (Tại sao cần làm?):** Bảo vệ nhóm phát triển trước các yêu cầu vô lý phát sinh giữa chừng từ khách hàng, đảm bảo tính minh bạch về tài chính và tiến độ.
* **EVIDENCE (Minh chứng dự án):** File `05-statement-of-work.md` mã tài liệu `HCMUS-LDMS-10`, bao gồm đầy đủ chữ ký giả định giữa Đại diện Thư viện và Project Manager.
