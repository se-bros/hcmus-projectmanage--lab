# PROJECT VISION & SCOPE (WHAT)

## Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS

**Trường Đại học Khoa học Tự nhiên, ĐHQG-HCM (HCMUS) — Thư viện & Phòng Công nghệ Thông tin**

Phiên bản 1.0 • Tháng 7/2026

## Mục lục

* [1. Glossary & Business Rules](#1-glossary--business-rules)
* [2. Feature Model & MVP](#2-feature-model--mvp)
* [3. Vision — Black-box Solution](#3-vision--black-box-solution)
* [4. Project Scope Statement](#4-project-scope-statement)
* [5. Mockup, Prototype & PoC](#5-mockup-prototype--poc)

---

## 1. Glossary & Business Rules

### Glossary

| Thuật ngữ | Định nghĩa |
| --- | --- |
| **HCMUS-LDMS** | Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS (Library Document Management & Digitization System). |
| **EPUB** | Định dạng sách điện tử mã nguồn mở (Electronic Publication), hỗ trợ hiển thị responsive và reflowable (tự co giãn dàn trang tương thích với mọi kích thước màn hình). |
| **OCR (Optical Character Recognition)** | Công nghệ nhận dạng ký tự quang học từ ảnh quét để chuyển đổi thành văn bản kỹ thuật số có thể tìm kiếm và chỉnh sửa. |
| **Signed URL** | Đường dẫn bảo mật có thời hạn, được sinh tự động bởi hệ thống để cho phép đọc tệp tin từ Object Storage (MinIO) mà không làm lộ URL gốc, ngăn chặn bot tải tệp hàng loạt. |
| **RBAC (Role-Based Access Control)** | Cơ chế quản lý phân quyền truy cập hệ thống dựa trên vai trò của người dùng (Admin, Editor, Reader). |
| **Dublin Core** | Chuẩn siêu dữ liệu (metadata) quốc tế gồm 15 trường cơ bản dùng để mô tả thông tin tài liệu học thuật. |

### Business Rules

| Quy tắc nghiệp vụ (Rule) | Nguồn tham chiếu (Source) | Mức độ biến động |
| --- | --- | --- |
| Siêu dữ liệu tài liệu phải tuân thủ chuẩn Dublin Core kết hợp danh mục và tag | Thông lệ nghiệp vụ thư viện số quốc tế và cấu trúc học liệu HCMUS | Thấp — chuẩn nghiệp vụ ổn định |
| Việc số hóa sách không cần xin phép/trả nhuận bút chỉ áp dụng cho tài liệu phục vụ giảng dạy, học tập nội bộ không thương mại | Khoản 1 Điều 25 Luật Sở hữu trí tuệ Việt Nam hiện hành | Trung bình — phụ thuộc vào thay đổi pháp lý về SHTT |
| Mỗi tài liệu được gán đúng 1 trong 3 mức truy cập: Công khai (Public), Nội bộ (Internal), hoặc Hạn chế (Restricted) | Quy chế hoạt động Thư viện HCMUS ban hành kèm Quyết định số 142/QĐ-KHTN | Trung bình |
| Thời hạn hạn chế truy cập tối đa đối với các tài liệu đặc thù là 36 tháng | Quy chế quản lý sở hữu trí tuệ của ĐHQG-HCM | Thấp |
| Quy trình hiệu chỉnh văn bản OCR bắt buộc phải được kiểm duyệt bởi thủ thư trước khi xuất bản thành EPUB | Quy trình quản lý chất lượng học liệu số của Thư viện trường | Thấp |

---

## 2. Feature Model & MVP

Nhóm tính năng của hệ thống được tổ chức dưới dạng **Feature Model** đầy đủ (And/Alternative/Or/Mandatory-Optional) để thể hiện các mối quan hệ ràng buộc:

![Sơ đồ mô hình tính năng (Feature Model)](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/hcmus-projectmanage--lab/docs/images/feature_model.svg)

Mỗi feature quan trọng được thiết kế theo mẫu *User → Business goal → Metric → Action*:

- **User** Thủ thư / Biên tập viên → **Business goal** số hóa sách giấy rách nát thành EPUB nhanh chóng → **Metric** thời gian đóng gói 1 cuốn sách, tỷ lệ lỗi chính tả → **Action** Quy trình Scan-to-EPUB (OCR Tesseract tự động kết hợp màn hình biên tập sửa lỗi chính tả và đóng gói Pandoc).
- **User** Độc giả (Sinh viên, Giảng viên) → **Business goal** đọc giáo trình thuận tiện trên di động từ xa → **Metric** số lượt đọc trên di động/tháng, thời gian tra cứu → **Action** Đọc sách qua trình Web EPUB Reader tích hợp (Epub.js) responsive và tìm kiếm toàn văn Elasticsearch.
- **User** Quản trị viên (Admin) → **Business goal** kiểm soát truy cập và bảo vệ bản quyền sách → **Metric** 0 trường hợp rò rỉ sách bản quyền → **Action** Quản lý vai trò người dùng (RBAC), cấu hình 3 mức độ tiếp cận và sinh Signed URL bảo mật.

**MVP (Minimum Viable Product):** Quy trình nộp & OCR cơ bản + Biên tập sửa lỗi trực tuyến + Xuất bản EPUB + Quản lý Category & Tag + Phân quyền người dùng (RBAC) + Tìm kiếm toàn văn. Triển khai thí điểm số hóa 500 cuốn giáo trình Công nghệ thông tin. Các tính năng AI/RAG **không** thuộc phạm vi MVP.

---

## 3. Vision — Black-box Solution

### Bối cảnh/Tổng quan

Hệ thống được mô tả như một "black-box" đối với độc giả và thủ thư: CÁI GÌ hệ thống thực hiện cho họ, không mô tả CÁCH xây dựng (xem chi tiết thiết kế hệ thống tại [06-architecture.md](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/hcmus-projectmanage--lab/docs/06-architecture.md)).

#### Tầm nhìn cho các vai trò tương tác (User Role Vision)
- **Tầm nhìn của Thủ thư (Librarian/Editor Vision):** Chuyển đổi từ người quản lý sách giấy vật lý thủ công thành nhà quản trị tài nguyên tri thức số. Hệ thống cung cấp một trợ lý số hóa khép kín: tự động OCR và biên dịch EPUB chỉ với vài thao tác kéo thả, giảm thiểu 85% sức lao động kiểm duyệt thủ công, giúp xuất bản sách số chất lượng cao dễ dàng.
- **Tầm nhìn của Học sinh / Độc giả (Student/Reader Vision):** Mang toàn bộ thư viện học liệu thu nhỏ vào thiết bị di động cá nhân. Sinh viên không còn rào cản về khoảng cách địa lý, giờ mở cửa hay số lượng bản in giới hạn; họ có thể tra cứu toàn văn tức thì và đọc sách EPUB responsive tương tác cao (ghi chú, tô sáng, bookmark, tự động trích dẫn) phục vụ đắc lực cho tự học và nghiên cứu khoa học.

![Sơ đồ ngữ cảnh hệ thống (System Context Diagram)](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/hcmus-projectmanage--lab/docs/images/context_diagram.svg)


### Current Situation (Trạng thái hiện tại)

#### Quy trình Hiện trạng (As-is Workflow)
Quy trình khai thác tài liệu giấy truyền thống tại thư viện HCMUS hiện nay hoàn toàn thủ công:

- **Bước 1 (Tiếp nhận & Lưu kho vật lý):** Thư viện tiếp nhận sách giấy từ nhà in/nhà tài trợ, thực hiện kiểm đếm số lượng thủ công, dán nhãn gáy sách (mã xếp giá DDC/UDC) và dán nhãn mã vạch (barcode). Cán bộ thư viện ghi chép vào sổ đăng ký cá biệt, đóng dấu thư viện lên trang bản quyền và xếp sách lên các kệ gỗ/sắt vật lý theo phân loại ngành tại kho sách cơ sở Nguyễn Văn Cừ (Quận 5).
- **Bước 2 (Hao mòn & Xuống cấp tự nhiên):** Do điều kiện khí hậu ẩm gió mùa tại TP.HCM và kho chứa không có hệ thống điều hòa chống ẩm chuyên dụng chạy 24/7, sách giấy chịu rủi ro ẩm mốc, mối mọt ăn mòn. Tần suất lật giở trang và mượn đọc liên tục của sinh viên qua nhiều năm khiến gáy sách bị bong tróc, trang sách bị rách nát, mờ chữ hoặc mất trang, gây hư hỏng nghiêm trọng tài liệu gốc.
- **Bước 3 (Độc giả di chuyển địa lý):** Độc giả (sinh viên, giảng viên từ các cơ sở khác như Linh Trung - Thủ Đức) khi cần mượn đọc buộc phải sắp xếp thời gian trong giờ hành chính, bắt các chuyến xe buýt dài hơn 15km để di chuyển trực tiếp đến cơ sở Quận 5, gây tốn kém thời gian và chi phí đi lại.
- **Bước 4 (Tra cứu thẻ mục lục & Điền phiếu mượn):** Độc giả đến phòng đọc, tự tra cứu mã sách trên cổng tra cứu OPAC cũ hoặc tìm kiếm trực tiếp trên tủ thẻ mục lục giấy. Độc giả điền tay đầy đủ thông tin sách (Tên sách, Tác giả, Mã đăng ký cá biệt) và thông tin cá nhân (MSSV, Họ tên) vào phiếu yêu cầu mượn bằng giấy rồi xếp hàng nộp cho thủ thư.
- **Bước 5 (Thủ thư tìm kiếm sách thủ công):** Thủ thư tiếp nhận phiếu mượn giấy, đối chiếu thông tin thủ công trên sổ đăng ký để xác định sách còn trong kho hay đã được người khác mượn. Sau đó, thủ thư phải trực tiếp di chuyển vào kho sách bám bụi, tìm kiếm giữa hàng chục kệ hàng dựa trên mã phân loại để rút cuốn sách cứng vật lý ra.
- **Bước 6 (Khai thác giới hạn & Chép tay thủ công):** Vì là giáo trình quý hiếm/độc bản, thư viện áp dụng quy chế nghiêm ngặt: chỉ cho phép đọc tại phòng đọc, nghiêm cấm mang về nhà và cấm photocopy để tránh hư hại gáy sách. Độc giả phải ngồi đọc tại chỗ và cắm cúi dùng bút ghi chép tay hoặc tự gõ lại từng dòng công thức, đoạn văn học thuật cần dùng vào laptop cá nhân.
- **Bước 7 (Trả sách & Hậu kiểm tình trạng):** Khi đọc xong hoặc hết giờ hành chính, độc giả mang sách trả lại bàn thủ thư. Thủ thư thực hiện hậu kiểm lật giở từng trang để kiểm tra xem sách có bị rách, viết vẽ bậy hay xé trang hay không. Nếu sách nguyên vẹn, thủ thư ký xác nhận hoàn thành vào sổ mượn trả và di chuyển vào kho xếp sách lại lên kệ gỗ.

#### Vấn đề của quy trình hiện tại (Core Pain Points)
- **Hao mòn & Hư hỏng vật lý:** Nhiều giáo trình cũ độc bản bị rách nát, mất trang, không thể phục hồi được, gây thất thoát tri thức.
- **Hạn chế địa lý & Thời gian:** Độc giả bắt buộc phải đến tận nơi để đọc sách, không hỗ trợ tra cứu học tập từ xa 24/7.
- **Tìm kiếm hạn chế:** Không thể tìm kiếm toàn văn (full-text) bên trong sách, độc giả chỉ tìm kiếm được theo tên sách, tác giả hoặc năm xuất bản ghi trên thẻ mục lục.
- **Trải nghiệm đọc số kém:** Việc quét sách sang PDF thông thường chỉ là ảnh chụp tĩnh, chữ hiển thị siêu nhỏ và không responsive trên thiết bị di động.
- **Quá tải không gian lưu trữ:** Kho chứa sách của thư viện đang chật kín, tốn nhiều chi phí quản lý diện tích.
- **Rủi ro pháp lý về bản quyền:** Thư viện thiếu một quy trình phân quyền truy cập và kiểm soát phân phối tài liệu số, dẫn đến rủi ro pháp lý khi tự ý chia sẻ tài liệu số hóa cho cộng đồng.

---

### Future Situation (Trạng thái tương lai)

#### Quy trình Tương lai (To-be Workflow)
Hệ thống HCMUS-LDMS tự động hóa luồng số hóa khép kín và phân phối sách điện tử EPUB responsive với các tương tác chi tiết như sau:

##### 1. Quy trình chi tiết của Thủ thư / Biên tập viên (Digitization & Publish Workflow)
- **Bước 1 (Chụp quét tài liệu - Scan/Capture):** Thủ thư sử dụng máy quét chuyên dụng (quét phẳng hoặc máy quét chữ V chống tháo gáy sách cổ/hiếm) quét toàn bộ sách giấy vật lý thành tệp PDF chất lượng cao (300 DPI, thẳng hàng, lọc vết lem mực).
- **Bước 2 (Tải lên & Khởi tạo - Upload & Metadata Init):** Thủ thư đăng nhập hệ thống bằng tài khoản vai trò Editor/Librarian, truy cập Dashboard Số hóa, tải lên tệp PDF gốc và khai báo siêu dữ liệu chuẩn học thuật Dublin Core (Tên tài liệu, Tác giả, Nhà xuất bản, Năm phát hành).
- **Bước 3 (Chạy OCR tự động - Auto OCR):** Hệ thống đưa tệp tin PDF vào hàng đợi xử lý bất đồng bộ, sử dụng công cụ OCR Tesseract nhận dạng ký tự tiếng Việt (`vie`) để trích xuất toàn bộ văn bản thô từ ảnh quét.
- **Bước 4 (Hiệu chỉnh văn bản & Đóng cấu trúc - Online Text Editing):** Biên tập viên sử dụng giao diện Split-screen (chia đôi màn hình):
  - *Bên trái:* Ảnh chụp PDF gốc của trang sách để đối chiếu trực quan.
  - *Bên phải:* Trình soạn thảo WYSIWYG/Markdown chứa văn bản thô sau OCR. Biên tập viên soát lỗi chính tả (sửa các lỗi ký tự nhận dạng sai), cấu hình phân cấp tiêu đề (H1, H2, H3) và chèn lại các hình ảnh minh họa tương ứng từ tệp gốc.
- **Bước 5 (Gắn phân loại & Phân quyền - Categorization & Access Control):** Biên tập viên chọn **Danh mục (Category)** theo sơ đồ hình cây môn học, gắn các nhãn **Thẻ (Tag)** liên quan, và thiết lập mức độ tiếp cận (Public, Internal, hoặc Restricted).
- **Bước 6 (Đóng gói & Lưu trữ - Compile EPUB & Save):** Thủ thư bấm nút "Đóng gói & Xuất bản". Hệ thống gọi tự động Pandoc/Calibre CLI biên dịch văn bản đã hiệu chỉnh thành tệp **EPUB 3.0 responsive**. Tệp EPUB hoàn chỉnh và tệp PDF gốc được lưu trữ an toàn trong MinIO Object Storage, đồng thời toàn bộ nội dung chữ được gửi sang Elasticsearch lập chỉ mục.

##### 2. Quy trình chi tiết của Học sinh / Độc giả (Search & Responsive Reading Workflow)
- **Bước 1 (Đăng nhập & Xác thực - Access & Login):** Sinh viên truy cập Web Portal bằng máy tính hoặc thiết bị di động, đăng nhập thông qua cổng định danh Keycloak SSO của trường bằng tài khoản sinh viên.
- **Bước 2 (Tìm kiếm & Bộ lọc - Search & Filter):**
  - *Tìm kiếm toàn văn (Elasticsearch):* Sinh viên nhập từ khóa để tìm kiếm sâu trong nội dung sách EPUB (tìm kiếm từ khóa, định lý, công thức) chứ không chỉ giới hạn ở tiêu đề hay tên tác giả. Kết quả phản hồi tức thì dưới 3 giây.
  - *Lọc thông minh:* Sử dụng bộ lọc danh mục ngành học (Category) và thẻ từ khóa (Tag) để thu hẹp danh sách kết quả.
- **Bước 3 (Sinh URL bảo mật - Secure File Load):** Khi sinh viên nhấn đọc sách, hệ thống đối chiếu phân quyền RBAC. Nếu được phép đọc, hệ thống sinh ra một **Signed URL** kết nối với MinIO có thời hạn hiệu lực 15 phút để tải tệp sách lên Web Reader.
- **Bước 4 (Đọc trực tuyến responsive - Web EPUB Reader):** Trình xem Epub.js hiển thị sách responsive thích ứng hoàn hảo mọi màn hình (mobile, tablet, PC) với các chức năng tương tác:
  - *Tùy chỉnh giao diện:* Tăng/giảm cỡ chữ, thay đổi font chữ, chọn chế độ nền đọc sách (Sáng, Vàng bảo vệ mắt, Tối - Dark mode).
  - *Xem mục lục:* Di chuyển nhanh giữa các chương mục của sách thông qua cây thư mục nội dung.
  - *Đánh dấu trang (Bookmark):* Tự động lưu lại vị trí trang sách đang đọc dở để tiếp tục đọc trong các phiên sau.
  - *Ghi chú & Tô sáng (Highlight & Note):* Sinh viên có thể bôi đen đoạn văn để tô màu highlight hoặc viết ghi chú trực tuyến, lưu trữ vào tài khoản cá nhân.
- **Bước 5 (Trích dẫn tự động - Auto Citation):** Sinh viên bấm nút "Trích dẫn" để hệ thống tự động xuất ra mẫu trích dẫn học thuật chuẩn APA/IEEE kèm link định danh sách phục vụ viết tiểu luận/nghiên cứu.


#### Sơ đồ Quy trình Hiện trạng (As-is) và Tương lai (To-be)
Sự chuyển đổi quy trình được trực quan hóa chi tiết trong sơ đồ dưới đây:

![Sơ đồ Quy trình Hiện trạng vs Tương lai](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/hcmus-projectmanage--lab/docs/images/as_is_to_be_workflow.svg)

#### Bảng Đối chiếu Vấn đề và Giải pháp Tính năng

| Vấn đề Hiện tại (Pain Point) | Giải pháp Số hóa (To-be Solution) | Tính năng Hệ thống (System Feature) | Giá trị mang lại (Value Delivered) |
| :--- | :--- | :--- | :--- |
| **Sách giấy hao mòn:** Giáo trình độc bản bị rách nát, mục ẩm theo thời gian. | Số hóa tài liệu gốc và bảo tồn vĩnh viễn dưới dạng tệp tin kỹ thuật số. | • Scan & Upload tệp PDF/Ảnh<br>• Lưu trữ đám mây MinIO | Triệt tiêu hoàn toàn sự hao mòn vật lý, bảo tồn nguyên vẹn tri thức học thuật lâu dài. |
| **PDF khó đọc trên di động:** Bản quét PDF chữ siêu nhỏ, không tự co giãn dòng. | Chuyển đổi văn bản sang định dạng responsive thích ứng màn hình di động. | • Dịch vụ OCR Tesseract tiếng Việt<br>• Module đóng gói EPUB bằng Pandoc | Độc giả đọc sách trên điện thoại/tablet mượt mà không cần phóng to hay kéo ngang màn hình. |
| **Hạn chế địa lý:** Phải đến tận thư viện Q5 để tra cứu và mượn giáo trình giấy. | Cho phép tra cứu và tiếp cận tài liệu trực tuyến mọi lúc mọi nơi. | • Cổng thông tin Web Portal responsive<br>• Xác thực Keycloak SSO trường | Độc giả dễ dàng tự học, tra cứu giáo trình từ xa 24/7 không giới hạn vị trí địa lý. |
| **Tìm kiếm hạn chế:** Chỉ tra được theo tên sách, tác giả trên thẻ mục lục. | Hỗ trợ tìm kiếm từ khóa bên trong nội dung sách. | • Tìm kiếm toàn văn bằng Elasticsearch<br>• Lọc tài liệu theo Category & Tag | Tiết kiệm 95% thời gian tra cứu, tìm kiếm sâu đến từng chương, đoạn văn nghiên cứu. |
| **Rủi ro vi phạm bản quyền:** Chia sẻ sách số dễ bị sao chép lậu và phát tán trái phép. | Thiết lập phân quyền truy cập và kiểm soát luồng đọc tệp tin nghiêm ngặt. | • Phân quyền vai trò RBAC<br>• Signed URL bảo mật (15 phút)<br>• Web EPUB Reader bảo mật | Ngăn chặn bot cào quét tải sách hàng loạt, bảo vệ sở hữu trí tuệ theo quy định pháp lý. |
| **Quá tải không gian kho:** Kệ sách vật lý chật kín, tốn diện tích quản lý. | Thay thế lưu trữ sách giấy bằng máy chủ số hóa dung lượng lớn. | • Máy chủ lưu trữ on-premise của trường | Thu hồi không gian phòng đọc thư viện Quận 5 làm khu vực tự học hiện đại cho sinh viên. |

---

## 4. Project Scope Statement

**Mô tả phạm vi sản phẩm:** Ứng dụng web HCMUS-LDMS quản lý và số hóa tài liệu thư viện, bao gồm luồng scan-to-EPUB (OCR, sửa lỗi, convert), phân loại tài liệu theo Category/Tag, quản trị phân quyền vai trò (RBAC), tìm kiếm toàn văn Elasticsearch và trình đọc Web EPUB Reader bảo mật.

**Deliverables (Các kết quả bàn giao):**
- Mã nguồn ứng dụng web HCMUS-LDMS (gồm mã nguồn Frontend React và Backend FastAPI).
- Kho giáo trình số hóa đợt đầu (~500 cuốn EPUB khoa CNTT).
- Tài liệu thiết kế hệ thống, cơ sở dữ liệu và API.
- Tài liệu hướng dẫn sử dụng cho thủ thư/biên tập viên và độc giả.
- 02 máy quét sách chuyên dụng được lắp đặt tại thư viện trường.

**Project Exclusions (Phạm vi loại trừ):**
- Bản quyền phần mềm chống đạo văn chuyên dụng (như Turnitin).
- Số hóa các tài liệu lưu trữ hành chính và hồ sơ nhân sự của trường.
- Quy trình di dời hoặc thanh lý sách giấy vật lý.
- Tính năng tìm kiếm AI/RAG thông minh (đưa vào Giai đoạn 3).

**Constraints (Các ràng buộc):**
- Tiến độ số hóa phụ thuộc vào tốc độ scan sách vật lý và hiệu suất sửa lỗi chính tả OCR của thủ thư.
- Tài nguyên máy chủ và băng thông mạng nội bộ của trường giới hạn dung lượng tải tệp đồng thời.
- Ràng buộc pháp lý về bản quyền: Chỉ được số hóa và chia sẻ nội bộ các tài liệu học tập của HCMUS tự soạn thảo.

**Yêu cầu phi chức năng (Non-Functional Requirements):**
- **Hiệu năng:** Thời gian phản hồi truy vấn tìm kiếm toàn văn dưới 3 giây đối với 95% số lượt tìm kiếm.
- **Độ tin cậy:** Hệ thống hoạt động ổn định với Uptime SLA ≥ 99.5%, chỉ số RPO < 24 giờ và RTO < 4 giờ.
- **Bảo mật:** Toàn bộ kết nối sử dụng HTTPS (TLS 1.3). Signed URL truy cập tệp tin EPUB hết hạn sau tối đa 15 phút.
- **Chất lượng OCR:** Tỷ lệ nhận dạng ký tự tiếng Việt chính xác (CAR) đạt tối thiểu 85% đối với các bản scan in chuẩn.

---

## 5. Mockup, Prototype & PoC

**Mockup & UI Prototype:**
- **Màn hình Biên tập lỗi OCR:** Giao diện chia đôi màn hình (Split-screen) hiển thị ảnh scan gốc ở bên trái và trình soạn thảo văn bản thô OCR ở bên phải giúp biên tập viên dễ dàng so sánh sửa lỗi chính tả.
- **Trình đọc Web EPUB Reader:** Mockup giao diện đọc sách responsive trên thiết bị di động, tích hợp bộ công cụ thay đổi font chữ, tăng giảm cỡ chữ, chuyển chế độ nền tối (Dark mode) bảo vệ mắt và nút Bookmark.

**Mục tiêu PoC (Proof of Concept):**
- **OCR Tesseract tiếng Việt:** Chạy thử nghiệm nhận dạng văn bản tiếng Việt trên 50 trang mẫu có chất lượng in khác nhau để đánh giá độ chính xác và cấu hình bộ tiền xử lý ảnh (bình chỉnh trang, tăng tương phản).
- **Pandoc / Calibre Conversion:** Thử nghiệm công cụ chuyển đổi tài liệu Markdown/HTML chứa hình ảnh và bảng biểu sang tệp EPUB để kiểm tra khả năng hiển thị định dạng chuẩn của file EPUB trên các thiết bị di động khác nhau.
