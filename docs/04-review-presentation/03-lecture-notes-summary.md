# Tóm tắt Kiến thức Quản lý Dự án (PM) - Các Buổi Học

Tài liệu này tóm tắt toàn bộ kiến thức, quy trình và bài tập thực hành được ghi chép từ Buổi 2 đến Buổi 5 trong môn học Quản lý Dự án Phần mềm.

---

## 📌 Buổi 02: Khởi động & Kỹ thuật Prompt trong QLDA

### 1. Nhiệm vụ & Yêu cầu môn học
* **Đăng ký nhóm**: Nhóm gồm 6 thành viên, yêu cầu tất cả đều đóng góp.
* **Nhiệm vụ nghiên cứu**:
  * Đọc Chương 10 (Áp dụng AI trong quản lý dự án).
  * Đọc Chương 9 (Đề xuất đề tài môn học theo quy tắc chuẩn 2025).
* **Nguyên tắc làm việc với AI**: 
  * Sinh viên phải giải thích rõ ràng và thuyết phục các kết quả/giải pháp được sinh ra từ AI.
  * Ưu tiên sử dụng mô hình mã nguồn mở như *Kiwi, GLM, Qwen* hoặc mua tài khoản *ChatGPT* thay vì *Claude*.

### 2. Kỹ thuật Prompt Engineering trong QLDA
* **Cấu trúc RACFT**:
  * **R**ole (Vai trò)
  * **A**sk (Yêu cầu hành động)
  * **C**ontext (Bối cảnh chi tiết)
  * **F**ormat (Định dạng đầu ra)
  * **T**one (Giọng điệu)
* **Context Engineering**: Cung cấp ngữ cảnh cực kỳ chi tiết (ghi nhật ký ở mức độ cực đoan) để AI hiểu sâu vấn đề.
* **Công cụ hỗ trợ**: Sử dụng extension **JAM** để giám sát và ghi vết (trace) các thao tác trên frontend khi debug.

---

## 📌 Buổi 03: Khởi tạo Dự án (Project Initiation)

Khởi tạo dự án tập trung vào việc trả lời các câu hỏi cốt lõi sau:

| Câu hỏi | Nội dung chi tiết |
| :--- | :--- |
| **WHY** | Tại sao dự án này cần thiết? Xác định vấn đề thực tế (Pain, fear, annoy, high cost, time-consuming). |
| **WHAT** | Dự án sẽ làm cái gì? Định hình ý tưởng và phạm vi. |
| **WHO** | Ai sẽ tham gia? Xác định các Stakeholders (Client, User, Customer, CEO, Director, Internal). |
| **Artifacts** | Các tài liệu bàn giao liên quan. |

### 1. Cách xác định và đánh giá Ý tưởng (Idea)
* **3 nguồn hình thành đề tài**: Ý tưởng cá nhân (Idea từ vấn đề thực tế), Yêu cầu từ khách hàng (RFP - Request for Proposal), hoặc Triển khai lại từ các bài báo khoa học (Paper Implementation).
* **Tiêu chí đánh giá tính hợp lý**:
  * Đã có ai làm chưa? Giải pháp của mình có tốt hơn hoặc rẻ hơn không?
  * Đánh giá thị trường, đối thủ cạnh tranh (kể cả các ứng dụng miễn phí).
  * **Ngân sách (Budget)**: Công cụ lọc các ý tưởng không khả thi. Hãy tự hỏi: *Chúng ta có sẵn sàng mua lại sản phẩm của chính mình với ngân sách đó không?*

### 2. Xây dựng Business Cases & Tài liệu liên quan
* **Business Cases**: Cần xây dựng một câu chuyện có đầu có đuôi, tập trung chủ đề, chứng minh cách giải quyết vấn đề và giá trị mang lại.
* **Quản lý tài nguyên dự án**: Tạo thư mục chứa file `notes.txt`, lưu trữ mã nguồn tương tự, biên bản họp, tận dụng AI Agents và xuất bản ra định dạng PDF.

---

## 📌 Buổi 04: Đánh giá Dự án & Project Charter (WHAT - HOW - WHO)

### 1. Cách tính điểm môn học
Dựa trên 4 yếu tố:
1. **Understanding concepts** (Hiểu khái niệm)
2. **Problem solve** (Giải quyết vấn đề)
3. **Completing work** (Hoàn thành công việc)
4. **Motivation** (Động lực làm việc)

### 2. Quy trình thiết lập Project Proposal & Phản biện Ý tưởng
* **Quy trình**: Executive summary $\rightarrow$ Sponsors/Clients $\rightarrow$ Stakeholders $\rightarrow$ Ước lượng Time/Cost/Resources (với sự hỗ trợ của Agent coding).
* **Feasibility Study**: Đánh giá tính khả thi về mặt luật pháp, kỹ thuật, vận hành, kinh phí... để hoàn thiện **Project Proposal**.
* **Kỹ thuật phản biện ý tưởng với AI**:
  * Hỏi AI $\rightarrow$ Lấy kết quả đem cho AI khác phản biện.
  * Phân biệt giữa LLM (mô hình ngôn ngữ) và Agent (có khả năng gọi công cụ - Tool Calling để tìm kiếm thông tin toàn diện hơn).
  * **MOAT (Tường hào bảo vệ)**: Tìm kiếm rào cản ngăn đối thủ sao chép nhanh (dữ liệu độc quyền, bản quyền). Đánh giá xem có thể giải quyết bằng cách kết hợp các công cụ sẵn có hay bắt buộc phải phát triển mới.

### 3. Thiết kế & Phân tích
* **WHAT** (Phạm vi & Tầm nhìn): Định nghĩa trạng thái hiện tại (Manual) và tương lai (Workflow $\rightarrow$ Features).
* **HOW** (Kiến trúc & Công nghệ): Thiết kế hệ thống, lựa chọn công nghệ.
* **WHO** (Project Charter): Phân tích Stakeholders và phân chia trách nhiệm.
* **Định tính vs. Định lượng**:
  * *Định lượng (Quantitative)*: Đo lường chính xác nhưng cần lưu ý: *"Cái gì đo được thì không còn là thước đo tốt"* (Định luật Goodhart).
  * *Định tính (Qualitative)*: Dùng để đánh giá và điều chỉnh lại định lượng sao cho hợp lý.

---

## 📌 Buổi 05: Quản lý và Lập kế hoạch Dự án (Project Planning & Execution)

Môn học kéo dài trong 7 tuần. Từ tuần 5-7 sẽ tập trung làm đồ án nhóm và ôn thi giữa kỳ.

### 1. Hệ thống hóa Project Initiation (WHY - WHAT - HOW - WHO)
* **Đề tài của nhóm**: *Ứng dụng quản lý tài liệu thư viện* (Số hóa từ bản scan PDF sang EPUB, hỗ trợ category, tags, tìm kiếm nâng cao, phân quyền user).
  * **Quy trình Thủ thư**: Chụp/Quét PDF $\rightarrow$ Chuyển sang EPUB $\rightarrow$ Lưu trữ.
  * **Quy trình Độc giả**: Tìm kiếm $\rightarrow$ Đọc sách & xem vị trí vật lý của sách.
  * **Tiêu chuẩn đánh giá**: Độ chính xác khi chuyển đổi PDF sang EPUB, cấu trúc định dạng có bị vỡ không, tốc độ tìm kiếm.

### 2. Quy trình Lập kế hoạch Dự án (Project Planning)
Giai đoạn này kết thúc khi **Hợp đồng (Contract/SoW) được đóng dấu**.

* **Requirements (Product Backlog - BA)**: Ánh xạ từ Workflow sang các Feature cụ thể kèm theo **Acceptance Criteria** (Tiêu chí nghiệm thu).
* **Architecture & Design**:
  * Chuyển đổi Workflow dạng text sang dạng Diagram (Prototype).
  * Xây dựng **POC (Proof of Concept)** dạng Skeleton với các tính năng cơ bản nhất để kiểm nghiệm công nghệ.
* **Methodology**:
  * *Waterfall*: Phù hợp khi bàn giao hoàn toàn cho Agent làm và sử dụng Playwright để kiểm thử giao diện.
  * *Kanban*: Giám sát độ trễ (gap time) giữa các stories ở trạng thái To-Do và Deployed. Điều tiết số lượng công việc giao cho Agent để tránh quá tải trong khâu Review.
* **Statement of Work (SoW)**: Thỏa thuận rõ ràng về nguồn lực, thời gian, chi phí, công nghệ. Nếu scope thay đổi thì các yếu tố này cũng thay đổi theo.
* **Ước lượng Thời gian**: Dựa vào số lượng User Stories có thể hoàn thành và deploy mỗi tuần (sử dụng LLM để hỗ trợ verify lại).

### 3. Thực thi Dự án (Project Execution)
* **Workflow**: Viết code (tận dụng AI) $\rightarrow$ Chạy Unit Test $\rightarrow$ Deploy $\rightarrow$ Validate $\rightarrow$ Review bởi con người.
* **Monitoring & Reporting (Giám sát & Báo cáo)**:
  * Theo dõi tiến độ hoàn thành, cost, rủi ro, và số lượng **token tiêu thụ**.
  * Báo cáo sau mỗi phiên làm việc với AI: thống kê nội dung hoàn thành, số lượng token, thời gian và chi phí ước tính.
