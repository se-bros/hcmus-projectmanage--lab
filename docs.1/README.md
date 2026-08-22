# HỆ THỐNG QUẢN LÝ VÀ SỐ HÓA TÀI LIỆU THƯ VIỆN HCMUS

## Danh mục hồ sơ dự án HCMUS-LDMS

### Thông tin bộ hồ sơ

| Trường | Nội dung |
|---|---|
| Baseline | MVP môn học 11 tuần |
| Phạm vi | 15 Bắt buộc, 6 Nên có, 5 Có thể xem xét |
| Nhân sự | Nhóm Sebros — 6 sinh viên |
| Trạng thái | Đang rà soát/phê duyệt; xem trạng thái trong từng tài liệu |
| Nguồn nội dung | Markdown là nguồn chỉnh sửa; PDF phải được tái xuất sau mỗi thay đổi |

## Mục lục

- [1. Đường cơ sở dùng chung](#1-đường-cơ-sở-dùng-chung)
- [2. Danh sách tài liệu](#2-danh-sách-tài-liệu)
- [3. Nguồn chuẩn theo chủ đề](#3-nguồn-chuẩn-theo-chủ-đề)
- [4. Ma trận bao phủ 21 câu hỏi](#4-ma-trận-bao-phủ-21-câu-hỏi)
- [5. Quy tắc cập nhật và phát hành](#5-quy-tắc-cập-nhật-và-phát-hành)

---

## 1. Đường cơ sở dùng chung

- Phiên bản đầu tiên kéo dài 11 tuần và được quản lý theo Kanban.
- Nhóm gồm 6 sinh viên kiêm nhiệm.
- Backlog có 26 hạng mục: 15 Bắt buộc, 6 Nên có, 5 Có thể xem xét.
- Dữ liệu nghiệm thu là bộ tài liệu mẫu đã xác nhận quyền sử dụng; không cam kết số hóa 500/2.000 cuốn.
- Local dùng Docker Compose, PostgreSQL và MinIO.
- Demo cloud có thể dùng Vercel, Render, Neon và Cloudflare R2 sau khi kiểm chứng.
- Production/on-premise, ngân sách triển khai thật và vận hành dài hạn nằm ngoài baseline môn học.
- Tài liệu chưa có chữ ký/ngày/bằng chứng giữ trạng thái Chờ phê duyệt hoặc Bản dự thảo.

## 2. Danh sách tài liệu

| Câu | Markdown | PDF | Nội dung chính | Trạng thái nội dung |
|---:|---|---|---|---|
| 1 | [Đề xuất dự án](01-project-proposal.md) | [PDF](01-project-proposal.pdf) | Vấn đề, cơ hội, giải pháp, phạm vi và quyết định đề xuất. | Chờ phê duyệt |
| 2 | [Viễn cảnh và phạm vi](02-vision-and-scope.md) | [PDF](02-vision-and-scope.pdf) | Viễn cảnh, người dùng, As-Is/To-Be, phạm vi và NFR định hướng. | Chờ phê duyệt |
| 3 | [Ủy nhiệm dự án](03-project-charter.md) | [PDF](03-project-charter.pdf) | Mục tiêu, quyền hạn, vai trò, RACI, mốc và ràng buộc. | Chờ phê duyệt |
| 4 | [Yêu cầu phần mềm](04-software-requirements.md) | [PDF](04-software-requirements.pdf) | Yêu cầu chức năng/phi chức năng, dữ liệu và truy vết. | Bản dự thảo để xem xét |
| 4 | [Danh mục công việc](04-product-backlog.md) | [PDF](04-product-backlog.pdf) | 26 story, ưu tiên 15/6/5, AC, phụ thuộc và DoR/DoD. | Bản dự thảo để xem xét |
| 4 | [Hướng dẫn sử dụng](04-user-guide.md) | [PDF](04-user-guide.pdf) | Hướng dẫn theo vai trò và luồng cốt lõi. | Chờ đối chiếu giao diện thực tế |
| 5 | [Kiến trúc phần mềm](05-software-architecture.md) | [PDF](05-software-architecture.pdf) | C4, công nghệ, dữ liệu, bảo mật và profile triển khai. | Bản dự thảo để xem xét |
| 6 | [Chứng minh ý tưởng](06-proof-of-concept.md) | [PDF](06-proof-of-concept.pdf) | Hai PoC, đầu vào/đầu ra, tiêu chí và biên bản chạy. | Kế hoạch có; kết quả Chưa chạy |
| 7 | [Bản mẫu giao diện](07-prototype.md) | [PDF](07-prototype.pdf) | Luồng giao diện và kế hoạch lấy phản hồi. | Bản mẫu có; đánh giá Chưa thực hiện |
| 8 | [Nghiên cứu khả thi](08-feasibility-study.md) | [PDF](08-feasibility-study.pdf) | Khả thi có điều kiện và rủi ro. | Chờ phê duyệt |
| 9 | [Quy trình phát triển](09-software-process-definition.md) | [PDF](09-software-process-definition.pdf) | Kanban, WIP, DoR/DoD, Trunk-Based và đo lường. | Bản dự thảo để xem xét |
| 10 | [Ước lượng dự án](10-project-estimate.md) | [PDF](10-project-estimate.pdf) | Bottom-up estimate, demand 190 giờ, capacity 198 giờ và forecast. | Dự thảo để hiệu chỉnh |
| 11 | [Kế hoạch dự án](11-project-plan.md) | [PDF](11-project-plan.pdf) | WBS, lịch, phụ thuộc, nguồn lực, chi phí và kiểm soát. | Đường cơ sở chờ phê duyệt |
| 12 | [Bản mô tả công việc](12-statement-of-work.md) | [PDF](12-statement-of-work.pdf) | Scope, deliverable, schedule, cost, acceptance và change control. | Chờ phê duyệt |
| 13 | [Tích hợp liên tục](13-continuous-integration.md) | [PDF](13-continuous-integration.pdf) | GitHub Actions, backend/frontend checks và email. | Có cấu hình; thiếu run/email evidence |
| 14 | [Chuyển giao liên tục](14-continuous-delivery.md) | [PDF](14-continuous-delivery.pdf) | Môi trường, triển khai, smoke, phê duyệt và rollback. | Runbook có; chưa có workflow/evidence |
| 15 | [DevOps, vận hành và bảo mật](15-devops-and-operations.md) | [PDF](15-devops-and-operations.pdf) | Luồng DevOps, secrets, log, backup, incident và rollback. | Runbook dự thảo; Chưa xác minh |
| 16 | [Hợp đồng nhóm](16-team-contract.md) | [PDF](16-team-contract.pdf) | Vai trò, workflow, source control, AI, giao tiếp và quyết định. | Chờ 6/6 thành viên xác nhận |
| 17 | [Nhật ký dự án](17-project-log.md) | [PDF](17-project-log.pdf) | Effort, completion, evidence, flow metrics và decision log. | Đang sử dụng; lịch sử cần xác minh |
| 18 | [Kế hoạch quản lý rủi ro](18-risk-management-plan.md) | [PDF](18-risk-management-plan.pdf) | 18 rủi ro, owner, trigger, ứng phó và tồn dư. | Bản dự thảo; hành động đang theo dõi |
| 19 | [Kế hoạch quản lý chất lượng](19-quality-management-plan.md) | [PDF](19-quality-management-plan.pdf) | Thuộc tính, gate, review, chỉ số và ngoại lệ. | Bản dự thảo; gate Chưa đánh giá |
| 20 | [Kế hoạch kiểm thử](20-test-plan.md) | [PDF](20-test-plan.pdf) | Cấp test, dữ liệu, truy vết, NFR, UAT và evidence. | Kế hoạch có; kết quả Chưa chạy |
| 21 | [Sổ bài học kinh nghiệm](21-lessons-learned.md) | [PDF](21-lessons-learned.pdf) | Bài học có căn cứ và giả thuyết cần kiểm chứng. | Đang ghi nhận; chưa đóng dự án |
| Phụ lục | [Nhật ký quyết định và ADR](A1-decision-log-and-adr.md) | [PDF](A1-decision-log-and-adr.pdf) | 10 quyết định kiến trúc và điều kiện kiểm chứng. | Đường cơ sở tài liệu; chưa đủ evidence kỹ thuật |

Thứ tự 1–21 bám theo `Final-Answer.md`. Một câu có thể cần nhiều tài liệu in kèm; câu 4 gồm SRS, Backlog và Hướng dẫn sử dụng. ADR là phụ lục kiến trúc nên không chiếm số câu 13.

## 3. Nguồn chuẩn theo chủ đề

| Chủ đề | Nguồn chuẩn | Nguồn bổ trợ |
|---|---|---|
| Vấn đề và giá trị | Proposal | Vision, Feasibility |
| Scope baseline | SOW | Vision, Charter, Backlog |
| Yêu cầu | SRS | Backlog |
| Story, ưu tiên, AC | Backlog | SRS |
| Kiến trúc/môi trường | Architecture | Root README và cấu hình repository |
| Rủi ro | Risk Register | Feasibility, SOW, Operations–Security Plan |
| Quality gates/metric | Quality Plan | Process, Test/UAT Plan |
| Kế hoạch tích hợp | Project Plan | SOW, Estimate, Risk/Quality/Test Plans |
| PoC/bản mẫu | PoC, Prototype | Architecture, Backlog, Test Plan |
| CI/CD/DevOps | CI, CD, DevOps documents | Workflow/Compose và run evidence |
| Quy trình/WIP/branching | Process | Team Contract |
| Effort/capacity/forecast | Estimate | Project Log |
| Kiểm thử/UAT/evidence | Test/UAT Plan | SRS, Backlog, Quality Plan |
| Quyết định kỹ thuật | Decision Log/ADR | Architecture, Project Log |
| Vận hành/bảo mật | Operations–Security Plan | Architecture, Risk Register |
| Deliverable/acceptance | SOW | Backlog, Test/UAT Evidence Index |
| Vai trò nội bộ | Team Contract | Charter, SOW |
| Trạng thái thực tế | Board + Project Log | Git/CI/test/UAT evidence |

Khi hai nguồn mâu thuẫn, không tự chọn một nguồn. Nhóm phải ghi Change Request/decision và cập nhật đồng thời các tài liệu bị ảnh hưởng.

## 4. Ma trận bao phủ 21 câu hỏi

| Câu | Nội dung | Nguồn/evidence hiện tại | Trạng thái |
|---:|---|---|---|
| 1 | Project Proposal | `01-project-proposal.md` | Ready for review |
| 2 | Vision & Scope | `02-vision-and-scope.md` | Ready for review |
| 3 | Project Charter | `03-project-charter.md` | Pending approval |
| 4 | Requirements/Backlog | `04-software-requirements.md`, `04-product-backlog.md` | Draft baseline |
| 5 | Architecture | `05-software-architecture.md`, `assets/` | Draft baseline |
| 6 | Proof of Concept | `06-proof-of-concept.md` + Architecture/Test Plan | Kế hoạch đầy đủ; hai PoC Chưa chạy |
| 7 | Prototype | `07-prototype.md` + SVG bản mẫu | Có phác thảo; chưa có phản hồi/ảnh hệ thống thật |
| 8 | Feasibility | `08-feasibility-study.md` | Conditional |
| 9 | Process | `09-software-process-definition.md` | Draft baseline |
| 10 | Estimation | `10-project-estimate.md` | Forecast ban đầu; cần actuals |
| 11 | Project Plan | `11-project-plan.md` + SOW/Estimate/board | Đường cơ sở chờ phê duyệt và actual |
| 12 | SOW | `12-statement-of-work.md` | Pending approval |
| 13 | CI | `13-continuous-integration.md` + `.github/workflows/ci.yml` | Cấu hình có; cần run/email evidence |
| 14 | CD | `14-continuous-delivery.md` | Runbook có; chưa có workflow/deploy evidence |
| 15 | DevOps | `15-devops-and-operations.md` + Docker/monitoring config | Hồ sơ có; vận hành còn Chưa xác minh |
| 16 | Team management | `16-team-contract.md` | Pending member confirmation |
| 17 | Monitoring/control | `17-project-log.md`, board, Estimate | Historical evidence incomplete |
| 18 | Risk Plan | `18-risk-management-plan.md` + SOW + Feasibility | Đủ cấu trúc; hành động/evidence đang theo dõi |
| 19 | Quality Plan | `19-quality-management-plan.md` + Process/Team Contract | Đủ cấu trúc; gate Chưa đánh giá |
| 20 | Test Plan | `20-test-plan.md` + SRS/Backlog AC | Đủ kế hoạch/truy vết; kết quả Chưa chạy |
| 21 | Lessons Learned | `21-lessons-learned.md` + Project Log/ADR | Có bài học từ hồ sơ; chưa retrospective đóng dự án |

## 5. Quy tắc cập nhật và phát hành

1. Sửa Markdown trước; cập nhật lịch sử phiên bản nếu thay đổi nghĩa.
2. Chạy kiểm tra liên kết, fragment và Markdown lint với `docs.1/.markdownlint.json`; bộ hồ sơ tắt MD013/MD060 vì bảng PDF rộng nhưng vẫn kiểm tra các lỗi cấu trúc.
3. Tái xuất PDF tương ứng với cỡ chữ cơ bản 11pt.
4. Kiểm tra trực quan trang đầu, mục lục, bảng rộng, sơ đồ và trang chữ ký.
5. Không ghi Approved/Active/Done khi thiếu người, ngày và evidence.
6. Cập nhật README/ma trận bao phủ khi thêm, đổi tên hoặc bỏ tài liệu.
