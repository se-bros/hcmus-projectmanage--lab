# NHẬT KÝ QUYẾT ĐỊNH VÀ HỒ SƠ QUYẾT ĐỊNH KIẾN TRÚC

## Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS (HCMUS-LDMS)

### Thông tin tài liệu

| Trường | Nội dung |
|---|---|
| Mã tài liệu | `HCMUS-LDMS-ADR` |
| Chủ sở hữu | Solution Architect — Ân Tiến Nguyên An |
| Người điều phối | Project Manager — Mạch Quốc Tấn |
| Phiên bản | 1.0 — 22/08/2026 |
| Trạng thái | Baseline tài liệu; các quyết định kỹ thuật vẫn cần PoC/evidence như ghi tại từng ADR |

## Mục lục

- [1. Mục đích và quy tắc](#1-mục-đích-và-quy-tắc)
- [2. Decision Log](#2-decision-log)
- [3. ADR-001 Kiến trúc modular monolith](#3-adr-001-kiến-trúc-modular-monolith)
- [4. ADR-002 Xử lý OCR và EPUB bằng job nền](#4-adr-002-xử-lý-ocr-và-epub-bằng-job-nền)
- [5. ADR-003 Tách PostgreSQL và object storage](#5-adr-003-tách-postgresql-và-object-storage)
- [6. ADR-004 PostgreSQL full-text search cho MVP](#6-adr-004-postgresql-full-text-search-cho-mvp)
- [7. ADR-005 RBAC phía máy chủ và tệp riêng tư](#7-adr-005-rbac-phía-máy-chủ-và-tệp-riêng-tư)
- [8. ADR-006 Local và demo cloud là hai profile](#8-adr-006-local-và-demo-cloud-là-hai-profile)
- [9. ADR-007 Trunk-Based Development](#9-adr-007-trunk-based-development)
- [10. ADR-008 Evidence-first completion](#10-adr-008-evidence-first-completion)
- [11. ADR-009 Bộ dữ liệu mẫu thay vì sản lượng quy mô lớn](#11-adr-009-bộ-dữ-liệu-mẫu-thay-vì-sản-lượng-quy-mô-lớn)
- [12. ADR-010 Chưa chọn production topology](#12-adr-010-chưa-chọn-production-topology)
- [13. Quy trình thay thế quyết định](#13-quy-trình-thay-thế-quyết-định)

## 1. Mục đích và quy tắc

Tài liệu lưu lý do, lựa chọn thay thế, hệ quả và điều kiện kiểm chứng của các quyết định ảnh hưởng nhiều thành phần. `Chấp nhận cho đường cơ sở` nghĩa là quyết định được dùng để giữ tài liệu nhất quán; không có nghĩa triển khai hoặc PoC đã hoàn thành.

Trạng thái dùng trong tài liệu:

- `Đề xuất`: đang xem xét.
- `Chấp nhận cho đường cơ sở`: nguồn chuẩn hiện hành của bộ hồ sơ.
- `Đã kiểm chứng`: có evidence kỹ thuật được liên kết.
- `Đã thay thế`: đã được ADR mới thay thế.
- `Đã bác bỏ`: không dùng, nhưng giữ lý do.

ADR không được sửa để xóa lịch sử quyết định. Khi đổi hướng, tạo ADR mới và đánh dấu ADR cũ `Đã thay thế`.

## 2. Decision Log

| ADR | Quyết định | Trạng thái | Owner | Evidence/điều kiện còn thiếu |
|---|---|---|---|---|
| ADR-001 | Modular monolith cho MVP | Chấp nhận cho đường cơ sở | Solution Architect | Review module boundaries và testability |
| ADR-002 | OCR/EPUB chạy job nền có trạng thái/retry | Chấp nhận cho đường cơ sở | Backend Lead | PoC restart/timeout/retry |
| ADR-003 | PostgreSQL lưu metadata; object storage lưu source/EPUB | Chấp nhận cho đường cơ sở | Solution Architect | Integrity/restore test |
| ADR-004 | PostgreSQL full-text search cho MVP | Chấp nhận cho đường cơ sở | Backend Lead | Dataset và performance measurement |
| ADR-005 | Server-side RBAC; private storage; URL tạm thời | Chấp nhận cho đường cơ sở | Backend Lead | Authorization/security test |
| ADR-006 | Local là nguồn phát triển; cloud là profile demo có điều kiện | Chấp nhận cho đường cơ sở | DevOps Lead | Cloud smoke test |
| ADR-007 | Trunk-Based với nhánh task ngắn | Chấp nhận cho đường cơ sở | PM + Technical Leads | Git/CI evidence |
| ADR-008 | Chỉ Done khi có evidence | Chấp nhận cho đường cơ sở | PM + QA | Completion event đầu tiên đủ evidence |
| ADR-009 | Nghiệm thu bằng dataset mẫu có quyền | Chấp nhận cho đường cơ sở | PM + nghiệp vụ | Dataset Register được duyệt |
| ADR-010 | Không tuyên bố production topology trong MVP | Chấp nhận cho đường cơ sở | PM + Architect | Business case/threat model sau MVP |

## 3. ADR-001 Kiến trúc modular monolith

**Bối cảnh:** Nhóm có 6 sinh viên, 11 tuần và 190 giờ-người demand. Microservices làm tăng triển khai, quan sát, consistency và vận hành.

**Quyết định:** Dùng một backend FastAPI có các mô-đun theo domain, frontend React/TypeScript và ranh giới API–nghiệp vụ–dữ liệu rõ.

**Lựa chọn đã xem xét:** microservices; ghép DSpace; ứng dụng nguyên khối không phân mô-đun.

**Hệ quả tích cực:** ít deployment unit; dễ setup; transaction và debug đơn giản hơn.

**Đánh đổi:** lỗi tiến trình có thể ảnh hưởng nhiều mô-đun; cần kỷ luật import/boundary; worker nền có thể phải tách sau.

**Điều kiện xem lại:** tải/concurrency hoặc chu kỳ phát hành chứng minh cần tách; module coupling ngăn kiểm thử độc lập.

## 4. ADR-002 Xử lý OCR và EPUB bằng job nền

**Bối cảnh:** OCR và tạo EPUB có thể kéo dài; chạy đồng bộ sẽ giữ request và làm trải nghiệm không tin cậy.

**Quyết định:** API tạo job có `pending/processing/completed/failed`, attempt, lỗi và quan hệ với document. MVP có thể chạy worker cùng backend nếu PoC đạt.

**Lựa chọn đã xem xét:** chạy đồng bộ; queue/worker riêng từ đầu; dịch vụ OCR bên ngoài.

**Hệ quả:** UI theo dõi được trạng thái và retry; cần timeout, recovery và idempotency. Mô hình cùng backend không được coi là queue production bền vững.

**Điều kiện xác minh:** restart khi đang xử lý, timeout, retry nhiều lần, job trùng và bảo toàn source/corrected text.

## 5. ADR-003 Tách PostgreSQL và object storage

**Bối cảnh:** Metadata/trạng thái cần truy vấn quan hệ; PDF/ảnh/EPUB lớn không phù hợp lưu trực tiếp trong bảng cho MVP.

**Quyết định:** PostgreSQL lưu record, quyền, job, metadata và object key/version/hash; MinIO dùng local, Cloudflare R2 dùng demo cloud cho binary object private.

**Hệ quả:** linh hoạt môi trường và không phình database; đổi lại phải giữ consistency giữa database và object storage, có cleanup/reconciliation và restore mapping.

**Điều kiện xác minh:** upload thất bại giữa chừng, object orphan, record trỏ object thiếu, hash mismatch và restore.

## 6. ADR-004 PostgreSQL full-text search cho MVP

**Bối cảnh:** Chưa có dữ liệu chứng minh cần Elasticsearch/OpenSearch; thêm dịch vụ tìm kiếm sẽ tăng phạm vi.

**Quyết định:** Dùng khả năng full-text search của PostgreSQL và lọc quyền trong truy vấn phía máy chủ.

**Hệ quả:** giảm thành phần vận hành; khả năng ranking/ngôn ngữ/quy mô có giới hạn. Không công bố ngưỡng tốc độ khi chưa đo DS-07.

**Điều kiện xem lại:** P95 không đạt ngưỡng UAT trên dataset được chốt; yêu cầu ranking/fuzzy/search scale vượt PostgreSQL.

## 7. ADR-005 RBAC phía máy chủ và tệp riêng tư

**Bối cảnh:** Ẩn nút ở frontend không bảo vệ API hoặc object URL.

**Quyết định:** Backend kiểm tra session/role/permission ở mọi thao tác protected. Bucket private; chỉ backend tạo quyền truy cập tạm thời sau authorization. Draft/private bị lọc khỏi search.

**Hệ quả:** chính sách tập trung và kiểm thử được; cần role matrix, expiry/revocation và audit cho hành động quan trọng. Không tuyên bố DRM tuyệt đối.

**Điều kiện xác minh:** direct API, object URL ẩn danh/hết hạn, đổi role, draft search và broken-object-level authorization tests.

## 8. ADR-006 Local và demo cloud là hai profile

**Bối cảnh:** Repository có Docker Compose/PostgreSQL/MinIO; tài liệu đề xuất Vercel/Render/Neon/R2 cho demo. Hai profile phục vụ mục đích khác nhau.

**Quyết định:** Local là nguồn chuẩn để phát triển/test. Demo cloud chỉ được gọi là sẵn sàng sau deploy/smoke. Production/on-premise không suy ra từ demo.

**Hệ quả:** giảm mâu thuẫn và có fallback trình diễn; phải giữ cấu hình tương thích, secrets riêng và không dùng kết quả local thay cloud evidence.

**Điều kiện xác minh:** clean local setup và cloud smoke cùng build/config schema.

## 9. ADR-007 Trunk-Based Development

**Bối cảnh:** Nhóm nhỏ và lịch ngắn; nhánh dài/GitFlow làm tăng merge delay.

**Quyết định:** `main` là nhánh tích hợp; dùng `task/LDMS-xxx-mo-ta` hoặc `fix/mo-ta` ngắn; merge khi review/test phù hợp đạt.

**Hệ quả:** feedback nhanh và ít divergence; yêu cầu thay đổi nhỏ, main ổn định, branch protection/CI khi khả dụng.

**Điều kiện xem lại:** repository/giảng viên áp đặt quy trình khác hoặc compliance cần release branch.

## 10. ADR-008 Evidence-first completion

**Bối cảnh:** Effort log cũ nhắc nhiều story nhưng không đủ PR/test/UAT; cộng điểm lặp làm sai throughput.

**Quyết định:** Effort và completion là hai loại record. Story chỉ Done khi có PR/commit, test evidence, reviewer, AC và xác nhận nghiệp vụ khi cần.

**Hệ quả:** số liệu trung thực nhưng completed scope ban đầu có thể thấp; phải duy trì Evidence Index và không hồi tố thiếu căn cứ.

**Điều kiện xác minh:** Completion Register có event đủ trường và audit ngẫu nhiên mở được artifact.

## 11. ADR-009 Bộ dữ liệu mẫu thay vì sản lượng quy mô lớn

**Bối cảnh:** Baseline không có nguồn lực/quyền để cam kết 500/2.000 tài liệu.

**Quyết định:** Nghiệm thu luồng trên bộ mẫu có quyền, đủ loại để kiểm tra happy path, lỗi, OCR, search và authorization.

**Hệ quả:** phù hợp dự án môn học nhưng không chứng minh quy mô production. Dataset phải có source, permission, hash và ground truth khi đo OCR.

**Điều kiện xem lại:** có dự án triển khai thật, ngân sách, owner dữ liệu và kế hoạch số hóa được phê duyệt.

## 12. ADR-010 Chưa chọn production topology

**Bối cảnh:** Demo cloud không bao quát HA, compliance, monitoring, backup, incident, capacity và cost dài hạn.

**Quyết định:** Không gọi Vercel/Render/Neon/R2 là production baseline. Production/on-premise phải có ADR/SOW riêng.

**Hệ quả:** tránh cam kết quá mức; vẫn có thể demo có kiểm soát. Không dùng từ production-ready nếu chưa có threat model, restore drill, monitoring, capacity và approval.

**Điều kiện xem lại:** sponsor/Thư viện khởi tạo giai đoạn triển khai thật.

## 13. Quy trình thay thế quyết định

1. Ghi vấn đề, nguồn và ADR bị ảnh hưởng.
2. So sánh tối thiểu hai lựa chọn theo scope, schedule, quality, security, data, operations và cost.
3. Thực hiện PoC nếu quyết định phụ thuộc giả định kỹ thuật quan trọng.
4. Solution Architect đề xuất; PM đánh giá baseline; owner nghiệp vụ/dữ liệu tham gia khi có tác động tương ứng.
5. Tạo ADR mới, cập nhật trạng thái ADR cũ và các tài liệu nguồn trong cùng Change Request.
6. Xuất lại PDF, chạy link/lint và gắn evidence.

Tài liệu liên quan: [Architecture](05-software-architecture.md), [SRS](04-software-requirements.md), [Risk Register](18-risk-management-plan.md), [Quality Plan](19-quality-management-plan.md), [Process](09-software-process-definition.md) và [Operations–Security Plan](15-devops-and-operations.md).
