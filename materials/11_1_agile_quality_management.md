# Quản lý chất lượng linh hoạt (Agile Quality Management)

**Giảng viên / Lecturer:** Ngô Huy Biên (Ngo Huy Bien) — nhbien@fit.hcmus.edu.vn
**Đơn vị / Department:** Bộ môn Kỹ thuật phần mềm, Khoa Công nghệ thông tin, Trường Đại học Khoa học Tự nhiên, ĐHQG-HCM
**Môn học / Course:** Quản lý Dự án Phần mềm (Software Project Management)

---

## 1. Mục tiêu bài học (Learning Objectives)

Sau bài học, người học có thể:

- Cải thiện chất lượng sản phẩm phần mềm.
  _(Improve your software quality.)_
- Cải thiện chất lượng hợp tác và làm việc nhóm.
  _(Improve your team collaboration quality.)_

## 2. Nội dung (Contents Overview)

| #   | Chủ đề (VI)                               | Topic (EN)                         |
| --- | ----------------------------------------- | ---------------------------------- |
| I   | Các kỹ thuật đảm bảo chất lượng linh hoạt | Agile Quality Assurance Techniques |
| II  | Tài liệu hóa trong dự án linh hoạt        | Documentation in Agile Projects    |
| III | Họp hồi tưởng (Retrospectives)            | Retrospective Meetings             |

---

## I. Các kỹ thuật đảm bảo chất lượng linh hoạt (Agile QA Techniques)

### 1.1 Tạo tiêu chuẩn mã hóa (Coding Standards) \[1\]

Thiết lập các tiêu chuẩn và quy ước mã nguồn thống nhất trong nhóm, tránh để tiêu chuẩn mã hóa trở thành vấn đề gây bất hòa:

- Quy ước định dạng code (Formatting).
- Thống nhất công cụ phát triển và IDE.
- Bố cục tệp tin và cấu trúc thư mục (File and directory layout).
- Cơ chế xử lý lỗi (Error handling).
- Cách thức tiếp cận xử lý sự kiện (Approach to events).
- Cơ chế ghi nhật ký hệ thống (Logging).

### 1.2 Viết kiểm thử đơn vị (Unit Testing)

- Tạo các unit test để kiểm tra mã nguồn tự động ở cấp độ hàm/mô-đun.
- Tích hợp chạy unit test tự động trong quy trình CI/CD/DevOps (như Cypress cho E2E Testing).

### 1.3 Thử nghiệm thăm dò (Exploratory Testing)

Tìm lỗi thủ công dựa trên việc thăm dò các kịch bản bất thường của các kiểu dữ liệu thường gặp:

- Giá trị biên đặc biệt: Không (zero), một (one), nhiều (many), quá lớn (too big), quá nhỏ (too small).
- Kiểm tra các thao tác dữ liệu: Create, Read, Update, Delete (CRUD).
- Kiểm tra độ khớp của các kiểu dữ liệu (data types).

### 1.4 Đánh giá mã nguồn (Code Inspection) & Thiết kế đơn giản (Simple Design)

Đảm bảo mã nguồn tuân thủ thiết kế đơn giản:

- **Phù hợp với người đọc (Appropriate for audience):** Dù thiết kế có sang xịn đến đâu, nếu những người làm việc trực tiếp không hiểu được thì nó không phải là thiết kế đơn giản.
- **Tính truyền đạt (Communicative):** Mọi ý tưởng cần truyền đạt đều được thể hiện tường minh trong hệ thống.
- **Tính phân rã tốt (Factored):** Không trùng lặp logic hoặc cấu trúc (tác nhân gây khó đọc và khó sửa đổi).
- **Tối giản (Minimal):** Trong phạm vi các ràng buộc trên, hệ thống cần có ít thành phần nhất có thể để giảm thiểu chi phí test, tài liệu hóa và giao tiếp.

### 1.5 Nhận diện mùi mã nguồn (Code Smells) và Tái cấu trúc (Refactoring)

- **Thay đổi phân kỳ (Divergent Change):** Xảy ra khi các thay đổi không liên quan cùng làm ảnh hưởng đến một lớp duy nhất (vi phạm nguyên tắc Single Responsibility).
- **Phẫu thuật súng thối (Shotgun Surgery):** Ngược lại với Divergent Change, xảy ra khi phải sửa đổi rất nhiều lớp khác nhau chỉ để hỗ trợ thay đổi cho một ý tưởng duy nhất.
- **Phụ thuộc thời gian (Time Dependencies):** Xảy ra khi các phương thức của lớp phải được gọi theo một thứ tự cụ thể (lỗi đóng gói khi bắt đối tượng gọi quản lý hộ trạng thái của lớp).
- **Đối tượng nửa sống nửa chín (Half-Baked Objects):** Một dạng của Time Dependency, đối tượng bắt buộc phải được tạo trước, rồi gọi hàm khởi tạo (init), rồi mới sử dụng được.

---

## II. Tài liệu hóa trong dự án linh hoạt (Documentation in Agile Projects)

- Tài liệu trong Agile (như bảng tầm nhìn, thẻ story) đóng vai trò là **lời nhắc nhở (reminders)** nhiều hơn là các tài liệu chính thức cồng kềnh.
- Vẫn cần sản xuất các tài liệu cung cấp giá trị kinh doanh thực tế: Hướng dẫn sử dụng (user manuals), tài liệu tham khảo API (API references) và các báo cáo cần thiết.
- **Tài liệu bàn giao (Handoff documentation):** Một bộ tài liệu tinh gọn ghi nhận các quyết định lớn và thông tin cốt lõi nhất để duy trì và bảo trì hệ thống lâu dài.

> **Định nghĩa hoàn thành (Definition of Done - DoD):**
> _"Chúng tôi chỉ thực sự hoàn thành khi sản phẩm đã sẵn sàng đưa vào môi trường sản xuất thực tế."_
> _(We’re done when we’re production-ready.)_

---

## III. Họp hồi tưởng (Retrospectives) \[2\]

Được tiến hành vào cuối mỗi lần lặp (Sprint) nhằm cải tiến quy trình của nhóm.

### 3.1 Thiết lập bối cảnh (Set the stage)

Mọi thành viên cùng đồng thuận với nguyên tắc tối cao của buổi Retrospective:

> _"Bất kể chúng ta phát hiện ra điều gì hôm nay, chúng ta hiểu và thực sự tin rằng tất cả mọi người đã làm công việc tốt nhất có thể, xét trong điều kiện hoàn cảnh lúc đó, với kiến thức, kỹ năng của họ, các tài nguyên sẵn có và tình hình thực tế."_
> _(Regardless of what we discover today, we understand and truly believe that everyone did the best job they could, given what they knew at the time, their skills and abilities, the resources available, and the situation at hand.)_

### 3.2 Động não thu thập ý kiến (Brainstorming)

Sử dụng thẻ chỉ mục (index cards) để ghi nhận cảm nhận của các thành viên theo các nhóm trạng thái:

- **Làm nản lòng (Frustrating):** Nhiều hơn / Như cũ / Ít hơn?
- **Thú vị (Enjoyable):** Nhiều hơn / Như cũ / Ít hơn?
- **Khó hiểu (Puzzling):** Nhiều hơn / Như cũ / Ít hơn?

### 3.3 Phân loại thẻ (Mute Mapping)

Các thành viên di chuyển các thẻ có nội dung liên quan lại gần nhau và đặt các thẻ không liên quan ra xa mà **không trò chuyện** (no talking). Tiến hành khoanh tròn các nhóm và đặt tên cho từng danh mục.

### 3.4 Biểu quyết mục tiêu cải tiến (Retrospective Objective)

- Mỗi người có **5 phiếu bầu** để bình chọn cho các danh mục cần cải tiến nhất. Có thể dồn phiếu hoặc chia đều.
- Chọn ra danh mục chiến thắng có số phiếu cao nhất (hoặc tung đồng xu nếu bằng phiếu) để tập trung cải thiện trong Sprint tiếp theo.
- Động não ý kiến cải tiến, áp dụng các kỹ thuật phân tích nguyên nhân gốc rễ (_Five Whys, Force Field Analysis, Fishbone Diagram_), viết các mục hành động thành các user story để đưa vào Sprint Backlog tiếp theo.

---

## Tài liệu tham khảo (References)

1. James Shore & Shane Warden (2008). _The Art of Agile Development_. O'Reilly.
2. Esther Derby & Diana Larsen (2006). _Agile Retrospectives: Making Good Teams Great_. Pragmatic Bookshelf.
