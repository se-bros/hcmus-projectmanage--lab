# KẾ HOẠCH QUẢN LÝ RỦI RO

## Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS (HCMUS-LDMS)

### Thông tin tài liệu

| Trường thông tin  | Nội dung                                |
| ----------------- | --------------------------------------- |
| Mã tài liệu       | `HCMUS-LDMS-RSK`                        |
| Tên tài liệu      | Kế hoạch quản lý rủi ro                 |
| Người phụ trách   | Mạch Quốc Tấn — Quản lý dự án           |
| Người xem xét     | Các thành viên nhóm Sebros              |
| Trạng thái        | Baseline nội bộ đã được nhóm xác nhận   |
| Thời gian áp dụng | 11 tuần                                 |
| Phạm vi           | 15 hạng mục Bắt buộc, tổng cộng 26 điểm |

### Lịch sử phiên bản

| Phiên bản | Ngày       | Mô tả thay đổi                                                            | Người thực hiện |
| --------- | ---------- | ------------------------------------------------------------------------- | --------------- |
| 1.0       | 22/08/2026 | Khởi tạo danh sách rủi ro và phương pháp đánh giá.                        | Mạch Quốc Tấn   |
| 2.0       | 24/08/2026 | Viết lại theo baseline, hệ số dự phòng 2,5, Pull Request và coding agent. | Mạch Quốc Tấn   |
| 2.1       | 24/08/2026 | Loại bỏ tham chiếu tới tài liệu vận hành chưa thuộc bộ hồ sơ hiện tại.    | Mạch Quốc Tấn   |

## Mục lục

- [1. Mục đích](#1-mục-đích)
- [2. Nguyên tắc quản lý](#2-nguyên-tắc-quản-lý)
- [3. Phương pháp đánh giá](#3-phương-pháp-đánh-giá)
- [4. Vai trò và trách nhiệm](#4-vai-trò-và-trách-nhiệm)
- [5. Danh sách rủi ro](#5-danh-sách-rủi-ro)
- [6. Kế hoạch ứng phó](#6-kế-hoạch-ứng-phó)
- [7. Theo dõi và báo cáo](#7-theo-dõi-và-báo-cáo)
- [8. Dự phòng tiến độ](#8-dự-phòng-tiến-độ)
- [9. Rủi ro khi dự án mở rộng](#9-rủi-ro-khi-dự-án-mở-rộng)
- [10. Điều kiện chấp nhận và đóng rủi ro](#10-điều-kiện-chấp-nhận-và-đóng-rủi-ro)
- [11. Tài liệu tham khảo](#11-tài-liệu-tham-khảo)

---

## 1. Mục đích

Tài liệu xác định cách nhóm nhận diện, đánh giá, theo dõi và xử lý những sự kiện không chắc chắn có thể ảnh hưởng đến phạm vi, tiến độ, chất lượng, dữ liệu hoặc bảo mật của dự án.

Kế hoạch áp dụng cho baseline gồm 15 hạng mục Bắt buộc trong 11 tuần. Các bên ngoài nhóm chỉ được xem là bên liên quan tham khảo nếu dự án được mở rộng.

## 2. Nguyên tắc quản lý

1. Mỗi rủi ro phải có một người phụ trách chính.
2. Rủi ro phải có dấu hiệu nhận biết và hành động cụ thể.
3. Khi rủi ro đã xảy ra, nhóm ghi nhận thành vấn đề cần xử lý; không tiếp tục gọi đó là khả năng chưa xảy ra.
4. Không ghi “Đã đóng” khi chưa có bằng chứng cho thấy nguyên nhân đã hết hoặc biện pháp xử lý đã đạt.
5. Không giảm tiêu chí chấp nhận, kiểm thử, bảo mật hoặc DoD để che giấu ảnh hưởng của rủi ro.
6. Coding agent hỗ trợ xử lý công việc nhưng không tự xác nhận chất lượng hoặc chấp nhận rủi ro.
7. Hệ số dự phòng 2,5 hỗ trợ lập kế hoạch nhưng không thay thế việc theo dõi và xử lý từng rủi ro.

## 3. Phương pháp đánh giá

### 3.1. Xác suất

| Điểm | Mức xác suất | Cách hiểu trong dự án                            |
| ---: | ------------ | ------------------------------------------------ |
|    1 | Hiếm         | Khó xảy ra trong 11 tuần.                        |
|    2 | Thấp         | Có thể xảy ra nhưng chưa có dấu hiệu.            |
|    3 | Trung bình   | Có phụ thuộc hoặc đã xuất hiện dấu hiệu ban đầu. |
|    4 | Cao          | Đã có tiền lệ hoặc điều kiện gây rủi ro đang có. |
|    5 | Rất cao      | Đang xảy ra hoặc gần như chắc chắn xảy ra.       |

### 3.2. Tác động

| Điểm | Mức tác động  | Cách hiểu trong dự án                                  |
| ---: | ------------- | ------------------------------------------------------ |
|    1 | Không đáng kể | Xử lý trong luồng làm việc thông thường.               |
|    2 | Nhỏ           | Ảnh hưởng một hạng mục nhưng không ảnh hưởng mốc tuần. |
|    3 | Vừa           | Gây làm lại hoặc làm chậm một mốc nội bộ.              |
|    4 | Lớn           | Ảnh hưởng nhiều hạng mục hoặc chất lượng bàn giao.     |
|    5 | Nghiêm trọng  | Có thể làm mất dữ liệu, lộ quyền hoặc phá vỡ baseline. |

Điểm rủi ro được tính như sau:

`Điểm rủi ro = Điểm xác suất × Điểm tác động`

| Tổng điểm | Mức rủi ro | Yêu cầu xử lý                                                       |
| --------: | ---------- | ------------------------------------------------------------------- |
|       1–4 | Thấp       | Người phụ trách theo dõi tại mốc liên quan.                         |
|       5–9 | Trung bình | Có hành động phòng ngừa và ngày xem xét.                            |
|     10–15 | Cao        | Báo Quản lý dự án và xử lý trước công việc phụ thuộc.               |
|     16–25 | Rất cao    | Ưu tiên xử lý; tạm dừng hoạt động có thể gây tác động nghiêm trọng. |

### 3.3. Trạng thái

| Trạng thái    | Ý nghĩa                                                       |
| ------------- | ------------------------------------------------------------- |
| Đang theo dõi | Rủi ro chưa xảy ra và đang được quan sát.                     |
| Đã xảy ra     | Dấu hiệu đã xuất hiện và rủi ro đã trở thành vấn đề.          |
| Đang xử lý    | Nhóm đang thực hiện hành động giảm ảnh hưởng.                 |
| Đã chấp nhận  | Nhóm chấp nhận phần ảnh hưởng còn lại với lý do rõ ràng.      |
| Đã đóng       | Nguyên nhân không còn hoặc biện pháp đã đạt và có bằng chứng. |

## 4. Vai trò và trách nhiệm

| Vai trò                  | Trách nhiệm                                                      |
| ------------------------ | ---------------------------------------------------------------- |
| Quản lý dự án            | Duy trì kế hoạch, ưu tiên xử lý và điều phối nguồn lực.          |
| Technical Lead           | Theo dõi rủi ro kiến trúc, tích hợp, Pull Request và bảo mật mã. |
| Đảm bảo chất lượng       | Theo dõi kiểm thử, lỗi, bằng chứng và điều kiện hoàn thành.      |
| Người phụ trách hạng mục | Báo dấu hiệu, thực hiện hành động và cập nhật kết quả.           |
| Các thành viên           | Nhận diện rủi ro mới và không che giấu vấn đề đã xảy ra.         |

## 5. Danh sách rủi ro

| ID   | Rủi ro                                                    | Xác suất | Tác động | Điểm | Mức        | Người phụ trách        | Dấu hiệu chính                                                   | Trạng thái    |
| ---- | --------------------------------------------------------- | -------: | -------: | ---: | ---------- | ---------------------- | ---------------------------------------------------------------- | ------------- |
| R-01 | Phạm vi tùy chọn làm ảnh hưởng baseline                   |        4 |        4 |   16 | Rất cao    | Quản lý dự án          | Hạng mục Nên có hoặc Có thể xem xét được đưa vào thực hiện.      | Đang theo dõi |
| R-02 | Thành viên thiếu thời gian hoặc nhận quá nhiều việc       |        3 |        4 |   12 | Cao        | Quản lý dự án          | Vượt giới hạn công việc hoặc hạng mục không tiến triển.          | Đang theo dõi |
| R-03 | Pull Request chờ Technical Lead xem xét quá lâu           |        3 |        3 |    9 | Trung bình | Technical Lead         | Pull Request chờ quá hai ngày làm việc.                          | Đang theo dõi |
| R-04 | Coding agent tạo mã hoặc tài liệu không chính xác         |        4 |        4 |   16 | Rất cao    | Người tạo kết quả      | Kết quả không hiểu được, kiểm thử lỗi hoặc sai phạm vi.          | Đang theo dõi |
| R-05 | Chất lượng OCR không đạt trên tài liệu mẫu                |        3 |        4 |   12 | Cao        | Technical Lead         | Kết quả nhận dạng sai nhiều và khó hiệu chỉnh.                   | Đang theo dõi |
| R-06 | Tệp gốc hoặc nội dung hiệu chỉnh bị mất hay ghi đè        |        3 |        5 |   15 | Cao        | Phụ trách máy chủ      | Tệp không mở được, sai phiên bản hoặc xử lý lại làm mất dữ liệu. | Đang theo dõi |
| R-07 | Người dùng truy cập nội dung không đúng quyền             |        3 |        5 |   15 | Cao        | Technical Lead; QA     | Kiểm thử sai quyền vẫn nhận được nội dung hoặc liên kết.         | Đang theo dõi |
| R-08 | Tác vụ OCR hoặc EPUB bị treo và không phục hồi            |        3 |        4 |   12 | Cao        | Phụ trách máy chủ      | Trạng thái xử lý kéo dài hoặc mất sau khi dịch vụ khởi động lại. | Đang theo dõi |
| R-09 | EPUB, tìm kiếm hoặc trình đọc không tích hợp đúng         |        3 |        4 |   12 | Cao        | Technical Lead         | Luồng đầu cuối lỗi dù từng thành phần chạy riêng.                | Đang theo dõi |
| R-10 | Thiếu Pull Request, kiểm thử hoặc bằng chứng đạt DoD      |        5 |        4 |   20 | Rất cao    | Đảm bảo chất lượng; PM | Hạng mục chờ xác nhận nhưng thiếu bằng chứng bắt buộc.           | Đã xảy ra     |
| R-11 | Khóa bí mật hoặc dữ liệu nhạy cảm bị đưa vào mã nguồn     |        2 |        5 |   10 | Cao        | Technical Lead         | Rà soát phát hiện khóa, mật khẩu hoặc dữ liệu không được phép.   | Đang theo dõi |
| R-12 | Yêu cầu, kế hoạch và tài liệu không được cập nhật đồng bộ |        3 |        4 |   12 | Cao        | Quản lý dự án          | Cùng một nội dung có số liệu hoặc quyết định khác nhau.          | Đang theo dõi |

## 6. Kế hoạch ứng phó

| ID   | Cách xử lý | Hành động phòng ngừa                                                    | Hành động khi xảy ra                                                      | Bằng chứng để giảm mức hoặc đóng                         |
| ---- | ---------- | ----------------------------------------------------------------------- | ------------------------------------------------------------------------- | -------------------------------------------------------- |
| R-01 | Tránh      | Chỉ thực hiện 15 hạng mục Bắt buộc khi baseline chưa ổn định.           | Dừng hạng mục tùy chọn và điều phối lại người thực hiện.                  | Bảng Kanban và quyết định phạm vi đã cập nhật.           |
| R-02 | Giảm       | Giữ giới hạn một việc đang thực hiện cho mỗi thành viên.                | Dừng nhận việc mới, hỗ trợ việc bị chặn và phân công lại.                 | Khối lượng trở về đúng giới hạn; hạng mục tiếp tục chạy. |
| R-03 | Giảm       | Technical Lead dành thời gian xem xét Pull Request trong tuần.          | Ghi người được ủy quyền xem xét và ưu tiên Pull Request chờ lâu nhất.     | Pull Request được phê duyệt hoặc có yêu cầu sửa rõ ràng. |
| R-04 | Giảm       | Thành viên đọc, hiểu, định dạng và kiểm thử kết quả của coding agent.   | Loại phần sai, sửa lại, chạy kiểm thử và yêu cầu Technical Lead xem xét.  | Kiểm thử đạt và Pull Request được phê duyệt.             |
| R-05 | Giảm       | Dùng tài liệu mẫu phù hợp và giữ bước hiệu chỉnh của con người.         | Điều chỉnh tiền xử lý, cấu hình hoặc giới hạn loại tài liệu được hỗ trợ.  | Kết quả kiểm thử OCR trên bộ mẫu đã xác định.            |
| R-06 | Tránh      | Không ghi đè tệp gốc; dùng định danh, phiên bản và kiểm tra dữ liệu.    | Dừng tác vụ, khôi phục bản gần nhất và kiểm tra phạm vi ảnh hưởng.        | Kiểm thử bảo toàn và khôi phục dữ liệu đạt.              |
| R-07 | Tránh      | Kiểm tra quyền tại máy chủ và kiểm thử trường hợp không đủ quyền.       | Khóa đường truy cập, sửa kiểm tra quyền và chạy kiểm thử hồi quy.         | Ma trận quyền và các kiểm thử sai quyền đều đạt.         |
| R-08 | Giảm       | Có giới hạn thời gian, trạng thái lỗi và xử lý lại an toàn.             | Đánh dấu thất bại, bảo toàn tệp gốc và chạy lại có kiểm soát.             | Kiểm thử lỗi, khởi động lại và xử lý lại đạt.            |
| R-09 | Giảm       | Tích hợp theo từng luồng nhỏ và kiểm thử sớm giữa các thành phần.       | Cô lập điểm lỗi, quay lại kết quả ổn định và sửa theo thứ tự phụ thuộc.   | Luồng đầu cuối và kiểm thử hồi quy đạt.                  |
| R-10 | Giảm       | DoD bắt buộc có Pull Request, kiểm thử, người xem xét và ngày xác nhận. | Trả hạng mục về Đang xem xét và bổ sung bằng chứng còn thiếu.             | Hạng mục có đầy đủ bằng chứng DoD.                       |
| R-11 | Tránh      | Không đưa tệp môi trường vào Git; rà soát mã và dùng quyền tối thiểu.   | Thu hồi khóa, thay khóa mới, loại khỏi bản phát hành và kiểm tra lịch sử. | Không còn khóa hợp lệ trong mã; kết quả rà soát đạt.     |
| R-12 | Giảm       | Khi có thay đổi, xác định và cập nhật tất cả tài liệu bị ảnh hưởng.     | Tạm dừng xác nhận tài liệu, sửa mâu thuẫn và rà chéo lại baseline.        | Các tài liệu dùng cùng số liệu, phạm vi và quyết định.   |

## 7. Theo dõi và báo cáo

### 7.1. Nhịp theo dõi

| Hoạt động                | Tần suất              | Người thực hiện                  |
| ------------------------ | --------------------- | -------------------------------- |
| Kiểm tra dấu hiệu rủi ro | Mỗi ngày có làm việc  | Người phụ trách hạng mục         |
| Rà soát danh sách rủi ro | Hai lần mỗi tuần      | Quản lý dự án và người phụ trách |
| Rà soát tại mốc          | Cuối mỗi tuần         | Nhóm Sebros                      |
| Rà soát toàn bộ          | Khi thay đổi baseline | Sáu thành viên nhóm Sebros       |

### 7.2. Ngưỡng hành động

- Rủi ro từ 16 điểm phải được ưu tiên trong lần trao đổi gần nhất.
- Rủi ro từ 10 đến 15 điểm phải có hành động và người phụ trách trước khi tiếp tục công việc phụ thuộc.
- Rủi ro gây mất dữ liệu, lộ quyền hoặc lộ khóa bí mật phải dừng hoạt động liên quan ngay.
- Pull Request chờ quá hai ngày phải được Technical Lead xử lý hoặc ủy quyền rõ ràng.
- Công việc bị chặn quá hai ngày phải được Quản lý dự án điều phối lại.
- Mọi rủi ro đã xảy ra phải được ghi vào Nhật ký dự án cùng hành động xử lý.

## 8. Dự phòng tiến độ

Baseline gồm 26 điểm. Giai đoạn làm thử ngày 16 và 17 tháng 07 năm 2026 đã triển khai 15 điểm Bắt buộc; phần chưa được triển khai thử còn 11 điểm.

Thời gian theo tốc độ làm thử:

`11 điểm ÷ 7,5 điểm/ngày = 1,47 ngày`

Thời gian sau khi thêm dự phòng:

`1,47 ngày × 2,5 = 3,68 ngày`

Nhóm làm tròn thành 4 ngày làm việc tương đương. Hệ số 2,5 dự phòng cho xem xét Pull Request, kiểm thử, tích hợp, sửa lỗi, tài liệu, công việc bị chặn và sai lệch giữa làm thử với phát triển đầy đủ.

Tiến độ baseline vẫn được bảo đảm trong 11 tuần. Khi rủi ro xảy ra, nhóm ưu tiên gỡ vướng, điều phối lại người thực hiện và thứ tự công việc; không tự động giảm DoD hoặc bổ sung hạng mục tùy chọn.

## 9. Rủi ro khi dự án mở rộng

Các rủi ro sau không thuộc điều kiện hoàn thành dự án học tập hiện tại nhưng phải được đánh giá lại nếu hệ thống được triển khai thực tế:

| Rủi ro mở rộng                           | Yêu cầu trước khi triển khai                               |
| ---------------------------------------- | ---------------------------------------------------------- |
| Chưa có quyền số hóa tài liệu thật       | Xác định nguồn, quyền sử dụng và người có thẩm quyền.      |
| Dữ liệu thật chứa thông tin nhạy cảm     | Phân loại dữ liệu, giới hạn truy cập và quy trình xử lý.   |
| Hạ tầng không đáp ứng quy mô sử dụng     | Đo tải, lập dự toán và thiết kế môi trường vận hành.       |
| Sao lưu và phục hồi chưa được kiểm chứng | Xác định mục tiêu phục hồi và chạy thử khôi phục.          |
| Dịch vụ trả phí thay đổi hạn mức         | Xác định ngân sách, người phê duyệt và phương án thay thế. |
| Chưa có đơn vị chịu trách nhiệm vận hành | Xác định chủ sở hữu, hỗ trợ người dùng và xử lý sự cố.     |

Việc nhắc đến Thư viện, Nhà trường hoặc đơn vị khác không đồng nghĩa các bên này đã chấp nhận rủi ro hay phê duyệt triển khai.

## 10. Điều kiện chấp nhận và đóng rủi ro

### 10.1. Chấp nhận rủi ro

| Loại tác động                      | Người xác nhận                                    |
| ---------------------------------- | ------------------------------------------------- |
| Ảnh hưởng nhỏ, không đổi baseline  | Người phụ trách và Quản lý dự án.                 |
| Ảnh hưởng baseline hoặc thời gian  | Sáu thành viên nhóm Sebros.                       |
| Ảnh hưởng bảo mật hoặc dữ liệu mẫu | Technical Lead, Quản lý dự án và QA.              |
| Ảnh hưởng triển khai thực tế       | Đơn vị có thẩm quyền trong một giai đoạn mở rộng. |

### 10.2. Đóng rủi ro

Một rủi ro chỉ được ghi Đã đóng khi:

1. Dấu hiệu không còn hoặc giai đoạn liên quan đã kết thúc.
2. Hành động ứng phó đã được thực hiện.
3. Có bằng chứng kiểm tra kết quả.
4. Phần ảnh hưởng còn lại đã được người có thẩm quyền chấp nhận.
5. Tài liệu và Nhật ký dự án đã được cập nhật.

Tại thời điểm cập nhật, R-10 được ghi Đã xảy ra vì Nhật ký dự án chưa có đầy đủ bằng chứng DoD cho các kết quả làm thử. Các rủi ro còn lại tiếp tục được theo dõi; chưa có rủi ro nào đủ điều kiện ghi Đã đóng.

## 11. Tài liệu tham khảo

- Bản mô tả công việc.
- Báo cáo nghiên cứu tính khả thi.
- Yêu cầu phần mềm.
- Product Backlog.
- Kiến trúc phần mềm.
- Định nghĩa quy trình phát triển phần mềm.
- Ước lượng dự án.
- Kế hoạch dự án.
- Kế hoạch quản lý chất lượng.
- Kế hoạch kiểm thử.
- Hợp đồng nhóm.
- Nhật ký dự án.
