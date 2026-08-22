# HỢP ĐỒNG NHÓM (TEAM CONTRACT)

## Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS (HCMUS-LDMS)

### Thông tin tài liệu

| Trường thông tin | Nội dung |
|---|---|
| Mã tài liệu | `HCMUS-LDMS-TCT` |
| Tên tài liệu | Hợp đồng nhóm |
| Đơn vị soạn thảo | Nhóm Sebros |
| Người phụ trách | Mạch Quốc Tấn — Project Manager |
| Người xem xét/phê duyệt | Toàn bộ 6 thành viên |
| Trạng thái | Chờ thành viên xác nhận |
| Phạm vi áp dụng | MVP 11 tuần |

### Lịch sử phiên bản

| Phiên bản | Ngày | Mô tả thay đổi | Người thực hiện |
|---:|:---:|---|---|
| 1.0 | 24/07/2026 | Khởi tạo Hợp đồng nhóm. | Ân Tiến Nguyên An |
| 2.0 | 22/08/2026 | Đồng bộ đường cơ sở 11 tuần, vai trò, Kanban, Trunk-Based, governance AI, biểu quyết và bằng chứng hoàn thành. | Mạch Quốc Tấn |

## Mục lục

- [1. Mục đích và hiệu lực](#1-mục-đích-và-hiệu-lực)
- [2. Thành viên và vai trò](#2-thành-viên-và-vai-trò)
- [3. Mục tiêu và nguyên tắc](#3-mục-tiêu-và-nguyên-tắc)
- [4. Phương pháp làm việc](#4-phương-pháp-làm-việc)
- [5. Giao tiếp và họp](#5-giao-tiếp-và-họp)
- [6. Quản lý mã nguồn và chất lượng](#6-quản-lý-mã-nguồn-và-chất-lượng)
- [7. Sử dụng công cụ AI](#7-sử-dụng-công-cụ-ai)
- [8. Quyết định và giải quyết bất đồng](#8-quyết-định-và-giải-quyết-bất-đồng)
- [9. Trách nhiệm và xử lý vi phạm](#9-trách-nhiệm-và-xử-lý-vi-phạm)
- [10. Sửa đổi hợp đồng](#10-sửa-đổi-hợp-đồng)
- [11. Xác nhận của thành viên](#11-xác-nhận-của-thành-viên)
- [12. Tài liệu tham chiếu](#12-tài-liệu-tham-chiếu)

---

## 1. Mục đích và hiệu lực

Hợp đồng nhóm thống nhất cách sáu thành viên phối hợp để hoàn thành MVP HCMUS-LDMS trong 11 tuần. Tài liệu quy định vai trò, luồng Kanban, giới hạn công việc đang làm, quản lý mã nguồn, chất lượng, sử dụng AI, giao tiếp, ra quyết định và xử lý vi phạm.

Tài liệu chỉ chuyển sang trạng thái **Có hiệu lực** khi tối thiểu 6/6 thành viên xác nhận tại [Mục 11](#11-xác-nhận-của-thành-viên). Trước thời điểm đó, trạng thái là **Chờ thành viên xác nhận**.

## 2. Thành viên và vai trò

### 2.1. Danh sách thống nhất

| STT | Thành viên | MSSV | Vai trò chính | Vai trò hỗ trợ |
|---:|---|---|---|---|
| 1 | Mạch Quốc Tấn | 23127115 | Project Manager; Backend | Yêu cầu, tài liệu, điều phối |
| 2 | Ân Tiến Nguyên An | 23127148 | Solution Architect; Backend Lead | Review kỹ thuật |
| 3 | Ngô Nguyễn Thế Khoa | 23127065 | Frontend Lead | UX và trình đọc |
| 4 | Nguyễn Tuấn Anh | 23127152 | Backend; DevOps | Xác thực và CI/CD |
| 5 | Nguyễn Quang Thái | 23127116 | QA; DevOps | Kiểm thử, giám sát |
| 6 | Nguyễn Lê Hồ Anh Khoa | 23127211 | Frontend | Reader và accessibility |

Mạch Quốc Tấn là Project Manager của đường cơ sở này. Nếu thay đổi PM, nhóm phải cập nhật Hợp đồng nhóm, SOW, Charter và tài liệu có liên quan trong cùng một Change Request.

### 2.2. Trách nhiệm theo vai trò

| Vai trò | Trách nhiệm | Người chịu trách nhiệm chính |
|---|---|---|
| Project Manager | Duy trì baseline, board, forecast, risk/change/evidence index và điều phối review. | Mạch Quốc Tấn |
| Solution Architect | Kiểm tra quyết định kỹ thuật, data/job/security model và review thay đổi ảnh hưởng kiến trúc. | Ân Tiến Nguyên An |
| Backend | API, persistence, OCR/EPUB, search, auth/RBAC và test backend. | Ân Tiến Nguyên An; Nguyễn Tuấn Anh; Mạch Quốc Tấn |
| Frontend | Dashboard, editor, search, reader, error/permission states và test frontend. | Ngô Nguyễn Thế Khoa; Nguyễn Lê Hồ Anh Khoa |
| QA | Test design, regression, evidence, defect triage và release readiness. | Nguyễn Quang Thái |
| DevOps | Local/demo environment, CI/CD, secrets, logs và rollback hướng dẫn. | Nguyễn Tuấn Anh; Nguyễn Quang Thái |

### 2.3. RACI theo gói công việc

| Gói | Tấn | An | Khoa Ngô | Tuấn Anh | Thái | Anh Khoa |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| Baseline, scope, tài liệu | A/R | C | C | C | C | I |
| Kiến trúc và backend lõi | C | A/R | I | R | C | I |
| Frontend và trải nghiệm đọc | I | C | A/R | I | C | R |
| OCR, EPUB và search | C | A/R | C | R | C | I |
| Kiểm thử và evidence | C | C | R | C | A/R | R |
| Triển khai local/demo | C | C | I | A/R | R | I |

Ký hiệu: R — thực hiện; A — chịu trách nhiệm cuối cùng; C — tham vấn; I — được thông báo. Mỗi gói có đúng một A.

## 3. Mục tiêu và nguyên tắc

### 3.1. Mục tiêu chung

1. Hoàn thành hoặc có ngoại lệ được phê duyệt cho 15 hạng mục Bắt buộc trong 11 tuần.
2. Mỗi hạng mục Done có thay đổi, kiểm thử, review và evidence tương ứng.
3. Không phát hành tài liệu thật khi chưa xác nhận quyền sử dụng.
4. Không hy sinh bảo mật, dữ liệu hoặc tính trung thực của bằng chứng để làm đẹp tiến độ.
5. Mỗi thành viên có đóng góp được truy vết và có thể giải thích phần việc của mình.

### 3.2. Nguyên tắc

- Hoàn thành việc đang làm trước khi kéo việc mới.
- Báo blocker sớm; không chuyển Done theo ngày dự kiến.
- Phản biện dựa trên yêu cầu, dữ liệu và thử nghiệm.
- Im lặng không được xem là phê duyệt.
- Không tự tạo số liệu, log, test result, chữ ký hoặc trạng thái hoàn thành.
- Người tạo thay đổi không phải người duy nhất quyết định thay đổi đó đạt chất lượng.

## 4. Phương pháp làm việc

### 4.1. Board Kanban thống nhất

Luồng duy nhất dùng cho dự án:

`Ý tưởng` → `Đã sẵn sàng` → `Đang thực hiện` → `Đang xem xét` → `Chờ xác nhận` → `Hoàn thành`.

| Cột | Điều kiện chính |
|---|---|
| Ý tưởng | Nhu cầu được ghi nhận nhưng chưa đủ thông tin. |
| Đã sẵn sàng | Đạt Definition of Ready, có owner/reviewer và phụ thuộc đã xử lý. |
| Đang thực hiện | Owner đang phát triển; card có ngày bắt đầu. |
| Đang xem xét | Có thay đổi để review và kiểm thử. |
| Chờ xác nhận | Kiểm tra kỹ thuật đạt; đang chờ người có trách nhiệm xác nhận nghiệp vụ/tài liệu. |
| Hoàn thành | Đạt toàn bộ Definition of Done và có evidence. |

Không tạo cột `Done – Tuần X`; tuần hoàn thành là một trường dữ liệu của card để có thể báo cáo mà không làm board tăng cột.

### 4.2. Giới hạn WIP

- Mỗi thành viên tối đa 1 card ở `Đang thực hiện`.
- Toàn nhóm tối đa 6 card ở `Đang thực hiện`.
- Toàn nhóm tối đa 4 card ở `Đang xem xét`.
- Khi chạm giới hạn, nhóm ưu tiên review, test, gỡ blocker hoặc hỗ trợ card hiện có.
- Ngoại lệ WIP phải được PM ghi lý do và thời hạn kết thúc ngoại lệ trên board.

### 4.3. Definition of Ready

Một card chỉ vào `Đã sẵn sàng` khi:

- có Story ID hoặc mã công việc;
- nêu người dùng, nhu cầu và kết quả;
- có AC kiểm thử được, gồm trường hợp lỗi/quyền khi phù hợp;
- có ưu tiên, cỡ, phụ thuộc, owner và reviewer;
- đã nhận diện dữ liệu/môi trường/evidence cần thiết;
- không còn câu hỏi có thể làm thay đổi đáng kể scope.

### 4.4. Definition of Done

Một card chỉ vào `Hoàn thành` khi:

- AC đạt hoặc có ngoại lệ được phê duyệt;
- mã/tài liệu đã được review bởi ít nhất một thành viên khác;
- kiểm thử phù hợp đã chạy và kết quả được lưu;
- không còn lỗi Critical/High chưa được chấp thuận;
- thay đổi đã tích hợp vào `main` và CI cần thiết đạt;
- tài liệu/truy vết/hướng dẫn đã cập nhật;
- có liên kết commit/PR, test evidence và người xác nhận khi cần;
- effort log đã ghi dữ liệu thực, không phải số ước đoán được trình bày như thực tế.

### 4.5. Cỡ công việc

Nhóm dùng một thang duy nhất:

| Cỡ | Effort hoàn chỉnh dự kiến | Quy tắc |
|---|---:|---|
| Nhỏ | 4–8 giờ-người | Phạm vi rõ, ít phụ thuộc. |
| Vừa | 8–16 giờ-người | Nhiều lớp hoặc cần tích hợp/test đáng kể. |
| Lớn | 16–32 giờ-người | Phải phân rã hoặc làm PoC trước khi kéo. |

Effort gồm phát triển, test, review, sửa lỗi và tài liệu để đạt DoD. Số liệu thực tế được dùng để hiệu chỉnh dải, không chia đều một phiên đa-story nếu không có timesheet riêng.

## 5. Giao tiếp và họp

### 5.1. Kênh

| Kênh | Mục đích | Mục tiêu phản hồi |
|---|---|---:|
| Nhóm chat | Điều phối nhanh, blocker, thông báo | 12 giờ |
| GitHub Issue/Project | Nhu cầu, card, quyết định và trạng thái | 24 giờ |
| Pull Request | Review code/tài liệu | 24 giờ làm việc |
| Email/biên bản | Trao đổi chính thức với bên ngoài | Theo thời hạn được thống nhất |

Mục tiêu phản hồi không đồng nghĩa tự động chấp thuận khi quá hạn.

### 5.2. Nhịp làm việc

| Hoạt động | Tần suất | Đầu ra bắt buộc |
|---|---|---|
| Cập nhật bất đồng bộ | Mỗi ngày có làm dự án | Trạng thái, việc tiếp theo, blocker. |
| Flow review | 2 lần/tuần hoặc khi có blocker cao | WIP, aging, blocked time và hành động. |
| Weekly review | Cuối tuần | Completion event, forecast, risk và thay đổi baseline. |
| Nghiệm thu nghiệp vụ | Theo mốc có deliverable | Kết quả và người xác nhận. |

Daily meeting chỉ tổ chức khi có giá trị điều phối; không bắt buộc họp để thay thế cập nhật minh bạch trên board.

## 6. Quản lý mã nguồn và chất lượng

### 6.1. Trunk-Based Development

- `main` là nhánh tích hợp và phải luôn ở trạng thái có thể kiểm tra.
- Nhánh ngắn dùng dạng `task/LDMS-xxx-mo-ta` hoặc `fix/mo-ta`.
- Không dùng `develop`, `release/*` hoặc GitFlow trong đường cơ sở này.
- Nhánh được cập nhật từ `main`, có thay đổi nhỏ, review và hợp nhất sớm.
- Không commit secret, `.env`, token, dữ liệu thật hoặc tài liệu chưa được phép.

### 6.2. Chất lượng thay đổi

- Commit có thông điệp nêu mục đích và Story ID khi áp dụng.
- Pull Request nêu phạm vi, cách kiểm tra, rủi ro và evidence.
- Người review kiểm tra AC, bảo mật, dữ liệu, test và ảnh hưởng tài liệu.
- CI phải chạy các kiểm tra có sẵn cho backend/frontend/tài liệu.
- Hotfix vẫn phải có review và regression phù hợp; khẩn cấp không phải lý do bỏ evidence.

## 7. Sử dụng công cụ AI

### 7.1. Phạm vi cho phép

AI có thể hỗ trợ phân tích, thiết kế, viết mã, test, tài liệu, review gợi ý và debug. Thành viên sử dụng AI vẫn chịu trách nhiệm về tính đúng, bản quyền, bí mật, bảo mật và khả năng giải thích kết quả.

### 7.2. Quy tắc

- Không đưa secret, dữ liệu cá nhân, tài liệu có bản quyền chưa được phép hoặc thông tin nội bộ nhạy cảm vào công cụ AI.
- Mọi mã/nội dung AI sinh phải được con người đọc, kiểm tra và review như nội dung do người viết.
- Không ghi “AI đã kiểm thử” thay cho lệnh/kết quả thực tế.
- Không bịa token, chi phí, model, phiên làm việc hoặc mức đóng góp.
- Chỉ ghi token/chi phí khi công cụ cung cấp số liệu đáng tin cậy; nếu không, ghi `Không có số đo`.
- Không dùng số token để đánh giá năng suất hoặc chất lượng cá nhân.

### 7.3. Nhật ký AI/effort

Chỉ bắt buộc ghi một dòng khi phiên AI tạo ra thay đổi hoặc quyết định đáng kể. Dòng log gồm ngày, thành viên, story, mục đích, effort thực, công cụ/model nếu biết, token nếu đo được, kết quả và liên kết evidence. Phiên hỏi đáp nhỏ không tạo artifact có thể được tổng hợp theo ngày.

## 8. Quyết định và giải quyết bất đồng

### 8.1. Ngưỡng quyết định

| Loại quyết định | Ngưỡng |
|---|---|
| Biên tập/triển khai trong story đã duyệt | Owner + reviewer |
| Kỹ thuật ảnh hưởng một module | SA + owner + reviewer; ghi rationale |
| Quy trình nội bộ không đổi baseline | Tối thiểu 4/6, PM ghi quyết định |
| Đổi PM, 15 hạng mục Bắt buộc, 11 tuần hoặc hợp đồng nhóm | 6/6 thành viên; bên ngoài nhóm phê duyệt thêm nếu SOW yêu cầu |
| Pháp lý/quyền tài liệu | Người có thẩm quyền bên ngoài nhóm; biểu quyết nhóm không thay thế |

### 8.2. Quy trình bất đồng

1. Ghi vấn đề và tiêu chí quyết định.
2. Thu thập yêu cầu, dữ liệu, PoC hoặc benchmark phù hợp.
3. So sánh lựa chọn và tác động.
4. Tìm đồng thuận; nếu không đạt, áp dụng ngưỡng ở Mục 8.1.
5. Ghi quyết định, người tham gia, ngày và điều kiện xem xét lại.

Không phản hồi không được xem là đồng ý.

## 9. Trách nhiệm và xử lý vi phạm

### 9.1. Trách nhiệm

- Cập nhật card và blocker trung thực.
- Báo sớm khi không thể hoàn thành hoặc vắng ở mốc quan trọng.
- Không mạo nhận công việc, test, chữ ký, effort hoặc số liệu.
- Bảo vệ secret và dữ liệu.
- Review với thái độ tập trung vào sản phẩm, không công kích cá nhân.

### 9.2. Xử lý

| Mức | Ví dụ | Xử lý |
|---|---|---|
| Nhẹ | Quên cập nhật card/log một lần | Nhắc và bổ sung trong ngày làm việc tiếp theo. |
| Trung bình | Lặp lại thiếu cập nhật; bỏ review/meeting quan trọng không báo | Ghi action, người hỗ trợ và thời hạn khắc phục trong weekly review. |
| Nặng | Bịa evidence/effort; làm lộ secret/dữ liệu; không hợp tác kéo dài | Tạm dừng quyền merge liên quan, báo giảng viên/người hướng dẫn và ghi đánh giá đóng góp. |

Mọi xử lý phải dựa trên bằng chứng, cho phép thành viên giải trình và tập trung khắc phục ảnh hưởng dự án.

## 10. Sửa đổi hợp đồng

- Đề xuất sửa đổi phải nêu lý do, tác động và ngày hiệu lực.
- Thay đổi nội bộ không đổi baseline cần ít nhất 4/6 thành viên.
- Thay đổi vai trò PM, mục tiêu 11 tuần, phạm vi Bắt buộc hoặc điều kiện hiệu lực cần 6/6.
- Phiên bản mới phải cập nhật lịch sử và các thành viên xác nhận lại nếu thay đổi nghĩa vụ.

## 11. Xác nhận của thành viên

| STT | Thành viên | MSSV | Hình thức xác nhận | Ngày |
|---:|---|---|---|---|
| 1 | Mạch Quốc Tấn | 23127115 |  |  |
| 2 | Ân Tiến Nguyên An | 23127148 |  |  |
| 3 | Ngô Nguyễn Thế Khoa | 23127065 |  |  |
| 4 | Nguyễn Tuấn Anh | 23127152 |  |  |
| 5 | Nguyễn Quang Thái | 23127116 |  |  |
| 6 | Nguyễn Lê Hồ Anh Khoa | 23127211 |  |  |

Khi chưa đủ 6/6 xác nhận, tài liệu không được ghi trạng thái **Có hiệu lực**.

## 12. Tài liệu tham chiếu

- [Ủy nhiệm dự án](03-project-charter.md)
- [Danh mục công việc](04-product-backlog.md)
- [Yêu cầu phần mềm](04-software-requirements.md)
- [Định nghĩa quy trình phát triển](09-software-process-definition.md)
- [Ước lượng dự án](10-project-estimate.md)
- [Bản mô tả công việc](12-statement-of-work.md)
- [Nhật ký dự án](17-project-log.md)
