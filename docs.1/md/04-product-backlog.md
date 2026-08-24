# DANH MỤC CÔNG VIỆC (PRODUCT BACKLOG)

## Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS (HCMUS-LDMS)

### Thông tin tài liệu

| Trường thông tin    | Nội dung                                |
| ------------------- | --------------------------------------- |
| Mã tài liệu         | `HCMUS-LDMS-PBL`                        |
| Tên tài liệu        | Danh mục công việc                      |
| Đơn vị thực hiện    | Nhóm Sebros                             |
| Người phụ trách     | Mạch Quốc Tấn — Đại diện nhóm Sebros    |
| Người xem xét       | Các thành viên nhóm Sebros              |
| Trạng thái          | Baseline nội bộ đã được nhóm xác nhận   |
| Phương pháp quản lý | Kanban, luồng công việc liên tục        |
| Thời gian           | 11 tuần                                 |
| Phạm vi             | 15 Bắt buộc, 6 Nên có, 5 Có thể xem xét |

### Lịch sử phiên bản

| Phiên bản |    Ngày    | Mô tả thay đổi                                                                                         | Người thực hiện |
| --------: | :--------: | ------------------------------------------------------------------------------------------------------ | --------------- |
|       1.0 | 11/07/2026 | Khởi tạo danh mục công việc.                                                                           | Mạch Quốc Tấn   |
|       2.0 | 14/07/2026 | Bổ sung câu chuyện người dùng, tiêu chí chấp nhận và mức độ ưu tiên.                                   | Mạch Quốc Tấn   |
|       3.0 | 15/07/2026 | Cập nhật phụ thuộc, quy tắc hoàn thành và nhóm chức năng.                                              | Mạch Quốc Tấn   |
|       4.0 | 21/08/2026 | Đồng bộ quy trình Kanban 11 tuần và phân biệt phạm vi Bắt buộc với các hạng mục xem xét sau.           | Mạch Quốc Tấn   |
|       5.0 | 22/08/2026 | Đồng bộ baseline 15/6/5, cỡ công việc, bằng chứng và điều kiện bổ sung hạng mục tùy chọn.              | Mạch Quốc Tấn   |
|       6.0 | 24/08/2026 | Chuyển toàn bộ 26 hạng mục thành một bảng thống nhất và loại bỏ đường dẫn tệp khỏi bản in.             | Mạch Quốc Tấn   |
|       6.1 | 24/08/2026 | Rút bảng còn sáu trường: ID, tiêu đề, câu chuyện người dùng, ưu tiên, ước lượng và tiêu chí chấp nhận. | Mạch Quốc Tấn   |
|       6.2 | 24/08/2026 | Tách tiêu chí chấp nhận của từng hạng mục thành các dòng được đánh số để dễ đọc và xác nhận.           | Mạch Quốc Tấn   |

## Mục lục

- [1. Mục đích và phạm vi sử dụng](#1-mục-đích-và-phạm-vi-sử-dụng)
- [2. Quy ước](#2-quy-ước)
- [3. Bảng Product Backlog](#3-bảng-product-backlog)
- [4. Quản lý thay đổi](#4-quản-lý-thay-đổi)
- [5. Tài liệu tham khảo](#5-tài-liệu-tham-khảo)

---

## 1. Mục đích và phạm vi sử dụng

Product Backlog chuyển các yêu cầu của HCMUS-LDMS thành 26 hạng mục có thể thực hiện, kiểm thử và xác nhận. Đây là nguồn chi tiết cho ID, tiêu đề, câu chuyện người dùng, mức ưu tiên, ước lượng và tiêu chí chấp nhận của từng hạng mục.

Baseline 11 tuần gồm 15 hạng mục **Bắt buộc**. Sáu hạng mục **Nên có** chỉ được thực hiện khi không ảnh hưởng đến baseline. Năm hạng mục **Có thể xem xét** nằm ngoài baseline và chỉ được bổ sung sau khi nhóm xác nhận thay đổi.

Chi tiết yêu cầu được trình bày trong tài liệu **Yêu cầu phần mềm**. Tiến độ, người phụ trách, phụ thuộc, trạng thái thực hiện và bằng chứng được quản lý trong bộ tài liệu **Kế hoạch dự án**, **Định nghĩa quy trình phát triển** và **Nhật ký dự án**.

## 2. Quy ước

### 2.1. Priority

| Priority       | Ý nghĩa                                                            |
| -------------- | ------------------------------------------------------------------ |
| Bắt buộc       | Thuộc baseline và cần thiết cho sản phẩm khả dụng tối thiểu.       |
| Nên có         | Có giá trị nhưng có thể hoãn nếu ảnh hưởng đến hạng mục Bắt buộc.  |
| Có thể xem xét | Nằm ngoài baseline; chỉ bổ sung khi có quyết định và đủ nguồn lực. |

### 2.2. Ước lượng

| Mức | Công sức tham khảo | Cách hiểu                                                |
| --- | ------------------ | -------------------------------------------------------- |
| Nhỏ | 4–8 giờ-người      | Công việc rõ và ít phụ thuộc.                            |
| Vừa | 8–16 giờ-người     | Cần phối hợp hoặc kiểm thử nhiều thành phần.             |
| Lớn | 16–32 giờ-người    | Cần phân rã hoặc kiểm chứng trước khi đưa vào thực hiện. |

Ước lượng bao gồm phát triển, kiểm thử, xem xét, sửa lỗi và cập nhật tài liệu. Chi tiết phương pháp được trình bày trong tài liệu **Ước lượng dự án**.

## 3. Bảng Product Backlog

| ID         | Title                            | Description (User story)                                                                                                      | Priority       | Ước lượng | Tiêu chí chấp nhận                                                                                                                                                                                            |
| ---------- | -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | -------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `LDMS-001` | Nền tảng phát triển thống nhất   | Là thành viên nhóm, tôi muốn có cấu trúc mã nguồn và môi trường thống nhất để có thể phát triển, kiểm thử và tái tạo kết quả. | Bắt buộc       | Vừa       | - **Tiêu chí 1:** Thành viên cài đặt và khởi chạy được hệ thống theo hướng dẫn.<br>- **Tiêu chí 2:** Các dịch vụ cần thiết hoạt động.<br>- **Tiêu chí 3:** Thông tin bí mật không được đưa vào mã nguồn.      |
| `LDMS-002` | Tải tài liệu gốc                 | Là thủ thư hoặc biên tập viên, tôi muốn tải tài liệu gốc lên để có thể bắt đầu quy trình số hóa.                              | Bắt buộc       | Vừa       | - **Tiêu chí 1:** Người có quyền tải được tệp hợp lệ.<br>- **Tiêu chí 2:** Tệp sai loại hoặc vượt giới hạn bị từ chối kèm lý do.<br>- **Tiêu chí 3:** Tệp gốc được lưu và không bị ghi đè.                    |
| `LDMS-003` | Khởi chạy và theo dõi OCR        | Là thủ thư hoặc biên tập viên, tôi muốn khởi chạy nhận dạng ký tự và theo dõi trạng thái để biết tiến độ xử lý.               | Bắt buộc       | Vừa       | - **Tiêu chí 1:** Người có quyền khởi chạy tác vụ.<br>- **Tiêu chí 2:** Trạng thái chờ, đang xử lý, hoàn tất hoặc thất bại được hiển thị.<br>- **Tiêu chí 3:** Tác vụ nền không làm gián đoạn thao tác chính. |
| `LDMS-004` | Xem kết quả OCR theo trang       | Là biên tập viên, tôi muốn xem văn bản nhận dạng theo từng trang để có thể đối chiếu với bản gốc.                             | Bắt buộc       | Vừa       | - **Tiêu chí 1:** Bản gốc mở được.<br>- **Tiêu chí 2:** Văn bản gắn đúng tài liệu và trang.<br>- **Tiêu chí 3:** Trường hợp chưa có kết quả được thông báo rõ.                                                |
| `LDMS-005` | Lưu văn bản đã hiệu chỉnh        | Là biên tập viên, tôi muốn sửa và lưu văn bản nhận dạng để giữ lại nội dung đã hiệu chỉnh.                                    | Bắt buộc       | Vừa       | - **Tiêu chí 1:** Văn bản sửa được lưu.<br>- **Tiêu chí 2:** Mở lại vẫn giữ đúng thay đổi.<br>- **Tiêu chí 3:** Thao tác lưu không làm mất hoặc thay đổi tệp gốc.                                             |
| `LDMS-006` | Hiệu chỉnh song song             | Là biên tập viên, tôi muốn xem song song bản gốc và văn bản để có thể đối chiếu thuận tiện hơn.                               | Nên có         | Vừa       | - **Tiêu chí 1:** Bản gốc và văn bản tương ứng cùng hiển thị.<br>- **Tiêu chí 2:** Trang đang đối chiếu được xác định rõ.<br>- **Tiêu chí 3:** Hệ thống cảnh báo trước khi bỏ nội dung chưa lưu.              |
| `LDMS-007` | Tạo EPUB                         | Là biên tập viên, tôi muốn tạo EPUB từ nội dung đã hiệu chỉnh để chuẩn bị xuất bản tài liệu.                                  | Bắt buộc       | Vừa       | - **Tiêu chí 1:** Nội dung hợp lệ tạo được EPUB.<br>- **Tiêu chí 2:** Tệp mở được bằng trình đọc hỗ trợ.<br>- **Tiêu chí 3:** Lỗi tạo tệp không làm mất nội dung đã hiệu chỉnh.                               |
| `LDMS-008` | Đọc tài liệu trực tuyến          | Là độc giả, tôi muốn đọc tài liệu EPUB đã xuất bản để có thể sử dụng tài liệu mà không tải tệp gốc.                           | Bắt buộc       | Vừa       | - **Tiêu chí 1:** Người có quyền mở được tài liệu.<br>- **Tiêu chí 2:** Nội dung hiển thị đúng và chuyển trang được.<br>- **Tiêu chí 3:** Giao diện phù hợp với máy tính và thiết bị di động.                 |
| `LDMS-009` | Đăng nhập thử nghiệm             | Là người dùng thử nghiệm, tôi muốn đăng nhập bằng dữ liệu mô phỏng để có thể kiểm thử các luồng chính.                        | Bắt buộc       | Nhỏ       | - **Tiêu chí 1:** Tài khoản hợp lệ tạo được phiên làm việc.<br>- **Tiêu chí 2:** Thông tin sai hoặc thiếu bị từ chối.<br>- **Tiêu chí 3:** Thông báo lỗi không làm lộ thông tin nhạy cảm.                     |
| `LDMS-010` | Phân quyền theo vai trò          | Là quản trị viên, tôi muốn gán vai trò và quyền để người dùng chỉ thực hiện được thao tác được phép.                          | Bắt buộc       | Vừa       | - **Tiêu chí 1:** Vai trò được gán hoặc thay đổi.<br>- **Tiêu chí 2:** Người không đủ quyền bị từ chối ở giao diện và máy chủ.<br>- **Tiêu chí 3:** Quyền mới có hiệu lực cho yêu cầu tiếp theo.              |
| `LDMS-011` | Quản lý thông tin mô tả          | Là thủ thư, tôi muốn nhập và sửa thông tin mô tả để có thể nhận biết, phân loại và tìm đúng tài liệu.                         | Bắt buộc       | Vừa       | - **Tiêu chí 1:** Trường bắt buộc được nhập và sửa.<br>- **Tiêu chí 2:** Dữ liệu thiếu hoặc sai được thông báo.<br>- **Tiêu chí 3:** Thông tin đã lưu xuất hiện đúng trong tài liệu và kết quả tìm kiếm.      |
| `LDMS-012` | Quản lý danh mục                 | Là quản trị viên, tôi muốn quản lý danh mục để tài liệu được phân loại thống nhất.                                            | Nên có         | Vừa       | - **Tiêu chí 1:** Danh mục được tạo và cập nhật.<br>- **Tiêu chí 2:** Tài liệu gắn được vào danh mục hợp lệ.<br>- **Tiêu chí 3:** Thay đổi danh mục không làm mất dữ liệu tài liệu.                           |
| `LDMS-013` | Kiểm tra điều kiện xuất bản      | Là biên tập viên, tôi muốn hệ thống kiểm tra điều kiện xuất bản để ngăn tài liệu chưa hoàn chỉnh được đưa ra sử dụng.         | Bắt buộc       | Nhỏ       | - **Tiêu chí 1:** Hệ thống kiểm tra nội dung, thông tin mô tả và EPUB.<br>- **Tiêu chí 2:** Thiếu điều kiện thì bị chặn kèm lý do.<br>- **Tiêu chí 3:** Tài liệu hợp lệ được xác nhận xuất bản.               |
| `LDMS-014` | Bảo vệ quyền đọc                 | Là độc giả hoặc quản trị viên, tôi muốn hệ thống kiểm tra quyền để nội dung chỉ được cung cấp cho người được phép.            | Bắt buộc       | Vừa       | - **Tiêu chí 1:** Người không có quyền bị từ chối.<br>- **Tiêu chí 2:** Giao diện không có chức năng tải EPUB gốc.<br>- **Tiêu chí 3:** Tệp riêng tư không dùng liên kết công khai lâu dài.                   |
| `LDMS-015` | Tìm kiếm toàn văn                | Là độc giả, tôi muốn tìm theo thông tin mô tả và nội dung để có thể tìm được tài liệu đã xuất bản phù hợp.                    | Bắt buộc       | Vừa       | - **Tiêu chí 1:** Tìm được theo thông tin mô tả và toàn văn.<br>- **Tiêu chí 2:** Tài liệu chưa xuất bản hoặc ngoài quyền truy cập không xuất hiện.<br>- **Tiêu chí 3:** Kết quả phù hợp từ khóa.             |
| `LDMS-016` | Hiển thị kết quả tìm kiếm        | Là độc giả, tôi muốn xem thông tin phù hợp trong kết quả để có thể chọn đúng tài liệu.                                        | Bắt buộc       | Nhỏ       | - **Tiêu chí 1:** Kết quả hiển thị tên và thông tin mô tả chính.<br>- **Tiêu chí 2:** Thể hiện ngữ cảnh phù hợp khi có thể.<br>- **Tiêu chí 3:** Người dùng mở được tài liệu hợp lệ.                          |
| `LDMS-017` | Chuyển trang khi hiệu chỉnh      | Là biên tập viên, tôi muốn chuyển giữa các trang để có thể hiệu chỉnh liên tục mà không mở lại tài liệu.                      | Nên có         | Nhỏ       | - **Tiêu chí 1:** Chuyển được trang trước và sau.<br>- **Tiêu chí 2:** Hiển thị đúng nội dung trang.<br>- **Tiêu chí 3:** Nội dung đã lưu không bị thay đổi hoặc mất.                                         |
| `LDMS-018` | Đăng nhập Google OAuth 2.0       | Là người dùng, tôi muốn đăng nhập bằng Google OAuth 2.0 để sử dụng tài khoản phù hợp khi môi trường được cấu hình.            | Nên có         | Vừa       | - **Tiêu chí 1:** Cấu hình hợp lệ cho phép đăng nhập.<br>- **Tiêu chí 2:** Lỗi xác thực không tạo phiên.<br>- **Tiêu chí 3:** Thông báo lỗi không làm lộ thông tin nhạy cảm.                                  |
| `LDMS-019` | Thiết lập đọc cơ bản             | Là độc giả, tôi muốn điều chỉnh thiết lập hiển thị để có thể đọc tài liệu thuận tiện hơn.                                     | Có thể xem xét | Nhỏ       | - **Tiêu chí 1:** Thiết lập được áp dụng trong phạm vi đã thống nhất.<br>- **Tiêu chí 2:** Không làm thay đổi nội dung gốc.<br>- **Tiêu chí 3:** Không ảnh hưởng luồng đọc chính.                             |
| `LDMS-020` | Lưu vị trí đọc                   | Là độc giả, tôi muốn lưu vị trí đang đọc để có thể tiếp tục ở lần sử dụng sau.                                                | Có thể xem xét | Nhỏ       | - **Tiêu chí 1:** Thống nhất dữ liệu lưu, tài khoản sở hữu và quyền riêng tư.<br>- **Tiêu chí 2:** Vị trí được cập nhật và xóa đúng.<br>- **Tiêu chí 3:** Người dùng chỉ truy cập vị trí của mình.            |
| `LDMS-021` | Đánh dấu và ghi chú              | Là độc giả, tôi muốn đánh dấu đoạn nội dung và lưu ghi chú để có thể xem lại thông tin quan trọng.                            | Có thể xem xét | Vừa       | - **Tiêu chí 1:** Người dùng tạo, xem, sửa và xóa được đánh dấu hoặc ghi chú của mình.<br>- **Tiêu chí 2:** Dữ liệu được gắn đúng tài liệu.<br>- **Tiêu chí 3:** Người khác không truy cập được.              |
| `LDMS-022` | Xử lý lại tác vụ thất bại        | Là biên tập viên, tôi muốn xem nguyên nhân và yêu cầu xử lý lại để có thể tiếp tục khi tác vụ nhận dạng thất bại.             | Nên có         | Nhỏ       | - **Tiêu chí 1:** Nguyên nhân lỗi được hiển thị phù hợp.<br>- **Tiêu chí 2:** Người có quyền yêu cầu chạy lại.<br>- **Tiêu chí 3:** Lần xử lý mới cập nhật trạng thái và không làm mất tệp gốc.               |
| `LDMS-023` | Nhật ký thao tác quan trọng      | Là quản trị viên, tôi muốn xem nhật ký thao tác để có thể kiểm tra và truy vết hoạt động quan trọng.                          | Nên có         | Nhỏ       | - **Tiêu chí 1:** Thao tác quan trọng được ghi với người thực hiện và thời điểm.<br>- **Tiêu chí 2:** Người không có quyền không xem, sửa hoặc xóa nhật ký.                                                   |
| `LDMS-024` | Tạo trích dẫn                    | Là độc giả, tôi muốn tạo thông tin trích dẫn để có thể sử dụng tài liệu theo định dạng đã thống nhất.                         | Có thể xem xét | Vừa       | - **Tiêu chí 1:** Xác định được dữ liệu nguồn và định dạng.<br>- **Tiêu chí 2:** Trích dẫn được tạo và sao chép.<br>- **Tiêu chí 3:** Trường hợp thiếu dữ liệu được thông báo rõ.                             |
| `LDMS-025` | Mở rộng công cụ tìm kiếm         | Là quản trị viên, tôi muốn đánh giá công cụ tìm kiếm mở rộng để đáp ứng khi quy mô dữ liệu vượt khả năng giải pháp hiện tại.  | Có thể xem xét | Vừa       | - **Tiêu chí 1:** Có dữ liệu đo và tiêu chí so sánh.<br>- **Tiêu chí 2:** Chứng minh giải pháp hiện tại không đáp ứng.<br>- **Tiêu chí 3:** Phương án thay thế được nhóm xác nhận trước khi thực hiện.        |
| `LDMS-026` | Danh sách và trạng thái tài liệu | Là thủ thư hoặc biên tập viên, tôi muốn xem danh sách và trạng thái để có thể theo dõi các tài liệu đang xử lý.               | Bắt buộc       | Nhỏ       | - **Tiêu chí 1:** Danh sách hiển thị thông tin và trạng thái chính.<br>- **Tiêu chí 2:** Chỉ hiện tài liệu trong phạm vi quyền.<br>- **Tiêu chí 3:** Trạng thái cập nhật theo các bước xử lý.                 |

Tổng số: **26 hạng mục**, gồm **15 Bắt buộc**, **6 Nên có** và **5 Có thể xem xét**.

## 4. Quản lý thay đổi

Khi thay đổi một hạng mục, nhóm phải rà soát tác động tới baseline, Priority, ước lượng và tiêu chí chấp nhận. Thay đổi baseline phải được nhóm Sebros xác nhận theo tài liệu **Bản mô tả công việc** và **Hợp đồng nhóm**.

Hạng mục đã được phát triển nhưng chưa thuộc baseline vẫn giữ đúng Priority đã xác nhận. Việc có mã nguồn không tự chuyển hạng mục Có thể xem xét thành hạng mục Bắt buộc. Trạng thái thực hiện và bằng chứng được trình bày trong tài liệu **Nhật ký dự án**.

## 5. Tài liệu tham khảo

- Đề xuất dự án.
- Viễn cảnh và phạm vi.
- Bản mô tả công việc.
- Yêu cầu phần mềm.
- Kiến trúc phần mềm.
- Định nghĩa quy trình phát triển.
- Ước lượng dự án.
- Kế hoạch dự án.
- Kế hoạch kiểm thử.
- Nhật ký dự án.
- Hợp đồng nhóm.
