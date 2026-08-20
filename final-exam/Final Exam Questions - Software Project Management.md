# QUẢN LÝ DỰ ÁN PHẦN MỀM

## Câu hỏi vấn đáp cuối kỳ

**GV. TS. Ngô Huy Biên. 2026.**

---

## Mục lục

1. [1. Đề xuất dự án (Project Proposal)](#1-đề-xuất-dự-án-project-proposal)
2. [2. Viễn cảnh và phạm vi dự án (Project Vision and Scope)](#2-viễn-cảnh-và-phạm-vi-dự-án-project-vision-and-scope)
3. [3. Ủy nhiệm dự án (Project Charter)](#3-ủy-nhiệm-dự-án-project-charter)
4. [4. Yêu cầu phần mềm (Software Requirements / Product Backlog)](#4-yêu-cầu-phần-mềm-software-requirements--product-backlog)
5. [5. Kiến trúc phần mềm (Software Architecture)](#5-kiến-trúc-phần-mềm-software-architecture)
6. [6. Chứng minh ý tưởng (Proof of Concept)](#6-chứng-minh-ý-tưởng-proof-of-concept)
7. [7. Bản mẫu (Prototype)](#7-bản-mẫu-prototype)
8. [8. Báo cáo tính khả thi (Feasibility Study Report)](#8-báo-cáo-tính-khả-thi-feasibility-study-report)
9. [9. Định nghĩa quy trình phát triển phần mềm (Software Process Definition)](#9-định-nghĩa-quy-trình-phát-triển-phần-mềm-software-process-definition)
10. [10. Ước lượng dự án (Project Estimate)](#10-ước-lượng-dự-án-project-estimate)
11. [11. Kế hoạch dự án (Project Plan)](#11-kế-hoạch-dự-án-project-plan)
12. [12. Phát biểu công việc (Statement of Work)](#12-phát-biểu-công-việc-statement-of-work)
13. [13. Mô hình tích hợp liên tục (Continuous Integration)](#13-mô-hình-tích-hợp-liên-tục-continuous-integration)
14. [14. Mô hình chuyển giao liên tục (Continuous Delivery)](#14-mô-hình-chuyển-giao-liên-tục-continuous-delivery)
15. [15. Mô hình DevOps](#15-mô-hình-devops)
16. [16. Quản lý con người và phát triển nhóm](#16-quản-lý-con-người-và-phát-triển-nhóm)
17. [17. Phân công, theo dõi, đánh giá, kiểm soát công việc và báo cáo tình trạng dự án](#17-phân-công-theo-dõi-đánh-giá-kiểm-soát-công-việc-và-báo-cáo-tình-trạng-dự-án)
18. [18. Kế hoạch quản lý rủi ro (Software Risk Management Plan)](#18-kế-hoạch-quản-lý-rủi-ro-software-risk-management-plan)
19. [19. Kế hoạch quản lý chất lượng (Software Quality Management Plan)](#19-kế-hoạch-quản-lý-chất-lượng-software-quality-management-plan)
20. [20. Kế hoạch kiểm thử (Test Plan)](#20-kế-hoạch-kiểm-thử-test-plan)
21. [21. Báo cáo bài học kinh nghiệm (Lessons Learned Register)](#21-báo-cáo-bài-học-kinh-nghiệm-lessons-learned-register)
22. [Chuẩn bị](#chuẩn-bị)
23. [Phiếu câu hỏi mẫu](#phiếu-câu-hỏi-mẫu)
24. [Quy trình vấn đáp](#quy-trình-vấn-đáp)
25. [Đánh giá](#đánh-giá)

---

## CÂU HỎI VẤN ĐÁP MÔN QUẢN LÝ DỰ ÁN PHẦN MỀM

Tất cả các câu trả lời cần trình bày bằng giấy bút trên giấy A4, không sử dụng bất kỳ tài liệu nào, kèm theo bản in các tài liệu và giao diện để hỗ trợ việc giải thích chi tiết.

---

### 1. Đề xuất dự án (Project Proposal)

Trình bày quá trình hình thành và phương pháp đánh giá tài liệu Đề xuất dự án (Project Proposal) của nhóm. _(Sinh viên nộp kèm bản in tài liệu Đề xuất dự án của nhóm.)_

**Các câu hỏi thường gặp:**

- Các câu hỏi chính cần trả lời trong tài liệu Đề xuất dự án là gì?
- Các đầu vào cần thiết và các bước nhóm đã thực hiện để tạo tài liệu Đề xuất dự án là gì?
- Dựa vào những dữ liệu nào mà bản đề xuất được hình thành?
- Các sản phẩm cạnh tranh trực tiếp với đề xuất là gì?
- Tài liệu Đề xuất dự án của nhóm đã được đánh giá thế nào?
- Tại sao cần tạo tài liệu Đề xuất dự án?
- Tài liệu Đề xuất dự án của nhóm đã được sử dụng và cập nhật trong quá trình thực hiện dự án như thế nào?
- Dự án phần mềm là gì?
- Phân biệt dự án (project) với hoạt động (operation), với chương trình (program), và với danh sách đầu tư (portfolio).
- Dự án phần mềm đến từ đâu?
- Phạm vi dự án là gì?
- Các vai trò nào thường tham gia vào một dự án phần mềm?
- Phân biệt các loại kết quả của một dự án.
- Phân tích các nguyên nhân chính khiến một dự án phần mềm thất bại.
- Các ràng buộc của một dự án có ý nghĩa gì?

#### ĐÁP ÁN LÝ THUYẾT

**▸ Dự án phần mềm là gì? (WHAT)**
Dự án là một nỗ lực **tạm thời** được thực hiện nhằm tạo ra một sản phẩm, dịch vụ hoặc kết quả **duy nhất**. Hai đặc điểm cốt lõi: (1) Tạm thời — có ngày bắt đầu và kết thúc xác định; (2) Kết quả duy nhất — không lặp lại y hệt giữa các dự án.
_Nguồn: [02_software_project.md](../materials/02_software_project.md) — dòng 49-57_

**▸ Phân biệt Dự án / Hoạt động / Chương trình / Danh mục đầu tư (WHAT)**

| Tiêu chí  | Dự án (Project)                    | Hoạt động (Operations) | Chương trình (Program) | Danh mục đầu tư (Portfolio) |
| --------- | ---------------------------------- | ---------------------- | ---------------------- | --------------------------- |
| Thời gian | Tạm thời, có ngày bắt đầu/kết thúc | Liên tục, lặp lại      | Nhóm dự án liên quan   | Tập hợp chương trình/dự án  |
| Kết quả   | Duy nhất                           | Tương tự nhau          | Phối hợp quản lý       | Đáp ứng mục tiêu kinh doanh |

_Nguồn: [02_software_project.md](../materials/02_software_project.md) — dòng 102-116_

**▸ Dự án phần mềm đến từ đâu? (WHAT)**
Từ: RFP của cơ quan/tổ chức; nghiên cứu; tài liệu chuyên ngành; kinh nghiệm giải quyết vấn đề thực tế (nguồn phổ biến nhất); ý tưởng cá nhân.
_Nguồn: [02_software_project.md](../materials/02_software_project.md) — dòng 89-99_

**▸ Phạm vi dự án là gì? (WHAT)**

- **Phạm vi sản phẩm (Product scope):** các tính năng và chức năng mô tả đặc điểm sản phẩm.
- **Phạm vi dự án (Project scope):** công việc được thực hiện để tạo ra sản phẩm với các tính năng đã chỉ định.
  _Nguồn: [02_software_project.md](../materials/02_software_project.md) — dòng 71-82_

**▸ Các vai trò tham gia dự án phần mềm (WHAT)**
Stakeholders (các bên liên quan): khách hàng, nhà tài trợ, tổ chức thực hiện, công chúng. Trong Scrum: Product Owner, Scrum Master, Development Team. Trong dự án truyền thống: PM, BA, Architect, Developer, Tester, QA/QC.
_Nguồn: [02_software_project.md](../materials/02_software_project.md) — dòng 116; [04_02_scrum_development_process.md](../materials/04_02_scrum_development_process.md) — dòng 108-131_

**▸ Phân biệt các loại kết quả dự án (WHAT)**

| Mức độ                         | Định nghĩa                                                          |
| ------------------------------ | ------------------------------------------------------------------- |
| **Thành công (Success)**       | Đúng hạn, đúng ngân sách, đủ tính năng, khách hàng hài lòng         |
| **Có thách thức (Challenged)** | Hoàn thành nhưng vượt ngân sách, trễ hạn, ít tính năng hơn          |
| **Thất bại (Failure)**         | Bị hủy trước khi hoàn thành, hoặc bàn giao nhưng không được sử dụng |

_Nguồn: [02_software_project.md](../materials/02_software_project.md) — dòng 151-158_

**▸ Nguyên nhân dự án phần mềm thất bại (WHY)**

1. Mục tiêu không thực tế/không rõ ràng; 2. Giao tiếp kém; 3. Ước tính không chính xác; 4. Báo cáo kém; 5. Công nghệ chưa trưởng thành; 6. Không xử lý được sự phức tạp; 7. Thực tiễn phát triển cẩu thả; 8. Yêu cầu xác định sai; 9. Quản lý dự án kém; 10. Thay đổi liên tục yêu cầu; 11. Chính trị stakeholder; 12. Áp lực thương mại.
   _Nguồn: [02_software_project.md](../materials/02_software_project.md) — dòng 163-177_

**▸ Ràng buộc dự án (WHAT)**
Tam giác phát triển: **Thời gian – Chi phí – Phạm vi/Chất lượng** (Tốt – Nhanh – Rẻ, chỉ chọn tối đa 2 trong 3). Tăng một yếu tố phải đánh đổi yếu tố khác.
_Nguồn: [02_software_project.md](../materials/02_software_project.md) — dòng 188-195_

**▸ Các câu hỏi chính trong Đề xuất dự án (HOW)**
Tài liệu cần trả lời: (1) Tên dự án; (2) Vấn đề (Problems) — NOT features; (3) Giải pháp (Solution) — trường hợp sử dụng kinh doanh cốt lõi; (4) Lý do giải quyết vấn đề; (5) Đối thủ cạnh tranh (tối thiểu 3); (6) Điểm khác biệt.
_Nguồn: [02_software_project.md](../materials/02_software_project.md) — dòng 225-236_

**▸ Tại sao cần tạo tài liệu Đề xuất dự án? (WHY)**
Để xác định rõ ràng vấn đề cần giải quyết, đánh giá tính khả thi ban đầu, so sánh với đối thủ cạnh tranh, và làm cơ sở cho các bước tiếp theo (Vision & Scope, Charter, WBS...).

**▸ Khi nào thực hiện? (WHEN)**
Giai đoạn khởi đầu dự án (Project Initiation), trước khi tạo tài liệu Vision & Scope và Project Charter.
_Nguồn: [03_software_project_initiation.md](../materials/03_software_project_initiation.md) — dòng 56-63_

---

### 2. Viễn cảnh và phạm vi dự án (Project Vision and Scope)

Trình bày quá trình hình thành và phương pháp đánh giá tài liệu Viễn cảnh và phạm vi dự án (Project Vision and Scope) của nhóm. _(Sinh viên nộp kèm bản in tài liệu Viễn cảnh và phạm vi dự án của nhóm.)_

**Các câu hỏi thường gặp:**

- Các câu hỏi chính cần trả lời trong tài liệu Viễn cảnh và phạm vi dự án là gì?
- Các đầu vào cần thiết và các bước nhóm đã thực hiện để tạo tài liệu Viễn cảnh và phạm vi dự án là gì?
- Tài liệu Viễn cảnh và phạm vi dự án của nhóm đã được đánh giá thế nào?
- Tại sao cần tạo tài liệu Viễn cảnh và phạm vi dự án?
- Tài liệu Viễn cảnh và phạm vi dự án của nhóm đã được sử dụng và cập nhật trong quá trình thực hiện dự án như thế nào?

#### ĐÁP ÁN LÝ THUYẾT

**▸ WHAT — Tài liệu Vision & Scope là gì?**
Tài liệu mô tả tầm nhìn tổng thể của dự án (mục tiêu kinh doanh, đối tượng người dùng, bối cảnh) và xác định rõ phạm vi sản phẩm (các tính năng IN scope và OUT of scope). Được tạo từ Yêu cầu người dùng (User Requirements).
_Nguồn: [03_software_project_initiation.md](../materials/03_software_project_initiation.md) — dòng 60-62; [03_1_business_requirements.md](../materials/03_1_business_requirements.md)_

**▸ HOW — Các đầu vào và bước thực hiện?**

1. Thu thập yêu cầu kinh doanh (Business Requirements) → Tóm tắt điều hành (Executive Summary).
2. Thu thập yêu cầu người dùng (User Requirements) → Tầm nhìn và phạm vi.
3. Xác định stakeholders, phân tích SWOT, benchmarking.
4. Xác định phạm vi sản phẩm (Product Scope) vs phạm vi dự án (Project Scope).
   _Nguồn: [03_software_project_initiation.md](../materials/03_software_project_initiation.md) — dòng 56-63; [03_2_user_requirements.md](../materials/03_2_user_requirements.md)_

**▸ WHY — Tại sao cần tạo?**
Để tất cả stakeholders có chung hiểu biết về mục tiêu và giới hạn dự án; làm cơ sở cho ước lượng, lập kế hoạch và kiểm soát phạm vi; tránh scope creep.

**▸ WHEN — Khi nào thực hiện?**
Giai đoạn Khởi tạo dự án (Initiation), sau khi có Đề xuất dự án, trước khi tạo Project Charter và bắt đầu lập kế hoạch chi tiết.

---

### 3. Ủy nhiệm dự án (Project Charter)

Trình bày quá trình hình thành và phương pháp đánh giá tài liệu Ủy nhiệm dự án (Project Charter) của nhóm. _(Sinh viên nộp kèm bản in tài liệu Ủy nhiệm dự án của nhóm.)_

**Các câu hỏi thường gặp:**

- Các câu hỏi chính cần trả lời trong tài liệu Ủy nhiệm dự án là gì?
- Các đầu vào cần thiết và các bước nhóm đã thực hiện để tạo tài liệu Ủy nhiệm dự án là gì?
- Tài liệu Ủy nhiệm dự án của nhóm đã được đánh giá thế nào?
- Tại sao cần tạo tài liệu Ủy nhiệm dự án?
- Tài liệu Ủy nhiệm dự án của nhóm đã được sử dụng và cập nhật trong quá trình thực hiện dự án như thế nào?

#### ĐÁP ÁN LÝ THUYẾT

**▸ WHAT — Project Charter là gì?**
Là tài liệu **chính thức cho phép** (formally authorizes) một dự án hoặc giai đoạn, ghi lại các yêu cầu ban đầu đáp ứng nhu cầu và mong đợi của các bên liên quan.
_Nguồn: [03_software_project_initiation.md](../materials/03_software_project_initiation.md) — dòng 66-80_

**▸ HOW — Nội dung chính của Project Charter:**

1. Bối cảnh, ngữ cảnh, tổng quan (Background, Context, Overview).
2. Quản lý và quản trị dự án — vai trò/tên/trách nhiệm.
3. Cơ sở vật chất và tài nguyên dự án.
4. Các cột mốc quan trọng (Milestones).
5. Phân tích tác động (Impact Analysis).
6. Giả định (Assumptions).
7. Chữ ký phê duyệt (Signatures).

**Danh sách kiểm tra:** Tại sao dự án này? Vấn đề là gì? Sản phẩm bàn giao là gì? Giải quyết như thế nào (kỹ thuật + quản lý)? Khi nào hoàn thành?
_Nguồn: [03_software_project_initiation.md](../materials/03_software_project_initiation.md) — dòng 71-90_

**▸ WHY — Tại sao cần?**
Để chính thức hóa sự ủy quyền cho dự án, xác định rõ vai trò/trách nhiệm, cột mốc, giả định và làm cơ sở pháp lý cho việc sử dụng tài nguyên.

**▸ WHEN — Khi nào?**
Tạo trong giai đoạn Khởi tạo (Initiation), sau khi có Vision & Scope, trước khi thực hiện Kickoff Meeting.

---

### 4. Yêu cầu phần mềm (Software Requirements / Product Backlog)

Trình bày quá trình hình thành và phương pháp đánh giá tài liệu Yêu cầu phần mềm (Software Requirements, hay Product Backlog) của nhóm. _(Sinh viên nộp kèm bản in tài liệu Yêu cầu phần mềm và bản in tài liệu Hướng dẫn sử dụng hệ thống của nhóm.)_

**Các câu hỏi thường gặp:**

- Các câu hỏi chính cần trả lời trong tài liệu Yêu cầu phần mềm là gì?
- Các đầu vào cần thiết và các bước nhóm đã thực hiện để tạo tài liệu tài liệu Yêu cầu phần mềm là gì?
- Tài liệu Yêu cầu phần mềm của nhóm đã được đánh giá thế nào?
- Tại sao cần tạo tài liệu Yêu cầu phần mềm?
- Tài liệu Yêu cầu phần mềm của nhóm đã được sử dụng và cập nhật trong quá trình thực hiện dự án như thế nào?

#### ĐÁP ÁN LÝ THUYẾT

**▸ WHAT — Yêu cầu phần mềm là gì?**
Là việc suy luận, phân tích, đặc tả và xác nhận các yêu cầu đối với phần mềm. Bao gồm: Gợi ý yêu cầu → Phân tích & đàm phán → Đặc tả → Mô hình hóa → Xác thực → Quản lý yêu cầu.
_Nguồn: [04_software_development_life_cycle_model.md](../materials/04_software_development_life_cycle_model.md) — dòng 31-46_

**Product Backlog** (trong Scrum) là danh sách toàn diện các chức năng và tính năng cần phát triển. Chỉ cần xác định rõ những gì cần làm cho Sprint tiếp theo.
_Nguồn: [04_02_scrum_development_process.md](../materials/04_02_scrum_development_process.md) — dòng 148-151_

**▸ HOW — Các bước thực hiện:**

1. Thu thập yêu cầu kinh doanh (Business Requirements) và yêu cầu người dùng.
2. Phân tích, đàm phán và ưu tiên hóa yêu cầu.
3. Đặc tả yêu cầu dưới dạng User Stories, Use Cases, hoặc SRS.
4. Xác thực yêu cầu với stakeholders.
5. Sản phẩm đầu ra: Từ điển thuật ngữ, Quy tắc kinh doanh, Product Backlog, User stories.
   _Nguồn: [03_1_business_requirements.md](../materials/03_1_business_requirements.md); [03_2_user_requirements.md](../materials/03_2_user_requirements.md)_

**▸ WHY — Tại sao cần?**
Yêu cầu xác định sai là một trong các nguyên nhân hàng đầu dẫn đến thất bại dự án. Tài liệu yêu cầu làm cơ sở cho thiết kế, phát triển, kiểm thử và nghiệm thu.

**▸ WHEN — Khi nào?**
Bắt đầu từ giai đoạn Initiation, liên tục cập nhật trong suốt dự án (đặc biệt trong Agile: mỗi Sprint cập nhật Product Backlog).

---

### 5. Kiến trúc phần mềm (Software Architecture)

Trình bày quá trình hình thành và phương pháp đánh giá tài liệu Kiến trúc phần mềm (Software Architecture) của nhóm. _(Sinh viên nộp kèm bản in tài liệu Kiến trúc phần mềm của nhóm.)_

**Các câu hỏi thường gặp:**

- Các câu hỏi chính cần trả lời trong tài liệu Kiến trúc phần mềm là gì?
- Các đầu vào cần thiết và các bước nhóm đã thực hiện để tạo tài liệu Kiến trúc phần mềm là gì?
- Tài liệu Kiến trúc phần mềm của nhóm đã được đánh giá thế nào?
- Tại sao cần tạo tài liệu Kiến trúc phần mềm?
- Tài liệu Kiến trúc phần mềm của nhóm đã được sử dụng và cập nhật trong quá trình thực hiện dự án như thế nào?

#### ĐÁP ÁN LÝ THUYẾT

**▸ WHAT — Kiến trúc phần mềm là gì?**
Thiết kế phần mềm là quy trình giải quyết vấn đề và lập kế hoạch cho giải pháp, bao gồm cả kiến trúc hệ thống (architectural view) và triển khai chi tiết. Câu hỏi cần trả lời: Tại sao chọn phong cách kiến trúc này? Tại sao chọn ngăn xếp công nghệ này? Tại sao chọn nền tảng/framework này?
_Nguồn: [04_software_development_life_cycle_model.md](../materials/04_software_development_life_cycle_model.md) — dòng 49-58; [03_software_project_initiation.md](../materials/03_software_project_initiation.md) — dòng 175-179_

**▸ HOW — Các bước thực hiện:**

1. Xem xét các hạng mục backlog được giao.
2. Phân tích miền và cập nhật mô hình miền.
3. Xác định các thay đổi cần thiết về kiến trúc.
4. Tinh chỉnh kiến trúc để hỗ trợ bối cảnh mới.
5. Tổ chức cuộc họp đánh giá thiết kế.
   _Nguồn: [06_1_agile_planning.md](../materials/06_1_agile_planning.md) — dòng 145-154_

**▸ WHY — Tại sao cần?**
Để đảm bảo hệ thống có cấu trúc rõ ràng, dễ mở rộng, bảo trì và đáp ứng các yêu cầu phi chức năng (hiệu suất, bảo mật, khả năng mở rộng).

**▸ WHEN — Khi nào?**
Sau khi có yêu cầu phần mềm ban đầu, trước khi bắt đầu triển khai (Construction). Trong Agile: tạo kiến trúc ban đầu trong Iteration 0, tinh chỉnh dần qua các Sprint.

---

### 6. Chứng minh ý tưởng (Proof of Concept)

Trình bày quá trình hình thành và phương pháp đánh giá sản phẩm Chứng minh ý tưởng (Proof of Concept) của nhóm. _(Sinh viên nộp kèm bản in giao diện thể hiện đầu vào và đầu ra khi chạy mã nguồn Chứng minh ý tưởng của nhóm.)_

**Các câu hỏi thường gặp:**

- Sản phẩm Chứng minh ý tưởng (Proof of Concept) là gì?
- Giải thích các phương pháp có thể dùng để chứng minh khả năng hoàn thành dự án về mặt kỹ thuật.
- Nhóm chọn sản phẩm gì để Chứng minh ý tưởng?
- Các đầu vào cần thiết và các bước nhóm đã thực hiện để tạo sản phẩm Chứng minh ý tưởng là gì?
- Tại sao cần tạo sản phẩm Chứng minh ý tưởng?
- Sản phẩm Chứng minh ý tưởng của nhóm đã được sử dụng trong quá trình thực hiện dự án như thế nào?

#### ĐÁP ÁN LÝ THUYẾT

**▸ WHAT — PoC là gì?**
Proof of Concept (PoC) là sản phẩm mã nguồn thực thi nhằm chứng minh tính khả thi kỹ thuật của giải pháp được đề xuất. PoC xác minh rằng nhóm có khả năng hoàn thành dự án về mặt công nghệ.
_Nguồn: [03_software_project_initiation.md](../materials/03_software_project_initiation.md) — dòng 23-24_

**▸ HOW — Phương pháp chứng minh:**

1. Xác định các rủi ro kỹ thuật lớn nhất (công nghệ mới, thuật toán phức tạp, tích hợp bên thứ ba).
2. Xây dựng mã nguồn thực thi nhỏ gọn (exercise source code) giải quyết các rủi ro đó.
3. Demo đầu vào/đầu ra của PoC cho stakeholders.
   _Nguồn: [05_1_work_breakdown_structure.md](../materials/05_1_work_breakdown_structure.md) — dòng 62-67 (Vòng 3 WBS cần xem lại PoC)_

**▸ WHY — Tại sao cần?**
Giảm thiểu rủi ro kỹ thuật sớm; xác nhận giải pháp khả thi trước khi đầu tư lớn; hỗ trợ tài liệu nghiên cứu khả thi (Feasibility Study).

**▸ WHEN — Khi nào?**
Giai đoạn Initiation, sau khi có yêu cầu ban đầu và kiến trúc sơ bộ, trước khi lập WBS chi tiết.

---

### 7. Bản mẫu (Prototype)

Trình bày quá trình hình thành và phương pháp đánh giá sản phẩm Bản mẫu (Prototype) của nhóm. _(Sinh viên nộp kèm bản in phác thảo giao diện ban đầu cho hệ thống của nhóm.)_

**Các câu hỏi thường gặp:**

- Sản phẩm Bản mẫu là gì?
- Giải thích sự khác nhau giữa bản mẫu hệ thống và tập hợp các màn hình giao diện hệ thống.
- Các đầu vào cần thiết và các bước nhóm đã thực hiện để tạo sản phẩm Bản mẫu là gì?
- Sản phẩm Bản mẫu của nhóm đã được đánh giá thế nào?
- Tại sao cần tạo sản phẩm Bản mẫu?
- Sản phẩm Bản mẫu của nhóm đã được sử dụng trong quá trình thực hiện dự án như thế nào?

#### ĐÁP ÁN LÝ THUYẾT

**▸ WHAT — Prototype là gì?**
Bản mẫu (Prototype) là mô hình mô phỏng hệ thống cho phép người dùng tương tác, đánh giá giao diện và luồng công việc trước khi phát triển chính thức. Khác với tập hợp màn hình (mockup/wireframe):

- **Prototype:** có tương tác, mô phỏng luồng nghiệp vụ (có thể click, chuyển trang).
- **Mockup/Wireframe:** chỉ là hình ảnh tĩnh thiết kế giao diện, không có tương tác.
  _Nguồn: [03_software_project_initiation.md](../materials/03_software_project_initiation.md) — dòng 21-22_

**▸ WHY — Tại sao cần?**
Để thu thập phản hồi sớm từ người dùng; làm rõ yêu cầu chưa rõ ràng; giảm rủi ro yêu cầu sai; hỗ trợ việc xem xét lại yêu cầu (WBS Vòng 2).
_Nguồn: [05_1_work_breakdown_structure.md](../materials/05_1_work_breakdown_structure.md) — dòng 61-62_

**▸ WHEN — Khi nào?**
Giai đoạn Initiation hoặc đầu giai đoạn phát triển, khi yêu cầu chưa rõ ràng.

---

### 8. Báo cáo tính khả thi (Feasibility Study Report)

Trình bày quá trình hình thành và phương pháp đánh giá tài liệu Báo cáo tính khả thi (Feasibility Study Report) của nhóm. _(Sinh viên nộp kèm bản in tài liệu Báo cáo tính khả thi của nhóm.)_

**Các câu hỏi thường gặp:**

- Các câu hỏi chính cần trả lời trong tài liệu Báo cáo tính khả thi là gì?
- Các đầu vào cần thiết và các bước nhóm đã thực hiện để tạo tài liệu Báo cáo tính khả thi là gì?
- Tài liệu Báo cáo tính khả thi của nhóm đã được đánh giá thế nào?
- Tại sao cần tạo tài liệu Báo cáo tính khả thi?
- Tài liệu Báo cáo tính khả thi của nhóm đã được sử dụng trong quá trình thực hiện dự án như thế nào?

#### ĐÁP ÁN LÝ THUYẾT

**▸ WHAT — Nghiên cứu khả thi là gì?**
Là đánh giá chi tiết về nhu cầu, giá trị, và tính thực tiễn của dự án được đề xuất. Các loại khả thi: Pháp lý, Thị trường, Kinh tế, Công nghệ & Hệ thống, Nguồn lực, Vận hành, Lập kế hoạch, Văn hóa.
_Nguồn: [03_software_project_initiation.md](../materials/03_software_project_initiation.md) — dòng 105-124_

**▸ HOW — Cấu trúc báo cáo:**

1. Mục đích (Purpose); 2. Lý do (Reason); 3. Thông tin cơ bản; 4. Tiêu chí đánh giá; 5. Kết quả nghiên cứu; 6. Khuyến nghị.
   Công cụ phân tích tài chính: Biểu đồ lợi nhuận, Phân tích Chi phí-Lợi ích, ROI.
   _Nguồn: [03_software_project_initiation.md](../materials/03_software_project_initiation.md) — dòng 136-152_

**▸ WHY — Tại sao cần?**
Phân tích yêu cầu đầy đủ; xác định và lập kế hoạch rủi ro; phân tích chi phí/lợi ích; lập kế hoạch đào tạo.
_Nguồn: [03_software_project_initiation.md](../materials/03_software_project_initiation.md) — dòng 125-134_

**▸ WHEN — Khi nào?**
Giai đoạn Initiation, sau khi có Đề xuất dự án và Vision & Scope, trước khi quyết định tiến hành dự án.

---

### 9. Định nghĩa quy trình phát triển phần mềm (Software Process Definition)

Trình bày quá trình hình thành và phương pháp đánh giá tài liệu Định nghĩa quy trình phát triển phần mềm (Software Process Definition) của nhóm. _(Sinh viên nộp kèm bản in tài liệu Định nghĩa quy trình phát triển phần mềm của nhóm.)_

**Các câu hỏi thường gặp:**

- Các câu hỏi chính cần trả lời trong tài liệu Định nghĩa quy trình phát triển phần mềm là gì?
- Mô hình cơ sở được lựa chọn để hiệu chỉnh là gì?
- Thời gian dự kiến của từng giai đoạn là bao lâu?
- Các vai trò nào từng thành viên trong nhóm sẽ đảm nhiệm?
- Các sản phẩm nào dự kiến sẽ khởi tạo?
- Quy trình để đưa ra một bản phân phối hoạt động là gì?
- Ưu và khuyết điểm của mô hình nhóm lựa chọn là gì?
- Tài liệu Định nghĩa quy trình phát triển phần mềm của nhóm đã được đánh giá thế nào?
- Tại sao cần tạo tài liệu Định nghĩa quy trình phát triển phần mềm?
- Tài liệu Định nghĩa quy trình phát triển phần mềm của nhóm đã được sử dụng và cập nhập trong quá trình thực hiện dự án như thế nào?

#### ĐÁP ÁN LÝ THUYẾT

**▸ WHAT — Mô hình SDLC là gì?**
Mô hình vòng đời phần mềm (SDLCM) là đặc tính mô tả hoặc quy định của sự phát triển phần mềm, bao gồm: Giai đoạn, Hoạt động, Công việc, Sản phẩm, Vai trò, Mẫu, Tiêu chuẩn, Thực hành.
_Nguồn: [04_software_development_life_cycle_model.md](../materials/04_software_development_life_cycle_model.md) — dòng 101-129_

**▸ HOW — Mô hình SDLC cần định nghĩa:**
Vòng đời (giai đoạn phân cấp/chồng chéo) → Tiêu chí đầu vào → Đầu vào → Vai trò → Nhiệm vụ → Luồng quy trình → Sản phẩm bàn giao → Điểm kiểm tra → Đầu ra → Tiêu chí thoát.
_Nguồn: [04_software_development_life_cycle_model.md](../materials/04_software_development_life_cycle_model.md) — dòng 131-148_

**Các mô hình phổ biến:** Waterfall, Iterative, Scrum/Agile. Mỗi mô hình có ưu/nhược riêng.

- Scrum: Phù hợp môi trường phức tạp, nhiều thay đổi; Sprint 2-4 tuần.
  _Nguồn: [04_01_software_development_models.md](../materials/04_01_software_development_models.md); [04_02_scrum_development_process.md](../materials/04_02_scrum_development_process.md) — dòng 280-301_

**▸ WHY — Tại sao cần định nghĩa SDLCM?**
Mô hình xác định rõ giúp đạt kết quả tốt và nhất quán, năng suất và chất lượng. Mô hình không xác định dẫn đến kết quả không nhất quán, gánh nặng tài liệu/cuộc họp không cần thiết.
_Nguồn: [04_software_development_life_cycle_model.md](../materials/04_software_development_life_cycle_model.md) — dòng 120-130, 153-158_

**▸ WHEN — Khi nào?**
Giai đoạn Initiation/Planning, trước khi bắt đầu phát triển.

---

### 10. Ước lượng dự án (Project Estimate)

Trình bày quá trình hình thành và phương pháp đánh giá tài liệu Ước lượng dự án (Project Estimate) của nhóm. _(Sinh viên nộp kèm bản in tài liệu Ước lượng dự án của nhóm.)_

**Các câu hỏi thường gặp:**

- Các câu hỏi chính cần trả lời trong tài liệu Ước lượng dự án là gì?
- Các đầu vào cần thiết và các bước nhóm đã thực hiện để tạo tài liệu Ước lượng dự án là gì?
- Tài liệu Ước lượng dự án của nhóm đã được đánh giá thế nào?
- Tại sao cần tạo tài liệu Ước lượng dự án?
- Tài liệu Ước lượng dự án của nhóm đã được sử dụng trong quá trình thực hiện dự án như thế nào?
- Giải thích các phương pháp phân rã một tính năng lớn thành các tính năng nhỏ.
- Khi không có khả năng phân rã được các tính năng lớn của dự án, nhóm phải làm thế nào?
- Ước lượng có thể sai lệch khoảng bao nhiêu lần ở giai đoạn đầu dự án?
- Tại sao cần ước lượng ở giai đoạn đầu của dự án?
- Ước lượng kích cỡ (Size) mang lại lợi ích gì cho dự án khi mối quan tâm chính của ban quản lý là khoảng thời gian (Duration) và chi phí (Cost) cần thiết để hoàn thành dự án?
- Giải thích quy tắc "Đếm, Tính toán và Đánh giá" khi thực hiện ước lượng dự án?
- Giải thích các kỹ thuật để tăng độ chính xác khi thực hiện việc ước lượng bằng đánh giá chủ quan?
- Giải thích các kỹ thuật để tăng độ chính xác khi ước lượng bằng phương pháp "Phân rã và Kết hợp" ("Decomposition and Recomposition")?
- Giải thích kỹ thuật ước lượng bằng các lá bài (Planning Poker).

#### ĐÁP ÁN LÝ THUYẾT

**▸ WHAT — Ước lượng dự án là gì?**
Là quá trình xác định kích cỡ (Size), nỗ lực (Effort = Staff × Time), thời gian (Duration) và chi phí (Cost) của dự án. Công thức WBS: Effort = Staff × Time.
_Nguồn: [05_1_work_breakdown_structure.md](../materials/05_1_work_breakdown_structure.md) — dòng 31-42; [05_2_introduction_to_software_estimation.md](../materials/05_2_introduction_to_software_estimation.md)_

**▸ HOW — Phương pháp phân rã WBS:**
Các loại phân rã: Theo sản phẩm, Theo hệ thống, Theo tính năng, Theo use case, Theo pha, Theo hoạt động chung. WBS qua 3 vòng: Vòng 1 (phân rã sơ bộ) → Vòng 2 (thêm ước tính nỗ lực) → Vòng 3 (chi tiết sau khi có SRS).
_Nguồn: [05_1_work_breakdown_structure.md](../materials/05_1_work_breakdown_structure.md) — dòng 45-68, 71-188_

**▸ Quy tắc "Đếm, Tính toán và Đánh giá" (Count, Compute, Judge):**

- **Đếm (Count):** Đếm trực tiếp các yếu tố đo được (số use case, số màn hình, số bảng DB).
- **Tính toán (Compute):** Dùng mô hình toán học (FPA, UCP, COCOMO) để tính.
- **Đánh giá (Judge):** Khi không thể đếm/tính được, dùng đánh giá chuyên gia.
  _Nguồn: [05_2_introduction_to_software_estimation.md](../materials/05_2_introduction_to_software_estimation.md)_

**▸ Planning Poker (WHAT + HOW):**
Kỹ thuật ước lượng nhóm: Mỗi thành viên có bộ bài Fibonacci (1,2,3,5,8,13,21...). PM mô tả story → mọi người úp bài → lật cùng lúc → thảo luận sai biệt → lặp lại cho đến khi đồng thuận. Chìa khóa: **tính tương đối** — chọn 1 story quen thuộc cho 3 điểm, so sánh các story khác với nó.
_Nguồn: [05_3_agile_estimation.md](../materials/05_3_agile_estimation.md); [06_1_agile_planning.md](../materials/06_1_agile_planning.md) — dòng 51-56_

**▸ Khi không phân rã được (HOW):**
Cần xem lại PoC (Proof of Concept), prototype hoặc nghiên cứu thêm để hiểu rõ hơn yêu cầu trước khi phân rã.
_Nguồn: [05_1_work_breakdown_structure.md](../materials/05_1_work_breakdown_structure.md) — dòng 61-67_

**▸ Ước lượng Size mang lại lợi ích gì? (WHY)**
Size là cơ sở để suy ra Duration và Cost: `Effort = f(Size)`, `Duration = f(Effort)`, `Cost = f(Duration, Resources)`. Không có Size thì không thể ước lượng chính xác hai yếu tố còn lại.

**▸ WHY — Tại sao cần ước lượng sớm?**
Dù sai lệch có thể lên đến 4x ở giai đoạn đầu, ước lượng sớm cần thiết để: xác định ngân sách ban đầu, lập kế hoạch phát hành, phân bổ tài nguyên, và đánh giá tính khả thi.

---

### 11. Kế hoạch dự án (Project Plan)

Trình bày quá trình hình thành và phương pháp đánh giá tài liệu Kế hoạch dự án (Project Plan) của nhóm. _(Sinh viên nộp kèm bản in tài liệu Kế hoạch dự án của nhóm.)_

**Các câu hỏi thường gặp:**

- Các câu hỏi chính cần trả lời trong tài liệu Kế hoạch dự án là gì?
- Các đầu vào cần thiết và các bước nhóm đã thực hiện để tạo tài liệu Kế hoạch dự án là gì?
- Tài liệu Kế hoạch dự án của nhóm đã được đánh giá thế nào?
- Tại sao cần tạo tài liệu Kế hoạch dự án?
- Tài liệu Kế hoạch dự án của nhóm đã được sử dụng và cập nhật trong quá trình thực hiện dự án như thế nào?
- Một số mô hình cho phép không xác định rõ các kết quả cuối cùng của dự án, vậy có cần tạo tài liệu Kế hoạch dự án trong các trường hợp này hay không?
- Tài liệu Kế hoạch dự án khác gì với tài liệu Định nghĩa quy trình phát triển phần mềm.

#### ĐÁP ÁN LÝ THUYẾT

**▸ WHAT — Kế hoạch dự án là gì?**
Tài liệu mô tả cụ thể: kích thước dự án, thời gian, chi phí, lịch trình, phân công nguồn lực, cột mốc, và các hoạt động cần thực hiện. Trong Agile: Product Roadmap → Release Plan → Sprint Plan.
_Nguồn: [06_software_project_planning.md](../materials/06_software_project_planning.md); [06_1_agile_planning.md](../materials/06_1_agile_planning.md) — dòng 75-99_

**▸ HOW — Quy trình lập kế hoạch phát hành (Agile):**

1. Tạo ước tính cấp cao (story points); 2. Tạo lộ trình sản phẩm; 3. Ưu tiên backlog; 4. Tạo Sprint Map; 5. Tạo kế hoạch phát hành sơ bộ; 6. Xác định ràng buộc phát hành; 7. Chi tiết kế hoạch; 8. Tính chi phí; 9. Tạo dự toán; 10. Chuẩn bị phát hành; 11. Tạo kiến trúc; 12. Iteration 0.
   _Nguồn: [06_1_agile_planning.md](../materials/06_1_agile_planning.md) — dòng 85-99_

**▸ Kế hoạch dự án vs. Định nghĩa quy trình (WHAT):**

- **Định nghĩa quy trình:** Mô tả **cách thức** (HOW) — mô hình, giai đoạn, vai trò, quy tắc chung.
- **Kế hoạch dự án:** Mô tả **cụ thể** — lịch trình, nhân sự, ngân sách, cột mốc cho dự án này.

**▸ WHY — Có cần kế hoạch trong Agile?**
Có! Agile vẫn cần kế hoạch nhưng tập trung vào **quá trình lập kế hoạch** hơn là kế hoạch cố định. Kế hoạch dễ thay đổi, được cập nhật mỗi Sprint.
_Nguồn: [06_1_agile_planning.md](../materials/06_1_agile_planning.md) — dòng 41-50_

---

### 12. Phát biểu công việc (Statement of Work)

Trình bày quá trình hình thành và phương pháp đánh giá tài liệu Phát biểu công việc (Statement of Work) của nhóm. _(Sinh viên nộp kèm bản in tài liệu Phát biểu công việc của nhóm.)_

**Các câu hỏi thường gặp:**

- Các câu hỏi chính cần trả lời trong tài liệu Phát biểu công việc là gì?
- Các đầu vào cần thiết và các bước nhóm đã thực hiện để tạo tài liệu Phát biểu công việc là gì?
- Tài liệu Phát biểu công việc của nhóm đã được đánh giá thế nào?
- Tại sao cần tạo tài liệu Phát biểu công việc?
- Tài liệu Phát biểu công việc của nhóm đã được sử dụng và cập nhật trong quá trình thực hiện dự án như thế nào?
- Giải thích sự khác nhau về thời gian và chi phí giữa các tài liệu: Đề xuất dự án, Ước lượng dự án, và Phát biểu công việc.
- Các câu hỏi chính cần trả lời trong tài liệu Hợp đồng dự án phần mềm (Software Contract) là gì?
- Giải thích sự khác nhau giữa Hợp đồng giá cố định và Hợp đồng theo nguyên vật liệu và thời gian.

#### ĐÁP ÁN LÝ THUYẾT

**▸ WHAT — SOW là gì?**
Statement of Work (SOW) là tài liệu mô tả chi tiết phạm vi công việc, sản phẩm bàn giao, tiến độ, chi phí cam kết chính thức với khách hàng. SOW là cơ sở cho hợp đồng (Contract).

**▸ Sự khác biệt về thời gian và chi phí giữa Đề xuất / Ước lượng / SOW:**

| Tài liệu            | Thời gian & Chi phí                   | Mức độ chính xác     |
| ------------------- | ------------------------------------- | -------------------- |
| **Đề xuất dự án**   | Sơ bộ, ước chừng                      | Thấp (có thể sai 4x) |
| **Ước lượng dự án** | Chi tiết hơn, dựa trên WBS/FPA/UCP    | Trung bình           |
| **SOW**             | Cam kết chính thức, ràng buộc pháp lý | Cao nhất             |

**▸ Hợp đồng giá cố định vs. Hợp đồng T&M (WHAT):**

- **Hợp đồng giá cố định (Fixed-Price):** Giá biết trước, phạm vi đóng băng. Ưu: Khách hàng an tâm chi phí. Nhược: Thay đổi tốn kém.
- **Hợp đồng T&M (Time & Materials):** Thanh toán theo thời gian và vật liệu thực tế. Ưu: Linh hoạt. Nhược: Khách hàng cần quản lý vi mô.
- **Hợp đồng Agile Fixed-Price:** Chia sẻ rủi ro, yêu cầu có thể thay đổi, giao phần mềm làm việc mỗi 2-3 tuần.
  _Nguồn: [06_1_agile_planning.md](../materials/06_1_agile_planning.md) — dòng 175-209_

---

### 13. Mô hình tích hợp liên tục (Continuous Integration)

Vẽ và giải thích mô hình tích hợp liên tục (Continuous Integration) của nhóm. Ghi chú trên mô hình các công cụ nhóm đã dùng cho từng thành phần. Tại sao cần sử dụng hệ thống tích hợp liên tục cho dự án? _(Sinh viên nộp kèm bản in kịch bản build (build scripts), giao diện email nhận thông báo về kết quả build từ hệ thống build tự động, và bản in tài liệu Hướng dẫn cài đặt công cụ và biên dịch mã nguồn hệ thống cho máy tính của nhà phát triển của nhóm)._

#### ĐÁP ÁN LÝ THUYẾT

**▸ WHAT — CI là gì?**
Tích hợp liên tục (Continuous Integration) là thực hành trong đó các thay đổi mã nguồn của lập trình viên được **xác thực tự động** bằng cách tạo bản dựng (build) và chạy kiểm thử (automated tests) mỗi khi có commit.
_Nguồn: [07_software_configuration_management.md](../materials/07_software_configuration_management.md) — dòng 205-209_

**▸ HOW — Mô hình CI điển hình:**
Developer commit code → Version Control (Git/GitHub) → CI Server trigger build → Chạy Unit Tests → Thông báo kết quả (email/Slack).
Công cụ phổ biến: GitHub Actions, GitLab CI, Jenkins, CircleCI.
_Nguồn: [07_software_configuration_management.md](../materials/07_software_configuration_management.md) — dòng 194-204_

**▸ WHY — Tại sao cần CI?**
Phát hiện lỗi sớm ngay khi code được tích hợp; giảm chi phí sửa lỗi; đảm bảo code build không lỗi mọi lúc; tăng tự tin của nhóm khi commit.

---

### 14. Mô hình chuyển giao liên tục (Continuous Delivery)

Vẽ và giải thích mô hình chuyển giao liên tục (Continuous Delivery) của nhóm. Ghi chú trên mô hình các công cụ nhóm đã dùng cho từng thành phần. Tại sao cần sử dụng hệ thống chuyển giao liên tục cho dự án? _(Sinh viên nộp kèm bản in kịch bản triển khai (deployment scripts), kịch bản cấu hình cơ sở dữ liệu, cấu hình các dịch vụ bên thứ ba, bản in giao diện email nhận thông báo về kết quả triển khai tự động, và bản in tài liệu Hướng dẫn triển khai hệ thống cho kỹ sư vận hành của nhóm.)_

#### ĐÁP ÁN LÝ THUYẾT

**▸ WHAT — CD là gì?**
Phân phối liên tục (Continuous Delivery) là mở rộng của CI, tự động hóa quy trình phát hành để có thể **triển khai ứng dụng bất kỳ lúc nào** chỉ bằng một nút bấm. Khác với Continuous Deployment (tự động hoàn toàn không cần can thiệp).
_Nguồn: [07_software_configuration_management.md](../materials/07_software_configuration_management.md) — dòng 207-209_

**▸ HOW — Mô hình CD:**
CI Pipeline → Automated Tests (Unit, Integration, E2E) → Staging Environment → Manual Approval → Production Deployment.

**▸ WHY — Tại sao cần CD?**
Giảm thời gian từ code đến triển khai; giảm rủi ro triển khai nhờ các bước tự động hóa; tăng tần suất phát hành; phản hồi nhanh từ khách hàng.

---

### 15. Mô hình DevOps

Vẽ và giải thích mô hình DevOps của nhóm. Ghi chú trên mô hình các công cụ nhóm đã dùng cho từng thành phần. Tại sao cần sử dụng quy trình DevOps cho dự án? Giải thích quy trình phát triển, triển khai và vận hành liên tục đồng thời nhiều phiên bản trên của dự án bằng cách áp dụng DevOps. _(Sinh viên nộp kèm bản in kịch bản khởi tạo và cấu hình tài nguyên hạ tầng cho việc triển khai hệ thống của nhóm, bản in hệ thống thư mục và tập tin hỗ trợ quản lý hạ tầng triển khai.)_

#### ĐÁP ÁN LÝ THUYẾT

**▸ WHAT — DevOps là gì?**
DevOps là tập hợp các thực hành kết hợp phát triển phần mềm (Dev) và vận hành IT (Ops), bao gồm: CI/CD, Infrastructure as Code, Feature Flags, Continuous Monitoring, Backup & Archiving.
_Nguồn: [07_software_configuration_management.md](../materials/07_software_configuration_management.md) — dòng 190-217_

**▸ HOW — Các thực hành DevOps:**

- **Infrastructure as Code:** Dùng scripts để tự động hóa hạ tầng (Docker, Kubernetes, Ansible).
- **Feature Flags:** Sử dụng cấu hình/IF-ELSE để kích hoạt/vô hiệu tính năng mới.
- **Continuous Monitoring:** Giám sát liên tục hệ thống.
- **Backup & Archiving:** Sao lưu và lưu trữ dữ liệu.

**▸ WHY — Tại sao cần DevOps?**
Tự động hóa quy trình từ phát triển → triển khai → vận hành; hỗ trợ vận hành đồng thời nhiều phiên bản (staging, production); phản hồi nhanh; giảm lỗi do con người.

---

### 16. Quản lý con người và phát triển nhóm

Trình bày quá trình hình thành và phát triển nhóm mà nhóm đã trải qua. Liệt kê các vấn đề liên quan đến quản lý con người nhóm đã thực sự vướng phải. Trình bày cách nhóm đã giải quyết các vấn đề này và kết quả thu được (có thể thành công, có thể không thành công). _(Sinh viên nộp kèm bản in ảnh chụp chung các thành viên trong nhóm, bản in tài liệu quy định, quy chế, lịch làm việc của nhóm, bản in một biên bản họp của nhóm, bản in giao diện hệ thống liên lạc với dữ liệu thực tế của nhóm.)_

**Các câu hỏi thường gặp:**

- Giải thích các giai đoạn phát triển nhóm.
- Giải thích các loại hình tổ chức: Theo chức năng, theo dự án, ma trận yếu, ma trận cân bằng và ma trận mạnh.
- Giải thích các mô hình quản lý nhóm: X, Y, Z.
- Giải thích nguyên tắc xử lý mâu thuẫn trong một nhóm.
- Giải thích các phương pháp tăng năng suất làm việc của nhóm.
- Giải thích mô hình tháp nhu cầu của Maslow.

#### ĐÁP ÁN LÝ THUYẾT

**▸ Các loại hình tổ chức (WHAT):**

- **Tổ chức chức năng (Functional):** Nhóm theo phòng ban chuyên môn.
- **Tổ chức dự án (Projectized):** Nhân sự toàn thời gian cho dự án, PM toàn quyền.
- **Tổ chức ma trận (Matrix):** Kết hợp. Ma trận yếu (PM điều phối), Ma trận cân bằng, Ma trận mạnh (PM quyền lực cao).
  _Nguồn: [08_software_team_management.md](../materials/08_software_team_management.md) — dòng 99-108_

**▸ Nguyên tắc xử lý mâu thuẫn (HOW):**

| Kỹ thuật                      | Mô tả                    | Hiệu quả                 |
| ----------------------------- | ------------------------ | ------------------------ |
| Rút lui/Tránh né              | Bỏ đi, từ chối thảo luận | Không giải quyết tận gốc |
| Xoa dịu/Nhượng bộ             | Nhấn mạnh điểm chung     | Không lâu dài            |
| Ép buộc/Áp đặt                | Dùng quyền lực áp đặt    | Tạm thời                 |
| Thỏa hiệp/Hòa giải            | Mỗi bên từ bỏ một phần   | Trung dung               |
| **Hợp tác/Giải quyết vấn đề** | Tìm sự thật, đồng thuận  | **Win-Win, lâu dài**     |

_Nguồn: [08_software_team_management.md](../materials/08_software_team_management.md) — dòng 141-153_

**▸ Tháp nhu cầu Maslow (WHAT):**

1. Sinh lý & An toàn → Mức độ sinh tồn (Survive).
2. Xã hội, Tôn trọng & Khẳng định bản thân → Mức độ phát triển mạnh mẽ (Thrive).
   _Nguồn: [08_software_team_management.md](../materials/08_software_team_management.md) — dòng 177-183_

**▸ Phương pháp tăng năng suất (HOW):**
Năng suất thực sự = đạt được nhiều hơn trong 1 giờ làm việc (English Theory), KHÔNG phải bóc lột (Spanish Theory). Cách tăng: Job Enrichment — giao nhiệm vụ mới thử thách, chuyên môn hóa, giảm kiểm soát, cung cấp thông tin trực tiếp.
_Nguồn: [08_software_team_management.md](../materials/08_software_team_management.md) — dòng 156-201_

**▸ Định luật Brooks (WHY):**
"Việc bổ sung nhân lực vào một dự án phần mềm muộn sẽ càng khiến dự án bị chậm trễ hơn" — do chi phí giao tiếp và đào tạo nhân sự mới tăng nhanh.
_Nguồn: [08_software_team_management.md](../materials/08_software_team_management.md) — dòng 244-248_

---

### 17. Phân công, theo dõi, đánh giá, kiểm soát công việc và báo cáo tình trạng dự án

Trình bày quá trình phân công, theo dõi, đánh giá, kiểm soát các công việc dự án, và báo cáo tình trạng dự án của nhóm. _(Sinh viên nộp kèm bản in giao diện hệ thống phân công, theo dõi công việc với dữ liệu thực tế của nhóm, bản in giao diện hệ thống quản lý thời gian đã dùng cho từng công việc với dữ liệu thực tế của nhóm, bản in bản cập nhật tài liệu Kế hoạch dự án theo dữ liệu thực tiễn, biểu đồ burndown của toàn dự án, tài liệu báo cáo tình trạng toàn bộ dự án của nhóm ở tuần trước tuần thi giữa học kỳ.)_

**Các câu hỏi thường gặp:**

- Làm sao để giải quyết vấn đề vượt phạm vi dự kiến (Scope Creep)?
- Làm sao để giải quyết vấn đề vượt công sức dự kiến (Effort Creep)?
- Làm sao để các thay đổi không trở nên bất ngờ và ảnh hưởng tiêu cực đến sự thành công của dự án?

**Các câu hỏi thường gặp cho mô hình Scrum:**

- Giải thích Sprint Backlogs, Sprint Boards, Sprint Tasks, Sprint Burndown Charts, Project Burndown Charts.
- Phải xử lý thế nào khi kết thúc một Sprint mà nhóm không đưa ra được bản phân phối?
- Phải xử lý thế nào khi kết quả của các Sprint chênh lệch một cách bất bình thường?

**Các câu hỏi thường gặp cho mô hình Kanban:**

- Giải thích Kanban Board, Development Workflow, WIP.

**Các câu hỏi thường gặp cho mô hình Waterfall:**

- Giải thích phương pháp cập nhật lịch trình, phương pháp tính toán thời gian, chi phí cần thiết để hoàn thành các công việc còn lại.

#### ĐÁP ÁN LÝ THUYẾT

**▸ Scope Creep (HOW giải quyết):**
Sử dụng quy trình kiểm soát thay đổi chính thức (Change Control Process): Yêu cầu thay đổi → Mô tả → Phân tích tác động → CCB phê duyệt → Cập nhật kế hoạch → Triển khai → Xác minh.
_Nguồn: [09_software_project_monitoring_and_control.md](../materials/09_software_project_monitoring_and_control.md) — dòng 99-131_

**▸ Effort Creep (HOW giải quyết):**

| Nguyên nhân          | Giải pháp                                      |
| -------------------- | ---------------------------------------------- |
| Ước tính thấp        | Dùng quỹ dự phòng rủi ro                       |
| Thiết kế quá mức     | Yêu cầu hiểu rõ giải pháp trước khi triển khai |
| Bùng nổ yêu cầu ngầm | Kiểm soát yêu cầu phái sinh                    |
| Ranh giới mờ nhạt    | Xác định rõ phạm vi trong hợp đồng             |
| Thiếu kỹ năng        | Tuyển dụng/đào tạo                             |

_Nguồn: [09_software_project_monitoring_and_control.md](../materials/09_software_project_monitoring_and_control.md) — dòng 85-96_

**▸ EVM — Quản lý giá trị thu được (WHAT + HOW):**

- PV (Planned Value), EV (Earned Value), AC (Actual Cost), BAC (Budget at Completion).
- SV = EV - PV; SPI = EV/PV; CV = EV - AC; CPI = EV/AC.
- EAC = BAC/CPI.
  _Nguồn: [09_software_project_monitoring_and_control.md](../materials/09_software_project_monitoring_and_control.md) — dòng 165-192_

**▸ Sprint (Scrum) — Các khái niệm:**

- **Sprint Backlog:** Danh sách công việc nhóm phải giải quyết trong Sprint.
- **Sprint Tasks:** Tính năng chia thành nhiệm vụ 4-16 giờ.
- **Burndown Chart:** Cho thấy mỗi ngày còn bao nhiêu việc.
- **Velocity:** Lượng công việc đã hoàn thành mỗi Sprint.
  _Nguồn: [04_02_scrum_development_process.md](../materials/04_02_scrum_development_process.md) — dòng 171-235_

**▸ Khi Sprint không đưa ra bản phân phối (HOW):**
Sử dụng iteration slack; đơn giản hóa/trì hoãn nhiệm vụ; giảm phạm vi (chia nhỏ/loại bỏ story). **Tuyệt đối không thay đổi deadline Sprint.**
_Nguồn: [09_1_agile_project_monitoring_and_control.md](../materials/09_1_agile_project_monitoring_and_control.md) — dòng 52-65_

---

### 18. Kế hoạch quản lý rủi ro (Software Risk Management Plan)

Trình bày quá trình hình thành và phương pháp đánh giá tài liệu Kế hoạch quản lý rủi ro (Software Risk Management Plan) của nhóm. _(Sinh viên nộp kèm bản in tài liệu Kế hoạch quản lý rủi ro của nhóm.)_

**Các câu hỏi thường gặp:**

- Các câu hỏi chính cần trả lời trong tài liệu Kế hoạch quản lý rủi ro là gì?
- Các đầu vào cần thiết và các bước nhóm đã thực hiện để tạo tài liệu Kế hoạch quản lý rủi ro là gì?
- Tài liệu Kế hoạch quản lý rủi ro của nhóm đã được đánh giá thế nào?
- Tại sao cần tạo tài liệu Kế hoạch quản lý rủi ro?
- Tài liệu Kế hoạch quản lý rủi ro của nhóm đã được sử dụng và cập nhật trong quá trình thực hiện dự án như thế nào.

#### ĐÁP ÁN LÝ THUYẾT

**▸ WHAT — Rủi ro là gì?**
Rủi ro là khả năng xảy ra điều xấu ở tương lai. Phân biệt: **Rủi ro** (chưa xảy ra) vs. **Vấn đề** (đã xảy ra).
_Nguồn: [10_software_risk_management.md](../materials/10_software_risk_management.md) — dòng 36-47_

**▸ HOW — Quy trình quản lý rủi ro:**

1. **Xác định rủi ro:** Brainstorming, Risk taxonomies, Phân rã, Critical path, Phỏng vấn.
2. **Phân tích rủi ro:** Xác suất × Tác động = Risk Exposure (RE).
3. **Lập kế hoạch ứng phó:** Chấp nhận, Tránh né, Chuyển giao, Giảm thiểu.
4. **Giám sát & Kiểm soát:** Theo dõi tiến trình, hành động khắc phục.
   _Nguồn: [10_software_risk_management.md](../materials/10_software_risk_management.md) — dòng 52-57, 75-137, 202-224_

**▸ Chiến lược ứng phó rủi ro (HOW):**

- **Chấp nhận (Acceptance):** Thừa nhận nhưng không hành động phủ đầu.
- **Tránh né (Avoidance):** Loại bỏ điều kiện cho phép rủi ro.
- **Chuyển giao (Transfer):** Mua bảo hiểm, thuê ngoài.
- **Giảm thiểu (Mitigation):** Chủ động giảm xác suất hoặc tác động.
  _Nguồn: [10_software_risk_management.md](../materials/10_software_risk_management.md) — dòng 131-137_

**▸ Agile Risk — Hệ số rủi ro (HOW):**
Dùng Risk Multipliers: Mức cam kết 90% (nghiêm ngặt: ×1.8; rủi ro: ×4.0) để điều chỉnh vận tốc khi lập kế hoạch phát hành.
_Nguồn: [10_1_agile_risk_management.md](../materials/10_1_agile_risk_management.md) — dòng 55-78_

**▸ WHY — Tại sao cần?**
"Nếu bạn không chủ động tấn công rủi ro, rủi ro sẽ chủ động tấn công bạn" — Tom Gilb.
_Nguồn: [10_software_risk_management.md](../materials/10_software_risk_management.md) — dòng 223-224_

---

### 19. Kế hoạch quản lý chất lượng (Software Quality Management Plan)

Trình bày quá trình hình thành và phương pháp đánh giá tài liệu Kế hoạch quản lý chất lượng (Software Quality Management Plan) của nhóm. _(Sinh viên nộp kèm bản in tài liệu Kế hoạch quản lý chất lượng của nhóm, bản in định nghĩa hoàn thành (Definition of Done) của nhóm, bản in giao diện cấu hình đảm bảo Coding Standards cho mã nguồn của nhóm, bản in biên bản thanh tra mã nguồn của nhóm, bản in biên bản phản hồi từ khách hàng của nhóm.)_

**Các câu hỏi thường gặp:**

- Các câu hỏi chính cần trả lời trong tài liệu Kế hoạch quản lý chất lượng là gì?
- Các đầu vào cần thiết và các bước nhóm đã thực hiện để tạo tài liệu Kế hoạch quản lý chất lượng là gì?
- Tài liệu Kế hoạch quản lý chất lượng của nhóm đã được đánh giá thế nào?
- Tại sao cần tạo tài liệu Kế hoạch quản lý chất lượng?
- Tài liệu Kế hoạch quản lý chất lượng của nhóm đã được sử dụng và cập nhật trong quá trình thực hiện dự án như thế nào.
- Giải thích sự hỗ trợ của các mô hình McCall, ISO 9126 trong việc kiểm soát chất lượng các sản phẩm của dự án?
- Đo lường định tính khác gì đo lường định lượng (qualitative vs. quantitative measurement)?
- Giải thích phương pháp đo lường chất lượng các sản phẩm, quy trình và con người trong một dự án.
- Giải thích các phương pháp giúp hạn chế việc các tài liệu dự án không đúng với yêu cầu khách hàng đề ra.
- Giải thích các phương pháp giúp hạn chế việc mã nguồn hệ thống không đúng với thiết kế đề ra.
- Giải thích các phương pháp giúp hạn chế việc phần mềm hoạt động không đúng với yêu cầu khách hàng đề ra.

#### ĐÁP ÁN LÝ THUYẾT

**▸ WHAT — Chất lượng là gì?**
Chất lượng là mức độ mà một tập hợp các đặc tính vốn có đáp ứng các yêu cầu. Mục tiêu: Đạt chất lượng và chi phí ở mức chấp nhận được.
_Nguồn: [11_software_quality_management.md](../materials/11_software_quality_management.md) — dòng 37-44, 71-72_

**▸ McCall (11 yếu tố) vs. ISO 9126 (WHAT):**

- **McCall:** Correctness, Reliability, Efficiency, Integrity, Usability, Maintainability, Testability, Flexibility, Portability, Reusability, Interoperability.
- **ISO 9126:** Functionality, Reliability, Usability, Efficiency, Maintainability, Portability — mỗi nhóm có các đặc tính phụ chi tiết.
  _Nguồn: [11_software_quality_management.md](../materials/11_software_quality_management.md) — dòng 74-100_

**▸ Định tính vs. Định lượng (WHAT):**

- **Định tính (Qualitative):** Mô tả bằng từ ngữ, không đo bằng số (màu sắc, đánh giá chủ quan).
- **Định lượng (Quantitative):** Đo lường bằng số (thời gian, chi phí, số lỗi).
  _Nguồn: [11_software_quality_management.md](../materials/11_software_quality_management.md) — dòng 112-116_

**▸ QA vs. QC (WHAT):**

- **QA (Quality Assurance):** Tập trung vào **Quy trình**, **ngăn ngừa** khiếm khuyết.
- **QC (Quality Control):** Tập trung vào **Sản phẩm**, **phát hiện** khiếm khuyết.
  _Nguồn: [11_software_quality_management.md](../materials/11_software_quality_management.md) — dòng 193-200_

**▸ Hạn chế tài liệu sai (HOW):** Review/Walkthrough tài liệu với stakeholders; sử dụng Requirements Traceability Matrix.
_Nguồn: [09_software_project_monitoring_and_control.md](../materials/09_software_project_monitoring_and_control.md) — dòng 149-152_

**▸ Hạn chế mã nguồn sai thiết kế (HOW):** Code Inspection (review mã nguồn); Coding Standards; Unit Testing.
_Nguồn: [11_1_agile_quality_management.md](../materials/11_1_agile_quality_management.md) — dòng 30-62_

**▸ Hạn chế phần mềm sai yêu cầu (HOW):** Kiểm thử chức năng, kiểm thử chấp nhận (Acceptance Testing), phản hồi khách hàng, Sprint Review/Demo.
_Nguồn: [04_software_development_life_cycle_model.md](../materials/04_software_development_life_cycle_model.md) — dòng 79-87_

---

### 20. Kế hoạch kiểm thử (Test Plan)

Trình bày quá trình hình thành và phương pháp đánh giá tài liệu Kế hoạch kiểm thử (Test Plan) của nhóm. _(Sinh viên nộp kèm bản in tài liệu Kế hoạch kiểm thử của nhóm, bản in giao diện cấu hình đảm bảo Coding Standards cho mã nguồn của nhóm, bản in giao diện hệ thống quản lý lỗi với dữ liệu thực tế của nhóm, bản in giao diện kết quả chạy mã nguồn kiểm thử đơn vị (Unit Tests) của nhóm, bản in biên bản thanh tra mã nguồn của nhóm, bản in báo cáo kết quả kiểm thử của nhóm, bản in biên bản phản hồi của khách hàng của nhóm.)_

**Các câu hỏi thường gặp:**

- Các câu hỏi chính cần trả lời trong tài liệu Kế hoạch kiểm thử là gì?
- Các đầu vào cần thiết và các bước nhóm đã thực hiện để tạo tài liệu Kế hoạch kiểm thử là gì?
- Tài liệu Kế hoạch kiểm thử của nhóm đã được đánh giá thế nào?
- Tại sao cần tạo tài liệu Kế hoạch kiểm thử?
- Tài liệu Kế hoạch kiểm thử của nhóm đã được sử dụng và cập nhật trong quá trình thực hiện dự án như thế nào.

#### ĐÁP ÁN LÝ THUYẾT

**▸ WHAT — Kiểm thử phần mềm là gì?**
Là các điều tra thực nghiệm để cung cấp cho stakeholders thông tin về chất lượng của sản phẩm, liên quan đến bối cảnh mà nó dự định hoạt động.
_Nguồn: [04_software_development_life_cycle_model.md](../materials/04_software_development_life_cycle_model.md) — dòng 79-87_

**▸ HOW — Nội dung Kế hoạch kiểm thử:**

1. Phạm vi kiểm thử (Scope); 2. Loại kiểm thử (Unit, Integration, System, Acceptance); 3. Tiêu chí đầu vào/đầu ra; 4. Môi trường kiểm thử; 5. Lịch trình; 6. Vai trò và trách nhiệm; 7. Tiêu chí chấp nhận.

Trong Agile: Unit Testing + Exploratory Testing + Code Inspection + Sprint Review (demo cho khách hàng).
_Nguồn: [11_1_agile_quality_management.md](../materials/11_1_agile_quality_management.md) — dòng 41-53_

**▸ Definition of Done (DoD) — ví dụ:**
Coded to standards → Reviewed → Unit tested → 100% test automation → Integrated → Documented → Tested by other member → Accepted by PO.
_Nguồn: [04_02_scrum_development_process.md](../materials/04_02_scrum_development_process.md) — dòng 200-226_

**▸ WHY — Tại sao cần?**
"Sửa lỗi trên giấy luôn dễ dàng và rẻ hơn so với xây dựng xong rồi mới sửa lỗi." Kiểm thử phải được lập kế hoạch và hỗ trợ xuyên suốt dự án.
_Nguồn: [09_software_project_monitoring_and_control.md](../materials/09_software_project_monitoring_and_control.md) — dòng 146_

---

### 21. Báo cáo bài học kinh nghiệm (Lessons Learned Register)

Trình bày quá trình hình thành và phương pháp đánh giá tài liệu Báo cáo bài học kinh nghiệm (Lessons Learned Register) của nhóm. _(Sinh viên nộp kèm bản in tài liệu Báo cáo bài học kinh nghiệm của nhóm.)_

**Các câu hỏi thường gặp:**

- Quản lý dự án là gì?
- Tại sao cần sự quản lý khi phát triển một dự án phần mềm?
- Liệt kê các công việc cần thực hiện để quản lý một dự án và các sản phẩm tương ứng được tạo ra bởi từng công việc.
- Một nhóm phát triển phần mềm có thực sự cần một người chỉ chuyên tâm vào các công việc quản lý trong dự án hay không? Tại sao?
- Quản lý một dự án dựa trên việc lên kế hoạch chặt chẽ có điểm gì giống và có điểm gì khác với quản lý một dự án dựa trên kinh nghiệm tích lũy dần và thích ứng với hoàn cảnh?
- Quản lý dự án và kỹ nghệ phần mềm liên quan với nhau như thế nào?
- Tại sao các công ty có quy mô lớn lại cần có Phòng quản lý dự án (Project Management Office)?

#### ĐÁP ÁN LÝ THUYẾT

**▸ WHAT — Quản lý dự án là gì?**
Là việc áp dụng kiến thức, kỹ năng, công cụ và kỹ thuật vào các hoạt động dự án nhằm đáp ứng yêu cầu của dự án. Đảm bảo: trong chi phí, đúng hạn, đúng phạm vi, đúng chất lượng.
_Nguồn: [12_software_project_management.md](../materials/12_software_project_management.md) — dòng 33-48_

**▸ WHY — Tại sao QLDA phần mềm khó?**
Sản phẩm vô hình; thiếu tính chính xác tuyệt đối; tiêu chuẩn hóa chưa đồng bộ; phụ thuộc lớn vào con người.
_Nguồn: [12_software_project_management.md](../materials/12_software_project_management.md) — dòng 50-56_

**▸ Các công việc quản lý dự án và sản phẩm tương ứng (HOW):**

| Công việc            | Sản phẩm                   |
| -------------------- | -------------------------- |
| Đề xuất dự án        | Project Proposal           |
| Tầm nhìn & Phạm vi   | Vision & Scope Document    |
| Ủy nhiệm dự án       | Project Charter            |
| Thu thập yêu cầu     | SRS / Product Backlog      |
| Thiết kế kiến trúc   | Architecture Document      |
| Ước lượng            | WBS, Estimation Document   |
| Lập kế hoạch         | Project Plan, Release Plan |
| Phát biểu công việc  | SOW, Contract              |
| Quản lý cấu hình     | CM Plan                    |
| Quản lý rủi ro       | Risk Management Plan       |
| Quản lý chất lượng   | SQAP                       |
| Kiểm thử             | Test Plan                  |
| Giám sát & Kiểm soát | Status Reports, EVM        |
| Đóng dự án           | Lessons Learned Register   |

**▸ Có cần PM chuyên trách? (WHY)**
Có. PM dành 80% thời gian giải quyết vấn đề con người (Human Dynamics), chỉ 20% cho kỹ thuật. PM hiểu cả góc nhìn kinh doanh lẫn kỹ thuật, dịch thuật giữa chúng. Thiếu PM → thiên kiến cá nhân, phe phái, lệch hướng dự án.
_Nguồn: [08_software_team_management.md](../materials/08_software_team_management.md) — dòng 77-78; [12_software_project_management.md](../materials/12_software_project_management.md) — dòng 91-95_

**▸ Ad-hoc vs. Process-driven (WHAT):**

- **Giống nhau:** Cả hai đều nhằm hoàn thành dự án thành công.
- **Khác nhau:**
  - **Ad-hoc:** Linh hoạt, chi phí thấp, rủi ro cao (mất người = mất dự án).
  - **Process-driven:** Văn bản hóa, giảm phụ thuộc cá nhân, chi phí thiết lập cao nhưng khả năng dự đoán tốt hơn.
    _Nguồn: [12_software_project_management.md](../materials/12_software_project_management.md) — dòng 129-138_

**▸ QLDA vs. Kỹ nghệ phần mềm (WHAT):**

- **Kỹ thuật phần mềm (SE):** Các hoạt động kỹ thuật xây dựng sản phẩm.
- **Quản lý dự án (PM):** Tạo điều kiện thuận lợi cho SE, đảm bảo đúng hạn, tiết kiệm, đúng mục tiêu.
- Hai khía cạnh liên kết lỏng lẻo nhưng bổ trợ lẫn nhau.
  _Nguồn: [12_software_project_management.md](../materials/12_software_project_management.md) — dòng 98-113_

**▸ WHAT — Lessons Learned là gì?**
Kiến thức thu được từ trải nghiệm thực tế (cả tích cực lẫn tiêu cực) để làm giàu kho tri thức tổ chức cho các dự án tương lai.
_Nguồn: [09_software_project_monitoring_and_control.md](../materials/09_software_project_monitoring_and_control.md) — dòng 224-226_

**▸ Tại sao cần PMO? (WHY)**
Khi tổ chức lớn lên, cách tiếp cận Ad-hoc không còn đáp ứng được. PMO cung cấp: quy trình chuẩn, công cụ, kho kiến thức, đào tạo và chuyên gia hỗ trợ — giảm thiểu phụ thuộc cá nhân, tăng khả năng dự đoán.
_Nguồn: [12_software_project_management.md](../materials/12_software_project_management.md) — dòng 129-138_

---

## CHUẨN BỊ

Lớp trưởng và lớp phó, độc lập với nhau, mỗi người làm bốn (2) bộ đề. Mỗi bộ đề bao gồm 21 câu hỏi ở trên. Mỗi bộ đề để riêng trong một túi ni lông. Mỗi câu hỏi là một lá phiếu có kích thước 12x12cm (xem ví dụ ở trang kế tiếp), gấp sẵn làm 4 trước khi bỏ vào túi.

Đối với các câu hỏi có nội dung quá dài, lớp trưởng và lớp phó chủ động làm phiếu to hơn (tất cả các phiếu cần có kích thước giống hệt nhau), hoặc thu nhỏ phông chữ lại.

Lớp trưởng và lớp phó, độc lập với nhau, nộp các bộ đề thi cho giảng viên lý thuyết trước giờ thi vấn đáp 15 phút, tại phòng thi vấn đáp.

Các bộ đề sẽ được kiểm tra trước khi đưa vào sử dụng. Các bộ đề thiếu câu hỏi, hoặc câu hỏi không đúng, hoặc câu hỏi bị trùng lắp, hoặc câu hỏi bị đánh dấu, sẽ không được sử dụng.

Xem phiếu câu hỏi mẫu ở trang kế tiếp.

---

## PHIẾU CÂU HỎI MẪU

_Xem ví dụ khác ở trang kế tiếp._

> **Họ tên:** **\*\*\*\***\_\_\_**\*\*\*\***
> **Mã số sinh viên:** **\*\*\*\***\_\_\_**\*\*\*\***
>
> **Câu hỏi 1.** Trình bày quá trình hình thành và phương pháp đánh giá tài liệu Đề xuất dự án (Project Proposal) của nhóm. (Sinh viên nộp kèm bản in tài liệu Đề xuất dự án của nhóm.)
>
> **Các câu hỏi thường gặp:** Các câu hỏi chính cần trả lời trong tài liệu Đề xuất dự án là gì? Các đầu vào cần thiết và các bước nhóm đã thực hiện để tạo tài liệu Đề xuất dự án là gì? Dựa vào những dữ liệu nào mà bản đề xuất được hình thành? Các sản phẩm cạnh tranh trực tiếp với đề xuất là gì? Tài liệu Đề xuất dự án của nhóm đã được đánh giá thế nào? Tại sao cần tạo tài liệu Đề xuất dự án? Tài liệu Đề xuất dự án của nhóm đã được sử dụng và cập nhật trong quá trình thực hiện dự án như thế nào? Dự án phần mềm là gì? Phân biệt dự án (project) với hoạt động (operation), với chương trình (program), và với danh sách đầu tư (portfolio). Dự án phần mềm đến từ đâu? Phạm vi dự án là gì? Các vai trò nào thường tham gia vào một dự án phần mềm? Phân biệt các loại kết quả của một dự án. Phân tích các nguyên nhân chính khiến một dự án phần mềm thất bại. Các ràng buộc của một dự án có ý nghĩa gì?

---

> **Họ tên:** **\*\*\*\***\_\_\_**\*\*\*\***
> **Mã số sinh viên:** **\*\*\*\***\_\_\_**\*\*\*\***
>
> **Câu hỏi 2.** Trình bày quá trình hình thành và phương pháp đánh giá tài liệu Viễn cảnh và phạm vi dự án (Project Vision and Scope) của nhóm. (Sinh viên nộp kèm bản in tài liệu Viễn cảnh và phạm vi dự án của nhóm.)
>
> **Các câu hỏi thường gặp:** Các câu hỏi chính cần trả lời trong tài liệu Viễn cảnh và phạm vi dự án là gì? Các đầu vào cần thiết và các bước nhóm đã thực hiện để tạo tài liệu Viễn cảnh và phạm vi dự án là gì? Tài liệu Viễn cảnh và phạm vi dự án của nhóm đã được đánh giá thế nào? Tại sao cần tạo tài liệu Viễn cảnh và phạm vi dự án? Tài liệu Viễn cảnh và phạm vi dự án của nhóm đã được sử dụng và cập nhật trong quá trình thực hiện dự án như thế nào?

---

## QUY TRÌNH VẤN ĐÁP

1. Mỗi sinh viên tự chuẩn bị 1 tờ giấy trắng A4 và 1 cây bút, trước khi vào phòng thi. Mỗi sinh viên tự in ra các thông tin cần nộp kèm với câu trả lời mình sẽ viết vào giấy A4, cho cá nhân mình. Sinh viên **KHÔNG** sử dụng các bản in này trong khi trả lời vào giấy A4. Sinh viên không mượn hoặc sử dụng các bản in của người khác, hoặc của nhóm khác.

2. Mỗi sinh viên sẽ được phát ngẫu nhiên 1 lá phiếu khi thi vấn đáp. Ngay sau khi nhận lá phiếu, sinh viên cần ghi Họ tên, Mã số sinh viên vào lá phiếu nhận được. Sinh viên được đổi phiếu tối đa 2 lần, mỗi lần đổi phiếu điểm vấn đáp của sinh viên sẽ bị trừ đi 2 điểm. Ví dụ, sinh viên đổi câu hỏi 1 lần thì điểm vấn đáp sẽ bị trừ đi 2 điểm, đổi câu hỏi 2 lần thì điểm vấn đáp sẽ bị trừ đi 4 điểm.

3. Toàn bộ các sinh viên có 10 phút để ghi câu trả lời vào giấy A4. Sinh viên **KHÔNG** sử dụng bản in liên quan đến câu hỏi trong quá trình trả lời vào giấy. Sinh viên không sử dụng bất kỳ tài liệu nào trong quá trình ghi câu trả lời vào giấy A4.

4. Sau 10 phút, toàn bộ các sinh viên có 2 phút để lựa chọn bản in liên quan đến câu hỏi mình nhận được, để nộp kèm. Sinh viên không ghi thêm vào giấy trả lời A4 trong 2 phút này. Sinh viên nên đánh số câu hỏi liên quan lên trên các sản phẩm in từ trước để việc lựa chọn được nhanh hơn.

5. Giảng viên đi thu câu trả lời, kèm theo câu hỏi được phát, và bản in liên quan trực tiếp đến câu trả lời của sinh viên.

6. Giảng viên gọi tên từng sinh viên lên vấn đáp theo số thứ tự trong danh sách.

7. Mỗi sinh viên có từ 5 – 10 phút để giải thích câu trả lời đã ghi trên giấy, và trả lời các câu hỏi vấn đáp của giảng viên.

### Một số lưu ý

1. Khi trả lời câu hỏi liên quan đến các khái niệm, phương pháp tổng quát, sinh viên cần tập trung trả lời ngắn gọn các câu hỏi **WHAT** (định nghĩa? đó là gì?), **HOW** (thực hiện vấn đề đó thế nào? bước 1 làm gì? bước 2 làm gì?…), **WHY** (tại sao lại làm như vậy? thuận lợi là gì? khó khăn là gì?), **WHEN** (khi nào thực hiện hoạt động? khi nào áp dụng phương pháp?)

2. Khi trả lời câu hỏi liên quan đến tài liệu, sinh viên cần tập trung trả lời rõ ràng từ các sự kiện đã thực sự xảy ra trong quá trình khởi tạo, đánh giá, sử dụng và cập nhật tài liệu được đề cập.

3. Khi trả lời câu hỏi liên quan đến mô hình, quy trình, sinh viên cần tập trung trả lời rõ ràng từ các sự kiện đã thực sự xảy ra trong quá trình thực hiện các hoạt động của mô hình, quy trình, các sản phẩm đầu vào, các sản phẩm được tạo ra của từng hoạt động.

4. Sinh viên cần trình bày to, rõ ràng, mạch lạc, logic, tập trung vào các kiến thức lý thuyết đã học, các bài thực hành đã làm, những gì mình đã thực nghiệm.

5. Sinh viên cần tránh trình bày vòng vo, tự mình suy diễn không dựa trên các sự kiện thực tế đã xảy ra, các công cụ, hệ thống mình đã thực hành, hay các sản phẩm mình thu được.

---

## ĐÁNH GIÁ

- **Điểm tối đa:** 10 điểm.
- Sinh viên không nộp bản giấy A4 ghi câu trả lời, hoặc bỏ trống: **0 điểm**.
- Sinh viên nộp bản giấy A4 ghi câu trả lời không liên quan đến nội dung lá phiếu: **0 điểm**.
- Sinh viên không trả lời được bất kỳ câu hỏi nào của giảng viên: **0 điểm**.
- Sinh viên trả lời được một phần các câu hỏi của giảng viên, hoặc không có đầy đủ các bản in kèm theo trong trường hợp câu hỏi yêu cầu nộp kèm bản in, hoặc nộp kèm bản in không liên quan đến nội dung lá phiếu: **tối đa 8 điểm**.
- Sinh viên trả lời được đầy đủ các câu hỏi của giảng viên, đồng thời nộp kèm đầy đủ các bản in liên quan nếu câu hỏi yêu cầu: **từ trên 8 đến 10 điểm**.
- Điểm cuối cùng là điểm trả lời vấn đáp được hiệu chỉnh lại theo số lần đổi phiếu, nếu có.

---

**--- CHÚC CÁC EM HOÀN THÀNH TỐT PHẦN THI VẤN ĐÁP. ---**
