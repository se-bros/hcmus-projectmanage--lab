# BẰNG CHỨNG NỘP KÈM — CÂU 14: MÔ HÌNH CHUYỂN GIAO LIÊN TỤC (CONTINUOUS DELIVERY)

**Mã câu hỏi:** `CÂU-14` | **Chủ đề:** Continuous Delivery (CD)

## 1. Đề bài và Yêu cầu nộp kèm từ Đề thi vấn đáp

> Vẽ và giải thích mô hình chuyển giao liên tục (Continuous Delivery) của nhóm. Ghi chú trên mô hình các công cụ nhóm đã dùng cho từng thành phần. Tại sao cần sử dụng hệ thống chuyển giao liên tục cho dự án? _(Sinh viên nộp kèm bản in kịch bản triển khai (deployment scripts), kịch bản cấu hình cơ sở dữ liệu, cấu hình các dịch vụ bên thứ ba, bản in giao diện email nhận thông báo về kết quả triển khai tự động, và bản in tài liệu Hướng dẫn triển khai hệ thống cho kỹ sư vận hành của nhóm.)_

## 2. Danh mục tài liệu / bằng chứng cần nộp kèm khi thi

| STT | Tên tài liệu / Bằng chứng nộp kèm                                                       | Loại tài liệu                 | Tệp đính kèm tại thư mục này                                                                   | Nguồn tài liệu PDF | Mô tả chi tiết                                                                                                     |
| :-: | --------------------------------------------------------------------------------------- | ----------------------------- | ---------------------------------------------------------------------------------------------- | ------------------ | ------------------------------------------------------------------------------------------------------------------ |
|  1  | **Bản in kịch bản triển khai (Deployment Scripts) — cd.yml**                            | `Kịch bản CD (Code printout)` | [01_cd_deploy_script_cd_yml.md](./01_cd_deploy_script_cd_yml.md)                               | N/A                | Kịch bản tự động hóa quy trình đóng gói container, chạy migration và deploy lên hạ tầng Staging/Production.        |
|  2  | **Bản in cấu hình Docker Compose Production (docker-compose.prod.yml)**                 | `Kịch bản cấu hình`           | [02_docker_compose_prod_config.md](./02_docker_compose_prod_config.md)                         | N/A                | Cấu hình Docker Compose Production, Nginx reverse proxy, PostgreSQL, MinIO S3 bucket, Prometheus và Grafana.       |
|  3  | **Bản in giao diện email nhận thông báo kết quả triển khai tự động**                    | `Ảnh chụp giao diện email`    | [cd-brevo-deploy-email-live-url-terraform.png](./cd-brevo-deploy-email-live-url-terraform.png) | N/A                | Ảnh chụp email Brevo gửi tự động xác nhận deploy thành công kèm đường link Live URL của hệ thống.                  |
|  4  | **Bản in tài liệu Hướng dẫn triển khai hệ thống cho kỹ sư vận hành (Deployment Guide)** | `Tài liệu in A4`              | [07-deployment-guide.md](./07-deployment-guide.md)                                             | N/A                | Quy trình vận hành, thiết lập biến môi trường, chạy migration Alembic, smoke test và kịch bản Rollback khi có lỗi. |
|  5  | **Bản in ảnh chụp GitHub Actions CD deploy và Live URL thực tế**                        | `Ảnh chụp màn hình`           | [cd-workflow-deploy.png](./cd-workflow-deploy.png)                                             | N/A                | Minh chứng thực tế pipeline CD chạy pass và live URL hệ thống.                                                     |

## 3. Các bằng chứng & số liệu then chốt cần chỉ ra trên tài liệu

- **Mô hình CD:** CI Pass → Build Docker Images → Provisioning → Apply Database Migrations (Alembic) → Deploy Containers → Smoke Test tự động → Gửi Email Live URL.
- **Kịch bản triển khai:** `cd.yml`, `scripts/run-prod.sh`, `docker-compose.prod.yml`.
- **Chiến lược Rollback:** Tự động giữ bản backup CSDL trước migration, hỗ trợ rollback phiên bản container trước đó trong < 2 phút.
- Bằng chứng Live URL và email thông báo thực tế từ Brevo.

## 4. Khung hướng dẫn trả lời vấn đáp (WHAT — HOW — WHY — EVIDENCE)

- **WHAT (Khái niệm & Nội dung):** Mở rộng của CI nhằm đảm bảo mã nguồn sau khi vượt qua kiểm tra có thể tự động triển khai an toàn lên môi trường vận hành.
- **HOW (Quy trình thực hiện):** Tự động hóa đóng gói container → Áp dụng IaC Terraform → Chạy migration cơ sở dữ liệu có kiểm soát → Kích hoạt smoke test → Gửi thông báo kết quả qua email.
- **WHY (Lý do & Giá trị):** Rút ngắn thời gian đưa tính năng mới tới người dùng (Time-to-Market), giảm thiểu rủi ro lỗi thao tác thủ công khi triển khai.
- **EVIDENCE (Minh chứng chỉ tay):** Chỉ vào File `cd.yml`, File `docker-compose.prod.yml`, Ảnh chụp Live URL và Email thông báo deploy.

## 5. Liên kết tệp nguồn và tài liệu liên quan

- [Kịch bản CD (.github/workflows/cd.yml)](../../../.github/workflows/cd.yml)
- [Deployment Guide (docs/03-execution-monitoring/07-deployment-guide.md)](../../../docs/03-execution-monitoring/07-deployment-guide.md)
- [Phiếu ôn tập Câu 14 (final-exam/preparation/5_CICD_DevOps_Testing/README.md)](../../../final-exam/preparation/5_CICD_DevOps_Testing/README.md)
