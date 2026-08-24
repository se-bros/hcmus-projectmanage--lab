# BIÊN BẢN THANH TRA MÃ NGUỒN (CODE INSPECTION RECORD)

## Dự án: Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS (HCMUS-LDMS)

### Tham chiếu: Pull Request #41 (Tính năng Highlight & Ghi chú — LDMS-021)

---

| Thông tin chung                           | Chi tiết                                                           |
| :---------------------------------------- | :----------------------------------------------------------------- |
| **Mã biên bản:**                          | `HCMUS-LDMS-CIR-PR41`                                              |
| **Tên Pull Request:**                     | `feat: highlight and note in reading books (LDMS-021)`             |
| **Người lập PR (Author):**                | Khoa Nguyễn (Frontend/Backend Dev)                                 |
| **Người thanh tra (Inspector/Reviewer):** | Nguyễn Tuấn Anh (Tech Lead / QA) + GitHub Copilot AI               |
| **Thời gian thực hiện:**                  | 13/08/2026 — 14:28:41 UTC+7                                        |
| **Trạng thái kiểm duyệt:**                | **APPROVED & MERGED** vào nhánh `main`                             |
| **Công cụ hỗ trợ:**                       | GitHub Pull Requests, GitHub CLI `gh`, Ruff Linter, Pytest, Oxlint |

---

## 1. Mục tiêu và Phạm vi Thanh tra (Inspection Scope)

- **Tính năng được thanh tra:** Triển khai chức năng Highlight và Ghi chú cá nhân khi đọc tài liệu EPUB (User Story `LDMS-021`), kế thừa mô hình bảo mật của `LDMS-020` (Bookmark).
- **Quy mô thay đổi:** **27 files** (Backend API, Database Migrations, SQLAlchemy Models, Pydantic Schemas, Frontend React Components, Test Suites và Specs).

---

## 2. Danh mục Kiểm tra Tuân thủ (Inspection Checklist)

| STT | Hạng mục kiểm tra                   | Tiêu chuẩn chất lượng                               | Kết quả  | Ghi chú của Reviewer                                                                |
| :-: | :---------------------------------- | :-------------------------------------------------- | :------: | :---------------------------------------------------------------------------------- |
|  1  | **Coding Standards**                | Tuân thủ cấu hình Ruff (`pyproject.toml`) và Oxlint | **PASS** | $109$ files backend đã format chuẩn; không có unused imports.                       |
|  2  | **Data Isolation (Quyền riêng tư)** | Lọc dữ liệu theo cặp `(document_id, user_sub)`      | **PASS** | Mọi câu query `WHERE` đều ràng buộc `user_sub` của token đăng nhập.                 |
|  3  | **Database Migration**              | Migration Alembic an toàn, có rollback              | **PASS** | Đã merge 2 heads sạch (`20260812_0009`) và tạo bảng `highlights` (`20260812_0010`). |
|  4  | **Input Validation**                | Pydantic Schema giới hạn độ dài ghi chú             | **PASS** | Giới hạn `MAX_NOTE_LENGTH = 2000` ký tự; validate CFI chapter hợp lệ.               |
|  5  | **Test Coverage & Contracts**       | Có Unit Test & Contract Tests                       | **PASS** | Suite `test_highlights.py` và `ReaderPage.test.tsx` pass $100\%$.                   |
|  6  | **UI / UX & Edge Cases**            | Xử lý CFI không định vị được (Orphaned)             | **PASS** | Có tab hiển thị các highlight bị mất dấu khi đổi file EPUB.                         |

---

## 3. Nhật ký Trao đổi và Phê duyệt (Review Logs)

```text
========================================================================================
[13:28 13/8/2026] Khoa Nguyễn (Discord #project):
"https://github.com/mqt4n/hcmus-projectmanage--lab/pull/41 - @TuanAnh | HCMC dạ em gửi PR"

[13:35 13/8/2026] GitHub Copilot AI (Automated Inspection):
- Summary: Copilot reviewed 27 out of 27 changed files.
- Status: Commented & Passed CI automated workflow (Ruff check, Pytest suite, Build).

[14:10 13/8/2026] Nguyễn Tuấn Anh (Tech Lead Review):
- Inspection Comments: Đã kiểm tra tính năng CRUD highlight, CFI range overlay và ràng buộc khóa ngoại CASCADE khi xóa tài liệu. Code viết chuẩn Clean Code, cấu trúc router tách biệt rõ ràng.
- Decision: APPROVED
- Review Comment: "lgtm" (Looks good to me)
========================================================================================
```

---

## 4. Kết luận của Ban Quản lý Chất lượng

1. Pull Request #41 thỏa mãn **100% tiêu chí Definition of Done (DoD)** theo quy chế của nhóm.
2. Cho phép merge chính thức vào nhánh `main` và kích hoạt luồng CI/CD tự động thông báo qua email Brevo.

| Đại diện Tác giả (Author) | Đại diện Người kiểm duyệt (Reviewer) | Trưởng ban Quản lý Dự án (PM) |
| :-----------------------: | :----------------------------------: | :---------------------------: |
|     _(Đã ký điện tử)_     |          _(Đã ký điện tử)_           |       _(Đã ký điện tử)_       |
|      **Khoa Nguyễn**      |         **Nguyễn Tuấn Anh**          |       **Mạch Quốc Tấn**       |
