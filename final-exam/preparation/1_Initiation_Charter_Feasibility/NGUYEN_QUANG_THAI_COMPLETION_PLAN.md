# KẾ HOẠCH HOÀN THÀNH PHẦN CỦA NGUYỄN QUANG THÁI

**Dự án:** HCMUS-LDMS  
**Môn học:** Quản lý Dự án Phần mềm  
**Thành viên:** Nguyễn Quang Thái - MSSV 23127116  
**Phạm vi:** Câu 1, Câu 3, Câu 8  
**Phiên bản:** 1.0  
**Ngày lập:** 20/08/2026  
**Trạng thái:** Kế hoạch hành động ưu tiên khẩn cấp

## Mục lục

- [1. Kết quả cần đạt](#1-kết-quả-cần-đạt)
- [2. Hiện trạng và khoảng trống](#2-hiện-trạng-và-khoảng-trống)
- [3. Nguồn sự thật và bộ dữ kiện phải khóa](#3-nguồn-sự-thật-và-bộ-dữ-kiện-phải-khóa)
- [4. Kế hoạch cứu hạn trước 20:00](#4-kế-hoạch-cứu-hạn-trước-2000)
- [5. Kế hoạch hoàn thiện theo từng câu](#5-kế-hoạch-hoàn-thiện-theo-từng-câu)
- [6. Kế hoạch đọc chéo, in ấn và thi thử](#6-kế-hoạch-đọc-chéo-in-ấn-và-thi-thử)
- [7. Tiêu chí hoàn thành](#7-tiêu-chí-hoàn-thành)
- [8. Checklist bàn giao cá nhân](#8-checklist-bàn-giao-cá-nhân)
- [9. Tài liệu nguồn](#9-tài-liệu-nguồn)

## 1. Kết quả cần đạt

Nguyễn Quang Thái phải hoàn thành một bộ ôn tập có thể dùng ngay trong phòng thi cho ba câu được phân công:

| Câu | Chủ đề | Sản phẩm phải hoàn thành | Bản in bắt buộc |
| :--: | :--- | :--- | :--- |
| 1 | Đề xuất dự án (Project Proposal) | Dàn ý WHAT-HOW-WHY-EVIDENCE, sơ đồ hình thành và đánh giá, 15 câu FAQ | `02-project-proposal.md` |
| 3 | Điều lệ dự án (Project Charter) | Dàn ý WHAT-HOW-WHY-EVIDENCE, sơ đồ quyền hạn/RACI, 5 câu FAQ | `04-project-charter.md` |
| 8 | Báo cáo tính khả thi (Feasibility Study) | Dàn ý WHAT-HOW-WHY-EVIDENCE, sơ đồ TELOS, 5 câu FAQ | `03-feasibility-study.md` |

Mục tiêu chất lượng là trả lời được trong 5-10 phút, tự viết được khung trả lời trên một tờ A4 trong 10 phút mà không dùng tài liệu, và chọn đúng bản in trong 2 phút.

## 2. Hiện trạng và khoảng trống

Tại thời điểm rà soát khoảng 19:20 ngày 20/08/2026, hạn soạn đề cương cá nhân là 20:00 cùng ngày. Phiếu bài làm hiện có:

- 37 vị trí trả lời còn trống, gồm 12 mục WHAT-HOW-WHY-EVIDENCE và 25 câu FAQ.
- 3 sơ đồ mới ở mức khung gợi ý, chưa được cá nhân hóa thành sơ đồ có thể tự vẽ lại.
- 3 mục bản in chưa được xác nhận.
- Các tài liệu nguồn đã có sẵn, vì vậy nút thắt nằm ở tổng hợp, thống nhất số liệu, diễn đạt và luyện phản xạ, không phải nghiên cứu lại từ đầu.

Mức ưu tiên thực hiện:

1. Hoàn thành đủ nội dung ba câu trước.
2. Sửa các mâu thuẫn số liệu và gắn dẫn chứng.
3. Rút gọn thành bản có thể viết trong 10 phút.
4. In, đánh số và luyện vấn đáp.

## 3. Nguồn sự thật và bộ dữ kiện phải khóa

### 3.1. Thứ tự ưu tiên nguồn

Khi dữ kiện không thống nhất, sử dụng thứ tự sau:

1. Phiên bản mới nhất của các tài liệu thực hành trong `docs/01-initiation/`.
2. Tài liệu bài giảng `materials/02_software_project.md` và `materials/03_software_project_initiation.md` cho định nghĩa, cấu trúc chuẩn.
3. `note.md` cho lời dặn của giảng viên và câu chuyện thực tế.
4. Phiếu bài làm cá nhân chỉ dùng như checklist, không dùng làm nguồn số liệu khi khác tài liệu gốc.

Mọi câu trả lời phải tách rõ:

- **Sự kiện đã được tài liệu ghi nhận:** số liệu, vai trò, công nghệ, KPI, lịch trình, revision history.
- **Hoạt động cần xác nhận:** phê duyệt thật, chữ ký thật, biên bản review, khảo sát gốc hoặc kết quả sử dụng thật chưa có bằng chứng trong repository.

### 3.2. Bộ dữ kiện cốt lõi

| Nhóm | Dữ kiện nên sử dụng khi trả lời |
| :--- | :--- |
| Bài toán | Kho Quận 5 quá tải; tài liệu xuống cấp; sinh viên Thủ Đức phải di chuyển khoảng 15 km; PDF scan khó đọc trên điện thoại |
| Giải pháp | Scan -> Tesseract OCR -> hiệu chỉnh Split-screen -> Pandoc/EPUB 3.0 -> PostgreSQL FTS -> Web Reader bảo mật |
| Công nghệ hiện hành | React 18, FastAPI, PostgreSQL FTS, MinIO, Google OAuth 2.0/Mock Auth, Tesseract OCR, Pandoc, Docker Compose |
| Đối chuẩn | HCMUS-LDMS so với Lạc Việt Vebrary, DSpace và chuỗi công cụ rời Abbyy + Calibre + Drive |
| Charter | Sponsor là Ban Giám hiệu; PM là Trưởng phòng CNTT; 20 tuần; MVP tuần 12; RACI cho 6 gói công việc |
| Nguồn lực | 4 kỹ sư CNTT kiêm nhiệm 50%, 2 cán bộ thư viện, 10-15 sinh viên cộng tác viên, 3 máy chủ ảo hóa |
| KPI | OCR tối thiểu 85%; tìm kiếm dưới 3 giây; mức hài lòng tối thiểu 85%; số hóa 500 sách CNTT theo phạm vi bàn giao |
| Tài chính | CapEx 75-95 triệu VNĐ; OpEx 15-30 triệu VNĐ/năm; kịch bản cơ sở 75 triệu CapEx và 15 triệu OpEx/năm |
| Bảo mật | Signed URL hết hạn sau 15 phút; hạn chế tải tệp gốc; chỉ phục vụ người dùng nội bộ theo quy chế bản quyền |
| Khả thi | TELOS là lõi 5 mặt: Technical, Economic, Legal, Operational, Schedule; báo cáo dự án mở rộng thêm Market, Resource, Cultural |

### 3.3. Mâu thuẫn phải xử lý trước khi học thuộc

| Vấn đề | Dữ kiện không thống nhất | Quyết định dùng khi trả lời |
| :--- | :--- | :--- |
| Chi phí | Phiếu gợi ý nêu 18,5 triệu; tài liệu khả thi và Charter nêu CapEx 75-95 triệu, OpEx 15-30 triệu/năm | Dùng số liệu trong Feasibility Study và Charter; không nhắc 18,5 triệu nếu chưa có tài liệu nguồn mới xác nhận |
| Hiệu năng tìm kiếm | Phiếu gợi ý nêu dưới 2 giây; tài liệu gốc nêu dưới 3 giây | Dùng dưới 3 giây |
| Công nghệ tìm kiếm | Một đoạn cũ còn nhắc Elasticsearch; các revision mới chuyển sang PostgreSQL FTS | Dùng PostgreSQL FTS và nói đây là phương án đã được đồng bộ hóa |
| Hòa vốn | Tiêu chí đặt mục tiêu trong 3 năm; phần tính toán cho 3,75 năm ở kịch bản cơ sở và 2,5-3,8 năm khi tính lợi ích dài hạn | Trình bày đây là điểm cần thẩm định lại; không khẳng định chắc chắn đạt dưới 3 năm |
| Trạng thái phê duyệt | Charter có câu ủy quyền chính thức nhưng trạng thái là Under Review và bảng chữ ký còn trống | Nêu chức năng của Charter là ủy quyền; chỉ khẳng định đã phê duyệt nếu có bản ký thật |
| Pháp lý | Tài liệu dùng câu khẳng định mạnh về quyền số hóa | Trình bày là khả thi có điều kiện, cần Pháp chế thẩm định và giới hạn tài liệu được phép số hóa |

## 4. Kế hoạch cứu hạn trước 20:00

Nếu bắt đầu trước hạn, thực hiện chuỗi 40 phút sau. Nếu đã qua 20:00, giữ nguyên thứ tự, hoàn thành trong phiên 60-90 phút và báo ngay cho nhóm về việc nộp muộn.

| Khoảng thời gian | Việc phải làm | Đầu ra bắt buộc |
| :---: | :--- | :--- |
| Phút 0-5 | Chép bộ dữ kiện cốt lõi ở Mục 3 ra một trang nháp; đánh dấu các số liệu không được dùng | Một evidence sheet thống nhất |
| Phút 5-18 | Hoàn thiện Câu 1 theo khung 4 phần; trả lời 15 FAQ bằng 2-4 gạch đầu dòng/câu | Câu 1 không còn placeholder |
| Phút 18-27 | Hoàn thiện Câu 3; ưu tiên chuỗi Proposal/Feasibility -> Charter -> Sponsor phê duyệt -> PM được trao quyền -> RACI | Câu 3 không còn placeholder |
| Phút 27-36 | Hoàn thiện Câu 8; trình bày TELOS 5 mặt và ba mặt mở rộng; chốt khuyến nghị có điều kiện | Câu 8 không còn placeholder |
| Phút 36-40 | Tìm toàn bộ `_Trả lời:_`, kiểm tra số liệu, liên kết và sơ đồ; lưu và gửi nhóm xin review | 0 placeholder, 3 sơ đồ, 1 yêu cầu review |

Luồng hoàn thành toàn bộ phần việc:

![Luồng hoàn thành phần của Nguyễn Quang Thái](./assets/nguyen_quang_thai_completion_flow.svg)

## 5. Kế hoạch hoàn thiện theo từng câu

### 5.1. Câu 1 - Project Proposal

**Mục tiêu trình bày:** kể được câu chuyện từ vấn đề thật đến đề xuất được đánh giá, tránh biến câu trả lời thành danh sách tính năng.

**Trình tự biên soạn:**

1. WHAT: định nghĩa Proposal và sáu nhóm nội dung cần trả lời: vấn đề, đối tượng, giải pháp, giá trị, chi phí/lợi ích, rủi ro/khuyến nghị.
2. HOW: mô tả chuỗi khảo sát pain point -> persona Linh/Mai -> hình thành giải pháp -> benchmarking -> cost-benefit -> stakeholder review -> revision.
3. WHY: làm cơ sở ra quyết định có đầu tư hay không, so sánh tự xây với giải pháp thay thế và tạo đầu vào cho Vision & Scope, Feasibility, Charter.
4. EVIDENCE: dùng ít nhất năm dẫn chứng gồm 15 km, quy trình Scan-to-EPUB, đối thủ, OCR 85%, tìm kiếm dưới 3 giây, Signed URL 15 phút hoặc revision history.
5. FAQ: gom 15 câu thành ba cụm để học: hình thành/đánh giá Proposal; kiến thức nền về dự án; phạm vi, vai trò, kết quả và nguyên nhân thất bại.
6. Sơ đồ: rút về sáu nút có thể vẽ trong 60 giây: Pain point -> Persona -> Benchmark -> Proposal -> Review -> Revision.

**Kiểm chứng:** mỗi nhận định “nhóm đã làm” phải chỉ ra được mục hoặc bảng trong `02-project-proposal.md`; nội dung chưa có chứng cứ phải đổi thành “được đề xuất”, “dự kiến” hoặc “cần xác nhận”.

### 5.2. Câu 3 - Project Charter

**Mục tiêu trình bày:** chứng minh Charter là điểm kết thúc khởi tạo, chính thức hóa dự án và trao quyền cho PM, chứ không phải kế hoạch chi tiết.

**Trình tự biên soạn:**

1. WHAT: nêu định nghĩa chính thức; liệt kê mục tiêu, deliverables, governance, nguồn lực, milestone, stakeholder, giả định/ràng buộc, RACI và chữ ký.
2. HOW: lấy đầu vào từ Proposal, Vision & Scope và Feasibility; xác định Sponsor/PM; chốt mục tiêu/KPI; phân bổ nguồn lực; lập RACI; review; xin chữ ký.
3. WHY: tạo căn cứ ủy quyền, ngăn mơ hồ trách nhiệm, khóa ranh giới cấp cao và làm đầu vào cho Project Plan.
4. EVIDENCE: 20 tuần, MVP tuần 12, 500 sách, 4 kỹ sư 50%, 2 cán bộ thư viện, 10-15 CTV, ngân sách, RACI và change control vượt 5%.
5. FAQ: với mỗi câu, phải trả lời đủ đầu vào -> cách tạo -> cách đánh giá -> lý do -> cách sử dụng/cập nhật.
6. Sơ đồ: Sponsor -> PM -> Technical Lead/Library/Dev Team; kèm nguyên tắc mỗi gói chỉ có một A trong RACI.

**Kiểm chứng:** không nói “đã ký/phê duyệt” khi chưa có bản chữ ký thật. Khi thi, dùng cách diễn đạt “Charter được thiết kế để được Sponsor phê duyệt và trao quyền cho PM”.

### 5.3. Câu 8 - Feasibility Study

**Mục tiêu trình bày:** chỉ ra cách nhóm biến ý tưởng thành quyết định go/no-go có điều kiện bằng tiêu chí đo được.

**Trình tự biên soạn:**

1. WHAT: định nghĩa nghiên cứu khả thi và cấu trúc Purpose, Reason, Background, Criteria, Findings, Recommendations.
2. HOW: lấy dữ liệu vấn đề, hạ tầng, nguồn lực, chi phí, lịch trình, pháp lý; đánh giá TELOS; bổ sung Market/Resource/Cultural; thực hiện SWOT và benchmarking; lập khuyến nghị.
3. WHY: phát hiện rủi ro sớm, kiểm tra tính thực tiễn, hỗ trợ cost-benefit, lập kế hoạch nguồn lực và tránh đầu tư sai.
4. EVIDENCE: OCR tối thiểu 85%, tìm kiếm dưới 3 giây, MVP 12 tuần, go-live 20 tuần, 92% người được phỏng vấn ủng hộ EPUB, CapEx/OpEx và bốn risk owner.
5. FAQ: mỗi câu trả lời phải kết thúc bằng tác động thực tế tới quyết định, Charter, phạm vi MVP hoặc biện pháp giảm rủi ro.
6. Sơ đồ: trung tâm là Feasibility, năm nhánh TELOS; ghi chú ba nhánh mở rộng M-R-C bên cạnh nếu còn thời gian.

**Kiểm chứng:** kết luận nên là “khả thi có điều kiện”, kèm ba điều kiện tối thiểu: thẩm định pháp lý, pilot MVP và kiểm tra lại mô hình hòa vốn.

## 6. Kế hoạch đọc chéo, in ấn và thi thử

### 6.1. Thứ Sáu 21/08/2026 - Tự kiểm tra và rút gọn

- Sáng: đọc lại ba câu bằng tài liệu nguồn, sửa mọi phát biểu không có evidence.
- Chiều: tạo ba bản dàn ý một trang, mỗi bản chỉ giữ 4 mục WHAT-HOW-WHY-EVIDENCE và một sơ đồ.
- Tối: luyện ba lượt viết 10 phút; ghi lại ý bị quên và bổ sung vào flashcard.

### 6.2. Thứ Bảy 22/08/2026 - Đọc chéo và bản in

- Nhờ Người 2 kiểm tra mối nối Proposal -> Vision & Scope.
- Nhờ Người 4 kiểm tra mối nối Charter -> Project Plan/WBS.
- Nhờ một thành viên không cùng chủ đề đặt câu hỏi ngẫu nhiên từ 25 FAQ.
- Chốt ba tài liệu nguồn, xuất PDF và in A4.
- Ghi `[Câu 1]`, `[Câu 3]`, `[Câu 8]` ở góc trên bên phải từng bộ; dùng bìa phân cách màu hoặc kẹp riêng.
- Tự thử lấy đúng bộ tài liệu ba lần; mỗi lần phải dưới 20 giây, thấp hơn nhiều so với giới hạn 2 phút.

### 6.3. Chủ Nhật 23/08/2026 - Mock Interview

Thực hiện tối thiểu hai vòng:

1. Vòng chuẩn: bốc một trong ba câu, viết 10 phút, chọn bản in, trình bày 5 phút.
2. Vòng chất vấn: người hỏi chọn ngẫu nhiên năm FAQ, ưu tiên mâu thuẫn số liệu, lý do lựa chọn công nghệ và bằng chứng cập nhật tài liệu.

Sau mỗi vòng, chấm theo bốn tiêu chí, mỗi tiêu chí 0-2,5 điểm: đúng lý thuyết, đúng quy trình thực tế, có evidence, trình bày rõ và đúng thời gian. Chỉ kết thúc khi đạt ít nhất 8,5/10 ở hai vòng liên tiếp.

## 7. Tiêu chí hoàn thành

Một câu chỉ được đánh dấu Done khi đáp ứng toàn bộ:

- Không còn placeholder hoặc ghi chú TODO.
- WHAT có định nghĩa và cấu trúc chuẩn.
- HOW có đầu vào, các bước, người tham gia, cách đánh giá và cách cập nhật.
- WHY nêu được giá trị ra quyết định và ít nhất một đánh đổi.
- EVIDENCE có tối thiểu năm dẫn chứng đúng với phiên bản tài liệu hiện hành.
- Tất cả FAQ có câu trả lời ngắn, có thể nói trong 30-60 giây.
- Sơ đồ có thể tự vẽ lại trong tối đa 60 giây.
- Bài thử viết hoàn thành trong 10 phút và vẫn đọc được rõ ràng.
- Bản in đúng tài liệu, đúng số câu và lấy ra được trong dưới 20 giây.

## 8. Checklist bàn giao cá nhân

### Nội dung

- [ ] Câu 1: hoàn thành 4 mục, 15 FAQ và sơ đồ.
- [ ] Câu 3: hoàn thành 4 mục, 5 FAQ và sơ đồ.
- [ ] Câu 8: hoàn thành 4 mục, 5 FAQ và sơ đồ.
- [ ] Không còn `_Trả lời:_`, “tự hoàn thiện” hoặc TODO trong phiếu.
- [ ] Tất cả số liệu đã đối chiếu theo Mục 3.

### Bản in

- [ ] Proposal đã in và đánh dấu `[Câu 1]`.
- [ ] Project Charter đã in và đánh dấu `[Câu 3]`.
- [ ] Feasibility Study đã in và đánh dấu `[Câu 8]`.
- [ ] Ba bộ được kẹp/tách riêng và kiểm tra khả năng lấy nhanh.

### Luyện tập

- [ ] Ba lượt viết A4 trong 10 phút.
- [ ] Hai lượt trình bày 5-10 phút không nhìn tài liệu.
- [ ] Trả lời ngẫu nhiên đủ 25 FAQ.
- [ ] Hai vòng mock interview liên tiếp đạt từ 8,5/10.

## 9. Tài liệu nguồn

- [Hướng dẫn thi chung](../../README.md)
- [Kế hoạch chuẩn bị chung](../../02_Preparation_Plan.md)
- [Phiếu bài làm cá nhân](./README.md)
- [Project Idea](../../../docs/01-initiation/01-project-idea.md)
- [Project Proposal](../../../docs/01-initiation/02-project-proposal.md)
- [Feasibility Study](../../../docs/01-initiation/03-feasibility-study.md)
- [Project Charter](../../../docs/01-initiation/04-project-charter.md)
- [Lý thuyết dự án phần mềm](../../../materials/02_software_project.md)
- [Lý thuyết khởi tạo dự án](../../../materials/03_software_project_initiation.md)
- [Ghi chú bài giảng](../../../note.md)
