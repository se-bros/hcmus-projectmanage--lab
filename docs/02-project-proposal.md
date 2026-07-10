# ĐỀ XUẤT DỰ ÁN (PROJECT PROPOSAL)

## Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS

**Trường Đại học Khoa học Tự nhiên, ĐHQG-HCM (HCMUS) — Thư viện & Phòng Công nghệ Thông tin**

Phiên bản 1.0 • Tháng 7/2026

## Mục lục

* [1. Tóm tắt điều hành (Executive Summary)](#1-tóm-tắt-điều-hành-executive-summary)
* [2. Business case (Câu chuyện bối cảnh & Lý do đầu tư)](#2-business-case-câu-chuyện-bối-cảnh--lý-do-đầu-tư)
* [3. Giải pháp đề xuất](#3-giải-pháp-đề-xuất)
* [4. Phân tích Chi phí – Lợi ích (Cost-Benefit Analysis)](#4-phân-tích-chi-phí--lợi-ích-cost-benefit-analysis)
* [5. Rủi ro & Biện pháp giảm thiểu](#5-rủi-ro--biện-pháp-giảm-thiểu)
* [6. Lộ trình triển khai theo giai đoạn (Roadmap)](#6-lộ-trình-triển-khai-theo-giai-đoạn-roadmap)
* [7. Tiêu chí thành công (KPIs)](#7-tiêu-chí-thành-công-kpis)
* [8. Các bên liên quan & Phân vai (Stakeholders & RACI)](#8-các-bên-liên-quan--phân-vai-stakeholders--raci)
* [9. Các đầu việc chính (Work Breakdown Structure - WBS)](#9-các-đầu-việc-chính-work-breakdown-structure---wbs)
* [10. Ước tính thời gian (Timeline)](#10-ước-tính-thời-gian-timeline)
* [11. Ước tính chi phí (USD)](#11-ước-tính-chi-phí-usd)
* [12. Kết luận & Khuyến nghị](#12-kết-luận--khuyến-nghị)

---

## 1. Tóm tắt điều hành (Executive Summary)

Trường Đại học Khoa học Tự nhiên (HCMUS) hiện đang lưu giữ hàng chục ngàn tài liệu học thuật, giáo trình, sách tham khảo và bài báo khoa học dưới dạng bản cứng (giấy) tại thư viện. Phương thức lưu trữ truyền thống này đối mặt với ba thách thức lớn: quá tải diện tích kho bãi, nguy cơ rách hỏng và ẩm mốc tài liệu giấy do tần suất mượn đọc cao, và quy trình tra cứu mượn đọc thủ công tại chỗ gây khó khăn cho người dùng ở xa. Đặc biệt, các tệp PDF scan hiện tại chỉ là ảnh chụp tĩnh, cực kỳ khó đọc trên các thiết bị di động như điện thoại thông minh hay máy tính bảng do không có khả năng tự động co giãn theo màn hình (không responsive).

Tài liệu này đề xuất xây dựng **Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS (HCMUS-LDMS)**. Ứng dụng này sẽ tự động hóa luồng số hóa khép kín: quét tài liệu giấy -> nhận dạng ký tự quang học (OCR) -> biên tập chỉnh sửa văn bản lỗi -> đóng gói tự động sang định dạng sách điện tử **EPUB responsive**. Hệ thống hỗ trợ tổ chức tài liệu theo Danh mục (Categories) và Thẻ phân loại (Tags), phân quyền người dùng chặt chẽ (RBAC) và tích hợp tìm kiếm toàn văn hiệu năng cao.

**Các kết quả chính mong đợi:**
*   Số hóa và chuyển đổi sang EPUB cho toàn bộ giáo trình và sách tham khảo cốt lõi (~10.000+ cuốn) của trường.
*   Cung cấp bộ công cụ biên tập và sửa lỗi văn bản OCR trực quan dành cho thủ thư và biên tập viên.
*   Rút ngắn thời gian tra cứu sách từ trung bình 30 phút tìm kiếm thủ công xuống còn dưới 3 giây trên cổng thông tin số.
*   Hỗ trợ đọc trực tuyến responsive mượt mà trên mọi thiết bị thông qua trình đọc Web EPUB Reader tích hợp.
*   Bảo vệ bản quyền số thông qua phân quyền 3 mức (Công khai / Nội bộ trường / Hạn chế truy cập) gắn liền với hệ thống bảo mật Signed URL.

**Kế hoạch tài chính & Lộ trình:**
Dự án được triển khai theo mô hình lai (Hybrid): quản lý các mốc lớn (Giai đoạn 0 khảo sát đến Giai đoạn 3 nâng cao) kết hợp phát triển lặp Scrum 2 tuần cho phần kỹ thuật.
*   **Tổng chi phí đầu tư một lần (CapEx):** Ước tính từ **$45.000 đến $85.000** (trong đó mua sắm máy scan sách chuyên dụng tốc độ cao và chi phí nhân sự số hóa/biên dịch EPUB chiếm khoảng 48%).
*   **Chi phí vận hành định kỳ (OpEx):** Ước tính từ **$8.000 đến $16.000/năm**.

**Khuyến nghị:** Ban Giám hiệu phê duyệt ngân sách và chủ trương triển khai **Giai đoạn 0 (Khảo sát & Bản quyền)** để đánh giá hạ tầng hiện có, chốt quy định pháp lý về số hóa sách giáo dục và hoàn tất báo giá máy quét chuyên dụng. Tiếp đó, triển khai **MVP thí điểm** luồng Scan-to-EPUB trước khi mở rộng quy mô toàn trường.

---

## 2. Business case (Câu chuyện bối cảnh & Lý do đầu tư)

### 2.1. Câu chuyện từ thực tế vận hành

Để hiểu rõ sự cấp thiết của dự án, hãy nhìn vào trải nghiệm thực tế hàng ngày của sinh viên và cán bộ thư viện:

![Sơ đồ Hiện trạng (As-is) vs Tương lai (To-be)](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/hcmus-projectmanage--lab/docs/images/as_is_to_be_workflow.svg)

#### Câu chuyện thứ nhất: Cuộc hành trình gian nan của sinh viên Nguyễn Văn A
Nguyễn Văn A là sinh viên năm cuối Khoa Công nghệ Thông tin tại cơ sở Linh Trung (Thủ Đức). Để chuẩn bị ôn thi môn "Học máy nâng cao", A cần tham khảo cuốn giáo trình chuyên ngành độc bản do thư viện giữ.
1.  **Di chuyển:** A phải bắt xe buýt dài hơn 15km trong thời tiết nắng nóng từ Linh Trung về cơ sở Nguyễn Văn Cừ (Quận 5), nơi đặt kho giáo trình giấy của trường.
2.  **Tra cứu:** Đến nơi trong giờ hành chính, A phải tra cứu mã số trên cổng thông tin cũ kỹ, rồi điền phiếu yêu cầu mượn bằng giấy.
3.  **Chờ đợi:** Thủ thư phải di chuyển vào sâu trong kho sách bám bụi để tìm cuốn giáo trình vật lý.
4.  **Hạn chế tiếp cận:** Vì là cuốn sách hiếm và bản duy nhất, A chỉ được phép đọc tại phòng đọc, không được mượn về nhà, không được photocopy để tránh hư hại gáy sách. A phải ngồi cắm cúi chép tay các đoạn công thức và thuật toán quan trọng suốt 3 tiếng.
5.  **Mất mát vật lý:** Một tuần sau, khi A cần xem lại, cuốn giáo trình đó đã bị rách vài trang cốt lõi do ẩm mốc và tần suất lật giở quá nhiều của các sinh viên khác. Nguồn tri thức học thuật quý giá đó đã bị hao mòn vật lý và không thể phục hồi.

#### Câu chuyện thứ hai: Áp lực bảo quản của cô thủ thư Mai
Mỗi học kỳ mới bắt đầu, cô Mai – cán bộ thư viện lâu năm – lại đối mặt với một cơn ác mộng mang tên "sách giấy hư hỏng". 
1.  **Quá tải không gian & Xuống cấp:** Diện tích kho lưu trữ có hạn nhưng số lượng sách nhập mới tăng liên tục. Nhiều cuốn sách chuyên ngành từ những năm 2000 bị ố vàng, mục nát, rách trang do thời tiết ẩm mốc và tần suất mượn đọc cao.
2.  **Hạn chế của việc số hóa cũ:** Thư viện từng thử quét sách sang file PDF, nhưng file PDF scan thực chất chỉ là các bức ảnh chụp tĩnh nặng nề. Khi sinh viên tải về đọc trên điện thoại, các chữ hiển thị siêu nhỏ, bắt buộc phải phóng to và kéo qua kéo lại liên tục để đọc hết một dòng, tạo ra trải nghiệm cực kỳ ức chế.
3.  **Rủi ro bản quyền:** Cô liên tục phải từ chối yêu cầu sao chép tài liệu của sinh viên vì không có cơ chế phân quyền chia sẻ rõ ràng, sợ vi phạm pháp lý về bản quyền đối với sách chưa có thỏa thuận cụ thể.

### 2.2. Vấn đề được giải quyết như thế nào?

Hệ thống **HCMUS-LDMS** được đề xuất nhằm giải quyết triệt để các nút thắt trên thông qua một chu trình số hóa khép kín:

*   **Quy trình Scan-to-EPUB khép kín:** Thay vì lưu trữ bản cứng dễ hỏng hoặc bản scan PDF tĩnh khó đọc, hệ thống hỗ trợ quét sách giấy, chạy OCR tự động trích xuất văn bản thô, cung cấp màn hình biên tập lỗi chính tả cho thủ thư, và tự động đóng gói sang định dạng **EPUB responsive**. Người đọc có thể dễ dàng co giãn font chữ, đổi màu nền và đọc sách mượt mà trên mọi kích thước màn hình di động.
*   **Quản lý khoa học qua Category & Tag:** Hỗ trợ phân loại tài liệu theo cấu trúc hình cây của Danh mục (Categories) ứng với từng Khoa/Môn học, và gắn thẻ phân loại (Tags) linh hoạt theo chủ đề, giúp độc giả tìm kiếm chéo cực kỳ dễ dàng.
*   **Bảo vệ bản quyền qua phân quyền chặt chẽ:** Tích hợp cơ chế phân quyền người dùng (Role-Based Access Control) cho cả 3 vai trò (Admin, Editor/Librarian, Reader) và quy định 3 mức độ tiếp cận (Public / Internal / Restricted), sử dụng Signed URL có thời hạn để chống tải lậu hàng loạt.
*   **Dân chủ hóa truy cập & Bảo tồn vĩnh viễn:** Độc giả có thể truy cập hệ thống 24/7 từ bất kỳ đâu, sử dụng Elasticsearch để tìm kiếm toàn văn đến từng từ khóa bên trong nội dung sách EPUB. Toàn bộ sách giấy được số hóa và lưu trữ an toàn trên máy chủ của trường, giảm tải áp lực cho kho sách vật lý.

---

## 3. Giải pháp đề xuất

### 3.1. Mô tả tổng quan

Giải pháp đề xuất là xây dựng ứng dụng web **HCMUS-LDMS** chuyên dụng cho việc quản lý và số hóa tài liệu thư viện, đóng vai trò là kho sách số tập trung của trường. Hệ thống quản lý toàn bộ vòng đời của tài liệu từ khâu thủ thư scan tải lên, qua khâu chạy OCR và biên tập lỗi chính tả, đóng gói thành EPUB, phân loại danh mục/tag, đến khâu phục vụ đọc trực tuyến responsive và tìm kiếm toàn văn của độc giả.

### 3.2. Năng lực cốt lõi (Core Capabilities)

*   **Quy trình số hóa Scan-to-EPUB:** 
    *   Hỗ trợ tải lên file PDF/Ảnh quét từ máy scan.
    *   Tích hợp dịch vụ OCR Tesseract tự động nhận dạng ký tự tiếng Việt.
    *   Giao diện biên tập văn bản OCR trực quan (Markdown/WYSIWYG) giúp thủ thư hiệu chỉnh lỗi chính tả và cấu trúc Heading.
    *   Tự động đóng gói và xuất bản tệp EPUB thông qua công cụ Pandoc / Calibre CLI.
*   **Quản lý phân loại đa chiều:**
    *   *Danh mục (Category):* Tổ chức tài liệu theo cây thư mục nhiều cấp (ví dụ: Công nghệ thông tin -> Khoa học máy tính -> Trí tuệ nhân tạo).
    *   *Thẻ (Tag):* Gắn nhãn tự do (ví dụ: #MachineLearning, #Python, #GiaoTrinh) để gom nhóm tài liệu theo chủ đề chéo.
*   **Quản lý Người dùng & Phân quyền (RBAC):**
    *   *Admin (Quản trị viên):* Quản lý cấu hình hệ thống, quản trị tài khoản người dùng và thiết lập phân quyền vai trò.
    *   *Editor / Librarian (Biên tập viên/Thủ thư):* Thực hiện tải tệp scan, chạy OCR, chỉnh sửa biên tập, đóng gói EPUB, quản lý danh mục và tag.
    *   *Reader (Độc giả - Sinh viên, Giảng viên, Khách):* Xem trang chi tiết siêu dữ liệu (metadata), tìm kiếm, đọc trực tuyến EPUB qua trình đọc tích hợp tùy thuộc vào mức phân quyền tài liệu.
*   **Phân mức truy cập tài liệu:**
    *   *Public (Công khai):* Ai cũng có thể đọc trực tuyến.
    *   *Internal (Nội bộ):* Độc giả phải đăng nhập tài khoản SSO trường HCMUS mới được phép đọc.
    *   *Restricted (Hạn chế):* Chỉ cho phép một số nhóm người dùng cụ thể (ví dụ: sinh viên đăng ký môn học đó) hoặc khóa truy cập có thời hạn.
*   **Tìm kiếm toàn văn Elasticsearch:** Chỉ mục hóa (index) toàn văn nội dung sách EPUB, hỗ trợ tìm kiếm nhanh theo từ khóa trong nội dung sách, tên sách, tác giả, kết hợp bộ lọc danh mục và tag.
*   **Trình đọc Web EPUB Reader bảo mật:** Tích hợp Epub.js để hiển thị sách EPUB responsive trực tiếp trên trình duyệt web của mobile/tablet/PC. Không cho phép tải file EPUB trực tiếp đối với tài liệu nội bộ/hạn chế, sử dụng Signed URL có thời hạn 15 phút để bảo mật tệp tin trên MinIO.

### 3.3. Định hướng kiến trúc (Architectural Direction)

Hệ thống được phát triển theo mô hình ứng dụng web tự xây dựng (custom-built) dựa trên kiến trúc Modular Monolith để tối ưu hóa chi phí vận hành và tính linh hoạt:

![Mô hình kiến trúc hệ thống (System Architecture)](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/hcmus-projectmanage--lab/docs/images/system_architecture.svg)

*   **Frontend:** React 18 (TypeScript), Tailwind CSS và thư viện **Epub.js** phục vụ hiển thị trình đọc sách responsive.
*   **Backend API:** **FastAPI (Python 3.11)** - lựa chọn tối ưu để xử lý bất đồng bộ các tác vụ xử lý file nặng (OCR bằng Tesseract, chuyển đổi định dạng bằng Pandoc/Calibre CLI).
*   **Cơ sở dữ liệu:** PostgreSQL 16 quản lý dữ liệu quan hệ (người dùng, phân quyền, danh mục, tag, metadata).
*   **Lưu trữ tệp:** **MinIO (On-premise Object Storage)** tương thích S3 để lưu trữ file scan gốc và file EPUB xuất bản.
*   **Tìm kiếm:** Elasticsearch 8.x chạy độc lập phục vụ lập chỉ mục và truy vấn toàn văn.
*   **Xác thực tập trung:** Keycloak 24.x hỗ trợ SSO, kết nối với LDAP/Active Directory sẵn có của trường.

### 3.4. Phạm vi loại trừ (Out of scope)

*   **Hệ thống chống đạo văn chuyên dụng (như Turnitin):** Không thuộc phạm vi phát triển, chỉ cung cấp API mở để tích hợp sau.
*   **Số hóa các tài liệu hành chính:** Dự án chỉ tập trung vào tài liệu học tập, giáo trình, sách tham khảo và bài báo khoa học phục vụ đào tạo.
*   **Thuê ngoài lập trình toàn bộ:** Dự án sẽ tận dụng năng lực kỹ thuật của Phòng CNTT trường kết hợp cố vấn nghiệp vụ thư viện để tự chủ công nghệ.

---

## 4. Phân tích Chi phí – Lợi ích (Cost-Benefit Analysis)

### 4.1. Ước tính chi phí (Investment)

Dự án phân tách rõ hai nguồn ngân sách: Chi phí đầu tư một lần (CapEx) phục vụ xây dựng phần mềm và mua sắm thiết bị scan; Chi phí vận hành định kỳ (OpEx) phục vụ hạ tầng server và license OCR hàng năm.

![Phân rã Ngân sách Đầu tư một lần (CapEx)](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/hcmus-projectmanage--lab/docs/images/capex_breakdown.svg)

> [!NOTE]
> Ngân sách chi tiết được phân rã cụ thể tại [Mục 11. Ước tính chi phí (USD)](#11-ước-tính-chi-phí-usd) của tài liệu này.

### 4.2. Lợi ích định lượng & định tính

| Đối tượng thụ hưởng | Lợi ích định lượng | Lợi ích định tính |
| :--- | :--- | :--- |
| **Thư viện HCMUS** | • Thu hồi khoảng **50-70%** không gian kệ sách vật lý khi chuyển đổi sách cũ sang kho số.<br>• Giảm **85%** thời gian thủ thư xử lý yêu cầu tìm kiếm và phục vụ mượn sách giấy.<br>• Quy trình số hóa tự động hóa **100%** khâu đóng gói EPUB. | • Bảo tồn vĩnh viễn nguồn học liệu quý giá của trường, tránh rách hỏng vật lý.<br>• Hiện đại hóa hình ảnh thư viện trường học số. |
| **Độc giả (Sinh viên, GV)** | • Đọc sách responsive **100%** trên smartphone/tablet mà không bị mỏi mắt.<br>• Truy cập **24/7** từ xa qua Internet.<br>• Tìm kiếm toàn văn nhanh chóng dưới **3 giây**. | • Tăng tính chủ động trong học tập, nghiên cứu trực tuyến.<br>• Dễ dàng tra cứu tài liệu phục vụ ôn thi, làm đề tài tốt nghiệp từ xa. |
| **Nhà trường / BGH** | • Tối ưu hóa hiệu quả sử dụng hạ tầng CNTT sẵn có của trường.<br>• Đạt chỉ tiêu chuyển đổi số giáo dục cấp ĐHQG-HCM. | • Nâng cao năng lực tự chủ công nghệ.<br>• Tạo kho tri thức số dùng chung hỗ trợ kiểm định chất lượng đào tạo. |

### 4.3. Đánh giá rủi ro và điểm lưu ý trong kỳ vọng

*   **Giới hạn của số hóa:** Số hóa sách không đồng nghĩa với việc tiêu hủy sách giấy. Các cuốn sách giấy gốc vẫn phải lưu trữ tại kho lưu trữ dự phòng của trường theo quy định. Lợi ích thực tế là giải phóng diện tích phòng đọc chính tại cơ sở Nguyễn Văn Cừ để làm không gian tự học hiện đại cho sinh viên.
*   **Bảo vệ bản quyền số:** Việc đọc trực tuyến được bảo mật tối đa qua PDF/EPUB Viewer (Signed URL, chặn download, chặn chuột phải). Tuy nhiên, nhà trường cần ban hành quy chế sử dụng học liệu số để sinh viên tự ý thức việc không chia sẻ tài khoản đăng nhập ra bên ngoài.

---

## 5. Rủi ro & Biện pháp giảm thiểu

| Nhóm rủi ro | Chi tiết rủi ro | Mức độ | Biện pháp giảm thiểu | Risk Owner |
| :--- | :--- | :--- | :--- | :--- |
| **Bản quyền sách giấy** | Số hóa và công bố sách dịch, sách giáo trình nước ngoài hoặc sách chưa có sự đồng ý của nhà xuất bản gây rủi ro pháp lý. | **Cao** | • Phân loại chặt chẽ tài liệu: Chỉ số hóa sách nội bộ trường, giáo trình do giảng viên trường tự biên soạn.<br>• Áp dụng mức phân quyền Restricted/Internal nghiêm ngặt, giới hạn phạm vi đọc đối với các sách nhạy cảm bản quyền. | **Ban Giám đốc Thư viện** |
| **Chất lượng OCR tiếng Việt** | Sách cũ, mờ quét ra chữ bị lỗi font nhiều, khiến quá trình hiệu chỉnh thủ công của thủ thư bị quá tải. | **Trung bình** | • Thiết lập quy trình tiền xử lý ảnh scan (lọc nhiễu, tăng độ tương phản) trước khi chạy OCR.<br>• MVP chỉ tập trung số hóa các tài liệu in sạch từ năm 2010 trở đi; tài liệu cũ hơn sẽ số hóa cuốn chiếu chậm hơn. | **Phòng Công nghệ Thông tin** |
| **Quá tải biên tập viên** | Số lượng sách cần biên tập thủ công sau OCR lớn gây chậm tiến độ xuất bản EPUB. | **Trung bình** | • Tuyển dụng đội ngũ cộng tác viên (sinh viên bán thời gian) hỗ trợ thủ thư biên tập lỗi chính tả OCR trực tuyến.<br>• Thiết lập hệ thống xếp hạng và khen thưởng cho sinh viên tham gia biên tập học liệu số. | **Ban Giám đốc Thư viện** |
| **Rò rỉ tài liệu số** | Sinh viên sử dụng các công cụ quay màn hình hoặc bot cào quét để lấy file EPUB/văn bản sách. | **Trung bình** | • Sử dụng Signed URL giới hạn 15 phút, chia nhỏ tệp EPUB thành nhiều chương tải bất đồng bộ.<br>• Giới hạn số trang đọc tối đa trong một phiên đối với tài khoản sinh viên (nếu cần). | **Phòng Công nghệ Thông tin** |

---

## 6. Lộ trình triển khai theo giai đoạn (Roadmap)

Dự án được đề xuất triển khai theo 4 giai đoạn rõ ràng với các điểm Gating (Go/No-go) tại cuối mỗi giai đoạn:

![Sơ đồ lộ trình triển khai theo giai đoạn](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/hcmus-projectmanage--lab/docs/images/project_roadmap.svg)

*   **Giai đoạn 0 — Khảo sát & Bản quyền (Tháng 1–2):**
    *   *Trọng tâm:* Kiểm kê danh mục giáo trình tự soạn của trường, thẩm định pháp lý bản quyền số hóa, mua sắm máy quét chuyên dụng tốc độ cao.
    *   *Kết quả:* Danh mục sách số hóa được phê duyệt, quy chế vận hành tài liệu số được ban hành, chốt thiết kế mockup giao diện.
*   **Giai đoạn 1 — Xây dựng MVP & Thí điểm (Tháng 3–5):**
    *   *Trọng tâm:* Thiết lập hạ tầng PostgreSQL/MinIO, phát triển ứng dụng FastAPI/React, tích hợp luồng Scan-to-EPUB (OCR Tesseract & Pandoc), thử nghiệm số hóa 500 cuốn giáo trình CNTT.
    *   *Kết quả:* Hệ thống HCMUS-LDMS chạy thử nghiệm, nghiệm thu UAT với ban biên tập thư viện và nhóm sinh viên CNTT mẫu.
*   **Giai đoạn 2 — Mở rộng toàn trường (Tháng 6–9):**
    *   *Trọng tâm:* Tích hợp Keycloak SSO trường, tối ưu hóa thuật toán OCR, mở rộng số hóa giáo trình tất cả các khoa còn lại (~10.000 cuốn), chính thức đưa hệ thống vào phục vụ giảng dạy và học tập.
    *   *Kết quả:* Go-live chính thức toàn trường, tắt bỏ quy trình mượn bản cứng đối với các sách đã số hóa xong.
*   **Giai đoạn 3 — Nâng cao (Giai đoạn sau, tùy chọn):**
    *   *Trọng tâm:* Nghiên cứu tích hợp API công cụ chống đạo văn, triển khai PoC tìm kiếm ngữ nghĩa AI/RAG hỗ trợ truy vấn thông minh.

---

## 7. Tiêu chí thành công (KPIs)

1.  **Tỷ lệ học liệu số:** Số hóa và chuyển đổi sang EPUB đạt tối thiểu **90%** số lượng giáo trình cốt lõi của tất cả các ngành đào tạo trong vòng 12 tháng từ khi go-live.
2.  **Độ chính xác OCR:** Tỷ lệ nhận dạng ký tự tiếng Việt chính xác (CAR) sau khi qua bộ tiền xử lý ảnh đạt tối thiểu **85%** đối với tài liệu in tiêu chuẩn.
3.  **Tốc độ tra cứu:** Thời gian phản hồi cho truy vấn tìm kiếm toàn văn nội dung sách dưới **3 giây** dưới tải trọng 500 người dùng đồng thời.
4.  **Tần suất sử dụng:** Đạt trung bình tối thiểu **10.000 lượt đọc sách/tháng** sau 6 tháng vận hành chính thức.
5.  **Mức độ hài lòng:** Đạt tối thiểu **85%** độc giả đánh giá hài lòng về trải nghiệm đọc sách EPUB responsive trên thiết bị di động.
6.  **An sau bảo mật:** **0** xảy ra sự cố rò rỉ toàn bộ file EPUB gốc từ hệ thống lưu trữ MinIO ra ngoài Internet.

---

## 8. Các bên liên quan & Phân vai (Stakeholders & RACI)

### 8.1. Stakeholder Register

*   **Sponsor (Nhà tài trợ):** Ban Giám hiệu HCMUS. Vai trò: Bảo trợ dự án, phê duyệt ngân sách máy quét và hạ tầng.
*   **Client (Chủ trì nghiệp vụ):** Ban Giám Đốc Thư viện HCMUS. Vai trò: Quản lý quy trình biên tập, số hóa sách, phân loại danh mục/tag, tổ chức đội ngũ thủ thư/sinh viên hiệu chỉnh OCR.
*   **Client (Chủ trì kỹ thuật):** Phòng Công nghệ Thông tin. Vai trò: Thiết kế kiến trúc, phát triển phần mềm custom (React, FastAPI), quản trị Elasticsearch/MinIO/Keycloak, bảo mật hệ thống.
*   **User (Người dùng cuối):** Độc giả (Sinh viên, Giảng viên), Thủ thư (Cán bộ số hóa và biên tập viên).
*   **Cố vấn Pháp lý:** Bộ phận Pháp chế & Lưu trữ. Vai trò: Thẩm định quy định pháp lý về giới hạn quyền tác giả cho mục đích giảng dạy học tập.

### 8.2. Ma trận Trách nhiệm (RACI Matrix)

*   **R** (Responsible): Người thực hiện công việc.
*   **A** (Accountable): Người chịu trách nhiệm cuối cùng.
*   **C** (Consulted): Người được tham vấn ý kiến.
*   **I** (Informed): Người được nhận thông tin.

| Gói công việc (WBS) | Thư viện | Phòng CNTT | Phòng Đào tạo | Pháp chế & Lưu trữ | Ban Giám hiệu | Độc giả |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **WP1 — Khảo sát & Bản quyền** | **A** / R | R | C | C | I | - |
| **WP2 — Thiết lập Backend & DB** | C | **A** / R | - | - | I | - |
| **WP3 — Phát triển UI & OCR/EPUB** | C | **A** / R | - | - | I | C |
| **WP4 — Số hóa tài liệu** | **A** / R | C | - | C | I | - |
| **WP5 — Kiểm thử & UAT** | R | **A** / R | - | - | I | C |
| **WP6 — Triển khai & Vận hành** | **A** / R | R | C | - | I | I |

---

## 9. Các đầu việc chính (Work Breakdown Structure - WBS)

*   **WP1 — Khảo sát & Bản quyền:**
    *   Kiểm kê và phân loại kho sách giấy thư viện để chọn lọc danh mục sách tự soạn đủ điều kiện số hóa.
    *   Phối hợp bộ phận Pháp chế xây dựng quy chế số hóa nội bộ tuân thủ Luật SHTT.
    *   Khảo sát thói quen đọc sách trên di động của 200+ sinh viên.
    *   Thiết kế mockup chi tiết cho màn hình Web Reader và màn hình Biên tập lỗi OCR.
*   **WP2 — Thiết lập Backend & DB:**
    *   Cấu hình hạ tầng máy chủ, cài đặt CSDL PostgreSQL 16 và MinIO Object Storage.
    *   Cài đặt và cấu hình Keycloak 24.x phục vụ xác thực người dùng tập trung.
    *   Phát triển hệ thống API Backend (FastAPI) quản lý tài khoản, danh mục, tag và quản trị phân quyền (RBAC).
    *   Thiết lập cơ chế backup tự động cơ sở dữ liệu và file lưu trữ.
*   **WP3 — Phát triển UI & OCR/EPUB:**
    *   Phát triển giao diện Web Portal bằng React 18 & Tailwind CSS.
    *   Tích hợp thư viện Epub.js xây dựng trình đọc Web EPUB Reader (chức năng co giãn chữ, đổi nền, đánh dấu trang).
    *   Xây dựng giao diện Biên tập trực quan so sánh song song ảnh scan gốc và văn bản OCR để thủ thư sửa lỗi.
    *   Tích hợp dịch vụ Tesseract OCR tiếng Việt và công cụ đóng gói Pandoc/Calibre CLI trên Backend.
    *   Cấu hình Elasticsearch 8.x lập chỉ mục toàn văn sách EPUB.
*   **WP4 — Số hóa tài liệu (Chạy song song):**
    *   Thực hiện scan sách giấy sang PDF/Ảnh bằng máy quét chuyên dụng.
    *   Tải tệp lên hệ thống, chạy OCR tự động trích xuất văn bản thô.
    *   Thủ thư và cộng tác viên sinh viên thực hiện biên tập sửa lỗi chính tả trực tuyến.
    *   Đóng gói thành tệp EPUB, phân loại danh mục, gắn thẻ (tag) và xuất bản lên hệ thống.
*   **WP5 — Kiểm thử & Nghiệm thu:**
    *   Kiểm thử chức năng (luồng số hóa, biên tập, đóng gói, đọc sách, phân quyền).
    *   Kiểm thử hiệu năng tìm kiếm toàn văn dưới tải trọng 500 người dùng đồng thời.
    *   Tổ chức đợt UAT đánh giá trải nghiệm đọc sách EPUB trên các thiết bị di động thật.
*   **WP6 — Triển khai & Vận hành:**
    *   Tổ chức tập huấn sử dụng cho thủ thư và các biên tập viên.
    *   Biên soạn và công bố tài liệu hướng dẫn đọc sách số cho sinh viên/giảng viên.
    *   Truyền thông ra mắt cổng HCMUS-LDMS.

---

## 10. Ước tính thời gian (Timeline)

### 10.1. So sánh 2 phương án triển khai

*   **Phương án A (Số hóa toàn bộ trước khi release):** Số hóa và biên tập EPUB xong toàn bộ ~10.000 cuốn sách rồi mới mở cổng hoạt động.
    *   *Thời gian dự kiến:* **8–12 tháng** (Đường găng đi qua khâu số hóa và sửa lỗi chính tả OCR quá lớn).
    *   *Đánh giá:* Rủi ro cao, không mang lại giá trị sớm cho sinh viên, dễ nản lòng và trễ tiến độ.
*   **Phương án B (Thí điểm MVP & Phát hành cuốn chiếu - Khuyến nghị):** Phát hành MVP hệ thống sau khi số hóa thí điểm xong 500 giáo trình CNTT cốt lõi để sinh viên trải nghiệm đọc ngay. Việc số hóa các giáo trình khác sẽ được thực hiện cuốn chiếu song song với quá trình vận hành hệ thống.
    *   *Thời gian dự kiến:* **3–4 tháng** tới lúc go-live MVP.
    *   *Đánh giá:* Rút ngắn thời gian đưa sản phẩm vào thực tế, kiểm chứng sớm mức độ chấp nhận của sinh viên đối với EPUB responsive, tinh chỉnh lỗi phần mềm kịp thời.

### 10.2. Bảng tiến độ chi tiết (Theo Phương án B)

![Sơ đồ tiến độ chi tiết (Gantt Chart)](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/hcmus-projectmanage--lab/docs/images/project_timeline.svg)

---

## 11. Ước tính chi phí (USD)

### 11.1. Đầu tư một lần (CapEx)

Ngân sách CapEx dùng để xây dựng hệ thống phần mềm custom và thực hiện số hóa đợt đầu cho kho tài liệu hiện hữu (~10.000 cuốn).

| Hạng mục đầu tư | Cơ sở ước tính chi tiết | Khoảng giá (USD) |
| :--- | :--- | :---: |
| **Số hóa & Biên tập EPUB** | Thuê sinh viên bán thời gian hỗ trợ scan sách + chạy OCR + biên tập hiệu chỉnh lỗi chính tả cho ~10.000 cuốn (ước tính đơn giá $2 - $4.5/cuốn tùy độ dày). | $20.000 – $45.000 |
| **Phát triển phần mềm custom** | Chi phí cơ hội nhân sự Phòng CNTT trường tự phát triển (3–4 kỹ sư × 3 tháng phát triển React/FastAPI cốt lõi). | $15.000 – $22.000 |
| **Thiết bị scan & Server** | Mua sắm 02 máy scan sách chuyên dụng dạng chữ V (chống tháo gáy sách hiếm) và bổ sung 01 máy chủ vật lý chạy MinIO/PostgreSQL. | $4.000 – $8.000 |
| **Đào tạo & Triển khai** | Tài liệu hướng dẫn, video trực quan, tổ chức các buổi tập huấn cho thủ thư và sinh viên. | $1.000 – $2.000 |
| **Dự phòng rủi ro (~15%)** | Ngân sách dự phòng cho các biến động giá phần cứng hoặc phát sinh kỹ thuật. | $5.000 – $8.000 |
| **TỔNG CAPEX** | **Ước tính tổng mức đầu tư một lần** | **≈ $45.000 – $85.000** |

### 11.2. Vận hành định kỳ (OpEx / năm)

Chi phí duy trì hệ thống hoạt động ổn định hàng năm, bắt đầu tính từ năm thứ 2.

| Hạng mục vận hành | Cơ sở ước tính chi tiết | Khoảng giá (USD/năm) |
| :--- | :--- | :---: |
| **Hạ tầng máy chủ & Lưu trữ** | Duy trì điện, đường truyền Internet băng thông cao cho server vật lý và sao lưu đám mây. | $2.000 – $4.000 |
| **Bảo trì phần mềm** | Cập nhật các bản vá bảo mật, nâng cấp thư viện React/FastAPI, xử lý sự cố. | $4.000 – $7.000 |
| **Bản quyền OCR & Dịch vụ** | Phí sử dụng Cloud OCR API hỗ trợ nếu gặp các tài liệu quá mờ cần công cụ thương mại (Google Cloud Vision). | $1.000 – $3.000 |
| **Số hóa bổ sung hàng năm** | Số hóa các giáo trình mới xuất bản hoặc sách tham khảo phát sinh. | $1.000 – $2.000 |
| **TỔNG OPEX / NĂM** | **Chi phí vận hành định kỳ hàng năm** | **≈ $8.000 – $16.000** |

---

## 12. Kết luận & Khuyến nghị

### 12.1. Kết luận

Dự án xây dựng **Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS (HCMUS-LDMS)** giải quyết trực tiếp một nhu cầu có thật và cấp bách trong việc bảo tồn học liệu và tối ưu hóa không gian của thư viện, đồng thời đem lại bước nhảy vọt về trải nghiệm đọc sách responsive (EPUB) của sinh viên trên thiết bị di động. 

Mặc dù việc tự xây dựng phần mềm custom (React + FastAPI) đòi hỏi nỗ lực lập trình ban đầu của Phòng CNTT, nhưng nó giúp nhà trường làm chủ hoàn toàn công nghệ, dễ dàng tùy biến luồng số hóa OCR -> EPUB và tích hợp sâu với hạ tầng định danh của trường mà không phụ thuộc vào bên thứ ba.

### 12.2. Khuyến nghị hành động

1.  **Phê duyệt triển khai Giai đoạn 0:** Cấp ngân sách ban đầu để Thư viện kiểm kê sách tự soạn của trường và phối hợp bộ phận Pháp chế chốt quy định số hóa nội bộ.
2.  **Thông qua phương án thí điểm cuốn chiếu (Phương án B):** Duyệt triển khai MVP phần mềm và số hóa trước 500 giáo trình CNTT để kiểm chứng tính năng EPUB Reader trên di động của sinh viên trước khi duyệt ngân sách lớn cho số hóa diện rộng.
3.  **Huy động nguồn lực sinh viên:** Cho phép Thư viện tuyển dụng sinh viên cộng tác viên bán thời gian hỗ trợ khâu biên tập sửa lỗi chính tả OCR, vừa tạo thu nhập cho sinh viên vừa tăng tốc tiến độ số hóa học liệu số.
