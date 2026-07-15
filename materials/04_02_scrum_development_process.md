# Quy trình phát triển Scrum (Scrum Development Process)

**Giảng viên / Lecturer:** Ngô Huy Biên (Ngo Huy Bien) — nhbien@fit.hcmus.edu.vn
**Đơn vị / Department:** Bộ môn Kỹ thuật phần mềm, Khoa Công nghệ thông tin, Trường Đại học Khoa học Tự nhiên, ĐHQG-HCM
**Môn học / Course:** Quản lý Dự án Phần mềm (Software Project Management)

---

## 1. Mục tiêu bài học (Learning Objectives)

Sau bài học, người học có thể:

- Trình bày lý do tại sao sử dụng phương pháp phát triển Agile.
  *(Present why use Agile development methods.)*
- Trình bày các vai trò trong Scrum.
  *(Present Scrum roles.)*
- Trình bày các hoạt động Scrum.
  *(Present Scrum activities.)*
- Trình bày các sản phẩm công việc Scrum.
  *(Present Scrum work products.)*
- Trình bày các giai đoạn của Scrum.
  *(Present Scrum phases.)*
- Áp dụng phương pháp Scrum để phát triển một hệ thống phần mềm.
  *(Apply Scrum method to develop a software system.)*

## 2. Nội dung (Contents Overview)

| # | Chủ đề (VI) | Topic (EN) |
|---|---|---|
| I | Tại sao dùng Agile? | Why Agile? |
| II | Scrum là gì? | What is Scrum? |
| III | Các vai trò trong Scrum | Scrum Roles |
| IV | Cuộc họp khởi động & Product Backlog | Kick-Off Meeting & Product Backlog |
| V | Release Backlog & Sprint | Release Backlog & Sprint |
| VI | Các sản phẩm công việc Scrum | Scrum Work Products |
| VII | Kiểm soát dự án trong Scrum | Controls Management in Scrum |
| VIII | Khi nào nên dùng Scrum? | When to Use Scrum? |
| IX | So sánh các phương pháp luận | Methodology Comparison |

---

## I. Tại sao dùng Agile? (Why Agile?) \[1\]

### 1.1 Thời gian đưa ra thị trường (Time To Market)

Thời gian đưa sản phẩm ra thị trường là thời gian cho đến khi sản phẩm đủ ổn định để có thể vận chuyển trong số lượng sản xuất lớn.
*(Time to market is the time until your product is sufficiently debugged that it can be shipped in volume production.)*

Thời gian đưa ra thị trường xác định sự thành công của sản phẩm **và** tỷ suất hoàn vốn đầu tư (ROI).

### 1.2 Vấn đề với tài liệu truyền thống

Tài liệu hệ thống truyền thống:
- Ngay lập tức lỗi thời *(instantly out of date)*
- Thường gây nhầm lẫn *(often misleading)*
- Tốn kém để duy trì *(expensive to maintain)*

**Giải pháp:** Làm cho kiến thức hệ thống trở nên rõ ràng — chỉ tạo tài liệu khi nhu cầu là ngay lập tức và có ý nghĩa.
*(Solution: making system knowledge explicit — produce no document unless its need is immediate and significant.)*

### 1.3 Phát triển phần mềm linh hoạt (Agile Software Development)

Các phương pháp Agile áp dụng phát triển lặp và tiến hóa theo khung thời gian, lập kế hoạch thích ứng, thúc đẩy phân phối tiến hóa — nhằm phản ứng nhanh và linh hoạt với sự thay đổi.
*(Agile development methods apply time-boxed iterative and evolutionary development, adaptive planning, promote evolutionary delivery — rapid and flexible response to change.)*

Tham khảo: https://agilemanifesto.org/

**Hợp đồng thành công** trong Agile nên quy định cách đội phát triển và khách hàng cộng tác, thay vì chi tiết phạm vi và lịch trình cho chi phí cố định.

### 1.4 12 Nguyên tắc Agile (Agile Principles)

1. Giao hàng sớm và liên tục phần mềm có giá trị. *(Early and continuous delivery of valuable software.)*
2. Chào mừng thay đổi yêu cầu, kể cả muộn trong quá trình phát triển. *(Welcome changing requirements, even late in development.)*
3. Cung cấp phần mềm hoạt động thường xuyên, ưu tiên khoảng thời gian ngắn hơn. *(Deliver working software frequently with a preference to the shorter timescale.)*
4. Doanh nhân và nhà phát triển phải làm việc cùng nhau hàng ngày. *(Business people and developers must work together daily.)*
5. Tin tưởng cá nhân để hoàn thành công việc. *(Trust individuals to get the job done.)*
6. Cuộc trò chuyện trực tiếp là phương thức giao tiếp hiệu quả nhất. *(Face-to-face conversation is the most effective method of communication.)*
7. Phần mềm hoạt động là thước đo chính của tiến độ. *(Working software is the primary measure of progress.)*
8. Phát triển bền vững — các bên tài trợ, nhà phát triển và người dùng duy trì tốc độ ổn định. *(Sustainable development.)*
9. Liên tục chú ý đến kỹ thuật xuất sắc và thiết kế tốt tăng cường sự linh hoạt. *(Continuous attention to technical excellence and good design enhances agility.)*
10. Sự đơn giản là điều cần thiết. *(Simplicity is essential.)*
11. Những kiến trúc, yêu cầu và thiết kế tốt nhất xuất hiện từ các đội tự tổ chức. *(The best architectures, requirements, and designs emerge from self-organizing teams.)*
12. Định kỳ, đội phản ánh về cách trở nên hiệu quả hơn, sau đó điều chỉnh hành vi phù hợp. *(At regular intervals, the team reflects on how to become more effective, then tunes and adjusts its behavior accordingly.)*

---

## II. Scrum là gì? (What is Scrum?) \[2\]

> SCRUM là một phương pháp quản lý, nâng cao và bảo trì cho một hệ thống hoặc nguyên mẫu sản xuất hiện có.
> *(SCRUM is a management, enhancement and maintenance methodology for an existing system or production prototype.)*

- Phương pháp Thác nước và Xoắn ốc đặt ra bối cảnh và định nghĩa sản phẩm bàn giao ngay từ đầu dự án.
  *(Waterfall and Spiral methodologies set the context and deliverable definition at the start of a project.)*
- SCRUM và các phương pháp lặp ban đầu lập kế hoạch bối cảnh và định nghĩa sản phẩm bàn giao rộng rãi, sau đó phát triển sản phẩm bàn giao trong quá trình thực hiện dự án dựa trên môi trường.
  *(SCRUM and Iterative methodologies initially plan the context and broad deliverable definition, and then evolve the deliverable during the project based on the environment.)*

**Giá trị Scrum (Scrum Values) \[1\]:**
- **Cam kết** *(Commitment)*
- **Tập trung** *(Focus)*
- **Cởi mở** *(Openness)*
- **Tôn trọng** *(Respect)*
- **Lòng can đảm** *(Courage)*

---

## III. Các vai trò trong Scrum (Scrum Roles) \[2\]

### 3.1 Chủ sở hữu sản phẩm (Product Owner)

- Đại diện cho lợi ích của tất cả những người có cổ phần trong dự án và hệ thống kết quả.
  *(Representing the interests of everyone with a stake in the project and its resulting system.)*
- Đạt được nguồn tài trợ ban đầu và liên tục bằng cách tạo ra các yêu cầu tổng thể, mục tiêu ROI và kế hoạch phát hành.
  *(Achieving initial and ongoing funding for the project by creating initial requirements, ROI objectives, and release plans.)*
- Sử dụng product backlog để đảm bảo chức năng có giá trị nhất được sản xuất trước.
  *(Using the product backlog to ensure that the most valuable functionality is produced first and built upon.)*

### 3.2 Nhóm Scrum (Scrum Team)

**Nhóm phát triển (Development Team):**
- Phát triển chức năng *(Developing functionality)*
- Tự quản lý, tự tổ chức và đa chức năng *(Self-managing, self-organizing, and cross-functional)*

**Bậc thầy Scrum (Scrum Master):**
- Dạy Scrum cho mọi người tham gia dự án *(Teaching Scrum to everyone involved in the project)*
- Triển khai Scrum phù hợp với văn hóa tổ chức *(Implementing Scrum so that it fits within an organization's culture)*
- Đảm bảo mọi người đều tuân theo các quy tắc và thực hành Scrum *(Ensuring that everyone follows Scrum rules and practices)*

---

## IV. Cuộc họp khởi động & Product Backlog (Kick-Off Meeting & Product Backlog)

### 4.1 Cuộc họp khởi động (Kick-Off Meeting)

Cuộc họp khởi động được tổ chức để thống nhất các mục tiêu nền tảng và yêu cầu của dự án.
*(Kick-off meeting is held to agree on the foundation objectives and requirements of the project.)*

Các đầu ra chính:
- Tầm nhìn dự án *(Project vision)*
- Nghiên cứu khả thi *(Feasibility study)*
- Tuyên bố công việc *(Statement of work)*
- Product backlog ban đầu *(Initial product backlog)*

### 4.2 Product Backlog (Tồn đọng sản phẩm)

Product backlog là danh sách toàn diện các chức năng và tính năng cần được phát triển. Chỉ cần tìm ra những gì cần làm cho Sprint tiếp theo.

---

## V. Release Backlog & Sprint

### 5.1 Release Backlog (Tồn đọng phát hành)

- Lựa chọn bản phát hành phù hợp nhất để phát triển ngay lập tức.
  *(Selection of the release most appropriate for immediate development.)*
- Release backlog là các user story được đưa vào bản phát hành tiếp theo.
  *(Release backlog are the user stories that are included in the next release.)*

**Lập kế hoạch phát hành (Release Planning):**
- Định nghĩa nhóm dự án cho bản phát hành mới.
- Đánh giá rủi ro và kiểm soát rủi ro thích hợp.
- Xác nhận/lựa chọn lại công cụ phát triển và hạ tầng.
- Ước tính chi phí phát hành (phát triển, tài liệu, tiếp thị, đào tạo, triển khai).
- Xác minh phê duyệt quản lý và tài trợ.

### 5.2 Sprint (Chạy nước rút)

Với Scrum, các dự án tiến triển qua một loạt lần lặp gọi là Sprint. Mỗi Sprint thường kéo dài 2-4 tuần.
*(With Scrum, projects progress via a series of iterations called sprints. Each sprint is typically 2-4 weeks long.)*

Mỗi Sprint trở thành một dự án nhỏ với phạm vi xác định rõ, ngày bắt đầu rõ ràng và ngày kết thúc cố định.
*(Every sprint becomes a small project with a well-defined scope, a clear beginning, and a fixed end date.)*

**Sprint Backlog:** Danh sách công việc nhóm phải giải quyết trong Sprint tiếp theo.

**Lập kế hoạch Sprint (Sprint Planning):**
- Xác định sản phẩm bàn giao Sprint *(Sprint deliverables)*
- Xác định cách đạt được sản phẩm bàn giao Sprint
- Thỏa thuận giữa Product Owner và nhóm

**Cuộc họp trạng thái hàng ngày (Daily Status Meeting / Daily Scrum):**
1. Bạn đã làm gì kể từ cuộc họp Scrum lần trước? *(What did you do since last Scrum meeting?)*
2. Bạn có gặp trở ngại gì không? *(Do you have any obstacles?)*
3. Bạn sẽ làm gì trước cuộc gặp tiếp theo? *(What will you do before next meeting?)*

> Khả năng của nhóm để giải quyết vấn đề và xử lý chúng là trái tim của Scrum.
> *(The team's ability to tackle its problems and solve them is the heart of Scrum.)*

---

## VI. Các sản phẩm công việc Scrum (Scrum Work Products)

### 6.1 Định nghĩa của Xong (Definition of Done — DoD) \[3\]

**Ví dụ DoD 1:**
- Mã hóa theo tiêu chuẩn *(coded to standards)*
- Được xem xét bởi thành viên khác *(reviewed by other member)*
- Thực hiện với bài kiểm tra đơn vị *(implemented with unit tests)*
- Được thử nghiệm với 100% tự động hóa *(tested with 100% test automation)*
- Tích hợp và triển khai *(integrated and deployed)*
- Có tài liệu *(documented)*
- Được thử nghiệm bởi thành viên khác *(tested by other member)*
- Được PO chấp nhận *(accepted by PO)*

**Ví dụ DoD 2:**
- Release backlog được tạo *(Release backlog created — documentation task)*
- Kế hoạch phát hành được tạo *(Release plan created — documentation task)*
- User story được ghi lại *(User story documented — documentation task)*
- Code build không có lỗi *(Code builds without errors — technical task)*
- Code được kiểm tra đơn vị *(Code unit tested — technical task)*
- Kiểm tra chức năng đã đạt *(Functional test passed — technical task)*
- Kiểm tra phi chức năng (UI và hiệu suất) đã đạt *(Non-functional test passed — technical task)*
- Hướng dẫn sử dụng ngắn gọn được tạo *(Brief user guide created — documentation task)*
- Build đã được đẩy lên máy chủ demo *(Build pushed to demo server — technical task)*
- Release backlog được cập nhật *(Release backlog updated — documentation task)*
- Kế hoạch/lịch trình phát hành được cập nhật *(Release plan/schedule updated — documentation task)*

### 6.2 Burn-down Chart (Biểu đồ đốt cháy)

Burn-down chart cho thấy mỗi ngày còn bao nhiêu việc (tính bằng giờ hoặc ngày) cho đến khi nhóm hoàn thành cam kết.
*(Burn-down chart shows, each day, how much work remains until the team's commitment is completed.)*

### 6.3 Vận tốc (Velocity)

Vận tốc là theo dõi dài hạn về lượng công việc đã được thực hiện bởi một nhóm trong mỗi lần lặp.
*(Velocity is the long-term tracking of how much work has been done by a team per iteration.)*

### 6.4 Đánh giá Sprint (Sprint Review)

Sprint Review là cuộc họp sau khi Sprint kết thúc — đây chỉ là một buổi demo những gì đã được xây dựng; bất kỳ ai có mặt đều có thể hỏi câu hỏi và đưa ý kiến.
*(Sprint review is a meeting after the Sprint ends — it's just a demo of what's been built, and anyone present is free to ask questions and give input.)*

### 6.5 Hồi tưởng Sprint (Sprint Retrospective)

Sprint Retrospective là cuộc họp để nhóm thảo luận về những gì đang hoạt động và không hoạt động, và đồng ý về những thay đổi để thử.
*(Sprint retrospective is a meeting for the team to discuss what's working and what's not working, and agree on changes to try.)*

**Công cụ hỗ trợ Scrum:**
- Jira: https://www.atlassian.com/software/jira
- Trello: https://trello.com/
- Agilefant: http://www.agilefant.com/
- Slack: https://slack.com/

---

## VII. Kiểm soát dự án trong Scrum (Controls Management in Scrum) \[2\]

### 7.1 Các biện pháp kiểm soát trong SCRUM

| Biện pháp | Mô tả |
|---|---|
| **Tồn đọng (Backlog)** | Các yêu cầu chức năng sản phẩm chưa được giải quyết đầy đủ bởi bản phát hành hiện tại |
| **Phát hành/Nâng cao (Release/Enhancement)** | Các hạng mục tồn đọng tại một thời điểm đại diện cho một bản phát hành khả thi dựa trên yêu cầu, thời gian, chất lượng và cạnh tranh |
| **Gói (Packets)** | Các thành phần hoặc đối tượng sản phẩm phải thay đổi để triển khai hạng mục tồn đọng vào bản phát hành mới |
| **Rủi ro (Risks)** | Các rủi ro ảnh hưởng đến thành công dự án, liên tục được đánh giá và lên kế hoạch ứng phó |
| **Thay đổi (Changes)** | Những thay đổi phải xảy ra với gói để triển khai hạng mục tồn đọng |
| **Sự cố (Problems)** | Vấn đề kỹ thuật xảy ra và phải giải quyết để triển khai thay đổi |
| **Giải pháp (Solutions)** | Giải pháp cho các vấn đề và rủi ro, thường dẫn đến thay đổi |
| **Vấn đề (Issues)** | Vấn đề chung về dự án không được định nghĩa theo gói, thay đổi và sự cố |

### 7.2 Phân công quản lý kiểm soát

- **Ban quản lý** sử dụng các biện pháp kiểm soát này để quản lý tồn đọng.
- **Các nhóm** sử dụng các điều khiển này để quản lý thay đổi, sự cố.
- **Cả ban quản lý và các nhóm** cùng quản lý vấn đề, rủi ro và giải pháp.
- Các biện pháp kiểm soát này được xem xét, sửa đổi và đối chiếu tại mỗi cuộc họp Sprint Review.

---

## VIII. Khi nào nên dùng Scrum? (When To Use Scrum?)

### 8.1 Tại sao dùng Scrum? \[4\]

- Cách tiếp cận phát triển trước đây đơn giản là không hiệu quả. *(Previous approach to development simply wasn't working.)*
- Môi trường phức tạp nơi có nhiều điều chưa biết hơn là đã biết. *(A complex domain where more was unknown than known.)*
- Sản phẩm chưa từng được sản xuất trước đây. *(Products that had never been built before.)*
- Cần thăm dò và phản hồi nhanh chóng. *(Need for rapid exploration and feedback.)*
- Tránh thiết kế kiến trúc lớn phía trước. *(Avoid big up-front architecture design.)*
- Các nhóm cần có nhiều chức năng hơn. *(Teams to be more cross-functional.)*

### 8.2 Phù hợp và không phù hợp theo loại môi trường

| Loại môi trường | Đặc điểm | Phù hợp với Scrum? |
|---|---|---|
| **Phức tạp (Complex)** | Miền xuất hiện; cần khám phá và điều chỉnh; phát triển sản phẩm đổi mới | ✅ Đặc biệt phù hợp |
| **Phức tạp vừa (Complicated)** | Thực hành tốt, chuyên gia chi phối; bảo trì phần mềm | ⚠️ Có thể dùng nhưng không tối ưu |
| **Hỗn loạn (Chaotic)** | Khủng hoảng, thiệt hại lớn, cần phản ứng nhanh | ❌ Không phải giải pháp tốt nhất |
| **Đơn giản (Simple)** | Giải pháp đã biết; sản xuất lặp lại; triển khai COTS | ❌ Quy trình dây chuyền lắp ráp phù hợp hơn |
| **Rối loạn (Disorder)** | Không biết mình đang ở môi trường nào | ❌ Cần thoát khỏi miền này trước |
| **Công việc gián đoạn (Interrupt-Driven)** | Hỗ trợ và bảo trì theo hướng ngắt | ⚠️ Xem xét Kanban thay thế |

---

## IX. So sánh các phương pháp luận (Methodology Comparison) \[2\]

### 9.1 Vấn đề của phương pháp Thác nước

- Bản chất tuyến tính là vấn đề lớn nhất.
  *(Its linear nature has been its largest problem.)*
- Quy trình không xác định cách phản hồi đến kết quả không mong đợi từ bất kỳ giai đoạn trung gian nào.
  *(The process does not define how to respond to unexpected output from any of the intermediate process.)*

### 9.2 Vấn đề của phương pháp Lặp

- Cách tiếp cận lặp vẫn kỳ vọng rằng các quy trình phát triển nền tảng được xác định và tuyến tính.
  *(The Iterative approach still expects that the underlying development processes are defined and linear.)*

### 9.3 Truyền thống vs. Agile \[5, 6\]

- Agile cố định ngày tháng và tài nguyên, biến đổi phạm vi.
  *(Agile fixes the date and resources and varies the scope.)*
- **Hợp đồng giá cố định** đóng băng cả ba yếu tố cùng một lúc: chi phí, thời gian và phạm vi — điều này mâu thuẫn với triết lý Agile.

---

## Tài liệu tham khảo (References)

1. Craig Larman (2003). *Agile and Iterative Development: A Manager's Guide*.
2. Ken Schwaber (1995). *SCRUM Development Process*.
3. Jonathan Rasmusson (2010). *The Agile Samurai: How Agile Masters Deliver Great Software*.
4. Kenneth S. Rubin (2012). *Essential Scrum: A Practical Guide to the Most Popular Agile Process*.
5. Dean Leffingwell (2011). *Agile Software Requirements: Lean Requirements Practices for Teams, Programs, and the Enterprise*. Addison-Wesley Professional.
6. Sridhar Nerur và cộng sự. (2005). *Challenges of Migrating to Agile Methodologies*.

## Đọc thêm (Further Reading)

- Craig Larman và Bas Vodde (2010). *Practices for Scaling Lean & Agile Development*. Addison-Wesley Professional. (Large-scale Scrum.)
