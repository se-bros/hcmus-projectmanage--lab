# ĐỀ XUẤT DỰ ÁN (PROJECT PROPOSAL)

## Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS (HCMUS-LDMS)

### THÔNG TIN TÀI LIỆU (DOCUMENT CONTROL)

| Trường thông tin (Field) | Nội dung đặc tả (Description) |
| :--- | :--- |
| **Mã tài liệu (Document ID)** | `HCMUS-LDMS-PRP` |
| **Tên tài liệu (Document Title)** | Đề xuất dự án (Project Proposal Document) |
| **Dự án (Project Name)** | HCMUS-LDMS |
| **Đơn vị soạn thảo (Author/Organization)** | Thư viện & Phòng Công nghệ Thông tin - HCMUS |
| **Người xem xét (Reviewer)** | Trưởng phòng CNTT & Giám đốc Thư viện |
| **Người phê duyệt (Approver)** | Ban Giám hiệu Trường ĐH Khoa học Tự nhiên |
| **Cấp độ bảo mật (Security Class)** | Internal (Nội bộ trường) |
| **Trạng thái tài liệu (Status)** | Under Review (Đang thẩm định) |

### LỊCH SỬ PHIÊN BẢN (REVISION HISTORY)

| Phiên bản (Version) | Ngày phát hành (Date) | Mô tả thay đổi (Description of Change) | Người thực hiện (Author) |
| :---: | :---: | :--- | :---: |
| 1.0 | 06/07/2026 | Khởi tạo dự thảo đề xuất dự án ban đầu (v1.0). | Mạch Quốc Tấn |
| 2.0 | 14/07/2026 | Chuẩn hóa, chuyển WBS/RACI sang các tài liệu phù hợp, cập nhật chi phí VNĐ. | Mạch Quốc Tấn |

---

## Mục lục

* [1. Tóm tắt điều hành (Executive Summary)](#1-tóm-tắt-điều-hành-executive-summary)
* [2. Lý do đầu tư và Bối cảnh thực tế (Business Case)](#2-lý-do-đầu-tư-và-bối-cảnh-thực-tế-business-case)
    * [2.1. Hành trình từ "Nỗi đau" vật lý đến rào cản tri thức của Độc giả](#21-hành-trình-từ-nỗi-đau-vật-lý-đến-rào-cản-tri-thức-của-độc-giả)
    * [2.2. Sự chuyển mình đột phá qua ý tưởng Scan-to-EPUB tích hợp](#22-sự-chuyển-mình-đột-phá-qua-ý-tưởng-scan-to-epub-tích-hợp)
    * [2.3. Phân tích đối chuẩn: Đối thủ cạnh tranh & Phương án kết hợp công cụ có sẵn](#23-phân-tích-đối-chuẩn-đối-thủ-cạnh-tranh--phương-án-kết-hợp-công-cụ-có-sẵn)
* [3. Giải pháp đề xuất và Định hướng công nghệ](#3-giải-pháp-đề-xuất-và-định-hướng-công-nghệ)
    * [3.1. Mô tả tổng quan giải pháp](#31-mô-tả-tổng-quan-giải-pháp)
    * [3.2. Định hướng kiến trúc công nghệ](#32-định-hướng-kiến-trúc-công-nghệ)
    * [3.3. Phạm vi loại trừ cấp cao](#33-phạm-vi-loại-trừ-cấp-cao)
* [4. Phân tích Chi phí – Lợi ích (Cost-Benefit Analysis)](#4-phân-tích-chi-phí--lợi-ích-cost-benefit-analysis)
    * [4.1. Bảng phân tích lợi ích định lượng và định tính](#41-bảng-phân-tích-lợi-ích-định-lượng-và-định-tính)
    * [4.2. Ước lượng chi phí đầu tư ban đầu (CapEx)](#42-ước-lượng-chi-phí-đầu-tư-ban-đầu-capex)
    * [4.3. Ước lượng chi phí vận hành định kỳ (OpEx)](#43-ước-lượng-chi-phí-vận-hành-định-kỳ-opex)
    * [4.4. Mô hình kinh tế tránh chi phí và Điểm hòa vốn](#44-mô-hình-kinh-tế-tránh-chi-phí-và-điểm-hòa-vốn)
* [5. Lộ trình triển khai cấp cao (High-Level Roadmap)](#5-lộ-trình-triển-khai-cấp-cao-high-level-roadmap)
* [6. Danh mục rủi ro kinh doanh và Biện pháp giảm thiểu](#6-danh-mục-rủi-ro-kinh-doanh-và-biện-pháp-giảm-thiểu)
* [7. Kết luận và Khuyến nghị hành động](#7-kết-luận-và-khuyến-nghị-hành-động)

---

## 1. Tóm tắt điều hành (Executive Summary)

Thư viện Trường Đại học Khoa học Tự nhiên (HCMUS) hiện quản lý hàng chục ngàn tài liệu học thuật cứng độc bản. Việc lưu trữ vật lý này đang đối mặt với các thách thức lớn về quá tải diện tích kho bãi, xuống cấp tài liệu và rào cản địa lý tiếp cận thông tin đối với sinh viên tại cơ sở Linh Trung (Thủ Đức). Các file PDF scan hiện tại chỉ là ảnh chụp tĩnh, không responsive và cực kỳ khó đọc trên các thiết bị di động.

Đề xuất này hướng tới việc xây dựng **Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS (HCMUS-LDMS)** nhằm tự động hóa luồng số hóa khép kín: quét tài liệu giấy -> nhận dạng ký tự quang học (**Tesseract OCR** tiếng Việt) -> hiệu chỉnh lỗi chính tả trực tuyến -> đóng gói tự động sang định dạng sách điện tử **EPUB 3.0 reflowable** tương thích mọi thiết bị di động, lập chỉ mục toàn văn (**Elasticsearch**) và phục vụ đọc trực tuyến bảo mật (**Signed URL**) cho sinh viên và giảng viên nội bộ trường.

**Các chỉ số thành công chính mong đợi:**

* Số hóa và đóng gói thành công 2.500+ tài liệu học liệu cốt lõi sang EPUB 3.0.
* Rút ngắn thời gian tra cứu và đọc tài liệu số xuống dưới 3 giây qua Elasticsearch.
* Tỷ lệ nhận dạng ký tự quang học chính xác đạt tối thiểu 85% trước khi soát lỗi.
* Không xảy ra sự cố rò rỉ hoặc tải lậu file sách gốc ra ngoài mạng nội bộ.

**Khung tài chính ước tính:**

* **Tổng mức đầu tư một lần (CapEx):** 75.000.000 VNĐ – 95.000.000 VNĐ (trong đó thiết bị quét chuyên nghiệp và chi phí nhân sự số hóa đợt đầu chiếm tỷ trọng lớn nhất).
* **Chi phí vận hành hàng năm (OpEx):** 15.000.000 VNĐ – 30.000.000 VNĐ/năm.
* **Thời gian hòa vốn kinh tế học thuật:** Dự kiến đạt được từ **2.5 – 3.8 năm** vận hành thông qua mô hình tránh chi phí lưu kho vật lý và tiết kiệm thời gian vận hành thủ thư.

## 2. Lý do đầu tư và Bối cảnh thực tế (Business Case)

### 2.1. Hành trình từ "Nỗi đau" vật lý đến rào cản tri thức của Độc giả
Câu chuyện bắt đầu từ hành trình học tập hàng ngày của một sinh viên khoa Công nghệ Thông tin tại cơ sở Linh Trung - Thủ Đức. Để mượn được một cuốn giáo trình chuyên ngành độc bản về Kiến trúc Máy tính, sinh viên này phải bắt tuyến xe buýt 08 di chuyển hơn 15km về cơ sở 1 Quận 5 trong cái nắng gay gắt. Khi đến nơi, cuốn sách giấy duy nhất đã bị rách góc, ố vàng do tuổi thọ hơn 15 năm và độ ẩm cao của kho lưu trữ. Sinh viên chỉ được phép đọc tại chỗ, cấm mang về và cấm photocopy vì lý do bảo vệ bản quyền. Khi cố gắng chụp ảnh lại các trang sách bằng điện thoại để về nhà đọc, các file ảnh tĩnh PDF scan này không thể co giãn chữ (non-responsive), buộc sinh viên phải liên tục zoom to nhỏ trên màn hình điện thoại di động nhỏ hẹp, dẫn đến mỏi mắt và giảm sút hiệu quả tiếp cận tri thức.

Tại phòng đọc chính Quận 5, các thủ thư cũng đang phải đối mặt với áp lực khổng lồ. Hơn 40% học liệu cốt lõi đang xuống cấp nghiêm trọng. Mỗi lần độc giả mượn trả, thủ thư phải tìm kiếm thủ công trong những kệ sách cũ kỹ bám đầy bụi. Diện tích kho kệ chứa sách giấy đã chiếm trọn 100% không gian thiết kế, khiến thư viện không còn bất kỳ khoảng trống nào để cải tạo thành không gian tự học số (Smart Learning Space) hiện đại phục vụ sinh viên thảo luận nhóm.

### 2.2. Sự chuyển mình đột phá qua ý tưởng Scan-to-EPUB tích hợp
Ý tưởng của **HCMUS-LDMS** ra đời để viết nên một câu chuyện hoàn toàn mới, biến quy trình thủ công lạc hậu thành một trải nghiệm số hóa tự động hóa khép kín:

* **Từ Trang giấy đến Sách điện tử động (Scan-to-EPUB):** Sách giấy được đặt lên máy quét chuyên dụng chữ V, hệ thống tự động đẩy ảnh lên và kích hoạt engine **Tesseract OCR** để nhận dạng văn bản tiếng Việt. Thay vì để thủ thư gõ lại thủ công, hệ thống cung cấp giao diện **Split-screen Editor** trực quan chia đôi màn hình: bên trái hiển thị ảnh chụp trang gốc, bên phải là trình soạn thảo văn bản đã OCR. Thủ thư hoặc sinh viên cộng tác viên chỉ cần đối chiếu nhanh, sửa vài lỗi chính tả thô và nhấn nút. Ngay lập tức, công cụ **Pandoc** tự động đóng gói nội dung đã biên tập thành chuẩn **EPUB 3.0 reflowable**.
* **Trải nghiệm Độc giả Kỷ nguyên số:** Cuốn sách sau khi xuất bản sẽ được lập chỉ mục toàn văn vào **Elasticsearch**. Sinh viên tại Thủ Đức nay chỉ cần mở điện thoại, truy cập hệ thống qua Keycloak SSO và gõ từ khóa tìm kiếm. Trong vòng chưa đầy 3 giây, hệ thống trả về kết quả chính xác đến từng chương sách và hiển thị vị trí vật lý của sách giấy tại kho Quận 5 nếu sinh viên muốn đến mượn trực tiếp. Trình đọc web Epub.js cho phép sinh viên co giãn cỡ chữ từ 80% đến 200%, đổi font (Roboto, Inter, hoặc OpenDyslexic cho người khó đọc) và chỉnh chế độ nền Sepia bảo vệ mắt, mang lại trải nghiệm đọc sách responsive tuyệt hảo trên mọi thiết bị.
* **Bảo vệ bản quyền số tuyệt đối:** Để giảng viên yên tâm đóng góp giáo trình, hệ thống tích hợp cơ chế bảo mật DRM nghiêm ngặt. Khi sinh viên đọc sách, hệ thống sử dụng **Signed URL** kết nối trực tiếp đến MinIO Storage với thời hạn hiệu lực tối đa 15 phút. Các hành vi nhấn chuột phải, copy (`Ctrl+C`), hoặc in ấn (`Ctrl+P`) đều bị vô hiệu hóa hoàn toàn đối với tài liệu nội bộ, ngăn chặn tuyệt đối việc tải lậu và rò rỉ file sách gốc ra ngoài.
* **Giải phóng và Hiện đại hóa thư viện:** Khi 2.500+ cuốn sách giáo trình được số hóa thành công lên hệ thống, thư viện Quận 5 sẽ thu hồi được hơn 60-70% diện tích kệ sách giấy cũ. Không gian này sẽ lập tức được cải tạo thành các phòng thảo luận thông minh, trang bị màn hình tương tác và mạng Wi-Fi tốc độ cao, hiện thực hóa mục tiêu Đại học số của HCMUS.

### 2.3. Phân tích đối chuẩn: Đối thủ cạnh tranh & Phương án kết hợp công cụ có sẵn

Để chứng minh tính thuyết phục của việc tự phát triển hệ thống HCMUS-LDMS, đề xuất này thực hiện phân tích đối chuẩn (benchmarking) giữa giải pháp đề xuất với hai phương án thay thế phổ biến:

* **So sánh với đối thủ cạnh tranh (Commercial Solutions):** Các giải pháp thư viện điện tử thương mại (như Lạc Việt Vebrary, DSpace thương mại) yêu cầu chi phí bản quyền và triển khai rất cao (thường từ 300 triệu đến hơn 1 tỷ VNĐ), vượt quá xa mức ngân sách giới hạn dưới 100 triệu VNĐ của dự án này. Hơn nữa, các hệ thống đóng này cực kỳ khó tùy biến để tích hợp quy trình sửa lỗi OCR Split-screen chuyên biệt cho tiếng Việt chuyên ngành, đồng thời không hỗ trợ cơ chế bảo mật DRM động thông qua Signed URL liên kết trực tiếp với LDAP của trường.
* **So sánh với phương án kết hợp công cụ có sẵn (Composition of Existing Tools):** Phương án thay thế thủ công là sử dụng máy quét văn phòng -> chạy phần mềm Abbyy FineReader offline -> đóng gói EPUB bằng Calibre -> chia sẻ qua Google Drive/OneDrive. Phương án này gặp 3 nút thắt lớn:
  1. *Quy trình rời rạc:* Không có tính liên kết tự động, tốn từ 2-3 giờ lao động thủ công của thủ thư cho mỗi đầu sách để chuyển đổi qua lại giữa các phần mềm.
  2. *Rủi ro bản quyền nghiêm trọng:* Google Drive/OneDrive không có cơ chế chặn tải xuống tệp gốc, không chặn được chuột phải copy, và không có Signed URL tự động hết hạn sau 15 phút, dẫn đến nguy cơ cao bị sinh viên phát tán học liệu ra ngoài.
  3. *Tra cứu hạn chế:* Không hỗ trợ cơ chế lập chỉ mục tìm kiếm toàn văn sâu đến từng trang sách và highlight kết quả theo ngữ cảnh như Elasticsearch.
* **Quy trình thẩm định AI và xem xét bởi con người (AI-assisted & Human Review):** Hệ thống LDMS ứng dụng mô hình kết hợp tối ưu: engine AI (Tesseract OCR chạy bất đồng bộ qua Celery/Redis) thực hiện nhận dạng thô, sau đó con người (biên tập viên/thủ thư/sinh viên CTV) đóng vai trò kiểm soát chất lượng (Human-in-the-loop) soát lỗi chính tả trực quan trên giao diện Split-screen trước khi phê duyệt xuất bản chính thức, bảo đảm độ chính xác học thuật đạt 100% với chi phí thấp nhất.

## 3. Giải pháp đề xuất và Định hướng công nghệ

### 3.1. Mô tả tổng quan giải pháp
Xây dựng một ứng dụng Web Portal và Dashboard nghiệp vụ tự phát triển (custom-built) quản lý vòng đời tài liệu số hóa. Thủ thư scan tài liệu giấy, đẩy lên hệ thống để chạy OCR và biên tập lỗi chính tả trên giao diện trực quan Split-screen, sau đó đóng gói EPUB và phát hành cho độc giả đọc trực tuyến responsive.

### 3.2. Định hướng kiến trúc công nghệ
Hệ thống được phát triển theo mô hình **Modular Monolith** nhằm tối ưu chi phí hạ tầng và vận hành nội bộ:

* **Frontend:** React 18 (TypeScript), Tailwind CSS và thư viện hiển thị sách Epub.js.
* **Backend:** FastAPI (Python 3.11) và Celery/Redis xử lý các tác vụ nặng (OCR, Pandoc) bất đồng bộ.
* **Cơ sở dữ liệu:** PostgreSQL 16 (lưu trữ quan hệ) và Elasticsearch 8.x (lập chỉ mục tìm kiếm toàn văn).
* **Lưu trữ đối tượng:** MinIO Object Storage (On-premise tương thích S3).
* **Định danh & Xác thực:** Keycloak 24.x liên kết LDAP/Active Directory sẵn có của trường.

### 3.3. Phạm vi loại trừ cấp cao
* Hệ thống chống đạo văn chuyên sâu (chỉ thiết lập API mở phục vụ tích hợp tương lai).
* Số hóa các hồ sơ hành chính, học bạ, tài liệu nhân sự của trường.
* Tính năng tìm kiếm trí tuệ nhân tạo (AI/RAG) - hoãn sang Giai đoạn 3 của dự án.

## 4. Phân tích Chi phí – Lợi ích (Cost-Benefit Analysis)

### 4.1. Bảng phân tích lợi ích định lượng và định tính

| Đối tượng thụ hưởng | Lợi ích định lượng | Lợi ích định tính |
| :--- | :--- | :--- |
| **Thư viện HCMUS** | • Thu hồi khoảng **60-70%** diện tích kệ sách giấy tại phòng đọc Quận 5.<br>• Giảm **85%** thời gian thủ thư xử lý yêu cầu mượn trả và tra kho vật lý. | • Bảo tồn vĩnh viễn học liệu gốc của trường.<br>• Hiện đại hóa hình ảnh thư viện, nâng cao thương hiệu đại học số. |
| **Độc giả (Sinh viên, GV)** | • Đọc sách responsive mượt mà **100%** trên smartphone.<br>• Tiếp cận học liệu từ xa **24/7**.<br>• Tra cứu từ khóa nội dung sách dưới **3 giây**. | • Chủ động trong học tập trực tuyến.<br>• Dễ dàng tra cứu công thức, lý thuyết phục vụ nghiên cứu và ôn thi. |
| **Ban Giám hiệu / Trường** | • Tối ưu hóa hạ tầng CNTT và server ảo hóa sẵn có.<br>• Đạt chỉ tiêu chuyển đổi số giáo dục cấp ĐHQG-HCM. | • Làm chủ hoàn toàn mã nguồn hệ thống.<br>• Tạo nền tảng chia sẻ học liệu số hóa dùng chung an toàn. |

### 4.2. Ước lượng chi phí đầu tư ban đầu (CapEx)

| Hạng mục đầu tư | Cơ sở ước tính | Khoảng giá (VNĐ) |
| :--- | :--- | :---: |
| **Số hóa & Biên tập EPUB** | Chi phí nhân công (sinh viên CTV bán thời gian) scan, OCR và soát lỗi chính tả cho ~10.000 cuốn sách (3.000 – 4.000 VNĐ/cuốn). | 30.000.000 – 40.000.000 |
| **Phát triển phần mềm custom** | Chi phí nhân sự Phòng CNTT tự lập trình React/FastAPI trong 3 tháng. | 25.000.000 – 35.000.000 |
| **Thiết bị scan & Server** | Mua 02 máy quét chữ V chuyên dụng và bổ sung RAM/SSD cho cụm máy chủ ảo hóa của trường. | 10.000.000 – 12.000.000 |
| **Đào tạo & Triển khai** | Tài liệu hướng dẫn sử dụng, video trực quan và tổ chức các buổi tập huấn cho thủ thư. | 2.000.000 – 4.000.000 |
| **Dự phòng rủi ro (~15%)** | Dự phòng biến động giá phần cứng hoặc phát sinh kỹ thuật. | 5.000.000 – 10.000.000 |
| **TỔNG CAPEX** | **Tổng đầu tư ban đầu ước tính** | **≈ 75.000.000 – 95.000.000** |

### 4.3. Ước lượng chi phí vận hành định kỳ (OpEx)

| Hạng mục vận hành | Cơ sở ước tính (hàng năm, từ năm thứ 2) | Khoảng giá (VNĐ/năm) |
| :--- | :--- | :---: |
| **Hạ tầng Server & Cloud** | Duy trì điện, mạng băng thông cao và sao lưu tự động (PgBackRest/Restic). | 4.000.000 – 8.000.000 |
| **Bảo trì phần mềm** | Nâng cấp bảo mật, vá lỗi, cập nhật các gói React/FastAPI. | 6.000.000 – 12.000.000 |
| **Dịch vụ Cloud OCR bổ sung** | Bản quyền Cloud OCR API dự phòng dành cho sách in quá mờ. | 3.000.000 – 6.000.000 |
| **Số hóa bổ sung hàng năm** | Số hóa giáo trình mới phát sinh. | 2.000.000 – 4.000.000 |
| **TỔNG OPEX / NĂM** | **Chi phí vận hành hàng năm** | **≈ 15.000.000 – 30.000.000** |

### 4.4. Mô hình kinh tế tránh chi phí và Điểm hòa vốn
* **Mô hình Tránh chi phí (Cost Avoidance):** Tiết kiệm tương đương **20.000.000 VNĐ/năm** nhờ giải phóng mặt bằng kệ sách vật lý tại Quận 5 làm phòng tự học số, tránh được chi phí đầu tư xây dựng kho bãi vật lý mới. Tiết kiệm giờ công lao động thủ thư mượn trả thủ công trị giá **15.000.000 VNĐ/năm**.
* **Phân tích hòa vốn:** Với mức lợi ích kinh tế gián tiếp quy đổi đạt **20.000.000 VNĐ/năm**, hệ thống dự kiến đạt điểm hòa vốn kinh tế học thuật sau **2.5 đến 3.8 năm** vận hành thực tế.

## 5. Lộ trình triển khai cấp cao (High-Level Roadmap)

Dự án kéo dài **20 tuần** và chia thành 4 giai đoạn lớn kết hợp kiểm soát cổng (Gating Checkpoints):

* **Giai đoạn 0 — Khảo sát & Bản quyền (Tuần 1–2):** Kiểm kê kho sách tự soạn, bộ phận Pháp chế thẩm định quy chế bản quyền số hóa nội bộ và khảo sát báo giá máy quét chữ V.
* **Giai đoạn 1 — Xây dựng MVP & Thí điểm (Tuần 3–12):** Lập trình React/FastAPI cốt lõi, tích hợp OCR, Pandoc, MinIO, Keycloak; tiến hành số hóa thí điểm 500 cuốn sách ngành CNTT để kiểm thử.
* **Giai đoạn 2 — Số hóa Diện rộng (Tuần 13–18):** Chuyển giao công nghệ cho thư viện, tuyển sinh viên CTV và tiến hành số hóa hàng loạt 2.000 giáo trình cốt lõi tiếp theo.
* **Giai đoạn 3 — Nghiệm thu & Chuyển giao (Tuần 19–20):** Kiểm thử nghiệm thu (UAT), pentest bảo mật, đào tạo thủ thư và chính thức go-live toàn trường.

## 6. Danh mục rủi ro kinh doanh và Biện pháp giảm thiểu

| Nhóm rủi ro | Chi tiết rủi ro | Mức độ | Biện pháp giảm thiểu | Risk Owner |
| :--- | :--- | :--- | :--- | :--- |
| **Bản quyền & SHTT** | Số hóa nhầm tài liệu có bản quyền ngoài trường gây tranh chấp pháp lý. | **Cao** | • Chỉ số hóa sách nội bộ, giáo trình tự soạn.<br>• Phân quyền truy cập Internal/Restricted nghiêm ngặt. | **Ban Giám đốc Thư viện** |
| **Chất lượng OCR** | Sách in cũ mờ làm giảm độ chính xác OCR dưới 85%, gây quá tải rà soát lỗi. | **Trung bình** | • Tiền xử lý ảnh scan (lọc nhiễu, tăng tương phản).<br>• MVP chỉ làm sách in rõ nét từ 2010 trở đi. | **Phòng Công nghệ Thông tin** |
| **Rò rỉ tài liệu** | Sinh viên dùng công cụ cào web lấy file EPUB gốc phát tán bên ngoài. | **Trung bình** | • Dùng Signed URL MinIO hạn dùng 15 phút.<br>• Chặn copy, chuột phải, chia nhỏ file EPUB. | **Phòng Công nghệ Thông tin** |
| **Quá tải nhân sự** | Đội ngũ kỹ sư kiêm nhiệm 50% bị quá tải công việc trường phát sinh. | **Trung bình** | • PM ký cam kết phân bổ thời gian làm việc chính thức.<br>• Sử dụng Docker để tối ưu hóa khâu deploy. | **Phòng Công nghệ Thông tin** |

## 7. Kết luận và Khuyến nghị hành động

### 7.1. Kết luận
Hệ thống **HCMUS-LDMS** giải quyết trực tiếp nhu cầu cấp thiết về học liệu số và giải phóng diện tích thư viện. Việc tự xây dựng hệ thống custom giúp trường làm chủ công nghệ vĩnh viễn, dễ dàng tích hợp hạ tầng định danh Keycloak sẵn có và tiết kiệm chi phí bản quyền khổng lồ so với mua phần mềm thương mại.

### 7.2. Khuyến nghị hành động
1. Phê duyệt chủ trương triển khai và cấp ngân sách ban đầu thực hiện **Giai đoạn 0 (Khảo sát)**.
2. Thông qua phương án triển khai **thí điểm cuốn chiếu MVP** để kiểm chứng hiệu quả thực tế trước khi đầu tư số hóa diện rộng.
3. Cho phép Thư viện tuyển dụng sinh viên CTV bán thời gian để hỗ trợ khâu biên tập hiệu chỉnh chữ OCR thô.
