# KẾ HOẠCH KIỂM THỬ

## Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS (HCMUS-LDMS)

### Thông tin tài liệu

| Trường thông tin  | Nội dung                                |
| ----------------- | --------------------------------------- |
| Mã tài liệu       | `HCMUS-LDMS-TST`                        |
| Tên tài liệu      | Kế hoạch kiểm thử                       |
| Người viết        | Mạch Quốc Tấn                           |
| Người xem xét     | Các thành viên nhóm Sebros              |
| Người xác nhận    | Mạch Quốc Tấn — Quản lý dự án           |
| Trạng thái        | Baseline nội bộ đã được nhóm xác nhận   |
| Thời gian áp dụng | 11 tuần                                 |
| Phạm vi           | 15 hạng mục Bắt buộc, tổng cộng 26 điểm |

### Lịch sử phiên bản

| Phiên bản | Ngày       | Mô tả thay đổi                                                           | Người thực hiện |
| --------- | ---------- | ------------------------------------------------------------------------ | --------------- |
| 1.0       | 22/08/2026 | Xây dựng phạm vi, chiến lược, môi trường và ma trận kiểm thử ban đầu.    | Mạch Quốc Tấn   |
| 2.0       | 24/08/2026 | Đồng bộ baseline, DoD, cổng chất lượng và kiểm thử chấp nhận nội bộ.     | Mạch Quốc Tấn   |
| 2.1       | 24/08/2026 | Đơn giản hóa cấu trúc và câu chữ, giữ đủ nội dung của kế hoạch kiểm thử. | Mạch Quốc Tấn   |
| 2.2       | 24/08/2026 | Đồng bộ Ân Tiến Nguyên An là người phụ trách QA theo Hợp đồng nhóm.      | Mạch Quốc Tấn   |
| 2.3       | 24/08/2026 | Loại bỏ tham chiếu tới tài liệu vận hành chưa thuộc bộ hồ sơ hiện tại.   | Mạch Quốc Tấn   |

## Mục lục

- [1. Mục đích và phạm vi](#1-mục-đích-và-phạm-vi)
- [2. Cách kiểm thử](#2-cách-kiểm-thử)
- [3. Môi trường và dữ liệu](#3-môi-trường-và-dữ-liệu)
- [4. Điều kiện bắt đầu và kết thúc](#4-điều-kiện-bắt-đầu-và-kết-thúc)
- [5. Kiểm thử 15 hạng mục Bắt buộc](#5-kiểm-thử-15-hạng-mục-bắt-buộc)
- [6. Kiểm thử phi chức năng](#6-kiểm-thử-phi-chức-năng)
- [7. Kiểm thử chấp nhận nội bộ](#7-kiểm-thử-chấp-nhận-nội-bộ)
- [8. Ghi nhận kết quả và bằng chứng](#8-ghi-nhận-kết-quả-và-bằng-chứng)
- [9. Quản lý lỗi](#9-quản-lý-lỗi)
- [10. Vai trò, lịch và báo cáo](#10-vai-trò-lịch-và-báo-cáo)
- [11. Điều kiện hoàn thành](#11-điều-kiện-hoàn-thành)
- [12. Tài liệu tham khảo](#12-tài-liệu-tham-khảo)

---

## 1. Mục đích và phạm vi

Tài liệu quy định nhóm kiểm thử gì, kiểm thử như thế nào, ai thực hiện và điều kiện nào cho phép xác nhận kết quả. Mục tiêu là chứng minh 15 hạng mục Bắt buộc đáp ứng tiêu chí chấp nhận, yêu cầu phi chức năng và Tiêu chí hoàn thành (Definition of Done - DoD).

### Trong phạm vi

- Cài đặt và khởi chạy hệ thống.
- Đăng nhập và phân quyền.
- Tải lên, lưu trữ và quản lý trạng thái tài liệu.
- OCR, xem kết quả theo trang và hiệu chỉnh văn bản.
- Quản lý thông tin mô tả.
- Tạo EPUB và kiểm tra điều kiện xuất bản.
- Tìm kiếm, hiển thị kết quả và đọc trực tuyến.
- Kiểm tra lỗi, bảo toàn dữ liệu và quyền truy cập.
- Kiểm thử đơn vị, tích hợp, chức năng, giao diện, hồi quy và chấp nhận nội bộ.

### Ngoài phạm vi

- Hạng mục Nên có hoặc Có thể xem xét chưa được đưa vào baseline.
- Kiểm thử xâm nhập chuyên nghiệp.
- Kiểm thử tải ở quy mô toàn trường.
- Kiểm định pháp lý đối với tài liệu thật.
- Chứng nhận môi trường vận hành chính thức.

Kiểm thử chấp nhận do nhóm Sebros thực hiện nội bộ. Đại diện Thư viện hoặc người dùng bên ngoài chỉ tham gia tham khảo nếu dự án được mở rộng.

## 2. Cách kiểm thử

### 2.1. Nguyên tắc

1. Mỗi tiêu chí chấp nhận có ít nhất một trường hợp kiểm thử thành công.
2. Yêu cầu về quyền, dữ liệu và trạng thái lỗi phải có trường hợp kiểm thử không hợp lệ.
3. Kết quả phải ghi phiên bản mã nguồn, môi trường, dữ liệu, người chạy và thời điểm.
4. “Chưa chạy” không được ghi thành “Đạt”.
5. Người tạo mã tự kiểm tra trước khi tạo Pull Request.
6. Technical Lead xem xét Pull Request trước khi hợp nhất vào `main`.
7. Coding agent có thể hỗ trợ viết kiểm thử; thành viên phải đọc, chạy và xác minh kết quả.
8. Không đưa khóa bí mật hoặc dữ liệu chưa được phép vào bằng chứng.

### 2.2. Các loại kiểm thử

| Loại kiểm thử    | Mục đích                                               | Người thực hiện chính       |
| ---------------- | ------------------------------------------------------ | --------------------------- |
| Đơn vị           | Kiểm tra hàm, logic và thành phần riêng lẻ.            | Người tạo mã                |
| Tích hợp         | Kiểm tra API, cơ sở dữ liệu, kho tệp và công cụ xử lý. | Máy chủ; QA                 |
| Chức năng        | Đối chiếu hệ thống với tiêu chí chấp nhận.             | QA; người phụ trách         |
| Giao diện        | Kiểm tra thao tác, hiển thị, trạng thái và lỗi.        | Giao diện; QA               |
| Phân quyền       | Kiểm tra đúng quyền và trường hợp sai quyền.           | Máy chủ; QA                 |
| Độ tin cậy       | Kiểm tra lỗi, khởi động lại và bảo toàn dữ liệu.       | Máy chủ; Technical Lead; QA |
| Hiệu năng        | Đo thời gian phản hồi trên môi trường xác định.        | QA; máy chủ                 |
| Hồi quy          | Kiểm tra thay đổi không làm hỏng chức năng đã đạt.     | QA; nhóm phát triển         |
| Chấp nhận nội bộ | Kiểm tra luồng chính phù hợp mục tiêu học tập.         | Nhóm Sebros                 |

Nhóm ưu tiên tự động hóa kiểm thử đơn vị, API, phân quyền và hồi quy. Kiểm thử giao diện và chấp nhận nội bộ có thể thực hiện thủ công theo kịch bản.

## 3. Môi trường và dữ liệu

### 3.1. Môi trường

| Môi trường                | Mục đích                                | Điều kiện sử dụng                                    |
| ------------------------- | --------------------------------------- | ---------------------------------------------------- |
| Cục bộ                    | Đơn vị, tích hợp, chức năng và hồi quy. | Thiết lập được theo hướng dẫn và kiểm tra nhanh đạt. |
| Trực tuyến, nếu được dùng | Kiểm tra nhanh và trình bày nội bộ.     | Cấu hình đã được xác minh.                           |
| Vận hành thực tế          | Không thuộc phạm vi dự án học tập.      | Cần kế hoạch và phê duyệt riêng.                     |

Mỗi lần chạy phải ghi hệ điều hành, trình duyệt khi liên quan, mã commit hoặc bản dựng, cấu hình, thời gian và bộ dữ liệu.

### 3.2. Dữ liệu

| Mã    | Dữ liệu                                              | Dùng để kiểm tra                    |
| ----- | ---------------------------------------------------- | ----------------------------------- |
| DS-01 | PDF hoặc ảnh hợp lệ, chữ rõ.                         | Tải lên và OCR thông thường.        |
| DS-02 | PDF nhiều trang, chất lượng ảnh khác nhau.           | Ánh xạ trang và hiệu chỉnh.         |
| DS-03 | Tệp sai loại, rỗng, hỏng hoặc vượt giới hạn.         | Xác thực dữ liệu và thông báo lỗi.  |
| DS-04 | Thông tin mô tả hợp lệ, thiếu và sai định dạng.      | Lưu thông tin và kiểm tra xuất bản. |
| DS-05 | EPUB hợp lệ và EPUB lỗi.                             | Tạo tệp và trình đọc.               |
| DS-06 | Tài liệu nháp, đã xuất bản và riêng tư.              | Tìm kiếm và phân quyền.             |
| DS-07 | Bộ tài liệu có từ khóa và quyền truy cập biết trước. | Tìm kiếm và đo hiệu năng.           |
| DS-08 | Tài khoản thử cho quản trị, biên tập và người đọc.   | Đăng nhập và ma trận quyền.         |

Dữ liệu phải có nguồn và quyền sử dụng phù hợp. Không dùng tài khoản, mật khẩu hoặc tài liệu thật chưa được phép. Khi dữ liệu thay đổi, các kiểm thử liên quan phải chạy lại.

## 4. Điều kiện bắt đầu và kết thúc

### 4.1. Bắt đầu kiểm thử

Chỉ bắt đầu khi:

- yêu cầu và tiêu chí chấp nhận đã rõ;
- Pull Request sẵn sàng hoặc mã đã được hợp nhất theo loại kiểm thử;
- môi trường chạy được và xác định được phiên bản;
- dữ liệu và kết quả mong đợi đã chuẩn bị;
- người chạy và phạm vi đã được xác định.

### 4.2. Tạm dừng và tiếp tục

Tạm dừng phần kiểm thử liên quan khi môi trường không ổn định, sai phiên bản, dữ liệu không hợp lệ, phụ thuộc chính bị lỗi hoặc phát hiện nguy cơ mất dữ liệu hay lộ quyền.

Chỉ tiếp tục sau khi nguyên nhân đã được xử lý, môi trường và dữ liệu được xác minh, và người phụ trách kiểm thử xác nhận kết quả mới có thể đánh giá.

### 4.3. Kết thúc kiểm thử baseline

- Cả 15 hạng mục Bắt buộc có kết quả theo tiêu chí chấp nhận.
- Tổng điểm Hoàn thành đạt 26 điểm.
- Không còn lỗi Nghiêm trọng hoặc Cao chưa xử lý.
- Kiểm thử phân quyền, toàn vẹn dữ liệu và luồng đầu cuối đạt.
- Các trường hợp bắt buộc có trạng thái và bằng chứng rõ ràng.
- Kiểm thử chấp nhận nội bộ có kết luận.
- Báo cáo tổng kết và danh sách lỗi còn lại đã được cập nhật.

## 5. Kiểm thử 15 hạng mục Bắt buộc

| Hạng mục | Nội dung kiểm tra chính                                   | Trường hợp lỗi hoặc biên bắt buộc                       | Trạng thái ban đầu |
| -------- | --------------------------------------------------------- | ------------------------------------------------------- | ------------------ |
| LDMS-001 | Cài đặt, khởi chạy và kiểm tra nhanh hệ thống.            | Thiếu cấu hình hoặc dịch vụ phụ thuộc bị lỗi.           | Chưa chạy          |
| LDMS-002 | Tải tệp hợp lệ và bảo toàn tệp gốc.                       | Tệp sai loại, rỗng, hỏng hoặc vượt giới hạn.            | Chưa chạy          |
| LDMS-003 | Tạo tác vụ OCR và theo dõi trạng thái.                    | Tác vụ lỗi, quá thời gian hoặc dịch vụ khởi động lại.   | Chưa chạy          |
| LDMS-004 | Hiển thị văn bản đúng tài liệu và trang.                  | Chưa có kết quả, thiếu hoặc sai ánh xạ trang.           | Chưa chạy          |
| LDMS-005 | Lưu và mở lại đúng nội dung đã hiệu chỉnh.                | Lưu lỗi, cập nhật đồng thời hoặc tệp gốc bị thay đổi.   | Chưa chạy          |
| LDMS-007 | Tạo EPUB hợp lệ và mở được bằng trình đọc.                | Nội dung lỗi, tạo tệp thất bại hoặc EPUB không hợp lệ.  | Chưa chạy          |
| LDMS-008 | Mở và đọc EPUB trên kích thước màn hình mục tiêu.         | EPUB lỗi, hết phiên hoặc màn hình nhỏ.                  | Chưa chạy          |
| LDMS-009 | Đăng nhập bằng dữ liệu thử và tạo phiên.                  | Sai hoặc thiếu thông tin; phiên hết hạn.                | Chưa chạy          |
| LDMS-010 | Gán vai trò và áp dụng quyền đúng.                        | Vai trò thấp gọi trực tiếp API quản trị.                | Chưa chạy          |
| LDMS-011 | Nhập, sửa và lưu thông tin mô tả hợp lệ.                  | Thiếu trường bắt buộc hoặc sai định dạng.               | Chưa chạy          |
| LDMS-013 | Xuất bản khi nội dung và thông tin đầy đủ.                | Thiếu nội dung, thông tin, EPUB hoặc quyền.             | Chưa chạy          |
| LDMS-014 | Người đủ quyền đọc được tài liệu.                         | Gọi API hoặc liên kết trực tiếp khi không đủ quyền.     | Chưa chạy          |
| LDMS-015 | Tìm theo thông tin mô tả, toàn văn và đúng phạm vi quyền. | Tài liệu nháp, riêng tư hoặc ngoài quyền xuất hiện.     | Chưa chạy          |
| LDMS-016 | Hiển thị kết quả và mở đúng tài liệu.                     | Không có kết quả, lỗi API hoặc thiếu thông tin mô tả.   | Chưa chạy          |
| LDMS-026 | Hiển thị danh sách và trạng thái đúng quyền.              | Danh sách rỗng, lỗi tải, sai phân trang hoặc lọc quyền. | Chưa chạy          |

“Chưa chạy” cho biết đây là kế hoạch, không phải kết quả. Sau khi thực hiện, trạng thái được đổi thành Đạt, Không đạt, Bị chặn hoặc Không áp dụng kèm lý do.

## 6. Kiểm thử phi chức năng

| Mã     | Nội dung           | Cách kiểm tra                                               | Tiêu chí đánh giá                                          |
| ------ | ------------------ | ----------------------------------------------------------- | ---------------------------------------------------------- |
| NFT-01 | Phân quyền         | Kiểm tra tại giao diện và gọi API trực tiếp.                | Trường hợp sai quyền trọng yếu đều bị từ chối.             |
| NFT-02 | Bảo vệ tệp         | Kiểm tra kho riêng tư và liên kết tạm thời.                 | Không truy cập ẩn danh; liên kết hết hạn bị từ chối.       |
| NFT-03 | Xử lý nền          | Chạy OCR/EPUB cùng thao tác giao diện.                      | Giao diện không bị khóa; trạng thái được hiển thị.         |
| NFT-04 | Hiệu năng tìm kiếm | Chạy nhiều lần trên DS-07 và ghi dữ liệu thô.               | Báo cáo nêu dữ liệu, số lượt, trung vị và phân vị 95.      |
| NFT-05 | Khả năng sử dụng   | Thực hiện các kịch bản chấp nhận nội bộ.                    | Người chạy hiểu trạng thái và hoàn thành được luồng chính. |
| NFT-06 | Tương thích        | Kiểm tra trên trình duyệt và kích thước màn hình đã chọn.   | Không có lỗi chặn luồng chính.                             |
| NFT-07 | Khả năng thiết lập | Thiết lập trên môi trường sạch theo hướng dẫn.              | Thành viên khác có thể khởi chạy hệ thống.                 |
| NFT-08 | Toàn vẹn dữ liệu   | Gây lỗi, khởi động lại và đối chiếu dữ liệu.                | Tệp gốc và nội dung đã xác nhận không bị mất.              |
| NFT-09 | Khả năng truy vết  | Rà yêu cầu, hạng mục, Pull Request, kiểm thử và DoD.        | Hạng mục Hoàn thành không thiếu bằng chứng.                |
| NFT-10 | Khả năng truy cập  | Kiểm tra bàn phím, tiêu điểm, nhãn, tương phản và phóng to. | Không có lỗi chặn luồng chính.                             |

Kết quả OCR và hiệu năng chỉ được công bố khi có dữ liệu, môi trường, số lượt chạy và cách tính rõ ràng.

## 7. Kiểm thử chấp nhận nội bộ

| Mã     | Vai trò         | Kịch bản                                       | Kết quả chấp nhận                                 |
| ------ | --------------- | ---------------------------------------------- | ------------------------------------------------- |
| UAT-01 | Biên tập viên   | Đăng nhập, tải tài liệu và theo dõi OCR.       | Tệp được lưu; trạng thái rõ; không mất tệp gốc.   |
| UAT-02 | Biên tập viên   | Xem từng trang, hiệu chỉnh và mở lại nội dung. | Đúng trang; thay đổi được giữ; tệp gốc không đổi. |
| UAT-03 | Biên tập viên   | Nhập thông tin và kiểm tra điều kiện xuất bản. | Dữ liệu thiếu bị chặn và có lý do rõ.             |
| UAT-04 | Người xuất bản  | Tạo EPUB và xuất bản tài liệu hợp lệ.          | EPUB mở được và trạng thái chuyển đúng.           |
| UAT-05 | Người đọc       | Tìm kiếm, mở kết quả và đọc trực tuyến.        | Chỉ thấy tài liệu được phép và đọc được nội dung. |
| UAT-06 | Người sai quyền | Truy cập tài liệu riêng tư hoặc chưa xuất bản. | Không lộ thông tin, nội dung hoặc tệp.            |
| UAT-07 | Biên tập viên   | Gặp lỗi OCR/EPUB và thực hiện lại.             | Lỗi rõ; xử lý lại được; dữ liệu không mất.        |
| UAT-08 | Quản trị viên   | Gán vai trò và kiểm tra quyền mới.             | Quyền có hiệu lực đúng và không vượt phạm vi.     |

Mỗi lần thực hiện phải ghi người chạy, ngày, phiên bản, môi trường, dữ liệu, kết quả thực tế, lỗi liên quan và kết luận. Bảng trên là kế hoạch, không phải kết quả đã đạt.

## 8. Ghi nhận kết quả và bằng chứng

### 8.1. Quy ước mã

| Bản ghi                | Định dạng         |
| ---------------------- | ----------------- |
| Trường hợp chức năng   | `TC-LDMS-xxx-nn`  |
| Kiểm thử phi chức năng | `NFT-nn`          |
| Kiểm thử chấp nhận     | `UAT-nn`          |
| Lỗi                    | `DEF-yyyymmdd-nn` |
| Bằng chứng             | `EVD-yyyymmdd-nn` |

### 8.2. Nội dung cần ghi

Mỗi trường hợp kiểm thử cần có:

- mã, tiêu đề và hạng mục liên quan;
- điều kiện trước và dữ liệu;
- các bước thực hiện;
- kết quả mong đợi và kết quả thực tế;
- trạng thái;
- phiên bản và môi trường;
- người thực hiện và ngày;
- lỗi và bằng chứng liên quan.

### 8.3. Trạng thái

| Trạng thái    | Ý nghĩa                                                   |
| ------------- | --------------------------------------------------------- |
| Chưa chạy     | Chưa thực hiện trên phiên bản và môi trường xác định.     |
| Đạt           | Kết quả thực tế đúng với kết quả mong đợi.                |
| Không đạt     | Có khác biệt cần sửa hoặc chấp nhận ngoại lệ.             |
| Bị chặn       | Không thể hoàn tất do môi trường, dữ liệu hoặc phụ thuộc. |
| Không áp dụng | Không còn phù hợp; phải ghi lý do và người xác nhận.      |

Bằng chứng có thể là kết quả máy, nhật ký đã che thông tin nhạy cảm, ảnh giao diện hoặc biên bản nội bộ. Bằng chứng phải mở được, gắn đúng mã và đủ để người khác kiểm tra lại kết luận.

## 9. Quản lý lỗi

### 9.1. Mức độ

| Mức độ       | Ý nghĩa                                                     | Cách xử lý                                     |
| ------------ | ----------------------------------------------------------- | ---------------------------------------------- |
| Nghiêm trọng | Mất dữ liệu, lộ quyền hoặc luồng chính không dùng được.     | Dừng phần liên quan; sửa và kiểm thử lại ngay. |
| Cao          | Hạng mục Bắt buộc không đạt hoặc ảnh hưởng nhiều chức năng. | Sửa trước khi đạt DoD.                         |
| Trung bình   | Lỗi cục bộ nhưng có cách xử lý tạm thời.                    | Có người phụ trách và thời điểm sửa.           |
| Thấp         | Lỗi trình bày không ảnh hưởng tiêu chí chấp nhận.           | Xử lý theo thứ tự ưu tiên.                     |

### 9.2. Vòng đời

`Mới → Đã phân công → Đang sửa → Chờ kiểm thử lại → Đã đóng`

Kiểm thử lại không đạt thì lỗi được Mở lại. Trường hợp không tái hiện được phải ghi rõ môi trường và các lần thử. Ngoại lệ phải có lý do, tác động, người chấp nhận và thời hạn.

Mỗi lỗi cần ghi mã, phiên bản, môi trường, bước tái hiện, kết quả mong đợi, kết quả thực tế, mức độ, người phụ trách, Pull Request sửa lỗi và kết quả kiểm thử lại.

## 10. Vai trò, lịch và báo cáo

### 10.1. Vai trò

| Hoạt động                     | Người thực hiện                      | Người xác nhận                  |
| ----------------------------- | ------------------------------------ | ------------------------------- |
| Viết và duy trì kế hoạch      | Mạch Quốc Tấn                        | Nhóm Sebros                     |
| Thiết kế trường hợp kiểm thử  | Ân Tiến Nguyên An và người phụ trách | Quản lý dự án                   |
| Kiểm thử đơn vị               | Người tạo mã                         | Technical Lead qua Pull Request |
| Kiểm thử tích hợp, phân quyền | Máy chủ; QA                          | Technical Lead                  |
| Kiểm thử giao diện            | Giao diện; QA                        | Ân Tiến Nguyên An               |
| Kiểm thử hồi quy              | QA; nhóm phát triển                  | Quản lý dự án                   |
| Kiểm thử chấp nhận nội bộ     | Các thành viên nhóm Sebros           | Quản lý dự án                   |
| Rà soát bằng chứng            | Ân Tiến Nguyên An                    | Quản lý dự án                   |

### 10.2. Lịch

| Tuần | Hoạt động chính                                             |
| ---: | ----------------------------------------------------------- |
|    1 | Chuẩn bị môi trường, dữ liệu và trường hợp kiểm thử.        |
|  2–8 | Kiểm thử liên tục theo từng hạng mục và Pull Request.       |
|    4 | Kiểm thử tích hợp nền tảng, phân quyền, tải lên và OCR.     |
|    8 | Kiểm thử toàn bộ chức năng Bắt buộc.                        |
|    9 | Kiểm thử đầu cuối, hồi quy, phân quyền và toàn vẹn dữ liệu. |
|   10 | Sửa lỗi, kiểm thử lại và chuẩn bị chấp nhận nội bộ.         |
|   11 | Kiểm thử chấp nhận, hồi quy cuối và tổng kết.               |

### 10.3. Báo cáo

Báo cáo theo tuần và báo cáo tổng kết cần có:

- phạm vi, phiên bản, môi trường và dữ liệu;
- số trường hợp Chưa chạy, Đạt, Không đạt và Bị chặn;
- lỗi mới, lỗi đã đóng và lỗi còn lại theo mức độ;
- hạng mục bị chặn, rủi ro và ngoại lệ;
- kết luận và hành động tiếp theo.

Các chỉ số chính gồm tỷ lệ trường hợp đã chạy, tỷ lệ đạt, mức bao phủ yêu cầu, lỗi theo mức độ, tỷ lệ kiểm thử lại đạt và mức đầy đủ của bằng chứng. Khi chưa có dữ liệu, báo cáo ghi “Chưa có dữ liệu”, không ghi 0 hoặc Đạt.

### 10.4. Rủi ro kiểm thử

| Rủi ro                           | Cách xử lý                                                |
| -------------------------------- | --------------------------------------------------------- |
| Môi trường không ổn định         | Ghi cấu hình, kiểm tra nhanh và tạm dừng khi cần.         |
| Dữ liệu không đại diện           | Dùng nhiều loại dữ liệu và ghi giới hạn của kết quả.      |
| Thiếu thời gian                  | Kiểm thử liên tục và ưu tiên theo rủi ro.                 |
| Người tạo tự xác nhận            | Technical Lead và QA kiểm tra trước khi đạt DoD.          |
| Coding agent tạo kiểm thử sai    | Thành viên đọc, chạy và đối chiếu với tiêu chí chấp nhận. |
| Thiếu bằng chứng                 | Rà soát bằng chứng tại cổng G3 và G4.                     |
| Pull Request chờ xem xét         | Technical Lead xử lý theo lịch hoặc ủy quyền rõ ràng.     |
| Bằng chứng chứa dữ liệu nhạy cảm | Dùng dữ liệu mẫu và rà soát trước khi lưu.                |

## 11. Điều kiện hoàn thành

Kế hoạch kiểm thử được áp dụng đầy đủ khi:

1. Cả 15 hạng mục Bắt buộc và 26 điểm có kiểm thử phù hợp.
2. Môi trường, dữ liệu và người thực hiện được xác định.
3. Mỗi hạng mục có trường hợp thành công và trường hợp lỗi quan trọng.
4. Mọi thay đổi mã nguồn có Pull Request được Technical Lead xem xét.
5. Không còn lỗi Nghiêm trọng hoặc Cao chưa xử lý.
6. Kiểm thử phân quyền, toàn vẹn dữ liệu và luồng đầu cuối đạt.
7. Kiểm thử chấp nhận nội bộ có kết luận và bằng chứng.
8. Báo cáo tổng kết kiểm thử được cập nhật trong bộ tài liệu dự án.

Việc xác nhận kế hoạch không đồng nghĩa các trường hợp kiểm thử đã được chạy hoặc đã đạt.

## 12. Tài liệu tham khảo

- Yêu cầu phần mềm.
- Product Backlog.
- Kiến trúc phần mềm.
- Định nghĩa quy trình phát triển phần mềm.
- Ước lượng dự án.
- Kế hoạch dự án.
- Bản mô tả công việc.
- Kế hoạch quản lý rủi ro.
- Kế hoạch quản lý chất lượng.
- Hợp đồng nhóm.
- Nhật ký dự án.
