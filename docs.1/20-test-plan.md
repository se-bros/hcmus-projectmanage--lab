# KẾ HOẠCH KIỂM THỬ VÀ NGHIỆM THU NGƯỜI DÙNG

## Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS (HCMUS-LDMS)

### Thông tin tài liệu

| Trường | Nội dung |
|---|---|
| Mã tài liệu | `HCMUS-LDMS-TUP` |
| Chủ sở hữu | QA Lead — Nguyễn Quang Thái |
| Người phê duyệt kết quả UAT | Đại diện nghiệp vụ Thư viện hoặc người được ủy quyền |
| Phiên bản | 1.0 — 22/08/2026 |
| Trạng thái | Kế hoạch sẵn sàng để xem xét; toàn bộ kết quả hiện là `Chưa chạy` |
| Phạm vi | 15 hạng mục Bắt buộc và NFR liên quan của MVP 11 tuần |

## Mục lục

- [1. Mục đích và phạm vi](#1-mục-đích-và-phạm-vi)
- [2. Chiến lược kiểm thử](#2-chiến-lược-kiểm-thử)
- [3. Môi trường và dữ liệu](#3-môi-trường-và-dữ-liệu)
- [4. Điều kiện vào và ra](#4-điều-kiện-vào-và-ra)
- [5. Ma trận kiểm thử chức năng](#5-ma-trận-kiểm-thử-chức-năng)
- [6. Kiểm thử phi chức năng](#6-kiểm-thử-phi-chức-năng)
- [7. Kịch bản UAT đầu cuối](#7-kịch-bản-uat-đầu-cuối)
- [8. Quản lý lỗi và ngoại lệ](#8-quản-lý-lỗi-và-ngoại-lệ)
- [9. Evidence Index](#9-evidence-index)
- [10. Vai trò, lịch và báo cáo](#10-vai-trò-lịch-và-báo-cáo)
- [11. Truy vết và phê duyệt](#11-truy-vết-và-phê-duyệt)

## 1. Mục đích và phạm vi

Tài liệu quy định cách chứng minh HCMUS-LDMS đáp ứng yêu cầu, tiêu chí chấp nhận và điều kiện nghiệm thu. Kế hoạch bao phủ unit/component test do developer thực hiện, integration/API test, UI/end-to-end test, security/authorization test, reliability test, performance measurement, compatibility/accessibility check và UAT.

Ngoài phạm vi:

- chứng nhận production, penetration test chuyên nghiệp hoặc kiểm toán pháp lý;
- tải ở quy mô kho 500/2.000 tài liệu;
- kết luận chất lượng OCR trên dữ liệu thật khi chưa có dataset và ground truth được duyệt;
- các story Có thể xem xét nếu chưa có Change Request đưa vào baseline.

## 2. Chiến lược kiểm thử

### 2.1. Các cấp kiểm thử

| Cấp | Mục tiêu | Owner chính | Evidence tối thiểu |
|---|---|---|---|
| Unit/component | Kiểm tra logic nhỏ, validation và trạng thái UI | Developer | Lệnh chạy, report/log, commit |
| Integration/API | Kiểm tra API–database–object storage–job | Backend + QA | Request/data, expected/actual, report |
| UI/E2E | Kiểm tra luồng người dùng trên browser | Frontend + QA | Script/checklist, screenshot/video khi phù hợp |
| Security/authorization | Kiểm tra từ chối quyền, private file, secret | Backend + QA/DevOps | Negative tests, scan/log đã loại bí mật |
| Reliability/recovery | Kiểm tra retry, restart, integrity và restore | Architect + DevOps + QA | Test log, hash/version, thời gian phục hồi |
| Performance | Đo, không suy diễn, trên dataset/môi trường ghi rõ | QA + Backend | Raw result, phép tổng hợp, percentile |
| UAT | Xác nhận kết quả nghiệp vụ đầu cuối | Đại diện nghiệp vụ | Biên bản UAT có người/ngày/kết quả |

### 2.2. Nguyên tắc thiết kế test

- Mỗi AC có ít nhất một trường hợp thành công và một trường hợp lỗi/quyền khi áp dụng.
- Test case dùng ID `TC-<Story>-NN`; UAT dùng `UAT-NN`; NFR dùng `NFT-<NFR>-NN`.
- Expected result lấy từ SRS/Backlog; hành vi chưa định nghĩa được ghi `Specification Gap`, không tự đặt oracle.
- `Chưa chạy` không được đổi thành `Pass` nếu chỉ đọc code hoặc xem tài liệu.
- Test evidence phải gắn phiên bản build/commit và môi trường.
- Dữ liệu nhạy cảm, token và URL tạm thời phải được che trong evidence.

## 3. Môi trường và dữ liệu

### 3.1. Ma trận môi trường

| Môi trường | Mục đích | Cấu hình chuẩn | Trạng thái xác minh |
|---|---|---|---|
| Local | Unit, integration, phần lớn E2E | Docker Compose, PostgreSQL, MinIO, frontend/backend local | Chưa ghi smoke evidence trong tài liệu này |
| Demo cloud | Smoke, UAT trình diễn | Vercel, Render, Neon, Cloudflare R2 | Chỉ dùng khi smoke đạt; hiện `Chưa xác minh` |
| Production/on-premise | Không thuộc MVP | Chưa chốt | Ngoài phạm vi |

Mỗi báo cáo chạy phải ghi hệ điều hành, browser/version, commit/build, cấu hình dịch vụ, thời gian và dataset. Không dùng kết quả local để khẳng định demo cloud đã đạt.

### 3.2. Dataset tối thiểu cần chuẩn bị

| ID | Dữ liệu | Mục đích | Điều kiện |
|---|---|---|---|
| DS-01 | PDF/ảnh hợp lệ, chữ rõ | Happy path upload/OCR | Có nguồn và quyền sử dụng |
| DS-02 | PDF nhiều trang, chất lượng không đồng đều | Mapping trang và hiệu chỉnh | Có ground truth cho phần đo OCR |
| DS-03 | Sai loại, vượt giới hạn, tệp hỏng | Validation/error | Không chứa dữ liệu thật |
| DS-04 | Metadata hợp lệ/thiếu/sai định dạng | Metadata/publish gate | Có expected result rõ |
| DS-05 | EPUB hợp lệ và EPUB lỗi | Reader/validator | Không chứa tài liệu trái quyền |
| DS-06 | Tài liệu draft/published/private theo nhiều vai trò | Search/RBAC | Tài khoản thử có role matrix |
| DS-07 | Dataset tìm kiếm có từ khóa và quyền biết trước | Functional/performance search | Ghi số tài liệu và kích thước |

Dataset Register phải ghi nguồn, quyền, hash, ngày tạo, người duyệt và nơi lưu. Chưa có Dataset Register được xác minh tại thời điểm lập kế hoạch.

## 4. Điều kiện vào và ra

### 4.1. Điều kiện vào System Test

- Build khởi chạy được theo hướng dẫn.
- Story có AC, requirement mapping và owner/reviewer.
- Dữ liệu thử có nguồn/quyền và expected result.
- Thay đổi đã qua review phù hợp; không còn blocker ngăn chạy test.
- Môi trường và build ID được ghi nhận.

### 4.2. Điều kiện vào UAT

- 15 story Bắt buộc đạt system test, hoặc có ngoại lệ được phê duyệt.
- Không còn defect Critical/High chưa có quyết định ngoại lệ.
- Luồng đầu cuối và phân quyền đã smoke test.
- Dataset UAT được Đại diện nghiệp vụ chấp thuận.
- Người chạy, lịch, môi trường, cách ghi phản hồi và người ký đã được xác nhận.

### 4.3. Điều kiện ra

- Toàn bộ test bắt buộc có trạng thái Pass/Fail/Blocked/Chưa chạy rõ ràng.
- Requirement/Story bắt buộc có evidence hoặc ngoại lệ được ký.
- Critical/High = 0 chưa xử lý; Medium còn lại có owner và quyết định.
- UAT có kết luận Đã chấp nhận, Đã chấp nhận with Exceptions hoặc Đã bác bỏ.
- Evidence Index và Completion Register được cập nhật.

## 5. Ma trận kiểm thử chức năng

| Story | Requirements chính | Test trọng tâm | Negative/boundary bắt buộc | Trạng thái |
|---|---|---|---|---|
| LDMS-001 | YC-PN-07, YC-PN-09 | Cài đặt, khởi chạy, health/smoke | Thiếu biến môi trường, service unavailable | Chưa chạy |
| LDMS-009 | YC-HT-01, YC-HT-02 | Đăng nhập dữ liệu thử và tạo phiên | Sai/thiếu credential, session hết hạn | Chưa chạy |
| LDMS-010 | YC-HT-03, YC-HT-04, YC-PN-01 | Gán role và kiểm tra quyền server | Role thấp gọi trực tiếp API quản trị | Chưa chạy |
| LDMS-002 | YC-TL-01..03 | Upload và bảo toàn source | Sai loại, rỗng, hỏng, vượt giới hạn | Chưa chạy |
| LDMS-003 | YC-ND-01..03, YC-PN-03 | Tạo job OCR và theo dõi trạng thái | Job lỗi/timeout/restart | Chưa chạy |
| LDMS-004 | YC-ND-03, YC-ND-04 | Văn bản đúng tài liệu/trang | Mapping thiếu/sai trang | Chưa chạy |
| LDMS-005 | YC-ND-05, YC-PN-08 | Lưu, mở lại nội dung đã sửa | Lỗi save/concurrency; source không đổi | Chưa chạy |
| LDMS-011 | YC-TL-04, YC-TL-05 | CRUD metadata và gán danh mục có sẵn | Thiếu trường bắt buộc, dữ liệu sai | Chưa chạy |
| LDMS-007 | YC-PH-04 | Tạo/lưu EPUB và mở bằng reader | Nội dung lỗi; validator fail; job fail | Chưa chạy |
| LDMS-013 | YC-PH-01..03 | Publish khi đủ điều kiện | Thiếu metadata/nội dung/quyền | Chưa chạy |
| LDMS-015 | YC-TC-01..03, YC-PN-04 | Full-text search và lọc quyền | Draft/private không xuất hiện; empty query | Chưa chạy |
| LDMS-016 | YC-TC-04 | Kết quả đủ thông tin và mở đúng tài liệu | Không kết quả, lỗi API, metadata thiếu | Chưa chạy |
| LDMS-008 | YC-PH-05, YC-TC-05 | Mở/đọc EPUB responsive | EPUB lỗi, mất phiên, viewport nhỏ | Chưa chạy |
| LDMS-014 | YC-PH-06, YC-TC-06, YC-PN-02 | Chỉ người có quyền đọc; không có nút download | API/URL trực tiếp, URL hết hạn, role không đủ | Chưa chạy |
| LDMS-026 | YC-TL-06 | Danh sách và trạng thái đúng | Lọc quyền, phân trang, empty/error state | Chưa chạy |

Các story Nên có chỉ được đưa vào release khi có test riêng đạt; chúng không được dùng để thay thế evidence của 15 story Bắt buộc.

## 6. Kiểm thử phi chức năng

| ID | NFR | Phương pháp | Chỉ số/Oracle cần chốt | Trạng thái |
|---|---|---|---|---|
| NFT-01 | YC-PN-01 | Authorization matrix ở UI và gọi API trực tiếp | 100% negative case trọng yếu bị từ chối | Chưa chạy |
| NFT-02 | YC-PN-02 | Kiểm tra bucket private, signed URL và expiry | Không truy cập ẩn danh; URL hết hạn bị từ chối | Chưa chạy |
| NFT-03 | YC-PN-03 | Chạy OCR/EPUB và tương tác UI song song | UI không bị khóa; có status/error | Chưa chạy |
| NFT-04 | YC-PN-04 | Đo search trên DS-07, warm-up và nhiều lần chạy | Dataset, số lượt, P50/P95 và ngưỡng chốt trước UAT | Chưa chạy |
| NFT-05 | YC-PN-05 | Heuristic/usability checklist + UAT | Người dùng hiểu trạng thái/lỗi và hoàn thành luồng | Chưa chạy |
| NFT-06 | YC-PN-06 | Browser/device matrix | Matrix phải được chốt trước chạy | Chưa chạy |
| NFT-07 | YC-PN-07 | Review module boundaries và hướng dẫn setup | Thành viên mới chạy được theo hướng dẫn | Chưa chạy |
| NFT-08 | YC-PN-08 | Failure injection/restart/hash comparison | Source và save gần nhất không mất | Chưa chạy |
| NFT-09 | YC-PN-09 | Clean environment setup/smoke | Khởi chạy từ cấu hình repo, ghi thời gian | Chưa chạy |
| NFT-10 | YC-PN-10 | Audit trace Requirement→Story→PR→Test→UAT | Không thiếu link ở story Done | Chưa chạy |
| NFT-11 | Accessibility | Keyboard, focus, label, contrast, zoom 200% | Không có lỗi chặn luồng core | Chưa chạy |
| NFT-12 | Backup/restore | Restore drill database + object mapping | RPO/RTO demo được ghi và kết quả đạt | Chưa chạy |

Kết quả hiệu năng/OCR phải kèm raw data và cách tính. Không chốt con số đạt trước khi đại diện liên quan thống nhất dataset và ngưỡng.

## 7. Kịch bản UAT đầu cuối

| ID | Vai trò | Kịch bản | Kết quả chấp nhận | Trạng thái |
|---|---|---|---|---|
| UAT-01 | Biên tập viên | Đăng nhập, upload DS-01, theo dõi OCR | Tệp được lưu; trạng thái rõ; không mất source | Chưa chạy |
| UAT-02 | Biên tập viên | Đối chiếu trang, sửa và mở lại nội dung | Mapping đúng; thay đổi được giữ; source nguyên vẹn | Chưa chạy |
| UAT-03 | Biên tập viên | Nhập metadata, gán danh mục, kiểm tra publish | Thiếu dữ liệu bị chặn và nêu lý do | Chưa chạy |
| UAT-04 | Người có quyền xuất bản | Tạo EPUB, xác nhận và xuất bản | EPUB hợp lệ; trạng thái chuyển đúng; có audit | Chưa chạy |
| UAT-05 | Độc giả có quyền | Tìm kiếm, mở kết quả và đọc | Chỉ thấy tài liệu được phép; reader dùng được | Chưa chạy |
| UAT-06 | Người không đủ quyền | Tìm/gọi URL/API của private/draft | Không lộ metadata/nội dung/tệp | Chưa chạy |
| UAT-07 | Biên tập viên | Job OCR/EPUB thất bại rồi retry | Lỗi rõ; retry truy vết được; dữ liệu không mất | Chưa chạy |
| UAT-08 | Quản trị viên | Gán role và kiểm tra quyền mới | Quyền có hiệu lực đúng; hành động được ghi nhận | Chưa chạy |

Mỗi kịch bản ghi người chạy, ngày, build, môi trường, dataset, actual result, defect liên quan và chữ ký/xác nhận. Bảng trên là kế hoạch, không phải kết quả.

## 8. Quản lý lỗi và ngoại lệ

| Mức | Định nghĩa | Quy tắc release |
|---|---|---|
| Critical | Mất dữ liệu, lộ dữ liệu/tệp nghiêm trọng, hệ thống core không dùng được | Không release/UAT |
| High | Hỏng story Bắt buộc, bypass quyền, sai dữ liệu đáng kể | Phải sửa hoặc ngoại lệ có thẩm quyền |
| Medium | Có workaround, ảnh hưởng cục bộ | Có owner, target và đánh giá tác động |
| Low | Trình bày/tiện ích nhỏ | Có thể đưa backlog nếu không ảnh hưởng AC |

Ngoại lệ phải ghi defect/test ID, phạm vi ảnh hưởng, rủi ro tồn dư, workaround, thời hạn và người chấp nhận. Developer không tự chấp nhận ngoại lệ bảo mật, dữ liệu hoặc nghiệp vụ.

## 9. Evidence Index

| Evidence ID | Story/NFR | Build/commit | Test report | Môi trường/dataset | Kết quả | Reviewer/UAT | Trạng thái |
|---|---|---|---|---|---|---|---|
| Chưa có evidence được xác minh | Chưa ghi nhận | Chưa ghi nhận | Chưa ghi nhận | Chưa ghi nhận | Chưa chạy | Chưa ghi nhận | Đang theo dõi |

Evidence ID dùng định dạng `EVD-YYYYMMDD-NN`. Artifact có thể là report máy, raw log đã che bí mật, screenshot, video ngắn, biên bản hoặc link CI. Chỉ link tồn tại và truy cập được mới được ghi.

## 10. Vai trò, lịch và báo cáo

| Hoạt động | R | A | C/I |
|---|---|---|---|
| Test design và evidence index | QA Lead | PM | Developer, nghiệp vụ |
| Unit/component test | Developer | Technical Lead | QA |
| Integration/security/recovery | Backend/DevOps/QA | Solution Architect | PM |
| UAT preparation | QA + PM | Đại diện nghiệp vụ | Nhóm |
| UAT decision | Đại diện nghiệp vụ | Đại diện nghiệp vụ | PM, QA |

- Tuần 2–3: chốt dataset, test design và PoC.
- Tuần 4–9: kiểm thử liên tục theo card; regression sau tích hợp.
- Tuần 9: chốt browser/device matrix, UAT dataset và ngưỡng NFR.
- Tuần 10: system test, security/recovery và defect triage.
- Tuần 11: UAT, regression cuối, evidence audit và release decision.

## 11. Truy vết và phê duyệt

Nguồn yêu cầu: [SRS](04-software-requirements.md), [Backlog](04-product-backlog.md), [Architecture](05-software-architecture.md), [SOW](12-statement-of-work.md), [Quality Plan](19-quality-management-plan.md) và [Operations–Security Plan](15-devops-and-operations.md).

| Vai trò | Người | Quyết định | Ngày |
|---|---|---|---|
| QA Lead | Nguyễn Quang Thái | Chờ xem xét kế hoạch | Chưa xác nhận |
| Project Manager | Mạch Quốc Tấn | Chờ xem xét kế hoạch | Chưa xác nhận |
| Đại diện nghiệp vụ Thư viện | Chưa chỉ định bằng tên | Chờ duyệt UAT | Chưa xác nhận |
