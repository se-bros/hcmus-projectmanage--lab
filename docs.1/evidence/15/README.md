# BẰNG CHỨNG NỘP KÈM — CÂU 15: MÔ HÌNH DEVOPS

**Mã câu hỏi:** `CÂU-15` | **Chủ đề:** DevOps Model & Operations

## 1. Đề bài và Yêu cầu nộp kèm từ Đề thi vấn đáp

> Vẽ và giải thích mô hình DevOps của nhóm. Ghi chú trên mô hình các công cụ nhóm đã dùng cho từng thành phần. Tại sao cần sử dụng quy trình DevOps cho dự án? Giải thích quy trình phát triển, triển khai và vận hành liên tục đồng thời nhiều phiên bản trên của dự án bằng cách áp dụng DevOps. _(Sinh viên nộp kèm bản in kịch bản khởi tạo và cấu hình tài nguyên hạ tầng cho việc triển khai hệ thống của nhóm, bản in hệ thống thư mục và tệp tin hỗ trợ quản lý hạ tầng triển khai.)_

## 2. Danh mục tài liệu / bằng chứng cần nộp kèm khi thi

| STT | Tên tài liệu / Bằng chứng nộp kèm                                                     | Loại tài liệu                    | Nguồn tệp Markdown                                                                         | Nguồn tệp PDF / Ảnh chụp                                                | Mô tả chi tiết                                                                                                                            |
| :-: | ------------------------------------------------------------------------------------- | -------------------------------- | ------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
|  1  | **Bản in kịch bản khởi tạo và cấu hình tài nguyên hạ tầng (Terraform / IaC Scripts)** | `Kịch bản IaC (Code printout)`   | [main.tf (hoặc docker-compose.prod.yml)](terraform/main.tf "hoặc docker-compose.prod.yml") | [README.pdf](final-exam/preparation/5_CICD_DevOps_Testing/README.pdf)   | Kịch bản Terraform và Docker Compose định nghĩa toàn bộ tài nguyên máy chủ, mạng, volume lưu trữ và dịch vụ giám sát.                     |
|  2  | **Bản in hệ thống thư mục và tệp tin hỗ trợ quản lý hạ tầng triển khai**              | `Cây thư mục / Cấu hình hạ tầng` | [15-devops-and-operations.md](docs.1/md/15-devops-and-operations.md)                       | [15-devops-and-operations.pdf](docs.1/pdf/15-devops-and-operations.pdf) | Cây cấu trúc thư mục `terraform/`, `monitoring/` (Prometheus, Grafana), `scripts/` (backup-postgres.sh, backup-minio.sh) và Nginx config. |
|  3  | **Bản in giao diện Monitoring Prometheus/Grafana, Docker Containers và Health Check** | `Ảnh chụp màn hình giám sát`     | [](final-exam/preparation/5_CICD_DevOps_Testing/printouts/Q15/)                            | [README.pdf](final-exam/preparation/5_CICD_DevOps_Testing/README.pdf)   | Ảnh chụp dashboard giám sát hiệu năng hệ thống CPU/RAM/Network, Prometheus metrics và Docker container health status.                     |

## 3. Các bằng chứng & số liệu then chốt cần chỉ ra trên tài liệu

- **Mô hình DevOps CALMS (Culture, Automation, Lean, Measurement, Sharing).:**
- **Quản lý hạ tầng bằng mã (Infrastructure as Code - IaC) qua Terraform và Docker Compose.:**
- **Quy trình đa môi trường:** Local Dev (Docker) → Staging CI/CD → Production/Demo Cloud.
- **Giám sát & Vận hành:** Prometheus thu thập metrics, Grafana trực quan hóa dashboard, kịch bản sao lưu tự động `backup-postgres.sh` và `backup-minio.sh`.

## 4. Khung hướng dẫn trả lời vấn đáp (WHAT — HOW — WHY — EVIDENCE)

- **WHAT (Khái niệm & Nội dung):** Sự kết hợp giữa triết lý văn hóa, thực hành và công cụ nhằm tăng khả năng phân phối ứng dụng với vận tốc cao và độ tin cậy vượt trội.
- **HOW (Quy trình thực hiện):** Thiết lập pipeline CI/CD → Chuẩn hóa hạ tầng bằng Terraform/Docker → Tích hợp hệ thống giám sát Prometheus/Grafana → Tự động hóa quy trình sao lưu và phục hồi.
- **WHY (Lý do & Giá trị):** Phá bỏ bức tường ngăn cách giữa Development và Operations, đảm bảo hệ thống vận hành liên tục và ổn định.
- **EVIDENCE (Minh chứng chỉ tay):** Chỉ vào File `terraform/main.tf`, Cây thư mục `monitoring/` và Ảnh chụp Grafana Dashboard trong bản in.

## 5. Liên kết tệp nguồn và tài liệu liên quan

- [docs.1/md/15-devops-and-operations.md](../../md/15-devops-and-operations.md)
- [docs.1/pdf/15-devops-and-operations.pdf](../../pdf/15-devops-and-operations.pdf)
- [Thư mục Terraform (terraform/)](../../../terraform)
- [Thư mục Monitoring (monitoring/)](../../../monitoring)
- [Phiếu ôn tập Câu 15 (final-exam/preparation/5_CICD_DevOps_Testing/README.md)](../../../final-exam/preparation/5_CICD_DevOps_Testing/README.md)
