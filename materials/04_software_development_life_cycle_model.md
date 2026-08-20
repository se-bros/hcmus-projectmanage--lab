# Mô hình vòng đời phát triển phần mềm (Software Development Life Cycle Model)

**Giảng viên / Lecturer:** Ngô Huy Biên (Ngo Huy Bien) — nhbien@fit.hcmus.edu.vn
**Đơn vị / Department:** Bộ môn Kỹ thuật phần mềm, Khoa Công nghệ thông tin, Trường Đại học Khoa học Tự nhiên, ĐHQG-HCM
**Môn học / Course:** Quản lý Dự án Phần mềm (Software Project Management)

---

## 1. Mục tiêu bài học (Learning Objectives)

Sau bài học, người học có thể:

- Xác định và định nghĩa một mô hình SDLC cho một dự án cụ thể.
  _(To define a Software Development Life Cycle Model (SDLCM) for a project.)_

## 2. Nội dung (Contents Overview)

| #    | Chủ đề (VI)                    | Topic (EN)                             |
| ---- | ------------------------------ | -------------------------------------- |
| I    | Yêu cầu phần mềm               | Software Requirements                  |
| II   | Thiết kế phần mềm              | Software Design                        |
| III  | Xây dựng phần mềm (triển khai) | Software Construction (Implementation) |
| IV   | Kiểm tra phần mềm              | Software Inspection                    |
| V    | Kiểm thử phần mềm              | Software Testing                       |
| VI   | Vận hành và bảo trì phần mềm   | Software Operation & Maintenance       |
| VII  | Định nghĩa mô hình SDLC        | SDLC Model Definition                  |
| VIII | Mô hình SDLC của NASA/SEL      | NASA/SEL SDLC Model                    |

---

## I. Yêu cầu phần mềm (Software Requirements) \[3\]

> Yêu cầu phần mềm là việc suy luận, phân tích, đặc tả và xác nhận các yêu cầu đối với phần mềm.
> _(Software requirements: the elicitation, analysis, specification, and validation of requirements for software.)_

Các bước trong quy trình yêu cầu phần mềm:

1. Gợi ý yêu cầu _(Requirements elicitation)_
2. Phân tích yêu cầu và đàm phán _(Requirements analysis and negotiation)_
3. Đặc tả yêu cầu _(Requirements specification)_
4. Mô hình hóa hệ thống _(System modeling)_
5. Xác thực yêu cầu _(Requirements validation)_
6. Quản lý yêu cầu _(Requirements management)_

**Vai trò và sản phẩm:** Nhà phân tích kinh doanh, Người dùng, Người quản lý dự án → Từ điển thuật ngữ, Quy tắc kinh doanh, Mô hình miền, Tầm nhìn dự án, Đặc tả yêu cầu chức năng, Đặc tả bổ sung, Product Backlog, User stories.

---

## II. Thiết kế phần mềm (Software Design)

- Quy trình giải quyết vấn đề và lập kế hoạch cho một giải pháp phần mềm.
  _(The process of problem-solving and planning for a software solution.)_
- Sau khi mục đích và thông số kỹ thuật của phần mềm được xác định, nhà phát triển lập kế hoạch cho một giải pháp.
  _(After the purpose and specifications of software are determined, software developers plan for a solution.)_
- Bao gồm các vấn đề triển khai thành phần và thuật toán cấp thấp cũng như quan điểm kiến trúc.
  _(It includes low-level component and algorithm implementation issues as well as the architectural view.)_

**Vai trò và sản phẩm:** Kiến trúc sư kỹ thuật, Nhà thiết kế, Nhà phát triển → Đặc điểm kỹ thuật thiết kế kiến trúc, Thông số thiết kế chi tiết, Giao diện GUI.

---

## III. Xây dựng phần mềm (Software Construction / Implementation)

Xây dựng phần mềm thông qua việc sử dụng các ngôn ngữ lập trình.
_(The construction of software through the use of programming languages.)_

**Vai trò và sản phẩm:** Nhà phát triển, Kiến trúc sư kỹ thuật → Tệp mã, Bài kiểm tra đơn vị, Mô-đun, Sản phẩm, Kế hoạch phát triển, Kế hoạch tích hợp.

---

## IV. Kiểm tra phần mềm (Software Inspection)

Kiểm tra mã nguồn để phát hiện lỗi và vấn đề vi phạm tiêu chuẩn code.

**Vai trò và sản phẩm:** Kiến trúc sư kỹ thuật, Nhà phát triển → Danh sách lỗi, Vấn đề tiêu chuẩn hoặc quy ước code.

---

## V. Kiểm thử phần mềm (Software Testing)

> Kiểm thử phần mềm là các điều tra thực nghiệm được tiến hành để cung cấp cho các bên liên quan thông tin về chất lượng của sản phẩm hoặc dịch vụ đang được thử nghiệm, liên quan đến bối cảnh mà nó được dự định hoạt động.
> _(The empirical investigations conducted to provide stakeholders with information about the quality of the product or service under test, with respect to the context in which it is intended to operate.)_

**Vai trò và sản phẩm:** QA/QC và Người kiểm tra → Kế hoạch kiểm tra, Dữ liệu thử nghiệm, Hướng dẫn sử dụng, Kết quả kiểm tra.

**Kiểm tra chấp nhận (Acceptance Testing):** Do Người ủng hộ, Nhóm phát triển, Khách hàng, Người dùng thực hiện → Kế hoạch kiểm tra chấp nhận, Kết quả kiểm tra.

---

## VI. Vận hành và bảo trì phần mềm (Software Operation & Maintenance)

- Hệ thống phần mềm thường gặp vấn đề và cần cải tiến trong thời gian dài sau khi hoàn thành lần đầu.
  _(Software systems often have problems and need enhancements for a long time after they are first completed.)_
- Bảo trì phần mềm là quá trình nâng cao và tối ưu hóa phần mềm đã triển khai, cũng như khắc phục các khiếm khuyết.
  _(Software maintenance is the process of enhancing and optimizing deployed software, as well as remedying defects.)_

**Vai trò:** Khách hàng, Người dùng, Người hỗ trợ và Nhóm phát triển.

---

## VII. Định nghĩa mô hình SDLC (SDLC Model Definition)

### 7.1 Vòng đời phát triển phần mềm (The Software Development Life Cycle) \[4\]

> Vòng đời phát triển phần mềm là tất cả các trạng thái mà qua đó phần mềm phát triển.
> _(Software development life cycle: all the states through which the software evolves.)_

### 7.2 Mô hình SDLC \[2\]

> Mô hình vòng đời phần mềm là đặc tính mô tả hoặc quy định của sự phát triển phần mềm.
> _(A software life cycle model is either a descriptive or prescriptive characterization of software evolution.)_

- **Mô hình quy định (Prescriptive):** quy định phần mềm nên được phát triển như thế nào — phổ biến và dễ trình bày hơn.
- **Mô hình mô tả (Descriptive):** mô tả cách phần mềm thực sự được phát triển trong các cài đặt cụ thể.

### 7.3 Các phần tử của SDLCM

Một mô hình SDLC bao gồm: **Giai đoạn** _(Phases)_, **Hoạt động** _(Activities)_, **Công việc** _(Work)_, **Sản phẩm** _(Products)_, **Vai trò** _(Roles)_, **Mẫu** _(Templates)_, **Tiêu chuẩn** _(Standards)_, **Thực hành** _(Practices)_.

### 7.4 Tại sao cần định nghĩa mô hình SDLC? \[2\]

- Mô tả hoặc quy định cách thức hệ thống phần mềm hình thành _(Comparative descriptive or prescriptive accounts for how software systems come to be)_.
- Tuân thủ quy định _(Regulatory compliance)_.
- Khuôn khổ để phân tích hoặc ước tính mô hình phân bổ tài nguyên _(Framework for analyzing resource allocation patterns)_.
- Tổ chức, lập kế hoạch, nhân sự, lập ngân sách, tiến độ và quản lý công việc dự án _(Organize, plan, staff, budget, schedule and manage software project work)_.
- Cơ sở để nghiên cứu thực nghiệm xác định yếu tố ảnh hưởng đến năng suất, chi phí và chất lượng _(Basis for empirical studies to determine what affects productivity, cost, and quality)_.
- Cơ sở để xác định công cụ và phương pháp kỹ thuật phần mềm phù hợp nhất _(Basis for determining appropriate software engineering tools and methodologies)_.
- Là phác thảo quy định về những sản phẩm cần sản xuất để phê duyệt và giao hàng _(Prescriptive outlines for what products to produce for approvals and delivery)_.
- Thiết lập khuôn khổ mà tất cả nhân sự phải tuân theo _(Establish a framework for building, implementing and enhancing systems)_.

### 7.5 Mẫu định nghĩa mô hình SDLC (SDLC Model Definition Template)

Một mô hình SDLC được định nghĩa bao gồm:

| Phần tử           | Mô tả                             |
| ----------------- | --------------------------------- |
| Vòng đời          | Các giai đoạn phân cấp/chồng chéo |
| Giai đoạn         | Tên và mục đích giai đoạn         |
| Tiêu chí đầu vào  | Điều kiện để bắt đầu giai đoạn    |
| Đầu vào           | Tài liệu/sản phẩm cần thiết       |
| Vai trò           | Ai thực hiện                      |
| Nhiệm vụ          | Các hoạt động cụ thể              |
| Luồng quy trình   | Cách các bước diễn ra             |
| Sản phẩm bàn giao | Kết quả đầu ra                    |
| Điểm kiểm tra     | Cột mốc đánh giá                  |
| Đầu ra            | Tài liệu/sản phẩm tạo ra          |
| Tiêu chí thoát    | Điều kiện để kết thúc giai đoạn   |

---

## VIII. Mô hình SDLC của NASA/SEL \[1\]

NASA/SEL đã phát triển một mô hình SDLC thực tiễn cho các dự án phần mềm lớn. Lý do học mô hình SDLC của NASA/SEL:

- Để hiểu rằng mô hình được xác định rõ ràng giúp đạt được kết quả tốt và nhất quán, năng suất và chất lượng.
  _(Well-defined model: achieving good and consistent results, productivity and quality.)_
- Mô hình không xác định dẫn đến kết quả không nhất quán, tạo gánh nặng cho thành viên với tài liệu, cuộc họp và yêu cầu báo cáo không cần thiết, dẫn đến ít năng suất và chất lượng hơn.
  _(Ill-defined model: producing inconsistent results, overburdening team members with unnecessary documents, meetings and report requests.)_

**Đo năng suất:**

- Năng suất = Quy mô / Công sức _(Productivity = Size / Effort)_
- Quy mô = LOC, Lớp, Phương thức, Tính năng, Lỗi đã sửa _(Size = LOC, Classes, Methods, Features, Bugs Fixed)_
- Công sức = Nhật ký thời gian, Số giờ được tính phí _(Effort = Time Log, Hours Billed)_

### 8.1 Câu hỏi quản lý cơ bản mà SDLCM phải trả lời

- Chúng ta nên làm bước nào tiếp theo?
- Sẽ mất bao lâu?
- Thực hiện bước này như thế nào?
- Nó sẽ tạo ra những hiện vật gì?
- Ai chịu trách nhiệm thực hiện bước này?

### 8.2 Đảm bảo không thất bại

> Đừng nhầm lẫn các quy trình với các mục tiêu — đây là một trong những tội lỗi lớn nhất của quản lý.
> _(Confusing processes with the goals is one of the great sins of management.)_

- Các vai trò được xác định rõ ràng giúp mọi người tổ chức xung quanh công việc, nhưng hình thành các vai trò không phải là mục tiêu.
  _(Well-defined roles might help people organize around the work, but the formation of roles is not the goal.)_
- Danh sách kiểm tra giúp thực hiện công việc đạt mục tiêu, nhưng danh sách kiểm tra cũng không phải là mục tiêu.
  _(A checklist might help do the work in a way that meets the goal, but the checklist is not the goal either.)_

---

## Tài liệu tham khảo (References)

1. NASA (1992). _Recommended Approach to Software Development_.
2. University of Southern California (1990). _Models of Software Evolution: Life Cycle and Process_.
3. Roger S. Pressman (2010). _Software Engineering: A Practitioner's Approach_.
4. Silvia T. Acuna và cộng sự. (1999). _A Process Model Applicable to Software Engineering and Knowledge Engineering_.
5. Scott Berkun (2008). _Making Things Happen: Mastering Project Management_.
