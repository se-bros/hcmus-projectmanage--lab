# PRODUCT BACKLOG & ACCEPTANCE CRITERIA

## Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS

**Trường Đại học Khoa học Tự nhiên, ĐHQG-HCM (HCMUS) — Thư viện & Phòng Công nghệ Thông tin**

Phiên bản 1.1 • Tháng 7/2026

---

## 1. Định nghĩa & Quy tắc Ưu tiên

Product Backlog này gom nhóm các yêu cầu nghiệp vụ dưới dạng User Story, ánh xạ trực tiếp từ **Quy trình Nghiệp vụ (Workflows)** và **Mô hình Tính năng (Feature Model)** của hệ thống HCMUS-LDMS. Các US được sắp xếp **theo trình tự thực tế người dùng** — bắt đầu từ bước đăng nhập.

Độ ưu tiên theo phương pháp **MoSCoW**:
- **Must-have (M):** Bắt buộc trong MVP (đăng nhập, số hóa Scan-to-EPUB, phân quyền, tìm kiếm).
- **Should-have (S):** Tăng trải nghiệm (Bookmark, highlight, bộ lọc nâng cao).
- **Could-have (C):** Có thể có nếu dư nguồn lực (trích dẫn APA/IEEE, thống kê).
- **Won't-have (W):** Hoãn sang giai đoạn sau (AI, RAG hỏi đáp).

---

## 2. Product Backlog — User Story & Acceptance Criteria

> **Cách đọc bảng:** Mỗi US có phần tiêu chí chấp nhận (✅ AC) liệt kê ngay bên dưới trong cùng một dòng gộp.

---

### EPIC A — Xác thực & Phân quyền

| Story ID | User Story | Workflow | Feature | Priority |
| :---: | :--- | :--- | :---: | :---: |
| **US00** | **Đăng nhập SSO**<br>*Là học sinh/thủ thư, tôi muốn đăng nhập bằng tài khoản HCMUS để hệ thống tự nhận diện vai trò của tôi.*<br><br>✅ **AC 1:** Trang `/login` hiển thị nút "Đăng nhập bằng tài khoản HCMUS"; khi nhấn, trình duyệt chuyển hướng đến Keycloak SSO của trường.<br>✅ **AC 2:** Sau khi xác thực thành công, Keycloak trả về JWT token hợp lệ chứa `role` (student / librarian / editor / admin).<br>✅ **AC 3:** Hệ thống map role từ token: `librarian`/`editor` → mở Dashboard Thủ thư; `student`/`faculty` → mở Cổng Học sinh (Reader).<br>✅ **AC 4:** Nếu token hết hạn (>60 phút), hệ thống tự refresh hoặc yêu cầu đăng nhập lại — người dùng không mất dữ liệu đang làm.<br>✅ **AC 5:** Nút "Đăng xuất" xóa session cả phía Keycloak lẫn cookie trình duyệt. | Xác thực (Tất cả) | Keycloak SSO (F3_1) | **Must** |
| **US00b** | **Kiểm soát quyền truy cập tài liệu**<br>*Là học sinh, tôi chỉ muốn thấy và đọc tài liệu mà tôi có quyền xem theo phân quyền.*<br><br>✅ **AC 1:** Tài liệu có access = `Restricted` không hiển thị trong kết quả tìm kiếm của học sinh thường.<br>✅ **AC 2:** Tài liệu `Internal` hiển thị với học sinh HCMUS đã đăng nhập, bị chặn với khách chưa đăng nhập.<br>✅ **AC 3:** Tài liệu `Public` hiển thị cho tất cả — kể cả người dùng chưa đăng nhập (Guest). | Xác thực (Tất cả) | RBAC (F3_1) | **Must** |

---

### EPIC B — Số hóa & Xuất bản (Luồng Thủ thư)

| Story ID | User Story | Workflow | Feature | Priority |
| :---: | :--- | :--- | :---: | :---: |
| **US01** | **Tải lên tệp scan gốc**<br>*Là thủ thư, tôi muốn tải lên tệp PDF hoặc ảnh scan để bắt đầu quy trình số hóa.*<br><br>✅ **AC 1:** Giao diện hỗ trợ kéo-thả (drag & drop) hoặc chọn file qua hộp thoại hệ thống.<br>✅ **AC 2:** Chấp nhận định dạng `.pdf`, `.jpg`, `.png`; từ chối các định dạng khác với thông báo rõ ràng.<br>✅ **AC 3:** Dung lượng tối đa **100 MB** mỗi lần tải; hiển thị lỗi nếu vượt quá.<br>✅ **AC 4:** Thanh tiến trình upload (0–100%) hiển thị theo thời gian thực.<br>✅ **AC 5:** Tệp được lưu vào MinIO theo đường dẫn: `bucket-library/raw_scans/YYYYMMDD/[ID]_[ten_file]`. | Số hóa & Xuất bản | Scan & Upload (F1_1) | **Must** |
| **US02** | **Tự động chạy OCR**<br>*Là thủ thư, tôi muốn hệ thống tự nhận dạng chữ viết từ ảnh scan để tôi không phải gõ lại văn bản.*<br><br>✅ **AC 1:** Tiến trình OCR Tesseract tự khởi động sau khi upload hoàn thành — không cần thao tác thêm.<br>✅ **AC 2:** Nhận dạng tiếng Việt có dấu chính xác ≥ **85% CAR** đối với bản scan in chuẩn (300 DPI).<br>✅ **AC 3:** Tiến trình chạy bất đồng bộ (background task); dashboard hiển thị trạng thái: "Đang xếp hàng" → "Đang nhận dạng" → "Hoàn thành" / "Lỗi".<br>✅ **AC 4:** Kết quả OCR từng trang được lưu riêng kèm số trang để thủ thư biên tập từng trang. | Số hóa & Xuất bản | Tích hợp OCR (F1_2) | **Must** |
| **US03** | **Biên tập & hiệu chỉnh văn bản OCR**<br>*Là thủ thư, tôi muốn xem ảnh gốc và văn bản OCR song song để sửa lỗi nhận dạng.*<br><br>✅ **AC 1:** Màn hình Split-screen: trái = ảnh trang PDF có zoom/xoay; phải = editor văn bản.<br>✅ **AC 2:** Auto-save nháp mỗi **30 giây**, hiển thị thông báo "Đã lưu tự động lúc HH:MM".<br>✅ **AC 3:** Editor hỗ trợ định dạng H1/H2/H3, in đậm, in nghiêng, danh sách có số thứ tự.<br>✅ **AC 4:** Nút "Gắn hình" cho phép cắt vùng ảnh từ scan để chèn vào văn bản (bảng biểu, hình vẽ).<br>✅ **AC 5:** Hiển thị chỉ số độ chính xác OCR (%) của trang hiện tại để thủ thư ưu tiên trang cần kiểm tra kỹ. | Số hóa & Xuất bản | Biên tập & Sinh EPUB (F1_3) | **Must** |
| **US04** | **Gán siêu dữ liệu (Metadata)**<br>*Là thủ thư, tôi muốn nhập tên sách, tác giả, danh mục, tag trước khi xuất bản.*<br><br>✅ **AC 1:** Form metadata có các trường bắt buộc: Tên tài liệu, Tác giả, Danh mục (Category); các trường tùy chọn: Nhà xuất bản, Năm, Tag, Mô tả.<br>✅ **AC 2:** Danh mục (Category) chọn từ cây thư mục có sẵn (do Admin cấu hình); không cho nhập tự do.<br>✅ **AC 3:** Tag nhập tự do, hỗ trợ gợi ý autocomplete các tag đã có trong hệ thống.<br>✅ **AC 4:** Trường Quyền truy cập (Access) là radio: Public / Internal / Restricted — mặc định Internal.<br>✅ **AC 5:** Validate: không cho phép bấm "Xuất bản" nếu Tên tài liệu hoặc Danh mục còn trống. | Số hóa & Xuất bản | Quản lý Metadata (F2_3) | **Must** |
| **US05** | **Đóng gói & Xuất bản EPUB**<br>*Là thủ thư, tôi muốn xuất bản tài liệu thành EPUB để học sinh có thể đọc online.*<br><br>✅ **AC 1:** Nút "Đóng gói & Xuất bản" gọi Pandoc biên dịch văn bản biên tập thành EPUB 3.0 hợp lệ.<br>✅ **AC 2:** File EPUB phải vượt kiểm tra `epubcheck` — không có lỗi nghiêm trọng (FATAL/ERROR).<br>✅ **AC 3:** File EPUB lưu vào MinIO: `bucket-library/epub/[ID].epub`; trạng thái tài liệu cập nhật thành `Published`.<br>✅ **AC 4:** Nội dung toàn văn tự động được index vào Elasticsearch ngay sau khi xuất bản.<br>✅ **AC 5:** Thủ thư nhận thông báo xuất bản thành công (hoặc thất bại kèm log lỗi) ngay trên màn hình. | Số hóa & Xuất bản | Biên tập & Sinh EPUB (F1_3) | **Must** |
| **US06** | **Quản lý danh mục & tag**<br>*Là admin, tôi muốn cấu hình cây danh mục và tag để tài liệu được phân loại có hệ thống.*<br><br>✅ **AC 1:** Admin tạo/sửa/xóa danh mục theo dạng cây phân cấp cha-con tối thiểu 2 cấp.<br>✅ **AC 2:** Ngăn tạo danh mục hoặc tag trùng tên (không phân biệt chữ hoa thường, bỏ qua khoảng trắng thừa).<br>✅ **AC 3:** Xóa danh mục chỉ thực hiện được khi không còn tài liệu nào đang thuộc danh mục đó (hiển thị cảnh báo nếu còn). | Quản trị hệ thống | Quản lý tài liệu (F2_1, F2_2) | **Must** |

---

### EPIC C — Tra cứu & Đọc sách (Luồng Học sinh)

| Story ID | User Story | Workflow | Feature | Priority |
| :---: | :--- | :--- | :---: | :---: |
| **US07** | **Tìm kiếm toàn văn**<br>*Là học sinh, tôi muốn tìm kiếm từ khóa trong nội dung sách để tìm tài liệu liên quan đến bài học.*<br><br>✅ **AC 1:** Kết quả trả về trong < **3 giây** kể cả khi tìm từ khóa trong nội dung sách (full-text search qua Elasticsearch).<br>✅ **AC 2:** Hỗ trợ Fuzzy Search — gõ "lap trinh" vẫn tìm ra "lập trình"; gõ thiếu dấu vẫn khớp.<br>✅ **AC 3:** Kết quả hiển thị snippet đoạn văn chứa từ khóa, từ khóa được bôi đậm (highlight).<br>✅ **AC 4:** Bộ lọc sidebar: Category, Năm xuất bản, Quyền truy cập (Public/Internal), Tác giả.<br>✅ **AC 5:** Kết quả được sắp xếp theo độ liên quan (Relevance Score); cho phép đổi sang sắp xếp theo Mới nhất / Cũ nhất. | Tra cứu & Đọc sách | Tìm kiếm toàn văn (F4_1) | **Must** |
| **US08** | **Đọc EPUB trực tuyến bảo mật**<br>*Là học sinh, tôi muốn đọc sách ngay trên trình duyệt mà không cần tải file về.*<br><br>✅ **AC 1:** Web Reader tải sách dạng XHTML chia trang — không tải toàn bộ file EPUB gốc về client.<br>✅ **AC 2:** URL tải nội dung sách là Signed URL MinIO với thời hạn **15 phút**; hết hạn tự gia hạn trong phiên đọc.<br>✅ **AC 3:** Với tài liệu `Internal`/`Restricted`: chặn chuột phải, `Ctrl+C`, `Ctrl+P`, không có nút download.<br>✅ **AC 4:** Giao diện responsive — đọc được trên máy tính, máy tính bảng, điện thoại.<br>✅ **AC 5:** Hiển thị số trang hiện tại / tổng số trang và thanh tiến trình đọc. | Tra cứu & Đọc sách | Trình đọc EPUB (F3_2) | **Must** |
| **US09** | **Tùy chỉnh giao diện đọc sách**<br>*Là học sinh, tôi muốn điều chỉnh cỡ chữ và nền màn hình để dễ đọc trong nhiều điều kiện ánh sáng.*<br><br>✅ **AC 1:** Tăng/giảm cỡ chữ từ **80% đến 200%** theo bước 10%.<br>✅ **AC 2:** Chọn font: Serif (Times-style), Sans-serif (Inter/Roboto), OpenDyslexic (hỗ trợ người khó đọc).<br>✅ **AC 3:** 3 chế độ nền: Light (nền trắng), Sepia (nền vàng nhạt bảo vệ mắt), Dark (nền đen).<br>✅ **AC 4:** Tùy chỉnh được lưu vào `localStorage` — giữ nguyên khi reload trang hoặc mở sách khác. | Tra cứu & Đọc sách | Trình đọc EPUB (F3_2) | **Should** |
| **US10** | **Đánh dấu trang (Bookmark)**<br>*Là học sinh, tôi muốn hệ thống ghi nhớ tôi đang đọc đến đâu để lần sau mở tiếp.*<br><br>✅ **AC 1:** Hệ thống tự động lưu vị trí đọc (EPUB CFI pointer) sau mỗi 30 giây và khi đóng tab.<br>✅ **AC 2:** Khi mở lại sách, hỏi "Tiếp tục từ trang X?" với nút Tiếp tục / Bắt đầu từ đầu.<br>✅ **AC 3:** Học sinh có thể tạo bookmark thủ công tại nhiều vị trí; quản lý danh sách bookmark trong panel bên trái.<br>✅ **AC 4:** Bookmark được lưu vào PostgreSQL — đồng bộ giữa các thiết bị khi đăng nhập cùng tài khoản. | Tra cứu & Đọc sách | Trình đọc EPUB (F3_2) | **Should** |
| **US11** | **Ghi chú & Highlight văn bản**<br>*Là học sinh, tôi muốn tô màu đoạn văn quan trọng và ghi chú bên lề để ôn tập sau.*<br><br>✅ **AC 1:** Bôi đen đoạn văn → thanh công cụ nổi hiện ra: chọn màu (Vàng / Hồng / Xanh) → lưu highlight.<br>✅ **AC 2:** Có thể gắn ghi chú văn bản vào highlight; icon ghi chú hiển thị nhỏ bên cạnh đoạn văn đó.<br>✅ **AC 3:** Toàn bộ highlight & ghi chú lưu vào PostgreSQL và hiển thị trong tab "Sổ ghi chép" trên cổng cá nhân.<br>✅ **AC 4:** Tổng hợp highlight của học sinh trong 1 cuốn sách có thể xuất ra file `.txt` định dạng ghi chú. | Tra cứu & Đọc sách | Trình đọc EPUB (F3_2) | **Should** |
| **US12** | **Trích dẫn tài liệu tự động**<br>*Là học sinh, tôi muốn copy trích dẫn chuẩn APA/IEEE của sách với 1 click để dùng trong báo cáo.*<br><br>✅ **AC 1:** Nút "Trích dẫn" trên trang sách sinh ra chuỗi trích dẫn chuẩn APA 7th và IEEE.<br>✅ **AC 2:** Nút "Copy" copy chuỗi vào clipboard ngay lập tức; hiển thị toast "Đã sao chép!".<br>✅ **AC 3:** Trích dẫn tự động điền đủ các trường có trong metadata: Tác giả, Năm, Tên sách, Nhà xuất bản, DOI (nếu có). | Tra cứu & Đọc sách | Quản lý Metadata (F2_3) | **Could** |

---

## 3. Tổng hợp Sprint Mapping

| Sprint | US | Mục tiêu | Priority |
| :---: | :--- | :--- | :---: |
| **Sprint 1** | US00, US00b, US01, US02 | Đăng nhập SSO + Upload + OCR pipeline cơ bản | Must |
| **Sprint 2** | US03, US04, US05 | Biên tập Split-screen + Metadata + Xuất bản EPUB | Must |
| **Sprint 3** | US06, US07, US08 | Quản lý Category + Tìm kiếm Elasticsearch + Đọc online | Must |
| **Sprint 4** | US09, US10, US11 | Reader UX: Theme/Font + Bookmark + Highlight | Should |
| **Sprint 5** | US12 | Trích dẫn tự động APA/IEEE | Could |

---

*Tài liệu được duy trì bởi Nhóm Phát triển HCMUS-LDMS. Cập nhật khi có thay đổi yêu cầu nghiệp vụ.*
