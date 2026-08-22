# NHẬT KÝ DỰ ÁN

## Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS (HCMUS-LDMS)

### Thông tin tài liệu

| Trường | Nội dung |
|---|---|
| Mã tài liệu | `HCMUS-LDMS-LOG` |
| Chủ sở hữu | Project Manager — Mạch Quốc Tấn |
| Trạng thái | Đang sử dụng; dữ liệu lịch sử cần xác minh evidence |
| Phạm vi | Effort log, completion log, quyết định và tổng hợp luồng |

### Lịch sử phiên bản

| Phiên bản | Ngày | Thay đổi |
|---:|:---:|---|
| 1.0 | 16/07/2026 | Khởi tạo bảng ghi các session/story. |
| 2.0 | 22/08/2026 | Tách effort khỏi completion, loại bỏ cách hiểu cộng trùng điểm là throughput và thêm yêu cầu evidence. |

## Mục lục

- [1. Quy tắc ghi nhận](#1-quy-tắc-ghi-nhận)
- [2. Effort log lịch sử](#2-effort-log-lịch-sử)
- [3. Tổng hợp dữ liệu lịch sử](#3-tổng-hợp-dữ-liệu-lịch-sử)
- [4. Completion register](#4-completion-register)
- [5. Mẫu dòng mới](#5-mẫu-dòng-mới)
- [6. Chỉ số Kanban](#6-chỉ-số-kanban)
- [7. Quyết định và thay đổi](#7-quyết-định-và-thay-đổi)

---

## 1. Quy tắc ghi nhận

### 1.1. Ba loại dữ liệu

| Loại | Mục đích | Có thể lặp Story ID? | Dùng tính throughput? |
|---|---|:---:|:---:|
| Effort log | Ghi phiên làm việc và effort thực | Có | Không |
| Completion event | Ghi lần story đạt DoD | Không, trừ khi Reopened và Done lại | Có |
| Evidence | Chứng minh AC/test/review/xác nhận | Có thể có nhiều | Không trực tiếp |

### 1.2. Nguyên tắc

- Không cộng điểm của cùng một story nhiều lần để báo completed scope.
- Dòng đa-story chỉ ghi tổng effort của session; không chia đều nếu không có timesheet riêng.
- Chỉ ghi `Done` khi đạt Definition of Done trong [Hợp đồng nhóm](16-team-contract.md).
- Mỗi completion event phải có commit/PR, test evidence, reviewer và ngày Done.
- Token/model chỉ ghi khi có số đo; nếu không có, ghi `Không có số đo`.
- Token không được dùng thay cho effort hoặc chất lượng.
- Placeholder, prototype hoặc partial implementation không được ghi là story hoàn thành nếu AC chưa đạt.

## 2. Effort log lịch sử

Các dòng dưới đây được bảo toàn từ nhật ký trước. Trường “phân bổ theo story” trước đây là giả định chia đều; phiên bản 2.0 không dùng giả định đó làm actual effort của từng story.

| Ngày | Thành viên | Story ID | Mô tả session | Effort session | Token được ghi | Công cụ/model được ghi | Tình trạng evidence |
|---|---|---|---|---:|---:|---|---|
| 16/07/2026 | Khoa Nguyễn | LDMS-008, 026 | Reader/Search placeholder và danh sách tài liệu | 2 giờ | 40K | Claude Sonnet 5; Claude Opus 4.8 | Chưa liên kết đủ PR/test/DoD trong nhật ký |
| 16/07/2026 | Khoa Ngô | LDMS-003, 004, 007 | OCR, kết quả theo trang và tạo EPUB | 45 phút | 140K | Không ghi rõ theo từng story | Chưa liên kết đủ PR/test/DoD trong nhật ký |
| 16/07/2026 | Thái | LDMS-013, 022 | Điều kiện xuất bản và retry tác vụ | 45 phút | 140K | Không ghi rõ theo từng story | Chưa liên kết đủ PR/test/DoD trong nhật ký |
| 17/07/2026 | Tuấn Anh | LDMS-001, 009, 010, 018 | Nền tảng, định danh, phân quyền và Google login | 1 giờ 20 phút | 120K | Claude Sonnet 5 | Chưa liên kết đủ PR/test/DoD trong nhật ký |
| 22/07/2026 | Tuấn Anh | LDMS-001, 009, 010, 018 | Local auth, RBAC, profile, role request và email domain | 2 giờ | 150K | Claude Sonnet 5 | Chưa liên kết đủ PR/test/DoD trong nhật ký |
| 18/07/2026 | Khoa Nguyễn | LDMS-008, 014, 015, 016, 019, 020, 026 | Trải nghiệm tìm kiếm và đọc | 6 giờ | 100K | Claude Sonnet 5; Claude Opus 4.8 | Chưa liên kết đủ PR/test/DoD trong nhật ký |
| 13/08/2026 | Khoa Nguyễn | LDMS-021 | Đánh dấu và ghi chú | 2 giờ | 40K | Claude Opus 5 | Có lịch sử Git liên quan; vẫn cần gắn test/DoD vào completion event |

## 3. Tổng hợp dữ liệu lịch sử

| Chỉ số | Giá trị | Cách hiểu đúng |
|---|---:|---|
| Số session đã ghi | 7 | Bảy dòng effort, không phải bảy story. |
| Tổng effort session | 14 giờ 50 phút | Tổng theo dòng, có thể gồm partial/rework. |
| Tổng token được ghi | 730K | Số liệu lịch sử chưa có nguồn đo/session ID kèm theo. |
| Tổng điểm theo cách cộng cũ | 37 | Không dùng làm completed points vì có story lặp. |
| Story ID duy nhất được nhắc | 17 | Không đồng nghĩa 17 story Done. |
| Completion event đủ evidence | 0 trong phiên bản nhật ký cũ | Phải tái xác minh từ Git/test/UAT. |

Danh sách 17 Story ID duy nhất đã được nhắc:

`LDMS-001`, `LDMS-003`, `LDMS-004`, `LDMS-007`, `LDMS-008`, `LDMS-009`, `LDMS-010`, `LDMS-013`, `LDMS-014`, `LDMS-015`, `LDMS-016`, `LDMS-018`, `LDMS-019`, `LDMS-020`, `LDMS-021`, `LDMS-022`, `LDMS-026`.

## 4. Completion register

Completion register không suy diễn Done từ effort log. Nhóm phải xác minh từng story bằng repository và tiêu chí hiện hành.

| Story | Mức độ | Trạng thái xác minh | Evidence cần bổ sung | Người xác nhận |
|---|---|---|---|---|
| LDMS-001 | Bắt buộc | Chưa xác minh DoD | PR/commit, hướng dẫn chạy, smoke result | PM + reviewer |
| LDMS-003 | Bắt buộc | Chưa xác minh DoD | OCR tests, job state/restart evidence | Backend + QA |
| LDMS-004 | Bắt buộc | Chưa xác minh DoD | Page mapping/preview tests | Frontend/Backend + QA |
| LDMS-007 | Bắt buộc | Chưa xác minh DoD | EPUB validation và failure test | Backend + QA |
| LDMS-008 | Bắt buộc | Chưa xác minh DoD | Reader AC, permission và responsive evidence | Frontend + QA |
| LDMS-009 | Bắt buộc | Chưa xác minh DoD | Auth tests và error cases | Backend + QA |
| LDMS-010 | Bắt buộc | Chưa xác minh DoD | Role matrix và negative authorization tests | Backend + QA |
| LDMS-013 | Bắt buộc | Chưa xác minh DoD | Publish gate tests | Backend + QA |
| LDMS-014 | Bắt buộc | Chưa xác minh DoD | Private access/expired URL/negative tests | Backend + QA |
| LDMS-015 | Bắt buộc | Chưa xác minh DoD | FTS dataset và permission-filtered results | Backend + QA |
| LDMS-016 | Bắt buộc | Chưa xác minh DoD | Result UI, empty/error states | Frontend + QA |
| LDMS-018 | Nên có | Chưa xác minh DoD | OAuth config/test và error evidence | Backend + QA |
| LDMS-019 | Có thể xem xét | Chưa xác minh DoD | AC riêng nếu được bổ sung scope | Frontend + nghiệp vụ |
| LDMS-020 | Có thể xem xét | Chưa xác minh DoD | Persistence/privacy tests nếu bổ sung scope | Frontend/Backend + QA |
| LDMS-021 | Có thể xem xét | Chưa xác minh DoD | PR, tests, privacy/delete behavior và quyết định scope | Frontend + QA |
| LDMS-022 | Nên có | Chưa xác minh DoD | Retry/error tests | Backend + QA |
| LDMS-026 | Bắt buộc | Chưa xác minh DoD | List/status/permission tests | Frontend/Backend + QA |

Các story Bắt buộc chưa xuất hiện trong effort log cũ (`LDMS-002`, `LDMS-005`, `LDMS-011`) vẫn phải được quản lý trên board và ghi completion event khi đạt DoD.

## 5. Mẫu dòng mới

### 5.1. Effort log

| Ngày | Thành viên | Story | Hoạt động | Effort thực | Blocked/Rework | AI/model | Token/chi phí | Evidence |
|---|---|---|---|---:|---:|---|---|---|
| Chưa có dữ liệu mới | Chưa ghi nhận | Chưa ghi nhận | Chưa ghi nhận | Chưa ghi nhận | Chưa ghi nhận | Chưa ghi nhận | Chưa ghi nhận | Chưa ghi nhận |

### 5.2. Completion event

| Done date | Story | Owner | Reviewer | PR/commit | Test evidence | Nghiệp vụ | Actual effort | Ghi chú |
|---|---|---|---|---|---|---|---:|---|
| Chưa có completion event được tái xác minh |  |  |  |  |  |  |  |  |

## 6. Chỉ số Kanban

Chỉ tính từ completion event đã xác minh:

| Tuần | Story Done duy nhất | Điểm Done | Cycle time P50/P85 | Blocked time | Rework | Ghi chú |
|---|---:|---:|---|---:|---:|---|
| Chưa có dữ liệu đủ điều kiện | 0 | 0 | Chưa tính | Chưa tính | Chưa tính | Không suy từ effort log cũ. |

Forecast chỉ được cập nhật khi có ít nhất ba completion event đủ evidence hoặc dữ liệu ba tuần có chất lượng phù hợp.

## 7. Quyết định và thay đổi

| Ngày | Mã | Quyết định | Lý do | Người quyết định | Tài liệu ảnh hưởng |
|---|---|---|---|---|---|
| 22/08/2026 | DEC-001 | Dùng baseline 11 tuần, 15 Bắt buộc, 6 Nên có, 5 Có thể xem xét cho bộ hồ sơ cập nhật. | Đồng bộ phần lớn tài liệu mới và loại bỏ đường cơ sở SOW 20 tuần. | Đề xuất để nhóm/bên liên quan xác nhận | SOW, Team Contract, Estimate, Process, README |
| 22/08/2026 | DEC-002 | Tách effort log khỏi completion log. | Tránh cộng trùng story và dùng dữ liệu thiếu evidence làm throughput. | Project Manager | Project Log, Estimate |

Các quyết định trên là quyết định cập nhật hồ sơ của nhóm; nội dung cần phê duyệt bên ngoài vẫn giữ trạng thái chờ xác nhận.

Quyết định kỹ thuật có alternatives, consequences và verification conditions được quản lý trong [Nhật ký quyết định và ADR](A1-decision-log-and-adr.md). Project Log chỉ ghi event và liên kết ADR/Change Request tương ứng, không sao chép lịch sử quyết định theo cách có thể gây lệch phiên bản.
