# BẰNG CHỨNG NỘP KÈM — CÂU 14: MÔ HÌNH CHUYỂN GIAO LIÊN TỤC (CONTINUOUS DELIVERY)

**Mã câu hỏi:** `CÂU-14` | **Chủ đề:** Continuous Delivery (CD)

## 1. Đề bài và Yêu cầu nộp kèm từ Đề thi vấn đáp

> Vẽ và giải thích mô hình chuyển giao liên tục (Continuous Delivery) của nhóm. Ghi chú trên mô hình các công cụ nhóm đã dùng cho từng thành phần. Tại sao cần sử dụng hệ thống chuyển giao liên tục cho dự án? _(Sinh viên nộp kèm bản in kịch bản triển khai (deployment scripts), kịch bản cấu hình cơ sở dữ liệu, cấu hình các dịch vụ bên thứ ba, bản in giao diện email nhận thông báo về kết quả triển khai tự động, và bản in tài liệu Hướng dẫn triển khai hệ thống cho kỹ sư vận hành của nhóm.)_

## 2. Danh mục tài liệu / bằng chứng cần nộp kèm khi thi

| STT | Tên tài liệu / Bằng chứng nộp kèm                                                                   | Loại tài liệu                       | Nguồn tệp Markdown                                                                                                                                      | Nguồn tệp PDF / Ảnh chụp                                              | Mô tả chi tiết                                                                                                     |
| :-: | --------------------------------------------------------------------------------------------------- | ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
|  1  | **Bản in kịch bản triển khai (Deployment Scripts) — .github/workflows/cd.yml, scripts/run-prod.sh** | `Kịch bản CD (Code printout)`       | [cd.yml](.github/workflows/cd.yml)                                                                                                                      | [README.pdf](final-exam/preparation/5_CICD_DevOps_Testing/README.pdf) | Kịch bản tự động hóa quy trình đóng gói container, chạy migration và deploy lên hạ tầng Staging/Production.        |
|  2  | **Bản in kịch bản cấu hình CSDL & dịch vụ bên thứ ba (docker-compose.prod.yml, Terraform)**         | `Kịch bản cấu hình (Code printout)` | [docker-compose.prod.yml](docker-compose.prod.yml)                                                                                                      | [README.pdf](final-exam/preparation/5_CICD_DevOps_Testing/README.pdf) | Cấu hình Docker Compose Production, Nginx reverse proxy, PostgreSQL, MinIO S3 bucket, Cloudflare R2 và Brevo SMTP. |
|  3  | **Bản in giao diện email nhận thông báo kết quả triển khai tự động**                                | `Ảnh chụp giao diện email`          | [cd-brevo-deploy-email-live-url-terraform.png](final-exam/preparation/5_CICD_DevOps_Testing/printouts/Q14/cd-brevo-deploy-email-live-url-terraform.png) | [README.pdf](final-exam/preparation/5_CICD_DevOps_Testing/README.pdf) | Ảnh chụp email Brevo gửi tự động xác nhận deploy thành công kèm đường link Live URL của hệ thống.                  |
|  4  | **Bản in tài liệu Hướng dẫn triển khai hệ thống cho kỹ sư vận hành (Deployment Guide)**             | `Tài liệu in A4`                    | [14-continuous-delivery.md)](docs/03-execution-monitoring/07-deployment-guide.md "hoặc docs.1/md/14-continuous-delivery.md")                            | [14-continuous-delivery.pdf](docs.1/pdf/14-continuous-delivery.pdf)   | Quy trình vận hành, thiết lập biến môi trường, chạy migration Alembic, smoke test và kịch bản Rollback khi có lỗi. |
|  5  | **Bản in ảnh chụp GitHub Actions CD deploy, Terraform Summary và Live URL**                         | `Ảnh chụp màn hình`                 | [cd-workflow-deploy.png](final-exam/preparation/5_CICD_DevOps_Testing/printouts/Q14/cd-workflow-deploy.png)                                             | [README.pdf](final-exam/preparation/5_CICD_DevOps_Testing/README.pdf) | Minh chứng thực tế pipeline CD chạy pass và live URL hệ thống.                                                     |

## 3. Các bằng chứng & số liệu then chốt cần chỉ ra trên tài liệu

- **Mô hình CD:** CI Pass → Build Docker Images → Terraform Provisioning → Apply Database Migrations (Alembic) → Deploy Containers → Smoke Test tự động → Gửi Email Live URL.
- **Kịch bản triển khai:** `.github/workflows/cd.yml`, `scripts/run-prod.sh`, `docker-compose.prod.yml`.
- **Chiến lược Rollback:** Tự động giữ bản backup CSDL trước migration, hỗ trợ rollback phiên bản container trước đó trong < 2 phút.
- **Bằng chứng Live URL và email thông báo thực tế từ Brevo.:**

## 4. Khung hướng dẫn trả lời vấn đáp (WHAT — HOW — WHY — EVIDENCE)

- **WHAT (Khái niệm & Nội dung):** Mở rộng của CI nhằm đảm bảo mã nguồn sau khi vượt qua kiểm tra có thể tự động hoặc bán tự động triển khai an toàn lên môi trường vận hành.
- **HOW (Quy trình thực hiện):** Tự động hóa đóng gói container → Áp dụng IaC Terraform → Chạy migration cơ sở dữ liệu có kiểm soát → Kích hoạt smoke test → Gửi thông báo kết quả qua email.
- **WHY (Lý do & Giá trị):** Rút ngắn thời gian đưa tính năng mới tới người dùng (Time-to-Market), giảm thiểu rủi ro lỗi thao tác thủ công khi triển khai.
- **EVIDENCE (Minh chứng chỉ tay):** Chỉ vào File `cd.yml`, File `docker-compose.prod.yml`, Ảnh chụp Live URL và Email thông báo deploy.

## 5. Liên kết tệp nguồn và tài liệu liên quan

- [docs.1/md/14-continuous-delivery.md](../../md/14-continuous-delivery.md)
- [docs.1/pdf/14-continuous-delivery.pdf](../../pdf/14-continuous-delivery.pdf)
- [Deployment Guide (docs/03-execution-monitoring/07-deployment-guide.md)](../../../docs/03-execution-monitoring/07-deployment-guide.md)
- [Phiếu ôn tập Câu 14 (final-exam/preparation/5_CICD_DevOps_Testing/README.md)](../../../final-exam/preparation/5_CICD_DevOps_Testing/README.md)
