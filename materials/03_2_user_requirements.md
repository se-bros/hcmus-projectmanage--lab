# Yêu cầu của người dùng (User Requirements)

**Giảng viên / Lecturer:** Ngô Huy Biên (Ngo Huy Bien) — nhbien@fit.hcmus.edu.vn
**Đơn vị / Department:** Bộ môn Kỹ thuật phần mềm, Khoa Công nghệ thông tin, Trường Đại học Khoa học Tự nhiên, ĐHQG-HCM
**Môn học / Course:** Quản lý Dự án Phần mềm (Software Project Management)

---

## 1. Mục tiêu bài học (Learning Objectives)

Sau bài học, người học có thể:

- Khám phá và thu thập các yêu cầu của người dùng.
  *(Discover user requirements.)*
- Tạo lập tài liệu tầm nhìn và phạm vi dự án (project vision and scope document).
  *(Create a project vision and scope document.)*

## 2. Nội dung (Contents Overview)

| # | Chủ đề (VI) | Topic (EN) |
|---|---|---|
| I | Khám phá yêu cầu của người dùng | Discovering User Requirements |
| II | Thuật ngữ | Glossary |
| III | Quy tắc kinh doanh | Business Rules |
| IV | Đặc trưng (Tính năng) | Features |
| V | Mô hình tính năng | Feature Model |
| VI | Cây đặc trưng | Feature Tree |
| VII | Tầm nhìn và phạm vi dự án | Project Vision and Scope |
| VIII | Tuyên bố phạm vi dự án | Project Scope Statement |

---

## I. Khám phá yêu cầu của người dùng (Discovering User Requirements)

- Người dùng là ai?
  *(Who are the users?)*
- Vấn đề, nhu cầu hoặc mục tiêu của họ là gì?
  *(What are their problems, needs or goals?)*
- Không xem phần mềm như "hộp đen" — cần hiểu rõ từng yêu cầu của người dùng.
  *(No black box software — refer to Business Use Cases and Domain Models for details.)*

---

## II. Thuật ngữ (Glossary) \[1\]

> Bảng chú giải thuật ngữ (Glossary) xác định các thuật ngữ đáng chú ý và ghi lại các yêu cầu liên quan đến dữ liệu, chẳng hạn như quy tắc xác thực, các giá trị được chấp nhận, v.v.
> *(Glossary defines noteworthy terms, records requirements related to data, such as validation rules, acceptable values, and so forth.)*

Cấu trúc của một mục trong Glossary:

| Trường | Mô tả |
|---|---|
| Thuật ngữ *(Term)* | Tên của thuật ngữ |
| Định nghĩa và thông tin *(Definition and Information)* | Giải thích chi tiết |
| Định dạng *(Format)* | Cấu trúc dữ liệu, kiểu dữ liệu |
| Xác thực *(Validation)* | Quy tắc kiểm tra tính hợp lệ |
| Quy tắc *(Rules)* | Quy tắc kinh doanh liên quan |
| Bí danh *(Aliases)* | Tên gọi khác |

**Ví dụ minh họa — Hệ thống bán hàng:**

| Thuật ngữ | Định nghĩa |
|---|---|
| Payment authorization | Xác thực bởi dịch vụ ủy quyền thanh toán bên ngoài rằng họ sẽ thực hiện hoặc đảm bảo thanh toán cho người bán. |
| Payment authorization request | Tập hợp các phần tử được gửi điện tử tới dịch vụ ủy quyền (thường là mảng char), bao gồm: ID cửa hàng, số tài khoản khách hàng, số tiền và dấu thời gian. |
| UPC (Universal Product Code) | Mã số nhận dạng sản phẩm, ký hiệu bằng mã vạch. Mã 12 chữ số gồm nhiều phần phụ; chữ số thứ 12 là chữ số kiểm tra. Chi tiết tại www.gs1us.org. |

---

## III. Quy tắc kinh doanh (Business Rules)

> Các quy tắc kinh doanh quy định cách thức hoạt động của một miền hoặc doanh nghiệp.
> *(Business rules dictate how a domain or business may operate.)*

Cấu trúc mô tả một quy tắc kinh doanh:

| Trường | Mô tả |
|---|---|
| ID | Mã định danh quy tắc |
| Luật lệ *(Rule)* | Nội dung quy tắc |
| Khả năng thay đổi *(Changeability)* | Mức độ ổn định của quy tắc |
| Nguồn *(Source)* | Xuất xứ của quy tắc |

**Ví dụ — RULE1: Chữ ký bắt buộc cho thanh toán tín dụng:**
- Yêu cầu chữ ký của người mua khi thanh toán bằng thẻ tín dụng.
- Trong vòng 2 năm, hầu hết khách hàng muốn chụp chữ ký trên thiết bị kỹ thuật số; trong vòng 5 năm, dự kiến có nhu cầu hỗ trợ mã chữ ký kỹ thuật số mới theo luật Hoa Kỳ.
- Nguồn: Chính sách của hầu hết các công ty ủy quyền tín dụng.

**Ví dụ — RULE2: Quy tắc thuế:**
- Giao dịch bán hàng cần tính thêm thuế theo quy định pháp luật hiện hành.
- Khả năng thay đổi cao — luật thuế thay đổi hàng năm ở tất cả các cấp chính quyền.

---

## IV. Đặc trưng / Tính năng (Features) \[2\]

> Một tính năng là một đặc điểm của hệ thống có thể nhìn thấy được từ phía người dùng cuối.
> *(A feature is an end-user visible characteristic of a system.)*

### 4.1 Tính năng phụ (Sub-features)

Một tính năng có thể được phân tách thành nhiều tính năng phụ. Mối quan hệ giữa tính năng cha và tính năng con được phân loại thành:

| Quan hệ | Mô tả |
|---|---|
| **Và (And)** | Tất cả các tính năng phụ phải được chọn |
| **Thay thế (Alternative)** | Chỉ có thể chọn một tính năng phụ |
| **Hoặc (Or)** | Một hoặc nhiều tính năng phụ có thể được chọn |
| **Bắt buộc (Mandatory)** | Tính năng là bắt buộc |
| **Tùy chọn (Optional)** | Tính năng là không bắt buộc |

### 4.2 Cách xác định tính năng đúng (How to Identify a Correct Feature?)

1. **Phát hiện vấn đề** *(Spot the problem)*: Nói chuyện với một khách hàng, sau đó tìm thêm hai khách hàng trong cùng ngành.
2. **Hiểu vấn đề** *(Understand it)*: Chỉ cần lắng nghe và hiểu vấn đề của họ — không vội đề xuất giải pháp.
3. **Tạo nguyên mẫu** *(Prototype it)*: Hướng dẫn họ cách bạn tưởng tượng tính năng hoạt động; kiểm tra xem họ có bối rối hay hào hứng không.
4. **Kiểm tra thực tế** *(Inspect them)*: Xây dựng nguyên mẫu hoạt động và quan sát họ sử dụng nó.

### 4.3 Cách chỉ định một tính năng (How to Specify a Feature?)

Mỗi tính năng nên được chỉ định theo: **Người dùng (User)** — **Mục tiêu kinh doanh (Business Goal)** — **Chỉ số đo lường (Metric)** — **Hành động (Action)**.

**Ví dụ:**

| Người dùng | Mục tiêu kinh doanh | Chỉ số | Hành động |
|---|---|---|---|
| Kathy (Hỗ trợ) | Giảm các cuộc gọi tốn kém tới khách hàng | Số lượng cuộc gọi được chuyển hướng | Tạo các bài viết tri thức dựa trên thuật ngữ tìm kiếm phổ biến |
| Michael (Nhân sự) | Cải thiện sự hài lòng của nhân viên | Số ứng viên cho mỗi vị trí tuyển dụng; tỷ lệ giữ lại nhân viên | Tạo công cụ tuyển dụng tích hợp |

---

## V. Mô hình tính năng (Feature Model)

> Mô hình tính năng là tập hợp các tính năng được sắp xếp theo thứ bậc.
> *(A feature model is a hierarchically arranged set of features.)*

- Sơ đồ đặc điểm (feature diagram) là biểu diễn đồ họa của một mô hình tính năng.
  *(A feature diagram is a graphical representation of a feature model.)*

---

## VI. Cây đặc trưng (Feature Tree)

- Cây đặc trưng cấu trúc theo thứ bậc tập hợp các tính năng của một hệ thống.
  *(A feature tree hierarchically structures the set of features of a system.)*
- Đơn giản hơn mô hình tính năng: chỉ sử dụng mối quan hệ **VÀ (AND)**.
  *(Simpler than feature model: only AND relationship.)*

---

## VII. Tầm nhìn và phạm vi dự án (Project Vision and Scope) \[4\]

> Tầm nhìn và phạm vi dự án là hình ảnh của sản phẩm bàn giao như là giải pháp cho nhu cầu hoặc vấn đề đã nêu.
> *(A project vision and scope is the picturing of the project's deliverable as the solution to the stated need or problem.)*

Tài liệu Tầm nhìn và Phạm vi (Vision and Scope Document) bao gồm:

- Bối cảnh, ngữ cảnh, tổng quan *(The background, context, overview)*
- Các trường hợp sử dụng kinh doanh hiện tại *(The current business use cases)*
- Mô hình miền hiện tại *(The current domain model)*
- Các vấn đề hiện tại của người dùng và mục tiêu tương ứng *(The current users' problems and their corresponding objectives)*
- Các thành phần và tính năng sẽ được phát triển để đạt mục tiêu người dùng *(The components and features that will be developed to obtain the users' objectives)*
- Các thành phần và tính năng sẽ bị loại trừ *(The components and features that will be excluded)*
- Các trường hợp sử dụng kinh doanh trong tương lai *(The future business use cases)*
- Mô hình miền tương lai *(The future domain model)*
- Những giả định, những rủi ro *(The assumptions, the risks)*
- Kết luận *(The conclusion)*

---

## VIII. Tuyên bố phạm vi dự án (Project Scope Statement) \[5\]

> Tuyên bố phạm vi dự án là mô tả phạm vi dự án, những kết quả chính, những giả định và những hạn chế.
> *(Project scope statement: The description of the project scope, major deliverables, assumptions, and constraints.)*

- Tuyên bố phạm vi dự án cho biết công việc nào đang được làm — và công việc nào không được làm — trong dự án.
  *(The project scope statement tells what work you are — and are not — going to do in the project.)*

Nội dung điển hình của tuyên bố phạm vi:

| Thành phần | Mô tả |
|---|---|
| Mô tả phạm vi sản phẩm | *(Product scope description)* |
| Loại trừ dự án | *(Project exclusions)* |
| Sản phẩm bàn giao của dự án | *(Project deliverables)* |
| Tiêu chí chấp nhận dự án | *(Project acceptance criteria)* |
| Hạn chế của dự án | *(Project constraints)* |
| Giả định dự án | *(Project assumptions)* |

---

## Tài liệu tham khảo (References)

1. Craig Larman (2004). *Applying UML and Patterns*, 3rd Edition. Prentice Hall.
2. Don Batory (2005). *Feature Models, Grammars, and Propositional Formulas*.
3. Karl Wiegers và Joy Beatty (2013). *Software Requirements*. Microsoft Press.
4. Jennifer Greene và Andrew Stellman (2005). *Applied Software Project Management*. O'Reilly Media.
5. Andrew Stellman và Jennifer Greene (2014). *Head First PMP*, 3rd Edition. O'Reilly Media.

## Đọc thêm (Further Reading)

- David Lorge Parnas và Jan Madey (1995). *Functional Documents for Computer Systems*. (Mô hình NAT, REQ, IN, OUT và SOF.)
- Carl A. Gunter và cộng sự. (1998). *A Reference Model for Requirements and Specifications*. (Mô hình tham chiếu WRSPM.)
