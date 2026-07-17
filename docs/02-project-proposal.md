# ĐỀ XUẤT DỰ ÁN (PROJECT PROPOSAL)

## Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS (HCMUS-LDMS)

### THÔNG TIN TÀI LIỆU (DOCUMENT CONTROL)

| Trường thông tin (Field)                   | Nội dung đặc tả (Description)                |
| :----------------------------------------- | :------------------------------------------- |
| **Mã tài liệu (Document ID)**              | `HCMUS-LDMS-PRP`                             |
| **Tên tài liệu (Document Title)**          | Đề xuất dự án (Project Proposal Document)    |
| **Dự án (Project Name)**                   | HCMUS-LDMS                                   |
| **Đơn vị soạn thảo (Author/Organization)** | Thư viện & Phòng Công nghệ Thông tin - HCMUS |
| **Người xem xét (Reviewer)**               | Trưởng phòng CNTT & Giám đốc Thư viện        |
| **Người phê duyệt (Approver)**             | Ban Giám hiệu Trường ĐH Khoa học Tự nhiên    |
| **Cấp độ bảo mật (Security Class)**        | Internal (Nội bộ trường)                     |
| **Trạng thái tài liệu (Status)**           | Under Review (Đang thẩm định)                |

### LỊCH SỬ PHIÊN BẢN (REVISION HISTORY)

| Phiên bản (Version) | Ngày phát hành (Date) | Mô tả thay đổi (Description of Change)                                      | Người thực hiện (Author) |
| :-----------------: | :-------------------: | :-------------------------------------------------------------------------- | :----------------------: |
|         1.0         |      06/07/2026       | Khởi tạo dự thảo đề xuất dự án ban đầu (v1.0).                              |      Mạch Quốc Tấn       |
|         2.0         |      14/07/2026       | Chuẩn hóa, chuyển WBS/RACI sang các tài liệu phù hợp, cập nhật chi phí VNĐ. |      Mạch Quốc Tấn       |
|         3.0         |      15/07/2026       | Bổ sung mục 2.4 Phân tích MOAT chi tiết (Lợi thế cạnh tranh bền vững).      |    Ân Tiến Nguyên An     |
|         4.0         |      17/07/2026       | Chuyển đổi Business Case sang tự sự ngôi thứ nhất và bổ sung phần Stakeholders & RACI. |    Ân Tiến Nguyên An     |
|         5.0         |      17/07/2026       | Đồng bộ hóa tech stack đơn giản hóa mới (Google OAuth 2.0, PostgreSQL FTS). |    Ân Tiến Nguyên An     |

---

## Mục lục

- [1. Tóm tắt điều hành (Executive Summary)](#1-tóm-tắt-điều-hành-executive-summary)
- [2. Lý do đầu tư và Bối cảnh thực tế (Business Case)](#2-lý-do-đầu-tư-và-bối-cảnh-thực-tế-business-case)
  - [2.1. Hành trình từ "Nỗi đau" vật lý đến rào cản tri thức của Độc giả](#21-hành-trình-từ-nỗi-đau-vật-lý-đến-rào-cản-tri-thức-của-độc-giả)
  - [2.2. Sự chuyển mình đột phá qua ý tưởng Scan-to-EPUB tích hợp](#22-sự-chuyển-mình-đột-phá-qua-ý-tưởng-scan-to-epub-tích-hợp)
  - [2.3. Phân tích đối chuẩn: Đối thủ cạnh tranh & Phương án kết hợp công cụ có sẵn](#23-phân-tích-đối-chuẩn-đối-thủ-cạnh-tranh--phương-án-kết-hợp-công-cụ-có-sẵn)
  - [2.4. Phân tích Lợi thế cạnh tranh bền vững (MOAT Analysis)](#24-phân-tích-lợi-thế-cạnh-tranh-bền-vững-moat-analysis)
- [3. Giải pháp đề xuất và Định hướng công nghệ](#3-giải-pháp-đề-xuất-và-định-hướng-công-nghệ)
  - [3.1. Mô tả tổng quan giải pháp](#31-mô-tả-tổng-quan-giải-pháp)
  - [3.2. Định hướng kiến trúc công nghệ](#32-định-hướng-kiến-trúc-công-nghệ)
  - [3.3. Phạm vi loại trừ cấp cao](#33-phạm-vi-loại-trừ-cấp-cao)
- [4. Phân tích Chi phí – Lợi ích (Cost-Benefit Analysis)](#4-phân-tích-chi-phí--lợi-ích-cost-benefit-analysis)
  - [4.1. Bảng phân tích lợi ích định lượng và định tính](#41-bảng-phân-tích-lợi-ích-định-lượng-và-định-tính)
  - [4.2. Ước lượng chi phí đầu tư ban đầu (CapEx)](#42-ước-lượng-chi-phí-đầu-tư-ban-đầu-capex)
  - [4.3. Ước lượng chi phí vận hành định kỳ (OpEx)](#43-ước-lượng-chi-phí-vận-hành-định-kỳ-opex)
  - [4.4. Mô hình kinh tế tránh chi phí và Điểm hòa vốn](#44-mô-hình-kinh-tế-tránh-chi-phí-và-điểm-hòa-vốn)
- [5. Phân tích các bên liên quan và Phân vai (Stakeholders & RACI)](#5-phân-tích-các-bên-liên-quan-và-phân-vai-stakeholders--raci)
- [6. Lộ trình triển khai cấp cao (High-Level Roadmap)](#6-lộ-trình-triển-khai-cấp-cao-high-level-roadmap)
- [7. Danh mục rủi ro kinh doanh và Biện pháp giảm thiểu](#7-danh-mục-rủi-ro-kinh-doanh-và-biện-pháp-giảm-thiểu)
- [8. Kết luận và Khuyến nghị hành động](#8-kết-luận-và-khuyến-nghị-hành-động)

---

## 1. Tóm tắt điều hành (Executive Summary)

Thư viện Trường Đại học Khoa học Tự nhiên (HCMUS) hiện quản lý hàng chục ngàn tài liệu học thuật cứng độc bản. Việc lưu trữ vật lý này đang đối mặt với các thách thức lớn về quá tải diện tích kho bãi, xuống cấp tài liệu và rào cản địa lý tiếp cận thông tin đối với sinh viên tại cơ sở Linh Trung (Thủ Đức). Các file PDF scan hiện tại chỉ là ảnh chụp tĩnh, không responsive và cực kỳ khó đọc trên các thiết bị di động.

Đề xuất này hướng tới việc xây dựng **Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS (HCMUS-LDMS)** nhằm tự động hóa luồng số hóa khép kín: quét tài liệu giấy -> nhận dạng ký tự quang học (**Tesseract OCR** tiếng Việt) -> hiệu chỉnh lỗi chính tả trực tuyến -> đóng gói tự động sang định dạng sách điện tử **EPUB 3.0 reflowable** tương thích mọi thiết bị di động, lập chỉ mục toàn văn (**Elasticsearch**) và phục vụ đọc trực tuyến bảo mật (**Signed URL**) cho sinh viên và giảng viên nội bộ trường.

**Các chỉ số thành công chính mong đợi:**

- Số hóa và đóng gói thành công 2.500+ tài liệu học liệu cốt lõi sang EPUB 3.0.
- Rút ngắn thời gian tra cứu và đọc tài liệu số xuống dưới 3 giây qua Elasticsearch.
- Tỷ lệ nhận dạng ký tự quang học chính xác đạt tối thiểu 85% trước khi soát lỗi.
- Không xảy ra sự cố rò rỉ hoặc tải lậu file sách gốc ra ngoài mạng nội bộ.

**Khung tài chính ước tính:**

- **Tổng mức đầu tư một lần (CapEx):** 75.000.000 VNĐ – 95.000.000 VNĐ (trong đó thiết bị quét chuyên nghiệp và chi phí nhân sự số hóa đợt đầu chiếm tỷ trọng lớn nhất).
- **Chi phí vận hành hàng năm (OpEx):** 15.000.000 VNĐ – 30.000.000 VNĐ/năm.
- **Thời gian hòa vốn kinh tế học thuật:** Dự kiến đạt được từ **2.5 – 3.8 năm** vận hành thông qua mô hình tránh chi phí lưu kho vật lý và tiết kiệm thời gian vận hành thủ thư.

## 2. Lý do đầu tư và Bối cảnh thực tế (Business Case)

### 2.1. Hành trình từ "Nỗi đau" vật lý đến rào cản tri thức của Độc giả

Để thấu hiểu tại sao dự án này là một bước đi sống còn cho sự phát triển của thư viện, hãy cùng phân tích hành trình trải nghiệm thực tế từ hai nhóm người dùng cốt lõi (User Personas): Sinh viên (Độc giả học tập) và Thủ thư (Vận hành hệ thống).

#### Câu chuyện thứ nhất: Persona Độc giả – Trải nghiệm thực tế của sinh viên Nguyễn Văn Linh

"Tôi là Nguyễn Văn Linh, sinh viên năm cuối khoa Công nghệ Thông tin tại cơ sở Linh Trung - Thủ Đức. Từ góc độ người dùng cuối (End-user), hành trình tiếp cận tài liệu học tập của tôi đang gặp phải những rào cản trải nghiệm (UX Pain Points) cực kỳ lớn:

1. **Rào cản địa lý & lãng phí tài nguyên thời gian:** Để chuẩn bị đề tài tốt nghiệp về _Kiến trúc Máy tính_, tôi buộc phải bắt chuyến xe buýt số 08 di chuyển quãng đường dài hơn 15km dưới thời tiết nắng nóng từ Linh Trung về cơ sở 1 Quận 5 — nơi duy nhất lưu trữ bản cứng độc bản. Cả hành trình đi và về tốn của tôi hơn 3 tiếng đồng hồ chỉ để tiếp cận một cuốn sách.
2. **Trải nghiệm tài liệu vật lý xuống cấp:** Khi tiếp cận được cuốn sách, tài liệu đã bị rách góc, ố vàng do tuổi thọ hơn 15 năm và không khí ẩm mốc của kho lưu trữ.
3. **Friction (ma sát) trong chính sách bảo mật cũ:** Vì là tài liệu độc bản, thư viện áp dụng quy chế nghiêm ngặt: chỉ đọc tại chỗ, không cho mang về và cấm photocopy. Tôi phải ngồi cắm cúi chép tay thủ công các sơ đồ mạch và công thức suốt nhiều giờ liền.
4. **Nỗi đau về định dạng (Format Pain Point):** Khi tôi cố chụp hình lại các trang sách bằng điện thoại để về nhà nghiên cứu, file ảnh chụp PDF tĩnh hoàn toàn không responsive. Tôi phải liên tục thực hiện thao tác zoom-in, zoom-out và cuộn ngang dọc trên màn hình điện thoại nhỏ hẹp, dẫn đến mỏi mắt và làm giảm sút 80% hiệu suất học tập."

#### Câu chuyện thứ hai: Persona Vận hành – Trải nghiệm thực tế của cô thủ thư Mai

"Tôi là Mai, cán bộ vận hành thư viện tại cơ sở Quận 5 của HCMUS. Dưới góc độ vận hành hệ thống (Operations), công việc hàng ngày của tôi đang đối mặt với những nút thắt (Bottlenecks) nghiêm trọng về hiệu suất và hạ tầng:

1. **Quá tải không gian vật lý (Physical Storage Bottleneck):** Số lượng giáo trình, tài liệu tăng lên qua từng năm nhưng diện tích kho kệ chứa sách giấy đã chiếm trọn 100% không gian thiết kế của thư viện. Tôi bất lực nhìn kho sách ngày một chật hẹp, không còn bất kỳ không gian trống nào để cải tạo thành không gian tự học số (Smart Learning Space) hiện đại hỗ trợ sinh viên thảo luận nhóm.
2. **Chi phí cơ hội và thời gian xử lý thủ công (Manual Overhead):** Mỗi khi độc giả có nhu cầu tra cứu, tôi phải di chuyển vào sâu trong kho tối, tìm kiếm thủ công từng cuốn sách giữa hàng ngàn kệ bám đầy bụi. Quy trình mượn trả giấy tờ rườm rà này ngốn của tôi hơn 85% thời gian làm việc, khiến tôi không thể tập trung vào các công việc có giá trị chuyên môn cao hơn như hỗ trợ nghiên cứu hay tối ưu hóa dịch vụ thông tin.
3. **Rủi ro xuống cấp tài liệu vĩnh viễn:** Với tần suất lật giở liên tục của sinh viên và điều kiện bảo quản nhiệt độ thông thường, tôi lo sợ nhiều tài liệu quý giá, giáo trình độc bản của nhà trường sẽ bị hư hại vĩnh viễn trước khi kịp chuyển giao cho thế hệ sau."

### 2.2. Sự chuyển mình đột phá qua ý tưởng Scan-to-EPUB tích hợp

Ý tưởng của **HCMUS-LDMS** ra đời để viết nên một câu chuyện hoàn toàn mới, biến quy trình thủ công lạc hậu thành một trải nghiệm số hóa tự động hóa khép kín:

- **Từ Trang giấy đến Sách điện tử động (Scan-to-EPUB):** Sách giấy được đặt lên máy quét chuyên dụng chữ V, hệ thống tự động đẩy ảnh lên và kích hoạt engine **Tesseract OCR** để nhận dạng văn bản tiếng Việt. Thay vì để thủ thư gõ lại thủ công, hệ thống cung cấp giao diện **Split-screen Editor** trực quan chia đôi màn hình: bên trái hiển thị ảnh chụp trang gốc, bên phải là trình soạn thảo văn bản đã OCR. Thủ thư hoặc sinh viên cộng tác viên chỉ cần đối chiếu nhanh, sửa vài lỗi chính tả thô và nhấn nút. Ngay lập tức, công cụ **Pandoc** tự động đóng gói nội dung đã biên tập thành chuẩn **EPUB 3.0 reflowable**.
- **Trải nghiệm Độc giả Kỷ nguyên số:** Cuốn sách sau khi xuất bản sẽ được lập chỉ mục toàn văn vào **CSDL PostgreSQL (FTS)**. Sinh viên tại Thủ Đức nay chỉ cần mở điện thoại, truy cập hệ thống qua Google OAuth 2.0 và gõ từ khóa tìm kiếm. Trong vòng chưa đầy 3 giây, hệ thống trả về kết quả chính xác đến từng chương sách và hiển thị vị trí vật lý của sách giấy tại kho Quận 5 nếu sinh viên muốn đến mượn trực tiếp. Trình đọc web Epub.js cho phép sinh viên co giãn cỡ chữ từ 80% đến 200%, đổi font (Roboto, Inter, hoặc OpenDyslexic cho người khó đọc) và chỉnh chế độ nền Sepia bảo vệ mắt, mang lại trải nghiệm đọc sách responsive tuyệt hảo trên mọi thiết bị.
- **Bảo vệ bản quyền số tuyệt đối:** Để giảng viên yên tâm đóng góp giáo trình, hệ thống tích hợp cơ chế bảo mật DRM nghiêm ngặt. Khi sinh viên đọc sách, hệ thống sử dụng **Signed URL** kết nối trực tiếp đến MinIO Storage với thời hạn hiệu lực tối đa 15 phút. Các hành vi nhấn chuột phải, copy (`Ctrl+C`), hoặc in ấn (`Ctrl+P`) đều bị vô hiệu hóa hoàn toàn đối với tài liệu nội bộ, ngăn chặn tuyệt đối việc tải lậu và rò rỉ file sách gốc ra ngoài.
- **Giải phóng và Hiện đại hóa thư viện:** Khi 2.500+ cuốn sách giáo trình được số hóa thành công lên hệ thống, thư viện Quận 5 sẽ thu hồi được hơn 60-70% diện tích kệ sách giấy cũ. Không gian này sẽ lập tức được cải tạo thành các phòng thảo luận thông minh, trang bị màn hình tương tác và mạng Wi-Fi tốc độ cao, hiện thực hóa mục tiêu Đại học số của HCMUS.

### 2.3. Phân tích đối chuẩn: Đối thủ cạnh tranh & Phương án kết hợp công cụ có sẵn

Để chứng minh tính thuyết phục của việc tự phát triển hệ thống HCMUS-LDMS, đề xuất này thực hiện phân tích đối chuẩn (benchmarking) giữa giải pháp đề xuất với hai phương án thay thế phổ biến:

- **So sánh với đối thủ cạnh tranh (Commercial Solutions):** Các giải pháp thư viện điện tử thương mại (như Lạc Việt Vebrary, DSpace thương mại) yêu cầu chi phí bản quyền và triển khai rất cao (thường từ 300 triệu đến hơn 1 tỷ VNĐ), vượt quá xa mức ngân sách giới hạn dưới 100 triệu VNĐ của dự án này. Hơn nữa, các hệ thống đóng này cực kỳ khó tùy biến để tích hợp quy trình sửa lỗi OCR Split-screen chuyên biệt cho tiếng Việt chuyên ngành, đồng thời không hỗ trợ cơ chế bảo mật DRM động thông qua Signed URL liên kết trực tiếp với LDAP của trường.
- **So sánh với phương án kết hợp công cụ có sẵn (Composition of Existing Tools):** Phương án thay thế thủ công là sử dụng máy quét văn phòng -> chạy phần mềm Abbyy FineReader offline -> đóng gói EPUB bằng Calibre -> chia sẻ qua Google Drive/OneDrive. Phương án này gặp 3 nút thắt lớn:
  1. _Quy trình rời rạc:_ Không có tính liên kết tự động, tốn từ 2-3 giờ lao động thủ công của thủ thư cho mỗi đầu sách để chuyển đổi qua lại giữa các phần mềm.
  2. _Rủi ro bản quyền nghiêm trọng:_ Google Drive/OneDrive không có cơ chế chặn tải xuống tệp gốc, không chặn được chuột phải copy, và không có Signed URL tự động hết hạn sau 15 phút, dẫn đến nguy cơ cao bị sinh viên phát tán học liệu ra ngoài.
  3. _Tra cứu hạn chế:_ Không hỗ trợ cơ chế lập chỉ mục tìm kiếm toàn văn sâu đến từng trang sách và highlight kết quả theo ngữ cảnh như PostgreSQL Full-Text Search.
- **Quy trình thẩm định AI và xem xét bởi con người (AI-assisted & Human Review):** Hệ thống LDMS ứng dụng mô hình kết hợp tối ưu: engine AI (Tesseract OCR chạy bất đồng bộ qua FastAPI BackgroundTasks) thực hiện nhận dạng thô, sau đó con người (biên tập viên/thủ thư/sinh viên CTV) đóng vai trò kiểm soát chất lượng (Human-in-the-loop) soát lỗi chính tả trực quan trên giao diện Split-screen trước khi phê duyệt xuất bản chính thức, bảo đảm độ chính xác học thuật đạt 100% với chi phí thấp nhất.

### 2.4. Phân tích Lợi thế cạnh tranh bền vững (MOAT Analysis)

Mục này phân tích chi tiết 5 yếu tố MOAT đã được nêu sơ bộ trong tài liệu [Ý tưởng Dự án (Project Idea, mục 5.1)](01-project-idea.md), nhằm chứng minh hệ thống HCMUS-LDMS sở hữu các lợi thế cạnh tranh bền vững khiến giải pháp thay thế rất khó sao chép hoặc cạnh tranh trực tiếp.

#### 2.4.1. Bảng tổng hợp MOAT

| Yếu tố MOAT                                    | Mức độ phòng thủ | Cơ chế vận hành                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Chiến lược gia cố                                                                                                                                                                                                                                                                                                               |
| :--------------------------------------------- | :--------------: | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **1. Nội dung độc quyền (Exclusive Content)**  |    ⭐⭐⭐⭐⭐    | Kho tài liệu vật lý của Thư viện HCMUS bao gồm: **(a)** giáo trình tự soạn bởi giảng viên nhà trường (không xuất bản thương mại), **(b)** tài liệu chuyên ngành độc bản in số lượng hạn chế, **(c)** luận văn, luận án và báo cáo nghiên cứu nội bộ, **(d)** ấn phẩm học thuật hiếm xuất bản trước năm 2010 không còn tái bản. Đây là **nguồn nội dung gốc mà chỉ duy nhất HCMUS sở hữu** — không trường nào khác, không nhà cung cấp thương mại nào có thể sao chép hoặc mua được. Khi số hóa thành EPUB, kho tri thức vật lý độc quyền này trở thành tài sản số không thể thay thế, tạo MOAT mạnh nhất của hệ thống. | • Ưu tiên số hóa tài liệu độc bản, giáo trình tự soạn trước — những nội dung có tính độc quyền cao nhất.<br>• Vận động giảng viên đóng góp giáo trình số mới trực tiếp lên hệ thống, mở rộng kho nội dung độc quyền liên tục.<br>• Liên kết với các khoa để tích hợp bài giảng, slide và tài liệu bổ trợ vào hệ sinh thái LDMS. |
| **2. Chi phí chuyển đổi cao (Switching Cost)** |    ⭐⭐⭐⭐⭐    | Hệ thống tích hợp sâu vào 3 trụ cột: hạ tầng định danh Google OAuth 2.0 / Mock Auth, quy trình nghiệp vụ scan-OCR-EPUB hàng ngày của thủ thư, và kho dữ liệu EPUB+PostgreSQL FTS độc quyền. Việc chuyển đổi sang giải pháp khác đồng nghĩa với: (a) di chuyển toàn bộ dữ liệu EPUB và chỉ mục, (b) tái tích hợp hệ thống định danh, (c) đào tạo lại toàn bộ đội ngũ thủ thư và sinh viên CTV. Ước tính chi phí chuyển đổi vượt 150% CapEx ban đầu.                                                                                                                                                                                     | • Tiếp tục mở rộng tích hợp với LMS Moodle và cổng thông tin đào tạo của trường.<br>• Xây dựng API Plugin cho các hệ thống quản lý học tập khác của ĐHQG-HCM.                                                                                                                                                                   |
| **3. Hiệu ứng mạng lưới (Network Effects)**    |     ⭐⭐⭐⭐     | Vòng lặp tăng trưởng tích cực 4 giai đoạn: **(1)** Thêm tài liệu số hóa → **(2)** Tăng giá trị tra cứu cho sinh viên → **(3)** Tăng lượng người dùng hoạt động → **(4)** Thu hút thêm sinh viên CTV tình nguyện biên tập OCR (quy đổi điểm rèn luyện) → quay lại **(1)**. Mỗi vòng lặp làm kho học liệu lớn hơn, chất lượng hơn, đối thủ mới phải bắt đầu từ zero.                                                                                                                                                                                                                                                     | • Thiết kế hệ thống gamification (bảng xếp hạng CTV, badge số hóa) để duy trì động lực đóng góp.<br>• Mở API cho giảng viên nhúng liên kết học liệu trực tiếp vào bài giảng Moodle, tạo thêm điểm chạm sử dụng.                                                                                                                 |
| **4. Lợi thế chi phí (Cost Advantage)**        |     ⭐⭐⭐⭐     | Tổng CapEx của HCMUS-LDMS (75–95 triệu VNĐ) chỉ bằng **≤25–30%** chi phí giải pháp thương mại tương đương (300 triệu – 1 tỷ VNĐ). Nguồn gốc lợi thế: **(a)** Toàn bộ tech stack mã nguồn mở (Tesseract, FastAPI, React, PostgreSQL, MinIO, Google OAuth 2.0) — không phát sinh bản quyền, **(b)** tận dụng hạ tầng VMware vSphere và mạng nội bộ sẵn có của trường, **(c)** nhân sự số hóa là sinh viên CTV bán thời gian (chi phí 3.000–4.000 VNĐ/cuốn vs. 50.000–100.000 VNĐ/cuốn nếu thuê ngoài).                                                                                                                           | • Duy trì cam kết với open-source, không phụ thuộc vendor lock-in.<br>• Ghi nhận tài liệu kỹ thuật đầy đủ để nhân sự mới có thể tiếp quản vận hành mà không cần chuyên gia đắt tiền.                                                                                                                                            |
| **5. Lợi thế dữ liệu tích lũy (Data MOAT)**    |    ⭐⭐⭐⭐⭐    | Kho EPUB reflowable được số hóa từ nguồn nội dung độc quyền của HCMUS (xem mục 1) kết hợp chỉ mục toàn văn PostgreSQL FTS là **tài sản dữ liệu độc quyền kép**: vừa độc quyền về nội dung gốc, vừa độc quyền về dữ liệu số hóa đã xử lý. Mỗi cuốn sách số hóa bao gồm: ảnh scan gốc, văn bản OCR đã hiệu chỉnh bởi con người, metadata thư mục học, và dữ liệu hành vi đọc của sinh viên. Sau 2.500 cuốn sách, khối lượng dữ liệu này trở thành rào cản gia nhập khổng lồ cho bất kỳ giải pháp thay thế nào.                                                                                                            | • Liên tục mở rộng kho bằng chương trình số hóa hàng năm (2.000 cuốn/năm).<br>• Khai thác dữ liệu hành vi đọc để đề xuất học liệu phù hợp (Giai đoạn 3 — AI/RAG).                                                                                                                                                               |

#### 2.4.2. Đánh giá tổng hợp sức mạnh MOAT

**Mức độ bền vững tổng thể: Mạnh (Strong MOAT).**

Sự kết hợp của 5 yếu tố MOAT tạo nên hệ thống phòng thủ đa lớp:

- **Lớp 1 — Nội dung không thể thay thế (Irreplaceable Content):** Kho tài liệu vật lý độc quyền của HCMUS là nền tảng MOAT mạnh nhất — không ai có thể mua hoặc sao chép nguồn nội dung gốc này.
- **Lớp 2 — Rào cản gia nhập (Entry Barrier):** Lợi thế chi phí khiến đối thủ cần đầu tư gấp 3–5 lần để xây dựng hệ thống tương đương.
- **Lớp 3 — Rào cản thoát ra (Exit Barrier):** Chi phí chuyển đổi cao khóa chặt trường vào hệ sinh thái LDMS sau khi go-live, giảm rủi ro bị thay thế.
- **Lớp 4 — Tăng trưởng tự thân (Organic Growth):** Hiệu ứng mạng lưới và Data MOAT cùng lớn theo thời gian, làm hệ thống càng sử dụng lâu càng khó thay thế.

> **So sánh đối chuẩn MOAT:** Các giải pháp thương mại như Lạc Việt Vebrary hoặc DSpace có lợi thế về thương hiệu và hỗ trợ kỹ thuật chuyên nghiệp, nhưng **hoàn toàn không sở hữu Exclusive Content MOAT** (không có kho giáo trình tự soạn, tài liệu độc bản của HCMUS) và không có Data MOAT về học liệu EPUB tiếng Việt chuyên ngành. Dù họ có sản công nghệ, họ không bao giờ có được nội dung gốc của thư viện HCMUS. Phương án kết hợp công cụ rời rạc (Abbyy + Calibre + Google Drive) không sở hữu bất kỳ MOAT nào do quy trình thủ công không tạo được tích lũy dữ liệu và không có rào cản chuyển đổi.

## 3. Giải pháp đề xuất và Định hướng công nghệ

### 3.1. Mô tả tổng quan giải pháp

Xây dựng một ứng dụng Web Portal và Dashboard nghiệp vụ tự phát triển (custom-built) quản lý vòng đời tài liệu số hóa. Thủ thư scan tài liệu giấy, đẩy lên hệ thống để chạy OCR và biên tập lỗi chính tả trên giao diện trực quan Split-screen, sau đó đóng gói EPUB và phát hành cho độc giả đọc trực tuyến responsive.

### 3.2. Định hướng kiến trúc công nghệ

Hệ thống được phát triển theo mô hình **Modular Monolith** nhằm tối ưu chi phí hạ tầng và vận hành nội bộ:

- **Frontend:** React 18 (TypeScript), Tailwind CSS và thư viện hiển thị sách Epub.js.
- **Backend:** FastAPI (Python 3.11) và FastAPI BackgroundTasks xử lý các tác vụ nặng (OCR, Pandoc) bất đồng bộ.
- **Cơ sở dữ liệu:** PostgreSQL 16 (lưu trữ quan hệ & lập chỉ mục tìm kiếm toàn văn Full-Text Search).
- **Lưu trữ đối tượng:** MinIO Object Storage (On-premise tương thích S3).
- **Định danh & Xác thực:** Google OAuth 2.0 / Mock Auth (roadmap: Keycloak OIDC liên kết LDAP/Active Directory của trường).

### 3.3. Phạm vi loại trừ cấp cao

- Hệ thống chống đạo văn chuyên sâu (chỉ thiết lập API mở phục vụ tích hợp tương lai).
- Số hóa các hồ sơ hành chính, học bạ, tài liệu nhân sự của trường.
- Tính năng tìm kiếm trí tuệ nhân tạo (AI/RAG) - hoãn sang Giai đoạn 3 của dự án.

## 4. Phân tích Chi phí – Lợi ích (Cost-Benefit Analysis)

### 4.1. Bảng phân tích lợi ích định lượng và định tính

| Đối tượng thụ hưởng         | Lợi ích định lượng                                                                                                                                     | Lợi ích định tính                                                                                                  |
| :-------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------- |
| **Thư viện HCMUS**          | • Thu hồi khoảng **60-70%** diện tích kệ sách giấy tại phòng đọc Quận 5.<br>• Giảm **85%** thời gian thủ thư xử lý yêu cầu mượn trả và tra kho vật lý. | • Bảo tồn vĩnh viễn học liệu gốc của trường.<br>• Hiện đại hóa hình ảnh thư viện, nâng cao thương hiệu đại học số. |
| **Độc giả (Sinh viên, GV)** | • Đọc sách responsive mượt mà **100%** trên smartphone.<br>• Tiếp cận học liệu từ xa **24/7**.<br>• Tra cứu từ khóa nội dung sách dưới **3 giây**.     | • Chủ động trong học tập trực tuyến.<br>• Dễ dàng tra cứu công thức, lý thuyết phục vụ nghiên cứu và ôn thi.       |
| **Ban Giám hiệu / Trường**  | • Tối ưu hóa hạ tầng CNTT và server ảo hóa sẵn có.<br>• Đạt chỉ tiêu chuyển đổi số giáo dục cấp ĐHQG-HCM.                                              | • Làm chủ hoàn toàn mã nguồn hệ thống.<br>• Tạo nền tảng chia sẻ học liệu số hóa dùng chung an toàn.               |

### 4.2. Ước lượng chi phí đầu tư ban đầu (CapEx)

| Hạng mục đầu tư                | Cơ sở ước tính                                                                                                                 |       Khoảng giá (VNĐ)        |
| :----------------------------- | :----------------------------------------------------------------------------------------------------------------------------- | :---------------------------: |
| **Số hóa & Biên tập EPUB**     | Chi phí nhân công (sinh viên CTV bán thời gian) scan, OCR và soát lỗi chính tả cho ~10.000 cuốn sách (3.000 – 4.000 VNĐ/cuốn). |    30.000.000 – 40.000.000    |
| **Phát triển phần mềm custom** | Chi phí nhân sự Phòng CNTT tự lập trình React/FastAPI trong 3 tháng.                                                           |    25.000.000 – 35.000.000    |
| **Thiết bị scan & Server**     | Mua 02 máy quét chữ V chuyên dụng và bổ sung RAM/SSD cho cụm máy chủ ảo hóa của trường.                                        |    10.000.000 – 12.000.000    |
| **Đào tạo & Triển khai**       | Tài liệu hướng dẫn sử dụng, video trực quan và tổ chức các buổi tập huấn cho thủ thư.                                          |     2.000.000 – 4.000.000     |
| **Dự phòng rủi ro (~15%)**     | Dự phòng biến động giá phần cứng hoặc phát sinh kỹ thuật.                                                                      |    5.000.000 – 10.000.000     |
| **TỔNG CAPEX**                 | **Tổng đầu tư ban đầu ước tính**                                                                                               | **≈ 75.000.000 – 95.000.000** |

### 4.3. Ước lượng chi phí vận hành định kỳ (OpEx)

| Hạng mục vận hành             | Cơ sở ước tính (hàng năm, từ năm thứ 2)                                   |     Khoảng giá (VNĐ/năm)      |
| :---------------------------- | :------------------------------------------------------------------------ | :---------------------------: |
| **Hạ tầng Server & Cloud**    | Duy trì điện, mạng băng thông cao và sao lưu tự động (PgBackRest/Restic). |     4.000.000 – 8.000.000     |
| **Bảo trì phần mềm**          | Nâng cấp bảo mật, vá lỗi, cập nhật các gói React/FastAPI.                 |    6.000.000 – 12.000.000     |
| **Dịch vụ Cloud OCR bổ sung** | Bản quyền Cloud OCR API dự phòng dành cho sách in quá mờ.                 |     3.000.000 – 6.000.000     |
| **Số hóa bổ sung hàng năm**   | Số hóa giáo trình mới phát sinh.                                          |     2.000.000 – 4.000.000     |
| **TỔNG OPEX / NĂM**           | **Chi phí vận hành hàng năm**                                             | **≈ 15.000.000 – 30.000.000** |

### 4.4. Mô hình kinh tế tránh chi phí và Điểm hòa vốn

- **Mô hình Tránh chi phí (Cost Avoidance):** Tiết kiệm tương đương **20.000.000 VNĐ/năm** nhờ giải phóng mặt bằng kệ sách vật lý tại Quận 5 làm phòng tự học số, tránh được chi phí đầu tư xây dựng kho bãi vật lý mới. Tiết kiệm giờ công lao động thủ thư mượn trả thủ công trị giá **15.000.000 VNĐ/năm**.
- **Phân tích hòa vốn:** Với mức lợi ích kinh tế gián tiếp quy đổi đạt **20.000.000 VNĐ/năm**, hệ thống dự kiến đạt điểm hòa vốn kinh tế học thuật sau **2.5 đến 3.8 năm** vận hành thực tế.

## 5. Phân tích các bên liên quan và Phân vai (Stakeholders & RACI)

Để đảm bảo tính khả thi trong vận hành và triển khai thực tế của dự án **HCMUS-LDMS**, cấu trúc phân vai và trách nhiệm của các bên liên quan được hoạch định rõ ràng như sau:

### 5.1. Stakeholder Register (Danh sách các bên liên quan)

* **Sponsor (Nhà tài trợ):** Ban Giám hiệu HCMUS. Vai trò: Phê duyệt chủ trương, cấp ngân sách (CapEx/OpEx) theo từng giai đoạn và định hướng chiến lược chuyển đổi số của nhà trường.
* **Client (Chủ trì nghiệp vụ):** Ban Giám đốc Thư viện HCMUS. Vai trò: Quản lý quy trình duyệt xuất bản, kiểm soát chất lượng dữ liệu OCR/EPUB, tổ chức đội ngũ sinh viên CTV số hóa và vận hành cổng thông tin sau go-live.
* **Client (Chủ trì kỹ thuật):** Phòng Công nghệ Thông tin. Vai trò: Thiết lập hạ tầng ảo hóa VMware, cài đặt và tùy biến phần mềm lõi (React/FastAPI/PostgreSQL/MinIO), tích hợp Google OAuth 2.0 và quản lý chỉ mục PostgreSQL FTS.
* **Cố vấn Pháp lý:** Bộ phận Pháp chế & Lưu trữ của trường. Vai trò: Thẩm định quy chế bản quyền số hóa nội bộ và phê duyệt điều khoản consent (đồng ý nộp và chia sẻ tài liệu số).
* **Độc giả (Người dùng cuối):** Sinh viên và Giảng viên trường. Vai trò: Người trực tiếp nộp tài liệu (đối với sách/giáo trình mới đóng góp) và sử dụng hệ thống tra cứu, đọc sách trực tuyến.

### 5.2. Ma trận Trách nhiệm (RACI Matrix)

* **R** (Responsible): Bộ phận thực hiện công việc.
* **A** (Accountable): Bộ phận chịu trách nhiệm cuối cùng (Mỗi gói công việc chỉ có duy nhất một đơn vị Accountable).
* **C** (Consulted): Bộ phận được tham vấn ý kiến trước khi thực hiện.
* **I** (Informed): Bộ phận được thông báo kết quả sau khi hoàn thành.

| Gói công việc WBS | Thư viện | Phòng CNTT | Giáo vụ Khoa | Bộ phận Pháp chế | Ban Giám hiệu | Độc giả |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **WP1 — Khảo sát & Bản quyền** | **A** / R | R | C | C | I | - |
| **WP2 — Thiết lập Backend & DB** | C | **A** / R | - | - | I | - |
| **WP3 — Phát triển UI & OCR/EPUB** | C | **A** / R | - | - | I | C |
| **WP4 — Số hóa tài liệu** | **A** / R | C | C | C | I | - |
| **WP5 — Kiểm thử & UAT** | R | **A** / R | - | - | I | C |
| **WP6 — Triển khai & Vận hành** | **A** / R | R | C | - | I | I |

---

## 6. Lộ trình triển khai cấp cao (High-Level Roadmap)

Dự án kéo dài **20 tuần** và chia thành 4 giai đoạn lớn kết hợp kiểm soát cổng (Gating Checkpoints):

- **Giai đoạn 0 — Khảo sát & Bản quyền (Tuần 1–2):** Kiểm kê kho sách tự soạn, bộ phận Pháp chế thẩm định quy chế bản quyền số hóa nội bộ và khảo sát báo giá máy quét chữ V.
- **Giai đoạn 1 — Xây dựng MVP & Thí điểm (Tuần 3–12):** Lập trình React/FastAPI cốt lõi, tích hợp OCR, Pandoc, MinIO, Google OAuth 2.0 / Mock Auth; tiến hành số hóa thí điểm 500 cuốn sách ngành CNTT để kiểm thử.
- **Giai đoạn 2 — Số hóa Diện rộng (Tuần 13–18):** Chuyển giao công nghệ cho thư viện, tuyển sinh viên CTV và tiến hành số hóa hàng loạt 2.000 giáo trình cốt lõi tiếp theo.
- **Giai đoạn 3 — Nghiệm thu & Chuyển giao (Tuần 19–20):** Kiểm thử nghiệm thu (UAT), pentest bảo mật, đào tạo thủ thư và chính thức go-live toàn trường.

---

## 7. Danh mục rủi ro kinh doanh và Biện pháp giảm thiểu

| Nhóm rủi ro          | Chi tiết rủi ro                                                            | Mức độ         | Biện pháp giảm thiểu                                                                                    | Risk Owner                    |
| :------------------- | :------------------------------------------------------------------------- | :------------- | :------------------------------------------------------------------------------------------------------ | :---------------------------- |
| **Bản quyền & SHTT** | Số hóa nhầm tài liệu có bản quyền ngoài trường gây tranh chấp pháp lý.     | **Cao**        | • Chỉ số hóa sách nội bộ, giáo trình tự soạn.<br>• Phân quyền truy cập Internal/Restricted nghiêm ngặt. | **Ban Giám đốc Thư viện**     |
| **Chất lượng OCR**   | Sách in cũ mờ làm giảm độ chính xác OCR dưới 85%, gây quá tải rà soát lỗi. | **Trung bình** | • Tiền xử lý ảnh scan (lọc nhiễu, tăng tương phản).<br>• MVP chỉ làm sách in rõ nét từ 2010 trở đi.     | **Phòng Công nghệ Thông tin** |
| **Rò rỉ tài liệu**   | Sinh viên dùng công cụ cào web lấy file EPUB gốc phát tán bên ngoài.       | **Trung bình** | • Dùng Signed URL MinIO hạn dùng 15 phút.<br>• Chặn copy, chuột phải, chia nhỏ file EPUB.               | **Phòng Công nghệ Thông tin** |
| **Quá tải nhân sự**  | Đội ngũ kỹ sư kiêm nhiệm 50% bị quá tải công việc trường phát sinh.        | **Trung bình** | • PM ký cam kết phân bổ thời gian làm việc chính thức.<br>• Sử dụng Docker để tối ưu hóa khâu deploy.   | **Phòng Công nghệ Thông tin** |

## 8. Kết luận và Khuyến nghị hành động

### 8.1. Kết luận

Hệ thống **HCMUS-LDMS** giải quyết trực tiếp nhu cầu cấp thiết về học liệu số và giải phóng diện tích thư viện. Việc tự xây dựng hệ thống custom giúp trường làm chủ công nghệ vĩnh viễn, dễ dàng tích hợp hạ tầng định danh Google OAuth 2.0 sẵn có và tiết kiệm chi phí bản quyền khổng lồ so với mua phần mềm thương mại.

### 8.2. Khuyến nghị hành động

1. Phê duyệt chủ trương triển khai và cấp ngân sách ban đầu thực hiện **Giai đoạn 0 (Khảo sát)**.
2. Thông qua phương án triển khai **thí điểm cuốn chiếu MVP** để kiểm chứng hiệu quả thực tế trước khi đầu tư số hóa diện rộng.
3. Cho phép Thư viện tuyển dụng sinh viên CTV bán thời gian để hỗ trợ khâu biên tập hiệu chỉnh chữ OCR thô.
