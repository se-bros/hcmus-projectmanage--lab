# YÊU CẦU PHẦN MỀM

## Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS (HCMUS-LDMS)

### Thông tin tài liệu

| Trường thông tin    | Nội dung                                 |
| ------------------- | ---------------------------------------- |
| Mã tài liệu         | `HCMUS-LDMS-SRS`                         |
| Tên tài liệu        | Yêu cầu phần mềm                         |
| Đơn vị thực hiện    | Nhóm Sebros                              |
| Người phụ trách     | Mạch Quốc Tấn — Đại diện nhóm Sebros     |
| Người xem xét       | Các thành viên nhóm Sebros               |
| Trạng thái          | Baseline nội bộ đã được nhóm xác nhận    |
| Thời gian thực hiện | 11 tuần                                  |
| Mục đích            | Phục vụ học tập và quản lý dự án môn học |

### Lịch sử phiên bản

| Phiên bản | Ngày       | Mô tả thay đổi                                                                                 | Người thực hiện |
| --------- | ---------- | ---------------------------------------------------------------------------------------------- | --------------- |
| 1.0       | 21/08/2026 | Khởi tạo yêu cầu chức năng, yêu cầu phi chức năng và yêu cầu dữ liệu.                          | Mạch Quốc Tấn   |
| 2.0       | 22/08/2026 | Bổ sung cách đo yêu cầu phi chức năng và bảng truy vết.                                        | Mạch Quốc Tấn   |
| 3.0       | 24/08/2026 | Đồng bộ baseline 15/6/5, chuẩn hóa thuật ngữ và truy vết đủ 26 hạng mục trong Product Backlog. | Mạch Quốc Tấn   |

## Mục lục

- [1. Mục đích và phạm vi](#1-mục-đích-và-phạm-vi)
- [2. Người sử dụng](#2-người-sử-dụng)
- [3. Thuật ngữ và quy tắc nghiệp vụ](#3-thuật-ngữ-và-quy-tắc-nghiệp-vụ)
- [4. Yêu cầu chức năng](#4-yêu-cầu-chức-năng)
- [5. Yêu cầu phi chức năng](#5-yêu-cầu-phi-chức-năng)
- [6. Yêu cầu dữ liệu](#6-yêu-cầu-dữ-liệu)
- [7. Truy vết và xác nhận](#7-truy-vết-và-xác-nhận)
- [8. Giả định, giới hạn và quản lý thay đổi](#8-giả-định-giới-hạn-và-quản-lý-thay-đổi)
- [9. Tài liệu tham khảo](#9-tài-liệu-tham-khảo)

---

## 1. Mục đích và phạm vi

Tài liệu xác định các hành vi, dữ liệu và đặc tính chất lượng mà HCMUS-LDMS cần đáp ứng. Đây là cơ sở để lập Product Backlog, thiết kế, phát triển, kiểm thử và xác nhận kết quả; không mô tả chi tiết mã nguồn hoặc cách triển khai.

Dự án được thực hiện trước hết để phục vụ học tập. Hệ thống mô phỏng quy trình tiếp nhận tài liệu gốc, nhận dạng ký tự, hiệu chỉnh nội dung, quản lý thông tin mô tả, tạo EPUB, xuất bản, tìm kiếm và đọc trực tuyến. Các bên liên quan ngoài nhóm được xem là đối tượng tham khảo nếu dự án được mở rộng trong tương lai.

Baseline 11 tuần gồm 15 yêu cầu **Bắt buộc**. Sáu yêu cầu **Nên có** chỉ được thực hiện khi không ảnh hưởng đến baseline. Năm yêu cầu **Có thể xem xét** nằm ngoài baseline và chỉ được bổ sung khi nhóm xác nhận thay đổi.

Chi tiết câu chuyện người dùng, mức ưu tiên, ước lượng và tiêu chí chấp nhận được trình bày trong tài liệu **Product Backlog**. Kịch bản và bằng chứng xác nhận được trình bày trong tài liệu **Kế hoạch kiểm thử** và **Nhật ký dự án**.

## 2. Người sử dụng

| Vai trò                    | Nhu cầu chính                                                                 |
| -------------------------- | ----------------------------------------------------------------------------- |
| Độc giả                    | Tìm kiếm và đọc tài liệu đã xuất bản trong phạm vi được phép.                 |
| Thủ thư hoặc biên tập viên | Tiếp nhận tài liệu, theo dõi OCR, hiệu chỉnh, bổ sung thông tin và xuất bản.  |
| Quản trị viên              | Quản lý vai trò, quyền truy cập, danh mục và nhật ký thao tác.                |
| Thành viên nhóm            | Cài đặt, phát triển, kiểm thử và tái tạo kết quả trong môi trường thống nhất. |

## 3. Thuật ngữ và quy tắc nghiệp vụ

| Thuật ngữ                | Giải thích                                                                    |
| ------------------------ | ----------------------------------------------------------------------------- |
| Tài liệu gốc             | Tệp PDF hoặc ảnh quét được đưa vào hệ thống để xử lý.                         |
| OCR                      | Quá trình nhận dạng ký tự trong tài liệu gốc thành văn bản có thể hiệu chỉnh. |
| Tác vụ OCR               | Lần xử lý OCR có trạng thái chờ, đang xử lý, hoàn tất hoặc thất bại.          |
| Thông tin mô tả tài liệu | Dữ liệu như tên tài liệu, tác giả, năm xuất bản, danh mục và từ khóa.         |
| Bản nháp                 | Tài liệu đang được xử lý hoặc hiệu chỉnh và chưa được cung cấp cho độc giả.   |
| Xuất bản                 | Xác nhận tài liệu đạt điều kiện và cho phép người có quyền đọc trực tuyến.    |
| EPUB                     | Định dạng sách điện tử được tạo từ nội dung đã hiệu chỉnh.                    |
| Baseline                 | Phạm vi Bắt buộc đã được nhóm xác nhận cho thời gian thực hiện 11 tuần.       |

Các quy tắc nghiệp vụ chính:

- Chỉ người có quyền mới được tiếp nhận, hiệu chỉnh, quản lý hoặc xuất bản tài liệu.
- Tài liệu chỉ được xuất bản khi có nội dung hợp lệ, thông tin mô tả bắt buộc và tệp EPUB có thể sử dụng.
- Tài liệu chưa xuất bản hoặc ngoài phạm vi quyền không xuất hiện trong kết quả tìm kiếm của độc giả.
- Tài liệu gốc phải được bảo toàn trong quá trình OCR, hiệu chỉnh và xuất bản.
- Giao diện đọc không cung cấp chức năng tải trực tiếp tệp EPUB gốc.
- Dữ liệu riêng của một người dùng không được cung cấp cho người dùng khác nếu chưa được phép.

## 4. Yêu cầu chức năng

Mỗi yêu cầu chức năng sử dụng từ “phải” để thể hiện hành vi cần được kiểm tra. Cột Product Backlog cung cấp liên kết truy vết về phạm vi và tiêu chí chấp nhận tương ứng.

| Mã yêu cầu | Product Backlog | Yêu cầu                                                                                                                              | Priority       |
| ---------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------ | -------------- |
| `YC-001`   | `LDMS-001`      | Hệ thống phải có môi trường phát triển thống nhất để thành viên cài đặt, khởi chạy và kiểm thử theo cùng một hướng dẫn.              | Bắt buộc       |
| `YC-002`   | `LDMS-002`      | Hệ thống phải cho phép người có quyền tải tài liệu gốc hợp lệ lên và phải từ chối tệp không đáp ứng điều kiện tiếp nhận.             | Bắt buộc       |
| `YC-003`   | `LDMS-003`      | Hệ thống phải cho phép khởi chạy tác vụ OCR ở nền và theo dõi trạng thái chờ, đang xử lý, hoàn tất hoặc thất bại.                    | Bắt buộc       |
| `YC-004`   | `LDMS-004`      | Hệ thống phải lưu và hiển thị kết quả OCR theo đúng tài liệu và trang tương ứng.                                                     | Bắt buộc       |
| `YC-005`   | `LDMS-005`      | Hệ thống phải cho phép người có quyền sửa, lưu và mở lại văn bản đã hiệu chỉnh mà không làm thay đổi tài liệu gốc.                   | Bắt buộc       |
| `YC-006`   | `LDMS-006`      | Hệ thống nên cho phép hiển thị song song tài liệu gốc và văn bản tương ứng để hỗ trợ hiệu chỉnh.                                     | Nên có         |
| `YC-007`   | `LDMS-007`      | Hệ thống phải tạo được tệp EPUB có thể đọc từ nội dung đã hiệu chỉnh và không làm mất nội dung khi quá trình tạo tệp thất bại.       | Bắt buộc       |
| `YC-008`   | `LDMS-008`      | Hệ thống phải cho phép độc giả có quyền đọc tài liệu EPUB đã xuất bản trên máy tính và thiết bị di động.                             | Bắt buộc       |
| `YC-009`   | `LDMS-009`      | Hệ thống phải hỗ trợ đăng nhập bằng dữ liệu mô phỏng để kiểm thử các luồng chính trong môi trường học tập.                           | Bắt buộc       |
| `YC-010`   | `LDMS-010`      | Hệ thống phải kiểm tra vai trò và từ chối thao tác khi người dùng không có quyền tương ứng.                                          | Bắt buộc       |
| `YC-011`   | `LDMS-011`      | Hệ thống phải cho phép người có quyền tạo và cập nhật thông tin mô tả bắt buộc của tài liệu.                                         | Bắt buộc       |
| `YC-012`   | `LDMS-012`      | Hệ thống nên cho phép quản trị viên tạo, cập nhật và sử dụng danh mục để phân loại tài liệu.                                         | Nên có         |
| `YC-013`   | `LDMS-013`      | Hệ thống phải kiểm tra nội dung, thông tin mô tả và EPUB trước khi cho phép xuất bản, đồng thời nêu rõ điều kiện chưa đạt.           | Bắt buộc       |
| `YC-014`   | `LDMS-014`      | Hệ thống phải kiểm tra quyền đọc, bảo vệ tệp riêng tư và không cung cấp chức năng tải trực tiếp EPUB gốc cho độc giả.                | Bắt buộc       |
| `YC-015`   | `LDMS-015`      | Hệ thống phải tìm kiếm được tài liệu đã xuất bản theo thông tin mô tả và nội dung toàn văn trong phạm vi quyền truy cập.             | Bắt buộc       |
| `YC-016`   | `LDMS-016`      | Hệ thống phải hiển thị kết quả tìm kiếm có thông tin nhận biết, ngữ cảnh phù hợp và khả năng mở tài liệu hợp lệ.                     | Bắt buộc       |
| `YC-017`   | `LDMS-017`      | Hệ thống nên cho phép biên tập viên chuyển giữa các trang khi hiệu chỉnh mà không làm mất nội dung đã lưu.                           | Nên có         |
| `YC-018`   | `LDMS-018`      | Hệ thống nên hỗ trợ đăng nhập Google OAuth 2.0 khi môi trường được cấu hình và không được tạo phiên khi xác thực thất bại.           | Nên có         |
| `YC-019`   | `LDMS-019`      | Hệ thống có thể cho phép độc giả thay đổi thiết lập hiển thị mà không làm thay đổi nội dung tài liệu.                                | Có thể xem xét |
| `YC-020`   | `LDMS-020`      | Hệ thống có thể cho phép độc giả lưu, cập nhật và xóa vị trí đọc của chính mình.                                                     | Có thể xem xét |
| `YC-021`   | `LDMS-021`      | Hệ thống có thể cho phép độc giả tạo, xem, sửa và xóa đánh dấu hoặc ghi chú của chính mình trên tài liệu.                            | Có thể xem xét |
| `YC-022`   | `LDMS-022`      | Hệ thống nên hiển thị nguyên nhân phù hợp và cho phép người có quyền yêu cầu xử lý lại tác vụ OCR thất bại.                          | Nên có         |
| `YC-023`   | `LDMS-023`      | Hệ thống nên ghi nhật ký người thực hiện và thời điểm của các thao tác quan trọng, đồng thời bảo vệ nhật ký khỏi truy cập trái phép. | Nên có         |
| `YC-024`   | `LDMS-024`      | Hệ thống có thể tạo và cho phép sao chép trích dẫn từ thông tin mô tả theo định dạng được nhóm xác nhận.                             | Có thể xem xét |
| `YC-025`   | `LDMS-025`      | Hệ thống có thể hỗ trợ công cụ tìm kiếm mở rộng sau khi có dữ liệu chứng minh giải pháp hiện tại không đáp ứng nhu cầu.              | Có thể xem xét |
| `YC-026`   | `LDMS-026`      | Hệ thống phải hiển thị danh sách và trạng thái chính của các tài liệu thuộc phạm vi quản lý của người dùng.                          | Bắt buộc       |

Tổng số: **26 yêu cầu chức năng**, gồm **15 Bắt buộc**, **6 Nên có** và **5 Có thể xem xét**.

## 5. Yêu cầu phi chức năng

| Mã yêu cầu | Nhóm        | Yêu cầu và cách xác nhận                                                                                                                                    | Priority |
| ---------- | ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `YCP-01`   | Bảo mật     | Phân quyền phải được kiểm tra ở phía máy chủ; kiểm thử bằng tài khoản hợp lệ, tài khoản không đủ quyền và yêu cầu không xác thực.                           | Bắt buộc |
| `YCP-02`   | Bảo mật     | Thông tin bí mật phải được cấu hình ngoài mã nguồn; việc rà soát kho mã nguồn không được phát hiện khóa hoặc mật khẩu thật.                                 | Bắt buộc |
| `YCP-03`   | Bảo mật     | Tệp riêng tư không được dùng liên kết công khai lâu dài; quyền truy cập phải hết hiệu lực theo cấu hình hoặc khi phiên không còn hợp lệ.                    | Bắt buộc |
| `YCP-04`   | Tin cậy     | Tác vụ OCR hoặc tạo EPUB thất bại không được làm mất tài liệu gốc hay nội dung đã lưu trước đó.                                                             | Bắt buộc |
| `YCP-05`   | Khả dụng    | Các luồng chính phải hiển thị trạng thái đang xử lý, thành công, dữ liệu trống và lỗi bằng thông báo có thể hiểu được.                                      | Bắt buộc |
| `YCP-06`   | Tương thích | Các luồng chính phải được kiểm tra trên trình duyệt và kích thước màn hình được ghi trong Kế hoạch kiểm thử.                                                | Bắt buộc |
| `YCP-07`   | Hiệu năng   | OCR và tạo EPUB phải chạy dưới dạng tác vụ nền; thao tác khởi chạy phải trả trạng thái mà không chờ toàn bộ quá trình hoàn tất.                             | Bắt buộc |
| `YCP-08`   | Hiệu năng   | Tìm kiếm phải được đo bằng dữ liệu, môi trường, số lần chạy và cách tổng hợp đã ghi nhận; ngưỡng chấp nhận được xác nhận trong Kế hoạch kiểm thử trước UAT. | Bắt buộc |
| `YCP-09`   | Bảo trì     | Hệ thống phải có hướng dẫn cài đặt, cấu hình, khởi chạy và kiểm thử đủ để một thành viên khác tái tạo môi trường.                                           | Bắt buộc |
| `YCP-10`   | Truy vết    | Yêu cầu, hạng mục Product Backlog, kiểm thử và kết quả xác nhận phải sử dụng mã nhận diện để có thể đối chiếu.                                              | Bắt buộc |

Không sử dụng một con số hiệu năng làm baseline nếu chưa có kết quả đo hoặc xác nhận của nhóm. Chi tiết môi trường, dữ liệu, ngưỡng và kết quả được trình bày trong **Kế hoạch kiểm thử** và **Nhật ký dự án**.

## 6. Yêu cầu dữ liệu

| Nhóm dữ liệu             | Nội dung tối thiểu                                                 | Quy tắc chính                                                                |
| ------------------------ | ------------------------------------------------------------------ | ---------------------------------------------------------------------------- |
| Tài khoản và quyền       | Định danh người dùng, vai trò, trạng thái và quyền.                | Người dùng chỉ được truy cập dữ liệu và thao tác trong phạm vi quyền.        |
| Tài liệu                 | Mã tài liệu, tệp gốc, trạng thái, người tạo và thời điểm cập nhật. | Tệp gốc không bị ghi đè bởi kết quả OCR, hiệu chỉnh hoặc xuất bản.           |
| Thông tin mô tả tài liệu | Tên tài liệu, tác giả và các trường phân loại được sử dụng.        | Trường bắt buộc phải hợp lệ trước khi xuất bản.                              |
| Nội dung OCR             | Văn bản, tài liệu và trang tương ứng, trạng thái hiệu chỉnh.       | Nội dung phải gắn đúng tài liệu và trang; thay đổi đã lưu phải đọc lại được. |
| Bản xuất bản             | Tệp EPUB, trạng thái, người xác nhận và thời điểm xuất bản.        | Chỉ bản đạt điều kiện mới được cung cấp cho độc giả có quyền.                |
| Tác vụ và nhật ký        | Loại tác vụ, trạng thái, lỗi, người thực hiện và thời điểm.        | Lần xử lý lại và thao tác quan trọng phải có thể truy vết khi chức năng có.  |
| Dữ liệu cá nhân          | Vị trí đọc, đánh dấu và ghi chú gắn với người dùng.                | Người dùng chỉ được truy cập dữ liệu cá nhân của mình.                       |

Dữ liệu thử nghiệm phải được phân biệt với dữ liệu thực. Dự án không giả định được sử dụng dữ liệu thật của Thư viện nếu chưa có sự cho phép phù hợp.

Vòng đời xử lý tối thiểu gồm: chờ OCR, đang OCR, OCR hoàn tất, OCR thất bại, đang xuất bản, đã xuất bản và xuất bản thất bại. Tên kỹ thuật của trạng thái được xác định trong tài liệu **Kiến trúc phần mềm**.

## 7. Truy vết và xác nhận

Mỗi mã `YC-001`–`YC-026` truy vết một-một tới mã `LDMS-001`–`LDMS-026` cùng số thứ tự. Yêu cầu phi chức năng được gắn vào các kịch bản kiểm thử liên quan bằng mã `YCP`. Cách tổ chức này giúp đối chiếu phạm vi mà không lặp lại toàn bộ tiêu chí chấp nhận.

Một yêu cầu được xác nhận khi:

- Nội dung không mâu thuẫn với phạm vi và quy tắc nghiệp vụ.
- Priority khớp với Product Backlog.
- Có tiêu chí chấp nhận quan sát được trong Product Backlog.
- Có kịch bản kiểm thử và kết quả được ghi nhận trong bộ tài liệu dự án.
- Không còn lỗi nghiêm trọng làm cho kết quả không thể sử dụng theo mục đích đã nêu.

Nhóm Sebros xác nhận toàn bộ 26 yêu cầu chức năng và 10 yêu cầu phi chức năng trong tài liệu này làm baseline nội bộ. Việc xác nhận không đồng nghĩa rằng các hạng mục Nên có hoặc Có thể xem xét được đưa vào baseline triển khai.

## 8. Giả định, giới hạn và quản lý thay đổi

Các giả định chính:

- Nhóm gồm sáu sinh viên và triển khai dự án trong 11 tuần để phục vụ môn học.
- Môi trường, dữ liệu và tài khoản sử dụng cho phát triển và kiểm thử có thể là dữ liệu mô phỏng.
- Đại diện Thư viện và các bên liên quan bên ngoài chỉ được tham vấn khi dự án có điều kiện mở rộng.

Các giới hạn chính:

- Không khẳng định độ chính xác OCR, khả năng chịu tải hoặc mức sẵn sàng vận hành khi chưa có dữ liệu đo.
- Không xem đăng nhập Google OAuth 2.0, dữ liệu thật hoặc hạ tầng vận hành chính thức là điều kiện bắt buộc của baseline.
- Không xem các hạng mục Có thể xem xét là cam kết thực hiện trong 11 tuần.

Khi thay đổi yêu cầu, nhóm phải ghi nhận lý do, Priority, tác động tới baseline, thời gian, chất lượng và các hạng mục liên quan. Thay đổi chỉ có hiệu lực sau khi nhóm Sebros xác nhận và cập nhật đồng thời **Yêu cầu phần mềm**, **Product Backlog**, **Kế hoạch kiểm thử** cùng các tài liệu bị ảnh hưởng.

## 9. Tài liệu tham khảo

- Đề xuất dự án.
- Viễn cảnh và phạm vi.
- Ủy nhiệm dự án.
- Product Backlog.
- Kiến trúc phần mềm.
- Bản mô tả công việc.
- Kế hoạch dự án.
- Kế hoạch kiểm thử.
- Kế hoạch quản lý chất lượng.
- Kế hoạch quản lý rủi ro.
- Nhật ký dự án.
