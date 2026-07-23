# ĐỀ XUẤT DỰ ÁN

## Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS (HCMUS-LDMS)

### KIỂM SOÁT TÀI LIỆU

| Trường thông tin        | Nội dung đặc tả                                      |
| :---------------------- | :--------------------------------------------------- |
| **Mã tài liệu**         | `HCMUS-LDMS-PRP`                                     |
| **Tên tài liệu**        | Đề xuất dự án                                        |
| **Tên dự án**           | HCMUS-LDMS                                           |
| **Đơn vị soạn thảo**    | Thư viện & Phòng Công nghệ Thông tin - HCMUS         |
| **Người xem xét**       | Trưởng phòng Công nghệ Thông tin & Giám đốc Thư viện |
| **Người phê duyệt**     | Ban Giám hiệu Trường Đại học Khoa học Tự nhiên       |
| **Cấp độ bảo mật**      | Nội bộ                                               |
| **Trạng thái tài liệu** | Đang thẩm định                                       |

### LỊCH SỬ PHIÊN BẢN

| Phiên bản | Ngày phát hành | Mô tả thay đổi                                                                        |  Người thực hiện  |
| :-------: | :------------: | :------------------------------------------------------------------------------------ | :---------------: |
|    1.0    |   06/07/2026   | Khởi tạo dự thảo đề xuất dự án ban đầu (v1.0).                                        |   Mạch Quốc Tấn   |
|    2.0    |   14/07/2026   | Chuẩn hóa, chuyển phân định trách nhiệm sang tài liệu phù hợp.                        |   Mạch Quốc Tấn   |
|    3.0    |   15/07/2026   | Bổ dung phân tích lợi thế cạnh tranh bền vững chi tiết.                               | Ân Tiến Nguyên An |
|    4.0    |   17/07/2026   | Chuyển đổi lý do đầu tư sang tự sự và bổ sung các bên liên quan.                      | Ân Tiến Nguyên An |
|    5.0    |   17/07/2026   | Đồng bộ hóa công nghệ phát triển đơn giản hóa mới (Google OAuth 2.0, PostgreSQL FTS). | Ân Tiến Nguyên An |
|    6.0    |   23/07/2026   | Loại bỏ số liệu định lượng bối cảnh, bổ sung đối chuẩn đối thủ, Việt hóa toàn diện.   |   Mạch Quốc Tấn   |

---

## Mục lục

- [1. Tóm tắt điều hành](#1-tóm-tắt-điều-hành)
- [2. Lý do đầu tư và Bối cảnh thực tế](#2-lý-do-đầu-tư-và-bối-cảnh-thực-tế)
  - [2.1. Hành trình từ "Nỗi đau" vật lý đến rào cản tri thức của Độc giả](#21-hành-trình-từ-nỗi-đau-vật-lý-đến-rào-cản-tri-thức-của-độc-giả)
  - [2.2. Sự chuyển mình đột phá qua ý tưởng số hóa tích hợp](#22-sự-chuyển-mình-đột-phá-qua-ý-tưởng-số-hóa-tích-hợp)
  - [2.3. Phân tích đối chuẩn: Đối thủ cạnh tranh và Phương án kết hợp công cụ sẵn có](#23-phân-tích-đối-chuẩn-đối-thủ-cạnh-tranh-và-phương-án-kết-hợp-công-cụ-sẵn-có)
  - [2.4. Phân tích Lợi thế cạnh tranh bền vững](#24-phân-tích-lợi-thế-cạnh-tranh-bền-vững)
- [3. Giải pháp đề xuất và Định hướng công nghệ](#3-giải-pháp-đề-xuất-và-định-hướng-công-nghệ)
  - [3.1. Mô tả tổng quan giải pháp](#31-mô-tả-tổng-quan-giải-pháp)
  - [3.2. Định hướng kiến trúc công nghệ](#32-định-hướng-kiến-trúc-công-nghệ)
  - [3.3. Phạm vi loại trừ cấp cao](#33-phạm-vi-loại-trừ-cấp-cao)
- [4. Phân tích Chi phí – Lợi ích](#4-phân-tích-chi-phí--lợi-ích)
  - [4.1. Bảng phân tích lợi ích định lượng và định tính](#41-bảng-phân-tích-lợi-ích-định-lượng-và-định-tính)
  - [4.2. Ước lượng chi phí đầu tư ban đầu](#42-ước-lượng-chi-phí-đầu-tư-ban-đầu)
  - [4.3. Ước lượng chi phí vận hành định kỳ](#43-ước-lượng-chi-phí-vận-hành-định-kỳ)
  - [4.4. Mô hình kinh tế tránh chi phí và Điểm hòa vốn](#44-mô-hình-kinh-tế-tránh-chi-phí-và-điểm-hòa-vốn)
- [5. Phân tích các bên liên quan và Phân vai](#5-phân-tích-các-bên-liên-quan-và-phân-vai)
  - [5.1. Danh sách các bên liên quan](#51-danh-sách-các-bên-liên-quan)
  - [5.2. Ma trận phân định trách nhiệm](#52-ma-trận-phân-định-trách-nhiệm)
  - [5.3. Đánh giá tính khả thi từ góc độ quản lý các bên liên quan](#53-đánh-giá-tính-khả-thi-từ-góc-độ-quản-lý-các-bên-liên-quan)
- [6. Lộ trình triển khai cấp cao](#6-lộ-trình-triển-khai-cấp-cao)
- [7. Danh mục rủi ro kinh doanh và Biện pháp giảm thiểu](#7-danh-mục-rủi-ro-kinh-doanh-và-biện-pháp-giảm-thiểu)
- [8. Kết luận và Khuyến nghị hành động](#8-kết-luận-và-khuyến-nghị-hành-động)

---

## 1. Tóm tắt điều hành

Thư viện Trường Đại học Khoa học Tự nhiên (HCMUS) hiện quản lý hàng chục ngàn tài liệu học thuật cứng độc bản. Việc lưu trữ vật lý này đang đối mặt với các thách thức lớn về quá tải diện tích kho bãi, xuống cấp tài liệu và rào cản địa lý tiếp cận thông tin đối với sinh viên tại cơ sở Linh Trung (Thủ Đức). Các tệp tin ảnh quét PDF tĩnh hiện tại không hỗ trợ tự co giãn dòng và cực kỳ khó đọc trên các thiết bị di động.

Đề xuất này hướng tới việc xây dựng **Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS (HCMUS-LDMS)** nhằm tự động hóa luồng số hóa khép kín: quét tài liệu giấy → nhận dạng chữ bằng công nghệ nhận dạng ký tự quang học Tesseract → hiệu chỉnh lỗi chính tả trực tuyến trên giao diện chia đôi màn hình → đóng gói tự động sang định dạng sách điện tử tương thích động EPUB 3.0, lập chỉ mục tìm kiếm toàn văn và đọc sách trực tuyến bảo mật thông qua đường dẫn bảo mật tự hủy cho sinh viên và giảng viên nội bộ trường.

**Các chỉ số thành công chính mong đợi:**

- Số hóa và đóng gói thành công kho tài liệu học liệu cốt lõi sang EPUB 3.0.
- Rút ngắn thời gian tra cứu và đọc tài liệu số xuống dưới 3 giây qua hệ thống tìm kiếm toàn văn.
- Tỷ lệ nhận dạng chữ tự động chính xác đạt tối thiểu 85% trước khi soát lỗi.
- Không xảy ra sự cố rò rỉ hoặc tải lậu tệp sách gốc ra ngoài mạng nội bộ.

**Khung tài chính ước tính:**

- **Chi phí đầu tư ban đầu:** Hợp lý và tối ưu hóa nhờ sử dụng thiết bị quét tự chế và máy chủ ảo hóa sẵn có của trường.
- **Chi phí vận hành hàng năm:** Tối ưu hóa bằng cách huy động cộng tác viên sinh viên.
- **Thời gian hòa vốn kinh tế học thuật:** Dự kiến đạt được trong ngắn hạn thông qua việc giải phóng không gian lưu kho vật lý và tiết kiệm thời gian vận hành của thủ thư.

## 2. Lý do đầu tư và Bối cảnh thực tế

### 2.1. Hành trình từ "Nỗi đau" vật lý đến rào cản tri thức của Độc giả

Để thấu hiểu tại sao dự án này là một bước đi sống còn cho sự phát triển của thư viện, hãy cùng phân tích hành trình trải nghiệm thực tế từ hai nhóm người dùng cốt lõi: Sinh viên (Độc giả học tập) và Thủ thư (Vận hành hệ thống).

#### Câu chuyện thứ nhất: Độc giả – Trải nghiệm thực tế của sinh viên Nguyễn Văn Linh

"Tôi là Nguyễn Văn Linh, sinh viên năm cuối khoa Công nghệ Thông tin tại cơ sở Linh Trung - Thủ Đức. Từ góc độ người dùng cuối, hành trình tiếp cận tài liệu học tập của tôi đang gặp phải những rào cản trải nghiệm cực kỳ lớn:

1. **Rào cản địa lý và lãng phí thời gian:** Để chuẩn bị đề tài tốt nghiệp, tôi buộc phải di chuyển quãng đường dài mệt mỏi từ Linh Trung về cơ sở Quận 5 — nơi duy nhất lưu trữ sách giáo trình độc bản. Cả hành trình đi và về tốn rất nhiều thời gian chỉ để tiếp cận một cuốn sách.
2. **Trải nghiệm tài liệu vật lý xuống cấp:** Khi tiếp cận được cuốn sách, tài liệu đã bị mục nát, rách góc do tuổi thọ cao và điều kiện bảo quản tự nhiên.
3. **Ma sát trong chính sách bảo mật cũ:** Vì là tài liệu độc bản duy nhất, thư viện chỉ cho đọc tại chỗ, cấm mang về và cấm sao chụp. Tôi phải ngồi cắm cúi ghi chép thủ công các sơ đồ và công thức suốt nhiều giờ liền.
4. **Nút thắt về định dạng:** Khi tôi chụp hình lại các trang sách bằng điện thoại để về nhà nghiên cứu, file ảnh chụp tĩnh không tự động co giãn dòng. Tôi phải liên tục phóng to thu nhỏ và cuộn ngang dọc trên màn hình điện thoại, dẫn đến mỏi mắt và làm giảm sút đáng kể hiệu suất học tập."

#### Câu chuyện thứ hai: Vận hành – Trải nghiệm thực tế của cô thủ thư Mai

"Tôi là Mai, cán bộ vận hành thư viện tại cơ sở Quận 5 của HCMUS. Dưới góc độ vận hành hệ thống, công việc hàng ngày của tôi đang đối mặt với những nút thắt nghiêm trọng về hiệu suất và hạ tầng:

1. **Quá tải không gian vật lý:** Diện tích kho kệ chứa sách giấy đã quá tải công suất thiết kế của thư viện. Tôi không còn diện tích trống để cải tạo thành phòng tự học hiện đại hỗ trợ sinh viên thảo luận nhóm.
2. **Thời gian xử lý thủ công quá lớn:** Mỗi khi độc giả có nhu cầu tra cứu, tôi phải tìm kiếm thủ công từng cuốn sách giữa hàng ngàn kệ. Quy trình mượn trả giấy tờ rườm rà này ngốn phần lớn thời gian làm việc, khiến tôi không thể tập trung tối ưu hóa các dịch vụ thông tin khác.
3. **Rủi ro xuống cấp tài liệu vĩnh viễn:** Với tần suất mượn đọc liên tục của sinh viên và điều kiện bảo quản nhiệt độ thông thường, nhiều tài liệu quý giá, giáo trình độc bản của nhà trường đang đối mặt với nguy cơ hư hại vĩnh viễn."

### 2.2. Sự chuyển mình đột phá qua ý tưởng số hóa tích hợp

Ý tưởng của **HCMUS-LDMS** ra đời để viết nên một câu chuyện hoàn toàn mới, biến quy trình thủ công lạc hậu thành một trải nghiệm số hóa tự động hóa khép kín:

- **Từ Trang giấy đến Sách điện tử động:** Sách giấy được quét bằng thiết bị chuyên dụng, hệ thống tự động đẩy ảnh lên và nhận dạng chữ bằng công nghệ Tesseract OCR. Hệ thống cung cấp giao diện soạn thảo chia đôi màn hình trực quan: bên trái hiển thị ảnh chụp trang gốc, bên phải là trình soạn thảo văn bản đã được nhận dạng chữ. Thủ thư hoặc cộng tác viên chỉ cần đối chiếu nhanh, sửa lỗi chính tả thô và lưu nháp. Sau đó, hệ thống tự động đóng gói nội dung thành chuẩn EPUB 3.0 tương thích động.
- **Trải nghiệm Độc giả Kỷ nguyên số:** Sách sau khi xuất bản sẽ được lập chỉ mục tìm kiếm toàn văn. Sinh viên nay chỉ cần mở điện thoại, đăng nhập tài khoản trường và gõ từ khóa tìm kiếm. Trong vòng chưa đầy 3 giây, hệ thống trả về kết quả chính xác đến từng từ và đoạn sách. Trình đọc web cho phép sinh viên tự co giãn cỡ chữ, đổi phông chữ và chỉnh chế độ nền bảo vệ mắt, mang lại trải nghiệm đọc sách tương thích động tuyệt hảo trên mọi thiết bị di động.
- **Bảo vệ bản quyền số tuyệt đối:** Để giảng viên yên tâm đóng góp giáo trình, hệ thống tích hợp cơ chế bảo quản bản quyền số chặt chẽ. Khi sinh viên đọc sách, hệ thống sử dụng đường dẫn bảo mật tự hủy sau 15 phút. Các hành vi nhấn chuột phải, sao chép văn bản, hoặc in ấn đều bị vô hiệu hóa hoàn toàn đối với tài liệu nội bộ, ngăn chặn hành vi tải lậu tệp sách gốc ra ngoài.
- **Giải phóng và Hiện đại hóa thư viện:** Khi các cuốn sách giáo trình được số hóa thành công lên hệ thống, thư viện Quận 5 sẽ thu hồi được phần lớn diện tích kệ sách giấy cũ để cải tạo thành các phòng tự học số thông minh.

### 2.3. Phân tích đối chuẩn: Đối thủ cạnh tranh và Phương án kết hợp công cụ sẵn có

Để làm rõ tính khả thi và thuyết phục của việc tự phát triển hệ thống HCMUS-LDMS, đề xuất này thực hiện đối chuẩn chi tiết giữa giải pháp tự xây dựng với các giải pháp thương mại và phương án kết hợp thủ công:

| Tiêu chí đối chuẩn                     | Giải pháp tự xây dựng (HCMUS-LDMS)                                                                                         | Giải pháp thương mại (Ví dụ: Lạc Việt Vebrary)                                                                          | Giải pháp nguồn mở sẵn có (Ví dụ: DSpace)                                                                          | Phương án ghép công cụ rời rạc (Abbyy + Calibre + Drive)                                                           |
| :------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------- |
| **Chi phí bản quyền & Vận hành**       | **Tối ưu**<br>Sử dụng công nghệ mã nguồn mở và thuê máy chủ đám mây (Cloud VPS) chi phí thấp. | **Rất cao**<br>Chi phí bản quyền ban đầu lớn và phí duy trì nâng cấp hàng năm cao.                                      | **Trung bình**<br>Miễn phí bản quyền nhưng tốn chi phí thuê ngoài tùy biến.                                        | **Thấp**<br>Tận dụng các công cụ có sẵn nhưng tốn chi phí giờ công vận hành thủ công rất lớn.                      |
| **Quy trình nhận dạng chữ & Soát lỗi** | **Khép kín & Tự động**<br>Tích hợp nhận dạng chữ OCR và giao diện soạn thảo chia đôi màn hình soát lỗi trực tiếp trên Web. | **Không tích hợp sẵn**<br>Không có quy trình soát lỗi chuyên biệt cho tiếng Việt chuyên ngành, phải dùng công cụ ngoài. | **Không hỗ trợ**<br>Chỉ đóng vai trò là kho lưu trữ tệp tĩnh, không có quy trình biên tập và chuyển đổi định dạng. | **Rời rạc & Thủ công**<br>Mất nhiều giờ chuyển đổi thủ công qua lại giữa các phần mềm ngoại tuyến độc lập.         |
| **Bảo mật và Bản quyền số**            | **Chặt chẽ (Đường dẫn bảo mật DRM)**<br>Chỉ cho đọc trực tuyến, tự động hết hạn liên kết sau 15 phút, chặn tải lậu.        | **Hạn chế**<br>Chỉ phân quyền tải tệp PDF thông thường, dễ bị sao chép và phát tán trái phép.                           | **Cơ bản**<br>Chỉ hỗ trợ phân quyền truy cập thư mục, thiếu cơ chế chống sao chụp nâng cao.                        | **Rủi ro cực cao**<br>Lưu trữ đám mây không chặn tải tệp gốc, không chặn chuột phải sao chép, dễ bị phát tán sách. |
| **Tìm kiếm toàn văn**                  | **Siêu tốc (Dưới 3 giây)**<br>Lập chỉ mục tìm kiếm toàn văn sâu đến từng trang sách và highlight kết quả theo ngữ cảnh.    | **Cơ bản**<br>Chỉ tìm kiếm theo từ khóa thư mục (tiêu đề, tác giả) thông thường.                                        | **Trung bình**<br>Hỗ trợ tìm kiếm cơ bản nhưng khó tối ưu hóa cho tiếng Việt chuyên ngành.                         | **Kém**<br>Không hỗ trợ tìm kiếm sâu trong nội dung sách trên diện rộng.                                           |

_Chú thích các từ viết tắt trong bảng:_

- **HCMUS-LDMS (HCMUS Library Document Management & Digitization System):** Hệ thống Quản lý và Số hóa Tài liệu Thư viện Trường Đại học Khoa học Tự nhiên.
- **DRM (Digital Rights Management):** Quản lý bản quyền số, giải pháp ngăn chặn sao chép và tải tập tin trái phép từ trình duyệt web.
- **DSpace:** Phần mềm nguồn mở phục vụ lưu trữ tài liệu số và nghiên cứu học thuật của thư viện.
- **Lạc Việt Vebrary:** Hệ thống phần mềm quản lý và vận hành thư viện tích hợp thương mại do Công ty Cổ phần Tin học Lạc Việt phát triển.
- **FTS (Full-Text Search):** Tìm kiếm toàn văn, cho phép người dùng tra cứu từ khóa chính xác đến từng từ trong toàn bộ nội dung sách.
- **EPUB (Electronic Publication):** Định dạng sách điện tử chuẩn mã nguồn mở, hỗ trợ tự co giãn văn bản (reflowable) để tối ưu hiển thị trên mọi kích thước màn hình thiết bị di động.

---

- **Quy trình thẩm định công nghệ và con người kiểm soát:** Hệ thống LDMS ứng dụng mô hình kết hợp tối ưu: nhận dạng chữ tự động chạy bất đồng bộ phía máy chủ thực hiện nhận dạng thô, sau đó con người (biên tập viên/thủ thư/sinh viên cộng tác viên) đóng vai trò soát lỗi chính tả trực quan trên giao diện chia đôi màn hình trước khi phê duyệt xuất bản chính thức, bảo đảm độ chính xác học thuật đạt tuyệt đối với chi phí thấp nhất.

### 2.4. Phân tích Lợi thế cạnh tranh bền vững (MOAT Analysis)

Thuật ngữ **MOAT** (Hào nước bảo vệ thành trì) là một ẩn dụ trong kinh doanh dùng để chỉ những lợi thế cạnh tranh bền vững, độc quyền mà dự án sở hữu nhằm tự bảo vệ trước sự sao chép hoặc thay thế bởi các giải pháp khác. Mục này phân tích chi tiết 5 yếu tố lợi thế cạnh tranh bền vững của hệ thống HCMUS-LDMS:

#### 2.4.1. Bảng tổng hợp Lợi thế cạnh tranh

| Yếu tố lợi thế cạnh tranh       | Mức độ phòng thủ | Cơ chế vận hành                                                                                                                                                                                             | Chiến lược gia cố                                                                                                                                        |
| :------------------------------ | :--------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1. Nội dung độc quyền**       |    Cực kỳ cao    | Kho tài liệu vật lý của Thư viện HCMUS bao gồm giáo trình tự soạn của giảng viên, tài liệu chuyên ngành độc bản và luận văn nội bộ. Đây là nguồn nội dung gốc độc quyền duy nhất HCMUS sở hữu.              | • Ưu tiên số hóa tài liệu độc bản, giáo trình tự soạn trước.<br>• Vận động giảng viên đóng góp giáo trình số mới trực tiếp lên hệ thống.                 |
| **2. Chi phí chuyển đổi cao**   |    Cực kỳ cao    | Hệ thống tích hợp sâu vào hạ tầng định danh trường, quy trình nghiệp vụ số hóa hàng ngày của thủ thư và kho dữ liệu sách điện tử tìm kiếm toàn văn. Chi phí chuyển đổi sang hệ thống khác cực kỳ lớn.       | • Tiếp tục mở rộng tích hợp với hệ thống quản lý học tập Moodle và cổng thông tin đào tạo của trường.                                                    |
| **3. Hiệu ứng mạng lưới**       |       Cao        | Thêm tài liệu số hóa → Tăng giá trị tra cứu cho sinh viên → Thu hút thêm sinh viên cộng tác viên tình nguyện biên tập nhận dạng chữ → Đẩy nhanh tốc độ số hóa học liệu. | • Thiết kế hệ thống khuyến khích thi đua đóng góp cho sinh viên cộng tác viên.<br>• Cho phép giảng viên nhúng liên kết học liệu trực tiếp vào bài giảng. |
| **4. Lợi thế chi phí**          |       Cao        | Tổng chi phí đầu tư ban đầu cực kỳ thấp nhờ sử dụng công nghệ mã nguồn mở, Cloud VPS và thù lao cộng tác viên sinh viên tối ưu.                                                                             | • Duy trì cam kết sử dụng công nghệ mã nguồn mở.<br>• Ghi nhận tài liệu kỹ thuật đầy đủ để nội bộ tự làm chủ và kế thừa.                                 |
| **5. Lợi thế dữ liệu tích lũy** |    Cực kỳ cao    | Kho sách tương thích động cùng chỉ mục tìm kiếm toàn văn là tài sản dữ liệu tích lũy dần theo thời gian, tạo khoảng cách ngày càng lớn mà đối thủ mới không thể bắt kịp.                                    | • Liên tục mở rộng kho bằng chương trình số hóa giáo trình hàng năm.                                                                                     |

#### 2.4.2. Đánh giá tổng hợp sức mạnh lợi thế cạnh tranh

**Mức độ bền vững tổng thể: Mạnh.**

Sự kết hợp của 5 yếu tố tạo nên hệ thống phòng thủ đa lớp:

- **Lớp 1 — Nội dung không thể thay thế:** Kho tài liệu vật lý độc quyền của HCMUS là nền tảng vững chắc nhất.
- **Lớp 2 — Rào cản gia nhập:** Lợi thế chi phí khiến đối thủ cần đầu tư gấp nhiều lần để xây dựng hệ thống tương đương.
- **Lớp 3 — Rào cản thoát ra:** Chi phí chuyển đổi cao khóa chặt người dùng vào hệ sinh thái LDMS sau khi bàn giao.
- **Lớp 4 — Tăng trưởng tự thân:** Hiệu ứng mạng lưới và dữ liệu tích lũy cùng lớn theo thời gian, làm hệ thống càng sử dụng lâu càng khó bị thay thế.

## 3. Giải pháp đề xuất và Định hướng công nghệ

### 3.1. Mô tả tổng quan giải pháp

Xây dựng một ứng dụng Cổng thông tin Web và Bảng điều khiển nghiệp vụ tự phát triển quản lý vòng đời tài liệu số hóa. Thủ thư quét tài liệu giấy, đẩy lên hệ thống để nhận dạng chữ tự động và biên tập lỗi chính tả trên giao diện trực quan chia đôi màn hình, sau đó đóng gói sách điện tử tương thích động và phát hành cho độc giả đọc trực tuyến bảo mật.

### 3.2. Định hướng kiến trúc công nghệ

Hệ thống tuân thủ kiến trúc Modular Monolith để tối ưu hóa nguồn lực triển khai:

- **Giao diện người dùng:** Xây dựng bằng React SPA, sử dụng thư viện Epub.js làm trình đọc sách tương thích động, tích hợp xác thực tài khoản định danh trường Google OAuth 2.0.
- **Phía máy chủ:** Phát triển bằng FastAPI Monolith, xử lý các tác vụ nhận dạng chữ OCR bất đồng bộ thông qua hàng đợi Backend.
- **Lưu trữ & Cơ sở dữ liệu:** Sử dụng PostgreSQL lưu trữ dữ liệu và lập chỉ mục tìm kiếm toàn văn FTS; sử dụng MinIO làm kho lưu trữ đối tượng và cấp đường dẫn bảo mật giới hạn thời gian.
- **Triển khai:** Đóng gói bằng Docker Compose chạy trực tiếp trên máy chủ đám mây (Cloud VPS) thuê ngoài.

### 3.3. Phạm vi loại trừ cấp cao

Dự án tập trung vào luồng số hóa cốt lõi và đọc trực tuyến an toàn. Các tính năng sau nằm ngoài phạm vi (Out of Scope) của dự án này:

- Trình đọc sách ngoại tuyến (Offline Reader) trên thiết bị di động.
- Tính năng thanh toán thương mại hoặc mua bán bản quyền sách.
- Tích hợp máy quét tự động hoàn toàn phần cứng.

## 4. Phân tích Chi Phí – Lợi Ích (Cost-Benefit Analysis)

### 4.1. Bảng phân tích lợi ích định lượng và định tính

Dự án mang lại hiệu quả kép về cả giá trị định lượng lẫn giá trị định tính:

| Nhóm lợi ích   | Lợi ích cụ thể                                                                                                                                                                                                                                  | Phương pháp đánh giá                                                                    |
| :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------- |
| **Định lượng** | **Tránh chi phí xây dựng kho bãi:** Số hóa giải phóng không gian lưu trữ vật lý.<br>**Tiết kiệm thời gian vận hành:** Tự động hóa quy trình mượn trả và tìm kiếm sách.                                                                          | Tính toán chi phí xây dựng kho bãi mới tránh được và giờ công lao động thủ thư giảm đi. |
| **Định tính**  | **Bảo tồn tri thức độc quyền:** Chuyển tài liệu cũ nát sang định dạng số vĩnh viễn.<br>**Nâng cao hiệu quả học tập:** Tra cứu tức thì, đọc sách responsive mọi lúc mọi nơi.<br>**Làm chủ công nghệ:** Đội ngũ trường tự chủ hoàn toàn hệ thống. | Khảo sát mức độ hài lòng của độc giả và chỉ số chuyển đổi số thư viện ĐHQG-HCM.         |

### 4.2. Ước lượng chi phí đầu tư ban đầu

Tổng chi phí đầu tư ban đầu được tối ưu hóa ở mức tối thiểu:

- Thiết bị quét sách tự chế chuyên dụng: Mua sắm linh kiện thiết bị quét chữ V.
- Chi phí thuê máy chủ đám mây (Cloud VPS) và bổ sung dung lượng lưu trữ.
- Thù lao nhân công số hóa đợt đầu cho sinh viên cộng tác viên.

### 4.3. Ước lượng chi phí vận hành định kỳ

Chi phí vận hành hàng năm bao gồm:

- Chi phí bảo trì phần cứng thiết bị quét và hạ tầng mạng.
- Chi phí điện năng máy chủ và thù lao cộng tác viên số hóa định kỳ.

### 4.4. Mô hình kinh tế tránh chi phí và Điểm hòa vốn

Dự án đạt được điểm hòa vốn nhanh nhờ mô hình tránh chi phí xây dựng kho bãi vật lý mới và tiết kiệm thời gian lao động. Thời gian hoàn vốn dự kiến trong ngắn hạn, mang lại hiệu quả đầu tư thực tế cao cho nhà trường.

## 5. Phân tích các bên liên quan và Phân vai

Để đảm bảo tính khả thi trong vận hành và triển khai thực tế của dự án **HCMUS-LDMS**, cấu trúc phân vai và trách nhiệm của các bên liên quan được hoạch định rõ ràng như sau:

### 5.1. Danh sách các bên liên quan

- **Nhà tài trợ dự án (Ban Giám hiệu nhà trường):** Vai trò: Phê duyệt chủ trương, cấp ngân sách đầu tư và vận hành theo từng giai đoạn, định hướng chiến lược chuyển đổi số của nhà trường. Mức độ ảnh hưởng/quan tâm: Quyền lực cao / Quan tâm cao.
- **Bên thụ hưởng nghiệp vụ (Ban Giám đốc & Đội ngũ Thủ thư):** Vai trò: Cung cấp tài liệu gốc, quản lý quy trình duyệt xuất bản sách điện tử, soát lỗi nhận dạng chữ trên giao diện chia đôi màn hình, tổ chức đội ngũ sinh viên cộng tác viên và vận hành cổng thông tin sau bàn giao. Mức độ ảnh hưởng/quan tâm: Quyền lực cao / Quan tâm cao.
- **Bên thụ hưởng kỹ thuật (Phòng Công nghệ Thông tin):** Vai trò: Thiết lập hạ tầng ảo hóa máy chủ, cài đặt và cấu hình phần mềm lõi, tích hợp định danh tài khoản trường và quản lý chỉ mục tìm kiếm toàn văn. Mức độ ảnh hưởng/quan tâm: Quyền lực trung bình / Quan tâm cao.
- **Cố vấn Pháp lý (Bộ phận Pháp chế trường):** Vai trò: Thẩm định quy chế bản quyền số hóa nội bộ và phê duyệt các điều khoản chia sẻ tài liệu số đảm bảo tuân thủ Luật Sở hữu trí tuệ. Mức độ ảnh hưởng/quan tâm: Quyền lực cao / Quan tâm trung bình.
- **Độc giả (Sinh viên, Giảng viên & Nghiên cứu viên):** Vai trò: Đối tượng sử dụng cuối cùng để tra cứu và đọc học liệu trực tuyến tương thích động trên mọi thiết bị. Mức độ ảnh hưởng/quan tâm: Quyền lực thấp / Quan tâm cao.

### 5.2. Ma trận phân định trách nhiệm

Các ký tự phân định trách nhiệm:

- **R** (Thực hiện trực tiếp): Đơn vị trực tiếp triển khai công việc.
- **A** (Trách nhiệm chính): Đơn vị chịu trách nhiệm cuối cùng cho gói công việc (chỉ có duy nhất một đơn vị chịu trách nhiệm chính).
- **C** (Tham vấn ý kiến): Đơn vị được lấy ý kiến chuyên môn trước khi thực hiện.
- **I** (Nhận thông tin): Đơn vị được thông báo kết quả sau khi hoàn thành.

| Gói công việc phân rã                            | Thư viện  | Phòng CNTT | Giáo vụ Khoa | Bộ phận Pháp chế | Ban Giám hiệu | Độc giả |
| :----------------------------------------------- | :-------: | :--------: | :----------: | :--------------: | :-----------: | :-----: |
| **Gói 1 — Khảo sát & Pháp lý**                   | **A** / R |     R      |      C       |        C         |       I       |    -    |
| **Gói 2 — Thiết lập Phía máy chủ & CSDL**        |     C     | **A** / R  |      -       |        -         |       I       |    -    |
| **Gói 3 — Phát triển Giao diện & Đóng gói sách** |     C     | **A** / R  |      -       |        -         |       I       |    C    |
| **Gói 4 — Số hóa tài liệu**                      | **A** / R |     C      |      C       |        C         |       I       |    -    |
| **Gói 5 — Kiểm thử & Nghiệm thu**                |     R     | **A** / R  |      -       |        -         |       I       |    C    |
| **Gói 6 — Triển khai & Vận hành chính thức**     | **A** / R |     R      |      C       |        -         |       I       |    I    |

_Chú thích các từ viết tắt trong mục:_

- **RACI (Responsible, Accountable, Consulted, Informed):** Ma trận phân định trách nhiệm (Thực hiện trực tiếp, Trách nhiệm chính, Tham vấn ý kiến, Nhận thông tin).
- **WBS (Work Breakdown Structure):** Cấu trúc phân rã công việc của dự án.
- **WP (Work Package):** Gói công việc nhỏ nhất trong cấu trúc phân rã công việc.
- **UAT (User Acceptance Testing):** Kiểm thử chấp nhận người dùng để đánh giá mức độ sẵn sàng bàn giao hệ thống.
- **CSDL (Database):** Cơ sở dữ liệu lưu trữ thông tin của dự án.

### 5.3. Đánh giá tính khả thi từ góc độ quản lý các bên liên quan

Sự phân định rõ ràng vai trò của các bên liên quan là cơ sở vững chắc bảo đảm tính khả thi thực tế của dự án:
1. **Tính khả thi về mặt pháp lý (Legal Feasibility):** Sự tham gia sớm của bộ phận Pháp chế (Gói 1) giúp xây dựng quy chế bản quyền và điều khoản sử dụng chặt chẽ, loại bỏ hoàn toàn các rủi ro pháp lý về sở hữu trí tuệ đối với tài liệu học tập.
2. **Tính khả thi về kỹ thuật và nhân lực (Technical & Resource Feasibility):** Giao trách nhiệm chính (A) cho Phòng CNTT giúp tận dụng nguồn lực kỹ sư chuyên môn cao của trường để làm chủ công nghệ lõi. Đồng thời, việc huy động sinh viên cộng tác viên tham gia số hóa giúp giải quyết triệt để nút thắt về nhân sự vận hành của Thư viện.
3. **Tính khả thi về mặt vận hành (Operational Feasibility):** Thư viện nắm vai trò chịu trách nhiệm chính (A) về quy trình số hóa và bàn giao vận hành (Gói 4, Gói 6) bảo đảm hệ thống mới tích hợp mượt mà vào nghiệp vụ hàng ngày của cán bộ thư viện mà không gây gián đoạn.

---

## 6. Lộ trình triển khai cấp cao

Dự án kéo dài **20 tuần** và chia thành 4 giai đoạn lớn kết hợp kiểm soát cổng phê duyệt (Gating Checkpoints):

- **Giai đoạn 0 — Khảo sát & Pháp lý (Tuần 1–2):** Kiểm kê kho sách tự soạn, bộ phận Pháp chế thẩm định quy chế bản quyền số hóa nội bộ và khảo sát báo giá máy quét chữ V.
- **Giai đoạn 1 — Xây dựng sản phẩm khả thi tối giản & Thí điểm (Tuần 3–12):** Lập trình hệ thống cốt lõi, tích hợp công cụ nhận dạng chữ OCR, đóng gói sách tương thích động, cài đặt lưu trữ và xác thực định danh; tiến hành số hóa thí điểm giáo trình công nghệ thông tin trọng yếu để kiểm thử.
- **Giai đoạn 2 — Số hóa Diện rộng (Tuần 13–18):** Chuyển giao công nghệ cho thư viện, tuyển cộng tác viên sinh viên và tiến hành số hóa hàng loạt giáo trình cốt lõi tiếp theo.
- **Giai đoạn 3 — Nghiệm thu & Bàn giao chính thức (Tuần 19–20):** Kiểm thử nghiệm thu người dùng, đánh giá bảo mật bản quyền số, đào tạo thủ thư và chính thức bàn giao vận hành toàn trường.

---

## 7. Danh mục rủi ro kinh doanh và Biện pháp giảm thiểu

| Loại rủi ro                  |     Mức độ     | Biện pháp giảm thiểu                                                                                      |
| :--------------------------- | :------------: | :-------------------------------------------------------------------------------------------------------- |
| **Bản quyền & Pháp lý**      |    **Cao**     | Chỉ số hóa giáo trình nội bộ HCMUS, phân quyền tài khoản nội bộ trường, khóa tính năng tải xuống tệp gốc. |
| **Chất lượng nhận dạng chữ** | **Trung bình** | Tiền xử lý ảnh quét cùng giao diện chia đôi màn hình cho cộng tác viên sửa lỗi chính tả nhanh.            |
| **Rò rỉ tệp tin gốc**        | **Trung bình** | Sử dụng đường dẫn bảo mật tự hủy sau 15 phút, chặn chuột phải và sao chép văn bản.                        |
| **Nguồn nhân lực quá tải**   | **Trung bình** | Đội ngũ cam kết thời gian chính thức, tuyển thêm cộng tác viên sinh viên theo giờ công.                   |

---

## 8. Kết luận và Khuyến nghị hành động

1. **Phê duyệt chủ trương & ngân sách khởi động:** Thông qua đề xuất dự án và cấp kinh phí mua sắm thiết bị đợt đầu để triển khai Giai đoạn 0.
2. **Ban hành quy chế bản quyền số nội bộ:** Phòng Pháp chế phối hợp Thư viện ban hành quy chế sử dụng tài liệu số hóa trước khi triển khai thực tế.
3. **Triển khai thí điểm sản phẩm Khoa CNTT:** Hoàn thành số hóa các tài liệu công nghệ thông tin đúng tiến độ kế hoạch trước khai giảng năm học mới.
