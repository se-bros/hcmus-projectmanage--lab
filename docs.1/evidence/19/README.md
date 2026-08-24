# BẰNG CHỨNG NỘP KÈM — CÂU 19: KẾ HOẠCH QUẢN LÝ CHẤT LƯỢNG (SOFTWARE QUALITY MANAGEMENT PLAN)

**Mã câu hỏi:** `CÂU-19` | **Chủ đề:** Software Quality Management Plan

## 1. Đề bài và Yêu cầu nộp kèm từ Đề thi vấn đáp

> Trình bày quá trình hình thành và phương pháp đánh giá tài liệu Kế hoạch quản lý chất lượng (Software Quality Management Plan) của nhóm. _(Sinh viên nộp kèm bản in tài liệu Kế hoạch quản lý chất lượng của nhóm, bản in Định nghĩa hoàn thành của nhóm, bản in giao diện cấu hình đảm bảo Coding Standards cho mã nguồn của nhóm, bản in biên bản thanh tra mã nguồn của nhóm, bản in biên bản phản hồi từ khách hàng của nhóm.)_

## 2. Danh mục tài liệu / bằng chứng cần nộp kèm khi thi

| STT | Tên tài liệu / Bằng chứng nộp kèm | Loại tài liệu | Tệp đính kèm tại thư mục này | Nguồn tài liệu PDF | Mô tả chi tiết |
|:---:|---|---|---|---|---|
| 1 | **Bản in tài liệu Kế hoạch quản lý chất lượng (Quality Management Plan)** | `Tài liệu in A4` | [19-quality-management-plan.pdf](./19-quality-management-plan.pdf) | [19-quality-management-plan.pdf](../../pdf/19-quality-management-plan.pdf) | Mô hình chất lượng, 6 cổng kiểm soát chất lượng (Quality Gates), tiêu chuẩn đánh giá và quy trình kiểm soát. |
| 2 | **Bản in Biên bản thanh tra mã nguồn của nhóm (Code Inspection Record PR #41)** | `Biên bản in A4` | [01_code_inspection_record_pr41.md](./01_code_inspection_record_pr41.md) | N/A | Biên bản thanh tra chính thức cho Pull Request #41 (Tối ưu hóa pipeline OCR) theo chuẩn IEEE 1028 với danh sách defect đã fix. |
| 3 | **Bản in Biên bản phản hồi từ khách hàng / UAT (UAT Feedback Record)** | `Biên bản in A4` | [02_uat_feedback_record.md](./02_uat_feedback_record.md) | N/A | Biên bản kiểm thử chấp nhận người dùng thực tế ngày 15/08/2026 với đại diện Thư viện nghiệm thu 6 kịch bản UAT. |
| 4 | **Bản in cấu hình tiêu chuẩn Coding Standards & Linter (ruff, eslint, markdownlint)** | `Tài liệu cấu hình linter` | [03_coding_standards_and_linter_config.md](./03_coding_standards_and_linter_config.md) | N/A | Cấu hình linter chuẩn: Ruff cho Python, ESLint/Prettier cho Next.js, Markdownlint cho tài liệu. |

## 3. Các bằng chứng & số liệu then chốt cần chỉ ra trên tài liệu

- 6 Quality Gates (G1 Commit → G2 Code Review → G3 CI Automation → G4 Staging Deploy → G5 UAT Acceptance → G6 Release).
- **Coding Standards tự động hóa 100% trong CI:** Không cho phép merge PR nếu vi phạm linting hoặc test failed.
- **Bằng chứng thanh tra mã nguồn PR #41:** Ghi nhận 3 defect (1 Major, 2 Minor) và bằng chứng fix.
- **Bằng chứng UAT thực tế:** Biên bản UAT có chữ ký đại diện Thư viện nghiệm thu 6/6 kịch bản.

## 4. Khung hướng dẫn trả lời vấn đáp (WHAT — HOW — WHY — EVIDENCE)

- **WHAT (Khái niệm & Nội dung):** Quy trình đảm bảo chất lượng (QA) nhằm ngăn ngừa lỗi và kiểm soát chất lượng (QC) nhằm phát hiện và loại bỏ lỗi trước khi bàn giao.
- **HOW (Quy trình thực hiện):** Thiết lập tiêu chuẩn Coding Standards & DoD → Cài đặt linter tự động trong CI → Tiến hành Code Inspection cho PR quan trọng → Thực hiện kiểm thử chấp nhận UAT với khách hàng.
- **WHY (Lý do & Giá trị):** Xây dựng chất lượng ngay từ trong quá trình phát triển (Quality at the Source) thay vì phụ thuộc vào việc tìm lỗi cuối kỳ.
- **EVIDENCE (Minh chứng chỉ tay):** Chỉ vào Bản in DoD, File cấu hình linter `03_coding_standards`, Biên bản Code Inspection PR #41 và Biên bản UAT.

## 5. Liên kết tệp nguồn và tài liệu liên quan

- [Tài liệu Kế hoạch chất lượng (docs.1/md/19-quality-management-plan.md)](../../md/19-quality-management-plan.md)
- [Phiếu ôn tập Câu 19 (final-exam/preparation/6_Team_Monitoring_Risk_Lessons/README.md)](../../../final-exam/preparation/6_Team_Monitoring_Risk_Lessons/README.md)
