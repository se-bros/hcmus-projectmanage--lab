# BẰNG CHỨNG NỘP KÈM — CÂU 20: KẾ HOẠCH KIỂM THỬ (TEST PLAN)

**Mã câu hỏi:** `CÂU-20` | **Chủ đề:** Software Test Plan

## 1. Đề bài và Yêu cầu nộp kèm từ Đề thi vấn đáp

> Trình bày quá trình hình thành và phương pháp đánh giá tài liệu Kế hoạch kiểm thử (Test Plan) của nhóm. _(Sinh viên nộp kèm bản in tài liệu Kế hoạch kiểm thử của nhóm, bản in giao diện cấu hình đảm bảo Coding Standards cho mã nguồn của nhóm, bản in giao diện hệ thống quản lý lỗi với dữ liệu thực tế của nhóm, bản in giao diện kết quả chạy mã nguồn kiểm thử đơn vị (Unit Tests) của nhóm, bản in biên bản thanh tra mã nguồn của nhóm, bản in báo cáo kết quả kiểm thử của nhóm, bản in biên bản phản hồi của khách hàng của nhóm.)_

## 2. Danh mục tài liệu / bằng chứng cần nộp kèm khi thi

| STT | Tên tài liệu / Bằng chứng nộp kèm                                                     | Loại tài liệu               | Tệp đính kèm tại thư mục này                                                           | Nguồn tài liệu PDF                             | Mô tả chi tiết                                                                                                                 |
| :-: | ------------------------------------------------------------------------------------- | --------------------------- | -------------------------------------------------------------------------------------- | ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
|  1  | **Bản in tài liệu Kế hoạch kiểm thử (Test Plan)**                                    | `Tài liệu in A4`            | [20-test-plan.pdf](./20-test-plan.pdf)                                                 | [20-test-plan.pdf](../../pdf/20-test-plan.pdf) | Chiến lược kiểm thử đa tầng (Unit, Integration, Security, Performance, UAT), ma trận truy vết RTM và báo cáo kết quả kiểm thử. |
|  2  | **Bản in cấu hình tiêu chuẩn Coding Standards & Linter (ruff, eslint, markdownlint)** | `Tài liệu cấu hình linter`  | [03_coding_standards_and_linter_config.md](./03_coding_standards_and_linter_config.md) | N/A                                            | Cấu hình linter chuẩn: Ruff cho Python, ESLint/Prettier cho Next.js, Markdownlint cho tài liệu.                                |
|  3  | **Bản in giao diện kết quả chạy mã nguồn Unit Tests (run-test.png)**                  | `Ảnh chụp màn hình console` | [run-test.png](./run-test.png)                                                         | N/A                                            | Ảnh chụp console chạy Pytest backend với 100% tests pass và báo cáo code coverage.                                             |
|  4  | **Bản in Biên bản thanh tra mã nguồn của nhóm (Code Inspection PR #41)**              | `Biên bản in A4`            | [01_code_inspection_record_pr41.md](./01_code_inspection_record_pr41.md)               | N/A                                            | Biên bản thanh tra PR #41 theo chuẩn IEEE 1028.                                                                                |
|  5  | **Bản in Biên bản phản hồi của khách hàng (UAT Feedback Record)**                     | `Biên bản in A4`            | [02_uat_feedback_record.md](./02_uat_feedback_record.md)                               | N/A                                            | Biên bản UAT nghiệm thu người dùng thực tế ngày 15/08/2026.                                                                    |

## 3. Các bằng chứng & số liệu then chốt cần chỉ ra trên tài liệu

- **Chiến lược kiểm thử Test Pyramid:** Unit Test (Pytest/Vitest) chiếm 70% → Integration Test 20% → E2E/UAT 10%.
- **Ma trận truy vết (RTM):** 100% của 15 Must stories đều có ít nhất 2 Test Cases tương ứng.
- **Bằng chứng chạy test:** Pytest backend pass 100%, code coverage đạt > 80%.
- **Hệ thống quản lý lỗi:** Quy trình Issue Lifecycle trên GitHub (Triage → In Progress → In Review → Verified & Closed).

## 4. Khung hướng dẫn trả lời vấn đáp (WHAT — HOW — WHY — EVIDENCE)

- **WHAT (Khái niệm & Nội dung):** Tài liệu chi tiết hóa phạm vi, phương pháp, nguồn lực và lịch trình của các hoạt động kiểm thử nhằm xác minh phần mềm đáp ứng đúng yêu cầu.
- **HOW (Quy trình thực hiện):** Phân tích yêu cầu từ SRS/Backlog → Thiết kế Test Cases & RTM → Viết mã nguồn Unit/Integration test tự động → Chạy test trong CI → Ghi nhận và theo dõi lỗi qua GitHub Issues → Thực hiện UAT.
- **WHY (Lý do & Giá trị):** Đảm bảo chất lượng phần mềm không có lỗi nghiêm trọng trước khi bàn giao cho người dùng cuối.
- **EVIDENCE (Minh chứng chỉ tay):** Chỉ vào Bản in Test Plan, Ảnh chụp màn hình Pytest Report `run-test.png` và Biên bản UAT.

## 5. Liên kết tệp nguồn và tài liệu liên quan

- [Tài liệu Kế hoạch kiểm thử (docs.1/md/20-test-plan.md)](../../md/20-test-plan.md)
- [Phiếu ôn tập Câu 20 (final-exam/preparation/5_CICD_DevOps_Testing/README.md)](../../../final-exam/preparation/5_CICD_DevOps_Testing/README.md)
