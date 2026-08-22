# BẢN MÔ TẢ CÔNG VIỆC (STATEMENT OF WORK — SOW)

## Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS (HCMUS-LDMS)

### Thông tin tài liệu

| Trường thông tin | Nội dung |
|---|---|
| Mã tài liệu | `HCMUS-LDMS-SOW` |
| Tên tài liệu | Bản mô tả công việc |
| Dự án | HCMUS-LDMS |
| Đơn vị soạn thảo | Nhóm Sebros |
| Người phụ trách | Mạch Quốc Tấn — Đại diện nhóm Sebros |
| Người xem xét | Đại diện nghiệp vụ Thư viện và đại diện Phòng Công nghệ Thông tin |
| Người phê duyệt | Các bên được chỉ định trong Mục 13 |
| Trạng thái | Chờ phê duyệt |
| Đường cơ sở | MVP môn học trong 11 tuần |

### Lịch sử phiên bản

| Phiên bản | Ngày | Mô tả thay đổi | Người thực hiện |
|---:|:---:|---|---|
| 1.0 | 24/07/2026 | Khởi tạo SOW. | Ân Tiến Nguyên An |
| 2.0 | 22/08/2026 | Tái lập đường cơ sở 11 tuần; đồng bộ 15 hạng mục Bắt buộc, dữ liệu mẫu, ngân sách môn học, kiến trúc theo môi trường và tiêu chí nghiệm thu có truy vết. | Mạch Quốc Tấn |

## Mục lục

- [1. Mục đích và hiệu lực](#1-mục-đích-và-hiệu-lực)
- [2. Các bên tham gia](#2-các-bên-tham-gia)
- [3. Đường cơ sở và phạm vi](#3-đường-cơ-sở-và-phạm-vi)
- [4. Công nghệ và môi trường](#4-công-nghệ-và-môi-trường)
- [5. Sản phẩm bàn giao](#5-sản-phẩm-bàn-giao)
- [6. Tiến độ 11 tuần](#6-tiến-độ-11-tuần)
- [7. Nguồn lực và ngân sách](#7-nguồn-lực-và-ngân-sách)
- [8. Tiêu chí nghiệm thu](#8-tiêu-chí-nghiệm-thu)
- [9. Bằng chứng và truy vết](#9-bằng-chứng-và-truy-vết)
- [10. Kiểm soát thay đổi](#10-kiểm-soát-thay-đổi)
- [11. Giả định, ràng buộc và phụ thuộc](#11-giả-định-ràng-buộc-và-phụ-thuộc)
- [12. Rủi ro và trách nhiệm xử lý](#12-rủi-ro-và-trách-nhiệm-xử-lý)
- [13. Phê duyệt](#13-phê-duyệt)
- [14. Tài liệu tham chiếu](#14-tài-liệu-tham-chiếu)

---

## 1. Mục đích và hiệu lực

Tài liệu này xác định công việc, sản phẩm bàn giao, thời gian, nguồn lực, điều kiện nghiệm thu và cơ chế kiểm soát thay đổi cho phiên bản đầu tiên của HCMUS-LDMS.

SOW chỉ có hiệu lực cam kết sau khi các bên có thẩm quyền điền đầy đủ họ tên, ngày và hình thức xác nhận tại [Mục 13](#13-phê-duyệt). Khi chưa đủ xác nhận, tài liệu ở trạng thái **Chờ phê duyệt** và được dùng để rà soát, không được trình bày như một hợp đồng đã ký.

SOW không thay thế yêu cầu phần mềm, danh mục công việc, kiến trúc hoặc kết quả kiểm thử. Khi có khác biệt, thay đổi phải được xử lý theo [Mục 10](#10-kiểm-soát-thay-đổi), không tự chọn nội dung có lợi từ nhiều phiên bản.

## 2. Các bên tham gia

| Bên/Vai trò | Đại diện | Trách nhiệm trong SOW |
|---|---|---|
| Nhà tài trợ/đơn vị phê duyệt | Đại diện Ban Giám hiệu khi được chỉ định | Phê duyệt chủ trương và thay đổi vượt thẩm quyền nhóm. |
| Chủ trì nghiệp vụ | Đại diện nghiệp vụ Thư viện | Xác nhận quy trình, dữ liệu mẫu, tiêu chí chấp nhận và kết quả nghiệp vụ. |
| Tư vấn kỹ thuật/hạ tầng | Đại diện Phòng Công nghệ Thông tin | Xem xét triển khai, bảo mật và hạ tầng khi cần. |
| Rà soát quyền tài liệu | Đại diện Pháp chế hoặc người được ủy quyền | Xác nhận điều kiện sử dụng tài liệu thật. |
| Bên thực hiện | Nhóm Sebros gồm 6 sinh viên | Phân tích, thiết kế, phát triển, kiểm thử, triển khai demo và lập tài liệu. |

Tên cá nhân của đại diện bên ngoài nhóm chỉ được điền khi có chỉ định thật. Việc để trống tên không được thay bằng chức danh kèm tuyên bố “đã ký”.

## 3. Đường cơ sở và phạm vi

### 3.1. Đường cơ sở

| Thuộc tính | Giá trị được đề xuất |
|---|---|
| Phiên bản | MVP phục vụ môn học và trình diễn có kiểm soát |
| Thời gian | 11 tuần |
| Nhân sự phát triển | 6 sinh viên kiêm nhiệm |
| Phương pháp | Kanban, luồng liên tục, giới hạn WIP |
| Phạm vi cơ sở | 15 hạng mục Bắt buộc |
| Phạm vi điều kiện | 6 hạng mục Nên có, chỉ kéo khi phạm vi cơ sở ổn định |
| Sau phạm vi cơ sở | 5 hạng mục Có thể xem xét |
| Dữ liệu | Bộ tài liệu mẫu đã xác nhận quyền sử dụng |
| Quy mô số hóa | Không cam kết số lượng sách thương mại hoặc số hóa toàn kho |

Danh sách 15 hạng mục Bắt buộc:

`LDMS-001`, `LDMS-009`, `LDMS-010`, `LDMS-002`, `LDMS-003`, `LDMS-004`, `LDMS-005`, `LDMS-026`, `LDMS-011`, `LDMS-007`, `LDMS-013`, `LDMS-015`, `LDMS-016`, `LDMS-008`, `LDMS-014`.

### 3.2. Trong phạm vi

- Chuẩn bị môi trường và cấu trúc mã nguồn thống nhất.
- Đăng nhập cho môi trường phát triển/demo và phân quyền server-side.
- Tiếp nhận PDF/ảnh hợp lệ, bảo toàn tệp gốc và quản lý trạng thái tài liệu.
- Khởi chạy, theo dõi và xem kết quả OCR theo trang.
- Hiệu chỉnh và lưu văn bản đã nhận dạng.
- Nhập thông tin mô tả tối thiểu cho tài liệu.
- Tạo EPUB, kiểm tra điều kiện và xác nhận xuất bản.
- Tìm kiếm theo thông tin mô tả và nội dung toàn văn của tài liệu đã xuất bản.
- Đọc EPUB trực tuyến và kiểm tra quyền trước khi cung cấp nội dung.
- Kiểm thử, triển khai demo, hướng dẫn sử dụng cơ bản và bàn giao tài liệu kỹ thuật.

### 3.3. Ngoài phạm vi cam kết

- Số hóa 500 hoặc 2.000 cuốn sách.
- Số hóa toàn bộ kho tài liệu Thư viện.
- Ứng dụng đọc ngoại tuyến native cho iOS/Android.
- Thanh toán, thương mại hóa hoặc bán bản quyền tài liệu.
- Tìm kiếm ngữ nghĩa/RAG, chống đạo văn hoặc tích hợp hệ thống đào tạo chưa được chấp thuận.
- Mua sắm máy quét, máy chủ hoặc phần mềm thương mại.
- Vận hành production toàn trường, pentest chính thức hoặc SLA dài hạn.
- `LDMS-019`, `LDMS-020`, `LDMS-021`, `LDMS-024`, `LDMS-025` nếu chưa có quyết định bổ sung phạm vi.

## 4. Công nghệ và môi trường

### 4.1. Công nghệ lõi

| Thành phần | Công nghệ/định hướng |
|---|---|
| Giao diện | React + TypeScript |
| API | FastAPI + Python |
| Cơ sở dữ liệu và tìm kiếm | PostgreSQL + Full-Text Search |
| OCR | Tesseract OCR |
| Tạo EPUB | Pandoc hoặc công cụ tương đương đã kiểm chứng |
| Trình đọc | Epub.js |
| Lưu trữ đối tượng | API tương thích S3 |
| Xác thực | Mock/dev token trong phát triển; Google OAuth 2.0 khi được cấu hình và chấp thuận |

### 4.2. Hồ sơ môi trường

| Môi trường | Cấu hình |
|---|---|
| Local development/test | Docker Compose, PostgreSQL, MinIO, backend và frontend chạy theo hướng dẫn repository. |
| Demo cloud | Frontend Vercel, backend Render, PostgreSQL Neon, object storage Cloudflare R2 nếu cấu hình và smoke test đạt. |
| Production/on-premise | Ngoài phạm vi; phải có kiến trúc, chi phí, bảo mật và phê duyệt riêng. |

Không được dùng kết quả chạy local để tuyên bố demo cloud hoặc production đã sẵn sàng. Mỗi môi trường phải có bằng chứng riêng.

## 5. Sản phẩm bàn giao

| Mã | Sản phẩm | Nội dung tối thiểu | Thời điểm mục tiêu |
|---|---|---|---|
| DL-01 | Mã nguồn | Frontend, backend, migration, cấu hình và lịch sử Git. | Tuần 11 |
| DL-02 | Bản dựng demo | Luồng bắt buộc có thể trình diễn trên môi trường đã chọn. | Tuần 10–11 |
| DL-03 | Cấu hình triển khai | Hướng dẫn local; cấu hình demo cloud nếu được sử dụng. | Tuần 10 |
| DL-04 | Dữ liệu mẫu | Bộ tài liệu mẫu có nguồn/quyền sử dụng được ghi nhận. | Tuần 3 |
| DL-05 | Bộ tài liệu dự án | Các tài liệu Markdown/PDF trong `docs.1` đã đồng bộ. | Liên tục, chốt tuần 11 |
| DL-06 | Hướng dẫn sử dụng | Hướng dẫn cho độc giả và người xử lý tài liệu ở mức MVP. | Tuần 10 |
| DL-07 | Bằng chứng kiểm thử | Kết quả kiểm thử, lỗi còn lại và xác nhận nghiệm thu. | Tuần 10–11 |
| DL-08 | Biên bản bàn giao | Danh sách deliverable, phiên bản, hạn chế và người nhận. | Tuần 11 |

## 6. Tiến độ 11 tuần

| Thời gian | Trọng tâm | Điều kiện kiểm tra |
|---|---|---|
| Tuần 1 | Chốt scope, DoR/DoD, môi trường và dữ liệu mẫu. | Baseline được ghi nhận; môi trường local chạy được. |
| Tuần 2–3 | Xác thực, phân quyền, upload và danh sách tài liệu. | Luồng đầu vào hoạt động đúng quyền. |
| Tuần 4–6 | OCR, kết quả theo trang và lưu hiệu chỉnh. | Tài liệu mẫu đi đến văn bản đã lưu. |
| Tuần 7–8 | Metadata, EPUB và xuất bản. | Thiếu điều kiện bị chặn; tài liệu hợp lệ được xuất bản. |
| Tuần 9–10 | Tìm kiếm, đọc và bảo vệ quyền. | Người dùng đúng quyền tìm và đọc được; quyền sai bị từ chối. |
| Tuần 11 | Hồi quy, sửa lỗi, nghiệm thu và bàn giao. | Có evidence index và biên bản/xác nhận kết quả. |

Đây là mốc điều phối, không phải Sprint cố định. Một hạng mục chỉ được ghi Done khi đạt DoD và có bằng chứng.

## 7. Nguồn lực và ngân sách

### 7.1. Nhân sự

| Vai trò | Thành viên/đầu mối |
|---|---|
| Đại diện nhóm/Project Manager | Mạch Quốc Tấn |
| Solution Architecture/Backend | Ân Tiến Nguyên An |
| Frontend | Ngô Nguyễn Thế Khoa; Nguyễn Lê Hồ Anh Khoa |
| Backend/DevOps | Nguyễn Tuấn Anh |
| QA/DevOps | Nguyễn Quang Thái |
| Xem xét nghiệp vụ | Đại diện nghiệp vụ Thư viện khi được chỉ định |

Chi tiết trách nhiệm và cơ chế thay thế xem [Hợp đồng nhóm](16-team-contract.md).

### 7.2. Ngân sách

Đường cơ sở môn học dùng **giả định 0 VNĐ tiền mặt được phê duyệt**. Công sức được theo dõi bằng giờ, không được diễn giải thành lao động miễn phí trong một dự án triển khai thật.

| Nhóm chi phí | Baseline MVP môn học | Quy tắc |
|---|---:|---|
| Nhân công sinh viên | 0 VNĐ tiền mặt; theo dõi effort | Không quy đổi thành cam kết lương. |
| Hạ tầng local/demo | 0 VNĐ nếu dùng tài nguyên/gói sẵn có | Phát sinh phí phải lập Change Request. |
| Thiết bị/số hóa quy mô lớn | Ngoài phạm vi | Lập dự toán riêng. |
| Vận hành/bảo trì production | Ngoài phạm vi | Lập business case và SOW riêng. |
| Công cụ AI trả phí | Không có hạn mức được phê duyệt trong baseline | Chỉ ghi chi phí thật khi có chứng từ/nguồn. |

## 8. Tiêu chí nghiệm thu

### 8.1. Điều kiện cấp dự án

- 15 hạng mục Bắt buộc có trạng thái Done, hoặc các bên phê duyệt danh sách ngoại lệ bằng Change Request.
- Mỗi hạng mục Done có liên kết tới thay đổi mã/tài liệu, kết quả kiểm thử và người xem xét.
- Luồng upload → OCR → hiệu chỉnh → EPUB → xuất bản → tìm kiếm → đọc chạy được trên bộ dữ liệu mẫu.
- Phân quyền được kiểm tra ở máy chủ; người không đủ quyền bị từ chối.
- Tài liệu chưa xuất bản không xuất hiện trong tìm kiếm của độc giả.
- Tệp gốc không bị ghi đè; giao diện độc giả không có nút tải trực tiếp EPUB gốc.
- Không còn lỗi Critical/High chưa có chấp thuận ngoại lệ.
- Hướng dẫn triển khai và sử dụng phản ánh đúng phiên bản bàn giao.

### 8.2. Chỉ số cần đo thay vì giả định

| Chỉ số | Cách chấp nhận |
|---|---|
| Thời gian tìm kiếm | Ghi dataset, môi trường, số lần chạy và percentile; ngưỡng được chốt trước UAT. |
| Chất lượng OCR | Ghi tài liệu mẫu, ground truth và công thức đo; không dùng tỷ lệ chưa đo. |
| Khởi động môi trường | Ghi máy, phiên bản công cụ, lệnh và thời gian thực tế. |
| Khả năng tương thích | Chốt browser/version/device matrix trước kiểm thử. |

## 9. Bằng chứng và truy vết

Mỗi hạng mục nghiệm thu phải có một dòng trong evidence index với tối thiểu:

| Trường | Nội dung |
|---|---|
| Story/Requirement | Mã `LDMS-xxx` và `YC-xx-xx`. |
| Thay đổi | Commit hoặc Pull Request. |
| Kiểm thử | Tên test, lệnh, báo cáo hoặc ảnh/chứng cứ phù hợp. |
| Môi trường | Local hoặc demo cloud và phiên bản cấu hình. |
| Kết quả | Pass/Fail/Accepted with exception. |
| Người xem xét | Thành viên review và người xác nhận nghiệp vụ khi cần. |
| Ngày | Ngày kết quả được xác nhận. |

Không dùng số token AI hoặc số commit làm bằng chứng rằng yêu cầu đã đạt.

## 10. Kiểm soát thay đổi

### 10.1. Phân loại

| Loại | Ví dụ | Người quyết định |
|---|---|---|
| Biên tập | Chính tả, liên kết, định dạng không đổi nghĩa | Chủ sở hữu tài liệu + reviewer |
| Nhỏ | Làm rõ AC, đổi thứ tự không ảnh hưởng 11 tuần/scope/cost | PM + đại diện nghiệp vụ |
| Lớn | Đổi 15 hạng mục Bắt buộc, 11 tuần, kiến trúc môi trường, quyền tài liệu hoặc ngân sách | Các bên phê duyệt SOW |

### 10.2. Quy trình

1. Ghi Change Request với lý do, nguồn và người đề xuất.
2. Phân tích tác động tới phạm vi, lịch, công sức, chi phí, chất lượng, pháp lý và tài liệu.
3. Xác định người có thẩm quyền quyết định.
4. Ghi quyết định bằng văn bản; im lặng không được coi là phê duyệt.
5. Cập nhật đồng thời SOW, Backlog, SRS, Estimate, Process và lịch sử phiên bản có liên quan.

## 11. Giả định, ràng buộc và phụ thuộc

### Giả định

- Nhóm có 6 thành viên và năng lực trung bình 4 giờ/người/tuần cho dự án.
- Có bộ tài liệu mẫu được phép dùng.
- Đại diện nghiệp vụ có thể tham gia các điểm cần xác nhận.
- Gói dịch vụ demo miễn phí/sẵn có đủ cho dữ liệu mẫu; nếu không, phải đổi cấu hình hoặc lập CR.

### Ràng buộc

- 11 tuần và lịch học của thành viên.
- Chưa có ngân sách tiền mặt được phê duyệt.
- Không phát hành tài liệu thật khi chưa xác nhận quyền.
- Hạng mục tùy chọn không được làm giảm khả năng hoàn thành phạm vi cơ sở.

### Phụ thuộc

- Chất lượng ảnh quét và OCR.
- Tài khoản OAuth/cloud và giới hạn dịch vụ.
- Khả năng review/nghiệm thu của đại diện nghiệp vụ.
- Chuỗi phụ thuộc OCR → hiệu chỉnh → EPUB → xuất bản → tìm kiếm/đọc.

## 12. Rủi ro và trách nhiệm xử lý

[Sổ đăng ký rủi ro](18-risk-management-plan.md) là nguồn chuẩn vận hành cho Risk ID, owner, trigger, response, trạng thái và residual risk. Bảng dưới đây chỉ tóm tắt các rủi ro cấp SOW; khi có khác biệt phải cập nhật Risk Register và SOW trong cùng Change Request.

| Rủi ro | Mức | Owner | Trigger | Ứng phó |
|---|:---:|---|---|---|
| Quyền tài liệu chưa rõ | Cao | PM + đại diện nghiệp vụ | Không có xác nhận nguồn/quyền | Chỉ dùng dữ liệu tự tạo hoặc đã được phép. |
| OCR không đạt | Cao | SA/Backend | PoC cho kết quả thấp hoặc job không ổn định | Giới hạn loại tài liệu, tiền xử lý, giữ human review. |
| Phạm vi vượt capacity | Cao | PM | Forecast vượt tuần 11 hoặc WIP/block tăng | Giữ 15 Bắt buộc, không kéo optional, tách story. |
| Mất job/tệp/dữ liệu | Cao | Backend/DevOps | Restart làm job treo hoặc dữ liệu không nhất quán | Recovery test, retry có kiểm soát, bảo toàn source. |
| Lỗi phân quyền | Cao | Backend + QA | Truy cập trái quyền trong test | Chặn release, sửa và chạy regression quyền. |
| Demo cloud không ổn định | Trung bình | DevOps | Quota, timeout, cold start hoặc cấu hình lỗi | Giữ local demo dự phòng và ghi hạn chế. |
| Thiếu người review | Trung bình | PM | PR/UAT chờ quá thời hạn | Điều phối reviewer thay thế và ưu tiên blocker. |

## 13. Phê duyệt

| Vai trò | Họ và tên | Hình thức xác nhận | Ngày |
|---|---|---|---|
| Đại diện Ban Giám hiệu/nhà tài trợ, nếu áp dụng |  |  |  |
| Đại diện nghiệp vụ Thư viện |  |  |  |
| Đại diện Phòng Công nghệ Thông tin, nếu áp dụng |  |  |  |
| Đại diện nhóm Sebros | Mạch Quốc Tấn |  |  |

Khi bảng chưa đủ xác nhận cần thiết, trạng thái tài liệu vẫn là **Chờ phê duyệt**.

## 14. Tài liệu tham chiếu

- [Đề xuất dự án](01-project-proposal.md)
- [Viễn cảnh và phạm vi](02-vision-and-scope.md)
- [Ủy nhiệm dự án](03-project-charter.md)
- [Yêu cầu phần mềm](04-software-requirements.md)
- [Danh mục công việc](04-product-backlog.md)
- [Kiến trúc phần mềm](05-software-architecture.md)
- [Nghiên cứu khả thi](08-feasibility-study.md)
- [Định nghĩa quy trình phát triển](09-software-process-definition.md)
- [Ước lượng dự án](10-project-estimate.md)
- [Hợp đồng nhóm](16-team-contract.md)
- [Nhật ký dự án](17-project-log.md)
- [Sổ đăng ký rủi ro](18-risk-management-plan.md)
- [Kế hoạch quản lý chất lượng](19-quality-management-plan.md)
- [Kế hoạch kiểm thử và UAT](20-test-plan.md)
- [Nhật ký quyết định và ADR](A1-decision-log-and-adr.md)
- [Kế hoạch vận hành và bảo mật](15-devops-and-operations.md)
