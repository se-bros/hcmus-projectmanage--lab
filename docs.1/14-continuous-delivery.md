# MÔ HÌNH CHUYỂN GIAO LIÊN TỤC

## Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS (HCMUS-LDMS)

### Thông tin tài liệu

| Trường | Nội dung |
|---|---|
| Mã tài liệu | `HCMUS-LDMS-CD` |
| Chủ sở hữu | DevOps — Nguyễn Tuấn Anh; Nguyễn Quang Thái |
| Phiên bản | 1.0 — 22/08/2026 |
| Trạng thái | Mô hình và runbook dự kiến; chưa có workflow CD/evidence triển khai tự động được xác minh |

## Mục lục

- [1. Mục tiêu và giới hạn](#1-mục-tiêu-và-giới-hạn)
- [2. Mô hình chuyển giao](#2-mô-hình-chuyển-giao)
- [3. Môi trường và cấu hình](#3-môi-trường-và-cấu-hình)
- [4. Các bước chuyển giao](#4-các-bước-chuyển-giao)
- [5. Phê duyệt, rollback và bằng chứng](#5-phê-duyệt-rollback-và-bằng-chứng)
- [6. Trạng thái triển khai](#6-trạng-thái-triển-khai)

## 1. Mục tiêu và giới hạn

Chuyển giao liên tục mở rộng CI để mỗi bản đạt kiểm tra có thể được đưa tới môi trường demo bằng quy trình lặp lại và có phê duyệt. Dự án không tuyên bố tự động triển khai production. Demo cloud chỉ được gọi là sẵn sàng sau smoke test.

## 2. Mô hình chuyển giao

`CI đạt → Tạo bản dựng → Kiểm tra tích hợp/bảo mật → Triển khai demo → Smoke test → Phê duyệt thủ công → Gắn phiên bản và ghi evidence`.

| Giai đoạn | Công cụ/đích dự kiến | Điều kiện ra |
|---|---|---|
| CI | GitHub Actions | Backend/frontend checks đạt |
| Bản dựng | Frontend bundle + backend image/build | Gắn commit và checksum/tag |
| Local release candidate | Docker Compose | Health/core smoke đạt |
| Demo cloud | Vercel, Render, Neon, R2 | Deploy và smoke đúng cùng build |
| Phê duyệt | PM, QA, nghiệp vụ khi cần | Gate/ngoại lệ và evidence rõ |

## 3. Môi trường và cấu hình

| Profile | Nguồn cấu hình | Vai trò |
|---|---|---|
| Local | `src/backend/docker-compose.yml` | Phát triển/tích hợp local |
| Local gần phát hành | `docker-compose.prod.yml` | Nginx, API, PostgreSQL, MinIO, MailHog, Prometheus, Grafana |
| Demo cloud | Platform settings + biến môi trường | Trình diễn có kiểm soát |

Tên biến môi trường và cấu hình schema được tài liệu hóa; giá trị secret không đưa vào Git hoặc PDF. Các giá trị mặc định phát triển như mật khẩu/JWT mẫu không được dùng cho môi trường công khai.

## 4. Các bước chuyển giao

1. Chọn commit đã qua CI và ghi Release Candidate ID.
2. Kiểm tra migration/config, dependency, known defects và backup/checkpoint.
3. Xây dựng frontend/backend từ commit đó; không sửa tay artifact sau build.
4. Triển khai local RC; chạy health, login, quyền, upload/job, search/reader smoke.
5. Nếu đưa demo cloud, cấu hình secret riêng rồi triển khai đúng build.
6. Chạy smoke trên cloud; ghi URL, thời gian, commit, người chạy và kết quả.
7. QA/PM đánh giá Quality/Test/Security gates; nghiệp vụ xác nhận khi là UAT.
8. Gắn tag/version, phát hành ghi chú và lưu evidence; nếu fail thì rollback.

## 5. Phê duyệt, rollback và bằng chứng

| Điều kiện | Hành động |
|---|---|
| CI/test/security gate fail | Không triển khai hoặc không phê duyệt |
| Health/core smoke fail | Rollback app; kiểm tra migration/data riêng |
| Lộ secret hoặc bypass quyền | Cô lập, rotate, incident response; không tiếp tục demo |
| Cloud lỗi nhưng local đã kiểm chứng | Có thể trình diễn local nếu công bố rõ profile |

Evidence cần có: workflow/run ID, build/tag, deploy log, cấu hình biến theo tên, migration, smoke report, approval, rollback record nếu có và email thông báo thực tế. Hiện bộ hồ sơ chưa có run ID/deploy log/email nên không đánh dấu Đạt.

## 6. Trạng thái triển khai

| Hạng mục | Trạng thái hiện tại |
|---|---|
| Docker Compose local | Có cấu hình trong repository; chưa xác minh bằng lần chạy trong tài liệu này |
| CI | Có workflow; chưa liên kết run evidence |
| CD workflow tự động | Chưa thấy cấu hình riêng trong repository |
| Demo Vercel/Render/Neon/R2 | Kiến trúc dự kiến; chưa có smoke evidence trong `docs.1` |
| Production deployment | Ngoài phạm vi |

Tài liệu liên quan: [CI](13-continuous-integration.md), [DevOps và vận hành](15-devops-and-operations.md), [Quality Plan](19-quality-management-plan.md), [Test Plan](20-test-plan.md) và [Architecture](05-software-architecture.md).
