# Cấu hình phần mềm (Software Configuration Management)

**Giảng viên / Lecturer:** Ngô Huy Biên (Ngo Huy Bien) — nhbien@fit.hcmus.edu.vn
**Đơn vị / Department:** Bộ môn Kỹ thuật phần mềm, Khoa Công nghệ thông tin, Trường Đại học Khoa học Tự nhiên, ĐHQG-HCM
**Môn học / Course:** Quản lý Dự án Phần mềm (Software Project Management)

---

## 1. Mục tiêu bài học (Learning Objectives)

Sau bài học, người học có thể:

- Thực hiện các hoạt động quản lý cấu hình.
  _(Perform configuration management activities.)_
- Tạo kế hoạch quản lý cấu hình.
  _(Create a configuration management plan.)_

## 2. Nội dung (Contents Overview)

| #   | Chủ đề (VI)                         | Topic (EN)                                 |
| --- | ----------------------------------- | ------------------------------------------ |
| I   | Các thuật ngữ quản lý cấu hình      | Configuration Management Terminologies     |
| II  | Các hoạt động quản lý cấu hình      | Configuration Management Activities        |
| III | Vai trò quản lý cấu hình            | Configuration Management Roles             |
| IV  | Kế hoạch quản lý cấu hình           | Configuration Management Plan              |
| V   | Giải pháp quản lý cấu hình & DevOps | Configuration Management Solution & DevOps |

---

## I. Các thuật ngữ quản lý cấu hình (Configuration Management Terminologies)

### 1.1 Quản lý cấu hình phần mềm (SCM/CM) là gì? \[1\]

> Quản lý cấu hình phần mềm là một khung tổ chức (một kỷ luật) để quản lý sự tiến hóa của các hệ thống máy tính trong suốt tất cả các giai đoạn phát triển của hệ thống.
> _(Software configuration management — SCM or CM is an organizational framework — a discipline — for managing the evolution of computer systems throughout all stages of systems development.)_

Hệ thống phần mềm rất phức tạp, để tạo một bản phát hành (release) cần quản lý nhiều thành phần: Tầm nhìn dự án, SOW, tiến độ, tài nguyên, thông số kỹ thuật, thiết kế, mã nguồn, kế hoạch kiểm thử, báo cáo kiểm thử và gói cài đặt.

### 1.2 Hạng mục cấu hình — CI (Configuration Item) \[2\]

> Hạng mục cấu hình là bất kỳ phần nào có thể có của quá trình phát triển hoặc bàn giao một hệ thống hoặc sản phẩm cần thiết để xác định, sản xuất, lưu trữ, sử dụng và thay đổi một cách riêng lẻ.
> _(A configuration item is any possible part of the development or delivery of a system or product that it's necessary to identify, produce, store, use, and change individually.)_

Các loại CI:

- **Đối tượng điện tử (Electronic Objects):** Có bản sao ở dạng điện tử hoặc vật lý, được lưu trữ dưới dạng điện tử và dễ dàng sản xuất số lượng bản sao không giới hạn.
- **Đối tượng vật lý (Physical Objects):** Khi giao một bản sao sẽ làm giảm số lượng bản sao có sẵn; không thể lưu trữ trên máy tính mà phải lưu trữ ở nơi vật lý; các công cụ CM truyền thống cần một proxy-object (đối tượng đại diện) ở dạng điện tử để xử lý đối tượng vật lý.
- **Các đối tượng khác:** Phần cứng, mạng, mô tả quy trình, thỏa thuận/hợp đồng dịch vụ, tài liệu đào tạo hoặc hướng dẫn sử dụng.

### 1.3 Đường cơ sở (Baseline) \[3\]

> Đường cơ sở là một thông số kỹ thuật hoặc sản phẩm đã được chính thức xem xét và đồng ý, sau đó làm cơ sở cho sự phát triển tiếp theo, và chỉ có thể được thay đổi thông qua các thủ tục kiểm soát thay đổi chính thức.
> _(A specification or product that has been formally reviewed and agreed upon, that thereafter serves as the basis for further development, and that can be changed only through formal change control procedures.)_

### 1.4 Phân phối bàn giao (Deliveries) \[2\]

Bàn giao là hệ thống phân cấp của các hạng mục cấu hình (CI) và có thể được xây dựng từ các lần giao hàng khác theo một cấu trúc phân nhánh.
Ví dụ: Giao nhận đặc tả yêu cầu, giao nhận liên quan đến phần cứng.

### 1.5 Cột mốc (Milestone) và Phát hành (Release)

- **Cột mốc (Milestone):** Một điểm hoặc sự kiện cụ thể với kết quả xác định dùng để theo dõi tiến độ hướng tới một mục tiêu.
- **Phát hành (Release):** Sự phân phối phiên bản đầu tiên hoặc phiên bản nâng cấp của sản phẩm phần mềm (chương trình thực thi, tài liệu, ghi chú phát hành, dữ liệu cấu hình).
  Các giai đoạn phát hành phổ biến: _Pre-Alpha, Alpha, Beta, Release Candidate (RC), Gold/RTM (Release to Manufacturing), GA (General Availability)._

---

## II. Các hoạt động quản lý cấu hình (Configuration Management Activities)

### 2.1 Xác định các hạng mục cấu hình (Identify CIs)

Các hạng mục cần đưa vào CM bao gồm:

- Sản phẩm bàn giao cho khách hàng.
- Sản phẩm công việc nội bộ được chỉ định.
- Sản phẩm mua ngoài.
- Công cụ và tài sản của môi trường làm việc dự án.
- Các hạng mục khác dùng để tạo và mô tả sản phẩm công việc.

### 2.2 Gán mã định danh duy nhất cho CIs

Quy tắc đặt mã định danh:

```text
<SYSTEM>\[<TLA>\]_\[<SUBSYSTEM>\]_\[<TLA>\]_\[R|A|B\]<X>[.<Y>.<Z>]\[.BL<#>\]
```

- **R|A|B:** Đại diện cho Release, Alpha, hoặc Beta.
- **X:** Số nguyên đại diện cho phiên bản chính (major release).
- **Y:** Số nguyên (tùy chọn) đại diện cho phiên bản phụ (minor release).
- **Z:** Số nguyên (tùy chọn) đại diện cho phiên bản thay thế (patches, ports).
- **BL:** Viết tắt của Base Level (bản phát hành nội bộ).
- Các viết tắt loại tài liệu: _PLN (Project Plans), SOW (Statement of Work), USC (Use Cases), SRD (Requirements Document), SDD (Software Design Document), SRC (Source Code), TSP (Test Plan)._

Ví dụ: `Windows_PLN_B1.0`, `Windows_IE_USC_R3.5`.

### 2.3 Quản lý đường cơ sở (Identify Baselines)

1. Xác định vai trò, trách nhiệm của người tạo và phê duyệt đường cơ sở.
2. Chọn các hạng mục cấu hình đưa vào đường cơ sở.
3. Phê duyệt và ghi lại bộ tài liệu có trong đường cơ sở.
   _(Đầu ra: Baselines & Description of baselines)_

### 2.4 Xác định mẫu phê duyệt hạng mục (Item Approval Template)

Bằng chứng xác nhận hạng mục đáp ứng tiêu chí để xếp vào quản lý cấu hình (ở dạng giấy hoặc điện tử).
Nội dung: CI liên quan, chữ ký ghi ngày (đầy đủ vai trò: nhà sản xuất, người chịu trách nhiệm, người phê duyệt), điều kiện phê duyệt, siêu dữ liệu liên quan.

### 2.5 Xác định mẫu yêu cầu thay đổi (Change Request Template)

Tài liệu yêu cầu điều chỉnh hệ thống (do công thức sai, lỗi mã hóa, lỗi test tích hợp, yêu cầu nâng cấp middleware, hoặc yêu cầu cải tiến).
Nội dung: Mã định danh thay đổi, độ ưu tiên, CI liên quan, thông tin về giai đoạn thay đổi (ngày giờ, người thực hiện, mô tả).

### 2.6 Xác định mẫu yêu cầu phát hành (Release Request Template)

Xác định những gì được phát hành từ thư viện cấu hình và cho ai.
Nội dung: CI liên quan, chữ ký của người yêu cầu, người chịu trách nhiệm, lý do yêu cầu phát hành, phương tiện phân phối và điểm đến.

### 2.7 Báo cáo trạng thái (Status Reporting)

Cung cấp thông tin dễ đọc, cần thiết để quản lý hiệu quả phát triển và bảo trì.
Các hoạt động: Liệt kê đường cơ sở, làm nổi bật các CI hiện tại và thay đổi, liệt kê danh sách thay đổi.
Mục đích: Lấy thông tin cho quyết định thay đổi, hỗ trợ lập kế hoạch tương lai, xem lại cấu hình sản phẩm và tài liệu, mã nguồn.

### 2.8 Kiểm toán cấu hình (Configuration Audits)

Xác nhận các đường cơ sở và tài liệu phù hợp với tiêu chuẩn hoặc yêu cầu đã quy định.
_(Confirm that the resulting baselines and documentation conform to a specified standard.)_

- **Kiểm toán cấu hình chức năng (FCA):** Xác minh hiệu suất thực tế của CI đáp ứng đặc tả hiệu suất. (Tránh rủi ro thiếu tính năng quan trọng khi giao hàng dẫn đến bị kiện).
- **Kiểm toán cấu hình vật lý (PCA):** Xác minh tài liệu thiết kế phù hợp với thiết kế của CI bàn giao thực tế. (Tránh rủi ro mã nguồn không khớp với file thực thi khi cần bảo trì/tái cấu trúc nhiều năm sau).
- **Hoạt động kiểm toán:** Đánh giá tính toàn vẹn của đường cơ sở, xác nhận bản ghi CM khớp với các hạng mục thực tế, kiểm tra tính đầy đủ/chính xác, xác nhận tuân thủ quy trình và theo dõi các hành động khắc phục đến khi hoàn tất.

---

## III. Vai trò quản lý cấu hình (Configuration Management Roles)

### 3.1 Quản trị viên cấu hình (Configuration Manager)

Chịu trách nhiệm triển khai, duy trì và cải tiến hoạt động quản lý cấu hình:

- Chuyển đổi nhu cầu của công ty thành các quy trình, tài nguyên và công cụ CM thực tế.
- Lựa chọn và kiểm thử công cụ CM.
- Theo dõi hiệu suất và hiệu quả của CM, lập báo cáo trạng thái cho quản lý kèm phân tích và đề xuất cải tiến.

### 3.2 Thủ thư (Librarian)

- Thiết lập thư viện quản lý cấu hình (thư viện chính được kiểm soát để lưu trữ CIs).
- Duy trì, kiểm soát nội dung và giao tiếp thông tin của thư viện cấu hình.

### 3.3 Ban kiểm soát cấu hình (Configuration Control Board — CCB)

Bao gồm các vai trò: Quản trị viên cấu hình, Quản lý dự án (Project Manager), Trưởng nhóm kỹ thuật (Technical Lead), Trưởng nhóm kiểm thử (Test Lead), Kỹ sư chất lượng (Quality Engineer), và Khách hàng liên quan.

### 3.4 Trách nhiệm của các vai trò khác đối với CM

- **Nhà phân tích (Analyst):** Xác định các CI liên quan (hợp đồng, yêu cầu); đưa chúng vào kho lưu trữ sau khi được phê duyệt; trích xuất CIs làm cơ sở cho phân tích; thực hiện phân tích dấu vết (trace analysis).
- **Kiến trúc sư (Architect):** Xác định và lưu trữ các CI tài liệu thiết kế; trích xuất đặc tả yêu cầu làm cơ sở thiết kế; kiểm tra tính dấu vết của thiết kế đối với yêu cầu.
- **Nhà phát triển (Developer):** Xác định và lưu trữ mã nguồn và file thực thi; trích xuất đặc tả yêu cầu và thiết kế làm cơ sở lập trình; kiểm tra đảm bảo mã nguồn bao phủ được thiết kế và yêu cầu.
- **Nhà tích hợp (Integrator):** Xác định kịch bản build và sản phẩm tích hợp hệ thống con; trích xuất thiết kế kiến trúc, kế hoạch phát triển/thử nghiệm làm cơ sở tích hợp.
- **Người thử nghiệm (Tester):** Xác định kế hoạch, kịch bản, dữ liệu kiểm thử và môi trường kiểm thử; trích xuất CI/hệ thống con làm cơ sở kiểm thử; theo dõi tiến độ các yêu cầu thay đổi.
- **Khách hàng (Customer):** Tham gia vào CCB, tạo các đăng ký sự kiện (lỗi/yêu cầu thay đổi), phê duyệt sản phẩm công việc bàn giao.
- **Nhà thầu phụ (Subcontractor):** Sử dụng hệ thống CM của nhà thầu chính; chuyển giao các đăng ký sự kiện hoặc yêu cầu thay đổi theo thỏa thuận hợp tác.

---

## IV. Kế hoạch quản lý cấu hình (Configuration Management Plan)

Kế hoạch CM là kế hoạch thực tế được thực hiện để giải quyết các nhu cầu CM của dự án, quy định tất cả các thủ tục, chính sách, lịch trình, trách nhiệm.
_(The CM plan is the actual plan implemented to address CM needs. It gives all procedures, policies, schedules, and responsibilities.)_

> **Phân biệt:** Kế hoạch (Plan) mô tả những gì bạn sẽ làm; Quy trình/Thủ tục (Procedure) mô tả nó được thực hiện như thế nào.
> _(A plan describes what you will do and a procedure describes how it will be done.)_

**Đề cương Kế hoạch CM mẫu (Outline of a Model CM Plan):**

- **1.0 Giới thiệu (Introduction):** Mục đích, phạm vi, định nghĩa, tài liệu tham khảo, may đo (tailoring).
- **2.0 Quản lý cấu hình phần mềm (SCM):** Tổ chức, trách nhiệm SCM, quan hệ của CM với vòng đời phát triển, giao diện và trách nhiệm CM của các tổ chức khác.
- **3.0 Hoạt động SCM:**
  - _3.1 Nhận dạng cấu hình:_ Ghi nhãn và đánh số tài liệu/file; quy tắc theo dõi; quản lý phiên bản/phát hành; quản lý cấu hình các Baseline dự án; quản lý Thư viện (sao lưu, khôi phục, xử lý thảm họa, chính sách lưu giữ).
  - _3.2 Kiểm soát cấu hình:_ Thủ tục thay đổi baseline; thủ tục xử lý yêu cầu thay đổi và phê duyệt; phân công trách nhiệm; điều lệ/vai trò của CCB; mức độ kiểm soát qua các giai đoạn; công cụ tự động.
  - _3.3 Kế toán trạng thái cấu hình (CSA):_ Bảo quản và phát hành media; các báo cáo cần lập; quy trình phát hành (release notes, hướng dẫn cài đặt, lỗi đã biết).
  - _3.4 Kiểm toán cấu hình:_ Số lượng, thời điểm, vai trò các bên và độ chính thức của các đợt kiểm toán (FCA, PCA).
- **4.0 Cột mốc CM (CM Milestones):** Các mốc baseline, đánh giá, kiểm toán liên kết với vòng đời phát triển.
- **5.0 Đào tạo (Training):** Đào tạo quy trình và sử dụng công cụ.
- **6.0 Hỗ trợ nhà thầu phụ/nhà cung cấp (Subcontractor/Vendor Support).**

---

## V. Giải pháp quản lý cấu hình & DevOps (CM Solution & DevOps)

### 5.1 Thiết lập hệ thống công cụ

| Nhóm công cụ                              | Các công cụ phổ biến                                                 |
| ----------------------------------------- | -------------------------------------------------------------------- |
| **Giao tiếp (Communication)**             | Zoom, Skype, Discord, Viber, Telegram, Gmail, Outlook, Slack         |
| **Quản lý yêu cầu (Requirements)**        | Confluence, Google Sheets                                            |
| **Theo dõi tác vụ (Task Tracking)**       | Trello, Asana, Jira/Atlassian Cloud, ClickUp                         |
| **Kiểm soát phiên bản (Version Control)** | Git, GitHub, GitLab, Apache Subversion (SVN), VisualSVN, TortoiseSVN |
| **CI/CD**                                 | GitHub Actions, GitLab CI, CircleCI, Jenkins, Xcode Cloud            |
| **Theo dõi lỗi (Bug Tracking)**           | Jira, Bugzilla, MantisBT                                             |
| **Theo dõi thời gian (Time Tracking)**    | Clockify, Toggl                                                      |
| **DevOps & Hạ tầng (Infrastructure)**     | Docker, Kubernetes, Chef, Ansible, Nagios                            |

### 5.2 Tích hợp liên tục, Phân phối liên tục và Triển khai liên tục (CI/CD)

- **Tích hợp liên tục (Continuous Integration):** Các thay đổi của lập trình viên được xác thực tự động bằng cách tạo bản dựng (build) và chạy kiểm thử (automated tests).
- **Phân phối liên tục (Continuous Delivery):** Mở rộng của CI, tự động hóa quy trình phát hành để có thể triển khai ứng dụng bất kỳ lúc nào chỉ bằng một nút bấm.
- **Triển khai liên tục (Continuous Deployment):** Mọi thay đổi vượt qua các bước kiểm thử tự động của pipeline sẽ tự động được phát hành trực tiếp đến khách hàng (không có sự can thiệp của con người).

### 5.3 Thực hành DevOps

- **Cơ sở hạ tầng dưới dạng mã (Infrastructure as Code):** Sử dụng các tập lệnh (scripts) để tự động hóa hạ tầng.
- **Bật/tắt tính năng (Feature Flags/Toggles):** Sử dụng các cài đặt cấu hình hoặc câu lệnh điều kiện (IF ELSE) trong code để dễ dàng kích hoạt hoặc vô hiệu hóa tính năng mới mà không cần deploy lại.
- **Giám sát liên tục (Continuous Monitoring).**
- **Sao lưu và Lưu trữ dữ liệu (Backup & Archiving):** Quy trình sao lưu giúp phục hồi dữ liệu khi có sự cố. Khi dự án kết thúc, cần lưu trữ dữ liệu dự án lâu dài, dọn dẹp môi trường làm việc và lưu trữ hoặc hủy tài liệu giấy theo quy định.

### 5.4 Mục tiêu của CM theo tiêu chuẩn ISO/IEC 15504 (SPICE) \[4\]

Để đạt cấp độ 2 (Level 2) trong bất kỳ quy trình nào của SPICE, tất cả sản phẩm công việc liên quan phải được đặt dưới sự quản lý cấu hình.
Mục tiêu bao gồm:

- Phát triển chiến lược CM.
- Xác định, định nghĩa và thiết lập baseline cho tất cả sản phẩm.
- Kiểm soát các thay đổi và bản phát hành.
- Ghi nhận và báo cáo trạng thái CI và yêu cầu thay đổi.
- Đảm bảo tính nhất quán, đầy đủ, bảo quản và phân phối an toàn cho các hạng mục.

---

## Tài liệu tham khảo (References)

1. Jessica Keyes (2004). _Software Configuration Management_. Auerbach Publications.
2. Anne Mette Jonassen Hass (2002). _Configuration Management Principles and Practice_. Addison-Wesley.
3. Roger S. Pressman (2010). _Software Engineering: A Practitioner's Approach_.
4. Susan A. Dart (1992). _The Past, Present, and Future of Configuration Management_.
5. Len Bass, Ingo Weber và Liming Zhu (2015). _DevOps: A Software Architect's Perspective_. Pearson Education.
6. Gene Kim et al. (2016). _The DevOps Handbook_. IT Revolution.
7. Julien Vehent (2018). _Securing DevOps_. Manning Publications.
