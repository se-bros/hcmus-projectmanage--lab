# Quản lý chất lượng phần mềm (Software Quality Management)

**Giảng viên / Lecturer:** Ngô Huy Biên (Ngo Huy Bien) — nhbien@fit.hcmus.edu.vn
**Đơn vị / Department:** Bộ môn Kỹ thuật phần mềm, Khoa Công nghệ thông tin, Trường Đại học Khoa học Tự nhiên, ĐHQG-HCM
**Môn học / Course:** Quản lý Dự án Phần mềm (Software Project Management)

---

## 1. Mục tiêu bài học (Learning Objectives)

Sau bài học, người học có thể:

- Đáp ứng các yêu cầu kinh doanh, người dùng và kỹ thuật của phần mềm.
  _(Meet business, user, and technical requirements.)_
- Đo lường các đặc tính chất lượng của một sản phẩm, dự án, quy trình và con người.
  _(Measure quality characteristics of a product, project, process, and person.)_
- Giải thích khái niệm chất lượng, cách thực hiện quản lý chất lượng và tầm quan trọng của nó.
  _(Explain what is quality, how to perform quality management, and why it is important.)_
- Xây dựng kế hoạch quản lý chất lượng dự án.
  _(Create a quality management plan.)_
- Trình bày các khái niệm chính và quy trình triển khai tiêu chuẩn ISO 9001.
  _(Present key concepts of ISO 9001.)_

## 2. Nội dung (Contents Overview)

| #   | Chủ đề (VI)                                     | Topic (EN)                                   |
| --- | ----------------------------------------------- | -------------------------------------------- |
| I   | Đáp ứng yêu cầu chất lượng                      | Meeting Quality Requirements                 |
| II  | Đặc tính chất lượng phần mềm                    | Software Quality Characteristics             |
| III | Đo lường chất lượng phần mềm                    | Software Quality Measurement                 |
| IV  | Số liệu chất lượng quy trình, dự án & con người | Process, Project, and Person Quality Metrics |
| V   | Kế hoạch Đảm bảo chất lượng (SQAP) & QA/QC      | Quality Assurance Plan & QA/QC               |
| VI  | Hệ thống quản lý chất lượng & Tiêu chuẩn ISO    | Quality Management System & ISO Standards    |

---

## I. Đáp ứng yêu cầu chất lượng (Meeting Quality Requirements)

### 1.1 Mục tiêu chất lượng dự án

- Bàn giao sản phẩm nhưng khách hàng/nhà tài trợ không chấp nhận do chất lượng thấp, dẫn đến dự án thất bại.
- Tuy nhiên, chất lượng cao nhất không phải lúc nào cũng cần thiết vì làm tăng chi phí quá cao.
- **Mục tiêu tối cao:** Đạt được chất lượng và chi phí ở mức độ chấp nhận được.
  _(Goal: Acceptable Quality and Cost.)_

### 1.2 Cách thức đáp ứng các nhóm yêu cầu

**1. Yêu cầu kinh doanh (Business Requirements):**

- Đảm bảo các chỉ tiêu ngân sách và doanh thu.
- So sánh hiệu quả chi phí với các hệ thống tương tự trong lịch sử.

**2. Yêu cầu người dùng (User Requirements):**

- Giải quyết đúng bài toán và đạt được mục tiêu của người dùng.
- Sử dụng nguyên mẫu (prototypes, workflow/story map) để kiểm thử thăm dò (khảo sát cả đầu vào sai/độc hại).
- Thiết lập và nâng cao chất lượng các trường hợp kiểm thử (test cases) và trường hợp sử dụng (use cases).
- _Ví dụ yêu cầu hiệu suất:_ Thời gian phản hồi tiêu chuẩn $\le 3\text{s}$; mức sử dụng CPU tối đa 25%; mức sử dụng RAM tối đa 600MB.

**3. Yêu cầu kỹ thuật (Technical Requirements):**

- Quy định rõ ràng Định nghĩa hoàn thành (Definition of Done - DoD).
- Thiết lập tiêu chuẩn và quy ước mã hóa (coding standards & conventions).
- Viết các unit tests có chất lượng để bao phủ mã nguồn.
- _Ví dụ yêu cầu bảo mật:_ Cấu hình hệ điều hành máy chủ bảo mật, thực hiện kiểm thử xâm nhập (Penetration Testing), áp dụng giao thức mã hóa an toàn (như TLS 1.2).

---

## II. Đặc tính chất lượng phần mềm (Software Quality Characteristics)

> Chất lượng là mức độ mà một tập hợp các đặc tính vốn có đáp ứng các yêu cầu (nhu cầu hoặc mong đợi).
> _(Quality is the degree to which a set of inherent characteristics fulfills requirements.)_

### 2.1 Mô hình chất lượng McCall (11 yếu tố chất lượng) \[1\]

McCall phân loại chất lượng phần mềm thành các đặc tính bên ngoài:

1. **Tính đúng đắn (Correctness):** Mức độ chương trình đáp ứng thông số kỹ thuật và hoàn thành mục tiêu của người dùng.
2. **Độ tin cậy (Reliability):** Khả năng thực hiện chức năng dự định với độ chính xác yêu cầu.
3. **Hiệu quả (Efficiency):** Lượng tài nguyên máy tính và mã nguồn cần thiết để thực hiện chức năng.
4. **Tính toàn vẹn (Integrity):** Mức độ kiểm soát việc truy cập trái phép vào phần mềm hoặc dữ liệu.
5. **Khả năng sử dụng (Usability):** Nỗ lực cần thiết để học, vận hành, chuẩn bị đầu vào và diễn giải đầu ra.
6. **Khả năng bảo trì (Maintainability):** Nỗ lực cần thiết để xác định và sửa lỗi trong chương trình đang vận hành.
7. **Khả năng kiểm thử (Testability):** Nỗ lực cần thiết để kiểm thử chương trình đảm bảo chạy đúng.
8. **Tính linh hoạt (Flexibility):** Nỗ lực cần thiết để sửa đổi một chương trình đang hoạt động.
9. **Tính di động (Portability):** Nỗ lực để chuyển chương trình từ cấu hình phần cứng/phần mềm này sang cấu hình khác.
10. **Khả năng tái sử dụng (Reusability):** Mức độ một chương trình có thể sử dụng lại trong các ứng dụng khác.
11. **Khả năng tương tác (Interoperability):** Nỗ lực cần thiết để kết hợp hệ thống này với hệ thống khác.

### 2.2 Tiêu chuẩn ISO/IEC 9126 (Mô hình chất lượng sản phẩm phần mềm) \[2\]

| Đặc tính chính                         | Các đặc tính phụ (Subcharacteristics)                                                                                                          |
| -------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| **Chức năng (Functionality)**          | Sự phù hợp (Suitability), Sự chính xác (Accuracy), Khả năng tương tác (Interoperability), Bảo mật (Security).                                  |
| **Độ tin cậy (Reliability)**           | Độ trưởng thành (Maturity), Khả năng chịu lỗi (Fault tolerance), Khả năng phục hồi (Recoverability).                                           |
| **Khả năng sử dụng (Usability)**       | Dễ hiểu (Understandability), Khả năng học hỏi (Learnability), Khả năng vận hành (Operability), Sự hấp dẫn (Attractiveness).                    |
| **Hiệu quả (Efficiency)**              | Hành vi thời gian (Time behavior), Hành vi tài nguyên (Resource behavior).                                                                     |
| **Khả năng bảo trì (Maintainability)** | Khả năng phân tích (Analyzability), Khả năng thay đổi (Changeability), Sự ổn định (Stability), Khả năng kiểm thử (Testability).                |
| **Tính di động (Portability)**         | Khả năng thích ứng (Adaptability), Khả năng cài đặt (Installability), Khả năng cùng tồn tại (Coexistence), Khả năng thay thế (Replaceability). |

---

## III. Đo lường chất lượng phần mềm (Software Quality Measurement)

### 3.1 Chuyển đổi ý tưởng mơ hồ thành chỉ số đo lường được

Đo lường phần mềm thu thập thông tin về sản phẩm, quá trình, dự án và môi trường nhằm cụ thể hóa các khái niệm chất lượng mơ hồ:

- _Ý tưởng mơ hồ:_ Tính đúng đắn (Correctness) $\rightarrow$ _Số lượng đo được:_ Số test cases $\rightarrow$ _Số liệu (Metric):_ Số lượng test cases chạy thành công (passed).
- _Ý tưởng mơ hồ:_ Khả năng sử dụng (Usability) $\rightarrow$ _Số lượng đo được:_ Thời gian học hệ thống $\rightarrow$ _Số liệu (Metric):_ Thời gian học trung bình của 100 người dùng (ví dụ: tiêu chuẩn $\le 10$ phút).

### 3.2 Phân biệt dữ liệu định tính và định lượng

- **Dữ liệu định tính (Qualitative Data):** Thỏa thuận với mô tả bằng từ ngữ, danh mục (có thể quan sát nhưng không đo lường được bằng số). Ví dụ: màu sắc, mùi vị, kết cấu, ngoại hình, đánh giá chủ quan kiểu _"Làm tốt lắm!"_.
- **Dữ liệu định lượng (Quantitative Data):** Thỏa thuận với các con số (có thể đo lường và biểu diễn bằng số). Ví dụ: chiều cao, cân nặng, thời gian, chi phí, tuổi tác, số lượng lỗi.

### 3.3 Quy trình định lượng (Quantification Steps)

1. Mô tả thực thể được đo lường (ví dụ: ứng dụng phần mềm).
2. Mô tả đặc tính muốn tìm hiểu (ví dụ: hiệu suất sử dụng tài nguyên).
3. Mô tả các thuộc tính sẽ đo và số liệu kết quả (ví dụ: CPU sử dụng %, dung lượng bộ nhớ MB).
4. Mô tả cách thức tiếp cận đo lường (ví dụ: khởi động Task Manager để xác định các giá trị).
5. Có tiêu chuẩn so sánh (ví dụ: CPU $\le 10\%$, RAM $\le 200\text{MB}$).

### 3.4 Số liệu chất lượng phần mềm từ góc nhìn của khách hàng \[4\]

- **Thời gian trung bình hoạt động không lỗi (Mean Time To Failure — MTTF).**
- **Khoảng thời gian giữa các lỗi (Time Between Failures).**
- **Mật độ lỗi (Defect Density):** Tỷ lệ số lượng lỗi chia cho kích thước phần mềm (KLOC, Function Points).
- **Vấn đề của khách hàng (Customer Problems):** Tổng số sự cố do khách hàng báo cáo (cả lỗi thực sự và các vấn đề ngoài lỗi) trong một khoảng thời gian.
- **Sự hài lòng của khách hàng (Customer Satisfaction):** Đánh giá qua khảo sát (Hài lòng, Bình thường, Không hài lòng).

---

## IV. Số liệu chất lượng quy trình, dự án & con người (Process, Project & Person Metrics)

### 4.1 Số liệu chất lượng quy trình (Process Quality Metrics) \[5\]

Dùng để đánh giá chất lượng của mô hình quy trình phần mềm (Software Process Model):

- **NA:** Số lượng hoạt động (activities) của mô hình quy trình.
- **NWP:** Số lượng sản phẩm công việc (work products).
- **NPR:** Số lượng vai trò (roles) tham gia vào quy trình.
- **NDWPIn:** Số lượng phụ thuộc đầu vào của sản phẩm công việc đối với hoạt động trong quy trình.
- **NDWPOut:** Số lượng phụ thuộc đầu ra của sản phẩm công việc đối với hoạt động.
- **NDWP:** Tổng số phụ thuộc giữa sản phẩm và hoạt động:
  $$NDWP = NDWPIn + NDWPOut$$
- **NDA:** Số lượng phụ thuộc ưu tiên giữa các hoạt động.

### 4.2 Số liệu chất lượng dự án (Project Quality Metrics) \[6\]

- **Năng suất (Productivity):** Số dòng code (SLOC), số mô-đun, số lớp hoặc số sản phẩm bàn giao phát triển được trên một đơn vị thời gian hoặc trên mỗi tài nguyên.
- **Chất lượng (Quality):** Mức độ hài lòng của khách hàng hoặc cấp quản lý sau khi hoàn thành mục tiêu dự án.
- **Độ phức tạp dự án:** Độ phức tạp của danh mục đầu tư (portfolio).
- **Sản phẩm bàn giao (Deliverables):** Tỷ lệ giữa sản phẩm hoàn thành thực tế và sản phẩm dự kiến; số lần phải làm lại (reworks) do kết quả không khớp với đặc tả kỹ thuật.
- **Chi phí (Costs):** Thống kê các hạng mục chi phí thực tế.
- **Tài nguyên (Resources):** Thống kê mức độ sử dụng, tải và phân phối tài nguyên, chi phí tài nguyên.

### 4.3 Số liệu chất lượng con người (Person Quality Metrics)

- **Kinh nghiệm nhân sự (Personnel Experience):** Số năm kinh nghiệm làm việc trong lĩnh vực cụ thể của dự án.
- **Mức độ hài lòng đối với nhân viên (Degree of Satisfaction):**
  $$\text{Chỉ số hài lòng} = \frac{\text{Tổng mức độ hài lòng của từng yêu cầu}}{\text{Tổng số yêu cầu}}$$
- Đánh giá chủ quan và khả năng giao tiếp xã hội (social abilities).

---

## V. Kế hoạch Đảm bảo chất lượng (SQAP) & QA/QC

### 5.1 Kế hoạch Đảm bảo chất lượng phần mềm (Software Quality Assurance Plan — SQAP)

Tài liệu chỉ rõ các thủ tục, tiêu chuẩn và tài nguyên được áp dụng bởi ai và khi nào để đảm bảo chất lượng cho một dự án cụ thể (tuân thủ tiêu chuẩn **IEEE 730-2002**).

**Đề cương SQAP:**

1. Mục đích (Purpose)
2. Tài liệu tham khảo (Reference documents)
3. Quản lý (Management)
4. Tài liệu cần quản lý (Documentation)
5. Các tiêu chuẩn, thông lệ, quy ước và số liệu (Standards, practices, conventions, metrics)
6. Các buổi đánh giá phần mềm (Software reviews)
7. Quy trình kiểm thử (Test)
8. Báo cáo vấn đề và hành động khắc phục (Problem reporting and corrective action)
9. Công cụ, kỹ thuật và phương pháp (Tools, techniques, methodologies)
10. Kiểm soát phương tiện truyền thông (Media control)
11. Kiểm soát nhà cung cấp (Supplier control)
12. Thu thập, duy trì và lưu giữ hồ sơ (Records collection, maintenance, retention)
13. Đào tạo nhân sự (Training)
14. Quản lý rủi ro (Risk management)
15. Thuật ngữ (Glossary)
16. Lịch sử thay đổi SQAP (SQAP change history)

### 5.2 Phân biệt Đảm bảo chất lượng (QA) và Kiểm soát chất lượng (QC)

| Khía cạnh     | Đảm bảo chất lượng (Quality Assurance — QA)                                                           | Kiểm soát chất lượng (Quality Control — QC)                                                                       |
| ------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| **Tập trung** | Tập trung vào **Quy trình** (Process). Mang lại niềm tin rằng các yêu cầu chất lượng sẽ được đáp ứng. | Tập trung vào **Sản phẩm** (Product). Trực tiếp kiểm tra để đáp ứng yêu cầu chất lượng.                           |
| **Mục đích**  | **Ngăn ngừa khiếm khuyết** (Prevent defects).                                                         | **Phát hiện khiếm khuyết** (Detect defects).                                                                      |
| **Hoạt động** | Định nghĩa quy trình, lựa chọn công cụ, đào tạo nhân sự, kiểm toán quy trình.                         | Desk-checks (kiểm tra chéo), Walkthrough (hướng dẫn/rà soát), Testing (kiểm thử), Inspection (điều tra sản phẩm). |

- Các công cụ quản lý kiểm thử phổ biến: Qase.io, Testpad, Trello.

### 5.3 Mô tả công việc của Kỹ sư QA/QC (QA/QC Job Profile)

- Định nghĩa và đo lường chất lượng sản phẩm.
- Thiết lập quy trình và công cụ quản lý chất lượng trên toàn bộ tổ chức R&D.
- Phối hợp với đội Dev và QA để thực thi các thực tiễn tốt nhất đáp ứng mục tiêu chất lượng.
- Phối hợp với ban quản lý để báo cáo số liệu chất lượng và đưa ra khuyến nghị sản phẩm đã sẵn sàng phát hành hay chưa.
- Tìm kiếm cơ hội cải tiến chất lượng và hiệu quả nhóm xuyên suốt chu kỳ phát triển.
- _Yêu cầu:_ Bằng cử nhân CNTT/Kỹ thuật phần mềm; hiểu biết sâu về các công cụ và quy trình chất lượng (kiểm thử, theo dõi lỗi, whitebox/blackbox, code coverage, code complexity, code analyzers); hiểu biết về quy trình phát triển (Waterfall, Agile); kinh nghiệm làm việc với khách hàng.

### 5.4 Phân biệt Kiểm thử (Test), Đánh giá (Evaluation) và Thẩm định (Assessment)

- **Kiểm thử (Test):** Quản lý đầu vào $\rightarrow$ chạy thử $\rightarrow$ so sánh đầu ra với kỳ vọng thực tế để đo lường định tính/định lượng một thuộc tính. _(Ví dụ: Sản phẩm A đạt kiểm thử hiệu suất)._
- **Đánh giá (Evaluation):** Đưa ra phán quyết dựa trên các tiêu chí và bằng chứng thu thập được (bằng chứng có thể là kết quả test). _(Ví dụ: Sản phẩm A chạy tốt hơn Sản phẩm B)._
- **Thẩm định (Assessment):** Quy trình toàn diện thu thập thông tin, thực hiện test, thực hiện đánh giá và đưa ra kết luận chiến lược. _(Ví dụ: Sản phẩm A đáp ứng hoàn toàn nhu cầu, đề xuất sử dụng sản phẩm A cho dự án)._

---

## VI. Hệ thống quản lý chất lượng & Tiêu chuẩn ISO

### 6.1 Khái niệm QMS \[7\]

Hệ thống quản lý chất lượng (Quality Management System — QMS) là phương thức định nghĩa cách thức tổ chức đáp ứng yêu cầu của khách hàng và các bên liên quan chịu ảnh hưởng bởi hoạt động của tổ chức.

### 6.2 Hệ tiêu chuẩn ISO liên quan

- **Tổ chức Tiêu chuẩn hóa Quốc tế (ISO):** Liên đoàn toàn cầu của các cơ quan tiêu chuẩn quốc gia. Việc soạn thảo tiêu chuẩn quốc tế được thực hiện bởi các Ủy ban Kỹ thuật ISO (ISO Technical Committees).
- **ISO 9000:2008:** Quy định các thuật ngữ và định nghĩa áp dụng cho tất cả các tiêu chuẩn quản lý chất lượng và hệ thống QMS phát triển bởi ISO/TC 176.
- **ISO 9001:** Tiêu chuẩn quy định các yêu cầu đối với hệ thống QMS, giúp doanh nghiệp hoạt động hiệu quả hơn và nâng cao sự hài lòng của khách hàng dựa trên triết lý **cải tiến liên tục** (continual improvement). Tổ chức phải tự xác định mục tiêu chất lượng và cải tiến quy trình để đạt chúng.
- **ISO 19011:** Hướng dẫn thực hiện đánh giá (audits) nội bộ và bên ngoài đối với hệ thống ISO 9001, chuẩn bị cho việc chứng nhận của bên thứ ba.
- **ISO 9004:** Hướng dẫn cách thức đạt được thành công bền vững với hệ thống QMS.

### 6.3 Thuật ngữ ISO 9001:2008

- **Tài liệu (Document):** Thông tin và phương tiện hỗ trợ của nó.
- **Thủ tục (Procedure):** Cách thức cụ thể để thực hiện một hoạt động hoặc một quá trình (có thể được tài liệu hóa hoặc không).
- **Sổ tay chất lượng (Quality Manual):** Tài liệu đặc tả hệ thống QMS của tổ chức.
- **Kế hoạch chất lượng (Quality Plan):** Tài liệu chỉ rõ các thủ tục và tài nguyên liên quan sẽ do ai áp dụng và khi nào áp dụng cho một dự án, sản phẩm hoặc hợp đồng cụ thể.
- **Hồ sơ (Record):** Tài liệu nêu rõ kết quả đạt được hoặc cung cấp bằng chứng về các hoạt động được thực hiện.
- **Đặc tả kỹ thuật (Specification):** Tài liệu nêu rõ các yêu cầu.

### 6.4 14 bước triển khai Hệ thống quản lý chất lượng ISO 9001 \[8\]

1. Cam kết của lãnh đạo cao nhất (Top management commitment).
2. Thành lập đội triển khai dự án (Establish implementation team).
3. Khởi động chương trình đào tạo nhận thức về ISO 9000.
4. Cung cấp các khóa đào tạo quy trình.
5. Tiến hành khảo sát hiện trạng ban đầu (Conduct initial status survey).
6. Tạo kế hoạch triển khai bằng văn bản.
7. Xây dựng tài liệu hệ thống QMS (sử dụng ISO 10013:1995 làm hướng dẫn).
8. Thực hiện kiểm soát tài liệu (quản lý tạo mới, phê duyệt, phân phối, sửa đổi, lưu trữ, hủy bỏ tài liệu).
9. Triển khai vận hành thực tế quy trình (Implementation).
10. Đánh giá chất lượng nội bộ (Internal quality audit - theo hướng dẫn ISO 19011).
11. Tổ chức đánh giá của ban lãnh đạo (Management review).
12. Đánh giá thử nghiệm trước chứng nhận (Pre-assessment audit).
13. Đăng ký và chứng nhận chính thức (Certification and registration).
14. Thực hiện cải tiến liên tục (Continual Improvement - theo phương pháp ISO 9004:2008).

---

## Tài liệu tham khảo (References)

1. J.A. McCall et al. (1977). _Factors in Software Quality_.
2. Robert T. Futrell et al. (2002). _Quality Software Project Management_.
3. Shari Lawrence Pfleeger et al. (1997). _Status Report on Software Measurement_.
4. Stephen H. Kan. (2002). _Metrics and Models in Software Quality Engineering_.
5. G. Canfora et al. (2005). _A Family of Experiments to Validate Metrics for Software Process Models_.
6. Paul Pocatilu (2007). _IT Project Management Metrics_.
7. ISO (2008). _Guidance on the Documentation Requirements of ISO 9001_.
8. Aston. _14 Steps to Implementing ISO 9001 Quality Management System_.
