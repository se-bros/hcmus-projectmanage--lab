# VIỄN CẢNH VÀ PHẠM VI DỰ ÁN

## Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS (HCMUS-LDMS)

### Thông tin tài liệu

| Trường thông tin        | Nội dung                              |
| :---------------------- | :------------------------------------ |
| **Mã tài liệu**         | `HCMUS-LDMS-VSD`                      |
| **Tên tài liệu**        | Viễn cảnh và phạm vi dự án            |
| **Tên dự án**           | HCMUS-LDMS                            |
| **Đơn vị soạn thảo**    | Sebros - Nhóm sinh viên đề xuất dự án |
| **Người xem xét**       | Toàn bộ 6 thành viên nhóm Sebros      |
| **Người phê duyệt**     | Nhóm Sebros                           |
| **Cấp độ bảo mật**      | Nội bộ                                |
| **Trạng thái tài liệu** | Baseline nội bộ đã được nhóm xác nhận |

### Lịch sử phiên bản

| Phiên bản | Ngày phát hành | Mô tả thay đổi                                                                                                                                                                                                                                                                                                         | Người thực hiện   |
| :-------: | :------------: | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------- |
|    1.0    |   07/07/2026   | Khởi tạo tài liệu viễn cảnh và phạm vi.                                                                                                                                                                                                                                                                                | Mạch Quốc Tấn     |
|    2.0    |   14/07/2026   | Chuẩn hóa cấu trúc, thuật ngữ và mô tả quy trình hiện tại/tương lai.                                                                                                                                                                                                                                                   | Mạch Quốc Tấn     |
|    3.0    |   17/07/2026   | Cập nhật vai trò người dùng, công nghệ và phạm vi theo đề xuất dự án.                                                                                                                                                                                                                                                  | Ân Tiến Nguyên An |
|    4.0    |   21/08/2026   | Việt hóa toàn bộ, đồng bộ với Đề xuất dự án đã chấp thuận, giới hạn phạm vi cho phiên bản đầu tiên trong 11 tuần, bổ sung phạm vi công việc, phương pháp đánh giá và cách cập nhật tài liệu, loại bỏ mục mô tả quá trình hình thành tài liệu và thống nhất cách gọi tài liệu Ủy nhiệm dự án trong nội dung tham chiếu. | Mạch Quốc Tấn     |
|    5.0    |   24/08/2026   | Đồng bộ mục đích học tập, xác nhận nội bộ, baseline 15/6/5, vai trò bên tham khảo và cách dẫn chiếu tài liệu dùng cho bản in.                                                                                                                                                                                          | Mạch Quốc Tấn     |
|    5.1    |   24/08/2026   | Mô tả chi tiết từng bước của quy trình hiện tại và quy trình đề xuất cho Thủ thư và Sinh viên.                                                                                                                                                                                                                         | Mạch Quốc Tấn     |

## Mục lục

- [1. Giới thiệu](#1-giới-thiệu)
- [2. Viễn cảnh và định vị sản phẩm](#2-viễn-cảnh-và-định-vị-sản-phẩm)
- [3. Người dùng và nhu cầu](#3-người-dùng-và-nhu-cầu)
- [4. Quy trình hiện tại và quy trình đề xuất](#4-quy-trình-hiện-tại-và-quy-trình-đề-xuất)
- [5. Phạm vi sản phẩm](#5-phạm-vi-sản-phẩm)
- [6. Yêu cầu phi chức năng](#6-yêu-cầu-phi-chức-năng)
- [7. Sản phẩm bàn giao và nội dung loại trừ](#7-sản-phẩm-bàn-giao-và-nội-dung-loại-trừ)
- [8. Giả định, phụ thuộc và ràng buộc](#8-giả-định-phụ-thuộc-và-ràng-buộc)
- [9. Tiêu chí thành công](#9-tiêu-chí-thành-công)
- [10. Tài liệu tham chiếu](#10-tài-liệu-tham-chiếu)

---

## 1. Giới thiệu

Tài liệu này xác định viễn cảnh, người dùng, nhu cầu, phạm vi và các yêu cầu định hướng của HCMUS-LDMS. Hệ thống hỗ trợ thư viện số hóa tài liệu giấy, biên tập nội dung nhận dạng ký tự, xuất bản tài liệu EPUB và cung cấp chức năng tìm kiếm, đọc tài liệu trực tuyến cho người dùng nội bộ.

Dự án được thực hiện để phục vụ học tập trong 11 tuần. Baseline gồm 15 hạng mục Bắt buộc, tổng cộng 26 điểm; 6 hạng mục Nên có và 5 hạng mục Có thể xem xét được quản lý ngoài baseline.

Tài liệu này được xây dựng từ **Đề xuất dự án**. Các yêu cầu chi tiết, điều kiện chấp nhận và thứ tự ưu tiên được quản lý trong **Danh mục công việc**.

### 1.1 Căn cứ và tài liệu liên quan

- Đề xuất dự án HCMUS-LDMS.
- Nhu cầu tiếp cận và bảo quản tài liệu học thuật của thư viện.
- Quy định pháp luật liên quan đến quyền tác giả và số hóa tài liệu.
- Định hướng kỹ thuật trong tài liệu **Kiến trúc phần mềm**.
- Các yêu cầu, điều kiện chấp nhận và tiêu chí hoàn thành trong **Danh mục công việc**.

## 2. Viễn cảnh và định vị sản phẩm

### 2.1 Viễn cảnh

HCMUS-LDMS giúp thư viện chuyển một phần tài liệu giấy phù hợp thành tài liệu số có thể tìm kiếm, đọc trực tuyến và quản lý tập trung. Hệ thống hướng tới việc giảm trở ngại khi sinh viên tiếp cận học liệu, hỗ trợ thủ thư kiểm soát quy trình số hóa và bảo vệ tài liệu trong phạm vi quyền sử dụng được chấp thuận.

### Mục tiêu của dự án

- Cung cấp một phiên bản đầu tiên trong 11 tuần, tập trung vào quy trình tiếp nhận, nhận dạng ký tự, hiệu chỉnh, phê duyệt, xuất bản và đọc tài liệu.
- Giúp người dùng nội bộ tìm kiếm và đọc tài liệu số thuận tiện hơn.
- Giúp thư viện quản lý tập trung trạng thái tài liệu, chất lượng nội dung và quyền truy cập.
- Tạo nền tảng có thể tiếp tục mở rộng sau phiên bản đầu tiên mà không làm thay đổi phạm vi đã được chấp thuận.

### 2.2 Định vị sản phẩm

- **Dành cho:** sinh viên, giảng viên, nghiên cứu viên, thủ thư, biên tập viên và quản trị viên của HCMUS.
- **Đang gặp vấn đề:** khó tiếp cận tài liệu giấy ở cơ sở khác, khó tìm nội dung trong tệp ảnh quét, tài liệu có nguy cơ xuống cấp và quy trình số hóa còn nhiều thao tác thủ công.
- **HCMUS-LDMS là:** hệ thống trực tuyến nội bộ quản lý quy trình số hóa, xuất bản và đọc tài liệu.
- **Sản phẩm mang lại:** quy trình tiếp nhận ảnh quét, nhận dạng ký tự, hiệu chỉnh, phê duyệt, xuất bản EPUB, tìm kiếm toàn văn và đọc tài liệu có kiểm soát quyền truy cập.
- **Khác với:** việc lưu trữ tệp ảnh hoặc PDF rời rạc, không có bước hiệu chỉnh tập trung và khó tìm kiếm nội dung.

## 3. Người dùng và nhu cầu

### 3.1 Các bên tham khảo khi dự án mở rộng

| Bên tham khảo                    | Nội dung có thể tham vấn                                   |
| :------------------------------- | :--------------------------------------------------------- |
| Ban Giám hiệu                    | Chủ trương và định hướng đầu tư.                           |
| Ban Giám đốc Thư viện và thủ thư | Quy trình nghiệp vụ, tài liệu nguồn và phát hành tài liệu. |
| Phòng Công nghệ Thông tin        | Hạ tầng, triển khai, bảo trì và hỗ trợ kỹ thuật.           |
| Bộ phận Pháp chế                 | Quyền số hóa, quyền sử dụng và chính sách truy cập.        |
| Người đọc                        | Nhu cầu tìm kiếm, đọc và khả năng sử dụng hệ thống.        |

Các bên trên không tham gia phê duyệt baseline hiện tại. Nhóm chỉ tham khảo ý kiến của họ nếu dự án có điều kiện mở rộng.

### 3.2 Nhóm người dùng

| Nhóm người dùng   | Nhu cầu chính                                                                                                                                 |
| :---------------- | :-------------------------------------------------------------------------------------------------------------------------------------------- |
| **Người đọc**     | Đăng nhập, tìm kiếm thông tin hoặc nội dung tài liệu, đọc trên nhiều kích thước màn hình và lưu dấu vị trí đọc nếu chức năng được chấp thuận. |
| **Thủ thư**       | Tiếp nhận tài liệu, nhập thông tin mô tả, theo dõi trạng thái số hóa, kiểm tra và phê duyệt xuất bản.                                         |
| **Biên tập viên** | Đối chiếu ảnh quét với văn bản nhận dạng, sửa lỗi và gửi tài liệu chờ phê duyệt.                                                              |
| **Quản trị viên** | Quản lý tài khoản, vai trò, danh mục và cấu hình hệ thống.                                                                                    |

### 3.3 Môi trường sử dụng

- Thủ thư, biên tập viên và quản trị viên sử dụng máy tính kết nối mạng tại thư viện hoặc môi trường được nhà trường cho phép.
- Sinh viên, giảng viên và nghiên cứu viên truy cập hệ thống trên máy tính hoặc thiết bị di động thông qua mạng phù hợp với chính sách của nhà trường.
- Phiên bản đầu tiên tập trung vào giao diện trực tuyến; không bao gồm ứng dụng đọc ngoại tuyến riêng cho điện thoại.

### 3.4 Nhu cầu và cách đáp ứng

| Nhóm người dùng | Nhu cầu                                           | Cách hệ thống đáp ứng                                          |
| :-------------- | :------------------------------------------------ | :------------------------------------------------------------- |
| Người đọc       | Tìm và đọc tài liệu thuận tiện hơn.               | Tìm kiếm thông tin, tìm kiếm toàn văn và trình đọc trực tuyến. |
| Thủ thư         | Quản lý quy trình số hóa và kiểm soát chất lượng. | Quản lý trạng thái, thông tin mô tả, hiệu chỉnh và phê duyệt.  |
| Biên tập viên   | Sửa văn bản nhận dạng nhanh và chính xác hơn.     | Màn hình đối chiếu ảnh gốc với văn bản nhận dạng.              |
| Quản trị viên   | Quản lý người dùng và quyền truy cập.             | Quản lý tài khoản, vai trò và quyền theo chức năng.            |

## 4. Quy trình hiện tại và quy trình đề xuất

### 4.1 Quy trình hiện tại

Quy trình dưới đây được mô tả theo bối cảnh mà nhóm ghi nhận cho dự án học tập. Đây chưa phải quy trình chính thức của Thư viện. Nếu dự án được mở rộng, nhóm phải xác minh lại với đơn vị thực tế.

#### 4.1.1 Quy trình hiện tại của Thủ thư

1. **Tiếp nhận tài liệu:** Thủ thư tiếp nhận tài liệu giấy hoặc yêu cầu xử lý tài liệu từ nguồn hiện có.
2. **Kiểm tra thông tin:** Thủ thư kiểm tra tên tài liệu, tác giả, tình trạng vật lý và thông tin quản lý cơ bản.
3. **Xác định quyền sử dụng:** Thủ thư kiểm tra tài liệu có được phép sao chụp, số hóa hoặc cung cấp cho người đọc hay không.
4. **Chuẩn bị bản quét:** Tài liệu được quét thành ảnh hoặc PDF bằng công cụ riêng.
5. **Lưu tệp:** Tệp quét được lưu trong thư mục hoặc kho lưu trữ riêng; thông tin mô tả có thể được ghi ở một công cụ khác.
6. **Kiểm tra thủ công:** Thủ thư mở từng tệp để kiểm tra thiếu trang, sai thứ tự, ảnh mờ hoặc lệch trang.
7. **Xử lý nội dung:** Nếu cần văn bản có thể tìm kiếm, Thủ thư phải dùng công cụ nhận dạng ký tự riêng và tự sửa kết quả.
8. **Theo dõi trạng thái:** Tiến độ nhận dạng, hiệu chỉnh và phê duyệt được theo dõi thủ công, chưa có một luồng trạng thái thống nhất.
9. **Cung cấp tài liệu:** Tài liệu được cung cấp dưới dạng bản giấy, ảnh quét hoặc PDF tùy điều kiện và quyền truy cập.
10. **Xử lý yêu cầu phát sinh:** Khi người đọc báo thiếu trang, khó đọc hoặc không tìm thấy tài liệu, Thủ thư phải kiểm tra lại ở nhiều nguồn.

#### 4.1.2 Quy trình hiện tại của Sinh viên

1. **Xác định nhu cầu:** Sinh viên xác định tên tài liệu, tác giả hoặc chủ đề cần tìm.
2. **Tra cứu ban đầu:** Sinh viên tra cứu thông tin hiện có hoặc liên hệ với Thủ thư để hỏi vị trí tài liệu.
3. **Đến nơi lưu trữ:** Nếu tài liệu chỉ có bản giấy, Sinh viên phải đến cơ sở đang lưu giữ tài liệu.
4. **Xác nhận quyền sử dụng:** Sinh viên thực hiện thủ tục mượn, đọc tại chỗ hoặc truy cập theo quy định hiện có.
5. **Nhận tài liệu:** Sinh viên nhận bản giấy, ảnh quét hoặc PDF nếu tài liệu đã có bản số.
6. **Tìm nội dung:** Với bản giấy hoặc PDF dạng ảnh, Sinh viên phải đọc từng trang vì không thể tìm kiếm toàn văn thuận tiện.
7. **Đọc tài liệu:** Việc đọc trên điện thoại có thể khó khăn do trang quét có kích thước cố định và phải phóng to, thu nhỏ.
8. **Yêu cầu hỗ trợ:** Khi không tìm thấy tài liệu hoặc bản quét có lỗi, Sinh viên liên hệ lại với Thủ thư để được xử lý.

#### 4.1.3 Hạn chế của quy trình hiện tại

- Thông tin mô tả, tệp quét, kết quả nhận dạng và trạng thái xử lý có thể nằm ở nhiều nơi.
- Thủ thư phải thực hiện nhiều bước thủ công và khó theo dõi toàn bộ tiến độ.
- Sinh viên gặp khó khăn khi tài liệu nằm ở cơ sở khác hoặc chỉ được đọc tại chỗ.
- Ảnh quét và PDF dạng ảnh khó đọc trên màn hình nhỏ và không thuận tiện cho tìm kiếm toàn văn.
- Quyền truy cập, phê duyệt và phát hành tài liệu số chưa được quản lý trong một quy trình thống nhất.

### 4.2 Quy trình đề xuất

HCMUS-LDMS đề xuất hai luồng chính cho Thủ thư và Sinh viên. Mỗi người chỉ được thực hiện chức năng phù hợp với vai trò đã được cấp.

#### 4.2.1 Quy trình đề xuất cho Thủ thư

1. **Đăng nhập:** Thủ thư mở hệ thống và đăng nhập bằng tài khoản nội bộ hoặc tài khoản mô phỏng trong môi trường học tập.
2. **Xác thực và phân quyền:** Hệ thống kiểm tra thông tin đăng nhập, xác định vai trò và chỉ hiển thị các chức năng mà Thủ thư được phép sử dụng.
3. **Mở khu vực quản lý:** Thủ thư xem danh sách tài liệu và trạng thái xử lý như mới tạo, đang nhận dạng, đang hiệu chỉnh, chờ phê duyệt hoặc đã xuất bản.
4. **Tạo tài liệu:** Thủ thư tạo hồ sơ mới và nhập thông tin mô tả cơ bản như tên tài liệu, tác giả, loại tài liệu và năm xuất bản.
5. **Tải tệp nguồn:** Thủ thư chọn PDF hoặc ảnh quét thuộc bộ dữ liệu được phép sử dụng và tải lên hệ thống.
6. **Kiểm tra tệp:** Hệ thống kiểm tra định dạng, kích thước và khả năng lưu tệp. Nếu không hợp lệ, hệ thống thông báo lỗi để Thủ thư sửa.
7. **Lưu tệp riêng tư:** Tệp nguồn được lưu ở vùng không công khai; người không có quyền không thể truy cập trực tiếp.
8. **Bắt đầu nhận dạng ký tự:** Thủ thư yêu cầu hệ thống xử lý OCR. Hệ thống tạo tác vụ và hiển thị trạng thái đang chờ, đang xử lý, hoàn thành hoặc thất bại.
9. **Theo dõi và xử lý lỗi:** Nếu tác vụ thất bại, Thủ thư xem thông báo, sửa dữ liệu đầu vào hoặc thực hiện lại theo quyền được cấp.
10. **Hiệu chỉnh nội dung:** Khi OCR hoàn thành, Thủ thư đối chiếu ảnh gốc với văn bản theo từng trang và sửa các lỗi nhận dạng.
11. **Hoàn thiện thông tin:** Thủ thư rà soát lại thông tin mô tả, thứ tự trang và nội dung đã hiệu chỉnh.
12. **Gửi chờ phê duyệt:** Thủ thư chuyển tài liệu sang trạng thái chờ phê duyệt. Người có quyền phê duyệt kiểm tra nội dung và quyền sử dụng.
13. **Xử lý phản hồi:** Nếu tài liệu chưa đạt, hệ thống chuyển lại trạng thái hiệu chỉnh và ghi rõ nội dung cần sửa.
14. **Tạo EPUB:** Khi nội dung đạt yêu cầu, Thủ thư yêu cầu hệ thống tạo EPUB từ văn bản và thông tin đã duyệt.
15. **Kiểm tra EPUB:** Hệ thống kiểm tra tệp EPUB; Thủ thư mở thử để kiểm tra cấu trúc, thứ tự và khả năng đọc.
16. **Xuất bản:** Thủ thư có quyền xuất bản xác nhận tài liệu. Hệ thống chỉ xuất bản khi nội dung, tệp EPUB và điều kiện quyền sử dụng đều hợp lệ.
17. **Lập chỉ mục tìm kiếm:** Hệ thống đưa thông tin mô tả và nội dung được phép tìm kiếm vào chỉ mục.
18. **Theo dõi sau xuất bản:** Thủ thư có thể xem trạng thái, sửa thông tin hoặc ngừng xuất bản khi phát hiện lỗi hay vấn đề quyền truy cập.
19. **Đăng xuất:** Thủ thư đăng xuất sau khi hoàn thành công việc, đặc biệt khi sử dụng thiết bị dùng chung.

#### 4.2.2 Quy trình đề xuất cho Sinh viên

1. **Đăng nhập:** Sinh viên mở hệ thống và đăng nhập bằng tài khoản được cấp hoặc tài khoản mô phỏng trong môi trường học tập.
2. **Xác thực và phân quyền:** Hệ thống kiểm tra tài khoản, xác định vai trò Sinh viên và giới hạn các chức năng quản trị.
3. **Mở trang tìm kiếm:** Sinh viên truy cập khu vực tìm kiếm tài liệu.
4. **Nhập yêu cầu tìm kiếm:** Sinh viên nhập tên tài liệu, tác giả, từ khóa hoặc nội dung cần tìm.
5. **Nhận kết quả:** Hệ thống tìm trong thông tin mô tả và nội dung toàn văn, đồng thời loại bỏ tài liệu mà Sinh viên không được phép xem.
6. **Thu hẹp kết quả:** Sinh viên dùng bộ lọc hoặc điều chỉnh từ khóa để tìm tài liệu phù hợp hơn.
7. **Xem thông tin tài liệu:** Sinh viên chọn một kết quả để xem tên, tác giả, mô tả và trạng thái có thể đọc.
8. **Yêu cầu mở tài liệu:** Sinh viên chọn chức năng đọc trực tuyến.
9. **Kiểm tra quyền truy cập:** Hệ thống kiểm tra tài liệu đã xuất bản hay chưa và Sinh viên có quyền đọc hay không. Nếu không đủ quyền, hệ thống từ chối và hiển thị thông báo phù hợp.
10. **Đọc trực tuyến:** Nếu được phép, hệ thống mở trình đọc EPUB. Sinh viên có thể chuyển trang, xem mục lục và điều chỉnh cách hiển thị trong phạm vi hệ thống hỗ trợ.
11. **Quay lại tìm kiếm:** Sinh viên đóng trình đọc hoặc quay lại danh sách kết quả để chọn tài liệu khác.
12. **Báo lỗi khi cần:** Nếu tài liệu thiếu nội dung, hiển thị sai hoặc không mở được, Sinh viên ghi nhận thông tin lỗi để nhóm xử lý.
13. **Đăng xuất:** Sinh viên đăng xuất sau khi sử dụng, đặc biệt trên thiết bị dùng chung.

Quy trình trên mô tả luồng nghiệp vụ ở mức viễn cảnh và phạm vi. Tiêu chí chấp nhận, trạng thái công việc và trường hợp lỗi chi tiết được quản lý trong **Danh mục công việc**, **Yêu cầu phần mềm** và **Kế hoạch kiểm thử**. Quyết định kỹ thuật được trình bày trong **Kiến trúc phần mềm**.

## 5. Phạm vi sản phẩm

### 5.1 Trong phạm vi phiên bản đầu tiên

- Đăng nhập và quản lý quyền truy cập người dùng nội bộ.
- Quản lý tài liệu và thông tin mô tả cơ bản.
- Tải ảnh quét hoặc tệp tài liệu lên hệ thống.
- Nhận dạng ký tự tiếng Việt ở mức phù hợp với bộ tài liệu thử nghiệm.
- Đối chiếu, hiệu chỉnh và gửi nội dung chờ phê duyệt.
- Phê duyệt và xuất bản tài liệu EPUB.
- Tìm kiếm theo thông tin tài liệu và tìm kiếm toàn văn.
- Đọc tài liệu trực tuyến trên máy tính và thiết bị di động.
- Quản lý trạng thái tài liệu; nhật ký thao tác chi tiết được thực hiện khi hạng mục `LDMS-023` được đưa vào phạm vi.
- Kiểm thử, triển khai phiên bản đầu tiên và hướng dẫn sử dụng cơ bản.

### 5.2 Có thể xem xét sau phiên bản đầu tiên

- Đọc tài liệu ngoại tuyến bằng ứng dụng riêng.
- Trích dẫn tài liệu tự động theo nhiều mẫu.
- Tìm kiếm ngữ nghĩa và hỗ trợ tóm tắt bằng trí tuệ nhân tạo.
- Tích hợp với hệ thống chống đạo văn hoặc các hệ thống đào tạo khác.
- Mở rộng quy mô số hóa sang toàn bộ kho tài liệu.

Các chức năng cụ thể chỉ được đưa vào phạm vi khi có trong **Danh mục công việc** và được nhóm xác nhận.

### 5.3 Phạm vi công việc của dự án

Phạm vi sản phẩm mô tả những gì HCMUS-LDMS cung cấp cho người dùng. Phạm vi công việc mô tả những việc nhóm cần thực hiện để tạo ra và bàn giao sản phẩm đó, gồm:

- Phân tích nhu cầu, xác nhận phạm vi và lập danh mục công việc.
- Thiết kế giao diện, kiến trúc và mô hình dữ liệu phù hợp với phiên bản đầu tiên.
- Phát triển chức năng, tích hợp các mô-đun và cấu hình môi trường triển khai.
- Kiểm thử, sửa lỗi, đánh giá nội bộ và kiểm tra quyền truy cập.
- Viết tài liệu, hướng dẫn sử dụng, triển khai và bàn giao phiên bản đầu tiên.

Các hoạt động vận hành lâu dài, số hóa toàn bộ kho tài liệu và phát triển các chức năng mở rộng không thuộc phạm vi công việc của phiên bản đầu tiên.

## 6. Yêu cầu phi chức năng

### 6.1 Hiệu năng

- Kết quả tìm kiếm toàn văn phải được đo trên bộ dữ liệu và môi trường được ghi nhận; ngưỡng chấp nhận được chốt trước UAT thay vì dùng số liệu chưa đo.
- Các thao tác chính như mở danh sách, xem thông tin và mở trình đọc phải được kiểm thử với dữ liệu, trình duyệt và thời gian phản hồi được ghi lại.
- Tác vụ nhận dạng ký tự có thể chạy nền để không buộc người dùng chờ trên cùng một màn hình.

### 6.2 Khả năng sử dụng

- Giao diện hiển thị được trên máy tính, máy tính bảng và điện thoại.
- Các bước tải tài liệu, hiệu chỉnh, phê duyệt, tìm kiếm và đọc phải có trạng thái rõ ràng.
- Màn hình hiệu chỉnh phải giúp người dùng đối chiếu ảnh gốc với văn bản nhận dạng.
- Giao diện và tài liệu hướng dẫn sử dụng bằng tiếng Việt.

### 6.3 Bảo mật và quyền riêng tư

- Người dùng phải đăng nhập trước khi truy cập chức năng hoặc tài liệu được bảo vệ.
- Quyền truy cập được phân theo vai trò và trạng thái tài liệu.
- Tệp gốc không được cung cấp công khai; đường dẫn truy cập tài liệu phải có thời hạn và được kiểm soát.
- Việc số hóa và phát hành tài liệu phải tuân thủ quyền sử dụng đã được xác nhận.

### 6.4 Độ tin cậy và khả năng phục hồi

- Hệ thống phải ghi nhận lỗi của các tác vụ chính và cho phép xử lý lại khi phù hợp.
- Dữ liệu và tệp quan trọng phải có phương án sao lưu theo điều kiện hạ tầng thực tế.
- Trạng thái tài liệu không được mất khi một tác vụ nhận dạng hoặc xuất bản thất bại.

### 6.5 Khả năng bảo trì và mở rộng

- Mã nguồn, cấu hình và hướng dẫn triển khai phải được quản lý trong kho mã nguồn của dự án.
- Các mô-đun chính cần có ranh giới rõ để có thể thay đổi hoặc mở rộng.
- Công nghệ và cấu hình triển khai phải phù hợp với nguồn lực của nhóm và hạ tầng được cấp.

### 6.6 Tương thích và tài liệu

- Hệ thống hoạt động trên các trình duyệt phổ biến ở phiên bản được nhóm hỗ trợ.
- Có tài liệu hướng dẫn cho người đọc, thủ thư và biên tập viên.
- Có tài liệu kỹ thuật đủ để cài đặt, kiểm thử và bàn giao hệ thống.

## 7. Sản phẩm bàn giao và nội dung loại trừ

### 7.1 Sản phẩm bàn giao

- Mã nguồn giao diện và máy chủ của hệ thống.
- Cấu hình local bằng Docker Compose/PostgreSQL/MinIO; cấu hình demo cloud Vercel/Render/Neon/R2 nếu môi trường này được dùng và smoke test đạt.
- Phiên bản đầu tiên có các chức năng trong phạm vi được chấp thuận.
- Bộ tài liệu hướng dẫn sử dụng, tài liệu kỹ thuật và hướng dẫn triển khai.
- Bộ tài liệu mẫu có nguồn và quyền sử dụng phù hợp để chạy thử và đánh giá.

Danh sách sản phẩm bàn giao, chức năng và điều kiện hoàn thành được trình bày trong **Bản mô tả công việc**.

### 7.2 Nội dung loại trừ

- Ứng dụng đọc sách ngoại tuyến riêng cho điện thoại.
- Thanh toán, thương mại hóa hoặc bán bản quyền tài liệu.
- Tự động hóa hoàn toàn phần cứng máy quét.
- Số hóa toàn bộ kho tài liệu trong phiên bản đầu tiên.
- Tích hợp với hệ thống bên ngoài nếu chưa được đưa vào danh mục công việc.

## 8. Giả định, phụ thuộc và ràng buộc

### 8.1 Giả định

- Nhóm sử dụng bộ tài liệu mẫu có nguồn và quyền sử dụng phù hợp với mục đích học tập.
- Các tài liệu đưa vào thử nghiệm đã được xác nhận quyền sử dụng.
- Ý kiến từ Thư viện chỉ được xem là nguồn tham khảo nếu dự án có điều kiện mở rộng.
- Nhóm có thể sử dụng hạ tầng và công cụ mã nguồn mở phù hợp với phạm vi phiên bản đầu tiên.

### 8.2 Phụ thuộc

- Tiến độ phụ thuộc vào việc thống nhất quyền số hóa và quyền đọc tài liệu.
- Chất lượng nhận dạng phụ thuộc vào chất lượng ảnh quét và loại tài liệu.
- Việc triển khai phụ thuộc vào hạ tầng máy chủ, lưu trữ và tài khoản xác thực được cấp.
- Các yêu cầu chi tiết phụ thuộc vào thứ tự ưu tiên và khả năng thực hiện của nhóm.

### 8.3 Ràng buộc

- Thời gian thực hiện phiên bản đầu tiên là 11 tuần.
- Nhóm quản lý công việc theo luồng liên tục, ưu tiên hạng mục bắt buộc và giới hạn số việc đang thực hiện.
- Phạm vi phải được kiểm soát để không vượt quá nguồn lực, thời gian và hạ tầng được chấp thuận.
- Các nội dung liên quan đến bản quyền phải được xác nhận trước khi phát hành tài liệu thật.

### 8.4 Kiểm soát thay đổi phạm vi

- Mọi yêu cầu bổ sung hoặc loại bỏ chức năng phải được ghi nhận trong danh mục công việc.
- Nhóm phân tích ảnh hưởng của thay đổi đối với mục tiêu, thời gian 11 tuần, nguồn lực, chi phí, chất lượng và các tài liệu liên quan.
- Thay đổi làm ảnh hưởng đáng kể đến phạm vi phiên bản đầu tiên phải được đại diện nhóm và các bên có thẩm quyền xem xét, chấp thuận trước khi thực hiện.
- Sau khi được chấp thuận, nhóm cập nhật danh mục công việc, tài liệu liên quan và lịch sử quyết định; các hạng mục chưa cần thiết được chuyển sang giai đoạn sau.

## 9. Tiêu chí thành công

Phiên bản đầu tiên được xem là đạt mục tiêu khi:

- Quy trình tiếp nhận, nhận dạng, hiệu chỉnh, phê duyệt và xuất bản hoạt động trên bộ tài liệu thử nghiệm.
- Người dùng nội bộ có thể tìm kiếm và đọc tài liệu đã xuất bản.
- Vai trò và quyền truy cập chính được kiểm tra trước nghiệm thu.
- Tài liệu mẫu được bảo vệ theo quyền sử dụng đã được xác nhận.
- Hệ thống được kiểm thử, chạy thử, hướng dẫn sử dụng và hoàn thiện trong 11 tuần.

Tiêu chí chấp nhận chi tiết của từng chức năng được trình bày trong **Danh mục công việc**. Các chỉ số và điều kiện hoàn thành sản phẩm được trình bày trong **Bản mô tả công việc**.

### Cách đánh giá tài liệu và phạm vi

Tài liệu được đánh giá bằng cách đối chiếu với Đề xuất dự án và nhu cầu của các nhóm người dùng. Nhóm kiểm tra các điểm sau:

- Viễn cảnh và mục tiêu có giải quyết đúng vấn đề đã nêu hay không.
- Người dùng, nhu cầu và cách hệ thống đáp ứng có rõ ràng hay không.
- Phạm vi trong và ngoài dự án có đủ cụ thể để tránh mở rộng không kiểm soát hay không.
- Các yêu cầu phi chức năng, giả định, phụ thuộc và ràng buộc có phù hợp với lộ trình 11 tuần hay không.
- Tiêu chí thành công có thể kiểm tra được trong quá trình nghiệm thu hay không.

Kết quả đánh giá được dùng để cập nhật tài liệu, danh mục công việc và các tài liệu lập kế hoạch trước khi nhóm thực hiện các hạng mục liên quan.

### Cách sử dụng và cập nhật tài liệu

Sau khi được chấp thuận, tài liệu này được dùng làm căn cứ để xây dựng danh mục công việc, kiến trúc, ước lượng chi phí và kế hoạch thực hiện. Trong quá trình làm việc, nhóm dùng tài liệu để kiểm tra yêu cầu mới có phù hợp với viễn cảnh và phạm vi đã thống nhất hay không.

Khi có thay đổi về người dùng, nhu cầu, chức năng, thời gian hoặc ràng buộc, nhóm phân tích ảnh hưởng, xin chấp thuận nếu cần, cập nhật lịch sử phiên bản và đồng bộ các tài liệu liên quan. Những chức năng chưa cần thiết cho phiên bản đầu tiên được giữ trong danh mục công việc để xem xét ở giai đoạn sau.

## 10. Tài liệu tham chiếu

- Đề xuất dự án: vấn đề, cơ hội, giá trị và quyết định thực hiện.
- Báo cáo nghiên cứu tính khả thi: đánh giá tám loại khả thi và kết luận dự án.
- Ủy nhiệm dự án: mục tiêu, vai trò, quyền hạn và ràng buộc.
- Kiến trúc phần mềm: các quyết định kỹ thuật, mô-đun, dữ liệu và triển khai.
- Danh mục công việc: hạng mục, điều kiện chấp nhận, mức ưu tiên và ước lượng.
- Ước lượng dự án: cơ sở làm thử, điểm và hệ số dự phòng.
- Bản mô tả công việc: sản phẩm bàn giao và điều kiện hoàn thành.
