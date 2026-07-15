# Giám sát và Kiểm soát Dự án Linh hoạt (Agile Project Monitoring and Control)

**Giảng viên / Lecturer:** Ngô Huy Biên (Ngo Huy Bien) — nhbien@fit.hcmus.edu.vn
**Đơn vị / Department:** Bộ môn Kỹ thuật phần mềm, Khoa Công nghệ thông tin, Trường Đại học Khoa học Tự nhiên, ĐHQG-HCM
**Môn học / Course:** Quản lý Dự án Phần mềm (Software Project Management)

---

## 1. Mục tiêu bài học (Learning Objectives)

Sau bài học, người học có thể:

- Theo dõi và kiểm soát dự án linh hoạt.
  *(Monitor and control agile project.)*
- Báo cáo tình trạng dự án một cách hiệu quả.
  *(Report project status.)*
- Đánh giá kết quả của từng lần lặp và dự án.
  *(Evaluate project results.)*
- Đánh giá năng suất của nhóm phát triển.
  *(Evaluate team productivity.)*

## 2. Nội dung (Contents Overview)

| # | Chủ đề (VI) | Topic (EN) |
|---|---|---|
| I | Lập dòng thời gian & Họp độc lập hàng ngày | Project Timeline & Daily Stand-Up Meetings |
| II | Nguyên tắc làm việc nhóm và ra quyết định | Teamwork & Decision-Making Principles |
| III | Quản lý thay đổi & Cập nhật kế hoạch | Change Management & Plan Updates |
| IV | Báo cáo trạng thái & Chỉ số hiệu suất | Status Reporting & Performance Metrics |

---

## I. Lập dòng thời gian & Họp độc lập hàng ngày (Project Timeline & Daily Stand-Up)

### 1.1 Tạo dòng thời gian dự án (Create Project Timeline)
Thiết lập tiến độ bàn giao sản phẩm cho từng giai đoạn của dự án.
*(Establish the timeline for deliverables for each phase of the project.)*
Các công cụ trực quan hóa phổ biến: MS Visio, Lucidchart.

### 1.2 Họp độc lập hàng ngày (Daily Stand-Up Meetings) \[1\]
Mỗi thành viên trả lời 3 câu hỏi cốt lõi hàng ngày để đồng bộ công việc:
1. Hôm qua tôi đã làm gì?
   *(What did I do yesterday?)*
2. Hôm nay tôi sẽ làm gì?
   *(What will I do today?)*
3. Những vấn đề nào đang ngăn cản tôi tiến bộ?
   *(What problems are preventing me from making progress?)*

### 1.3 Xử lý khi công việc đi chệch hướng
Khi có sự cố xảy ra, hãy áp dụng các biện pháp:
- Sử dụng thời gian dự phòng lặp lại (iteration slack).
  *(Use iteration slack.)*
- Đơn giản hóa hoặc trì hoãn một nhiệm vụ kỹ thuật chưa cấp bách.
  *(Simplify or postpone an engineering task.)*
- Giảm phạm vi: Chia nhỏ hoặc loại bỏ user story khỏi Sprint.
  *(Reduce the scope: split or remove a story.)*

> **Nguyên tắc:** Luôn giữ quyền kiểm soát việc lặp lại (iteration) của bạn, ngay cả khi phải thay đổi kế hoạch. Một iteration thành công là khi bàn giao được tất cả story trong kế hoạch hiện tại (dù kế hoạch đó đã được điều chỉnh).
> **Tuyệt đối không thay đổi thời hạn lặp lại (deadline của Sprint).**
> *(Under no circumstances should you change the iteration deadline.)*

---

## II. Nguyên tắc làm việc nhóm và ra quyết định (Teamwork & Decision-Making)

### 2.1 Môi trường bình đẳng (An Environment of Equality)
Các nhà phát triển có kỹ năng kém hơn cũng cần có cơ hội đưa ra ý kiến và thay đổi đóng góp giá trị cho nhóm.
*(Lesser-skilled developers should be able to bring ideas and changes to the team which may be valuable.)*
> *"Không có cái tôi trong tập thể. Không bỏ lại ai phía sau."*
> *(There's no "I" in Team. Leave no man behind.)*

### 2.2 Đưa ra quyết định công nghệ
Khi quyết định áp dụng công nghệ hay chuẩn mực kỹ thuật (như viết Unit Test), người lãnh đạo không nên giả định mình luôn biết mọi thứ tốt nhất. Phải giải thích **TẠI SAO** đó là hướng đi đúng đắn bằng các lập luận kỹ thuật thuyết phục.
*(Explain WHY it's the right way to follow with technical justifications.)*

### 2.3 Phân vai và chống độc quyền kiến thức (Understudy)
Khuyến khích mọi người làm việc theo thế mạnh của mình, nhưng tránh tình trạng chỉ có duy nhất một người hiểu và kiểm soát hoàn toàn một mảng nghiệp vụ hoặc công nghệ cụ thể.
*(Let people do what they're good at, but not to the extent where they are the only one who knows what's going on with that area.)*

### 2.4 Không sở hữu mã nguồn cá nhân (Collective Code Ownership)
Khi mã nguồn đã được đưa lên hệ thống kiểm soát phiên bản (source control), đó không còn là mã nguồn "của bạn" nữa, nó thuộc về **toàn bộ nhóm**.
*(Once you write code and check it in, it's no longer 'your' code, it's the team’s.)*
- Bất kỳ thành viên nào cũng có quyền chỉnh sửa mã nguồn của nhóm để cải tiến hoặc sửa lỗi.
- Không được tự ý revert (khôi phục lại) mã nguồn của người khác khi chưa thảo luận và thống nhất.

### 2.5 Các nguyên tắc kỹ thuật bắt buộc (Technical No-No's)
- **Không check-in một phần:** Đảm bảo code chạy ổn định hoàn toàn trước khi commit.
- **Chạy tất cả unit tests** và đảm bảo chúng pass trước khi check-in.
- **Không thay đổi công nghệ nền tảng** hoặc cấu trúc thư mục/mã nguồn khi chưa thảo luận thống nhất trong nhóm.
- **Không tự ý thêm thư viện liên kết mới** (dependencies).
- Đảm bảo các hoạt động của mình không làm tắc nghẽn công việc của người khác.

---

## III. Quản lý thay đổi & Cập nhật kế hoạch (Change Management & Plan Updates)

### 3.1 Quản lý thay đổi trong Agile
Thích ứng linh hoạt với thay đổi thay vì đóng cứng kế hoạch từ đầu đến cuối (khác với mô hình RUP truyền thống).
- Product Owner chịu trách nhiệm quản lý Product Backlog và thực hiện việc chăm chút, tinh chỉnh backlog (backlog grooming).
- Đảm bảo thực hiện phân tích, tài liệu và thiết kế ở mức độ **vừa đủ** để bàn giao sớm nhằm tạo ra giá trị kinh doanh thực tế giải quyết vấn đề của khách hàng.

### 3.2 Cập nhật kế hoạch phát hành (Update Release Plan)
Khi kết thúc mỗi Sprint, tiến hành đánh giá và cập nhật kế hoạch phát hành của các phiên bản tiếp theo dựa trên vận tốc thực tế (tái cấu trúc lại các PBI thuộc các Release 1, 2, 3...).

---

## IV. Báo cáo trạng thái & Chỉ số hiệu suất (Status Reporting & Metrics)

### 4.1 Báo cáo trạng thái dự án (Project Status Report)
Nội dung báo cáo trạng thái định kỳ:
- **Phạm vi hoàn thành (Percent completed):** Được tính bằng `Số điểm đã hoàn thành / Tổng số điểm`.
- **Ngày hoàn thành dự kiến:** Được tính bằng `Tổng số điểm / Vận tốc (Velocity) = Số Sprint cần thiết`.
- **Sử dụng ngân sách** và ước tính chi phí cuối cùng.
- Các vấn đề phát sinh và hướng giải quyết (Issues & Resolutions).
- Thay đổi và tác động của chúng (Changes & Impacts).
- Trạng thái Product Backlog cập nhật (Stories được thêm, xóa hoặc hoàn thành).
- Rủi ro có xác suất xảy ra và tác động cao.
- Trạng thái các sản phẩm bàn giao (phần mềm chạy được và tài liệu).

### 4.2 Các báo cáo quản lý cần xem xét
- **Năng suất (Productivity) & Thông lượng (Throughput):** Thông lượng là số lượng tính năng nhóm phát triển được trong một khoảng thời gian cụ thể.
- **Lỗi (Defects)** tồn đọng và xu hướng phát sinh lỗi.
- **Sử dụng thời gian (Time usage).**

### 4.3 Các báo cáo cần TRÁNH
- **Dòng mã nguồn (SLOC) hoặc Điểm chức năng (FP):** Báo cáo số dòng code sẽ khuyến khích lập trình viên viết code dài dòng, dễ phát sinh lỗi và làm tăng chi phí bảo trì.
- **Số lượng câu chuyện (Number of stories):** Thiếu tính khách quan do kích thước các story khác nhau.
- **Vận tốc (Velocity):** **Tuyệt đối không so sánh vận tốc giữa các nhóm khác nhau** (Never compare velocity across teams) vì mỗi nhóm có cách ước tính điểm số riêng biệt.
- **Chất lượng mã (Độ phức tạp Cyclomatic):** Công cụ này tốt cho nhà phát triển nhưng quá mơ hồ đối với các bên liên quan (stakeholders).

### 4.4 Hướng dẫn báo cáo hiệu quả
- Báo cáo phù hợp xây dựng niềm tin của stakeholders đối với nhóm. Theo thời gian khi độ tin cậy tăng lên, tần suất và lượng thông tin báo cáo có thể giảm dần.
- Thời gian làm báo cáo thủ công là thời gian lãng phí vì không đóng góp trực tiếp vào tiến độ phát triển.
- Hãy tận dụng tối đa các **biểu đồ tự động** từ công cụ quản trị (như biểu đồ Burndown Chart, Burnup Chart, bảng Kanban/Scrum, các buổi Iteration Demo) để làm báo cáo trực quan cho stakeholders bất cứ khi nào có thể.

---

## Tài liệu tham khảo (References)

1. James Shore & Shane Warden (2008). *The Art of Agile Development*. O'Reilly.
