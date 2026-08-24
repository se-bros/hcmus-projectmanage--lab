# BẢN IN KỊCH BẢN HẠ TẦNG TERRAFORM IAAC: `variables.tf`

## Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS (HCMUS-LDMS)

---

### THÔNG TIN TỆP NGUỒN (FILE CONTROL)

| Trường thông tin                 | Nội dung chi tiết                                                                |
| -------------------------------- | -------------------------------------------------------------------------------- |
| **Tên tệp tin (File Name):**     | `variables.tf`                                                                   |
| **Đường dẫn trong Repo (Path):** | `terraform/variables.tf`                                                         |
| **Công nghệ:**                   | HashiCorp Terraform (Infrastructure as Code - IaC)                               |
| **Mô tả chức năng:**             | Khai báo các biến cấu hình tham số hóa hạ tầng (Ports, Credentials, Environment) |

---

## 1. Toàn văn mã nguồn kịch bản `terraform/variables.tf`

```hcl
# ==============================================================================
# Terraform Variables - HCMUS-LDMS Infrastructure as Code (IaaC)
# ==============================================================================

variable "app_env" {
  description = "Target application environment (development or production)"
  type        = string
  default     = "production"
}

variable "project_name" {
  description = "Project name identifier used for container and network naming"
  type        = string
  default     = "ldms"
}

# --- Database Variables ---

variable "postgres_user" {
  description = "PostgreSQL superuser username"
  type        = string
  default     = "ldms"
}

variable "postgres_password" {
  description = "PostgreSQL superuser password"
  type        = string
  default     = "ldms"
  sensitive   = true
}

variable "postgres_db" {
  description = "PostgreSQL default database name"
  type        = string
  default     = "ldms"
}

variable "postgres_port" {
  description = "Host port exposed for PostgreSQL"
  type        = number
  default     = 5434
}

# --- Object Storage Variables ---

variable "minio_root_user" {
  description = "MinIO root administrator username"
  type        = string
  default     = "ldms"
}

variable "minio_root_password" {
  description = "MinIO root administrator password"
  type        = string
  default     = "ldms12345"
  sensitive   = true
}

variable "minio_api_port" {
  description = "Host port exposed for MinIO S3 API"
  type        = number
  default     = 9002
}

variable "minio_console_port" {
  description = "Host port exposed for MinIO Web Console"
  type        = number
  default     = 9003
}

# --- Service Ports ---

variable "api_port" {
  description = "Host port exposed for FastAPI Backend API"
  type        = number
  default     = 8000
}

variable "web_port" {
  description = "Host port exposed for Nginx Frontend (HTTP)"
  type        = number
  default     = 8080
}

variable "web_ssl_port" {
  description = "Host port exposed for Nginx Frontend (HTTPS)"
  type        = number
  default     = 8443
}

variable "grafana_port" {
  description = "Host port exposed for Grafana Dashboard"
  type        = number
  default     = 3000
}

variable "prometheus_port" {
  description = "Host port exposed for Prometheus Metrics"
  type        = number
  default     = 9090
}

variable "mailhog_ui_port" {
  description = "Host port exposed for MailHog Web UI"
  type        = number
  default     = 8025
}

variable "live_app_url" {
  description = "Public live deployment URL"
  type        = string
  default     = "https://hcmus-projectmanage-lab.vercel.app"
}
```
