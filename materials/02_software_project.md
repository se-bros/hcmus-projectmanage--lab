# Dự án Phần mềm (Software Project)

**Giảng viên / Lecturer:** Ngô Huy Biên (Ngo Huy Bien) — nhbien@fit.hcmus.edu.vn
**Đơn vị / Department:** Bộ môn Kỹ thuật phần mềm, Khoa Công nghệ thông tin, Trường Đại học Khoa học Tự nhiên, ĐHQG-HCM
**Môn học / Course:** Nhập môn Công nghệ phần mềm — Software Project

---

## 1. Mục tiêu bài học (Learning Objectives)

Sau bài học, người học có thể:

- Giải thích được các khái niệm nền tảng để giao tiếp trong dự án (phần mềm, dự án, phạm vi).
  *(Explain foundational concepts for communicating within a project — software, project, scope.)*
- Giải thích được vì sao dự án phần mềm thường thất bại.
  *(Explain why software projects fail.)*
- Giải thích được các ràng buộc (constraints) của một dự án.
  *(Explain project constraints.)*
- Đề xuất và đánh giá được một ý tưởng dự án.
  *(Propose and evaluate a project idea.)*

## 2. Nội dung (Contents Overview)

| # | Chủ đề (VI) | Topic (EN) |
|---|---|---|
| I | Phần mềm | Software |
| II | Dự án | Project |
| III | Phạm vi dự án & phạm vi sản phẩm | Project scope & product scope |
| IV | Các loại dự án | Project types |
| V | Nguyên nhân dự án thất bại | Project failure reasons |
| VI | Ràng buộc của dự án | Project constraints |

---

## I. Phần mềm (Software)

Trước khi bàn về dự án, cần thống nhất khái niệm "phần mềm" và các loại phần mềm, vì đây là nền tảng để giao tiếp chung trong nhóm dự án.
*(Before discussing projects, we must agree on what "software" means and its types, as this is the communication foundation for a project team.)*

> Câu hỏi gợi mở: Tại sao phải quan tâm đến định nghĩa và các loại phần mềm?
> *(Guiding question: Why care about the software definition and software types?)*

---

## II. Dự án (Project)

### 2.1 Định nghĩa

> Dự án là một nỗ lực tạm thời được thực hiện nhằm tạo ra một sản phẩm, dịch vụ hoặc kết quả duy nhất.
> *(A project is a temporary endeavor undertaken to create a unique product, service, or result.)* \[1\]

Hai đặc điểm cốt lõi của dự án:

- **Tạm thời (Temporary):** có ngày bắt đầu và ngày kết thúc xác định.
  *(Has a definite start date and end date.)*
- **Kết quả duy nhất (Unique product, service, or result):** không lặp lại y hệt giữa các dự án.

### 2.2 Các thành phần cần quản lý của một dự án

| Thành phần (VI) | Component (EN) | Diễn giải |
|---|---|---|
| Ngân sách | Budget | Chi phí được cấp phát cho dự án |
| Cố gắng / Nỗ lực | Effort | Khối lượng công sức (nhân-giờ, nhân-tháng...) |
| Khoảng thời gian | Duration | Từ ngày bắt đầu (Start Date) đến ngày kết thúc (End Date) |
| Tài nguyên | Resource | Con người, công cụ, hạ tầng phục vụ dự án |
| Sản phẩm, sản phẩm bàn giao | Products, Deliverables | Kết quả cụ thể phải giao nộp |
| Yêu cầu, phạm vi | Requirements, Scope | Những gì dự án phải đáp ứng và giới hạn công việc |
| Lịch trình | Schedule | Kế hoạch thời gian thực hiện |
| Trị giá | Cost | Giá trị/chi phí thực tế phát sinh |

### 2.3 Phạm vi sản phẩm so với phạm vi dự án (Product Scope vs. Project Scope)

Trong bối cảnh dự án, thuật ngữ *phạm vi (scope)* có thể chỉ hai điều khác nhau:
*(In the project context, the term scope can refer to two different things:)*

- **Phạm vi sản phẩm (Product scope):** các tính năng và chức năng mô tả đặc điểm của sản phẩm, dịch vụ hoặc kết quả.
  *(The features and functions that characterize a product, service, or result.)*
- **Phạm vi dự án (Project scope):** công việc được thực hiện để tạo ra sản phẩm, dịch vụ hoặc kết quả với các tính năng và chức năng được chỉ định.
  *(The work performed to deliver a product, service, or result with the specified features and functions.)*

> Lưu ý: Thuật ngữ "phạm vi dự án" đôi khi được xem là đã bao gồm cả "phạm vi sản phẩm".
> *(Note: "Project scope" is sometimes viewed as including "product scope".)*

### 2.4 Cách quản lý dự án

- **Quản lý đặc biệt (Ad-hoc management):** xử lý theo tình huống, không quy trình chuẩn.
- **Quản lý có hệ thống (Systematic management):** theo quy trình, phương pháp luận rõ ràng.

### 2.5 Dự án đến từ đâu? (Where Do Projects Come From?) \[4\]

- Các yêu cầu đề xuất (RFP) do cơ quan nhà nước và một số tổ chức công bố.
  *(Requests for proposals (RFPs) published by government agencies and organizations.)*
- Dự án và sản phẩm từ nghiên cứu (Research projects and products).
- Kinh nghiệm từ tài liệu/văn học chuyên ngành (Literature in the specific field).
- Kinh nghiệm giải quyết vấn đề thực tế trong lĩnh vực — nguồn phổ biến nhất.
  *(Experience of practical problems in the field — the most common source.)*
- Ý tưởng cá nhân, chịu ảnh hưởng bởi nền tảng, văn hóa, giáo dục và trải nghiệm.
  *(Personal ideas, influenced by background, culture, education, and experience.)*

**Yếu tố thường thấy trong một RFP:** ngân sách; nhu cầu từ quản lý, nhân viên, bán hàng, tiếp thị, hỗ trợ, dịch vụ khách hàng; tự động hóa quy trình kinh doanh, sửa lỗi, yêu cầu cụ thể; quan hệ với cơ quan/tổ chức chính phủ; kinh nghiệm trong lĩnh vực.

### 2.6 Hoạt động (Operations) và Dự án (Projects) \[2\]

| Tiêu chí | Dự án (Project) | Hoạt động (Operations) |
|---|---|---|
| Thời gian | Tạm thời, có ngày bắt đầu/kết thúc xác định | Diễn ra liên tục, lặp lại |
| Quy trình | Quy trình gốc/mới (original processes) | Quy trình lặp lại giống nhau |
| Kết quả | Kết quả độc đáo, duy nhất | Kết quả tương tự nhau |

> Dự án có thể xuất phát từ chính nhu cầu cải tiến hoạt động (operations improvement).

### 2.7 Dự án, Chương trình, Danh mục đầu tư (Projects, Programs, Portfolio) \[2\]

- **Chương trình (Program):** nhóm các dự án liên quan, được quản lý bằng các kỹ thuật giống nhau một cách phối hợp.
- **Danh mục đầu tư (Portfolio):** tập hợp các chương trình và dự án nhằm đáp ứng một mục tiêu kinh doanh cụ thể.
- **Các bên liên quan (Stakeholders)** \[1\]: cá nhân hoặc tổ chức (khách hàng, nhà tài trợ, tổ chức thực hiện, công chúng...) tham gia tích cực vào dự án, hoặc có lợi ích bị ảnh hưởng (tích cực/tiêu cực) bởi việc thực hiện hay hoàn thành dự án.

---

## III. Các loại dự án phần mềm (Software Project Types) \[3\]

Theo khảo sát trên 100 dự án phần mềm tại một công ty Fortune 500 — một ví dụ về "hỗn hợp hiện đại" (a modern mix) các loại dự án:

| Loại dự án (VI) | Project Type (EN) |
|---|---|
| Cải tiến hệ thống kế thừa | Legacy enhancements |
| Phát triển mới | New development |
| Sửa đổi ERP | ERP modifications |
| Cải tạo hệ thống kế thừa | Legacy renovations |
| Sửa đổi phần mềm COTS | COTS modifications |
| Sửa đổi mã nguồn mở | Open-source modifications |
| Sửa chữa hệ thống kế thừa | Legacy repairs |
| Phục hồi sau tấn công mạng | Cyber-attack recovery |

### Dự án nghiên cứu (Research Project)

Động lực để thực hiện dự án nghiên cứu có thể đến từ:

- **Tổ chức:** năng suất, khả năng cạnh tranh kinh doanh và cơ hội.
- **Nhóm hoặc cá nhân:** cơ hội kinh doanh.
- Nguồn gốc: tài liệu chuyên ngành (literature), vấn đề thực tế (practical problems), sự sáng tạo (creativity).

### Dự án nguồn mở (Open Source Projects)

Ví dụ về hình thức tổ chức: 7 thành viên, 8 giờ/tuần mỗi thành viên.

---

## IV. Làm rõ các bên liên quan (Stakeholders Clarification)

### 4.1 Dự án thành công và thất bại (Project Success and Failure)

| Mức độ | Định nghĩa |
|---|---|
| **Thành công (Success)** | Hoàn thành đúng thời hạn, đúng ngân sách, đủ tính năng như đặc tả ban đầu, khách hàng hài lòng. |
| **Có thách thức (Challenged)** | Hoàn thành và vận hành được, nhưng vượt ngân sách, trễ hạn, và có ít tính năng hơn đặc tả ban đầu. |
| **Thất bại (Failure)** | Bị hủy trước khi hoàn thành, hoặc bàn giao rồi nhưng không bao giờ được sử dụng. |

### 4.2 Nguyên nhân thất bại (Causes of Project Failure)

Một cách phân loại: dự án thất bại thường rơi vào các tổ hợp **mục tiêu (Objectives)** và **phương pháp (Methods)** không rõ ràng — chỉ khi cả mục tiêu lẫn phương pháp đều **rõ ràng (Clear)** thì dự án mới có nền tảng thành công vững chắc; còn lại (mục tiêu rõ/phương pháp không rõ, mục tiêu không rõ/phương pháp rõ, hoặc cả hai không rõ) đều là các vùng rủi ro cao dẫn đến thất bại.

### 4.3 Vì sao dự án thất bại? (Why Do Projects Fail?) \[5\]

1. Mục tiêu dự án không thực tế hoặc không rõ ràng.
2. Giao tiếp kém giữa khách hàng, nhà phát triển và người dùng.
3. Ước tính không chính xác về nguồn lực cần thiết.
4. Báo cáo kém về tình trạng dự án.
5. Sử dụng công nghệ chưa trưởng thành (immature technology).
6. Không có khả năng xử lý sự phức tạp của dự án.
7. Thực tiễn phát triển cẩu thả (sloppy development practices).
8. Yêu cầu hệ thống được xác định sai (badly defined system requirements).
9. Quản lý dự án kém (poor project management), bao gồm rủi ro không được quản lý (unmanaged risks).
10. Thay đổi liên tục các yêu cầu (constant change of requirements).
11. Chính trị giữa các bên liên quan (stakeholder politics).
12. Áp lực thương mại (commercial pressures).

### 4.4 Điều cần đảm bảo \[1\]

- Dự án nằm trong chi phí cho phép (within cost).
- Dự án được bàn giao đúng thời hạn (on time).
- Dự án nằm trong phạm vi đã định (within scope).
- Dự án đáp ứng yêu cầu chất lượng của khách hàng.
- Khách hàng hài lòng.

---

## V. Quản lý các ràng buộc dự án (Managing Constraints) \[6\]

Mỗi dự án bị ràng buộc theo những cách khác nhau; người quản lý phải quyết định ràng buộc nào là quan trọng nhất với từng dự án cụ thể.

> **Tam giác phát triển (Development Triangle):** Tốt – Nhanh – Rẻ, chỉ có thể chọn tối đa hai trong ba (good, fast, cheap – pick any two).

Ba đỉnh tam giác thường gặp: **Thời gian (Time)**, **Chi phí (Cost)**, **Phạm vi/Chất lượng (Scope/Quality)** — tăng một yếu tố thường phải đánh đổi bằng yếu tố khác.

---

## VI. Động não và đánh giá ý tưởng dự án

### 6.1 Động não ý tưởng dự án (Brainstorming Project Ideas)

Nguồn ý tưởng gợi ý:

- Vấn đề thực tế (Practical problems).
- Phần mềm nguồn mở — ví dụ tổ chức: 7 thành viên, 8 giờ/tuần/thành viên.

**Sản phẩm minh họa cho vấn đề thực tế:**

- Các ứng dụng trên thiết bị di động, các trang web bạn truy cập nhiều nhất.
- Ứng dụng thịnh hành trên Google Play, App Store.
- Phần mềm nguồn mở.
- Trách nhiệm công việc hàng ngày của bạn.

> Câu hỏi gợi mở: Trở ngại hiện tại của bạn là gì? *(What are your current obstacles?)*

### 6.2 Đánh giá ý tưởng dự án (Evaluating Project Ideas)

- Quy mô tổ chức tham khảo: 7 thành viên, 8 giờ/tuần/thành viên.
- Tiêu chí cốt lõi: ý tưởng phải **giải quyết một vấn đề có thật trong thế giới thực** (solving a real world problem).

---

## VII. Lựa chọn ý tưởng dự án nhóm (Team Project Idea Selection)

### Mẫu ghi nhận ý tưởng dự án (Documenting Team Project Idea)

Mỗi nhóm cần trình bày các mục sau:

1. **Số nhóm:** X (1 dòng).
2. **Tên dự án:** ABC (1 dòng).
3. **Vấn đề (Problems)** — KHÔNG phải tính năng (NOT features), nêu rõ điểm khó khăn (pain points).
4. **Giải pháp (Solution):** trường hợp sử dụng kinh doanh cốt lõi (the core business use case) — kịch bản hoặc quy trình làm việc trong thế giới thực.
5. **Lý do giải quyết vấn đề (Reason to solve the problems).**
6. **Đối thủ cạnh tranh (Competitors):** tối thiểu 3.
7. **Điểm khác biệt của nhóm (Your differentiators).**

---

## Tài liệu tham khảo (References)

1. Project Management Institute (2017). *A Guide to the Project Management Body of Knowledge*, 6th Edition.
2. Kim Heldman (2018). *PMP Project Management Professional Study Guide*. Sybex.
3. Capers Jones (2018). *Software Methodologies: A Quantitative Guide*. Auerbach Publications.
4. William Trochim and James P. Donnelly (2007). *The Research Methods Knowledge Base*.
5. Robert N. Charette (2005). *Why Software Fails*. IEEE Spectrum.
6. Kathy Schwalbe (2017). *An Introduction to Project Management*, 6th Edition.