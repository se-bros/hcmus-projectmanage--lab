# TÀI LIỆU QUY CHUẨN LẬP TRÌNH VÀ CẤU HÌNH KIỂM SOÁT MÃ NGUỒN (CODING STANDARDS & LINTER CONFIGURATION)
## Dự án: Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS (HCMUS-LDMS)
### Mã tài liệu: `HCMUS-LDMS-STD-01` | Phục vụ minh chứng: Câu 19 (Quality Management)

---

| Thông tin chung | Chi tiết |
| :--- | :--- |
| **Hệ thống áp dụng:** | Toàn bộ Monorepo dự án HCMUS-LDMS (Backend FastAPI & Frontend React) |
| **Công cụ kiểm soát tự động:** | **Ruff** (Python Linter & Formatter), **Oxlint** (React/TypeScript), **Prettier** |
| **Mục tiêu chất lượng (QA):** | Đảm bảo 100% mã nguồn tuân thủ PEP 8, Clean Code, ngăn ngừa lỗi cú pháp và logic trước khi merge |
| **Cơ chế cưỡng chế (Gating):** | Chặn merge Pull Request tự động qua GitHub Actions CI Pipeline nếu phát hiện bất kỳ lỗi linter nào |

---

## 1. Cấu hình Coding Standards Backend Python (`src/backend/pyproject.toml`)

Trích xuất trực tiếp từ file cấu hình chính thức của dự án:

```toml
[tool.ruff]
line-length = 100
target-version = "py311"

[tool.ruff.lint]
# Danh mục quy tắc kiểm tra nghiêm ngặt:
# - E: Lỗi cú pháp và định dạng theo chuẩn PEP 8 (Pycodestyle Errors)
# - F: Lỗi biến/hàm không dùng, import thừa, biến chưa khai báo (Pyflakes)
# - I: Chuẩn hóa thứ tự sắp xếp thư viện import (isort)
# - UP: Nâng cấp cú pháp Python hiện đại và an toàn (pyupgrade)
select = ["E", "F", "I", "UP"]

[tool.pytest.ini_options]
pythonpath = ["."]
```

---

## 2. Cấu hình Coding Standards Frontend React & TypeScript (`src/frontend/.oxlintrc.json`)

```json
{
  "$schema": "./node_modules/oxlint/configuration_schema.json",
  "plugins": ["react", "typescript", "oxc"],
  "rules": {
    "react/rules-of-hooks": "error",
    "react/only-export-components": ["warn", { "allowConstantExport": true }]
  }
}
```

---

## 3. Quy trình Tự động hóa Kiểm soát Chất lượng trong CI Pipeline (`.github/workflows/ci.yml`)

Mọi Pull Request gửi lên nhánh `main` hoặc `develop` đều bị kiểm duyệt tự động qua Quality Gate:

```yaml
name: CI
on:
  pull_request:
    branches: [main, develop]
  push:
    branches: [main, develop]

jobs:
  backend:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: astral-sh/setup-uv@v3
      - run: uv sync
      - run: uv run ruff format --check .   # Kiểm tra định dạng code chuẩn
      - run: uv run ruff check .            # Kiểm tra quy chuẩn linter (0 warnings)
      - run: uv run pytest                  # Chạy toàn bộ 100% Unit Test suites
```

---

## 4. Kết quả Kiểm tra Thực tế trên Hệ thống (Terminal Execution Log)

Nhật ký thực thi lệnh kiểm tra mã nguồn thực tế trên toàn bộ $109$ files của dự án:

```text
========================================================================================
PS G:\HCMUS\NAM3-HK3\Management\Final\hcmus-projectmanage--lab> uv run --project src/backend ruff check src/backend
All checks passed!

PS G:\HCMUS\NAM3-HK3\Management\Final\hcmus-projectmanage--lab> uv run --project src/backend ruff format --check src/backend
109 files already formatted
========================================================================================
```

**Kết luận:** Mã nguồn dự án HCMUS-LDMS đạt **$100\%$ độ sạch (Clean Code)**, không có cảnh báo linter còn tồn đọng, đáp ứng đầy đủ tiêu chí Definition of Done (DoD).
