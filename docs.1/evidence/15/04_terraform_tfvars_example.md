# BẢN IN KỊCH BẢN HẠ TẦNG TERRAFORM IAAC: `terraform.tfvars.example`

## Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS (HCMUS-LDMS)

---

### THÔNG TIN TỆP NGUỒN (FILE CONTROL)

| Trường thông tin                 | Nội dung chi tiết                                         |
| -------------------------------- | --------------------------------------------------------- |
| **Tên tệp tin (File Name):**     | `terraform.tfvars.example`                                |
| **Đường dẫn trong Repo (Path):** | `terraform/terraform.tfvars.example`                      |
| **Công nghệ:**                   | HashiCorp Terraform (Infrastructure as Code - IaC)        |
| **Mô tả chức năng:**             | Tệp cấu hình biến mẫu cho môi trường Production / Staging |

---

## 1. Toàn văn mã nguồn kịch bản `terraform/terraform.tfvars.example`

```hcl
# ==============================================================================
# Sample Terraform Variables - HCMUS-LDMS Infrastructure Customization
# ==============================================================================

app_env             = "production"
project_name        = "ldms"
postgres_user       = "ldms"
postgres_password   = "ldms"
postgres_db         = "ldms"
postgres_port       = 5434

minio_root_user     = "ldms"
minio_root_password = "ldms12345"
minio_api_port      = 9002
minio_console_port  = 9003

web_port            = 8080
web_ssl_port        = 8443
api_port            = 8000
grafana_port        = 3000
prometheus_port     = 9090
mailhog_ui_port     = 8025

live_app_url        = "https://hcmus-projectmanage-lab.vercel.app"
```
