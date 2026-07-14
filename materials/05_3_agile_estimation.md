# Ước tính linh hoạt (Agile Estimation)

**Giảng viên / Lecturer:** Ngô Huy Biên (Ngo Huy Bien) — nhbien@fit.hcmus.edu.vn
**Đơn vị / Department:** Bộ môn Kỹ thuật phần mềm, Khoa Công nghệ thông tin, Trường Đại học Khoa học Tự nhiên, ĐHQG-HCM
**Môn học / Course:** Quản lý Dự án Phần mềm (Software Project Management)

---

## 1. Mục tiêu bài học (Learning Objectives)

Sau bài học, người học có thể:

- Ước tính kích thước theo điểm câu chuyện (story points).
  *(Estimate size in story points.)*
- Ước tính kích thước bằng phương pháp Planning Poker.
  *(Estimate size using planning poker method.)*
- Ước tính kích thước bằng phương pháp Wideband Delphi.
  *(Estimate size using Wideband Delphi method.)*

## 2. Nội dung (Contents Overview)

| # | Chủ đề (VI) | Topic (EN) |
|---|---|---|
| I | Điểm câu chuyện và Vận tốc | Story Points and Velocity |
| II | Ngày lý tưởng | Ideal Days |
| III | Thang đo ước tính | Estimation Scale |
| IV | Các phương pháp đưa ra ước tính | Methods for Deriving Estimates |
| V | Planning Poker | Planning Poker |
| VI | Phương pháp Wideband Delphi | Wideband Delphi Method |

---

## I. Điểm câu chuyện và Vận tốc (Story Points and Velocity) \[1\]

### 1.1 Điểm câu chuyện (Story Points)

> Điểm câu chuyện là đơn vị đo lường để thể hiện tổng thể kích thước của một user story, tính năng hoặc phần công việc khác.
> *(Story points are a unit of measure for expressing the overall size of a user story, feature, or other piece of work.)*

- Giá trị thô được gán không quan trọng. Điều quan trọng là **các giá trị tương đối**.
  *(The raw value we assign is unimportant. What matters are the relative values.)*
- Một câu chuyện được giao 2 điểm nên có khối lượng gấp đôi một câu chuyện được giao 1 điểm.
  *(A story assigned a two should be twice as much as a story assigned a one.)*

### 1.2 Vận tốc (Velocity)

Vận tốc là thước đo tốc độ tiến bộ của một nhóm.
*(Velocity is a measure of a team's rate of progress.)*

- Được tính bằng cách tổng hợp số điểm câu chuyện của tất cả user story mà nhóm đã hoàn thành trong suốt một lần lặp.
  *(Calculated by summing the number of story points of each user story the team completed during the iteration.)*
- Ví dụ: Nhóm hoàn thành 3 câu chuyện, mỗi câu chuyện ước tính 5 điểm → Vận tốc = 15.

---

## II. Ngày lý tưởng (Ideal Days)

Ngày lý tưởng là đơn vị ước tính thay thế cho điểm câu chuyện, giả định:
- Câu chuyện được ước tính là **việc duy nhất** bạn làm.
  *(The story being estimated is the only thing you'll work on.)*
- Mọi thứ cần thiết **sẵn sàng** khi bạn bắt đầu.
  *(Everything you need will be on hand when you start.)*
- **Không có sự gián đoạn** nào xảy ra.
  *(There will be no interruptions.)*

Khi ước tính bằng ngày lý tưởng, tốt nhất nên **kết hợp một ước tính duy nhất** với từng user story.

Thay vì ước tính riêng lẻ (4 ngày lập trình + 2 ngày kiểm tra + 3 ngày product owner), tốt hơn là nói câu chuyện đó tốn **9 ngày lý tưởng** tổng cộng.

---

## III. Thang đo ước tính (Estimation Scale)

Các thang đo phi tuyến phản ánh tốt hơn sự không chắc chắn liên quan đến ước tính cho các đơn vị công việc lớn hơn:

- **Dãy Fibonacci:** 1, 2, 3, 5, 8 — khoảng cách giữa các số trở nên lớn hơn theo cách phù hợp. Số tiếp theo = tổng 2 số liền trước.
  *(1, 2, 3, 5, 8 — the gaps become appropriately larger as numbers increase.)*
- **Dãy nhân đôi:** 1, 2, 4, 8 — mỗi số gấp đôi số liền trước.
  *(1, 2, 4, 8 — each number is twice the number that precedes it.)*

> **Lưu ý:** Nếu nhóm đưa số 0 vào thang đo, mọi người cần hiểu rằng 13 × 0 ≠ 0 (vẫn có chi phí quản lý).
> *(If the team elects to include 0, everyone needs to understand that 13 × 0 ≠ 0.)*

---

## IV. Các phương pháp đưa ra ước tính (Deriving Estimates) \[1, 2\]

### 4.1 Tương tự (Analogy)

Đánh giá mỗi câu chuyện mới dựa trên những thứ đã được ước tính trước đó, so sánh tương đối với nhau.
*(Estimate each new story against an assortment of those that have already been estimated.)*

### 4.2 Phân chia (Disaggregation)

Chia một câu chuyện hoặc tính năng thành các phần nhỏ hơn, dễ ước tính hơn.
*(Splitting a story or feature into smaller, easier-to-estimate pieces.)*

Nếu hầu hết user story trong dự án có phạm vi 2-5 ngày, rất khó ước tính một câu chuyện có thể là 100 ngày — cần phân chia trước.

### 4.3 Ý kiến chuyên gia (Expert Opinion)

Cách tiếp cận này ít hữu ích hơn trong dự án Agile so với dự án truyền thống, vì:
*(This approach is less useful on agile projects than on traditional projects, because:)*
- Ước tính được gán cho user story đòi hỏi nhiều kỹ năng khác nhau, thường do nhiều người thực hiện.
- Khó tìm chuyên gia phù hợp có thể đánh giá nỗ lực trên tất cả các lĩnh vực.

---

## V. Planning Poker \[1\]

Planning Poker kết hợp ý kiến chuyên gia, so sánh và phân chia thành một cách tiếp cận thú vị, cho kết quả ước tính nhanh nhưng đáng tin cậy.
*(Planning poker combines expert opinion, analogy, and disaggregation into an enjoyable approach that results in quick but reliable estimates.)*

**Nguyên tắc:**
- Ba junior không có số phiếu đông hơn một senior có kinh nghiệm.
  *(Three juniors don't outvote one experienced senior.)*
- Giữ câu chuyện nhỏ (1, 3 và 5 điểm, đôi khi có epic lớn).
  *(Size your stories small — one, three, and five points with the occasional epic.)*
- Thảo luận phù hợp: Dùng đồng hồ cát 2 phút đặt giữa bàn để giới hạn thời gian thảo luận.
  *(The right discussion time: use a two-minute sand timer in the middle of the table.)*

---

## VI. Phương pháp Wideband Delphi (Wideband Delphi Method) \[3\]

### 6.1 Thiết lập

- Đặc tả vấn đề.
- Người điều hành (moderator), quản lý dự án và 2-4 người ước tính khác.
- Nhóm xem xét mục tiêu ước tính, thảo luận vấn đề và các câu hỏi ước tính.
- Thống nhất về đơn vị ước tính.
- Tất cả thành viên đủ kiến thức để đóng góp vào hoạt động ước tính.

### 6.2 Chuẩn bị cá nhân (Individual Preparation)

Mỗi người tham gia **độc lập** phát triển danh sách ban đầu các nhiệm vụ cần hoàn thành để đạt mục tiêu dự án, sau đó ước tính nỗ lực cho mỗi nhiệm vụ.
*(Each participant independently develops an initial list of tasks that will have to be completed to reach the stated project goal, then estimates the effort each task will consume.)*

### 6.3 Cuộc họp ước tính — Vòng 1

- Người điều hành thu thập ước tính cá nhân và tạo biểu đồ (**không** xác định ai tạo ra ước tính nào).
  *(The moderator collects the participants' individual estimates and creates a chart — without identifying who created each estimate.)*
- Mỗi người ước tính đọc danh sách nhiệm vụ ban đầu, nêu giả định và câu hỏi mà **không** tiết lộ ước tính của mình.
  *(Each estimator reads out his or her initial task list, identifying assumptions and raising questions, without revealing which estimate was theirs.)*
- Kết hợp các danh sách nhiệm vụ riêng lẻ dẫn đến danh sách đầy đủ hơn.

### 6.4 Cuộc họp ước tính — Vòng 2

- Tất cả người tham gia sửa đổi ước tính **đồng thời và im lặng** trong phòng họp.
  *(All participants modify their estimates concurrently and silently in the meeting room.)*
- Có thể thêm nhiệm vụ mới hoặc ghi chú thay đổi so với ước tính ban đầu.
- Người điều hành thu thập và vẽ biểu đồ các ước tính đã sửa đổi.

### 6.5 Tổng hợp nhiệm vụ và đánh giá

- Người điều hành hoặc quản lý dự án tổng hợp danh sách nhiệm vụ chính, gộp các giả định, hoạt động liên quan đến chất lượng và quy trình, nhiệm vụ quản lý và thời gian chờ.
  *(The moderator or project manager assembles the project tasks into a single master task list, merging individual lists of assumptions, quality- and process-related activities, overhead tasks and wait times.)*
- Loại bỏ nhiệm vụ trùng lặp và đạt được giải pháp hợp lý cho các ước tính khác nhau.
- Nhóm ước tính xem xét kết quả tổng hợp và đạt **thỏa thuận về kết quả cuối cùng**.
  *(The estimation team reviews the summarized results and reaches agreement on the final outcome.)*

---

## Tài liệu tham khảo (References)

1. Mike Cohn (2005). *Agile Estimating and Planning*. Pearson Education.
2. Jonathan Rasmusson (2010). *The Agile Samurai: How Agile Masters Deliver Great Software*. Pragmatic Bookshelf.
3. Karl E. Wiegers (2000). *Stop Promising Miracles*.
