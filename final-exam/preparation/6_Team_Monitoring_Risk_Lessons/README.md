# ĐỀ CƯƠNG ÔN TẬP — NGƯỜI 6: QUẢN TRỊ NHÂN SỰ, GIÁM SÁT, RỦI RO & BÀI HỌC

- **Phạm vi phụ trách:** **Câu 16, Câu 17, Câu 18, Câu 19, Câu 21**
- **Tài liệu tham chiếu chính trong dự án:**
  - [`docs/01-initiation/05-team-contract.md`](../../docs/01-initiation/05-team-contract.md) (Lý thuyết Y & Chính sách phòng ngừa xung đột)
  - [`docs/03-execution-monitoring/02-project-log.md`](../../docs/03-execution-monitoring/02-project-log.md) (Nhật ký thực thi & số liệu token)
  - [`docs/03-execution-monitoring/03-ai-development-workflow.md`](../../docs/03-execution-monitoring/03-ai-development-workflow.md) (Báo cáo quy trình AI)
- **Bản in cần nộp kèm khi thi:** Bản in file `05-team-contract.md`, `02-project-log.md` và `03-ai-development-workflow.md`.

---

## CÂU 16: QUẢN LÝ CON NGƯỜI VÀ PHÁT TRIỂN NHÓM

> **Câu hỏi chính:** Trình bày quá trình hình thành và phát triển nhóm mà nhóm đã trải qua. Liệt kê các vấn đề nhóm gặp phải và cách giải quyết.

### 1. Dàn ý trả lời:
* **Triết lý Quản trị Lý thuyết Y (Douglas McGregor):** Nhóm tin tưởng thành viên luôn siêng năng, có tinh thần tự giác cao và khao khát hoàn thành công việc. Áp dụng cơ chế **Tự chọn Task (Self-Selection)** trên Kanban và **Tự báo cáo Tiến độ (Self-Reporting)** thay vì ép buộc phân công vi mô.
* **5 Giai đoạn phát triển nhóm (Mô hình Tuckman):**
  1. *Forming (Thành lập):* Thống nhất Hợp đồng nhóm `05-team-contract.md`, chọn công cụ giao tiếp.
  2. *Storming (Sóng gió):* Bất đồng quan điểm về tech stack (DSpace vs Tự phát triển, PostgreSQL FTS vs Elasticsearch). Giải quyết bằng dữ liệu benchmark PoC và biểu quyết dân chủ.
  3. *Norming (Ổn định):* Thiết lập 3 chính sách tiền lệ (Policy 1: Minh bạch Log trong 12h; Policy 2: 100% code qua PR Review; Policy 3: Báo bận trước 24h).
  4. *Performing (Bứt phá):* Tăng tốc lập trình cùng AI Coding Assistant, đạt tốc độ hoàn thành 17 story/tuần.
  5. *Adjourning (Kết thúc):* Tổng kết bài học kinh nghiệm và chuyển giao sản phẩm.

---

## CÂU 17: PHÂN CÔNG, THEO DÕI, KIỂM SOÁT CÔNG VIỆC VÀ BÁO CÁO DỰ ÁN

> **Câu hỏi chính:** Trình bày quá trình phân công, theo dõi, đánh giá, kiểm soát các công việc dự án, và báo cáo tình trạng dự án.

### 1. Dàn ý trả lời:
* **Theo dõi Tiến độ thực tế:** Sử dụng Kanban Board, theo dõi độ trễ (gap time) từ To-Do $\rightarrow$ Done.
* **Ghi nhận Số liệu Thực tế với AI:** Mỗi thành viên ghi log sau phiên làm việc vào `02-project-log.md`:
  - Tổng thời gian: **14 giờ 05 phút**.
  - Tổng token tiêu thụ: **730.000 tokens** (trung bình ~13K–14K token/Story Point).
  - Chi phí AI: ~350.000 VNĐ $\ll$ 5.000.000 VNĐ ngân sách AI cho phép.
* **Xử lý Điểm nghẽn (Blocker):** Họp Daily Standup ngắn gọn 10 phút để giải tỏa blocker kỹ thuật ngay trong ngày.

---

## CÂU 18: KẾ HOẠCH QUẢN LÝ RỦI RO (RISK MANAGEMENT PLAN)

> **Câu hỏi chính:** Trình bày quá trình hình thành và phương pháp đánh giá tài liệu Kế hoạch quản lý rủi ro của nhóm.

### 1. Dàn ý trả lời:
* **Quy trình 4 bước:** Nhận diện $\rightarrow$ Đánh giá ma trận Xác suất × Tác động (P×I) $\rightarrow$ Lập kế hoạch ứng phó $\rightarrow$ Giám sát định kỳ.
* **3 Rủi ro lớn nhất của dự án và giải pháp:**
  1. *Rủi ro Bản quyền học liệu:* Khắc phục bằng cơ chế DRM Signed URL có hiệu lực 15 phút, không cung cấp nút download file gốc.
  2. *Rủi ro Chất lượng OCR tiếng Việt:* Khắc phục bằng giao diện Split-screen cho phép thủ thư đối soát và sửa lỗi chính tả trực quan.
  3. *Rủi ro Token AI vượt ngân sách:* Khắc phục bằng kỹ thuật Prompt Spec-driven và quy định hạn mức 5 triệu VNĐ.

---

## CÂU 19: KẾ HOẠCH QUẢN LÝ CHẤT LƯỢNG (QUALITY MANAGEMENT PLAN)

> **Câu hỏi chính:** Trình bày quá trình hình thành và phương pháp đánh giá tài liệu Kế hoạch quản lý chất lượng của nhóm.

### 1. Dàn ý trả lời:
* **Chỉ số Chất lượng Định lượng (Quality Metrics):**
  - Tỷ lệ lỗi nhận dạng ký tự OCR: CER < 5% trên văn bản in tiêu chuẩn.
  - Thời gian phản hồi API tra cứu FTS: < 500ms cho 100 trang sách.
  - Test Coverage: Đạt tối thiểu 80% coverage cho tầng Service và Repository.
* **Quy trình Đảm bảo Chất lượng (QA/QC):**
  - **QA (Phòng ngừa lỗi):** Thiết lập quy tắc coding style, linter tự động, quy trình spec-driven.
  - **QC (Phát hiện lỗi):** Bộ test tự động CI, thủ thư nghiệm thu UAT thực tế trên tài liệu mẫu.

---

## CÂU 21: BÁO CÁO BÀI HỌC KINH NGHIỆM (LESSONS LEARNED REGISTER)

> **Câu hỏi chính:** Trình bày quá trình hình thành và phương pháp đánh giá tài liệu Báo cáo bài học kinh nghiệm của nhóm.

### 1. Dàn ý trả lời:
* **Các bài học đắt giá rút ra từ dự án:**
  1. *Về Ứng dụng AI:* AI không thể thay thế kiến trúc sư phần mềm — nếu không có bản Spec và thiết kế Data Model rõ ràng, code AI sinh ra sẽ bị rời rạc và lỗi logic. Kỹ thuật Context Engineering là chìa khóa để tiết kiệm token.
  2. *Về Lựa chọn Công nghệ:* Chọn giải pháp đơn giản và đủ tốt (PostgreSQL FTS thay vì dựng cụm Elasticsearch phức tạp) giúp giảm 60% gánh nặng vận hành.
  3. *Về Phối hợp Nhóm:* Minh bạch hoá tiến độ và nhật ký log token giúp loại bỏ hoàn toàn sự nghi ngờ về đóng góp của các thành viên.
