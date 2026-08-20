# Cấu trúc phân chia công việc (Work Breakdown Structure)

**Giảng viên / Lecturer:** Ngô Huy Biên (Ngo Huy Bien) — nhbien@fit.hcmus.edu.vn
**Đơn vị / Department:** Bộ môn Kỹ thuật phần mềm, Khoa Công nghệ thông tin, Trường Đại học Khoa học Tự nhiên, ĐHQG-HCM
**Môn học / Course:** Quản lý Dự án Phần mềm (Software Project Management)

---

## 1. Mục tiêu bài học (Learning Objectives)

Sau bài học, người học có thể:

- Tạo lập một cấu trúc phân chia công việc (WBS).
  _(Create a work breakdown structure.)_
- Tính toán ước tính nỗ lực từ WBS.
  _(Calculate an effort estimate from a WBS.)_

## 2. Nội dung (Contents Overview)

| #   | Chủ đề (VI)                  | Topic (EN)                   |
| --- | ---------------------------- | ---------------------------- |
| I   | Định nghĩa WBS               | WBS Definition               |
| II  | Cách tạo WBS (3 vòng)        | How to Create WBS (3 Rounds) |
| III | Các loại phân rã WBS         | Types of WBS Decomposition   |
| IV  | Tại sao cần WBS?             | Why WBS?                     |
| V   | Các khái niệm WBS quan trọng | Key WBS Concepts             |
| VI  | Công cụ cho WBS              | Tools for WBS                |

---

## I. Định nghĩa WBS (WBS Definition) \[1\]

> WBS là sự phân rã theo thứ bậc của tổng phạm vi công việc mà nhóm dự án sẽ thực hiện để đạt được các mục tiêu dự án và tạo ra các sản phẩm bàn giao cần thiết.
> _(The WBS is a hierarchical decomposition of the total scope of work to be carried out by the project team to accomplish the project objectives and create the required deliverables.)_

WBS trả lời câu hỏi: "Khi nào bạn sẽ hoàn thành dự án nếu chỉ có bạn làm việc trên dự án?"
_(WBS only answers the question "When will you complete your project if there is only you working on the project?")_

Từ WBS, ta xác định:

- **Công sức = Nhân viên × Thời gian** _(Effort = Staff × Time)_

---

## II. Cách tạo WBS (How to Create WBS)

### 2.1 Vòng 1 — Phân rã sơ bộ

- **Đầu vào:** Tài liệu tầm nhìn và phạm vi, PoC, các tài liệu và hệ thống khác.
  _(Input: Vision and scope document, PoC, other documentation and systems.)_
- **Quá trình:** Lặp lại việc xác định, đánh giá, thảo luận sản phẩm bàn giao, công việc và loại bỏ trùng lặp.
  _(Process: Repeat identifying, judging, discussing deliverables, work and removing duplicates.)_
- **Đầu ra:** Cấu trúc phân chia công việc (WBS).
  _(Output: Work breakdown structure (WBS).)_

### 2.2 Vòng 2 — Thêm ước tính nỗ lực

- **Đầu vào:** Tài liệu tầm nhìn và phạm vi, PoC, các tài liệu và hệ thống khác.
- **Đầu ra:** WBS + **Ước tính nỗ lực** cho từng nhiệm vụ trong WBS.
  _(WBS + Effort estimates for each of the tasks in the WBS.)_
- Ở giai đoạn này, yêu cầu phần mềm có thể chưa rõ ràng → cần xem lại nguyên mẫu (prototype).

### 2.3 Vòng 3 — Chi tiết sau khi có SRS

- **Đầu vào:** Tài liệu tầm nhìn và phạm vi, PoC, Đặc tả yêu cầu phần mềm (SRS), các tài liệu và hệ thống khác.
- **Đầu ra:** WBS + Ước tính nỗ lực cho từng nhiệm vụ trong WBS.
- Ở giai đoạn này, giải pháp có thể chưa rõ ràng → cần xem lại bằng chứng về khái niệm (Proof of Concept).

---

## III. Các loại phân rã WBS (Types of WBS Decomposition)

### 3.1 Phân rã theo sản phẩm (Product Decomposition)

```text
Sản phẩm (Product)
├── Tài liệu (Documents)
│   ├── Tóm tắt điều hành (Executive summary)
│   ├── Tầm nhìn dự án (Project vision)
│   └── …
├── Hệ thống (System)
│   ├── Mã nguồn (Source code)
│   ├── Dữ liệu (Data)
│   └── …
└── Đồ họa (Graphics)
    ├── Biểu tượng (Icons)
    ├── Giao diện người dùng (UIs)
    └── …
```

### 3.2 Phân rã theo hệ thống (System Decomposition)

```text
Cổng thông tin (Portal)
├── Xác thực (Authentication)
│   ├── Đăng nhập (Login)
│   └── Quên mật khẩu (Forgot password)
├── Ủy quyền (Authorization)
│   ├── Vai trò (Roles)
│   └── Người dùng (Users)
└── Chủ đề (Theme)
    ├── Chủ đề hệ thống (System theme)
    ├── Chủ đề mô-đun (Module theme)
    └── Chủ đề người dùng (User's theme)
```

### 3.3 Phân rã theo tính năng (Features Decomposition)

```text
Tính năng (Features)
├── Quản lý khách hàng (Manage Customers)
│   ├── CRUD
│   └── Quản lý phản hồi (Manage Feedback)
├── Quản lý nhân viên (Manage Employees)
│   ├── CRUD
│   └── Quản lý lương (Manage Salaries)
└── Báo cáo (Reports)
    ├── Tạo báo cáo (Generate reports)
    └── Lọc thông tin (Filter information)
```

### 3.4 Phân rã theo trường hợp sử dụng (Use Case Decomposition)

Mỗi Use Case phân rã thành các sản phẩm bàn giao:

- Lược đồ cơ sở dữ liệu _(Database schema)_
- Giao diện người dùng _(UIs)_
- Sơ đồ lớp, sơ đồ tuần tự, lưu đồ, biểu đồ trạng thái, mô tả thuật toán, mô tả giải pháp.
  _(Class diagram, sequence diagram, flow chart, state chart, algorithm description, solution description.)_
- Mã nguồn (bao gồm bài kiểm tra đơn vị) _(Source code including unit tests)_
- Trường hợp thử nghiệm, báo cáo thử nghiệm _(Test cases, test report)_
- Hướng dẫn sử dụng, hướng dẫn phát triển, hướng dẫn triển khai _(User guide, development guide, deployment guide)_
- Biên bản họp, kịch bản trò chuyện _(Meeting minutes, chat scripts)_

### 3.5 Phân rã theo pha (Phases Decomposition)

**Pha I:**

```text
Dự án (Project)
├── Lập kế hoạch (Planning): Tóm tắt điều hành, Tầm nhìn dự án
├── Yêu cầu (Requirements): Yêu cầu người dùng, Yêu cầu phần mềm…
├── Thiết kế (Design): Thiết kế kiến trúc, Thiết kế chi tiết…
└── Xây dựng (Construction): Mã hóa, Kiểm tra đơn vị, Tích hợp…
```

**Pha II:**

```text
Dự án (Project)
├── Kiểm tra (Testing): Kế hoạch kiểm tra, Báo cáo kiểm tra, Báo cáo điều tra
├── Tài liệu (Documentation): Hướng dẫn sử dụng, Hướng dẫn cài đặt, Hướng dẫn nhà phát triển
├── Triển khai (Deployment): Gói, Tài liệu đào tạo
└── Hỗ trợ (Support): Vé sự cố, Vé hỗ trợ, Gói đã cập nhật
```

### 3.6 Phân rã theo hoạt động chung (Common Activities Decomposition)

| Hoạt động                                    | Sản phẩm                                                         |
| -------------------------------------------- | ---------------------------------------------------------------- |
| Nhân sự _(Staffing)_                         | Mô tả công việc, Biên bản phỏng vấn, Hướng dẫn đánh giá ứng viên |
| Môi trường & Công cụ _(Environment & Tools)_ | Kế hoạch quản lý cấu hình                                        |
| Quản lý _(Management)_                       | Lịch trình, Báo cáo giám sát, Báo cáo trạng thái                 |
| Giao tiếp _(Communication)_                  | Biên bản họp, Email, Nhật ký cuộc gọi                            |

### 3.7 Phân rã theo kỹ thuật yêu cầu (Requirements Engineering Decomposition)

- Biên bản họp, kịch bản trò chuyện _(Meeting minutes, chat scripts)_
- Giao diện người dùng _(UIs)_
- Mô hình miền _(Domain model)_
- Mô hình dữ liệu _(Data model)_
- Đặc tả yêu cầu phần mềm: use cases, quy tắc kinh doanh, khả năng sử dụng, vận hành, môi trường, bảo mật, tài liệu, ngôn ngữ lập trình, công nghệ, ràng buộc.
  _(Software requirement specification: use cases, business rules, usability, operation, environment, security, documentation, programming languages, technologies, constraints.)_
- Biên bản xem xét _(Review minutes)_

### 3.8 Phân rã theo kỹ thuật giải pháp (Solution Engineering Decomposition)

- Ghi chú điều tra _(Investigation notes)_
- Đặc tả thiết kế: kiến trúc, thành phần hệ thống, công nghệ, thành phần bên thứ ba, mô hình cơ sở dữ liệu, thuật toán và mẫu.
  _(Design specification: architecture, system components, technologies, 3rd party components, database model, algorithms and patterns.)_
- Mã nguồn bài tập _(Exercise source code)_

### 3.9 Từ trên xuống và từ dưới lên (Top-Down vs. Bottom-Up) \[3\]

- **Từ trên xuống (Top-Down):** Cách hợp lý để mô tả những thứ đã được hiểu đầy đủ. Khi giai đoạn từ trên xuống bắt đầu, vấn đề đã được giải quyết và chỉ còn các chi tiết cần giải quyết.
  _(Top-down is a reasonable way of describing things already fully understood. When the top-down phase begins, the problem is already solved, and only details remain.)_
- **Từ dưới lên (Bottom-Up):** Sử dụng khi chi tiết được xác định trước, sau đó tổng hợp lên.

---

## IV. Tại sao cần WBS? (Why WBS?) \[4\]

- Giao tiếp tốt hơn với nhà tài trợ dự án, các bên liên quan và thành viên nhóm thông qua tầm nhìn có cấu trúc về những gì cần bàn giao.
  _(Better communication to project sponsors, stakeholders, and team members by providing a structured vision of what has to be delivered.)_
- Tăng sự tự tin rằng 100% công việc (phạm vi) được xác định và bao gồm.
  _(Increased confidence that 100% of the work (scope) is identified and included.)_
- Ước tính chính xác hơn về nhiệm vụ, rủi ro, thời gian và chi phí.
  _(More accurate estimation of tasks, risks, timelines, and costs.)_
- Nền tảng cho quá trình kiểm soát trong dự án.
  _(A foundation for the control processes within the project.)_

**Cạm bẫy (Pitfalls):** Phân rã quá mức dẫn đến:

- Nỗ lực quản lý phi sản xuất _(nonproductive management effort)_
- Sử dụng tài nguyên không hiệu quả _(inefficient use of resources)_
- Giảm hiệu quả thực hiện công việc _(decreased efficiency in performing the work)_
- Khó tổng hợp dữ liệu ở các cấp độ khác nhau của WBS _(difficulty aggregating data over different levels)_

---

## V. Các khái niệm WBS quan trọng (Key WBS Concepts)

### 5.1 Sản phẩm bàn giao (Deliverable) \[4\]

> Bất kỳ sản phẩm, kết quả hoặc khả năng độc đáo và có thể kiểm chứng nào phải được sản xuất để hoàn thành một quá trình, giai đoạn hoặc dự án.
> _(Any unique and verifiable product, result, or capability to perform a service that must be produced to complete a process, phase, or project.)_

Thường được dùng trong nghĩa hẹp hơn để chỉ **sản phẩm bàn giao bên ngoài** — sản phẩm được phê duyệt bởi nhà tài trợ dự án hoặc khách hàng.

### 5.2 Phần tử WBS (WBS Element)

Bất kỳ thành phần WBS đơn lẻ và các thuộc tính WBS liên quan được chứa trong một cấu trúc phân chia công việc riêng lẻ.
_(Any single work breakdown structure (WBS) component and its associated WBS attributes contained within an individual work breakdown structure.)_

### 5.3 Gói công việc (Work Package)

> Sản phẩm bàn giao hoặc thành phần công việc dự án ở mức thấp nhất của mỗi nhánh trong cấu trúc phân chia công việc.
> _(A deliverable or project work component at the lowest level of each branch of the work breakdown structure.)_

Gói công việc bao gồm các hoạt động theo lịch trình và các cột mốc cần thiết để hoàn thành sản phẩm bàn giao của gói công việc.

### 5.4 Tài khoản kiểm soát (Control Account)

> Điểm kiểm soát quản lý tại đó phạm vi, ngân sách (kế hoạch nguồn lực), chi phí thực tế và lịch trình được tích hợp và so sánh với giá trị đạt được để đo lường hiệu suất.
> _(A management control point where scope, budget (resource plans), actual cost, and schedule are integrated and compared to earned value for performance measurement.)_

- Mỗi tài khoản kiểm soát có thể bao gồm một hoặc nhiều gói công việc.
- Mỗi gói công việc chỉ được liên kết với một tài khoản kiểm soát.

### 5.5 Quy tắc 100% (The 100% Rule) \[4\]

> WBS bao gồm 100% công việc được xác định bởi phạm vi dự án và nắm bắt TẤT CẢ các sản phẩm bàn giao (nội bộ, bên ngoài và tạm thời) về mặt công việc phải hoàn thành, bao gồm cả quản lý dự án.
> _(The WBS includes 100% of the work defined by the project scope and captures ALL deliverables — internal, external, and interim — in terms of work to be completed, including project management.)_

Quy tắc áp dụng ở tất cả các cấp: tổng công việc ở cấp "con" phải bằng 100% công việc của "cha". WBS không được bao gồm công việc nằm ngoài phạm vi thực tế (không thể > 100%).

### 5.6 Từ điển WBS (WBS Dictionary)

Từ điển WBS định nghĩa, chi tiết hóa và làm rõ các phần tử khác nhau của WBS để đảm bảo mỗi thành phần được trình bày chính xác và có thể truyền đạt cho bất kỳ ai tham khảo WBS.
_(The WBS dictionary defines, details, and clarifies the various elements of the WBS to ensure that each component is accurately articulated and can be communicated to anyone referencing the WBS.)_

Từ điển WBS chứa thông tin về mỗi phần tử WBS, bao gồm mô tả chi tiết về công việc, sản phẩm bàn giao, hoạt động và cột mốc gắn liền với từng phần tử.

---

## VI. Công cụ cho WBS (Tools for WBS)

- Microsoft Project: https://products.office.com/en-au/Project/project-for-office-365
- GanttProject: https://www.ganttproject.biz/download/free
- GanttPRO: https://ganttpro.com/
- Smartsheet: https://www.smartsheet.com/

---

## Tài liệu tham khảo (References)

1. Project Management Institute (2017). _A Guide to the Project Management Body of Knowledge_. Sixth Edition.
2. Roger S. Pressman và Bruce R. Maxim (2015). _Software Engineering: A Practitioner's Approach_. 8th Edition. McGraw-Hill.
3. Bertrand Meyer (1997). _Object Oriented Software Construction_.
4. Project Management Institute (2006). _Practice Standard for Work Breakdown Structures_.
5. Eric S. Norman, Shelly A. Brotherton và Robert T. Fried (2008). _Work Breakdown Structures: The Foundation for Project Management Excellence_. John Wiley & Sons.
