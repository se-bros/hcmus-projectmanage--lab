# BẰNG CHỨNG NỘP KÈM — CÂU 20: KẾ HOẠCH KIỂM THỬ (TEST PLAN)

**Mã câu hỏi:** `CÂU-20` | **Chủ đề:** Software Test Plan

## 1. Đề bài và Yêu cầu nộp kèm từ Đề thi vấn đáp

> Trình bày quá trình hình thành và phương pháp đánh giá tài liệu Kế hoạch kiểm thử (Test Plan) của nhóm. _(Sinh viên nộp kèm bản in tài liệu Kế hoạch kiểm thử của nhóm, bản in giao diện cấu hình đảm bảo Coding Standards cho mã nguồn của nhóm, bản in giao diện hệ thống quản lý lỗi với dữ liệu thực tế của nhóm, bản in giao diện kết quả chạy mã nguồn kiểm thử đơn vị (Unit Tests) của nhóm, bản in biên bản thanh tra mã nguồn của nhóm, bản in báo cáo kết quả kiểm thử của nhóm, bản in biên bản phản hồi của khách hàng của nhóm.)_

## 2. Danh mục tài liệu / bằng chứng cần nộp kèm khi thi

| STT | Tên tài liệu / Bằng chứng nộp kèm                                                            | Loại tài liệu                      | Nguồn tệp Markdown                                                                                                                         | Nguồn tệp PDF / Ảnh chụp                                                       | Mô tả chi tiết                                                                                                                                |
| :-: | -------------------------------------------------------------------------------------------- | ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------- |
|  1  | **Bản in tài liệu Kế hoạch kiểm thử (Test Plan)**                                            | `Tài liệu in A4`                   | [20-test-plan.md](docs.1/md/20-test-plan.md)                                                                                               | [20-test-plan.pdf](docs.1/pdf/20-test-plan.pdf)                                | Chiến lược kiểm thử đa tầng (Unit, Integration, Security, Performance, UAT), ma trận truy vết yêu cầu - ca kiểm thử (RTM) và môi trường test. |
|  2  | **Bản in giao diện cấu hình đảm bảo Coding Standards cho mã nguồn**                          | `Tài liệu / Cấu hình linter`       | [03_coding_standards_and_linter_config.md](final-exam/preparation/6_Team_Monitoring_Risk_Lessons/03_coding_standards_and_linter_config.md) | [README.pdf](final-exam/preparation/6_Team_Monitoring_Risk_Lessons/README.pdf) | Cấu hình linter `ruff.toml` và `.eslintrc.json` đảm bảo kiểm soát cú pháp và chuẩn code.                                                      |
|  3  | **Bản in giao diện hệ thống quản lý lỗi với dữ liệu thực tế (Bug Tracking / GitHub Issues)** | `Ảnh chụp màn hình Bug Tracker`    | [](final-exam/preparation/5_CICD_DevOps_Testing/printouts/Q20/)                                                                            | [README.pdf](final-exam/preparation/5_CICD_DevOps_Testing/README.pdf)          | Ảnh chụp GitHub Issues với các bug thực tế được gắn nhãn `bug`, `severity: high/medium`, `status: closed/resolved` kèm commit fix.            |
|  4  | **Bản in giao diện kết quả chạy mã nguồn Unit Tests (Pytest / Vitest Report)**               | `Ảnh chụp màn hình Test Execution` | [](final-exam/preparation/5_CICD_DevOps_Testing/printouts/Q20/)                                                                            | [README.pdf](final-exam/preparation/5_CICD_DevOps_Testing/README.pdf)          | Ảnh chụp màn hình console chạy Pytest backend và Vitest frontend với 100% tests pass và báo cáo code coverage.                                |
|  5  | **Bản in Biên bản thanh tra mã nguồn của nhóm (Code Inspection Record)**                     | `Biên bản in A4`                   | [01_code_inspection_record_pr41.md](final-exam/preparation/6_Team_Monitoring_Risk_Lessons/01_code_inspection_record_pr41.md)               | [README.pdf](final-exam/preparation/6_Team_Monitoring_Risk_Lessons/README.pdf) | Biên bản thanh tra PR #41.                                                                                                                    |
|  6  | **Bản in Báo cáo kết quả kiểm thử (Test Execution Summary Report)**                          | `Báo cáo in A4`                    | [20-test-plan.md (Mục Báo cáo kết quả)](docs.1/md/20-test-plan.md "Mục Báo cáo kết quả")                                                   | [20-test-plan.pdf](docs.1/pdf/20-test-plan.pdf)                                | Tổng hợp kết quả kiểm thử: Tổng test cases, số lượng pass/fail, độ bao phủ coverage và tình trạng đóng defect.                                |
|  7  | **Bản in Biên bản phản hồi của khách hàng (UAT Feedback Record)**                            | `Biên bản in A4`                   | [02_uat_feedback_record.md](final-exam/preparation/6_Team_Monitoring_Risk_Lessons/02_uat_feedback_record.md)                               | [README.pdf](final-exam/preparation/6_Team_Monitoring_Risk_Lessons/README.pdf) | Biên bản UAT nghiệm thu người dùng.                                                                                                           |

## 3. Các bằng chứng & số liệu then chốt cần chỉ ra trên tài liệu

- **Chiến lược kiểm thử Test Pyramid:** Unit Test (Pytest/Vitest) chiếm 70% → Integration Test 20% → E2E/UAT 10%.
- **Ma trận truy vết (RTM):** 100% của 15 Must stories đều có ít nhất 2 Test Cases tương ứng.
- **Bằng chứng chạy test:** Pytest backend pass 100%, code coverage đạt > 80%.
- **Hệ thống quản lý lỗi:** Quy trình Issue Lifecycle trên GitHub (Triage → In Progress → In Review → Verified & Closed).

## 4. Khung hướng dẫn trả lời vấn đáp (WHAT — HOW — WHY — EVIDENCE)

- **WHAT (Khái niệm & Nội dung):** Tài liệu chi tiết hóa phạm vi, phương pháp, nguồn lực và lịch trình của các hoạt động kiểm thử nhằm xác minh phần mềm đáp ứng đúng yêu cầu.
- **HOW (Quy trình thực hiện):** Phân tích yêu cầu từ SRS/Backlog → Thiết kế Test Cases & RTM → Viết mã nguồn Unit/Integration test tự động → Chạy test trong CI → Ghi nhận và theo dõi lỗi qua GitHub Issues → Thực hiện UAT.
- **WHY (Lý do & Giá trị):** Đảm bảo chất lượng phần mềm không có lỗi nghiêm trọng trước khi bàn giao cho người dùng cuối.
- **EVIDENCE (Minh chứng chỉ tay):** Chỉ vào Bản in Test Plan, Ảnh chụp màn hình Pytest Report, GitHub Issues Bug Tracker và Biên bản UAT.

## 5. Liên kết tệp nguồn và tài liệu liên quan

- [docs.1/md/20-test-plan.md](../../md/20-test-plan.md)
- [docs.1/pdf/20-test-plan.pdf](../../pdf/20-test-plan.pdf)
- [Phiếu ôn tập Câu 20 (final-exam/preparation/5_CICD_DevOps_Testing/README.md)](../../../final-exam/preparation/5_CICD_DevOps_Testing/README.md)
- [Biên bản thanh tra PR #41 (01_code_inspection_record_pr41.md)](../../../final-exam/preparation/6_Team_Monitoring_Risk_Lessons/01_code_inspection_record_pr41.md)
- [Biên bản phản hồi UAT (02_uat_feedback_record.md)](../../../final-exam/preparation/6_Team_Monitoring_Risk_Lessons/02_uat_feedback_record.md)
