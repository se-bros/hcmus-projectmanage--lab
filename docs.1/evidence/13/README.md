# BẰNG CHỨNG NỘP KÈM — CÂU 13: MÔ HÌNH TÍCH HỢP LIÊN TỤC (CONTINUOUS INTEGRATION)

**Mã câu hỏi:** `CÂU-13` | **Chủ đề:** Continuous Integration (CI)

## 1. Đề bài và Yêu cầu nộp kèm từ Đề thi vấn đáp

> Vẽ và giải thích mô hình tích hợp liên tục (Continuous Integration) của nhóm. Ghi chú trên mô hình các công cụ nhóm đã dùng cho từng thành phần. Tại sao cần sử dụng hệ thống tích hợp liên tục cho dự án? _(Sinh viên nộp kèm bản in kịch bản build (build scripts), bản in giao diện email nhận thông báo về kết quả build tự động, và bản in tài liệu Hướng dẫn cài đặt công cụ và biên dịch mã nguồn hệ thống cho máy tính của nhà phát triển của nhóm.)_

## 2. Danh mục tài liệu / bằng chứng cần nộp kèm khi thi

| STT | Tên tài liệu / Bằng chứng nộp kèm                                             | Loại tài liệu                 | Tệp đính kèm tại thư mục này                                   | Nguồn tài liệu PDF | Mô tả chi tiết                                                                                                         |
| :-: | ----------------------------------------------------------------------------- | ----------------------------- | -------------------------------------------------------------- | ------------------ | ---------------------------------------------------------------------------------------------------------------------- |
|  1  | **Bản in kịch bản CI Build Scripts (.github/workflows/ci.yml)**               | `Kịch bản CI (Code printout)` | [01_ci_build_script_ci_yml.md](./01_ci_build_script_ci_yml.md) | N/A                | Kịch bản tự động hóa GitHub Actions thực hiện format check, linting, unit test backend/frontend và validate Terraform. |
|  2  | **Bản in ảnh chụp GitHub Actions CI chạy thành công (CI-pass.png)**           | `Ảnh chụp màn hình`           | [CI-pass.png](./CI-pass.png)                                   | N/A                | Ảnh chụp thực tế tất cả các jobs CI trên GitHub Actions đều pass 100%.                                                 |
|  3  | **Bản in giao diện email nhận thông báo kết quả build tự động (Mail.png)**    | `Ảnh chụp giao diện email`    | [Mail.png](./Mail.png)                                         | N/A                | Ảnh chụp email Brevo gửi tự động thông báo kết quả build sau mỗi lần merge vào nhánh main.                             |
|  4  | **Bản in tài liệu Hướng dẫn cài đặt và biên dịch mã nguồn (Developer Guide)** | `Tài liệu in A4`              | [06-developer-guide.md](./06-developer-guide.md)               | N/A                | Tài liệu chuẩn hóa các bước cài đặt môi trường dev, chạy Docker, cài thư viện và biên dịch mã nguồn.                   |

## 3. Các bằng chứng & số liệu then chốt cần chỉ ra trên tài liệu

- **Mô hình CI:** Developer Commit → Push PR → GitHub Actions kích hoạt 4 jobs song song: (1) Backend Ruff/Pytest, (2) Frontend ESLint/Next Build, (3) Terraform Validate, (4) Notify Email qua Brevo API.
- Kịch bản `.github/workflows/ci.yml` có sẵn trong repo, thiết lập ma trận kiểm tra tự động.
- **Lợi ích CI:** Phát hiện lỗi tích hợp ngay trong vòng 3 phút, bảo đảm nhánh `main` luôn ở trạng thái biên dịch thành công.
- **Developer Guide chuẩn:** Các bước `docker compose up -d`, `npm ci`, `pytest` được chuẩn hóa.

## 4. Khung hướng dẫn trả lời vấn đáp (WHAT — HOW — WHY — EVIDENCE)

- **WHAT (Khái niệm & Nội dung):** Thực hành phát triển phần mềm trong đó các thành viên tích hợp mã nguồn thường xuyên vào nhánh chính, mỗi lần tích hợp được kiểm tra tự động bằng build và test.
- **HOW (Quy trình thực hiện):** Cấu hình GitHub Actions runner → Thiết lập jobs linting, testing, validation → Tích hợp dịch vụ gửi email Brevo qua Webhook/Action → Ban hành Developer Guide.
- **WHY (Lý do & Giá trị):** Loại bỏ 'Integration Hell' (địa ngục tích hợp vào cuối kỳ), tăng độ tin cậy và tốc độ phát triển của nhóm.
- **EVIDENCE (Minh chứng chỉ tay):** Chỉ vào Bản in file `ci.yml`, Ảnh chụp màn hình CI-pass và Email thông báo thực tế.

## 5. Liên kết tệp nguồn và tài liệu liên quan

- [Kịch bản CI (.github/workflows/ci.yml)](../../../.github/workflows/ci.yml)
- [Developer Guide (docs/03-execution-monitoring/06-developer-guide.md)](../../../docs/03-execution-monitoring/06-developer-guide.md)
- [Phiếu ôn tập Câu 13 (final-exam/preparation/5_CICD_DevOps_Testing/README.md)](../../../final-exam/preparation/5_CICD_DevOps_Testing/README.md)
