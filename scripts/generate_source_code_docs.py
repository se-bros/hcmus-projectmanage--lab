import os
import subprocess
import shutil

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MD_TO_PDF = os.path.join(BASE_DIR, ".agents", "skills", "doc_generator", "scripts", "md_to_pdf.py")

def build_q13_ci_script():
    ev_dir = os.path.join(BASE_DIR, "docs.1", "evidence", "13")
    pr_dir = os.path.join(BASE_DIR, "docs.1", "print", "13")
    os.makedirs(ev_dir, exist_ok=True)
    os.makedirs(pr_dir, exist_ok=True)

    ci_yml_path = os.path.join(BASE_DIR, ".github", "workflows", "ci.yml")
    with open(ci_yml_path, "r", encoding="utf-8") as f:
        ci_code = f.read().strip()

    md_content = f"""# BẢN IN KỊCH BẢN TÍCH HỢP LIÊN TỤC (CI BUILD SCRIPT)

## Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS (HCMUS-LDMS)

---

### THÔNG TIN TỆP NGUỒN (FILE CONTROL)

| Trường thông tin | Nội dung chi tiết |
|---|---|
| **Tên tệp tin (File Name):** | `ci.yml` |
| **Đường dẫn trong Repo (Path):** | `.github/workflows/ci.yml` |
| **Công cụ CI áp dụng:** | GitHub Actions |
| **Mục đích:** | Tự động hóa kiểm tra format, linting mã nguồn Backend/Frontend, chạy suite 141 test cases Pytest, xác thực cấu hình Terraform và gửi thông báo kết quả qua email Brevo |
| **Sự kiện kích hoạt (Triggers):** | Push vào `main`, `master`, `develop`, `release/*` hoặc mở Pull Request |

---

## 1. Giải thích các luồng công việc (Jobs Breakdown)

1. **`backend-tests`**: Cài đặt môi trường Python 3.12 bằng công cụ `uv`, cấu hình cache thư viện, chạy linter `ruff check .`, format `ruff format --check .` và thực thi toàn bộ suite kiểm thử `uv run pytest --maxfail=1 --disable-warnings -v`.
2. **`frontend-lint-build`**: Cài đặt Node.js 20, thực hiện cài đặt sạch `npm ci`, chạy linter `npm run lint` và biên dịch kiểm tra tính toàn vẹn `npm run build`.
3. **`terraform-validate`**: Cài đặt Terraform CLI, khởi tạo `terraform init -backend=false`, kiểm tra định dạng `terraform fmt -check` và xác thực cú pháp `terraform validate`.
4. **`notify-email`**: Thu thập trạng thái kết quả của 3 jobs trên, gửi email báo cáo chi tiết đến quản trị viên qua Brevo API / SMTP webhook.

---

## 2. Toàn văn mã nguồn kịch bản `.github/workflows/ci.yml`

```yaml
{ci_code}
```
"""
    md_file = os.path.join(ev_dir, "01_ci_build_script_ci_yml.md")
    with open(md_file, "w", encoding="utf-8") as f:
        f.write(md_content)

    pdf_file = os.path.join(pr_dir, "01_ci_build_script_ci_yml.pdf")
    subprocess.run(["python", MD_TO_PDF, md_file, pdf_file], check=True)
    print("Generated Q13 CI script markdown and PDF.")

def build_q14_cd_scripts():
    ev_dir = os.path.join(BASE_DIR, "docs.1", "evidence", "14")
    pr_dir = os.path.join(BASE_DIR, "docs.1", "print", "14")
    os.makedirs(ev_dir, exist_ok=True)
    os.makedirs(pr_dir, exist_ok=True)

    # 1. cd.yml
    cd_yml_path = os.path.join(BASE_DIR, ".github", "workflows", "cd.yml")
    with open(cd_yml_path, "r", encoding="utf-8") as f:
        cd_code = f.read().strip()

    cd_md = f"""# BẢN IN KỊCH BẢN CHUYỂN GIAO LIÊN TỤC (CD DEPLOYMENT SCRIPT)

## Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS (HCMUS-LDMS)

---

### THÔNG TIN TỆP NGUỒN (FILE CONTROL)

| Trường thông tin | Nội dung chi tiết |
|---|---|
| **Tên tệp tin (File Name):** | `cd.yml` |
| **Đường dẫn trong Repo (Path):** | `.github/workflows/cd.yml` |
| **Công cụ CD áp dụng:** | GitHub Actions |
| **Mục đích:** | Tự động hóa quy trình đóng gói container, kiểm tra hạ tầng staging/production, kích hoạt triển khai và gửi email Live URL qua Brevo |
| **Sự kiện kích hoạt (Triggers):** | Push vào nhánh `main` hoặc `release/*` sau khi vượt qua toàn bộ CI Pipeline |

---

## 1. Giải thích quy trình Chuyển giao liên tục (CD Pipeline Flow)

1. **`build-and-test`**: Xác minh lần cuối toàn bộ kiểm thử trước khi tiến hành đóng gói phiên bản phát hành.
2. **`deploy`**: Đóng gói các Docker images (`web`, `api`), áp dụng biến môi trường Production an toàn, kiểm tra tính sẵn sàng của cơ sở dữ liệu PostgreSQL và kho MinIO.
3. **`smoke-test`**: Gửi yêu cầu HTTP kiểm tra endpoint `GET /health` đảm bảo hệ thống phản hồi mã trạng thái 200 OK.
4. **`notify-deployment`**: Tự động trích xuất Live URL triển khai và gửi thông báo nghiệm thu qua email Brevo.

---

## 2. Toàn văn mã nguồn kịch bản `.github/workflows/cd.yml`

```yaml
{cd_code}
```
"""
    cd_md_file = os.path.join(ev_dir, "01_cd_deploy_script_cd_yml.md")
    with open(cd_md_file, "w", encoding="utf-8") as f:
        f.write(cd_md)
    subprocess.run(["python", MD_TO_PDF, cd_md_file, os.path.join(pr_dir, "01_cd_deploy_script_cd_yml.pdf")], check=True)

    # 2. docker-compose.prod.yml
    compose_path = os.path.join(BASE_DIR, "docker-compose.prod.yml")
    with open(compose_path, "r", encoding="utf-8") as f:
        compose_code = f.read().strip()

    compose_md = f"""# BẢN IN CẤU HÌNH HẠ TẦNG DOCKER COMPOSE PRODUCTION

## Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS (HCMUS-LDMS)

---

### THÔNG TIN TỆP NGUỒN (FILE CONTROL)

| Trường thông tin | Nội dung chi tiết |
|---|---|
| **Tên tệp tin (File Name):** | `docker-compose.prod.yml` |
| **Đường dẫn trong Repo (Path):** | `docker-compose.prod.yml` |
| **Công nghệ:** | Docker Compose v2 (Multi-container Orchestration) |
| **Mục đích:** | Định nghĩa toàn bộ hạ tầng vận hành: Reverse Proxy Nginx (TLS 8443), Frontend React, Backend FastAPI, CSDL PostgreSQL, Lưu trữ MinIO S3, Giám sát Prometheus & Grafana |

---

## 1. Danh mục các dịch vụ cấu hình (Services Architecture)

1. **`nginx`**: Cổng đón tiếp HTTP (cổng 8080) và HTTPS (cổng 8443), định tuyến traffic tới Frontend và Backend.
2. **`web`**: Giao diện người dùng React/Next.js phục vụ độc giả và thủ thư.
3. **`api`**: Máy chủ backend FastAPI xử lý OCR, trích xuất metadata và quản lý phân quyền RBAC.
4. **`postgres`**: Cơ sở dữ liệu quan hệ PostgreSQL 16 lưu trữ người dùng, mục lục và siêu dữ liệu.
5. **`minio`**: Kho lưu trữ đối tượng S3-compatible lưu trữ tệp scan gốc và tệp sách điện tử EPUB.
6. **`prometheus` & `grafana`**: Hệ thống thu thập metrics và giám sát hiệu năng trực quan.

---

## 2. Toàn văn cấu hình `docker-compose.prod.yml`

```yaml
{compose_code}
```
"""
    compose_md_file = os.path.join(ev_dir, "02_docker_compose_prod_config.md")
    with open(compose_md_file, "w", encoding="utf-8") as f:
        f.write(compose_md)
    subprocess.run(["python", MD_TO_PDF, compose_md_file, os.path.join(pr_dir, "02_docker_compose_prod_config.pdf")], check=True)
    print("Generated Q14 CD scripts markdown and PDFs.")

def build_q15_terraform_scripts():
    ev_dir = os.path.join(BASE_DIR, "docs.1", "evidence", "15")
    pr_dir = os.path.join(BASE_DIR, "docs.1", "print", "15")
    os.makedirs(ev_dir, exist_ok=True)
    os.makedirs(pr_dir, exist_ok=True)

    tf_files = [
        ("main.tf", "01_terraform_main_tf.md", "01_terraform_main_tf.pdf", "Kịch bản khởi tạo và cấu hình toàn bộ tài nguyên hạ tầng (Networks, Volumes, Containers)"),
        ("variables.tf", "02_terraform_variables_tf.md", "02_terraform_variables_tf.pdf", "Khai báo các biến cấu hình tham số hóa hạ tầng (Ports, Credentials, Environment)"),
        ("outputs.tf", "03_terraform_outputs_tf.md", "03_terraform_outputs_tf.pdf", "Định nghĩa các đầu ra thông tin hạ tầng sau khi triển khai (Live URLs, API Docs, Monitoring Endpoints)"),
        ("terraform.tfvars.example", "04_terraform_tfvars_example.md", "04_terraform_tfvars_example.pdf", "Tệp cấu hình biến mẫu cho môi trường Production / Staging")
    ]

    for orig_name, md_name, pdf_name, desc in tf_files:
        orig_path = os.path.join(BASE_DIR, "terraform", orig_name)
        if os.path.exists(orig_path):
            with open(orig_path, "r", encoding="utf-8") as f:
                code_content = f.read().strip()
        else:
            code_content = "# File not found"

        md_content = f"""# BẢN IN KỊCH BẢN HẠ TẦNG TERRAFORM IAAC: `{orig_name}`

## Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS (HCMUS-LDMS)

---

### THÔNG TIN TỆP NGUỒN (FILE CONTROL)

| Trường thông tin | Nội dung chi tiết |
|---|---|
| **Tên tệp tin (File Name):** | `{orig_name}` |
| **Đường dẫn trong Repo (Path):** | `terraform/{orig_name}` |
| **Công nghệ:** | HashiCorp Terraform (Infrastructure as Code - IaC) |
| **Mô tả chức năng:** | {desc} |

---

## 1. Toàn văn mã nguồn kịch bản `terraform/{orig_name}`

```hcl
{code_content}
```
"""
        md_file = os.path.join(ev_dir, md_name)
        with open(md_file, "w", encoding="utf-8") as f:
            f.write(md_content)
        subprocess.run(["python", MD_TO_PDF, md_file, os.path.join(pr_dir, pdf_name)], check=True)

    print("Generated Q15 Terraform IaC scripts markdown and PDFs.")

if __name__ == "__main__":
    build_q13_ci_script()
    build_q14_cd_scripts()
    build_q15_terraform_scripts()
    print("\nAll source code markdown and PDF documents generated successfully!")
