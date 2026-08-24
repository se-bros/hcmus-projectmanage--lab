# BẰNG CHỨNG NỘP KÈM — CÂU 19: KẾ HOẠCH QUẢN LÝ CHẤT LƯỢNG (SOFTWARE QUALITY MANAGEMENT PLAN)

**Mã câu hỏi:** `CÂU-19` | **Chủ đề:** Software Quality Management Plan

## 1. Đề bài và Yêu cầu nộp kèm từ Đề thi vấn đáp

> Trình bày quá trình hình thành và phương pháp đánh giá tài liệu Kế hoạch quản lý chất lượng (Software Quality Management Plan) của nhóm. _(Sinh viên nộp kèm bản in tài liệu Kế hoạch quản lý chất lượng của nhóm, bản in định nghĩa hoàn thành (Definition of Done) của nhóm, bản in giao diện cấu hình đảm bảo Coding Standards cho mã nguồn của nhóm, bản in biên bản thanh tra mã nguồn của nhóm, bản in biên bản phản hồi từ khách hàng của nhóm.)_

## 2. Danh mục tài liệu / bằng chứng cần nộp kèm khi thi

| STT | Tên tài liệu / Bằng chứng nộp kèm                                                  | Loại tài liệu                 | Nguồn tệp Markdown                                                                                                                         | Nguồn tệp PDF / Ảnh chụp                                                       | Mô tả chi tiết                                                                                                                               |
| :-: | ---------------------------------------------------------------------------------- | ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------- |
|  1  | **Bản in tài liệu Kế hoạch quản lý chất lượng (Software Quality Management Plan)** | `Tài liệu in A4`              | [19-quality-management-plan.md](docs.1/md/19-quality-management-plan.md)                                                                   | [19-quality-management-plan.pdf](docs.1/pdf/19-quality-management-plan.pdf)    | Tài liệu định nghĩa hệ thống QA/QC, 6 Quality Gates, tiêu chuẩn chất lượng sản phẩm ISO 25010 và chỉ số đo lường.                            |
|  2  | **Bản in Định nghĩa hoàn thành (Definition of Done - DoD)**                        | `Tài liệu / Tiêu chuẩn in A4` | [ 04-product-backlog.md](docs.1/md/19-quality-management-plan.md (Mục 3) / 04-product-backlog.md)                                          | [19-quality-management-plan.pdf](docs.1/pdf/19-quality-management-plan.pdf)    | Checklist tiêu chí bắt buộc để một User Story được công nhận Done: Code clean, Unit test pass, Code Review pass, Tài liệu cập nhật, CI pass. |
|  3  | **Bản in giao diện cấu hình đảm bảo Coding Standards cho mã nguồn**                | `Tài liệu / Kịch bản linter`  | [03_coding_standards_and_linter_config.md](final-exam/preparation/6_Team_Monitoring_Risk_Lessons/03_coding_standards_and_linter_config.md) | [README.pdf](final-exam/preparation/6_Team_Monitoring_Risk_Lessons/README.pdf) | Cấu hình linter chuẩn: Ruff cho Python (`ruff.toml`), ESLint/Prettier cho Next.js, Markdownlint cho tài liệu.                                |
|  4  | **Bản in Biên bản thanh tra mã nguồn của nhóm (Code Inspection Record)**           | `Biên bản in A4`              | [01_code_inspection_record_pr41.md](final-exam/preparation/6_Team_Monitoring_Risk_Lessons/01_code_inspection_record_pr41.md)               | [README.pdf](final-exam/preparation/6_Team_Monitoring_Risk_Lessons/README.pdf) | Biên bản thanh tra chính thức cho Pull Request #41 (Tối ưu hóa pipeline OCR) theo chuẩn IEEE 1028 với checklist và danh sách defect đã fix.  |
|  5  | **Bản in Biên bản phản hồi từ khách hàng / UAT (UAT Feedback Record)**             | `Biên bản in A4`              | [02_uat_feedback_record.md](final-exam/preparation/6_Team_Monitoring_Risk_Lessons/02_uat_feedback_record.md)                               | [README.pdf](final-exam/preparation/6_Team_Monitoring_Risk_Lessons/README.pdf) | Biên bản kiểm thử chấp nhận người dùng thực tế ngày 15/08/2026 với đại diện Thư viện đánh giá 6 kịch bản UAT.                                |

## 3. Các bằng chứng & số liệu then chốt cần chỉ ra trên tài liệu

- **6 Quality Gates (G1 Commit → G2 Code Review → G3 CI Automation → G4 Staging Deploy → G5 UAT Acceptance → G6 Release).:**
- **Coding Standards tự động hóa 100% trong CI:** Không cho phép merge PR nếu vi phạm linting hoặc test failed.
- **Bằng chứng thanh tra mã nguồn PR #41:** Ghi nhận 3 defect (1 Major, 2 Minor) và bằng chứng fix.
- **Bằng chứng UAT thực tế:** Biên bản UAT có chữ ký đại diện Thư viện nghiệm thu 6/6 kịch bản.

## 4. Khung hướng dẫn trả lời vấn đáp (WHAT — HOW — WHY — EVIDENCE)

- **WHAT (Khái niệm & Nội dung):** Quy trình đảm bảo chất lượng (QA) nhằm ngăn ngừa lỗi và kiểm soát chất lượng (QC) nhằm phát hiện và loại bỏ lỗi trước khi bàn giao.
- **HOW (Quy trình thực hiện):** Thiết lập tiêu chuẩn Coding Standards & DoD → Cài đặt linter tự động trong CI → Tiến hành Code Inspection cho PR quan trọng → Thực hiện kiểm thử chấp nhận UAT với khách hàng.
- **WHY (Lý do & Giá trị):** Xây dựng chất lượng ngay từ trong quá trình phát triển (Quality at the Source) thay vì phụ thuộc vào việc tìm lỗi cuối kỳ.
- **EVIDENCE (Minh chứng chỉ tay):** Chỉ vào Bản in DoD, File cấu hình linter `03_coding_standards`, Biên bản Code Inspection PR #41 và Biên bản UAT.

## 5. Liên kết tệp nguồn và tài liệu liên quan

- [docs.1/md/19-quality-management-plan.md](../../md/19-quality-management-plan.md)
- [docs.1/pdf/19-quality-management-plan.pdf](../../pdf/19-quality-management-plan.pdf)
- [Biên bản thanh tra PR #41 (01_code_inspection_record_pr41.md)](../../../final-exam/preparation/6_Team_Monitoring_Risk_Lessons/01_code_inspection_record_pr41.md)
- [Biên bản phản hồi UAT (02_uat_feedback_record.md)](../../../final-exam/preparation/6_Team_Monitoring_Risk_Lessons/02_uat_feedback_record.md)
- [Cấu hình Coding Standards (03_coding_standards_and_linter_config.md)](../../../final-exam/preparation/6_Team_Monitoring_Risk_Lessons/03_coding_standards_and_linter_config.md)
- [Phiếu ôn tập Câu 19 (final-exam/preparation/6_Team_Monitoring_Risk_Lessons/README.md)](../../../final-exam/preparation/6_Team_Monitoring_Risk_Lessons/README.md)
