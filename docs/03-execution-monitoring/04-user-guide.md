# BỘ CẨM NANG HƯỚNG DẪN SỬ DỤNG HỆ THỐNG HCMUS-LDMS
## User Guides Suite for HCMUS Library Digitization & Management System

### THÔNG TIN TÀI LIỆU (DOCUMENT CONTROL)

| Trường thông tin (Field) | Nội dung đặc tả (Description) |
| :--- | :--- |
| **Mã tài liệu (Document ID)** | `HCMUS-LDMS-UG-INDEX` |
| **Tên tài liệu (Document Title)** | Tổng mục lục Bộ Cẩm nang Hướng dẫn Sử dụng Hệ thống (User Guides Suite) |
| **Dự án (Project Name)** | Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS (HCMUS-LDMS) |
| **Đơn vị soạn thảo (Author/Organization)** | Nhóm Phát triển Dự án HCMUS-LDMS |
| **Người phụ trách biên soạn** | Ngô Nguyễn Thế Khoa (MSSV: 23127065) |
| **Cấp độ bảo mật (Security Class)** | Public / Internal Users |
| **Trạng thái tài liệu (Status)** | Phát hành chính thức (Active) |

### LỊCH SỬ PHIÊN BẢN (REVISION HISTORY)

| Phiên bản (Version) | Ngày phát hành (Date) | Mô tả thay đổi (Description of Change) | Người thực hiện (Author) |
| :---: | :---: | :--- | :---: |
| 1.0 | 21/08/2026 | Khởi tạo tài liệu tổng quan và bộ 3 cẩm nang hướng dẫn sử dụng chuyên biệt cho 3 nhóm người dùng: Độc giả (Reader), Biên tập viên (Editor) và Quản trị viên (Admin). | Ngô Nguyễn Thế Khoa |

---

## Mục lục

- [1. Giới thiệu Bộ Cẩm nang Hướng dẫn Sử dụng](#1-giới-thiệu-bộ-cẩm-nang-hướng-dẫn-sử-dụng)
- [2. Phân loại Hướng dẫn theo Nhóm Người dùng](#2-phân-loại-hướng-dẫn-theo-nhóm-người-dùng)
- [3. Hướng dẫn dành cho Độc giả (Reader)](#3-hướng-dẫn-dành-cho-độc-giả-reader)
- [4. Hướng dẫn dành cho Biên tập viên (Editor)](#4-hướng-dẫn-dành-cho-biên-tập-viên-editor)
- [5. Hướng dẫn dành cho Quản trị viên (Admin)](#5-hướng-dành-cho-quản-trị-viên-admin)
- [6. Bảng Ma trận Quyền hạn và Tính năng Tương ứng](#6-bảng-ma-trận-quyền-hạn-và-tính-năng-tương-ứng)

---

## 1. Giới thiệu Bộ Cẩm nang Hướng dẫn Sử dụng

Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS (**HCMUS-LDMS**) là giải pháp chuyển đổi số toàn diện cho công tác quản trị, xử lý và phục vụ tài liệu học liệu tại Trường Đại học Khoa học Tự nhiên - ĐHQG-HCM.

Để phục vụ tốt nhất cho từng đối tượng tương tác với hệ thống, bộ tài liệu hướng dẫn sử dụng được chia thành **3 cẩm nang chuyên sâu độc lập**:

```
docs/03-execution-monitoring/
├── 04-user-guide.md            # [Tài liệu hiện tại] Tổng quan bộ cẩm nang
├── 04-user-guide-reader.md     # Cẩm nang chuyên sâu dành cho ĐỘC GIẢ (Reader)
├── 04-user-guide-editor.md     # Cẩm nang chuyên sâu dành cho BIÊN TẬP VIÊN (Editor)
└── 04-user-guide-admin.md      # Cẩm nang chuyên sâu dành cho QUẢN TRỊ VIÊN (Admin)
```

---

## 2. Phân loại Hướng dẫn theo Nhóm Người dùng

| Nhóm người dùng | Đối tượng thực tế | Tài liệu chi tiết | Định dạng PDF đính kèm |
| :--- | :--- | :--- | :--- |
| **1. Độc giả (Reader)** | Sinh viên, học viên cao học, giảng viên, nhà nghiên cứu | [04-user-guide-reader.md](./04-user-guide-reader.md) | [04-user-guide-reader.pdf](./04-user-guide-reader.pdf) |
| **2. Biên tập viên (Editor)** | Thủ thư số hóa, cán bộ xử lý học liệu, cộng tác viên | [04-user-guide-editor.md](./04-user-guide-editor.md) | [04-user-guide-editor.pdf](./04-user-guide-editor.pdf) |
| **3. Quản trị viên (Admin)** | Quản trị viên hệ thống CNTT Thư viện, Trưởng phòng | [04-user-guide-admin.md](./04-user-guide-admin.md) | [04-user-guide-admin.pdf](./04-user-guide-admin.pdf) |

---

## 3. Hướng dẫn dành cho Độc giả (Reader)

* **Tài liệu chi tiết:** [`docs/03-execution-monitoring/04-user-guide-reader.md`](./04-user-guide-reader.md)
* **Nội dung cốt lõi:**
  * **Tìm kiếm toàn văn (Full-Text Search - FTS):** Tra cứu từ khóa sâu trong nội dung hàng ngàn trang sách tiếng Việt với tốc độ dưới 3 giây, hiển thị trích đoạn ngữ cảnh làm nổi bật từ khóa tìm kiếm.
  * **Trình đọc sách EPUB thông minh:** Đọc sách responsive trên mọi kích cỡ màn hình thiết bị, điều hướng mượt mà, tự động nhớ vị trí đang đọc dở (chuẩn EPUB CFI).
  * **Tùy biến trải nghiệm đọc:** Điều chỉnh tăng/giảm cỡ chữ từ 80% đến 200%, chuyển đổi màu nền Sáng (Light) / Tối (Dark) chống mỏi mắt và tự lưu cấu hình.
  * **Đánh dấu (Highlight) & Ghi chú (Notes):** Bôi đen đoạn văn để tô màu highlight vàng nhạt, viết ghi chú phân tích và quản lý trích dẫn qua thanh bên (Sidebar).
  * **Bảo vệ bản quyền học liệu:** Đọc sách an toàn thông qua Presigned URL bảo mật có thời hạn 15 phút.

---

## 4. Hướng dẫn dành cho Biên tập viên (Editor)

* **Tài liệu chi tiết:** [`docs/03-execution-monitoring/04-user-guide-editor.md`](./04-user-guide-editor.md)
* **Nội dung cốt lõi:**
  * **Tải lên tài liệu số hóa:** Hỗ trợ tải các tệp scan dạng PDF, JPG, PNG với chuẩn khuyến nghị 300 DPI.
  * **Theo dõi tiến trình OCR tự động:** Bảng điều khiển thời gian thực (Live Dashboard) tự cập nhật mỗi 2 giây, hỗ trợ tính năng "Thử lại" (Retry OCR) khi gặp sự cố.
  * **Trình biên tập màn hình đôi (Split-screen Editor):** Không gian làm việc trực quan đối chiếu ảnh scan gốc ở khung trái và khung soạn thảo văn bản nhận dạng ở khung phải, có cơ chế cảnh báo chống mất dữ liệu khi chuyển trang.
  * **Nhập siêu dữ liệu chuẩn thư viện:** Khai báo Tiêu đề, Tác giả, Vị trí kệ sách vật lý, gán danh mục 2 cấp và gắn thẻ (tags) linh hoạt.
  * **Đóng gói & Xuất bản EPUB:** Kích hoạt tiến trình Pandoc tự động tạo tệp EPUB 3.0 và cập nhật chỉ mục FTS vào cơ sở dữ liệu.

---

## 5. Hướng dẫn dành cho Quản trị viên (Admin)

* **Tài liệu chi tiết:** [`docs/03-execution-monitoring/04-user-guide-admin.md`](./04-user-guide-admin.md)
* **Nội dung cốt lõi:**
  * **Quản trị cây danh mục 2 cấp:** Khởi tạo, đổi tên và xóa các danh mục cấp 1 (Khối ngành/Khoa) và danh mục cấp 2 (Chuyên ngành con) với giao diện trực quan.
  * **Phân quyền tài khoản (RBAC):** Xét duyệt các yêu cầu nâng quyền từ `reader` lên `editor` tại trang Yêu cầu, quản lý quyền hạn truy cập an toàn.
  * **Kiểm soát & Giám sát toàn diện:** Đặc quyền chỉnh sửa và can thiệp chất lượng trên toàn bộ kho tài liệu, cưỡng chế chạy lại các job OCR bị lỗi.
  * **Cấu hình vận hành & Bảo mật:** Quản trị danh sách domain email cho phép đăng nhập SSO, cấu hình thời gian sống của Presigned URL, quy trình sao lưu và phục hồi dữ liệu định kỳ.

---

## 6. Bảng Ma trận Quyền hạn và Tính năng Tương ứng

| Chức năng chính | Màn hình | Reader | Editor | Admin |
| :--- | :--- | :---: | :---: | :---: |
| Tra cứu FTS & Đọc sách EPUB | `/documents`, `/search`, `/reader/:id` |  |  |  |
| Tùy chỉnh Cỡ chữ, Theme, Highlight | `/reader/:id` |  |  |  |
| Tải lên tệp scan & Theo dõi OCR | `/`, `/dashboard` | ❌ |  |  |
| Đối chiếu Split-screen & Sửa text | `/documents/:id` | ❌ (Chỉ đọc) |  (Sách sở hữu) |  (Toàn bộ) |
| Nhập Metadata & Xuất bản EPUB | `/documents/:id` | ❌ |  (Sách sở hữu) |  (Toàn bộ) |
| Quản lý Cây danh mục 2 cấp | `/categories` | ❌ | ❌ |  |
| Duyệt Yêu cầu Nâng quyền | `/requests` | ❌ | ❌ |  |
