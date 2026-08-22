# SỔ BÀI HỌC KINH NGHIỆM

## Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS (HCMUS-LDMS)

### Thông tin tài liệu

| Trường | Nội dung |
|---|---|
| Mã tài liệu | `HCMUS-LDMS-LLR` |
| Chủ sở hữu | Project Manager — Mạch Quốc Tấn |
| Phiên bản | 1.0 — 22/08/2026 |
| Trạng thái | Đang ghi nhận; chưa phải báo cáo đóng dự án |
| Nguồn | Rà soát hồ sơ, Project Log, Risk/Decision records và cấu hình repository |

## Mục lục

- [1. Mục đích và nguyên tắc](#1-mục-đích-và-nguyên-tắc)
- [2. Bài học đã có căn cứ](#2-bài-học-đã-có-căn-cứ)
- [3. Bài học cần kiểm chứng thêm](#3-bài-học-cần-kiểm-chứng-thêm)
- [4. Cách áp dụng](#4-cách-áp-dụng)
- [5. Quy trình tổng kết cuối dự án](#5-quy-trình-tổng-kết-cuối-dự-án)
- [6. Mẫu bổ sung bài học](#6-mẫu-bổ-sung-bài-học)

## 1. Mục đích và nguyên tắc

Sổ bài học ghi điều đã xảy ra, nguyên nhân, tác động và khuyến nghị có thể tái sử dụng. Nó không phải danh sách lời khuyên chung. Bài học chỉ được ghi `Đã kiểm chứng` khi có nguồn; nhận định chưa có dữ liệu giữ trạng thái `Cần kiểm chứng`.

Không dùng tài liệu này để quy lỗi cá nhân. Bài học tập trung vào hệ thống làm việc, quyết định, giao tiếp, chất lượng và rủi ro.

## 2. Bài học đã có căn cứ

| ID | Quan sát có căn cứ | Bài học | Hành động áp dụng | Nguồn |
|---|---|---|---|---|
| LL-01 | Hai đường cơ sở 11/20 tuần và 15/16 Must từng cùng tồn tại | SOW/Plan phải là nguồn chuẩn và thay đổi cần cập nhật đồng thời | Source-of-truth matrix + Change Request | Báo cáo đánh giá, lịch sử tài liệu |
| LL-02 | Effort log lặp Story ID từng bị hiểu như completed points | Effort không phải completion; throughput chỉ tính event đạt DoD | Tách Effort/Completion/Evidence | Project Log v2.0 |
| LL-03 | Chữ ký/trạng thái phê duyệt không có evidence gây rủi ro hồ sơ | Im lặng hoặc ô ký trống không phải chấp thuận | Giữ Chờ phê duyệt đến khi có người/ngày | Charter, SOW, Team Contract |
| LL-04 | Demand 190 giờ gần capacity 198 giờ | Buffer 8 giờ không chịu được scope creep đáng kể | Khóa 15 Must; cấm kéo tùy chọn sớm | Estimate, Risk R-05 |
| LL-05 | Local Docker/MinIO và demo cloud từng bị mô tả như một môi trường | Mỗi profile cần mục đích và evidence riêng | Tách local/demo/production | Architecture, ADR-006 |
| LL-06 | CI hiện có trigger nhánh kiểu cũ trong khi quy trình chọn Trunk-Based | Cấu hình thực tế phải được audit cùng tài liệu quy trình | Quyết định giữ/bỏ trigger và ghi evidence | `.github/workflows/ci.yml`, CI doc |
| LL-07 | PDF có thể lỗi thời sau khi Markdown sửa | Markdown là nguồn; PDF phải tái xuất và kiểm tra text/link/visual | Quy tắc phát hành 11pt và kiểm tra tự động | README, pipeline tài liệu |
| LL-08 | NFR định tính dễ bị diễn giải thành đã đạt | Mọi claim hiệu năng/OCR/recovery cần dataset, phương pháp và raw result | Test Plan giữ trạng thái Chưa chạy | SRS, Test Plan |
| LL-09 | Risk được nhắc rải rác nhưng thiếu owner/trigger | Risk register vận hành cần owner, trigger, contingency và residual risk | Dùng Risk ID trong Plan/SOW/Status | Risk Plan |
| LL-10 | Prototype, PoC và sản phẩm dễ bị đánh đồng | Mỗi artifact trả lời câu hỏi khác và có evidence khác | Tách Prototype, PoC, Test/UAT | Prototype và PoC docs |

## 3. Bài học cần kiểm chứng thêm

| Giả thuyết | Dữ liệu cần có | Khi đánh giá |
|---|---|---|
| WIP 1/người giảm thời gian chu kỳ | Board history, cycle/blocked time | Sau ít nhất ba completion event |
| Modular monolith phù hợp capacity | Rework, module coupling, deploy/test effort | Mốc tuần 7 và đóng dự án |
| PostgreSQL full-text search đủ cho MVP | DS-07 và P50/P95/search correctness | Trước UAT |
| Job cùng backend đủ cho demo | Restart/timeout/concurrency PoC | PoC-01 |
| Bản mẫu giảm rework giao diện | Feedback và change history | Sau prototype review |

Các giả thuyết này chưa phải bài học thành công/thất bại cho đến khi có dữ liệu.

## 4. Cách áp dụng

- PM dùng LL-01/03/04 trong baseline/change/status review.
- QA dùng LL-02/08/10 để audit Done, evidence và test state.
- Architect/DevOps dùng LL-05/06/09 cho môi trường, CI/CD, risk và ADR.
- Toàn nhóm dùng LL-07 trước mỗi lần phát hành tài liệu.
- Mỗi hành động phải có owner/ngày trong board hoặc tài liệu nguồn; sổ bài học không thay task.

## 5. Quy trình tổng kết cuối dự án

1. Thu nguồn: Plan so với actual, completion/effort, test/defect, risk/incident, UAT và stakeholder feedback.
2. Mỗi thành viên nêu điều hiệu quả, không hiệu quả, nguyên nhân và đề xuất.
3. Tách sự kiện khỏi suy đoán; xác nhận nguồn và mức tin cậy.
4. Chọn bài học có khả năng tái sử dụng; gán category, owner và hành động.
5. Đại diện nhóm review; cập nhật trạng thái tài liệu thành Báo cáo đóng dự án khi đủ căn cứ.

## 6. Mẫu bổ sung bài học

| Trường | Nội dung |
|---|---|
| Mã/ngày | `LL-NN`, thời điểm ghi |
| Bối cảnh/sự kiện | Điều thực sự xảy ra |
| Tác động | Scope, schedule, quality, people, risk hoặc operations |
| Nguyên nhân | Nguyên nhân có evidence; ghi mức tin cậy |
| Bài học | Điều nên lặp lại hoặc thay đổi |
| Hành động/owner/ngày | Cách áp dụng cụ thể |
| Nguồn | Link log, PR, test, UAT, risk, incident hoặc feedback |
| Trạng thái | Cần kiểm chứng / Đã kiểm chứng / Đã áp dụng |

Tài liệu liên quan: [Project Plan](11-project-plan.md), [Project Log](17-project-log.md), [Risk Plan](18-risk-management-plan.md), [Quality Plan](19-quality-management-plan.md), [Test Plan](20-test-plan.md) và [ADR](A1-decision-log-and-adr.md).
