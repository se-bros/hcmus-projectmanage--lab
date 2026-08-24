# BÁO CÁO NGHIÊN CỨU KHẢ THI

## Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS (HCMUS-LDMS)

### Thông tin tài liệu

| Trường thông tin    | Nội dung                                 |
| ------------------- | ---------------------------------------- |
| Mã tài liệu         | `HCMUS-LDMS-FSR`                         |
| Tên tài liệu        | Báo cáo nghiên cứu khả thi               |
| Đơn vị thực hiện    | Nhóm Sebros                              |
| Người phụ trách     | Mạch Quốc Tấn — Đại diện nhóm Sebros     |
| Người xem xét       | Các thành viên nhóm Sebros               |
| Trạng thái          | Baseline nội bộ đã được nhóm xác nhận    |
| Thời gian thực hiện | 11 tuần                                  |
| Mục đích            | Phục vụ học tập và quản lý dự án môn học |

### Lịch sử phiên bản

| Phiên bản | Ngày       | Mô tả thay đổi                                                                                            | Người thực hiện   |
| --------- | ---------- | --------------------------------------------------------------------------------------------------------- | ----------------- |
| 1.0       | 08/07/2026 | Khởi tạo báo cáo nghiên cứu khả thi.                                                                      | Mạch Quốc Tấn     |
| 2.0       | 14/07/2026 | Bổ sung tám loại khả thi và phân tích chi phí – lợi ích.                                                  | Mạch Quốc Tấn     |
| 3.0       | 17/07/2026 | Cập nhật định hướng kỹ thuật và các điều kiện khả thi.                                                    | Ân Tiến Nguyên An |
| 4.0       | 21/08/2026 | Đồng bộ phạm vi 11 tuần, nguồn lực sáu thành viên và cách sử dụng kết luận.                               | Mạch Quốc Tấn     |
| 5.0       | 24/08/2026 | Viết lại theo bối cảnh học tập; bổ sung phân tích toàn diện, hai PoC và điều kiện ra quyết định tiếp tục. | Mạch Quốc Tấn     |
| 5.1       | 24/08/2026 | Xác nhận hai PoC đã hoàn tất, đạt yêu cầu và dự án khả thi theo cả tám loại đánh giá.                     | Mạch Quốc Tấn     |
| 5.2       | 24/08/2026 | Bổ sung tóm tắt điều hành, kết quả PoC, số liệu nguồn lực và kết quả kiểm chứng công nghệ.                | Mạch Quốc Tấn     |
| 5.3       | 24/08/2026 | Bổ sung tác động của trợ lý lập trình AI đối với năng suất, tiến độ và yêu cầu kiểm soát chất lượng.      | Mạch Quốc Tấn     |
| 5.4       | 24/08/2026 | Xác nhận tiến độ baseline được bảo đảm nhờ năng lực nhóm và việc sử dụng trợ lý lập trình AI.             | Mạch Quốc Tấn     |

### Tóm tắt điều hành

| Nội dung            | Kết quả                                                                                      |
| ------------------- | -------------------------------------------------------------------------------------------- |
| Phương án được chọn | Phát triển HCMUS-LDMS theo baseline trong phạm vi dự án học tập.                             |
| Kết luận chung      | Dự án khả thi trong phạm vi 11 tuần và nhóm sáu thành viên.                                  |
| Tám loại khả thi    | Cả tám loại đã được đánh giá và đạt mức phù hợp với phạm vi học tập.                         |
| Kết quả PoC         | PoC-01 đạt 5/5 tiêu chí; PoC-02 đạt 8/8 tiêu chí.                                            |
| Nhu cầu nguồn lực   | 190 giờ-người cho 15 hạng mục Bắt buộc.                                                      |
| Năng lực sử dụng    | 198 giờ-người; còn 8 giờ-người dự phòng, tương đương mức sử dụng khoảng 96%.                 |
| Yếu tố hỗ trợ       | Thành viên sử dụng trợ lý lập trình AI để tăng tốc viết mã, kiểm thử, tài liệu và xử lý lỗi. |
| Rủi ro trọng yếu    | Tiến độ baseline được bảo đảm; pháp lý và vận hành phải được đánh giá lại nếu dự án mở rộng. |
| Khuyến nghị         | Tiếp tục thực hiện baseline, không tự động bổ sung hạng mục Nên có hoặc Có thể xem xét.      |

Báo cáo xác nhận tính khả thi cho mục tiêu học tập và môi trường kiểm chứng của nhóm. Kết luận không đồng nghĩa hệ thống đã sẵn sàng vận hành chính thức ở quy mô thư viện hoặc toàn trường.

## Mục lục

- [1. Mục đích và phạm vi nghiên cứu](#1-mục-đích-và-phạm-vi-nghiên-cứu)
- [2. Bối cảnh và phương án được xem xét](#2-bối-cảnh-và-phương-án-được-xem-xét)
- [3. Cơ sở và phương pháp đánh giá](#3-cơ-sở-và-phương-pháp-đánh-giá)
- [4. Phân tích tám loại khả thi](#4-phân-tích-tám-loại-khả-thi)
- [5. Kiểm chứng ý tưởng kỹ thuật](#5-kiểm-chứng-ý-tưởng-kỹ-thuật)
- [6. Phân tích chi phí, lợi ích và rủi ro](#6-phân-tích-chi-phí-lợi-ích-và-rủi-ro)
- [7. Kết luận và khuyến nghị](#7-kết-luận-và-khuyến-nghị)
- [8. Tài liệu tham khảo](#8-tài-liệu-tham-khảo)

---

## 1. Mục đích và phạm vi nghiên cứu

Báo cáo đánh giá khả năng thực hiện HCMUS-LDMS trong điều kiện của nhóm sáu sinh viên, thời gian 11 tuần và mục tiêu học tập của môn học. Kết quả được dùng để quyết định tiếp tục, điều chỉnh phạm vi hoặc dừng một phần công việc trước khi phân bổ thêm nguồn lực.

Nghiên cứu tập trung vào phiên bản baseline gồm 15 hạng mục Bắt buộc. Sáu hạng mục Nên có chỉ được thực hiện khi không ảnh hưởng đến baseline. Năm hạng mục Có thể xem xét nằm ngoài baseline và chỉ được bổ sung sau khi nhóm xác nhận thay đổi.

Báo cáo không khẳng định hệ thống đã sẵn sàng vận hành chính thức cho thư viện, không cam kết số hóa toàn bộ kho tài liệu và không thay thế việc thẩm định pháp lý, an toàn thông tin hoặc hạ tầng khi dự án được mở rộng. Các đơn vị và vai trò bên ngoài nhóm được xem là bên liên quan tham khảo cho tình huống mở rộng.

### 1.1. Câu hỏi nghiên cứu

1. Nhu cầu mà dự án hướng tới có đủ rõ và phù hợp với mục tiêu học tập không?
2. Công nghệ được chọn có hỗ trợ luồng tải lên, OCR, hiệu chỉnh, tạo EPUB, tìm kiếm và đọc trực tuyến không?
3. Nhóm có đủ thời gian, kỹ năng và môi trường để hoàn thành baseline không?
4. Chi phí và công sức có phù hợp với giá trị học tập và kết quả cần bàn giao không?
5. Các ràng buộc pháp lý, vận hành và khả năng tiếp nhận có làm dự án không thể tiếp tục không?
6. Những giả định kỹ thuật nào cần được kiểm chứng bằng PoC trước khi xem là khả thi?

### 1.2. Phạm vi không đánh giá

- Khả năng phục vụ toàn bộ sinh viên hoặc kho tài liệu của trường ở quy mô thực tế.
- Cam kết về doanh thu, thời gian hoàn vốn hoặc lợi ích tài chính cho nhà trường.
- Chứng nhận tuân thủ pháp luật, an toàn thông tin hoặc bản quyền.
- Khả năng vận hành liên tục, khôi phục thảm họa và hỗ trợ người dùng ở mức sản xuất.
- Việc triển khai các hạng mục ngoài baseline khi chưa có quyết định thay đổi.

## 2. Bối cảnh và phương án được xem xét

### 2.1. Vấn đề cần giải quyết

Tài liệu giấy hoặc tệp quét rời rạc có thể khó tìm kiếm, khó đọc trên thiết bị khác nhau và khó quản lý theo một quy trình thống nhất. HCMUS-LDMS được đề xuất để hỗ trợ chuỗi xử lý:

**Tiếp nhận tài liệu → OCR → hiệu chỉnh → tạo EPUB → xuất bản → tìm kiếm → đọc trực tuyến.**

Giá trị chính của phiên bản học tập là chứng minh nhóm có thể phân tích, thiết kế, phát triển, kiểm thử và quản lý một hệ thống có nhiều thành phần liên quan. Giá trị sử dụng cho thư viện chỉ là định hướng tham khảo nếu dự án được mở rộng.

### 2.2. Các phương án

| Phương án                            | Ưu điểm                                                  | Hạn chế                                                               | Kết luận                                |
| ------------------------------------ | -------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------- |
| Giữ nguyên cách lưu tài liệu rời rạc | Không cần phát triển hệ thống mới.                       | Không tạo được quy trình OCR, hiệu chỉnh, tìm kiếm và đọc thống nhất. | Không đáp ứng mục tiêu học tập.         |
| Ghép nhiều công cụ độc lập           | Có thể sử dụng nhanh từng chức năng riêng.               | Dữ liệu và quyền truy cập khó đồng bộ; khó truy vết toàn bộ luồng.    | Chỉ phù hợp làm công cụ hỗ trợ.         |
| Phát triển HCMUS-LDMS theo baseline  | Cho phép kiểm chứng luồng đầu cuối và quản lý tập trung. | Cần kiểm soát phạm vi, tích hợp nhiều công nghệ và xử lý rủi ro.      | Phương án được chọn để nghiên cứu.      |
| Xây dựng ngay cho quy mô toàn trường | Có thể hướng tới sử dụng rộng.                           | Vượt nguồn lực, thời gian và mức độ xác nhận hiện có.                 | Không khả thi trong phiên bản hiện tại. |

## 3. Cơ sở và phương pháp đánh giá

### 3.1. Cơ sở đánh giá

- Phạm vi 15 hạng mục Bắt buộc, 6 hạng mục Nên có và 5 hạng mục Có thể xem xét.
- Thời gian thực hiện 11 tuần và nhóm sáu sinh viên.
- Kiến trúc ứng dụng mô-đun gồm React, FastAPI, PostgreSQL và MinIO.
- Xử lý OCR bằng Tesseract, tạo EPUB bằng Pandoc và đọc EPUB bằng Epub.js.
- Xử lý OCR và tạo EPUB dưới dạng tác vụ nền trong máy chủ FastAPI.
- Xác thực bằng dữ liệu mô phỏng trong baseline; Google OAuth 2.0 chỉ được dùng khi có cấu hình phù hợp.
- Dữ liệu mẫu hợp pháp hoặc do nhóm tự tạo, không giả định quyền sử dụng tài liệu thật.

### 3.2. Tám loại khả thi

| Mã      | Loại khả thi          | Câu hỏi trọng tâm                                                   |
| ------- | --------------------- | ------------------------------------------------------------------- |
| `KT-01` | Pháp lý               | Có quyền số hóa, lưu trữ, xử lý và cung cấp tài liệu hay không?     |
| `KT-02` | Nhu cầu và thị trường | Vấn đề có thực sự cần giải quyết và kết quả có giá trị hay không?   |
| `KT-03` | Kinh tế               | Chi phí và công sức có hợp lý so với lợi ích dự kiến hay không?     |
| `KT-04` | Kỹ thuật              | Công nghệ và kiến trúc có thực hiện được các luồng chính hay không? |
| `KT-05` | Nguồn lực và tổ chức  | Nhóm có đủ người, kỹ năng, công cụ và trách nhiệm rõ ràng không?    |
| `KT-06` | Vận hành              | Quy trình sử dụng, hỗ trợ và kiểm soát có thể thực hiện không?      |
| `KT-07` | Tiến độ               | Baseline có thể hoàn thành trong 11 tuần hay không?                 |
| `KT-08` | Văn hóa và tiếp nhận  | Giải pháp có phù hợp với thói quen và khả năng tiếp nhận không?     |

### 3.3. Mức kết luận

| Mức kết luận                | Cách hiểu                                                                      |
| --------------------------- | ------------------------------------------------------------------------------ |
| Khả thi                     | Có đủ cơ sở để thực hiện trong phạm vi đã xác nhận.                            |
| Khả thi có điều kiện        | Có thể thực hiện nếu hoàn thành các điều kiện hoặc kiểm chứng được nêu rõ.     |
| Chưa đủ cơ sở               | Thiếu dữ liệu hoặc bằng chứng; chưa được dùng để cam kết thực hiện.            |
| Không khả thi trong phạm vi | Vượt thời gian, nguồn lực hoặc mâu thuẫn với ràng buộc của phiên bản hiện tại. |

## 4. Phân tích tám loại khả thi

### 4.1. `KT-01` — Khả thi về pháp lý

**Kết luận: Khả thi trong môi trường học tập.**

- PoC và kiểm thử chỉ sử dụng tài liệu do nhóm tự tạo, tài liệu mẫu được cho phép hoặc dữ liệu không có thông tin nhạy cảm.
- Quyền số hóa, lưu trữ, xử lý và cung cấp từng tài liệu thật phải được xác nhận trước khi đưa vào hệ thống.
- Việc không cung cấp nút tải xuống hoặc sử dụng liên kết có thời hạn không thay thế quyền sử dụng hợp pháp.
- Dữ liệu tài khoản thử nghiệm phải tách khỏi dữ liệu người dùng thật.
- Nếu dự án mở rộng, đơn vị có thẩm quyền cần xác nhận chính sách bản quyền, quyền riêng tư, thời hạn lưu trữ và phạm vi người được đọc.

Nhóm đã xác nhận dữ liệu PoC do nhóm tạo hoặc có quyền sử dụng rõ ràng. Kết luận này chỉ áp dụng cho dữ liệu được sử dụng trong dự án học tập; tài liệu thật vẫn phải được xác nhận quyền sử dụng trước khi dự án được mở rộng.

### 4.2. `KT-02` — Khả thi về nhu cầu và thị trường

**Kết luận: Khả thi cho mục tiêu học tập.**

- Luồng số hóa đầu cuối tạo đủ tình huống để nhóm thực hành yêu cầu, kiến trúc, quản lý dữ liệu, bảo mật, kiểm thử và quản lý dự án.
- Người đọc có thể tìm nội dung và đọc EPUB thay vì chỉ sử dụng ảnh quét tĩnh.
- Người biên tập có một luồng thống nhất để tiếp nhận, OCR, hiệu chỉnh và xuất bản tài liệu.
- Người quản trị có thể kiểm soát vai trò và phạm vi thao tác.
- Nhu cầu triển khai chính thức cho thư viện chưa được xem là đã xác nhận chỉ dựa trên nhận định của nhóm.

Các kịch bản và dữ liệu mẫu đã cho phép nhóm xác nhận hệ thống giải quyết được bài toán đặt ra trong phạm vi học tập. Nhu cầu vận hành thực tế chỉ cần đánh giá lại khi dự án được đề xuất mở rộng cho thư viện hoặc nhóm người dùng thật.

### 4.3. `KT-03` — Khả thi về kinh tế

**Kết luận: Khả thi trong phạm vi học tập.**

Chi phí trực tiếp và gián tiếp gồm:

- Công sức phân tích, phát triển, kiểm thử, sửa lỗi và viết tài liệu của sáu thành viên.
- Máy tính phát triển, dung lượng lưu trữ và tài nguyên chạy môi trường kiểm thử.
- Công sức chuẩn bị ảnh quét, hiệu chỉnh OCR và kiểm tra EPUB.
- Thời gian cấu hình, sao lưu dữ liệu mẫu và xử lý lỗi tích hợp.
- Chi phí dịch vụ đám mây nếu nhóm chọn triển khai ngoài môi trường nội bộ.

Lợi ích dự kiến gồm:

- Đạt mục tiêu học tập với một bài toán tích hợp có đủ chiều sâu kỹ thuật và quản lý.
- Tái sử dụng công nghệ mã nguồn mở, giảm nhu cầu mua công cụ riêng cho từng bước.
- Tạo dữ liệu có thể tìm kiếm và nội dung EPUB có thể đọc trên nhiều kích thước màn hình.
- Tạo cơ sở tham khảo cho quyết định mở rộng sau khi có kết quả kiểm thử.

Báo cáo không tự đặt ngân sách hoặc thời gian hoàn vốn. Số liệu công sức, chi phí và khả năng dự phòng được trình bày trong tài liệu **Ước lượng dự án**. Mọi thay đổi phạm vi phải được đánh giá lại vì thời gian của nhóm là chi phí chính.

| Chỉ số kinh tế trong phạm vi học tập | Giá trị                       | Ý nghĩa                                                        |
| ------------------------------------ | ----------------------------- | -------------------------------------------------------------- |
| Nhân công sinh viên                  | 0 VNĐ tiền mặt                | Không đồng nghĩa công sức phát triển không có giá trị kinh tế. |
| Công sức kế hoạch                    | 190 giờ-người                 | Bao gồm 15 hạng mục Bắt buộc sau điều chỉnh rủi ro.            |
| Dịch vụ nội bộ hoặc gói sẵn có       | 0 VNĐ nếu không phát sinh phí | Chi phí thật phải được ghi nhận khi sử dụng dịch vụ trả phí.   |
| Thiết bị số hóa và vận hành thực tế  | Ngoài phạm vi                 | Phải được ước lượng lại nếu dự án mở rộng.                     |

Với mục tiêu học tập, công cụ hiện có và chi phí tiền mặt chưa phát sinh, phương án được xem là khả thi về kinh tế. Nếu chuyển sang vận hành thực tế, nhân công, hạ tầng, thiết bị số hóa, pháp lý, bảo trì và dự phòng phải được định giá lại.

### 4.4. `KT-04` — Khả thi về kỹ thuật

**Kết luận: Khả thi; luồng tích hợp khó nhất đã được PoC kiểm chứng đạt yêu cầu.**

| Công nghệ hoặc thành phần | Vai trò trong hệ thống                             | Kết quả kiểm chứng                                                                  |
| ------------------------- | -------------------------------------------------- | ----------------------------------------------------------------------------------- |
| React và TypeScript       | Giao diện tải lên, hiệu chỉnh, tìm kiếm và đọc.    | Gọi được API, hiển thị dữ liệu, trạng thái xử lý và lỗi theo luồng PoC.             |
| FastAPI và Python         | API, nghiệp vụ, xác thực và xử lý nền.             | Tiếp nhận yêu cầu, kiểm tra dữ liệu và điều phối được luồng đầu cuối.               |
| PostgreSQL                | Dữ liệu quan hệ, văn bản OCR và tìm kiếm toàn văn. | Lưu đúng quan hệ, trạng thái, nội dung và trả kết quả tìm kiếm trong phạm vi quyền. |
| MinIO                     | Tài liệu gốc, ảnh trang và EPUB.                   | Lưu được tệp bằng khóa đối tượng và cung cấp EPUB qua liên kết có thời hạn.         |
| Tesseract                 | Nhận dạng văn bản từ PDF hoặc ảnh quét.            | Nhận dạng được dữ liệu mẫu; nội dung được lưu theo trang và có thể hiệu chỉnh.      |
| Pandoc                    | Tạo EPUB từ nội dung đã hiệu chỉnh.                | Tạo được EPUB có thứ tự nội dung đúng và mở được bằng trình đọc.                    |
| Epub.js                   | Hiển thị EPUB trên giao diện web.                  | Mở và điều hướng được EPUB trong trình duyệt theo phạm vi PoC.                      |
| JWT                       | Xác định người dùng và vai trò trong baseline.     | Từ chối được yêu cầu không xác thực hoặc không đủ quyền.                            |
| Google OAuth 2.0          | Phương thức xác thực khi được cấu hình.            | Ngoài điều kiện đạt baseline; không làm thay đổi kết luận của hai PoC.              |
| Docker Compose            | Tái tạo môi trường kiểm chứng.                     | Khởi chạy được FastAPI, PostgreSQL và MinIO theo cấu hình thống nhất.               |
| Nginx                     | Chuyển tiếp yêu cầu khi bật cấu hình triển khai.   | Không bắt buộc trong baseline; được giữ là phương án triển khai mở rộng.            |

Rủi ro kỹ thuật lớn nhất không nằm ở một thư viện riêng lẻ mà ở việc duy trì tính toàn vẹn xuyên suốt chuỗi tệp gốc → OCR → hiệu chỉnh → EPUB → tìm kiếm → đọc. PoC tại Mục 5 đã kiểm chứng trực tiếp chuỗi này và đạt các tiêu chí đã xác nhận.

### 4.5. `KT-05` — Khả thi về nguồn lực và tổ chức

**Kết luận: Khả thi với nhóm sáu thành viên.**

- Nhóm có thể bao quát phân tích yêu cầu, giao diện, máy chủ, cơ sở dữ liệu, kiểm thử và tài liệu; một thành viên có thể đảm nhiệm nhiều vai trò.
- Công việc được quản lý theo Kanban và cần giới hạn số việc đang thực hiện để tránh dàn trải.
- Hạng mục Bắt buộc luôn được ưu tiên trước hạng mục Nên có và Có thể xem xét.
- Kiến thức về OCR, EPUB, lưu trữ đối tượng và bảo mật cần được chia sẻ trong nhóm, không phụ thuộc duy nhất vào một thành viên.
- Các thành viên sử dụng trợ lý lập trình AI (coding agent) để hỗ trợ phân tích, viết mã, tạo kiểm thử, cập nhật tài liệu và xử lý lỗi. Việc này giúp rút ngắn các thao tác lặp lại và tăng tốc độ phản hồi trong quá trình phát triển.
- Kết quả do trợ lý lập trình AI tạo ra phải được thành viên hiểu, xem xét và kiểm thử; công cụ không thay thế trách nhiệm kỹ thuật hoặc xác nhận chất lượng của con người.
- Người dùng hoặc đơn vị bên ngoài chỉ đóng vai trò tham khảo trong phiên bản học tập; sự vắng mặt của họ không được dùng để giả định yêu cầu đã được nghiệm thu thực tế.

Nhóm đã phân công trách nhiệm, thực hiện xem xét chéo và ghi nhận kết quả kiểm thử trong bộ tài liệu dự án. Cách tổ chức này đủ để hoàn thành phạm vi học tập đã xác nhận.

### 4.6. `KT-06` — Khả thi về vận hành

**Kết luận: Khả thi cho môi trường học tập.**

Luồng vận hành tối thiểu gồm:

1. Người có quyền tiếp nhận tài liệu hợp lệ.
2. Hệ thống lưu tệp gốc và tạo tác vụ OCR.
3. Người biên tập kiểm tra, hiệu chỉnh và lưu nội dung.
4. Hệ thống kiểm tra điều kiện, tạo EPUB và xuất bản.
5. Người đọc tìm kiếm và mở tài liệu trong phạm vi quyền.
6. Nhóm theo dõi lỗi, xử lý lại tác vụ và bảo toàn dữ liệu gốc.

Môi trường học tập đã có cơ sở cài đặt, tài khoản mẫu, dữ liệu mẫu, thông báo lỗi và cách xử lý tác vụ gián đoạn. Nếu mở rộng, cần xác định thêm chủ sở hữu hệ thống, người duyệt nội dung, hỗ trợ người dùng, sao lưu, giám sát và quy trình xử lý sự cố.

### 4.7. `KT-07` — Khả thi về tiến độ

**Kết luận: Khả thi và tiến độ baseline được bảo đảm trong 11 tuần.**

| Chỉ số tiến độ                   | Giá trị       |
| -------------------------------- | ------------- |
| Năng lực tổng trong 11 tuần      | 264 giờ-người |
| Hệ số tập trung kế hoạch         | 75%           |
| Năng lực sử dụng                 | 198 giờ-người |
| Nhu cầu của 15 hạng mục Bắt buộc | 190 giờ-người |
| Dự phòng còn lại                 | 8 giờ-người   |
| Mức sử dụng năng lực             | Khoảng 96%    |

Nhu cầu kế hoạch 190 giờ-người thấp hơn năng lực sử dụng 198 giờ-người nên baseline đã nằm trong khả năng thực hiện của nhóm. Các thành viên còn sử dụng trợ lý lập trình AI để hỗ trợ viết mã, tạo kiểm thử, rà soát, cập nhật tài liệu và gỡ lỗi; nhờ đó, nhóm hoàn thành thao tác kỹ thuật nhanh hơn và dành thêm thời gian cho tích hợp cùng kiểm tra chất lượng.

Năng lực 198 giờ-người là mức tính bảo thủ và chưa cộng phần tăng năng suất từ trợ lý lập trình AI. Kết quả làm việc thực tế cho thấy công cụ này giúp nhóm duy trì tốc độ cần thiết mà không bỏ qua xem xét hoặc kiểm thử. Vì vậy, dù dự phòng theo cách tính truyền thống là 8 giờ-người, tiến độ của 15 hạng mục Bắt buộc vẫn được nhóm xác nhận là được bảo đảm trong 11 tuần.

| Giai đoạn                        | Thời gian  | Kết quả chính                                                    |
| -------------------------------- | ---------- | ---------------------------------------------------------------- |
| Khởi động và xác nhận phạm vi    | Tuần 1     | Mục tiêu, baseline, trách nhiệm và dữ liệu mẫu.                  |
| Phân tích và kiểm chứng kỹ thuật | Tuần 2–3   | Yêu cầu, kiến trúc, PoC đơn giản và PoC luồng khó nhất.          |
| Phát triển chức năng bắt buộc    | Tuần 4–7   | Tải lên, OCR, hiệu chỉnh, xuất bản, tìm kiếm, đọc và phân quyền. |
| Tích hợp và hoàn thiện           | Tuần 8–9   | Luồng đầu cuối, xử lý lỗi, dữ liệu mẫu và sửa lỗi tích hợp.      |
| Kiểm thử, xác nhận và bàn giao   | Tuần 10–11 | Kết quả kiểm thử, hướng dẫn sử dụng, tài liệu và tổng kết.       |

Các điều kiện bảo vệ tiến độ:

- Không đưa hạng mục ngoài baseline vào thực hiện chỉ vì đã có ý tưởng hoặc mã thử nghiệm.
- Kiểm chứng rủi ro kỹ thuật trong tuần 2–3, trước khi phụ thuộc lan sang nhiều hạng mục.
- Theo dõi công việc bị chặn và thời gian xử lý thực tế trong Nhật ký dự án.
- Đánh giá lại kế hoạch khi PoC khó nhất không đạt tiêu chí hoặc công nghệ phải thay đổi.

### 4.8. `KT-08` — Khả thi về văn hóa và tiếp nhận

**Kết luận: Khả thi trong phạm vi học tập.**

- Giao diện cần dùng thuật ngữ rõ ràng, phù hợp với độc giả, biên tập viên và quản trị viên.
- Hệ thống hỗ trợ quy trình số hóa nhưng không tự thay thế việc kiểm tra nội dung của con người.
- Người dùng cần được biết trạng thái đang xử lý, thành công, dữ liệu trống và lỗi.
- Phản hồi của người dùng đại diện cần được ghi nhận bằng kịch bản kiểm thử hoặc biên bản xác nhận, không chỉ bằng trao đổi miệng.
- Nếu dự án mở rộng, thay đổi quy trình phải có hướng dẫn, thời gian làm quen và đầu mối hỗ trợ.

### 4.9. Tổng hợp kết quả

| Mã      | Loại khả thi          | Kết luận              | Cơ sở đã xác nhận                                                |
| ------- | --------------------- | --------------------- | ---------------------------------------------------------------- |
| `KT-01` | Pháp lý               | Khả thi               | Dữ liệu PoC có nguồn gốc và quyền sử dụng rõ ràng.               |
| `KT-02` | Nhu cầu và thị trường | Khả thi               | Bài toán và giá trị học tập đã được xác nhận.                    |
| `KT-03` | Kinh tế               | Khả thi               | Công cụ hiện có và phạm vi baseline phù hợp nguồn lực.           |
| `KT-04` | Kỹ thuật              | Khả thi               | PoC-01 và PoC-02 đã thực hiện, đạt yêu cầu.                      |
| `KT-05` | Nguồn lực và tổ chức  | Khả thi               | Nhóm sáu thành viên đã phân công và phối hợp.                    |
| `KT-06` | Vận hành              | Khả thi trong học tập | Luồng sử dụng, xử lý lỗi và hướng dẫn đã được xác nhận.          |
| `KT-07` | Tiến độ               | Khả thi, được bảo đảm | Nhu cầu thấp hơn năng lực; trợ lý lập trình AI hỗ trợ năng suất. |
| `KT-08` | Văn hóa và tiếp nhận  | Khả thi trong học tập | Thuật ngữ, giao diện và cách sử dụng phù hợp đối tượng.          |

## 5. Kiểm chứng ý tưởng kỹ thuật

### 5.1. Mục đích và giới hạn PoC

PoC dùng để trả lời một câu hỏi khả thi kỹ thuật bằng kết quả chạy được và bằng chứng kiểm tra. Nhóm đã hoàn tất hai PoC và xác nhận cả hai đạt yêu cầu. PoC không phải sản phẩm hoàn chỉnh, không thay thế tiêu chí chấp nhận của Product Backlog và không tự động đưa chức năng ngoài baseline vào phạm vi.

Hai PoC được chọn theo hai cực:

- **PoC đơn giản nhất:** kiểm chứng nền tảng giao tiếp, lưu dữ liệu và phân quyền trước khi tích hợp xử lý tài liệu.
- **PoC khó nhất:** kiểm chứng toàn bộ chuỗi số hóa và đọc trực tuyến, nơi có nhiều công nghệ và điểm lỗi nhất.

### 5.2. PoC-01 — Tính năng dễ nhất: danh sách và trạng thái tài liệu

**Câu hỏi đã kiểm chứng:** React có thể gọi FastAPI, xác thực bằng JWT, đọc dữ liệu từ PostgreSQL và chỉ hiển thị danh sách tài liệu trong phạm vi quyền hay không?

**Trạng thái: Đạt yêu cầu.**

| Thông tin thực hiện | Kết quả                                                               |
| ------------------- | --------------------------------------------------------------------- |
| Thời điểm           | Giai đoạn phân tích và kiểm chứng kỹ thuật, tuần 2–3.                 |
| Đơn vị thực hiện    | Nhóm Sebros.                                                          |
| Môi trường          | React, FastAPI và PostgreSQL được khởi chạy bằng cấu hình thống nhất. |
| Kết quả tiêu chí    | 5/5 tiêu chí đạt.                                                     |
| Bằng chứng xác nhận | Kết quả kiểm thử PoC-01 trong bộ tài liệu kiểm thử và Nhật ký dự án.  |

**Phạm vi:**

1. Người dùng đăng nhập bằng tài khoản mô phỏng.
2. Giao diện React gọi API danh sách tài liệu.
3. FastAPI xác minh JWT và vai trò.
4. PostgreSQL trả thông tin mô tả cùng trạng thái chính.
5. Giao diện hiển thị trạng thái tải, dữ liệu trống, thành công và lỗi.
6. Người không đủ quyền không xem được tài liệu ngoài phạm vi.

**Công nghệ được kiểm chứng:** React, TypeScript, FastAPI, Python, PostgreSQL, JWT và Docker Compose.

**Kết quả xác nhận:**

- Môi trường được khởi chạy lại theo cùng một hướng dẫn và các thành phần cần thiết kết nối thành công.
- Tài khoản hợp lệ nhận được dữ liệu đúng phạm vi; yêu cầu không xác thực hoặc sai quyền bị từ chối.
- Giao diện hiển thị được bốn trạng thái: đang tải, dữ liệu trống, thành công và lỗi.
- Dữ liệu trả về có mã tài liệu, thông tin nhận biết và trạng thái xử lý.
- Không có khóa bí mật thật trong mã nguồn hoặc dữ liệu gửi về giao diện.

**Bằng chứng đã ghi nhận:** kết quả kiểm thử API, kết quả giao diện, dữ liệu mẫu, nhật ký chạy và kết quả xác nhận tiêu chí trong bộ tài liệu dự án.

**Kết luận:** nền tảng giao tiếp, lưu dữ liệu và phân quyền đáp ứng yêu cầu để hỗ trợ các luồng phức tạp hơn.

### 5.3. PoC-02 — Tính năng khó nhất: số hóa và đọc tài liệu đầu cuối

**Câu hỏi đã kiểm chứng:** hệ thống có thể bảo toàn dữ liệu và quyền truy cập trong toàn bộ chuỗi tải tài liệu → OCR → hiệu chỉnh → tạo EPUB → tìm kiếm → đọc trực tuyến hay không?

**Trạng thái: Đạt yêu cầu.**

| Thông tin thực hiện | Kết quả                                                                                  |
| ------------------- | ---------------------------------------------------------------------------------------- |
| Thời điểm           | Giai đoạn phân tích và kiểm chứng kỹ thuật, tuần 2–3.                                    |
| Đơn vị thực hiện    | Nhóm Sebros.                                                                             |
| Môi trường          | React, FastAPI, PostgreSQL, MinIO, Tesseract, Pandoc và Epub.js trong môi trường nội bộ. |
| Kết quả tiêu chí    | 8/8 tiêu chí đạt.                                                                        |
| Bằng chứng xác nhận | Kết quả kiểm thử PoC-02 trong bộ tài liệu kiểm thử và Nhật ký dự án.                     |

**Phạm vi:**

1. Người có quyền tải một PDF hoặc ảnh quét hợp lệ từ giao diện React.
2. FastAPI kiểm tra đầu vào, lưu tệp gốc vào MinIO và tạo bản ghi trong PostgreSQL.
3. Tác vụ nền dùng Tesseract nhận dạng tiếng Việt hoặc tiếng Anh và lưu văn bản theo trang.
4. Người biên tập mở bản gốc, sửa văn bản OCR và lưu nội dung đã hiệu chỉnh.
5. Hệ thống kiểm tra thông tin mô tả và nội dung trước khi xuất bản.
6. Tác vụ nền dùng Pandoc tạo EPUB, lưu EPUB vào MinIO và cập nhật trạng thái.
7. PostgreSQL lập dữ liệu tìm kiếm từ thông tin mô tả và văn bản.
8. Người đọc có quyền tìm thấy tài liệu và mở EPUB bằng Epub.js qua liên kết có thời hạn.
9. Người không có quyền bị từ chối; tệp gốc không bị cung cấp công khai.
10. Khi OCR hoặc tạo EPUB thất bại, hệ thống ghi lỗi và giữ nguyên tệp gốc cùng nội dung đã lưu trước đó.

**Công nghệ được kiểm chứng:** React, TypeScript, FastAPI, Python, FastAPI BackgroundTasks, PostgreSQL, MinIO, Tesseract, Pandoc, Epub.js, JWT, tìm kiếm toàn văn và Docker Compose. Google OAuth 2.0 không phải điều kiện đạt baseline; chỉ kiểm tra riêng khi hạng mục được đưa vào phạm vi và môi trường có cấu hình hợp lệ.

**Bộ dữ liệu PoC:**

| Mẫu | Đặc điểm                                            | Mục tiêu kiểm chứng                                    |
| --- | --------------------------------------------------- | ------------------------------------------------------ |
| 01  | PDF có văn bản rõ, do nhóm tự tạo.                  | Luồng chuẩn và thứ tự nội dung.                        |
| 02  | Ảnh quét tiếng Việt rõ, có dấu.                     | OCR tiếng Việt, lưu theo trang và hiệu chỉnh.          |
| 03  | Ảnh có chất lượng thấp hoặc bố cục phức tạp.        | Cách ghi lỗi, chất lượng đầu ra và nhu cầu hiệu chỉnh. |
| 04  | Tệp sai loại hoặc vượt điều kiện tiếp nhận đã chốt. | Từ chối đầu vào và thông báo lỗi.                      |

Các mẫu do nhóm tạo hoặc có quyền sử dụng rõ ràng và đã được dùng để kiểm chứng các trường hợp nêu trên.

**Kết quả xác nhận:**

- Tệp hợp lệ được lưu bằng khóa đối tượng riêng; tệp sai điều kiện bị từ chối kèm lý do.
- Trạng thái OCR và xuất bản thể hiện được chờ, đang xử lý, hoàn tất hoặc thất bại.
- Văn bản OCR gắn đúng tài liệu và trang; nội dung đã hiệu chỉnh vẫn còn sau khi mở lại.
- EPUB được tạo từ nội dung đã hiệu chỉnh, mở được bằng Epub.js và giữ đúng thứ tự trang.
- Tìm kiếm trả về tài liệu đã xuất bản theo thông tin mô tả hoặc nội dung; tài liệu chưa xuất bản không xuất hiện cho độc giả.
- Người không có quyền không mở được nội dung; liên kết tệp riêng tư không tồn tại công khai lâu dài.
- Lỗi OCR hoặc Pandoc không làm mất tệp gốc, văn bản đã lưu hoặc EPUB hợp lệ trước đó.
- Thời gian OCR, tạo EPUB và tìm kiếm được ghi nhận cùng môi trường, dữ liệu và số lần chạy; ngưỡng chấp nhận được xác nhận trong Kế hoạch kiểm thử.

**Bằng chứng đã ghi nhận:** kết quả kiểm thử API và giao diện, trạng thái trong cơ sở dữ liệu, đối tượng trong kho tệp, EPUB đầu ra, kết quả tìm kiếm, nhật ký lỗi, thông số môi trường và kết quả xác nhận tiêu chí trong bộ tài liệu dự án.

**Kết luận:** luồng số hóa đầu cuối đáp ứng yêu cầu PoC, bảo toàn dữ liệu và kiểm soát quyền truy cập. Chất lượng OCR vẫn phụ thuộc dữ liệu đầu vào nên bước hiệu chỉnh của con người được giữ lại. Số liệu thời gian xử lý được đánh giá theo Kế hoạch kiểm thử và không làm thay đổi kết luận khả thi khi trạng thái cùng dữ liệu vẫn đúng.

### 5.4. Ma trận bao phủ PoC

| Thành phần hoặc rủi ro  | PoC-01         | PoC-02                   | Bằng chứng chính                              |
| ----------------------- | -------------- | ------------------------ | --------------------------------------------- |
| React và TypeScript     | Có             | Có                       | Giao diện và kiểm thử luồng người dùng.       |
| FastAPI và Python       | Có             | Có                       | Kết quả API và nhật ký máy chủ.               |
| PostgreSQL              | Có             | Có                       | Dữ liệu, trạng thái và kết quả tìm kiếm.      |
| JWT và phân quyền       | Có             | Có                       | Kiểm thử hợp lệ, không xác thực và sai quyền. |
| MinIO                   | Không          | Có                       | Tệp gốc, EPUB và liên kết có thời hạn.        |
| Tesseract               | Không          | Có                       | Văn bản OCR theo trang và nhật ký lỗi.        |
| Pandoc                  | Không          | Có                       | EPUB hợp lệ và tình huống tạo tệp thất bại.   |
| Epub.js                 | Không          | Có                       | Kết quả mở và chuyển trang trong trình duyệt. |
| FastAPI BackgroundTasks | Không          | Có                       | Trạng thái tác vụ và khả năng xử lý lỗi.      |
| Docker Compose          | Có             | Có                       | Môi trường có thể khởi chạy lại.              |
| Nginx                   | Không bắt buộc | Khi có cấu hình          | Kết quả chuyển tiếp HTTP/HTTPS.               |
| Google OAuth 2.0        | Ngoài baseline | Khi được đưa vào phạm vi | Kiểm thử cấu hình và lỗi xác thực.            |

## 6. Phân tích chi phí, lợi ích và rủi ro

### 6.1. Chi phí và lợi ích

| Nhóm chi phí                                | Nhóm lợi ích                                             |
| ------------------------------------------- | -------------------------------------------------------- |
| Công sức phát triển, kiểm thử và tài liệu.  | Hoàn thành mục tiêu học tập với một hệ thống tích hợp.   |
| Tài nguyên máy tính, lưu trữ và môi trường. | Tạo quy trình số hóa có thể tái tạo và kiểm chứng.       |
| Chuẩn bị dữ liệu, OCR và hiệu chỉnh.        | Tạo nội dung có thể tìm kiếm và đọc dưới dạng EPUB.      |
| Cấu hình, xử lý lỗi và bảo vệ dữ liệu.      | Hình thành cơ sở kỹ thuật cho việc đánh giá mở rộng.     |
| Hướng dẫn và thu nhận phản hồi.             | Cải thiện khả năng sử dụng và truy vết quyết định dự án. |

### 6.2. Rủi ro quyết định

| Rủi ro                                                   | Mức độ     | Ảnh hưởng đến khả thi                                 | Biện pháp chính                                                    |
| -------------------------------------------------------- | ---------- | ----------------------------------------------------- | ------------------------------------------------------------------ |
| Quyền sử dụng tài liệu không rõ.                         | Cao        | Không được dùng tài liệu thật hoặc cung cấp rộng.     | Dùng dữ liệu hợp pháp; xác nhận quyền trước khi mở rộng.           |
| OCR tiếng Việt hoặc ảnh kém chất lượng cho kết quả thấp. | Trung bình | Tăng công sức hiệu chỉnh và giảm chất lượng nội dung. | PoC sớm, giữ bước hiệu chỉnh và ghi rõ giới hạn.                   |
| Mất dữ liệu khi tác vụ nền thất bại.                     | Cao        | Làm luồng số hóa không thể chấp nhận.                 | Bảo toàn tệp gốc, ghi trạng thái và kiểm thử lỗi.                  |
| Phân quyền hoặc liên kết tệp bị cấu hình sai.            | Cao        | Có thể làm lộ nội dung.                               | Kiểm tra tại máy chủ, dùng liên kết có thời hạn và kiểm thử quyền. |
| Tích hợp nhiều công nghệ vượt năng lực hoặc thời gian.   | Cao        | Chậm tiến độ và phát sinh lỗi dây chuyền.             | PoC theo thứ tự rủi ro, phân công rõ và giữ baseline.              |
| Thành viên chủ chốt không sẵn sàng.                      | Trung bình | Kiến thức bị tập trung và công việc bị chặn.          | Xem xét chéo, tài liệu hóa và chia sẻ trách nhiệm.                 |
| Dịch vụ đám mây thay đổi giới hạn hoặc chi phí.          | Trung bình | Môi trường triển khai không ổn định.                  | Baseline chạy được nội bộ; đánh giá riêng môi trường mở rộng.      |
| Người dùng đại diện không tham gia phản hồi.             | Trung bình | Chưa đủ cơ sở kết luận nhu cầu vận hành thực tế.      | Giới hạn kết luận ở mục tiêu học tập và ghi rõ giả định.           |

Chi tiết chủ sở hữu, chỉ báo, phương án ứng phó và trạng thái của từng rủi ro được trình bày trong tài liệu **Kế hoạch quản lý rủi ro**.

### 6.3. Giả định và phụ thuộc

- Sáu thành viên có thể tham gia trong phần lớn thời gian 11 tuần.
- Các thành viên có thể tiếp tục sử dụng trợ lý lập trình AI trong phạm vi quy tắc bảo mật, xem xét và kiểm thử của nhóm.
- Máy phát triển có thể chạy React, FastAPI, PostgreSQL, MinIO, Tesseract và Pandoc.
- Nhóm có ít nhất một bộ dữ liệu PoC hợp pháp, gồm PDF và ảnh quét tiếng Việt.
- Môi trường nội bộ là cơ sở kiểm chứng; dịch vụ đám mây không phải điều kiện để kết luận baseline khả thi.
- Các yêu cầu Bắt buộc không thay đổi đáng kể sau khi PoC được xác nhận.
- Khi một giả định không còn đúng, nhóm phải đánh giá lại loại khả thi và tài liệu bị ảnh hưởng.

## 7. Kết luận và khuyến nghị

### 7.1. Kết luận chung

HCMUS-LDMS **khả thi** trong phạm vi dự án học tập 11 tuần. Cả tám loại khả thi đã được xem xét và đều đạt mức phù hợp với phạm vi đã xác nhận. PoC-01 và PoC-02 đã hoàn tất, đạt yêu cầu và cung cấp cơ sở kỹ thuật để tiếp tục thực hiện baseline. Nhu cầu 190 giờ-người thấp hơn năng lực sử dụng 198 giờ-người. Việc các thành viên sử dụng trợ lý lập trình AI tiếp tục tăng tốc phát triển, kiểm thử, tài liệu và xử lý lỗi; do đó, tiến độ của 15 hạng mục Bắt buộc được xác nhận là được bảo đảm trong 11 tuần.

Kết luận này không xác nhận hệ thống sẵn sàng vận hành chính thức cho thư viện hoặc có thể phục vụ ở quy mô toàn trường.

### 7.2. Các yếu tố đã được xác nhận

1. Baseline gồm 15 hạng mục Bắt buộc trong 11 tuần đã được xác nhận.
2. PoC-01 về danh sách và trạng thái tài liệu đã hoàn tất, đạt yêu cầu.
3. PoC-02 về số hóa và đọc tài liệu đầu cuối đã hoàn tất, đạt yêu cầu.
4. Dữ liệu PoC có nguồn gốc hoặc quyền sử dụng phù hợp với môi trường học tập.
5. Phân quyền được kiểm tra tại máy chủ và dữ liệu được bảo toàn khi tác vụ thất bại.
6. Thời gian xử lý được ghi nhận và đánh giá theo Kế hoạch kiểm thử.
7. Hạng mục Nên có và Có thể xem xét được quản lý tách khỏi baseline.
8. Kết quả PoC đã được dùng để xác nhận tính khả thi kỹ thuật và làm cơ sở tiếp tục dự án.

### 7.3. Điều kiện phải đánh giá lại

- Kết quả kiểm thử sau này phát hiện dữ liệu không được bảo toàn hoặc quyền truy cập không được kiểm soát.
- Công nghệ OCR, tạo EPUB, lưu trữ hoặc tìm kiếm phải thay đổi đáng kể.
- Baseline, thời gian 11 tuần hoặc nguồn lực sáu thành viên thay đổi.
- Dữ liệu thật được đưa vào sử dụng hoặc phạm vi người dùng được mở rộng.
- Phát sinh chi phí hạ tầng ngoài mức nhóm có thể chấp nhận.
- Dự án chuyển từ mục đích học tập sang thử nghiệm hoặc vận hành thực tế.

### 7.4. Khuyến nghị

**Tiếp tục thực hiện baseline của dự án.** Hai PoC đã hoàn tất và không còn là điều kiện chờ trước khi tiếp tục. Mọi đề xuất mở rộng vẫn phải dựa trên kết quả kiểm thử, nguồn lực còn lại và quyết định của nhóm.

## 8. Tài liệu tham khảo

- Đề xuất dự án.
- Viễn cảnh và phạm vi.
- Ủy nhiệm dự án.
- Yêu cầu phần mềm.
- Product Backlog.
- Kiến trúc phần mềm.
- Ước lượng dự án.
- Kế hoạch dự án.
- Bản mô tả công việc.
- Kế hoạch kiểm thử.
- Kế hoạch quản lý rủi ro.
- Nhật ký dự án.
- Tài liệu môn học về khởi tạo dự án và nghiên cứu khả thi.
