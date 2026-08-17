# TÓM TẮT ĐỀ THI VẤN ĐÁP — QUẢN LÝ DỰ ÁN PHẦN MỀM

## Môn học: Quản lý Dự án Phần mềm (Software Project Management)

**Giảng viên:** TS. Ngô Huy Biên — Năm học 2026

---

## TỔNG QUAN ĐỀ THI

- **Hình thức thi:** Vấn đáp cá nhân 1-1 với Giảng viên (kèm giấy viết A4 và bản in tài liệu/giao diện liên quan).
- **Quy mô đề thi:** **21 câu hỏi lớn** bao quát toàn bộ vòng đời quản lý dự án phần mềm từ Khởi tạo, Lập kế hoạch, Ước lượng, Thực thi, CI/CD, Quản trị nhân sự đến Đánh giá chất lượng và Rút ra bài học kinh nghiệm.
- **Thời gian chuẩn bị tại phòng thi:** 10 phút viết ra giấy A4 + 2 phút chọn bản in nộp kèm.
- **Thời gian vấn đáp:** 5 – 10 phút giải thích và trả lời chất vấn của Giảng viên.
- **Thang điểm:** 0 – 10 điểm (Đổi đề bị trừ 2 điểm/lần, tối đa đổi 2 lần).

---

## MA TRẬN PHÂN LOẠI 21 CÂU HỎI THEO 5 NHÓM CHUYÊN MÔN

```
                                  21 CÂU HỎI VẤN ĐÁP
                                          │
    ┌────────────────┬────────────────────┼───────────────────┬────────────────┐
    ▼                ▼                    ▼                   ▼                ▼
[Nhóm 1: Khởi tạo] [Nhóm 2: Yêu cầu]   [Nhóm 3: Kỹ thuật]  [Nhóm 4: Lập lịch] [Nhóm 5: Quản trị]
Câu 1, 3, 8      Câu 2, 4, 12         Câu 5, 6, 7         Câu 9, 10, 11      Câu 13–21
(Proposal,       (Vision, Backlog,    (Architecture,      (Process, UCP,     (CI/CD, Team,
Charter, Feas.)  SoW Scope)           PoC, Prototype)     COCOMO, Plan WBS)  Risk, Quality, Lessons)
```

---

## BẢNG TỔNG HỢP CHI TIẾT 21 CÂU HỎI & BẢN IN NỘP KÈM

|  Câu   | Chủ đề câu hỏi                                    | Nội dung trọng tâm                                                                                | Bản in nộp kèm từ Repo HCMUS-LDMS                                                                                                 |
| :----: | :------------------------------------------------ | :------------------------------------------------------------------------------------------------ | :-------------------------------------------------------------------------------------------------------------------------------- |
| **01** | **Đề xuất dự án (Project Proposal)**              | Lý do đầu tư, đối chuẩn đối thủ, phân tích Stakeholders, phương pháp đánh giá đề xuất với AI.     | In [`docs/01-initiation/02-project-proposal.md`](../docs/01-initiation/02-project-proposal.md) (Mục 2 & 3).                       |
| **02** | **Viễn cảnh & Phạm vi (Vision & Scope)**          | Quy trình As-Is vs To-Be, so sánh với giải pháp có sẵn, phạm vi MVP vs mở rộng.                   | In [`docs/02-planning/01-vision-and-scope.md`](../docs/02-planning/01-vision-and-scope.md) (Mục 2 & 3).                           |
| **03** | **Ủy nhiệm dự án (Project Charter)**              | Mục tiêu SMART, quyền hạn PM, ma trận RACI Stakeholders, ngân sách trần 100M.                     | In [`docs/01-initiation/04-project-charter.md`](../docs/01-initiation/04-project-charter.md) (Mục 3, 5 & 6).                      |
| **04** | **Yêu cầu phần mềm (Product Backlog)**            | Cấu trúc Epic/User Story, Acceptance Criteria (AC), Definition of Done (DoD), MoSCoW.             | In [`docs/02-planning/03-product-backlog.md`](../docs/02-planning/03-product-backlog.md) (Mục 1.1, 1.2 & 2).                      |
| **05** | **Kiến trúc phần mềm (Software Architecture)**    | Tech stack (FastAPI, React, MinIO, Postgres FTS, OCR), 4+1 Views, bảo mật Signed URL DRM.         | In [`docs/02-planning/02-architecture.md`](../docs/02-planning/02-architecture.md) (Sơ đồ kiến trúc & Mục 3).                     |
| **06** | **Chứng minh ý tưởng (Proof of Concept - PoC)**   | PoC Pipeline OCR tiếng Việt với Tesseract & Pandoc EPUB, PoC giải bài toán khó nhất.              | In [`docs/02-planning/02-architecture.md`](../docs/02-planning/02-architecture.md) (Mục 5 & 6).                                   |
| **07** | **Bản mẫu (Prototype)**                           | Thiết kế UI/UX Editor Split-screen đối soát song song ảnh scan, Reader EPUB reflowable.           | In ảnh chụp giao diện `/documents/:id` (Editor) và `/reader` (Reader).                                                            |
| **08** | **Báo cáo tính khả thi (Feasibility Study)**      | 5 khía cạnh khả thi: Kỹ thuật, Kinh tế (18.5M/100M), Vận hành, Pháp lý bản quyền, Lịch trình.     | In [`docs/01-initiation/03-feasibility-study.md`](../docs/01-initiation/03-feasibility-study.md).                                 |
| **09** | **Định nghĩa quy trình phát triển (Process)**     | Mô hình Agile/Kanban Spec-Driven theo Epic, WIP Limit = 1, gating review PR.                      | In [`docs/02-planning/03-product-backlog.md`](../docs/02-planning/03-product-backlog.md) (Mục 1.1) & Sprint Plan.                 |
| **10** | **Ước lượng dự án (Project Estimate)**            | Top-Down (Use Case Points - AUCP 126 điểm) và Bottom-Up (COCOMO II 10.4 PM, 3.5 KLOC).            | In [`docs/02-planning/04-cost-time-resource.md`](../docs/02-planning/04-cost-time-resource.md) (Mục 2 & 3).                       |
| **11** | **Kế hoạch dự án (Project Plan)**                 | Phân rã WBS (6 Work Packages), lộ trình 4 giai đoạn, đường găng WP4 (Số hóa).                     | In [`docs/03-execution-monitoring/01-sprint-plan.md`](../docs/03-execution-monitoring/01-sprint-plan.md) & WBS Chart.             |
| **12** | **Phát biểu công việc (Statement of Work - SoW)** | Ràng buộc Scope–Feature–Resource, ngân sách thống nhất, cơ chế quản lý thay đổi CR.               | In [`docs/02-planning/05-statement-of-work.md`](../docs/02-planning/05-statement-of-work.md) (Mục 3, 7 & 10).                     |
| **13** | **Tích hợp liên tục (Continuous Integration)**    | Luồng GitFlow (`feature/*` → `develop` → `main`), linting (ruff, eslint), automated test pytest.  | In Sơ đồ GitFlow & file cấu hình CI / test script trong repo.                                                                     |
| **14** | **Chuyển giao liên tục (Continuous Delivery)**    | Đóng gói Docker Compose production profile (`prod`), reverse proxy Nginx TLS 1.3, release tag.    | In Sơ đồ CD & file `docker-compose.yml` (`nginx` prod profile).                                                                   |
| **15** | **Mô hình DevOps**                                | Vòng lặp DevOps (Code → Test → Package → Deploy → Monitor), MinIO Console, pg_dump backup.        | In Sơ đồ công cụ DevOps & script backup (`scripts/backup-*.sh`).                                                                  |
| **16** | **Quản lý con người & Phát triển nhóm**           | Triết lý Lý thuyết Y (Douglas McGregor), 5 giai đoạn Tuckman, văn hóa tự giác & tôn trọng.        | In [`docs/01-initiation/05-team-contract.md`](../docs/01-initiation/05-team-contract.md) (Mục 8: Theory Y).                       |
| **17** | **Phân công, theo dõi & kiểm soát công việc**     | Nhật ký hoàn thành Story, đo lường 730K token AI, theo dõi throughput, xử lý blocker.             | In [`docs/03-execution-monitoring/02-project-log.md`](../docs/03-execution-monitoring/02-project-log.md) & Sprint Plan.           |
| **18** | **Quản lý rủi ro (Risk Management Plan)**         | Ma trận xác suất / tác động (P×I), rủi ro bản quyền, rủi ro OCR tiếng Việt, phương án giảm thiểu. | In Mục Quản lý Rủi ro trong Feasibility Study & Statement of Work.                                                                |
| **19** | **Quản lý chất lượng (Quality Management Plan)**  | Tiêu chuẩn DoD 5 mục, QA/QC, test coverage, chỉ số chất lượng OCR (CER < 5%).                     | In Quy tắc DoD trong Backlog & Bảng chất lượng trong SoW.                                                                         |
| **20** | **Kế hoạch kiểm thử (Test Plan)**                 | Unit test API (pytest), Integration test, Component UI test, Smoke test curl commands.            | In Bộ test cases mẫu & kết quả chạy `pytest` backend.                                                                             |
| **21** | **Bài học kinh nghiệm (Lessons Learned)**         | Bài học về Prompt Spec-driven, quản lý token AI, tối ưu hóa tech stack, cải tiến quy trình.       | In [`docs/03-execution-monitoring/03-ai-development-workflow.md`](../docs/03-execution-monitoring/03-ai-development-workflow.md). |

---

## 4 CÂU HỎI VÀNG CẦN TRẢ LỜI CHO MỌI CÂU HỎI VẤN ĐÁP

Giảng viên sẽ đánh giá dựa trên khả năng trả lời gãy gọn 4 khía cạnh cốt lõi:

1. **WHAT (Khái niệm & Định nghĩa):** Đây là tài liệu / quy trình / mô hình gì? Có cấu trúc ra sao?
2. **HOW (Cách làm & Các bước thực hiện):** Nhóm đã thực hiện những bước nào để tạo ra sản phẩm này? Công cụ và kỹ thuật nào đã dùng?
3. **WHY (Lý do & Giá trị mang lại):** Tại sao nhóm lại chọn cách này thay vì cách khác? Thuận lợi và thách thức là gì?
4. **EVIDENCE & NUMBERS (Minh chứng & Số liệu thực tế):** Chỉ rõ số liệu, biểu đồ, bảng biểu hoặc dẫn chứng cụ thể trong dự án HCMUS-LDMS để chứng minh (không nói lý thuyết suông).
