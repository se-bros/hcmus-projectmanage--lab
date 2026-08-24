# BẢN IN KỊCH BẢN TÍCH HỢP LIÊN TỤC (CI BUILD SCRIPT)

## Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS (HCMUS-LDMS)

---

### THÔNG TIN TỆP NGUỒN (FILE CONTROL)

| Trường thông tin                  | Nội dung chi tiết                                                                                                                                                      |
| --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Tên tệp tin (File Name):**      | `ci.yml`                                                                                                                                                               |
| **Đường dẫn trong Repo (Path):**  | `.github/workflows/ci.yml`                                                                                                                                             |
| **Công cụ CI áp dụng:**           | GitHub Actions                                                                                                                                                         |
| **Mục đích:**                     | Tự động hóa kiểm tra format, linting mã nguồn Backend/Frontend, chạy suite 141 test cases Pytest, xác thực cấu hình Terraform và gửi thông báo kết quả qua email Brevo |
| **Sự kiện kích hoạt (Triggers):** | Push vào `main`, `master`, `develop`, `release/*` hoặc mở Pull Request                                                                                                 |

---

## 1. Giải thích các luồng công việc (Jobs Breakdown)

1. **`backend-tests`**: Cài đặt môi trường Python 3.12 bằng công cụ `uv`, cấu hình cache thư viện, chạy linter `ruff check .`, format `ruff format --check .` và thực thi toàn bộ suite kiểm thử `uv run pytest --maxfail=1 --disable-warnings -v`.
2. **`frontend-lint-build`**: Cài đặt Node.js 20, thực hiện cài đặt sạch `npm ci`, chạy linter `npm run lint` và biên dịch kiểm tra tính toàn vẹn `npm run build`.
3. **`terraform-validate`**: Cài đặt Terraform CLI, khởi tạo `terraform init -backend=false`, kiểm tra định dạng `terraform fmt -check` và xác thực cú pháp `terraform validate`.
4. **`notify-email`**: Thu thập trạng thái kết quả của 3 jobs trên, gửi email báo cáo chi tiết đến quản trị viên qua Brevo API / SMTP webhook.

---

## 2. Toàn văn mã nguồn kịch bản `.github/workflows/ci.yml`

```yaml
name: CI

on:
  pull_request:
    branches: [main, develop]
  push:
    branches: [main, develop, "release/**", "hotfix/**"]

jobs:
  backend:
    runs-on: ubuntu-latest
    defaults:
      run:
        working-directory: src/backend
    steps:
      - uses: actions/checkout@v4
      - uses: astral-sh/setup-uv@v3
        with:
          version: "latest"
      - run: uv sync
      - run: uv run ruff format --check .
      - run: uv run ruff check .
      - run: uv run pytest

  frontend:
    runs-on: ubuntu-latest
    defaults:
      run:
        working-directory: src/frontend
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: "20"
      - run: npm ci
      - run: npm run lint
      - run: npm run build
      - run: npm test

  terraform:
    name: Terraform IaaC
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: hashicorp/setup-terraform@v3
      - name: Validate Terraform Configuration
        working-directory: terraform
        run: |
          terraform fmt -check
          terraform init -backend=false
          terraform validate

  publish-backend-image:
    name: Build & Push Backend Image to Docker Hub
    needs: [backend]
    if: github.event_name == 'push' && (github.ref == 'refs/heads/main' || startsWith(github.ref, 'refs/heads/release/'))
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: docker/login-action@v3
        with:
          username: anhnguyen835
          password: ${{ secrets.DOCKERHUB_TOKEN }}
      - uses: docker/build-push-action@v5
        id: push
        with:
          context: src/backend
          push: true
          tags: |
            anhnguyen835/hcmus-ldms-api:latest
            anhnguyen835/hcmus-ldms-api:${{ github.sha }}
      - name: Log image link
        run: |
          echo "### Backend image published" >> "$GITHUB_STEP_SUMMARY"
          echo "- Docker Hub: https://hub.docker.com/r/anhnguyen835/hcmus-ldms-api/tags" >> "$GITHUB_STEP_SUMMARY"
          echo "- Image: \`anhnguyen835/hcmus-ldms-api:${{ github.sha }}\`" >> "$GITHUB_STEP_SUMMARY"
          echo "- Digest: \`${{ steps.push.outputs.digest }}\`" >> "$GITHUB_STEP_SUMMARY"

  notify:
    needs: [backend, frontend, terraform]
    if: always() && github.event_name == 'push' && github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    timeout-minutes: 5
    continue-on-error: true
    defaults:
      run:
        working-directory: src/backend
    steps:
      - uses: actions/checkout@v4
      - uses: astral-sh/setup-uv@v3
        with:
          version: "latest"
      - run: uv sync
      - name: Send merge notification email
        env:
          BREVO_API_KEY: ${{ secrets.BREVO_API_KEY }}
          BREVO_SENDER_EMAIL: ${{ secrets.BREVO_SENDER_EMAIL }}
          GITHUB_REPOSITORY: ${{ github.repository }}
          GITHUB_REF_NAME: ${{ github.ref_name }}
          GITHUB_SHA: ${{ github.sha }}
          GITHUB_SERVER_URL: ${{ github.server_url }}
          GITHUB_RUN_ID: ${{ github.run_id }}
          COMMIT_MESSAGE: ${{ github.event.head_commit.message }}
          COMMIT_AUTHOR: ${{ github.event.head_commit.author.name }}
          JOB_STATUSES: '{"backend":"${{ needs.backend.result }}","frontend":"${{ needs.frontend.result }}","terraform":"${{ needs.terraform.result }}"}'
        run: uv run python -m app.scripts.send_merge_notification
```
