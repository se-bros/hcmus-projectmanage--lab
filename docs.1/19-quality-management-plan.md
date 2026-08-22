# KẾ HOẠCH QUẢN LÝ CHẤT LƯỢNG

## Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS (HCMUS-LDMS)

### Thông tin tài liệu

| Trường | Nội dung |
|---|---|
| Mã tài liệu | `HCMUS-LDMS-QMP` |
| Chủ sở hữu | QA Lead — Nguyễn Quang Thái |
| Chịu trách nhiệm cuối | Project Manager — Mạch Quốc Tấn |
| Phiên bản | 1.0 — 22/08/2026 |
| Trạng thái | Bản dự thảo để xem xét; gate chưa chạy giữ `Chưa đánh giá` |
| Phạm vi | Sản phẩm, quy trình, tài liệu và evidence của MVP 11 tuần |

## Mục lục

- [1. Mục tiêu và nguyên tắc](#1-mục-tiêu-và-nguyên-tắc)
- [2. Thuộc tính chất lượng](#2-thuộc-tính-chất-lượng)
- [3. Quality Gates](#3-quality-gates)
- [4. Tiêu chuẩn review](#4-tiêu-chuẩn-review)
- [5. Kiểm thử và quản lý lỗi](#5-kiểm-thử-và-quản-lý-lỗi)
- [6. Chất lượng tài liệu và truy vết](#6-chất-lượng-tài-liệu-và-truy-vết)
- [7. Chỉ số và báo cáo](#7-chỉ-số-và-báo-cáo)
- [8. Ngoại lệ và cải tiến](#8-ngoại-lệ-và-cải-tiến)
- [9. RACI và truy vết](#9-raci-và-truy-vết)

## 1. Mục tiêu và nguyên tắc

Chất lượng của HCMUS-LDMS được hiểu là khả năng đáp ứng đúng yêu cầu, bảo toàn dữ liệu, kiểm soát quyền, phục hồi được khi lỗi, dùng được trong luồng nghiệp vụ và có bằng chứng truy vết. Mục tiêu không phải tạo nhiều artifact mà là ngăn kết quả chưa kiểm chứng đi qua gate.

- Quality được xây vào từng card, không để đến tuần 11.
- Người tạo không phải là người duy nhất xác nhận thay đổi của mình.
- Automation được ưu tiên cho kiểm tra lặp lại; manual/UAT dùng cho trải nghiệm và nghiệp vụ.
- Coverage phần trăm không thay thế test case đúng rủi ro; chưa có baseline coverage nên không đặt số đạt giả.
- Mọi metric phải ghi nguồn, thời gian và cách tính.
- Không hạ severity để đạt release gate; ngoại lệ cần người có thẩm quyền.

## 2. Thuộc tính chất lượng

| Thuộc tính | Mục tiêu MVP | Cách chứng minh |
|---|---|---|
| Functional suitability | 15 story Bắt buộc đạt AC hoặc có ngoại lệ được duyệt | Story test + UAT + trace |
| Security/privacy | Server-side authorization, private objects, không lộ secrets | Negative tests, scan, review |
| Reliability/integrity | Lỗi/retry/restart không làm mất source hoặc save gần nhất | Failure/recovery/integrity tests |
| Performance | UI không bị block bởi job; search được đo đúng phương pháp | Job/UI test, raw performance result |
| Usability/accessibility | Trạng thái/lỗi rõ; core flow dùng bàn phím và viewport mục tiêu | Checklist + UAT |
| Maintainability | Module rõ, setup tái lập, thay đổi được review/test | Architecture review, clean setup |
| Portability/deployability | Local chạy từ repo; demo cloud có smoke riêng | Setup/smoke evidence |
| Traceability | Requirement→Story→Change→Test→UAT | Evidence audit |

## 3. Quality Gates

### 3.1. Gate theo card

| Gate | Điều kiện bắt buộc | Người xác nhận | Trạng thái hiện tại |
|---|---|---|---|
| G0 — Idea→Ready | AC, priority, size, dependency, data, owner/reviewer và NFR rõ | PM + QA/Technical Lead | Chưa đánh giá |
| G1 — Ready→Doing | WIP còn chỗ; blocker chính xử lý; test approach biết trước | Owner + PM | Chưa đánh giá |
| G2 — Doing→Review | Thay đổi hoàn chỉnh; self-test; doc/config cập nhật; không có secret | Owner | Chưa đánh giá |
| G3 — Review→Waiting | Review đạt; test phù hợp đạt; defect được phân loại; evidence mở được | Reviewer + QA | Chưa đánh giá |
| G4 — Waiting→Done | AC đạt; nghiệp vụ xác nhận khi cần; completion event đủ trường | PM + QA + nghiệp vụ khi áp dụng | Chưa đánh giá |

### 3.2. Gate theo mốc

| Mốc | Điều kiện | Quyết định có thể đưa ra |
|---|---|---|
| Tuần 3 — Architecture/PoC | ADR chính có owner; PoC plan; risk rất cao có response | Continue / Rework / Reduce scope |
| Tuần 7 — Core flow | Happy path core tích hợp; evidence không đứt; forecast cập nhật | Continue / Swarm / Scope control |
| Tuần 9 — Feature complete mục tiêu | 15 Must không còn gap không owner; UAT/data/matrix chốt | Enter system test / Delay |
| Tuần 10 — Release candidate | System/security/recovery test; Critical/High triage | Enter UAT / Reject RC |
| Tuần 11 — Release/UAT | SOW acceptance, evidence audit, UAT decision, runbook | Accept / Accept with exception / Reject |

Không có gate nào được xem là đạt tại thời điểm lập kế hoạch nếu chưa có record đánh giá.

## 4. Tiêu chuẩn review

### 4.1. Code/Configuration Review

- Liên kết đúng Story/Requirement và mô tả tác động.
- Validation, error path và authorization được xử lý phía server khi cần.
- Không có credential, dữ liệu thật hoặc log nhạy cảm trong Git/UI.
- Migration/config thay đổi có backward/rollback consideration.
- Job/retry không ghi đè source và có idempotency phù hợp.
- Test mới/sửa bao phủ hành vi thay đổi và thất bại trọng yếu.
- Thay đổi nhỏ, dễ đọc; tên/module/API phù hợp ADR.
- Reviewer độc lập ghi kết luận; comment nghiêm trọng được giải quyết.

### 4.2. Architecture Review

- Không tạo thành phần ngoài scope khi chưa có ADR/CR.
- Xem tác động security, data consistency, recovery, operations và cost.
- Quyết định có alternatives, consequences và verification conditions.
- Interface/state/data owner rõ; failure mode được mô tả.

### 4.3. Document Review

- Baseline 11 tuần, scope 15/6/5, vai trò và môi trường không mâu thuẫn.
- ID và liên kết mở được; bảng/TOC/PDF đồng bộ.
- Trạng thái Approved/Done/Pass chỉ có khi có evidence.
- Metric có nguồn/phương pháp; giả định và giới hạn được ghi rõ.
- Markdown là nguồn chỉnh sửa; PDF 11pt được tái xuất sau thay đổi.

## 5. Kiểm thử và quản lý lỗi

Chiến lược chi tiết nằm trong [Kế hoạch kiểm thử và UAT](20-test-plan.md). Quality Plan đặt các quy tắc release:

| Mức lỗi | Ví dụ | Gate |
|---|---|---|
| Critical | Mất source, lộ tài liệu hàng loạt, core unavailable | Chặn RC/UAT/release |
| High | Bypass quyền, story Must hỏng, publish sai | Chặn trừ ngoại lệ đúng thẩm quyền |
| Medium | Hành vi cục bộ có workaround | Có owner, target, impact và quyết định |
| Low | Trình bày/tiện ích không ảnh hưởng AC | Có thể đưa backlog |

Mỗi defect có ID, build, environment, data, steps, expected, actual, severity, owner, state, fix link và retest evidence. `Cannot Reproduce` phải ghi môi trường/lần thử, không dùng để đóng thiếu căn cứ.

## 6. Chất lượng tài liệu và truy vết

### 6.1. Traceability gate

Mỗi story Done phải liên kết:

`Requirement ID → Story ID → PR/commit → Test/Evidence ID → Reviewer → UAT/Acceptance (khi cần) → Completion event`.

Nếu một liên kết không áp dụng, phải ghi lý do. Không dùng token, số commit hoặc effort làm bằng chứng AC đạt.

### 6.2. Document release checklist

- [ ] Markdown lint đạt theo cấu hình dự án.
- [ ] Không có liên kết nội bộ hỏng.
- [ ] TOC và heading phản ánh nội dung.
- [ ] PDF tương ứng mới hơn hoặc cùng thời điểm nguồn Markdown.
- [ ] PDF có text layer, tiếng Việt và bảng đọc được.
- [ ] Sơ đồ là SVG vector, nhãn không chồng lấn.
- [ ] Version/status/history được cập nhật.
- [ ] Không có claim Pass/Approved/Done thiếu nguồn.

Checklist trên là tiêu chí; dấu chưa chọn không có nghĩa lỗi đã xảy ra, mà là chưa có release record cho lần phát hành cụ thể.

## 7. Chỉ số và báo cáo

| Chỉ số | Nguồn | Cách tính | Ngưỡng hành động |
|---|---|---|---|
| Gate pass rate | Gate records | Gate đạt / gate được đánh giá | Bất kỳ Must card thất bại G3/G4 phải xử lý |
| Requirement coverage | Trace matrix | Must requirements có evidence / tổng Must | Phải 100% hoặc có ngoại lệ trước accept |
| Test status | Test report | Pass/Fail/Blocked/Chưa chạy theo build | Critical/High Fail chặn release |
| Defect escape | UAT/post-Done defect | Lỗi phát hiện sau G4 | Mọi Critical/High kích hoạt RCA |
| Rework | Board/effort | Effort sửa do lỗi/yêu cầu sai | Tăng liên tiếp hai review cần cải tiến |
| Cycle/blocked time | Completion/board | Theo quy tắc Process | Card già/blocker vượt ngưỡng nhóm chốt cần swarm |
| Evidence completeness | Evidence audit | Event đủ trường / event được audit | Bất kỳ event thiếu trường bị trả khỏi Done |

Hiện chưa có dữ liệu đủ để điền các chỉ số trên. Báo cáo phải giữ `Chưa có dữ liệu` thay vì 0 nếu chưa đo.

## 8. Ngoại lệ và cải tiến

Ngoại lệ chất lượng ghi `QEX-NN`, gate/requirement bị ảnh hưởng, lý do, risk ID, workaround, thời hạn, người chấp nhận và điều kiện đóng. Ngoại lệ không được dùng để hợp thức hóa vi phạm quyền hoặc che mất dữ liệu.

Sau mỗi mốc, nhóm chọn tối đa hai cải tiến dựa trên defect/rework/blocker/evidence. Mỗi cải tiến có giả thuyết, owner, thay đổi, chỉ số quan sát và ngày đánh giá. Nếu không có dữ liệu chứng minh hiệu quả, không tuyên bố cải tiến đã thành công.

## 9. RACI và truy vết

| Hoạt động | R | A | C |
|---|---|---|---|
| Duy trì Quality Plan/gates | QA Lead | PM | Technical Leads |
| Code review | Reviewer kỹ thuật | Technical Lead | QA |
| Architecture review | Solution Architect | Solution Architect | PM, QA/DevOps |
| Test/evidence audit | QA | QA Lead | Developer, PM |
| UAT/release decision | QA + nghiệp vụ | Đại diện nghiệp vụ/PM theo phạm vi | Nhóm |

Nguồn liên quan: [SRS](04-software-requirements.md), [Backlog](04-product-backlog.md), [Architecture](05-software-architecture.md), [Risk Register](18-risk-management-plan.md), [Process](09-software-process-definition.md), [Test/UAT Plan](20-test-plan.md), [SOW](12-statement-of-work.md) và [Operations–Security Plan](15-devops-and-operations.md).
