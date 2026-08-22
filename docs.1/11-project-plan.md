# KẾ HOẠCH DỰ ÁN

## Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS (HCMUS-LDMS)

### Thông tin tài liệu

| Trường | Nội dung |
|---|---|
| Mã tài liệu | `HCMUS-LDMS-PLAN` |
| Chủ sở hữu | Project Manager — Mạch Quốc Tấn |
| Người xem xét | Nhóm Sebros và Đại diện nghiệp vụ Thư viện |
| Phiên bản | 1.0 — 22/08/2026 |
| Trạng thái | Bản kế hoạch cơ sở chờ phê duyệt; actual được cập nhật từ board/Project Log |
| Thời gian | 11 tuần |

## Mục lục

- [1. Mục tiêu và đường cơ sở](#1-mục-tiêu-và-đường-cơ-sở)
- [2. Phân rã công việc](#2-phân-rã-công-việc)
- [3. Lịch, phụ thuộc và mốc](#3-lịch-phụ-thuộc-và-mốc)
- [4. Nguồn lực và phân công](#4-nguồn-lực-và-phân-công)
- [5. Công sức, chi phí và dự phòng](#5-công-sức-chi-phí-và-dự-phòng)
- [6. Kế hoạch chất lượng và kiểm thử](#6-kế-hoạch-chất-lượng-và-kiểm-thử)
- [7. Rủi ro, truyền thông và thay đổi](#7-rủi-ro-truyền-thông-và-thay-đổi)
- [8. Theo dõi và báo cáo](#8-theo-dõi-và-báo-cáo)
- [9. Điều kiện hoàn thành và phê duyệt](#9-điều-kiện-hoàn-thành-và-phê-duyệt)

## 1. Mục tiêu và đường cơ sở

Mục tiêu là bàn giao MVP trình diễn có kiểm soát cho luồng tải tài liệu → OCR → hiệu chỉnh → EPUB → xuất bản → tìm kiếm → đọc trong 11 tuần. Phạm vi có 15 hạng mục Bắt buộc, 6 Nên có và 5 Có thể xem xét; chỉ 15 Bắt buộc thuộc cam kết cơ sở.

| Yếu tố | Đường cơ sở |
|---|---|
| Phạm vi | 15 story Bắt buộc; dữ liệu mẫu có quyền |
| Thời gian | 11 tuần |
| Nhân sự | 6 sinh viên kiêm nhiệm |
| Công sức | Nhu cầu 190 giờ-người; năng lực hữu dụng 198 giờ-người |
| Dự phòng | 8 giờ-người, mức thấp; scope creep phải được chặn |
| Tiền mặt | Giả định 0 VNĐ cho môn học nếu dùng tài nguyên sẵn có |
| Cách làm | Kanban sáu cột, giới hạn WIP, Trunk-Based |
| Môi trường | Local là nguồn phát triển; demo cloud có điều kiện sau smoke test |

## 2. Phân rã công việc

| Gói | Nội dung | Story/deliverable chính | Owner |
|---|---|---|---|
| WP-01 Quản trị | Baseline, board, risk/change/status và phối hợp | Charter, Plan, SOW, logs | PM |
| WP-02 Yêu cầu/UX | SRS, backlog, AC, bản mẫu, phản hồi | SRS, Backlog, Prototype | PM/Frontend/QA |
| WP-03 Nền tảng/quyền | Setup, đăng nhập, phiên, RBAC | LDMS-001, 009, 010 | Backend/DevOps |
| WP-04 Tiếp nhận/OCR | Upload, source, job, kết quả trang | LDMS-002, 003, 004 | Backend/Architect |
| WP-05 Hiệu chỉnh/metadata | Save text, metadata, danh sách | LDMS-005, 011, 026 | Backend/Frontend |
| WP-06 Xuất bản/đọc | EPUB, gate, reader, quyền đọc | LDMS-007, 013, 008, 014 | Backend/Frontend/QA |
| WP-07 Tìm kiếm | Full-text search và kết quả | LDMS-015, 016 | Backend/Frontend |
| WP-08 Chất lượng | Review, test, evidence, UAT | Quality/Test Plan, reports | QA |
| WP-09 Triển khai/bàn giao | Local/demo, hướng dẫn, backup/rollback | CI/CD/DevOps docs, release | DevOps/PM |

Gói không thay thế story. Mỗi card vẫn phải có AC, owner, reviewer, estimate, dependency và evidence.

## 3. Lịch, phụ thuộc và mốc

### 3.1. Kế hoạch 11 tuần

| Tuần | Mục tiêu | Đầu ra dự kiến | Gate/mốc |
|---:|---|---|---|
| 1 | Khởi động và khóa mục tiêu | Charter/Plan/SOW draft, vai trò, dataset request | M1 Baseline review |
| 2 | Yêu cầu, backlog, bản mẫu | SRS, AC, Prototype, test/risk draft | G0 readiness |
| 3 | Kiến trúc và PoC | ADR, PoC runs nếu môi trường sẵn sàng, setup | M2 Architecture/PoC |
| 4 | Nền tảng, auth, upload | LDMS-001, 009, 010, 002 ở luồng review | Integration đầu |
| 5 | OCR và kết quả | LDMS-003, 004; job states | Core processing |
| 6 | Hiệu chỉnh và metadata | LDMS-005, 011, 026 | Core content |
| 7 | EPUB, gate và reader | LDMS-007, 013, 008, 014 | M3 Core flow |
| 8 | Tìm kiếm và tích hợp | LDMS-015, 016; flow đầu cuối | Feature integration |
| 9 | Hoàn thiện và đóng gap | Regression, data, docs, cloud smoke | M4 Feature complete mục tiêu |
| 10 | System/security/recovery test | Release candidate, defect triage | M5 Enter UAT decision |
| 11 | UAT và bàn giao | UAT, evidence index, hướng dẫn, lessons | M6 Acceptance/closeout |

Đây là forecast theo baseline, không phải khẳng định các đầu ra đã hoàn thành. Actual lấy từ completion event đủ evidence.

### 3.2. Phụ thuộc và đường găng dự kiến

Chuỗi có khả năng quyết định mốc là:

`Setup/Auth → Upload → OCR → Hiệu chỉnh → Metadata/Publish gate → EPUB → Reader/Search → System test → UAT`.

| Phụ thuộc | Tác động nếu trễ | Hành động |
|---|---|---|
| Dataset/quyền trước PoC/UAT | Không thể chứng minh OCR/nghiệp vụ | PM chốt owner trước tuần 2; chỉ dùng mẫu có quyền |
| Upload/source trước OCR | Chặn WP-04 | Ưu tiên vertical slice nhỏ |
| Corrected text/metadata trước EPUB/publish | Chặn WP-06 | Làm contract và dữ liệu mẫu sớm |
| RBAC trước search/reader security | Không thể nghiệm thu quyền | Negative tests từ lúc có endpoint |
| Evidence trước Done/UAT | Không thể báo hoàn thành | G3/G4 trả card nếu thiếu evidence |

Đường găng chỉ là giả thuyết kế hoạch vì chưa có actual duration/dependency đầy đủ. PM cập nhật khi có ít nhất ba completion event đủ evidence.

## 4. Nguồn lực và phân công

| Thành viên | Vai trò chính | Gói ưu tiên |
|---|---|---|
| Mạch Quốc Tấn | PM; Backend | WP-01, WP-02, hỗ trợ WP-03/04 |
| Ân Tiến Nguyên An | Solution Architect; Backend Lead | WP-03, WP-04, WP-06 |
| Ngô Nguyễn Thế Khoa | Frontend Lead | WP-02, WP-05, WP-07 |
| Nguyễn Tuấn Anh | Backend; DevOps | WP-03, WP-04, WP-09 |
| Nguyễn Quang Thái | QA; DevOps | WP-08, WP-09 |
| Nguyễn Lê Hồ Anh Khoa | Frontend | WP-05, WP-06, accessibility |

Giới hạn: tối đa 1 card Đang thực hiện mỗi người; 6 card toàn nhóm ở Đang thực hiện; 4 card ở Đang xem xét. Việc review/QA không được dồn hết cuối lịch.

## 5. Công sức, chi phí và dự phòng

| Thành phần | Giá trị | Nguồn/cách dùng |
|---|---:|---|
| 15 story Bắt buộc | 190 giờ-người | Bottom-up Estimate |
| Năng lực danh nghĩa | 264 giờ-người | 6 × 4 giờ/tuần × 11 tuần |
| Năng lực hữu dụng | 198 giờ-người | 75% sau overhead |
| Dự phòng còn lại | 8 giờ-người | Không đủ hấp thụ scope tùy chọn lớn |

Chi phí tiền mặt baseline là 0 VNĐ nếu dùng thiết bị/tài nguyên/gói sẵn có. Phí cloud, AI, thiết bị số hóa hoặc production phải có Change Request và nguồn phê duyệt; không tự quy đổi effort sinh viên thành lương cam kết.

## 6. Kế hoạch chất lượng và kiểm thử

- [Kế hoạch chất lượng](19-quality-management-plan.md) định nghĩa G0–G4, review, metric và ngoại lệ.
- [Kế hoạch kiểm thử](20-test-plan.md) định nghĩa dataset, test matrix, NFR, UAT và evidence.
- Story Done phải có Requirement → Story → Change → Test → Reviewer → UAT khi cần.
- Critical/High chưa xử lý chặn release, trừ ngoại lệ đúng thẩm quyền.
- PoC và Prototype không thay System Test/UAT.

## 7. Rủi ro, truyền thông và thay đổi

### 7.1. Rủi ro

[Kế hoạch rủi ro](18-risk-management-plan.md) là nguồn chuẩn. R-01, R-04, R-05, R-06, R-07 và R-12 cần được xem tại mọi mốc chính.

### 7.2. Truyền thông

| Nhịp | Người tham gia | Nội dung | Đầu ra |
|---|---|---|---|
| Cập nhật ngắn 2–3 lần/tuần | Nhóm | WIP, blocker, việc tiếp theo | Board/log cập nhật |
| Rà soát tuần | PM, leads, QA | Scope, forecast, risk, quality | Status note/decision |
| Review nghiệp vụ theo mốc | PM, QA, nghiệp vụ | AC, prototype, demo/UAT | Phản hồi/xác nhận |
| Incident/change | Owner liên quan | Tác động và quyết định | Incident/CR/ADR |

### 7.3. Thay đổi

Mọi thay đổi baseline có mã CR, nguồn, lý do, tác động phạm vi–effort–lịch–quality–risk–operations, lựa chọn, người quyết định và tài liệu bị ảnh hưởng. Không thêm story tùy chọn vào WIP khi core chưa ổn định.

## 8. Theo dõi và báo cáo

| Chỉ số | Nguồn | Quy tắc |
|---|---|---|
| WIP/blocked/age | Kanban board | Dùng phát hiện bottleneck, không xếp hạng cá nhân |
| Throughput/cycle time | Completion event | Chỉ tính story Done đủ evidence |
| Actual effort/rework | Effort log | Không chia đều session đa-story nếu thiếu timesheet |
| Scope/forecast | Backlog + Estimate | Cập nhật khi actual đủ tin cậy hoặc CR thay đổi scope |
| Defect/test/evidence | Test/Quality records | Không đổi Chưa chạy thành Đạt |
| Risk/action | Risk Register | Owner cập nhật trigger, action và residual risk |

Báo cáo tình trạng nêu: kỳ báo cáo, baseline, Done đã xác minh, WIP/blocker, milestone, forecast, risk/issue, test/defect, quyết định cần thiết và bằng chứng. Hiện Project Log chưa có completion event đủ evidence nên không tạo burndown giả.

## 9. Điều kiện hoàn thành và phê duyệt

Dự án chỉ đạt baseline khi 15 story Bắt buộc Done hoặc có ngoại lệ được duyệt; core flow chạy trên dataset mẫu; quyền, integrity và recovery đạt; Critical/High = 0 chưa xử lý; UAT có quyết định; tài liệu/bàn giao đồng bộ.

| Vai trò | Người | Trạng thái |
|---|---|---|
| Project Manager | Mạch Quốc Tấn | Chờ xác nhận baseline |
| Đại diện nhóm Sebros | Chưa ghi người ký riêng | Chờ xác nhận |
| Đại diện nghiệp vụ Thư viện | Chưa chỉ định bằng tên | Chờ phê duyệt |

Tài liệu tham chiếu: [Charter](03-project-charter.md), [Backlog](04-product-backlog.md), [Estimate](10-project-estimate.md), [SOW](12-statement-of-work.md), [Team Contract](16-team-contract.md) và [Project Log](17-project-log.md).
