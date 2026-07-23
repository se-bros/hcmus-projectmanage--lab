# Ý TƯỞNG DỰ ÁN (PROJECT IDEA)

## Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS (HCMUS-LDMS)

### THÔNG TIN TÀI LIỆU (DOCUMENT CONTROL)

| Trường thông tin (Field)                   | Nội dung đặc tả (Description)                |
| :----------------------------------------- | :------------------------------------------- |
| **Mã tài liệu (Document ID)**              | `HCMUS-LDMS-PID`                             |
| **Tên tài liệu (Document Title)**          | Ý tưởng dự án (Project Idea Document)        |
| **Dự án (Project Name)**                   | HCMUS-LDMS                                   |
| **Đơn vị soạn thảo (Author/Organization)** | Thư viện & Phòng Công nghệ Thông tin - HCMUS |
| **Người xem xét (Reviewer)**               | Trưởng phòng CNTT & Giám đốc Thư viện        |
| **Người phê duyệt (Approver)**             | Ban Giám hiệu Trường ĐH Khoa học Tự nhiên    |
| **Cấp độ bảo mật (Security Class)**        | Internal (Nội bộ trường)                     |
| **Trạng thái tài liệu (Status)**           | Under Review (Đang thẩm định)                |

### LỊCH SỬ PHIÊN BẢN (REVISION HISTORY)

| Phiên bản (Version) | Ngày phát hành (Date) | Mô tả thay đổi (Description of Change)                                      | Người thực hiện (Author) |
| :-----------------: | :-------------------: | :-------------------------------------------------------------------------- | :----------------------: |
|         1.0         |      05/07/2026       | Khởi tạo dự thảo ý tưởng ban đầu (v1.0).                                    |      Mạch Quốc Tấn       |
|         2.0         |      14/07/2026       | Chuẩn hóa cấu trúc và thuật ngữ, bổ sung định lượng thực trạng.             |      Mạch Quốc Tấn       |
|         3.0         |      15/07/2026       | Bổ sung mục 5.1 Phân tích MOAT sơ bộ (Lợi thế cạnh tranh bền vững).         |    Ân Tiến Nguyên An     |
|         4.0         |      17/07/2026       | Đồng bộ hóa tech stack đơn giản hóa mới (Google OAuth 2.0, PostgreSQL FTS). |    Ân Tiến Nguyên An     |
|         5.0         |      23/07/2026       | Loại bỏ các số liệu định lượng lý do thực hiện, tập trung vào thách thức.   |      Mạch Quốc Tấn       |

---

## Mục lục

- [1. Tên ý tưởng và Tóm tắt tổng quan](#1-tên-ý-tưởng-và-tóm-tắt-tổng-quan)
- [2. Nguồn gốc hình thành ý tưởng (Origin)](#2-nguồn-gốc-hình-thành-ý-tưởng-origin)
- [3. Vấn đề thực trạng và Cơ hội giải quyết](#3-vấn-đề-thực-trạng-và-cơ-hội-giải-quyết)
  - [3.1. Thực trạng và Vấn đề](#31-thực-trạng-và-vấn-đề)
  - [3.2. Cơ hội nâng cấp](#32-cơ-hội-nâng-cấp)
- [4. Đối tượng hưởng lợi dự kiến](#4-đối-tượng-hưởng-lợi-dự-kiến)
- [5. Giá trị cốt lõi (Core Value Proposition)](#5-giá-trị-cốt-lõi-core-value-proposition)
  - [5.1. Lợi thế cạnh tranh bền vững sơ bộ (Preliminary MOAT Analysis)](#51-lợi-thế-cạnh-tranh-bền-vững-sơ-bộ-preliminary-moat-analysis)
- [6. Các giả định quan trọng và Ràng buộc khả thi](#6-các-giả-định-quan-trọng-và-ràng-buộc-khả-thi)
- [7. Mức độ ưu tiên và Khẩn cấp sơ bộ](#7-mức-độ-ưu-tiên-và-khẩn-cấp-sơ-bộ)
- [8. Các bước tiếp theo đề xuất (Next Steps)](#8-các-bước-tiếp-theo-đề-xuất-next-steps)

---

## 1. Tên ý tưởng và Tóm tắt tổng quan

- **Tên tiếng Việt:** Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS.
- **Tên tiếng Anh:** HCMUS Library Document Management & Digitization System.
- **Mã viết tắt:** HCMUS-LDMS.
- **Ý tưởng cốt lõi:** Xây dựng một nền tảng ứng dụng Web nội bộ tích hợp quy trình số hóa khép kín nhằm chuyển đổi tài liệu học thuật (sách giáo trình, tài liệu tham khảo, bài báo khoa học) từ định dạng giấy sang định dạng sách điện tử responsive (**EPUB 3.0 reflowable**). Quy trình bao gồm các khâu: quét tài liệu (Scan), nhận dạng ký tự quang học (**Tesseract OCR**) tối ưu hóa tiếng Việt chuyên ngành, hiệu chỉnh văn bản trên giao diện phân tách màn hình (**Split-screen Editor**), đóng gói tự động, lập chỉ mục tìm kiếm toàn văn (**Full-text search**) và đọc sách trực tuyến bảo mật cho độc giả nội bộ (sinh viên, giảng viên) mà không cho phép tải file gốc.

## 2. Nguồn gốc hình thành ý tưởng (Origin)

Ý tưởng dự án xuất phát từ sự kết hợp nhu cầu nghiệp vụ của Ban Giám gốc Thư viện và năng lực công nghệ của Phòng Công nghệ Thông tin HCMUS, dựa trên 3 nền tảng:

1. **Chiến lược Đại học số ĐHQG-HCM:** Thực hiện kế hoạch chuyển đổi số giáo dục giai đoạn 2026-2030, hướng tới mục tiêu nâng cao tỷ lệ học liệu số sẵn có phục vụ học tập và nghiên cứu trực tuyến.
2. **Áp lực hạ tầng vật lý tại Thư viện cơ sở 1 (Nguyễn Văn Cừ, Q.5):** Không gian lưu trữ sách giấy tại cơ sở 1 đã hoàn toàn quá tải công suất thiết kế kho. Cần giải phóng kệ sách vật lý để cải tạo thành các không gian tự học số (Smart Learning Space) cho sinh viên.
3. **Phản hồi trải nghiệm người dùng (UX):** Khảo sát cho thấy phần lớn sinh viên sử dụng smartphone để tra cứu học liệu số, nhưng định dạng PDF scan hiện tại của thư viện không hỗ trợ tự co giãn chữ (non-responsive), gây mỏi mắt và giảm hiệu quả tiếp cận tài liệu số.

## 3. Vấn đề thực trạng và Cơ hội giải quyết

### 3.1. Thực trạng và Vấn đề

- **Xuống cấp học liệu vật lý:** Nhiều giáo trình cũ và tài liệu chuyên ngành độc bản xuất bản từ lâu tại thư viện đang bị mục nát, rách hỏng do thời tiết nóng ẩm và tần suất lật giở mượn đọc cao.
- **Khoảng cách địa lý tiếp cận tri thức:** Sinh viên học tập tại cơ sở 2 (Linh Trung - Thủ Đức) gặp khó khăn khi phải di chuyển quãng đường xa giữa hai cơ sở chỉ để mượn hoặc đọc trực tiếp các tài liệu giấy độc bản chỉ có ở cơ sở Quận 5.
- **Trải nghiệm đọc số hóa kém:** Các tài liệu số hóa hiện tại chủ yếu là PDF scan ảnh tĩnh. Việc không hỗ trợ tự động co giãn dòng (reflowable) khiến sinh viên phải zoom liên tục khi đọc trên màn hình điện thoại di động.
- **Tìm kiếm hạn chế:** Cổng tra cứu cũ chỉ hỗ trợ tìm theo tiêu đề sách hoặc tác giả, hoàn toàn không hỗ trợ tra cứu nội dung chi tiết bên trong sách (chương, định lý, công thức).

### 3.2. Cơ hội nâng cấp

- **Ứng dụng OCR nguồn mở tối ưu:** Sử dụng engine **Tesseract OCR** để tự động chuyển ảnh quét sang văn bản số hóa dạng text thô.
- **Chuyển đổi sang chuẩn EPUB 3.0:** Đóng gói văn bản sau OCR sang định dạng EPUB 3.0 reflowable, cho phép thay đổi cỡ chữ, màu nền hiển thị tối ưu trên mọi màn hình di động.
- **Lập chỉ mục toàn văn (Full-text Search):** Sử dụng công nghệ **Elasticsearch** lập chỉ mục nội dung sách số hóa, hỗ trợ tra cứu từ khóa chính xác đến từng trang sách dưới 3 giây đối với tải trọng 500 người dùng đồng thời, bảo đảm khả năng đáp ứng toàn diện yêu cầu kỹ thuật phi chức năng về hiệu năng hệ thống.
- **Kiến trúc Modular Monolith dễ mở rộng và bảo trì:** Hệ thống được thiết kế theo cấu trúc tách biệt Frontend (React) và Backend (FastAPI) qua RESTful API, phân chia các mô-đun nghiệp vụ độc lập, tuân thủ nguyên lý SOLID và DRY nhằm đảm bảo tính dễ bảo trì và sẵn sàng chuyển đổi nâng cấp sang Microservices khi quy mô sử dụng tăng cao.
- **Tối ưu hóa không gian phòng đọc:** Giải phóng 60-70% diện tích kệ sách giấy cũ của phòng đọc chính để chuyển công năng thành phòng tự học hiện đại.

## 4. Đối tượng hưởng lợi dự kiến

- **Sinh viên & Học viên:** Tiếp cận và đọc trực tuyến giáo trình chuẩn EPUB responsive mọi lúc, mọi nơi thông qua trình đọc web tích hợp an toàn.
- **Giảng viên & Nghiên cứu viên:** Dễ dàng chia sẻ, nhúng liên kết học liệu số hóa vào hệ thống quản lý học tập (LMS Moodle) phục vụ giảng dạy.
- **Thủ thư & Biên tập viên:** Sử dụng công cụ biên tập và quản lý quy trình số hóa tự động hóa cao, giảm thiểu các công việc thủ công liên quan đến mượn trả và bảo quản sách giấy.
- **Ban Giám hiệu nhà trường:** Tiết kiệm chi phí đầu tư xây dựng kho bãi vật lý mới và nâng cao các chỉ số xếp hạng đại học số của HCMUS.

## 5. Giá trị cốt lõi (Core Value Proposition)

Hệ thống HCMUS-LDMS đem lại giá trị cốt lõi duy nhất: **"Bảo tồn tri thức học thuật giấy tĩnh truyền thống sang định dạng học liệu số reflowable responsive động, thông qua một quy trình số hóa khép kín tự động và kiểm soát bản quyền số chặt chẽ bằng công nghệ DRM Signed URL với thời hạn hết hiệu lực 15 phút, chặn copy/tải lậu tệp sách gốc nhằm thỏa mãn tuyệt đối yêu cầu phi chức năng về an toàn bảo mật."**

### 5.1. Lợi thế cạnh tranh bền vững sơ bộ (Preliminary MOAT Analysis)

Ngoài giá trị cốt lõi, HCMUS-LDMS sở hữu **5 lợi thế cạnh tranh bền vững (MOAT)** khiến các giải pháp thay thế cực kỳ khó sao chép hoặc thay thế hệ thống sau khi triển khai:

1. **Nội dung độc quyền (Exclusive Content):** Kho tài liệu vật lý của Thư viện HCMUS — bao gồm giáo trình tự soạn bởi giảng viên nhà trường, tài liệu chuyên ngành độc bản, sách in nội bộ và các ấn phẩm học thuật hiếm — là **nguồn nội dung gốc mà chỉ duy nhất HCMUS sở hữu**. Không trường đại học, tổ chức hay nhà cung cấp thương mại nào có thể sao chép hoặc mua được kho tri thức vật lý này. Khi số hóa thành EPUB, nội dung độc quyền này trở thành tài sản số không thể thay thế.
2. **Chi phí chuyển đổi cao (High Switching Cost):** Hệ thống tích hợp sâu vào hạ tầng định danh Google OAuth 2.0 / Mock Auth (roadmap: Keycloak) và quy trình nghiệp vụ quản lý tài liệu hàng ngày của thư viện. Sau khi vận hành, việc chuyển sang giải pháp khác đồng nghĩa với việc phải di chuyển toàn bộ kho EPUB, chỉ mục PostgreSQL Full-Text Search (FTS), phân quyền người dùng và đào tạo lại toàn bộ đội ngũ thủ thư — tạo rào cản chuyển đổi rất lớn.
3. **Hiệu ứng mạng lưới (Network Effects):** Càng nhiều tài liệu được số hóa → càng nhiều sinh viên sử dụng hệ thống → càng nhiều sinh viên CTV tình nguyện tham gia biên tập OCR → kho học liệu số tăng trưởng nhanh hơn. Vòng lặp tích cực này tạo lợi thế tích lũy theo thời gian mà đối thủ mới không thể bắt kịp ngay.
4. **Lợi thế chi phí (Cost Advantage):** Toàn bộ công nghệ lõi sử dụng mã nguồn mở (Tesseract, FastAPI, React, PostgreSQL, MinIO) kết hợp hạ tầng server ảo hóa sẵn có của trường, tránh hoàn toàn chi phí bản quyền phần mềm thương mại và cloud hosting đắt đỏ.
5. **Lợi thế dữ liệu tích lũy (Data MOAT):** Kho EPUB reflowable được số hóa từ nguồn nội dung độc quyền nói trên, cùng chỉ mục toàn văn PostgreSQL FTS, là tài sản dữ liệu tích lũy dần theo thời gian. Mỗi cuốn sách số hóa bổ sung thêm giá trị cho cả hệ thống tìm kiếm và trải nghiệm đọc, tạo khoảng cách ngày càng lớn mà đối thủ mới không thể bắt kịp.

> **Ghi chú:** Phân tích MOAT chi tiết với đánh giá mức độ phòng thủ, chiến lược gia cố và so sánh đối chuẩn được trình bày đầy đủ trong tài liệu **Đề xuất Dự án (Project Proposal)**, mục 2.4.

## 6. Các giả định quan trọng và Ràng buộc khả thi

1. **Pháp lý (Legal):** Thẩm định việc số hóa tài liệu học tập phục vụ nội bộ nhà trường có hoàn toàn tuân thủ Khoản 1 Điều 25 Luật Sở hữu trí tuệ Việt Nam hiện hành hay không.
2. **Kỹ thuật và Khả thi Công nghệ (Technical Feasibility):** Nhóm kỹ sư CNTT của trường đủ năng lực làm chủ các công nghệ mã nguồn mở phổ biến (React, FastAPI, PostgreSQL, MinIO, Google OAuth 2.0), có tài liệu phát triển phong phú. Giả định độ chính xác nhận dạng của Tesseract OCR đối với sách in cũ đạt tối thiểu 85% để tránh làm quá tải thời gian sửa lỗi thủ công của biên tập viên.
3. **Tiến độ và Thời gian chuyển giao (Time-to-Delivery):** Đảm bảo chuyển giao tối thiểu một phiên bản MVP hoàn chỉnh với các tính năng cốt lõi nhất (Scan, OCR, Web Reader) trong vòng 12 tuần (thuộc tổng tiến độ 20 tuần) để kịp khai giảng năm học mới 2026. Công việc được song song hóa qua việc chia nhỏ các module phát triển giữa các thành viên.
4. **Chi phí và Tài nguyên hệ thống (Resource Feasibility):** Dự án tối ưu hóa chi phí bằng cách tận dụng hạ tầng ảo hóa máy chủ VMware vSphere sẵn có của trường và tuyển dụng CTV sinh viên bán thời gian đổi điểm rèn luyện, tránh phát sinh chi phí server đám mây hoặc mua bản quyền phần mềm thương mại đắt đỏ.
5. **Nhu cầu người dùng (User Demand):** Sinh viên sẵn sàng chuyển đổi thói quen từ đọc sách giấy/in ấn photocopy sang đọc trực tuyến định dạng EPUB responsive trên smartphone.
6. **Bảo mật và Rủi ro triển khai (Deployment Risk Management):** Sử dụng môi trường ảo hóa container (Docker Compose) thống nhất giữa các môi trường phát triển và vận hành thực tế nhằm giảm thiểu tối đa rủi ro cấu hình sai lệch. Triển khai các luồng kiểm thử tự động, quét mã nguồn trước khi tích hợp để ngăn chặn rò rỉ API keys hoặc thông tin nhạy cảm.

## 7. Mức độ ưu tiên và Khẩn cấp sơ bộ

- **Mức độ ưu tiên:** Cao (High Priority).
- **Mức độ khẩn cấp:** Nằm trong danh mục chuyển đổi số cấp bách của trường. Cần xây dựng phiên bản tối giản (MVP) tập trung vào luồng số hóa và đọc sách bảo mật trước thềm năm học mới 2026 để phục vụ kịp thời khóa sinh viên mới.

## 8. Các bước tiếp theo đề xuất (Next Steps)

1. Trình Ban Giám hiệu thông qua ý tưởng và phê duyệt chủ trương nghiên cứu chi tiết.
2. Lập **Đề xuất Dự án (Project Proposal)** chi tiết, tập trung vào phân tích chi phí đầu tư thiết bị quét (CapEx), chi phí vận hành (OpEx) và phân tích hiệu quả kinh tế hòa vốn (Cost-Benefit Analysis).
3. Bộ phận Pháp chế phối hợp với Thư viện dự thảo quy chế kiểm soát bản quyền tài liệu số hóa nội bộ.
4. Đóng gói quy trình công nghệ và tài liệu hướng dẫn thành bộ giải pháp chuyển giao tiêu chuẩn, chuẩn bị cho tiềm năng nhân rộng mô hình số hóa giáo trình cho các trường đại học thành viên khác trong khối ĐHQG-HCM.
