# TỔNG MỤC LỤC TÀI LIỆU DỰ ÁN HCMUS-LDMS
## Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS

> Thư mục này chứa toàn bộ hệ thống tài liệu quản lý dự án (Project Management Deliverables), kế hoạch thực thi, nhật ký phát triển với AI và tài liệu ôn tập/bảo vệ dự án cho môn học **Quản lý Dự án Phần mềm** tại **Trường Đại học Khoa học Tự nhiên - ĐHQG-HCM (HCMUS)**.

---

## Cấu trúc Tài liệu theo Vòng đời Quản lý Dự án (PM Lifecycle)

```
docs/
├── 01-initiation/                # Giai đoạn 1: Khởi tạo Dự án (WHY & WHO)
├── 02-planning/                  # Giai đoạn 2: Lập kế hoạch Dự án (WHAT & HOW & RESOURCE)
├── 03-execution-monitoring/      # Giai đoạn 3: Thực thi, Giám sát & Quản lý AI Workflow
├── 04-review-presentation/       # Giai đoạn 4: Đánh giá, Báo cáo & Thuyết trình
└── assets/                       # Sơ đồ kiến trúc, biểu đồ luồng & hình ảnh minh họa
```

---

## Bảng Tra cứu Chi tiết Tài liệu

### 1. Giai đoạn Khởi tạo Dự án (`01-initiation/`)
*Mục tiêu: Định hình bài toán thực tế, đánh giá tính khả thi, xác lập điều lệ và cam kết nhóm.*

| STT | Tài liệu | Mô tả tóm tắt | Mã tài liệu |
| :---: | :--- | :--- | :--- |
| 01 | [01-project-idea.md](file:///g:/HCMUS/NAM3-HK3/Management/Final/hcmus-projectmanage--lab/docs/01-initiation/01-project-idea.md) | Ý tưởng đề tài, bối cảnh thực trạng thư viện HCMUS và giải pháp số hóa. | `HCMUS-LDMS-01` |
| 02 | [02-project-proposal.md](file:///g:/HCMUS/NAM3-HK3/Management/Final/hcmus-projectmanage--lab/docs/01-initiation/02-project-proposal.md) | Đề xuất dự án, phân tích đối thủ cạnh tranh, lợi thế cạnh tranh (Moat). | `HCMUS-LDMS-02` |
| 03 | [03-feasibility-study.md](file:///g:/HCMUS/NAM3-HK3/Management/Final/hcmus-projectmanage--lab/docs/01-initiation/03-feasibility-study.md) | Nghiên cứu tính khả thi: Kỹ thuật, Kinh tế, Pháp lý, Vận hành, Lịch trình. | `HCMUS-LDMS-03` |
| 04 | [04-project-charter.md](file:///g:/HCMUS/NAM3-HK3/Management/Final/hcmus-projectmanage--lab/docs/01-initiation/04-project-charter.md) | Bản điều lệ dự án, phân tích Stakeholders, ma trận quyền hạn RACI. | `HCMUS-LDMS-04` |
| 05 | [05-team-contract.md](file:///g:/HCMUS/NAM3-HK3/Management/Final/hcmus-projectmanage--lab/docs/01-initiation/05-team-contract.md) | Hợp đồng làm việc nhóm, nguyên tắc phối hợp, giải quyết xung đột & KPI. | `HCMUS-LDMS-05` |

---

### 2. Giai đoạn Lập kế hoạch Dự án (`02-planning/`)
*Mục tiêu: Đặc tả chi tiết phạm vi nghiệp vụ, thiết kế kiến trúc kỹ thuật, lập backlog và ước lượng chi phí.*

| STT | Tài liệu | Mô tả tóm tắt | Mã tài liệu |
| :---: | :--- | :--- | :--- |
| 01 | [01-vision-and-scope.md](file:///g:/HCMUS/NAM3-HK3/Management/Final/hcmus-projectmanage--lab/docs/02-planning/01-vision-and-scope.md) | Tầm nhìn & Phạm vi hệ thống, so sánh quy trình thủ công vs tự động. | `HCMUS-LDMS-06` |
| 02 | [02-architecture.md](file:///g:/HCMUS/NAM3-HK3/Management/Final/hcmus-projectmanage--lab/docs/02-planning/02-architecture.md) | Kiến trúc hệ thống toàn diện, công nghệ (FastAPI, React, MinIO, OCR), PoC. | `HCMUS-LDMS-07` |
| 03 | [03-product-backlog.md](file:///g:/HCMUS/NAM3-HK3/Management/Final/hcmus-projectmanage--lab/docs/02-planning/03-product-backlog.md) | Toàn bộ 26 User Stories, Acceptance Criteria (AC) và Definition of Done (DoD). | `HCMUS-LDMS-08` |
| 04 | [04-cost-time-resource.md](file:///g:/HCMUS/NAM3-HK3/Management/Final/hcmus-projectmanage--lab/docs/02-planning/04-cost-time-resource.md) | Ước lượng chi phí (COCOMO II, AI Assisted), thời gian và nguồn lực. | `HCMUS-LDMS-09` |
| 05 | [05-statement-of-work.md](file:///g:/HCMUS/NAM3-HK3/Management/Final/hcmus-projectmanage--lab/docs/02-planning/05-statement-of-work.md) | Bản mô tả công việc (SoW) làm việc với khách hàng & đơn vị thụ hưởng. | `HCMUS-LDMS-10` |
| 09 | [09-test-plan.md](./02-planning/09-test-plan.md) | Kế hoạch kiểm thử: Pytest/Vitest, kim tự tháp, cổng CI, khoảng trống E2E/coverage. | `LDMS_TSP_B1.0` |

---

### 3. Giai đoạn Thực thi & Giám sát (`03-execution-monitoring/`)
*Mục tiêu: Phân công công việc Sprint, theo dõi tiến độ, kiểm soát token AI và ghi nhật ký phát triển.*

| STT | Tài liệu / Thư mục | Mô tả tóm tắt | Mã tài liệu |
| :---: | :--- | :--- | :--- |
| 01 | [01-sprint-plan.md](file:///g:/HCMUS/NAM3-HK3/Management/Final/hcmus-projectmanage--lab/docs/03-execution-monitoring/01-sprint-plan.md) | Kế hoạch phân công công việc Sprint 1 theo Epic cho 4 thành viên. | `HCMUS-LDMS-SPR1` |
| 02 | [02-project-log.md](file:///g:/HCMUS/NAM3-HK3/Management/Final/hcmus-projectmanage--lab/docs/03-execution-monitoring/02-project-log.md) | Nhật ký hoàn thành Story, thời gian thực tế và lượng token AI tiêu thụ. | `HCMUS-LDMS-LOG` |
| 03 | [03-ai-development-workflow.md](file:///g:/HCMUS/NAM3-HK3/Management/Final/hcmus-projectmanage--lab/docs/03-execution-monitoring/03-ai-development-workflow.md) | Báo cáo chi tiết phương pháp lập trình cùng AI Coding Assistant. | `HCMUS-LDMS-AI` |
| 06 | [06-developer-guide.md](./03-execution-monitoring/06-developer-guide.md) | Hướng dẫn cài đặt công cụ, chạy local, lệnh trùng CI cho lập trình viên. | `HCMUS-LDMS-DEVGUIDE` |
| 07 | [07-deployment-guide.md](./03-execution-monitoring/07-deployment-guide.md) | Hướng dẫn triển khai Compose prod-like, migration, backup MVP, gap CD. | `HCMUS-LDMS-DEPLOY` |
| - | [superpowers/](file:///g:/HCMUS/NAM3-HK3/Management/Final/hcmus-projectmanage--lab/docs/03-execution-monitoring/superpowers) | Thư mục chứa các bản đặc tả (specs) và kế hoạch (plans) chi tiết từng tính năng. | - |

---

### 4. Giai đoạn Đánh giá, Ôn tập & Thuyết trình (`04-review-presentation/`)
*Mục tiêu: Ôn tập kiến thức môn học, tài liệu phục vụ báo cáo bảo vệ và slide thuyết trình.*

| STT | Tài liệu / Thư mục | Mô tả tóm tắt |
| :---: | :--- | :--- |
| 01 | [01-midterm-requirement.md](file:///g:/HCMUS/NAM3-HK3/Management/Final/hcmus-projectmanage--lab/docs/04-review-presentation/01-midterm-requirement.md) | Đề cương và checklist yêu cầu báo cáo giữa kỳ môn Quản lý Dự án. |
| 02 | [02-project-evaluation-qa.md](file:///g:/HCMUS/NAM3-HK3/Management/Final/hcmus-projectmanage--lab/docs/04-review-presentation/02-project-evaluation-qa.md) | Bộ câu hỏi phản biện chi tiết và trích dẫn kiểm chứng cho toàn bộ dự án. |
| 03 | [03-lecture-notes-summary.md](file:///g:/HCMUS/NAM3-HK3/Management/Final/hcmus-projectmanage--lab/docs/04-review-presentation/03-lecture-notes-summary.md) | Tóm tắt kiến thức lý thuyết và bài học thực hành từ Buổi 2 đến Buổi 5. |
| 04 | [slide/](file:///g:/HCMUS/NAM3-HK3/Management/Final/hcmus-projectmanage--lab/docs/04-review-presentation/slide) | Bộ Slide thuyết trình tương tác xây dựng bằng framework Slidev. |

---

### 5. Thư viện Assets & Sơ đồ (`assets/`)
* [assets/images/](file:///g:/HCMUS/NAM3-HK3/Management/Final/hcmus-projectmanage--lab/docs/assets/images): Chứa các sơ đồ kiến trúc hệ thống (`.mmd`, `.svg`, `.png`), mockup giao diện và flowchart quy trình.
