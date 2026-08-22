# HƯỚNG DẪN SỬ DỤNG HỆ THỐNG

## Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS (HCMUS-LDMS)

### Thông tin tài liệu

| Trường | Nội dung |
|---|---|
| Mã tài liệu | `HCMUS-LDMS-UG` |
| Chủ sở hữu | Frontend Lead và QA |
| Phiên bản | 1.0 — 22/08/2026 |
| Trạng thái | Hướng dẫn theo đường cơ sở yêu cầu; cần đối chiếu giao diện thực tế trước phát hành |
| Đối tượng | Độc giả, Biên tập viên/Thủ thư và Quản trị viên |

## Mục lục

- [1. Phạm vi và lưu ý](#1-phạm-vi-và-lưu-ý)
- [2. Đăng nhập và vai trò](#2-đăng-nhập-và-vai-trò)
- [3. Tải và theo dõi tài liệu](#3-tải-và-theo-dõi-tài-liệu)
- [4. Hiệu chỉnh và thông tin mô tả](#4-hiệu-chỉnh-và-thông-tin-mô-tả)
- [5. Tạo EPUB và xuất bản](#5-tạo-epub-và-xuất-bản)
- [6. Tìm kiếm và đọc trực tuyến](#6-tìm-kiếm-và-đọc-trực-tuyến)
- [7. Quản trị và xử lý lỗi](#7-quản-trị-và-xử-lý-lỗi)
- [8. Bảo mật và hỗ trợ](#8-bảo-mật-và-hỗ-trợ)

## 1. Phạm vi và lưu ý

Hướng dẫn mô tả hành vi dự kiến của 15 chức năng Bắt buộc. Tên nút/đường dẫn cụ thể phải được đối chiếu build dùng để bàn giao; tài liệu không khẳng định màn hình chưa kiểm chứng đã tồn tại. Không dùng tài liệu thật khi chưa xác nhận quyền số hóa và quyền đọc.

## 2. Đăng nhập và vai trò

1. Mở địa chỉ của môi trường được nhóm cung cấp.
2. Chọn cơ chế đăng nhập đang được cấu hình: tài khoản thử ở local hoặc Google khi demo đã cấu hình.
3. Nếu thông tin hợp lệ, hệ thống tạo phiên và chuyển đến trang phù hợp vai trò.
4. Nếu thất bại, đọc thông báo; không gửi mật khẩu/token qua kênh chat công khai.

| Vai trò | Quyền chính |
|---|---|
| Độc giả | Tìm kiếm và đọc tài liệu đã xuất bản được phép xem |
| Biên tập viên/Thủ thư | Tải, theo dõi OCR, hiệu chỉnh, nhập metadata và chuẩn bị xuất bản |
| Quản trị viên | Quản lý vai trò/quyền và danh mục khi chức năng tương ứng có trong bản dựng |

Không đủ quyền phải nhận thông báo từ chối; việc ẩn nút không thay thế kiểm tra phía máy chủ.

## 3. Tải và theo dõi tài liệu

### 3.1. Tải tài liệu

1. Vào khu vực quản lý tài liệu và chọn **Tải tài liệu**.
2. Chọn PDF/ảnh thuộc bộ dữ liệu đã được phép sử dụng.
3. Kiểm tra loại/kích thước và thông tin nguồn theo biểu mẫu.
4. Xác nhận tải lên; chờ thông báo tiếp nhận và mã/trạng thái tài liệu.

Tệp sai loại, rỗng, hỏng hoặc vượt giới hạn phải bị từ chối kèm lý do. Nếu không rõ file đã được tiếp nhận, không tải lặp nhiều lần; kiểm tra danh sách/trạng thái trước.

### 3.2. Theo dõi OCR

Trạng thái có thể gồm Chờ xử lý, Đang xử lý, Hoàn tất hoặc Thất bại. Khi thất bại, người có quyền xem lý do phù hợp và dùng **Xử lý lại** nếu chức năng được cung cấp. Retry không được làm mất tệp gốc hoặc nội dung đã lưu.

## 4. Hiệu chỉnh và thông tin mô tả

### 4.1. Hiệu chỉnh

1. Mở tài liệu có OCR hoàn tất.
2. Đối chiếu bản gốc với văn bản theo trang.
3. Sửa nội dung; chọn **Lưu** trước khi chuyển trang hoặc rời màn hình.
4. Mở lại để chắc rằng thay đổi đã được lưu.

Khi save lỗi, giữ nội dung đang nhập nếu giao diện hỗ trợ, ghi lại trang và thử lại sau khi kết nối ổn định. Không sửa trực tiếp hoặc xóa tệp gốc.

### 4.2. Thông tin mô tả

Nhập tên, tác giả, năm, thể loại/danh mục, từ khóa và các trường bắt buộc được hiển thị. Hệ thống phải báo trường thiếu/sai. Việc gán danh mục có sẵn thuộc phạm vi bắt buộc; quản trị cây danh mục là chức năng Nên có.

## 5. Tạo EPUB và xuất bản

1. Kiểm tra nội dung đã hiệu chỉnh và metadata bắt buộc.
2. Chọn tạo EPUB hoặc bước chuẩn bị xuất bản theo giao diện của bản dựng.
3. Chờ job hoàn tất; mở thử EPUB bằng trình đọc.
4. Người có quyền chọn **Xuất bản** khi toàn bộ điều kiện đạt.

Nếu thiếu điều kiện, hệ thống phải chặn và liệt kê lý do. Nếu tạo EPUB thất bại, xem trạng thái/lỗi và retry có kiểm soát; không xuất bản artifact lỗi.

## 6. Tìm kiếm và đọc trực tuyến

### 6.1. Tìm kiếm

1. Nhập từ khóa trong khu vực tìm kiếm.
2. Xem tên, tác giả, năm/danh mục và thông tin nhận biết.
3. Chọn đúng tài liệu; tài liệu draft/private trái quyền không được xuất hiện.

Trạng thái không có kết quả khác với lỗi hệ thống. Nếu thấy tài liệu không thuộc quyền, dừng truy cập và báo ngay cho nhóm.

### 6.2. Đọc

Độc giả đủ quyền mở tài liệu đã xuất bản bằng trình đọc EPUB, điều hướng nội dung và dùng giao diện trên viewport mục tiêu. Giao diện không hiển thị nút tải trực tiếp tệp EPUB gốc; điều này không được mô tả như cơ chế chống sao chép tuyệt đối.

## 7. Quản trị và xử lý lỗi

Quản trị viên gán vai trò theo nguyên tắc quyền tối thiểu. Thay đổi quyền phải có actor, action và thời gian trong nhật ký phù hợp. Khi gặp lỗi:

| Tình huống | Hành động người dùng |
|---|---|
| 401/phiên hết hạn | Đăng nhập lại; không chia sẻ token |
| 403/không đủ quyền | Kiểm tra vai trò; liên hệ quản trị, không thử vượt quyền |
| Upload/job thất bại | Ghi mã tài liệu/job, thời gian, thông báo; thử lại khi được phép |
| Nội dung không lưu | Không tiếp tục sửa nhiều trang; ghi trang và báo lỗi |
| EPUB không mở | Ghi tài liệu/build/browser; không đánh dấu xuất bản đạt |
| Tài liệu trái quyền xuất hiện | Dừng truy cập và báo sự cố bảo mật |

## 8. Bảo mật và hỗ trợ

- Không gửi password, token, signed URL hoặc dữ liệu thật qua kênh không được duyệt.
- Đăng xuất khi dùng máy chung; không dùng tài khoản quản trị cho đọc thông thường.
- Báo lỗi với thời gian, môi trường, build, bước, expected/actual và ảnh đã che dữ liệu nhạy cảm.
- Kênh hỗ trợ/địa chỉ chính thức chưa được xác nhận trong bộ tài liệu; PM phải bổ sung trước bàn giao.

Nguồn hành vi: [SRS](04-software-requirements.md), [Backlog](04-product-backlog.md), [Prototype](07-prototype.md), [Test Plan](20-test-plan.md) và [DevOps](15-devops-and-operations.md).
