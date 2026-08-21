# CẨM NANG HƯỚNG DẪN SỬ DỤNG HỆ THỐNG — DÀNH CHO BIÊN TẬP VIÊN (EDITOR)

## Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS (HCMUS-LDMS)

### THÔNG TIN TÀI LIỆU (DOCUMENT CONTROL)

| Trường thông tin (Field) | Nội dung đặc tả (Description) |
| :--- | :--- |
| **Mã tài liệu (Document ID)** | `HCMUS-LDMS-UG-EDITOR` |
| **Tên tài liệu (Document Title)** | Cẩm nang Hướng dẫn Sử dụng dành cho Biên tập viên (Editor User Guide) |
| **Dự án (Project Name)** | Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS (HCMUS-LDMS) |
| **Đơn vị soạn thảo (Author/Organization)** | Nhóm Phát triển Dự án HCMUS-LDMS |
| **Người phụ trách biên soạn** | Ngô Nguyễn Thế Khoa (MSSV: 23127065) |
| **Cấp độ bảo mật (Security Class)** | Internal / Library Staff & Editors (Thủ thư & Biên tập viên) |
| **Trạng thái tài liệu (Status)** | Phát hành chính thức (Active) |

### LỊCH SỬ PHIÊN BẢN (REVISION HISTORY)

| Phiên bản (Version) | Ngày phát hành (Date) | Mô tả thay đổi (Description of Change) | Người thực hiện (Author) |
| :---: | :---: | :--- | :---: |
| 1.0 | 21/08/2026 | Khởi tạo cẩm nang hướng dẫn sử dụng chi tiết cho Biên tập viên (Editor): Tải lên bản scan, Giám sát OCR tự động, Hiệu chỉnh Split-screen đối chiếu hình ảnh - văn bản, Nhập siêu dữ liệu Dublin Core và Đóng gói xuất bản EPUB 3.0. | Ngô Nguyễn Thế Khoa |

---

## Mục lục

- [1. Giới thiệu Vai trò & Quyền hạn Biên tập viên](#1-giới-thiệu-vai-trò--quyền-hạn-biên-tập-viên)
- [2. Quy trình Tải lên Tài liệu Số hóa (Upload Page)](#2-quy-trình-tải-lên-tài-liệu-số-hóa-upload-page)
  - [2.1 Chuẩn bị tệp scan và tiêu chuẩn chất lượng](#21-chuẩn-bị-tệp-scan-và-tiêu-chuẩn-chất-lượng)
  - [2.2 Thao tác tải lên tài liệu](#22-thao-tác-tải-lên-tài-liệu)
  - [2.3 Luồng xử lý ngầm của hệ thống (Under the Hood)](#23-luồng-xử-lý-ngầm-của-hệ-thống-under-the-hood)
- [3. Theo dõi Tiến trình OCR Tự động (Dashboard OCR)](#3-theo-dõi-tiến-trình-ocr-tự-động-dashboard-ocr)
  - [3.1 Bảng điều khiển thời gian thực (Live Dashboard)](#31-bảng-điều-khiển-thời-gian-thực-live-dashboard)
  - [3.2 Các trạng thái vòng đời xử lý OCR](#32-các-trạng-thái-vòng-đời-xử-lý-ocr)
  - [3.3 Tính năng Thử lại (Retry OCR) khi gặp sự cố](#33-tính-năng-thử-lại-retry-ocr-khi-gặp-sự-cố)
- [4. Sử dụng Trình biên tập Đối chiếu Màn hình đôi (Split-screen Editor)](#4-sử-dụng-trình-biên-tập-đối-chiếu-màn-hình-đôi-split-screen-editor)
  - [4.1 Bố cục không gian làm việc màn hình đôi](#41-bố-cục-không-gian-làm-việc-màn-hình-đôi)
  - [4.2 Điều hướng giữa các trang tài liệu](#42-điều-hướng-giữa-các-trang-tài-liệu)
  - [4.3 Cơ chế cảnh báo dữ liệu chưa lưu (Data Loss Prevention)](#43-cơ-chế-cảnh-báo-dữ-liệu-chưa-lưu-data-loss-prevention)
  - [4.4 Thao tác soát lỗi và lưu văn bản từng trang](#44-thao-tác-soát-lỗi-và-lưu-văn-bản-từng-trang)
- [5. Nhập và Quản lý Siêu dữ liệu Sách (Dublin Core Metadata & Tags)](#5-nhập-và-quản-lý-siêu-dữ-liệu-sách-dublin-core-metadata--tags)
  - [5.1 Các trường siêu dữ liệu chuẩn thư viện](#51-các-trường-siêu-dữ-liệu-chuẩn-thư-viện)
  - [5.2 Gán danh mục phân loại 2 cấp (Category Taxonomy)](#52-gán-danh-mục-phân-loại-2-cấp-category-taxonomy)
  - [5.3 Gán và quản lý thẻ linh hoạt (Tags)](#53-gán-và-quản-lý-thẻ-linh-hoạt-tags)
- [6. Đóng gói & Đề xuất Xuất bản Sách EPUB (Publishing Workflow)](#6-đóng-gói--đề-xuất-xuất-bản-sách-epub-publishing-workflow)
  - [6.1 Điều kiện tiên quyết để xuất bản](#61-điều-kiện-tiên-quyết-để-xuất-bản)
  - [6.2 Kích hoạt tiến trình đóng gói Pandoc EPUB 3.0](#62-kích-hoạt-tiến-trình-đóng-gói-pandoc-epub-30)
  - [6.3 Kiểm tra chất lượng sách hoàn thiện trên Reader](#63-kiểm-tra-chất-lượng-sách-hoàn-thiện-trên-reader)
- [7. Kinh nghiệm & Thực hành Tốt nhất cho Biên tập viên (Best Practices)](#7-kinh-nghiệm--thực-hành-tốt-nhất-cho-biên-tập-viên-best-practices)
- [8. Xử lý Sự cố Thường gặp (Troubleshooting)](#8-xử-lý-sự-cố-thường-gặp-troubleshooting)

---

## 1. Giới thiệu Vai trò & Quyền hạn Biên tập viên

Trong hệ thống HCMUS-LDMS, **Biên tập viên (Editor)** là lực lượng nòng cốt (bao gồm các thủ thư, chuyên viên số hóa tài liệu và cộng tác viên học liệu) chịu trách nhiệm biến các bản quét tài liệu/giáo trình thô thành các ấn phẩm số hóa EPUB hoàn chỉnh, chất lượng cao và sẵn sàng phục vụ bạn đọc.

Biên tập viên vận hành theo mô hình **Human-in-the-Loop (AI OCR hỗ trợ + Con người kiểm định)**: Công nghệ OCR tự động nhận diện phần lớn văn bản, sau đó biên tập viên sử dụng trình biên tập màn hình đôi để rà soát, đối chiếu và chuẩn hóa nội dung trước khi xuất bản.

```
+-----------------------------------------------------------------------------------------+
|                                    LUỒNG BIÊN TẬP VIÊN                                  |
|                                                                                         |
|  [Tải tệp PDF/Ảnh]  -->  [Theo dõi OCR Dashboard]  -->  [Split-screen: Đối chiếu & Sửa] |
|                                                                     |                   |
|                                                                     v                   |
|  [Xem trước trên Reader] <-- [Đóng gói Xuất bản EPUB] <-- [Nhập Metadata & Gắn Tags]    |
+-----------------------------------------------------------------------------------------+
```

### Bảng so sánh quyền hạn Biên tập viên (Editor) trong hệ thống

| Quyền hạn / Thao tác | Reader | Editor | Admin |
| :--- | :---: | :---: | :---: |
| Tra cứu FTS & Đọc sách EPUB | Có | Có | Có |
| Tải tệp PDF / Ảnh scan lên hệ thống | Không | **Có** | Có |
| Theo dõi và Retry các job OCR trên Dashboard | Không | **Có** | Có |
| Sử dụng Split-screen Editor chỉnh sửa văn bản | Không | **Có (Sách sở hữu)** | Có (Toàn quyền) |
| Nhập / Cập nhật Metadata Dublin Core & Tags | Không | **Có (Sách sở hữu)** | Có (Toàn quyền) |
| Đóng gói và phát hành sách EPUB | Không | **Có (Sách sở hữu)** | Có (Toàn quyền) |
| Tạo / Đổi tên / Xóa Danh mục 2 cấp | Không | Không | **Có** |
| Phê duyệt yêu cầu nâng quyền tài khoản | Không | Không | **Có** |

> **Lưu ý về quyền sở hữu (Ownership RBAC):** Biên tập viên có toàn quyền chỉnh sửa và xuất bản các tài liệu do chính tài khoản của mình tải lên (`owner_id === current_user_id`). Đối với tài liệu do biên tập viên khác tải lên, chỉ tài khoản Quản trị viên (`admin`) hoặc chính chủ mới có quyền chỉnh sửa.

---

## 2. Quy trình Tải lên Tài liệu Số hóa (Upload Page)

### 2.1 Chuẩn bị tệp scan và tiêu chuẩn chất lượng

Để đảm bảo độ chính xác nhận dạng ký tự (OCR Accuracy) đạt mức tối ưu (mục tiêu hệ thống **≥ 85%** đối với tiếng Việt):

1. **Định dạng được hỗ trợ:** `.pdf`, `.jpg`, `.jpeg`, `.png`.
2. **Khuyến nghị kỹ thuật khi scan:**
   * **Độ phân giải:** Tối thiểu **300 DPI** (khuyến nghị 300 - 400 DPI cho tài liệu chữ in thông thường).
   * **Định hướng trang:** Trang sách phải được xoay thẳng, không bị nghiêng lệch (skew angle < 2 độ).
   * **Độ tương phản:** Chữ in đậm rõ nét trên nền giấy trắng sáng, hạn chế bóng đổ ở gáy sách hoặc vết ố vàng.
   * **Cắt lề:** Loại bỏ các phần ngón tay giữ sách hoặc viền đen quét thừa để OCR không sinh ra các ký tự rác.

### 2.2 Thao tác tải lên tài liệu

1. Truy cập trang chủ hoặc nhấp vào mục **"Tải lên"** trên thanh điều hướng (`/`).
2. Tại khung **"Tải tài liệu scan"** (`UploadCard`):
   * Nhấp vào ô chọn tệp để mở cửa sổ trình duyệt file trên máy tính hoặc kéo thả file vào khung.
   * Hệ thống hiển thị tên file đã chọn (ví dụ: `Giai_Tich_1_HCMUS.pdf`).
3. Bấm nút **"Tải tài liệu lên"** (`isUploading`).
4. Khi tải lên hoàn tất, hệ thống hiển thị thông báo thành công màu xanh lá kèm các thông tin khởi tạo:
   * **ID:** Mã định danh duy nhất của tài liệu (ví dụ: `doc_9a8b7c6d...`).
   * **Tên file:** Tên tệp gốc được giữ nguyên.
   * **Trạng thái:** Khởi tạo ở trạng thái `pending`.
   * **Thời điểm tạo:** Ngày giờ tải lên theo chuẩn Việt Nam.
   * Bảng điều khiển thu nhỏ (`OcrStatusPanel`) hiển thị ngay trạng thái xử lý của tài liệu.

### 2.3 Luồng xử lý ngầm của hệ thống (Under the Hood)

Ngay sau khi tệp tin được tải lên:
1. **Lưu trữ Object Storage:** Tệp gốc được đẩy an toàn vào MinIO bucket `documents`.
2. **Khởi tạo Database Record:** Bản ghi tài liệu được ghi vào cơ sở dữ liệu PostgreSQL.
3. **Kích hoạt Hàng đợi OCR:** FastAPI BackgroundTasks khởi chạy tiến trình trích xuất:
   * Chuyển đổi các trang PDF thành các tệp ảnh riêng biệt bằng thư viện `poppler` (`pdf2image`).
   * Gọi công cụ Tesseract OCR với tập ngôn ngữ tiếng Việt và tiếng Anh (`vie+eng`) để bóc tách văn bản từng trang.
   * Lưu các đoạn văn bản thô vào bảng `document_pages` trong cơ sở dữ liệu.

---

## 3. Theo dõi Tiến trình OCR Tự động (Dashboard OCR)

### 3.1 Bảng điều khiển thời gian thực (Live Dashboard)

Biên tập viên truy cập mục **"Dashboard OCR"** (`/dashboard`) trên thanh menu điều hướng.

Giao diện Dashboard được trang bị cơ chế **Live Polling (tự động cập nhật mỗi 2 giây)**, giúp theo dõi trạng thái xử lý hàng loạt tài liệu mà không cần tải lại trang thủ công:
* **Hàng thẻ thống kê tổng quan (`Summary Grid`):**
  * `Đang chờ` (Pending): Số tài liệu đang xếp hàng đợi phân bổ tài nguyên.
  * `Đang nhận dạng` (Processing): Số tài liệu đang được các tiến trình OCR thực hiện.
  * `Hoàn tất` (Completed): Số tài liệu đã xử lý xong OCR, sẵn sàng chuyển sang bước hiệu chỉnh.
  * `Thất bại` (Failed): Số tài liệu gặp lỗi trong quá trình OCR.
* **Đèn tín hiệu Live:** Nhấp nháy xanh lá báo hiệu kết nối theo dõi thời gian thực đang hoạt động.
* **Nút "Làm mới":** Cho phép chủ động yêu cầu đồng bộ trạng thái ngay lập tức.

### 3.2 Các trạng thái vòng đời xử lý OCR

Trong bảng **"Tiến trình tài liệu"** (`Jobs Table`):

| Trạng thái | Biểu tượng / Màu sắc | Ý nghĩa | Hành động tiếp theo của Editor |
| :--- | :--- | :--- | :--- |
| `pending` | Huy hiệu xám (`status-pending`) | Tài liệu đang nằm trong hàng đợi xử lý | Chờ vài giây để worker tiếp nhận |
| `processing` | Huy hiệu xanh dương có xung nhịp (`status-processing`) | Worker đang bóc tách trang và chạy Tesseract OCR | Chờ tiến trình hoàn tất |
| `completed` | Huy hiệu xanh lá (`status-completed`) | Nhận dạng toàn bộ các trang thành công | Nhấp vào tài liệu để mở Split-screen Editor |
| `failed` | Huy hiệu đỏ (`status-failed`) | Quá trình OCR gặp sự cố lỗi | Đọc thông báo lỗi và bấm "Thử lại" |

### 3.3 Tính năng Thử lại (Retry OCR) khi gặp sự cố

Nếu một tài liệu bị rơi vào trạng thái `failed` (ví dụ: máy chủ bị nghẽn bộ nhớ tạm thời hoặc tệp scan có trang bị lỗi định dạng cục bộ):

1. Cột **"Lỗi / thao tác"** sẽ hiển thị chi tiết thông báo lỗi nhận được từ worker.
2. Biên tập viên nhấp vào nút **"Thử lại"** (`handleRetry`) bên cạnh tài liệu bị lỗi.
3. Hệ thống sẽ cấp số lần chạy mới (`Attempt #2`, `Attempt #3`), dọn dẹp dữ liệu tạm trước đó và đưa tài liệu trở lại hàng đợi xử lý tự động mà không bắt buộc biên tập viên phải upload lại file từ đầu.

---

## 4. Sử dụng Trình biên tập Đối chiếu Màn hình đôi (Split-screen Editor)

Trình biên tập màn hình đôi (`DocumentViewerPage` tại `/documents/:documentId`) là công cụ quan trọng nhất giúp đảm bảo tính chính xác và chất lượng của tài liệu số hóa.

```
+-----------------------------------------------------------------------------+
| TRÌNH BIÊN TẬP ĐỐI CHIẾU MÀN HÌNH ĐÔI (SPLIT-SCREEN EDITOR)                 |
|                                                                             |
| Trang: [ 1 ] [ (2) ] [ 3 ] [ 4 ] [ 5 ] ...                                  |
| +------------------------------------+------------------------------------+ |
| | KHUNG TRÁI: ẢNH SCAN GỐC           | KHUNG PHẢI: VĂN BẢN OCR HIỆU CHỈNH | |
| |                                    |                                    | |
| | +--------------------------------+ | +--------------------------------+ | |
| | |                                | | | Chương 1: Giới hạn của dãy số  | | |
| | |   Chương 1: Giới hạn của dãy số| | |                                | | |
| | |                                | | | Định nghĩa 1.1: Cho dãy số     | | |
| | |   Định nghĩa 1.1: Cho dãy số   | | | (x_n) xác định trên tập số...  | | |
| | |   (x_n) xác định trên tập số...| | |                                | | |
| | |                                | | |                                | | |
| | +--------------------------------+ | +--------------------------------+ | |
| |                                    | [ 1,420 ký tự ]     [ Lưu trang ]  | |
| +------------------------------------+------------------------------------+ |
+-----------------------------------------------------------------------------+
```

### 4.1 Bố cục không gian làm việc màn hình đôi

* **Thanh tiêu đề (Header):** Hiển thị Tiêu đề tài liệu, Tác giả, Tên file gốc, Huy hiệu trạng thái OCR và liên kết **"Mở file gốc ↗"** để tải về xem trực tiếp tệp PDF scan ban đầu.
* **Khung thông tin tóm tắt:** Hiển thị Document ID, Định dạng nội dung (`application/pdf`, `image/jpeg`), Tổng số trang đã xử lý và Ngày khởi tạo.
* **Khung trái — Bản scan gốc (`Scan Pane`):**
  * Hiển thị ảnh chụp trực tiếp của trang scan hiện tại với độ phân giải nguyên gốc.
  * Hỗ trợ cuộn dọc để soi rõ từng chi tiết chữ in, bảng biểu, ký tự toán học hoặc hình minh họa.
* **Khung phải — Trình soạn thảo văn bản (`Processed Pane`):**
  * Khung nhập liệu văn bản nhiều dòng (`textarea`) chứa toàn bộ chữ nghĩa bóc tách được từ OCR.
  * Bộ đếm độ dài hiển thị số lượng ký tự thực tế của trang hiện hành (ví dụ: `1,450 ký tự`).

### 4.2 Điều hướng giữa các trang tài liệu

* Phía trên khung đối chiếu là thanh chọn trang (**Page Selector**):
  * Liệt kê danh sách tất cả các trang từ 1 đến hết: `[ 1 ]`, `[ 2 ]`, `[ 3 ]`...
  * Trang đang được chọn sẽ sáng màu nổi bật (`aria-current="page"`).
  * Nhấp vào số trang bất kỳ để tải ngay ảnh scan và văn bản tương ứng của trang đó vào hai khung đối chiếu.

### 4.3 Cơ chế cảnh báo dữ liệu chưa lưu (Data Loss Prevention)

Để ngăn ngừa việc biên tập viên gõ sửa văn bản nhưng vô tình bấm nhầm phím chuyển trang hoặc đóng tab trình duyệt làm mất công sức:

1. **Trạng thái sửa đổi:** Khi bạn thay đổi bất kỳ ký tự nào trong khung văn bản, hệ thống lập tức ghi nhận trạng thái có thay đổi chưa lưu (`hasUnsavedPageText`).
2. **Cảnh báo chuyển trang:** Nếu bạn nhấp chọn trang khác khi chưa lưu, trình duyệt sẽ bật hộp thoại xác nhận:
   > *"Trang hiện tại có nội dung chưa lưu. Bỏ thay đổi và chuyển trang?"*
   * Bấm `Hủy` (Cancel): Ở lại trang hiện tại để tiếp tục chỉnh sửa và bấm lưu.
   * Bấm `OK`: Bỏ qua các thay đổi chưa lưu và chuyển sang trang mới.
3. **Cảnh báo đóng tab:** Tự động kích hoạt cơ chế `beforeunload` của trình duyệt nếu bạn cố gắng tải lại hoặc đóng tab khi văn bản chưa được lưu.

### 4.4 Thao tác soát lỗi và lưu văn bản từng trang

1. Quan sát ảnh scan ở khung bên trái và đối chiếu từng đoạn văn ở khung bên phải.
2. Sửa các lỗi OCR thường gặp:
   * Chữ tiếng Việt bị dính dấu hoặc nhầm dấu (ví dụ: `được` thành `đuợc`, `nghĩa` thành `nghĩ a`).
   * Các dấu gạch nối ngắt từ ở cuối dòng (ví dụ: `nghiên-` `cứu` -> sửa thành `nghiên cứu`).
   * Ký tự số bị nhầm với chữ (ví dụ: số `0` nhầm với chữ `O`, số `1` nhầm với chữ `l` hoặc chữ `I`).
3. Bấm nút **"Lưu trang"** (`savePageText`).
4. Khi lưu thành công, nhãn trạng thái chuyển sang **"Đã lưu trang."** màu xanh lá.

---

## 5. Nhập và Quản lý Siêu dữ liệu Sách (Dublin Core Metadata & Tags)

Trước khi phát hành sách, tài liệu cần được khai báo siêu dữ liệu thư viện chuẩn hóa (theo bộ chuẩn Dublin Core đơn giản hóa) để phục vụ cho công tác phân loại, xếp giá và tìm kiếm:

### 5.1 Các trường siêu dữ liệu chuẩn thư viện

Tại phân vùng **"Metadata tài liệu"** (`metadata-editor`):

1. **Title (Tiêu đề sách):**
   * *Bắt buộc.* Tên đầy đủ, chính xác của giáo trình/tài liệu (ví dụ: *Giáo trình Giải tích 1 - Tái bản lần 3*).
2. **Author (Tác giả):**
   * *Bắt buộc.* Họ tên tác giả, chủ biên hoặc nhóm tác giả biên soạn (ví dụ: *PGS. TS. Nguyễn Đình Trí (Chủ biên), TS. Trần Văn Bình*).
3. **Vị trí kệ sách (Shelf Location):**
   * *Không bắt buộc nhưng khuyến nghị.* Ghi chú vị trí lưu trữ bản in vật lý tại Thư viện HCMUS (ví dụ: *Kệ K3-D, Phòng Đọc Tự Nhiên CSLT*), giúp bạn đọc dễ dàng tìm đến kệ sách giấy khi cần.
4. Bấm nút **"Lưu metadata"** để cập nhật các thông tin vào cơ sở dữ liệu.

### 5.2 Gán danh mục phân loại 2 cấp (Category Taxonomy)

* Trong mục chọn **Category**, nhấp vào danh sách thả xuống.
* Cây danh mục hiển thị phân cấp rõ ràng theo 2 tầng:
  * Nhóm lĩnh vực cấp 1 (ví dụ: `Khoa học Máy tính — cấp 1`, `Toán học — cấp 1`).
  * Chuyên ngành cụ thể cấp 2 lồng bên trong (ví dụ: `Kỹ thuật Phần mềm — cấp 2`, `Giải tích & Đại số — cấp 2`).
* Chọn đúng chuyên ngành phù hợp với cuốn sách để bạn đọc dễ dàng duyệt sách theo môn học.

### 5.3 Gán và quản lý thẻ linh hoạt (Tags)

Tại phân vùng **"Tags tài liệu"** (`tags-section`):
* **Xem danh sách thẻ hiện có:** Các thẻ được hiển thị dạng huy hiệu (ví dụ: `#giai-tich`, `#k23`, `#toan-cao-cap`).
* **Thêm tag mới:** Nhập tên thẻ vào ô văn bản (ví dụ: `tin-hoc-dai-cuong`) -> Bấm nút **"Thêm tag"**.
* **Xóa tag:** Nhấp vào dấu nhân (`×`) trên huy hiệu thẻ tương ứng để gỡ bỏ.

---

## 6. Đóng gói & Đề xuất Xuất bản Sách EPUB (Publishing Workflow)

### 6.1 Điều kiện tiên quyết để xuất bản

Để tiến trình đóng gói sách EPUB diễn ra trôi chảy và không phát sinh lỗi:
* [x] Toàn bộ các trang tài liệu đã được OCR thành công (`pages.length > 0`).
* [x] Biên tập viên đã rà soát và lưu văn bản chuẩn xác cho các trang quan trọng.
* [x] Đã nhập đầy đủ hai trường thông tin bắt buộc: **Title** và **Author**.

### 6.2 Kích hoạt tiến trình đóng gói Pandoc EPUB 3.0

1. Tại phân vùng **"Xuất bản EPUB"** (`publish-heading`):
2. Bấm nút **"Xuất bản EPUB"** (`handlePublish`).
3. Hệ thống sẽ chuyển sang trạng thái **"Đang xuất bản…"** và khởi chạy tiến trình Pandoc tại máy chủ:
   * Tập hợp nội dung văn bản của tất cả các trang theo đúng thứ tự logic.
   * Tạo tệp cấu trúc chuẩn EPUB 3.0 với bảng mục lục, tệp metadata `content.opf` và định dạng CSS đọc sách tối ưu.
   * Lưu tệp `.epub` hoàn chỉnh vào MinIO Storage.
   * Đồng bộ hóa và cập nhật chỉ mục tìm kiếm toàn văn (FTS Index) trong PostgreSQL.
4. Khi hoàn tất, giao diện hiển thị thông báo **"Tài liệu đã xuất bản."** và trạng thái tài liệu chuyển sang `published`.

### 6.3 Kiểm tra chất lượng sách hoàn thiện trên Reader

Sau khi xuất bản thành công:
1. Nhấp vào liên kết **"Mở Reader →"** xuất hiện trên màn hình.
2. Hệ thống sẽ mở cuốn sách vừa xuất bản trong giao diện trình đọc EPUB (`/reader/:documentId`).
3. Biên tập viên kiểm tra:
   * Khả năng cuộn trang và dàn chữ.
   * Bố cục các tiêu đề chương và đoạn văn.
   * Thử nghiệm tính năng tạo highlight và ghi chú để đảm bảo trải nghiệm độc giả hoàn hảo nhất.

---

## 7. Kinh nghiệm & Thực hành Tốt nhất cho Biên tập viên (Best Practices)

1. **Phân chia công việc theo cụm trang (Chunking):** Đối với các cuốn giáo trình dày (trên 200 trang), nên rà soát theo từng cụm 20 - 30 trang và bấm "Lưu trang" ngay sau khi hoàn thành mỗi trang để tránh mệt mỏi và rủi ro mất điện.
2. **Quy chuẩn tiêu đề chương:** Khi rà soát văn bản OCR, hãy thống nhất cách đặt tiêu đề đầu mục (ví dụ: viết hoa toàn bộ `CHƯƠNG 1: ...` hoặc thêm dấu `#` nếu dùng cú pháp markdown) để khi Pandoc xuất bản EPUB sẽ tự động sinh bảng mục lục sắc nét.
3. **Xử lý bảng biểu và hình vẽ:** Đối với các trang có biểu đồ phức tạp, nên để lại phần chú thích và tóm tắt nội dung bảng biểu trong khung văn bản để độc giả vẫn tra cứu FTS được nội dung của bảng.

---

## 8. Xử lý Sự cố Thường gặp (Troubleshooting)

### Q1: Tôi bấm "Xuất bản EPUB" nhưng hệ thống báo lỗi không thành công?
* **Nguyên nhân:** Thiếu trường `Title` hoặc `Author` trong phần Metadata, hoặc có trang tài liệu bị rỗng hoàn toàn nội dung văn bản.
* **Cách khắc phục:** Kiểm tra lại phần Metadata xem đã điền đủ Title, Author chưa; kiểm tra danh sách trang xem có trang nào bị lỗi OCR không.

### Q2: Tại sao tôi không thấy nút "Lưu trang" hay "Lưu metadata"?
* **Nguyên nhân:** Bạn đang mở tài liệu do một người dùng khác tải lên và bạn không có quyền sở hữu đối với tài liệu này (`owner_id` khác với tài khoản của bạn).
* **Cách khắc phục:** Chỉ chính chủ tải lên tài liệu hoặc Quản trị viên (`admin`) mới có quyền hiệu chỉnh. Liên hệ Quản trị viên nếu cần cấp quyền can thiệp đặc biệt.

### Q3: Sau khi sửa văn bản trang scan, kết quả tìm kiếm FTS có cập nhật ngay không?
* **Trả lời:** Có. Khi bạn nhấn "Lưu trang" và thực hiện "Xuất bản EPUB", hệ thống sẽ tự động cập nhật lại véc-tơ chỉ mục toàn văn trong PostgreSQL để độc giả tra cứu được ngay nội dung mới nhất.
