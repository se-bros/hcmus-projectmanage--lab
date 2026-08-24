# BẰNG CHỨNG NỘP KÈM — CÂU 15: MÔ HÌNH DEVOPS

**Mã câu hỏi:** `CÂU-15` | **Chủ đề:** DevOps Model & Operations

## 1. Đề bài và Yêu cầu nộp kèm từ Đề thi vấn đáp

> Vẽ và giải thích mô hình DevOps của nhóm. Ghi chú trên mô hình các công cụ nhóm đã dùng cho từng thành phần. Tại sao cần sử dụng quy trình DevOps cho dự án? Giải thích quy trình phát triển, triển khai và vận hành liên tục đồng thời nhiều phiên bản trên của dự án bằng cách áp dụng DevOps. _(Sinh viên nộp kèm bản in kịch bản khởi tạo và cấu hình tài nguyên hạ tầng cho việc triển khai hệ thống của nhóm, bản in hệ thống thư mục và tệp tin hỗ trợ quản lý hạ tầng triển khai.)_

## 2. Danh mục tài liệu / bằng chứng cần nộp kèm khi thi

| STT | Tên tài liệu / Bằng chứng nộp kèm | Loại tài liệu | Tệp đính kèm tại thư mục này | Nguồn tài liệu PDF | Mô tả chi tiết |
|:---:|---|---|---|---|---|
| 1 | **Bản in kịch bản khởi tạo tài nguyên hạ tầng Terraform (terraform_main.tf)** | `Kịch bản IaC (Code printout)` | [terraform_main.tf](./terraform_main.tf) | N/A | Kịch bản Terraform định nghĩa toàn bộ tài nguyên Docker network, volume, container PostgreSQL, MinIO, Prometheus và Grafana. |
| 2 | **Bản in biến và đầu ra Terraform (terraform_variables.tf, terraform_outputs.tf)** | `Kịch bản IaC` | [terraform_outputs.tf](./terraform_outputs.tf) | N/A | Khai báo biến cấu hình hạ tầng và trích xuất tự động các Live URL endpoint sau khi apply. |
| 3 | **Bản in ảnh chụp kết quả chạy Terraform Init, Plan và CI Validation** | `Ảnh chụp màn hình` | [terraform-plan.png](./terraform-plan.png) | N/A | Ảnh chụp thực tế quá trình chạy terraform plan, terraform apply và kiểm tra tự động trong CI pipeline. |

## 3. Các bằng chứng & số liệu then chốt cần chỉ ra trên tài liệu

- Mô hình DevOps CALMS (Culture, Automation, Lean, Measurement, Sharing).
- Quản lý hạ tầng bằng mã (Infrastructure as Code - IaC) qua Terraform và Docker Compose.
- **Quy trình đa môi trường:** Local Dev (Docker) → Staging CI/CD → Production/Demo Cloud.
- **Giám sát & Vận hành:** Prometheus thu thập metrics, Grafana trực quan hóa dashboard, kịch bản sao lưu tự động `backup-postgres.sh` và `backup-minio.sh`.

## 4. Khung hướng dẫn trả lời vấn đáp (WHAT — HOW — WHY — EVIDENCE)

- **WHAT (Khái niệm & Nội dung):** Sự kết hợp giữa triết lý văn hóa, thực hành và công cụ nhằm tăng khả năng phân phối ứng dụng với vận tốc cao và độ tin cậy vượt trội.
- **HOW (Quy trình thực hiện):** Thiết lập pipeline CI/CD → Chuẩn hóa hạ tầng bằng Terraform/Docker → Tích hợp hệ thống giám sát Prometheus/Grafana → Tự động hóa quy trình sao lưu và phục hồi.
- **WHY (Lý do & Giá trị):** Phá bỏ bức tường ngăn cách giữa Development và Operations, đảm bảo hệ thống vận hành liên tục và ổn định.
- **EVIDENCE (Minh chứng chỉ tay):** Chỉ vào File `terraform_main.tf`, File `terraform_outputs.tf` và Ảnh chụp Terraform Plan.

## 5. Liên kết tệp nguồn và tài liệu liên quan

- [Thư mục Terraform (terraform/)](../../../terraform)
- [Thư mục Monitoring (monitoring/)](../../../monitoring)
- [Phiếu ôn tập Câu 15 (final-exam/preparation/5_CICD_DevOps_Testing/README.md)](../../../final-exam/preparation/5_CICD_DevOps_Testing/README.md)
