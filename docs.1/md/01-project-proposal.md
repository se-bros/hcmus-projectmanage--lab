# ĐỀ XUẤT DỰ ÁN

## Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS (HCMUS-LDMS)

### Kiểm soát tài liệu

| Trường thông tin        | Nội dung                              |
| :---------------------- | :------------------------------------ |
| **Mã tài liệu**         | `HCMUS-LDMS-PRP`                      |
| **Tên tài liệu**        | Đề xuất dự án                         |
| **Tên dự án**           | HCMUS-LDMS                            |
| **Đơn vị soạn thảo**    | Sebros - Nhóm sinh viên đề xuất dự án |
| **Người xem xét**       | Toàn bộ 6 thành viên nhóm Sebros      |
| **Người phê duyệt**     | Nhóm Sebros                           |
| **Cấp độ bảo mật**      | Nội bộ                                |
| **Trạng thái tài liệu** | Baseline nội bộ đã được nhóm xác nhận |

### Lịch sử phiên bản

| Phiên bản | Ngày phát hành | Mô tả thay đổi                                                                                                                                                                                                                                                           | Người thực hiện |
| :-------: | :------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------- |
|    1.0    |   06/07/2026   | Khởi tạo đề xuất dự án.                                                                                                                                                                                                                                                  | Mạch Quốc Tấn   |
|    2.0    |   14/07/2026   | Chuẩn hóa cấu trúc và chuyển các nội dung phân định trách nhiệm sang tài liệu phù hợp.                                                                                                                                                                                   | Mạch Quốc Tấn   |
|    3.0    |   23/07/2026   | Cập nhật đối chuẩn, định hướng công nghệ và Việt hóa nội dung.                                                                                                                                                                                                           | Mạch Quốc Tấn   |
|    4.0    |   21/08/2026   | Rút gọn về đúng phạm vi đề xuất dự án, bổ sung lộ trình 11 tuần, liên kết tới tài liệu chi tiết, rà soát cách diễn đạt, thay thuật ngữ chưa tự nhiên bằng cách viết tiếng Việt rõ ràng hơn và thống nhất cách gọi tài liệu Ủy nhiệm dự án trong các nội dung tham chiếu. | Mạch Quốc Tấn   |
|    5.0    |   24/08/2026   | Đồng bộ mục đích học tập, xác nhận nội bộ, baseline 15/6/5, cách gọi hoạt động chạy thử và tài liệu tham chiếu dùng cho bản in.                                                                                                                                          | Mạch Quốc Tấn   |

## Mục lục

- [1. Tóm tắt đề xuất](#1-tóm-tắt-đề-xuất)
- [2. Vấn đề và cơ hội](#2-vấn-đề-và-cơ-hội)
- [3. Giải pháp đề xuất](#3-giải-pháp-đề-xuất)
- [4. Mục tiêu và tiêu chí thành công](#4-mục-tiêu-và-tiêu-chí-thành-công)
- [5. Phạm vi dự án](#5-phạm-vi-dự-án)
- [6. Tính khả thi và giá trị dự kiến](#6-tính-khả-thi-và-giá-trị-dự-kiến)
- [7. Các bên tham khảo khi dự án mở rộng](#7-các-bên-tham-khảo-khi-dự-án-mở-rộng)
- [8. Lộ trình tổng quát trong 11 tuần](#8-lộ-trình-tổng-quát-trong-11-tuần)
- [9. Rủi ro chính và điều kiện giả định](#9-rủi-ro-chính-và-điều-kiện-giả-định)
- [10. Sử dụng và cập nhật đề xuất](#10-sử-dụng-và-cập-nhật-đề-xuất)
- [11. Quyết định của nhóm](#11-quyết-định-của-nhóm)
- [12. Tài liệu tham chiếu](#12-tài-liệu-tham-chiếu)

---

## 1. Tóm tắt đề xuất

HCMUS-LDMS là hệ thống trực tuyến hỗ trợ thư viện số hóa tài liệu giấy, xử lý nhận dạng ký tự, biên tập nội dung, đóng gói EPUB và cho phép người dùng nội bộ tìm kiếm, đọc tài liệu.

Đề xuất này ghi nhận chủ trương nội bộ của nhóm về việc xây dựng phiên bản đầu tiên trong **11 tuần** để phục vụ học tập. Baseline gồm 15 hạng mục Bắt buộc; 6 hạng mục Nên có và 5 hạng mục Có thể xem xét được quản lý ngoài baseline. Phiên bản này hỗ trợ toàn bộ quy trình: tiếp nhận tài liệu → nhận dạng ký tự → hiệu chỉnh → xuất bản → tìm kiếm → đọc trực tuyến có kiểm soát quyền truy cập.

Các chi tiết về yêu cầu, chức năng người dùng, kiến trúc, chi phí và kế hoạch thực hiện không lặp lại trong đề xuất này; xem các tài liệu được dẫn tại [Mục 12](#12-tài-liệu-tham-chiếu).

## 2. Vấn đề và cơ hội

### Câu chuyện của Tấn — sinh viên

“Tôi là Tấn, một sinh viên cần tra cứu tài liệu học tập. Mỗi khi cần một cuốn sách chỉ có tại cơ sở khác, tôi phải di chuyển đến thư viện, chờ tìm tài liệu giấy và đọc trong thời gian hoặc không gian thư viện cho phép. Nếu tài liệu được cung cấp dưới dạng ảnh quét hoặc PDF tĩnh, tôi cũng khó đọc trên điện thoại và khó tìm nhanh một khái niệm nằm sâu trong nội dung. Những trở ngại này làm tôi mất nhiều thời gian và hạn chế khả năng tiếp cận học liệu.”

### Câu chuyện của anh Toàn — thủ thư

“Tôi là Toàn, một thủ thư. Công việc của tôi mỗi ngày không chỉ là bảo quản tài liệu giấy, mà còn phải tìm tài liệu theo yêu cầu và hỗ trợ độc giả bằng nhiều thao tác thủ công. Tài liệu cũ có nguy cơ xuống cấp, còn không gian lưu trữ thì có giới hạn. Khi số hóa, tôi vẫn phải kiểm tra chất lượng nhận dạng chữ, sửa lỗi và kiểm soát quyền phát hành. Nếu không có một quy trình thống nhất, các công việc này dễ bị lặp lại và khó theo dõi.”

Hai câu chuyện của Tấn và anh Toàn cho thấy cơ hội của HCMUS-LDMS: xây dựng một luồng số hóa có kiểm duyệt, giúp sinh viên tìm kiếm và đọc tài liệu thuận tiện hơn, đồng thời giúp thư viện bảo tồn tài liệu và quản lý quy trình phát hành tập trung.

### Căn cứ hình thành và phương án thay thế

Đề xuất được hình thành từ bối cảnh sử dụng tài liệu của sinh viên, nhu cầu vận hành của thủ thư, định hướng của Thư viện và Phòng Công nghệ Thông tin, cùng các tài liệu ý tưởng, phạm vi, khả thi và kế hoạch của dự án. Nhu cầu thực tế được mô tả qua câu chuyện của Tấn và anh Toàn. Các căn cứ này được ghi nhận và cụ thể hóa trong các tài liệu tham chiếu ở [Mục 12](#12-tài-liệu-tham-chiếu). Đề xuất hiện chưa sử dụng số liệu khảo sát định lượng; nhóm chỉ bổ sung số liệu khi có dữ liệu thực tế và nguồn kiểm chứng rõ ràng.

Nhóm đã xem xét các phương án thay thế cụ thể:

- **Giải pháp thương mại:** Lạc Việt Vebrary.
- **Hệ thống lưu trữ mã nguồn mở:** DSpace.
- **Phương án ghép công cụ:** Abbyy FineReader, Google Drive và Calibre.

HCMUS-LDMS được đề xuất vì tích hợp nhận dạng ký tự, hiệu chỉnh, xuất bản EPUB, tìm kiếm toàn văn và kiểm soát quyền truy cập trong một quy trình; đồng thời phù hợp hơn với quy trình nội bộ và cho phép nhóm chủ động điều chỉnh hệ thống. Việc so sánh chi tiết được trình bày trong tài liệu **Báo cáo nghiên cứu tính khả thi**.

## 3. Giải pháp đề xuất

Hệ thống được đề xuất gồm hai nhóm chức năng chính:

- **Nghiệp vụ số hóa:** cán bộ hoặc cộng tác viên tải ảnh quét, thực hiện nhận dạng ký tự, đối chiếu ảnh gốc với văn bản nhận dạng, chỉnh sửa và gửi tài liệu qua bước duyệt xuất bản.
- **Tra cứu và đọc tài liệu:** người dùng nội bộ đăng nhập, tìm kiếm theo thông tin tài liệu hoặc nội dung toàn văn, sau đó đọc sách trên trình duyệt với giao diện tương thích nhiều kích thước màn hình.

Định hướng kỹ thuật ở mức đề xuất là React cho giao diện, FastAPI cho máy chủ, PostgreSQL cho tìm kiếm toàn văn và kho đối tượng tương thích S3. Môi trường cục bộ dùng Docker Compose, PostgreSQL và MinIO; môi trường chạy thử trên đám mây có thể dùng Vercel, Render, Neon và Cloudflare R2 sau khi kiểm chứng. Chi tiết được trình bày trong tài liệu **Kiến trúc phần mềm**.

## 4. Mục tiêu và tiêu chí thành công

### Mục tiêu

- Xây dựng và chạy thử phiên bản đầu tiên của hệ thống số hóa tài liệu trong 11 tuần.
- Cho phép người dùng nội bộ tìm kiếm và đọc tài liệu số trên nền tảng trực tuyến.
- Có bước biên tập và phê duyệt trước khi tài liệu được phát hành.
- Giảm rủi ro phát tán tệp gốc bằng xác thực, phân quyền và cơ chế cấp quyền truy cập có thời hạn.

### Tiêu chí thành công

- Luồng quét/nhận dạng ký tự/biên tập/xuất bản hoạt động được trên bộ tài liệu thử nghiệm.
- Tài liệu đã xuất bản có thể được tìm kiếm toàn văn và mở bằng trình đọc trực tuyến.
- Các vai trò chính và quyền truy cập được kiểm tra trước nghiệm thu.
- Phiên bản đầu tiên được kiểm thử, đánh giá nội bộ và hoàn thiện theo kế hoạch 11 tuần.

Điều kiện chấp nhận và tiêu chí hoàn thành được trình bày trong tài liệu **Danh mục công việc**; các điều kiện hoàn thành sản phẩm được trình bày trong tài liệu **Bản mô tả công việc**.

## 5. Phạm vi dự án

### Trong phạm vi

- Quản lý tài khoản và phân quyền người dùng nội bộ.
- Tiếp nhận ảnh quét và tạo nội dung bằng nhận dạng ký tự.
- Giao diện đối chiếu, hiệu chỉnh và phê duyệt nội dung.
- Đóng gói và quản lý tài liệu EPUB.
- Tìm kiếm thông tin tài liệu và tìm kiếm toàn văn.
- Đọc tài liệu trực tuyến trên các kích thước màn hình phổ biến.
- Kiểm thử, triển khai phiên bản đầu tiên và hướng dẫn sử dụng cơ bản.

### Ngoài phạm vi

- Ứng dụng đọc sách ngoại tuyến riêng cho điện thoại iOS/Android.
- Thanh toán, thương mại hóa hoặc bán bản quyền tài liệu.
- Tự động hóa hoàn toàn phần cứng máy quét.
- Số hóa toàn bộ kho tài liệu của thư viện trong phiên bản đầu tiên.
- Các tích hợp ngoài danh sách được chấp thuận trong danh mục công việc.

Phân rã phạm vi, các giả định và yêu cầu cụ thể được trình bày trong tài liệu **Viễn cảnh và phạm vi**.

## 6. Tính khả thi và giá trị dự kiến

### Tính khả thi

- **Kỹ thuật:** sử dụng các công nghệ mã nguồn mở và kiến trúc mô-đun đơn khối phù hợp với quy mô phiên bản đầu tiên.
- **Vận hành:** quy trình được thiết kế quanh vai trò của thư viện, Phòng Công nghệ Thông tin và người đọc; việc phát hành tài liệu vẫn có bước kiểm duyệt của con người.
- **Pháp lý:** quyền số hóa và quyền đọc tài liệu cần được Phòng Pháp chế xác nhận trước khi đưa tài liệu thật vào hệ thống.
- **Thời gian:** phạm vi phiên bản đầu tiên được giới hạn vào các chức năng cốt lõi và triển khai theo từng mốc trong 11 tuần.

Báo cáo đánh giá đầy đủ theo các khía cạnh kỹ thuật, vận hành, pháp lý, nguồn lực và tài chính được trình bày trong tài liệu **Báo cáo nghiên cứu tính khả thi**.

### Giá trị dự kiến

- Bảo tồn và tăng khả năng tiếp cận tài liệu học thuật nội bộ.
- Rút ngắn thao tác tra cứu và giảm phụ thuộc vào việc tìm tài liệu giấy trực tiếp.
- Tạo quy trình số hóa có thể lặp lại, theo dõi và mở rộng sau phiên bản đầu tiên.
- Tăng quyền tự chủ công nghệ của nhà trường thông qua hệ thống có tài liệu và mã nguồn do nhóm quản lý.
- Nếu phiên bản đầu tiên vận hành hiệu quả và được nhà trường chấp thuận, mô hình có thể được giới thiệu cho các trường đại học lân cận trong khối Đại học Quốc gia Thành phố Hồ Chí Minh, qua đó phục vụ thêm nhiều thư viện và sinh viên.

Phân tích nguồn lực và phương pháp ước lượng được trình bày trong tài liệu **Ước lượng dự án**; nội dung chi tiết không lặp lại trong đề xuất này.

## 7. Các bên tham khảo khi dự án mở rộng

| Bên tham khảo                          | Nội dung có thể tham vấn khi dự án mở rộng                      |
| :------------------------------------- | :-------------------------------------------------------------- |
| Ban Giám hiệu                          | Chủ trương và định hướng đầu tư.                                |
| Ban Giám đốc Thư viện và thủ thư       | Quy trình nghiệp vụ, tài liệu nguồn và khả năng sử dụng.        |
| Phòng Công nghệ Thông tin              | Hạ tầng, tích hợp, triển khai và hỗ trợ kỹ thuật.               |
| Bộ phận Pháp chế                       | Quyền số hóa, quyền sử dụng và chính sách truy cập.             |
| Sinh viên, giảng viên, nghiên cứu viên | Nhu cầu tìm kiếm, đọc tài liệu và phản hồi về khả năng sử dụng. |

Các bên trên không tham gia phê duyệt baseline hiện tại. Phân công nội bộ và cơ chế phối hợp được trình bày trong tài liệu **Ủy nhiệm dự án**, **Hợp đồng nhóm** và **Bản mô tả công việc**.

## 8. Lộ trình tổng quát trong 11 tuần

Lộ trình dưới đây là kế hoạch tổng quát cho phiên bản đầu tiên. Dự án quản lý công việc theo luồng liên tục; các hạng mục được chuyển lần lượt qua các trạng thái trên bảng công việc thay vì chia thành các đợt cố định. Nhóm ưu tiên các hạng mục có giá trị cao, giới hạn số việc đang thực hiện và theo dõi tiến độ qua thời gian hoàn thành, các mốc kiểm tra và kết quả nghiệm thu.

| Giai đoạn                                  | Tuần | Kết quả chính                                                                                                                            |
| :----------------------------------------- | :--: | :--------------------------------------------------------------------------------------------------------------------------------------- |
| Khởi động và xác nhận phạm vi              |  1   | Chốt mục tiêu, phạm vi phiên bản đầu tiên, vai trò, tài liệu mẫu và tiêu chí nghiệm thu.                                                 |
| Phân tích, thiết kế và kiểm chứng kỹ thuật | 2–3  | Chốt danh mục công việc ưu tiên, kiến trúc, luồng nhận dạng ký tự/xuất bản và kiểm chứng các rủi ro kỹ thuật chính.                      |
| Phát triển các chức năng lõi               | 4–7  | Hoàn thành lần lượt các hạng mục cho xác thực, quản lý tài liệu, nhận dạng ký tự/biên tập, xuất bản và tìm kiếm/đọc theo luồng liên tục. |
| Tích hợp và hoàn thiện phiên bản đầu tiên  | 8–9  | Tích hợp các mô-đun, xử lý lỗi, hoàn thiện dữ liệu mẫu, phân quyền và trải nghiệm người dùng.                                            |
| Kiểm thử và nghiệm thu người dùng          |  10  | Kiểm thử chức năng, tích hợp, an toàn ở mức phù hợp và nghiệm thu với đại diện nghiệp vụ.                                                |
| Triển khai và đóng dự án                   |  11  | Sửa lỗi nghiệm thu, triển khai phiên bản đầu tiên, hướng dẫn sử dụng, bàn giao và tổng kết.                                              |

Chi tiết thứ tự ưu tiên và điều kiện hoàn thành được trình bày trong **Danh mục công việc**; tình trạng thực tế được ghi trong **Nhật ký dự án**; phương pháp ước lượng được trình bày trong **Ước lượng dự án**.

## 9. Rủi ro chính và điều kiện giả định

| Rủi ro/điều kiện                             | Cách xử lý                                                                                                              |
| :------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------- |
| Quyền số hóa hoặc quyền đọc tài liệu chưa rõ | Chỉ đưa tài liệu đã được xác nhận quyền sử dụng vào thử nghiệm; rà soát pháp lý từ đầu.                                 |
| Chất lượng nhận dạng ký tự không đồng đều    | Dùng bộ tài liệu mẫu để kiểm chứng sớm, tiền xử lý ảnh và giữ bước hiệu chỉnh của con người.                            |
| Phạm vi vượt quá 11 tuần                     | Ưu tiên hạng mục bắt buộc trong danh mục công việc; đưa hạng mục tùy chọn hoặc mở rộng kho tài liệu sang giai đoạn sau. |
| Rò rỉ tệp hoặc truy cập trái phép            | Áp dụng xác thực, phân quyền, giới hạn quyền tải và kiểm tra bảo mật trước nghiệm thu.                                  |
| Thiếu thời gian hoặc nhân lực kiểm duyệt     | Chốt người duyệt nghiệp vụ, chia nhỏ tài liệu thí điểm và theo dõi tiến độ theo tuần.                                   |

Danh mục rủi ro, biện pháp ứng phó và cơ chế theo dõi chi tiết được quản lý trong các tài liệu lập kế hoạch và thực hiện tương ứng.

## 10. Sử dụng và cập nhật đề xuất

Đề xuất là căn cứ để nhóm thống nhất vấn đề, giá trị, phạm vi và quyết định tiếp tục dự án. Sau khi được chấp thuận, nội dung đề xuất được dùng làm đầu vào cho tài liệu viễn cảnh và phạm vi, nghiên cứu khả thi, ủy nhiệm dự án, danh mục công việc và kế hoạch thực hiện.

Đề xuất được xem xét lại khi có thay đổi đáng kể về vấn đề, người dùng, phương án giải pháp, phạm vi, thời gian hoặc điều kiện pháp lý. Mọi thay đổi phải được ghi vào lịch sử phiên bản và đồng bộ với các tài liệu liên quan. Các phiên bản trước đã thể hiện việc nhóm chuẩn hóa nội dung, cập nhật công nghệ, bổ sung đối chuẩn và rút gọn tài liệu.

Việc đánh giá đề xuất tập trung vào năm điểm: vấn đề có cơ sở hay không, giải pháp có phù hợp với nhu cầu hay không, giá trị có hợp lý hay không, phạm vi và lộ trình 11 tuần có khả thi hay không, và rủi ro cùng điều kiện xác nhận đã rõ hay chưa.

## 11. Quyết định của nhóm

Nhóm Sebros đã thống nhất:

1. Thực hiện phiên bản đầu tiên của HCMUS-LDMS trong 11 tuần để phục vụ học tập.
2. Sử dụng baseline gồm 15 hạng mục Bắt buộc, tổng cộng 26 điểm.
3. Chỉ sử dụng tài liệu mẫu có nguồn và quyền sử dụng phù hợp.
4. Tham khảo ý kiến của các bên liên quan bên ngoài nếu dự án có điều kiện mở rộng.

## 12. Tài liệu tham chiếu

- Tài liệu này là nguồn mô tả ý tưởng, vấn đề và bối cảnh đề xuất của dự án.
- Báo cáo nghiên cứu tính khả thi: phân tích tám loại khả thi và kết luận dự án.
- Ủy nhiệm dự án: mục tiêu, quyền hạn, vai trò và ràng buộc.
- Viễn cảnh và phạm vi: phạm vi, yêu cầu tổng quát và nội dung loại trừ.
- Kiến trúc phần mềm: cấu trúc, công nghệ và quyết định kỹ thuật.
- Danh mục công việc: hạng mục, mức ưu tiên, ước lượng và tiêu chí chấp nhận.
- Ước lượng dự án: cơ sở làm thử, điểm và hệ số dự phòng.
- Bản mô tả công việc: sản phẩm bàn giao và điều kiện hoàn thành.
- Nhật ký dự án: tình trạng thực hiện, quyết định và cuộc họp.
