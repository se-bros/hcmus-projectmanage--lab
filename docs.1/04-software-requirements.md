# YÊU CẦU PHẦN MỀM

## Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS (HCMUS-LDMS)

### THÔNG TIN TÀI LIỆU

| Trường thông tin    | Nội dung                                            |
| ------------------- | --------------------------------------------------- |
| Mã tài liệu         | `HCMUS-LDMS-SRS`                                    |
| Tên tài liệu        | Yêu cầu phần mềm                                    |
| Dự án               | HCMUS-LDMS                                          |
| Đơn vị soạn thảo    | Sebros – Nhóm sinh viên đề xuất dự án               |
| Người thực hiện     | Mạch Quốc Tấn                                       |
| Người xem xét       | Đại diện nhóm Sebros và Đại diện nghiệp vụ Thư viện |
| Trạng thái tài liệu | Bản dự thảo để xem xét                              |
| Phạm vi phiên bản   | Phiên bản đầu tiên trong 11 tuần                    |

### LỊCH SỬ PHIÊN BẢN

| Phiên bản | Ngày       | Mô tả thay đổi                                                                                                                               | Người thực hiện |
| --------- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| 1.0       | 21/08/2026 | Khởi tạo và hoàn thiện yêu cầu phần mềm, bổ sung tiêu chí chấp nhận, điều kiện sẵn sàng, điều kiện hoàn thành, truy vết và quản lý thay đổi. | Mạch Quốc Tấn   |
| 2.0       | 22/08/2026 | Làm rõ phân loại tài liệu, trạng thái vòng đời, cách đo NFR và truy vết tới bằng chứng; đồng bộ SOW 11 tuần. | Mạch Quốc Tấn |

## Mục lục

- [Mục đích và phạm vi](#1-mục-đích-và-phạm-vi)
- [Bối cảnh và người sử dụng](#2-bối-cảnh-và-người-sử-dụng)
- [Thuật ngữ và quy tắc nghiệp vụ](#3-thuật-ngữ-và-quy-tắc-nghiệp-vụ)
- [Yêu cầu chức năng](#4-yêu-cầu-chức-năng)
- [Yêu cầu phi chức năng](#5-yêu-cầu-phi-chức-năng)
- [Yêu cầu dữ liệu](#6-yêu-cầu-dữ-liệu)
- [Tiêu chí chấp nhận và truy vết](#7-tiêu-chí-chấp-nhận-và-truy-vết)
- [Giả định, giới hạn và quản lý thay đổi](#8-giả-định-giới-hạn-và-quản-lý-thay-đổi)
- [Cách sử dụng tài liệu](#9-cách-sử-dụng-tài-liệu)
- [Tài liệu tham khảo](#10-tài-liệu-tham-khảo)

## 1. Mục đích và phạm vi

Tài liệu xác định các nhu cầu và hành vi mà HCMUS-LDMS cần đáp ứng trong phiên bản đầu tiên. Đây là cơ sở để nhóm lập danh mục công việc, thiết kế, lập trình, kiểm thử và nghiệm thu; không phải tài liệu mô tả chi tiết mã nguồn.

Phạm vi phiên bản đầu tiên gồm: tiếp nhận tài liệu, nhận dạng ký tự, hiệu chỉnh văn bản, nhập thông tin mô tả tài liệu, phân loại, xuất bản EPUB, tìm kiếm toàn văn, đọc trực tuyến và kiểm soát quyền truy cập. Công việc được tổ chức theo luồng Kanban trong 11 tuần; các chức năng nâng cao như ghi chú, đánh dấu, trích dẫn và mở rộng công cụ tìm kiếm chỉ được thực hiện khi còn năng lực sau khi hoàn thành phạm vi bắt buộc.

## 2. Bối cảnh và người sử dụng

HCMUS-LDMS hỗ trợ Thư viện chuyển tài liệu giấy hoặc bản quét thành học liệu số có thể tìm kiếm và đọc trực tuyến. Nhu cầu thực tế được mô tả trong [Đề xuất dự án](01-project-proposal.md) và [Tài liệu viễn cảnh và phạm vi](02-vision-and-scope.md). Không sử dụng số liệu khảo sát định lượng nếu nhóm chưa có dữ liệu thực tế.

Các nhóm người sử dụng chính:

- **Độc giả:** sinh viên, giảng viên hoặc người được cấp quyền; tìm kiếm và đọc tài liệu trực tuyến.
- **Thủ thư hoặc biên tập viên:** tiếp nhận tài liệu, theo dõi nhận dạng ký tự, sửa lỗi, bổ sung thông tin và xuất bản.
- **Quản trị viên:** quản lý tài khoản, vai trò, quyền truy cập và danh mục dùng chung.

## 3. Thuật ngữ và quy tắc nghiệp vụ

| Thuật ngữ             | Giải thích                                                              |
| --------------------- | ----------------------------------------------------------------------- |
| Tài liệu gốc          | Bản PDF hoặc ảnh quét được đưa vào hệ thống để xử lý.                   |
| Nhận dạng ký tự       | Quá trình chuyển chữ trong ảnh hoặc PDF thành văn bản có thể chỉnh sửa. |
| Thông tin mô tả tài liệu | Thông tin như tên, tác giả, năm, thể loại và từ khóa dùng để nhận biết tài liệu. |
| Bản nháp              | Tài liệu đang được xử lý hoặc hiệu chỉnh, chưa cho độc giả đọc.         |
| Xuất bản              | Đưa tài liệu đã đạt điều kiện lên kho để người có quyền truy cập.       |
| Độc giả               | Người được phép tìm kiếm và đọc tài liệu đã xuất bản.                   |
| Thủ thư/biên tập viên | Người chịu trách nhiệm kiểm tra và hoàn thiện nội dung tài liệu.        |

Quy tắc nghiệp vụ chính:

- Chỉ tài liệu đã có nội dung xử lý, thông tin mô tả tài liệu tối thiểu và kết quả kiểm tra đạt mới được xuất bản.
- Tài liệu chưa xuất bản không xuất hiện trong kết quả tìm kiếm và không được cung cấp cho độc giả.
- Người dùng chỉ thực hiện được chức năng phù hợp với vai trò và quyền đã được cấp.
- Kết quả nhận dạng ký tự phải có thể kiểm tra, hiệu chỉnh và lưu lại trước khi xuất bản.
- Tệp gốc và tệp EPUB được bảo vệ; người đọc sử dụng trình đọc trực tuyến theo quyền được cấp, không có nút tải tệp EPUB gốc trong giao diện.

## 4. Yêu cầu chức năng

### 4.1. Tài khoản và phân quyền

| Mã       | Yêu cầu                                                                                                                                                                                                | Ưu tiên  |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------- |
| YC-HT-01 | Hệ thống cho phép người dùng đăng nhập bằng cơ chế xác thực được cấu hình cho phiên bản đầu tiên; có thể dùng dữ liệu mô phỏng trong môi trường phát triển và Google OAuth 2.0 khi triển khai phù hợp. | Bắt buộc |
| YC-HT-02 | Hệ thống tạo và duy trì phiên làm việc, đồng thời từ chối yêu cầu không có thông tin xác thực hợp lệ.                                                                                                  | Bắt buộc |
| YC-HT-03 | Quản trị viên có thể gán vai trò và quyền cho tài khoản.                                                                                                                                               | Bắt buộc |
| YC-HT-04 | Hệ thống kiểm tra quyền trước các thao tác xem, sửa, xuất bản và quản trị.                                                                                                                             | Bắt buộc |

### 4.2. Tiếp nhận và quản lý tài liệu

| Mã       | Yêu cầu                                                                                                 | Ưu tiên  |
| -------- | ------------------------------------------------------------------------------------------------------- | -------- |
| YC-TL-01 | Thủ thư hoặc biên tập viên có thể tải tài liệu gốc lên hệ thống.                                        | Bắt buộc |
| YC-TL-02 | Hệ thống kiểm tra loại tệp, kích thước và các điều kiện đầu vào trước khi tiếp nhận.                    | Bắt buộc |
| YC-TL-03 | Hệ thống lưu tài liệu gốc an toàn và thông báo kết quả tiếp nhận.                                       | Bắt buộc |
| YC-TL-04 | Người có quyền có thể tạo và cập nhật thông tin mô tả tài liệu tối thiểu.                                  | Bắt buộc |
| YC-TL-05 | Người có quyền có thể gán tài liệu vào danh mục đã có; quản trị cây danh mục là hạng mục Nên có riêng.       | Bắt buộc |
| YC-TL-06 | Người có quyền có thể xem danh sách, trạng thái và thông tin cơ bản của các tài liệu mình được quản lý. | Bắt buộc |

### 4.3. Nhận dạng ký tự và hiệu chỉnh

| Mã       | Yêu cầu                                                                                                           | Ưu tiên  |
| -------- | ----------------------------------------------------------------------------------------------------------------- | -------- |
| YC-ND-01 | Người có quyền có thể yêu cầu hệ thống nhận dạng ký tự cho tài liệu đã tiếp nhận.                                 | Bắt buộc |
| YC-ND-02 | Hệ thống xử lý tác vụ nhận dạng ký tự ở nền và hiển thị trạng thái chờ xử lý, đang xử lý, hoàn tất hoặc thất bại. | Bắt buộc |
| YC-ND-03 | Hệ thống lưu văn bản nhận dạng được gắn với tài liệu và từng trang tương ứng khi có thể xác định.                 | Bắt buộc |
| YC-ND-04 | Người có quyền có thể xem ảnh hoặc PDF gốc cùng với văn bản nhận dạng để đối chiếu.                               | Bắt buộc |
| YC-ND-05 | Người có quyền có thể sửa, lưu và tiếp tục hiệu chỉnh văn bản nhận dạng.                                          | Bắt buộc |
| YC-ND-06 | Giao diện hiệu chỉnh hỗ trợ xem song song nội dung gốc và nội dung văn bản.                                       | Nên có   |
| YC-ND-07 | Người có quyền có thể yêu cầu xử lý lại khi tác vụ nhận dạng thất bại và xem nguyên nhân lỗi ở mức phù hợp.       | Nên có   |

### 4.4. Xuất bản và đọc tài liệu

| Mã       | Yêu cầu                                                                                              | Ưu tiên  |
| -------- | ---------------------------------------------------------------------------------------------------- | -------- |
| YC-PH-01 | Hệ thống cho phép kiểm tra các điều kiện trước khi xuất bản.                                         | Bắt buộc |
| YC-PH-02 | Hệ thống thông báo rõ các điều kiện chưa đạt và không cho xuất bản khi còn thiếu điều kiện bắt buộc. | Bắt buộc |
| YC-PH-03 | Người có quyền có thể xác nhận xuất bản tài liệu đã đạt điều kiện.                                   | Bắt buộc |
| YC-PH-04 | Hệ thống tạo hoặc lưu bản EPUB từ nội dung đã được hiệu chỉnh.                                       | Bắt buộc |
| YC-PH-05 | Độc giả có quyền có thể đọc tài liệu đã xuất bản trên trình đọc trực tuyến.                          | Bắt buộc |
| YC-PH-06 | Hệ thống chỉ cung cấp tài liệu đã xuất bản cho người dùng có quyền truy cập.                         | Bắt buộc |

### 4.5. Tìm kiếm và quản trị danh mục

| Mã       | Yêu cầu                                                                                                   | Ưu tiên        |
| -------- | --------------------------------------------------------------------------------------------------------- | -------------- |
| YC-TC-01 | Độc giả có thể tìm kiếm tài liệu theo thông tin mô tả cơ bản.                                             | Bắt buộc       |
| YC-TC-02 | Độc giả có thể tìm kiếm toàn văn trong nội dung tài liệu đã xuất bản.                                     | Bắt buộc       |
| YC-TC-03 | Hệ thống chỉ đưa tài liệu mà người dùng được phép xem vào kết quả tìm kiếm.                               | Bắt buộc       |
| YC-TC-04 | Kết quả tìm kiếm hiển thị thông tin đủ để người dùng nhận biết và mở tài liệu phù hợp.                    | Bắt buộc       |
| YC-TC-05 | Trình đọc hiển thị nội dung EPUB theo cách dễ đọc trên màn hình máy tính và thiết bị di động.             | Bắt buộc       |
| YC-TC-06 | Hệ thống không hiển thị liên kết tải trực tiếp tệp EPUB gốc cho độc giả.                                  | Bắt buộc       |
| YC-TC-07 | Người đọc có thể thay đổi một số thiết lập đọc cơ bản nếu chức năng đã được đưa vào phiên bản triển khai. | Có thể xem xét |

| Mã       | Yêu cầu                                                                                           | Ưu tiên |
| -------- | ------------------------------------------------------------------------------------------------- | ------- |
| YC-QL-01 | Quản trị viên có thể tạo, sửa, sắp xếp hoặc ẩn danh mục tài liệu.                                 | Nên có  |
| YC-QL-02 | Hệ thống ghi nhận trạng thái và lỗi chính của các tác vụ xử lý để người có quyền theo dõi.        | Nên có  |
| YC-QL-03 | Hệ thống lưu nhật ký tối thiểu cho các thao tác quan trọng như tải lên, sửa nội dung và xuất bản. | Nên có  |

## 5. Yêu cầu phi chức năng

| Mã       | Nhóm        | Yêu cầu                                                                                                               | Ưu tiên  |
| -------- | ----------- | --------------------------------------------------------------------------------------------------------------------- | -------- |
| YC-PN-01 | Bảo mật     | Kiểm tra xác thực và phân quyền ở phía máy chủ, không chỉ dựa vào giao diện.                                          | Bắt buộc |
| YC-PN-02 | Bảo mật     | Tệp riêng tư được lưu trong vùng bảo vệ; liên kết truy cập tạm thời phải có thời hạn và không được công khai lâu dài. | Bắt buộc |
| YC-PN-03 | Hiệu năng   | Các tác vụ nhận dạng ký tự và tạo EPUB không làm treo yêu cầu giao diện; người dùng nhận được trạng thái xử lý.       | Bắt buộc |
| YC-PN-04 | Hiệu năng   | Tìm kiếm toàn văn phải được đo trên dataset và môi trường được ghi nhận; nhóm chốt ngưỡng/percentile trước UAT.       | Bắt buộc |
| YC-PN-05 | Dễ sử dụng  | Luồng tải lên, hiệu chỉnh, kiểm tra và xuất bản phải có trạng thái và thông báo dễ hiểu.                              | Bắt buộc |
| YC-PN-06 | Tương thích | Giao diện chính được kiểm thử theo browser/version/device matrix được chốt trước UAT.                                | Nên có   |
| YC-PN-07 | Bảo trì     | Mã nguồn được tổ chức theo các phần chức năng, có hướng dẫn cài đặt, cấu hình và chạy hệ thống.                       | Bắt buộc |
| YC-PN-08 | Tin cậy     | Lỗi tác vụ không làm mất tài liệu gốc hoặc dữ liệu đã lưu trước đó.                                                   | Bắt buộc |
| YC-PN-09 | Triển khai  | Hệ thống có thể chạy trong môi trường phát triển thống nhất bằng cấu hình được quản lý trong kho mã nguồn.            | Nên có   |
| YC-PN-10 | Truy vết    | Yêu cầu, câu chuyện người dùng, mã nguồn, kiểm thử và kết quả nghiệm thu có thể liên kết với nhau.                   | Bắt buộc |

Các chỉ số như thời gian phản hồi hoặc tỷ lệ lỗi chỉ được chốt thành số cụ thể khi nhóm có dữ liệu kiểm thử hoặc thỏa thuận nghiệm thu tương ứng; không tự xem các con số trong tài liệu kiến trúc là số liệu đã đo.

Khi chốt một chỉ số, bằng chứng phải ghi tối thiểu môi trường, dataset, số lần chạy, cách tổng hợp và kết quả thực tế. Tuyên bố “phù hợp” không thay thế phép đo.

## 6. Yêu cầu dữ liệu

| Nhóm dữ liệu         | Nội dung chính                                                                     |
| -------------------- | ---------------------------------------------------------------------------------- |
| Tài khoản và vai trò | Mã người dùng, thông tin định danh, vai trò, trạng thái và quyền.                  |
| Tài liệu             | Tên, mã, tệp gốc, trạng thái xử lý, người tạo và thời điểm cập nhật.               |
| Thông tin mô tả tài liệu | Tác giả, năm, thể loại, từ khóa, mô tả và thông tin phân loại.                     |
| Nội dung nhận dạng   | Văn bản theo tài liệu hoặc trang, trạng thái hiệu chỉnh và phiên bản lưu gần nhất. |
| Bản xuất bản         | Tệp EPUB, trạng thái xuất bản, thời điểm xuất bản và người xác nhận.               |
| Tác vụ và nhật ký    | Loại tác vụ, trạng thái, lỗi chính, người thực hiện và thời điểm.                  |

Tệp gốc phải được bảo toàn; việc xử lý hoặc xuất bản tạo dữ liệu kết quả, không ghi đè làm mất bản gốc. Dữ liệu thử nghiệm phải được phân biệt với dữ liệu thật của Thư viện.

Vòng đời tài liệu tối thiểu gồm: `ocr_pending`, `ocr_processing`, `ocr_completed`, `ocr_failed`, `publishing`, `published`, `publish_failed`. Trạng thái lỗi không được làm mất tệp gốc hoặc nội dung đã lưu; hành động retry phải tạo hoặc ghi nhận lần thử mới có thể truy vết.

## 7. Tiêu chí chấp nhận và truy vết

Một yêu cầu được xem là đạt khi thỏa các điều kiện: đúng nhu cầu đã thống nhất, không mâu thuẫn với yêu cầu khác, khả thi trong phạm vi 11 tuần, có mức ưu tiên, có cách kiểm thử và có liên kết đến câu chuyện người dùng hoặc công việc tương ứng.

Tiêu chí chấp nhận của từng câu chuyện người dùng phải mô tả kết quả quan sát được, gồm cả trường hợp thành công và trường hợp dữ liệu không hợp lệ hoặc không đủ quyền. Các tiêu chí phải được xem xét cùng Đại diện nghiệp vụ Thư viện trước khi đưa vào thực hiện.

### Điều kiện đưa vào luồng thực hiện

- Nêu rõ người sử dụng và nhu cầu cần giải quyết.
- Có mô tả đủ rõ để nhóm ước lượng và phân chia công việc.
- Có mức ưu tiên, tiêu chí chấp nhận và yêu cầu phi chức năng liên quan.
- Đã nhận diện phụ thuộc, dữ liệu đầu vào và người xem xét.

### Điều kiện hoàn thành

- Mã nguồn đã được xem xét và tích hợp vào nhánh ổn định.
- Kiểm thử phù hợp đã được thực hiện và không còn lỗi nghiêm trọng chưa xử lý.
- Toàn bộ tiêu chí chấp nhận đạt, tài liệu liên quan được cập nhật.
- Kết quả đã được trình bày hoặc xác nhận bởi người có trách nhiệm nghiệm thu.

| Nhóm yêu cầu | Câu chuyện người dùng hoặc nhóm công việc         | Truy vết sang danh mục công việc                                                               |
| ------------ | ------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| YC-HT        | Đăng nhập, phiên làm việc, phân quyền             | `LDMS-009`, `LDMS-010`, `LDMS-018`                                                             |
| YC-TL        | Tải lên, thông tin mô tả, gán danh mục, danh sách tài liệu | `LDMS-002`, `LDMS-011`, `LDMS-026`; quản trị cây danh mục: `LDMS-012`                    |
| YC-ND        | Nhận dạng ký tự, theo dõi, hiệu chỉnh, xử lý lại  | `LDMS-003`, `LDMS-004`, `LDMS-005`, `LDMS-006`, `LDMS-017`, `LDMS-022`                         |
| YC-PH        | Kiểm tra, tạo EPUB, xuất bản, đọc                 | `LDMS-007`, `LDMS-008`, `LDMS-013`, `LDMS-014`                                                 |
| YC-TC        | Tìm kiếm, kết quả, đọc trực tuyến                 | `LDMS-008`, `LDMS-015`, `LDMS-016`, `LDMS-019`                                                 |
| YC-QL        | Danh mục, trạng thái, nhật ký                     | `LDMS-012`, `LDMS-022`, `LDMS-023`                                                             |
| YC-PN        | Bảo mật, hiệu năng, dễ dùng, triển khai, truy vết | AC của story, [Tài liệu kiến trúc](05-software-architecture.md), [Test/UAT Plan](20-test-plan.md) và evidence index theo [SOW](12-statement-of-work.md) |

## 8. Giả định, giới hạn và quản lý thay đổi

Các giả định chính: nhóm gồm 6 sinh viên chuyên ngành Kỹ thuật phần mềm; nhóm có đủ kỹ năng triển khai phiên bản học tập; người đại diện nghiệp vụ là Đại diện nghiệp vụ Thư viện; hạ tầng và dữ liệu thật có thể cần được cung cấp sau khi dự án được chấp thuận.

Giới hạn chính: thời gian thực hiện phiên bản đầu tiên là 11 tuần; ngân sách sơ bộ chưa có con số cụ thể vì đây là dự án phục vụ môn học; chi phí mở rộng quy mô được xem xét trong tài liệu khác; không khẳng định kết quả nhận dạng ký tự hoàn toàn chính xác nếu chưa có bộ dữ liệu đánh giá.

Yêu cầu được quản lý theo Kanban. Khi có đề xuất thay đổi, nhóm ghi rõ lý do, nguồn yêu cầu, tác động đến phạm vi, thời gian, chất lượng và phụ thuộc; sau đó Đại diện nhóm Sebros cùng Đại diện nghiệp vụ Thư viện quyết định cập nhật hoặc đưa vào danh sách xem xét sau. Mọi thay đổi được cập nhật đồng thời ở câu chuyện người dùng, tiêu chí chấp nhận và bảng truy vết.

## 9. Cách sử dụng tài liệu

- Tạo và rà soát câu chuyện người dùng trong [Danh mục công việc](04-product-backlog.md).
- Làm căn cứ cho [Tài liệu kiến trúc phần mềm](05-software-architecture.md).
- Lập công việc, kiểm thử và nghiệm thu theo luồng Kanban.
- Cập nhật yêu cầu khi có quyết định thay đổi đã được ghi nhận.

## 10. Tài liệu tham khảo

- [Đề xuất dự án](01-project-proposal.md)
- [Tài liệu viễn cảnh và phạm vi](02-vision-and-scope.md)
- [Ủy nhiệm dự án](03-project-charter.md)
- [Tài liệu kiến trúc phần mềm](05-software-architecture.md)
- [Nghiên cứu tính khả thi](08-feasibility-study.md)
- [Sổ đăng ký rủi ro](18-risk-management-plan.md)
- [Kế hoạch quản lý chất lượng](19-quality-management-plan.md)
- [Kế hoạch kiểm thử và UAT](20-test-plan.md)
