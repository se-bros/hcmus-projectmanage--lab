# ĐỀ XUẤT DỰ ÁN (PROJECT PROPOSAL)

## Hệ thống Quản lý Số hóa Thư viện (LibDMS)
**Thư viện hiện đại & Ban Công nghệ Thông tin**

Phiên bản 1.0 • Tháng 7/2026

## Mục lục

* [1. Tóm tắt điều hành (Executive Summary)](#1-tóm-tắt-điều-hành-executive-summary)
* [2. Business case (Câu chuyện bối cảnh & Lý do đầu tư)](#2-business-case-câu-chuyện-bối-cảnh--lý-do-đầu-tư)
* [3. Giải pháp đề xuất](#3-giải-pháp-đề-xuất)
* [4. Phân tích Chi phí – Lợi ích (Cost-Benefit Analysis)](#4-phân-tích-chi-phí--lợi-ích-cost-benefit-analysis)
* [5. Rủi ro & Biện pháp giảm thiểu](#5-rủi-ro--biện-pháp-giảm-thiểu)
* [6. Lộ trình triển khai theo giai đoạn (Roadmap)](#6-lộ-trình-triển-khai-theo-giai-đoạn-roadmap)
* [7. Tiêu chí thành công (KPIs)](#7-tiêu-chị-thành-công-kpis)
* [8. Các bên liên quan & Phân vai (Stakeholders & RACI)](#8-các-bên-liên-quan--phân-vai-stakeholders--raci)
* [9. Các đầu việc chính (Work Breakdown Structure - WBS)](#9-các-đầu-việc-chính-work-breakdown-structure---wbs)
* [10. Ước tính thời gian (Timeline)](#10-ước-tính-thời-gian-timeline)
* [11. Ước tính chi phí (USD)](#11-ước-tính-chi-phí-usd)
* [12. Kết luận & Khuyến nghị](#12-kết-luận--khuyến-nghị)

---

## 1. Tóm tắt điều hành (Executive Summary)

Trong kỷ nguyên số hóa, các thư viện truyền thống đang đối mặt với bài toán tối ưu hóa vận hành và mở rộng khả năng tiếp cận tài nguyên thông tin. Việc lưu trữ tài liệu giấy (sách, giáo trình, báo cáo, tài liệu nghiên cứu) gặp nhiều hạn chế như: diện tích lưu kho vật lý quá tải, xuống cấp cơ lý theo thời gian, quy trình quản lý mượn/trả thủ công phức tạp và bạn đọc chỉ có thể tra cứu trực tiếp tại chỗ.

Dự án đề xuất xây dựng **Hệ thống Quản lý Số hóa Thư viện (Library Digitization Management System - LibDMS)**. Đây là một nền tảng cloud-native hỗ trợ nhập tài liệu thô đa định dạng (PDF, PNG, JPEG, hoặc kết quả scan vật lý), tự động chạy nhận dạng ký tự quang học (OCR) tiếng Việt để chuyển đổi sang sách điện tử chuẩn **EPUB** (bao gồm cả Fixed-Layout và Reflowable). Hệ thống tích hợp các chức năng quản lý danh mục (category), nhãn (tag), hệ thống tài khoản phân quyền người dùng (RBAC), tìm kiếm nâng cao, tích hợp quản lý mượn/trả tài liệu vật lý, thống kê báo cáo và trình đọc sách trực tuyến (EPUB Reader).

**Các kết quả chính mong đợi:**
*   **Số hóa & Chuẩn hóa:** Xây dựng quy trình tự động hóa chuyển đổi tài liệu thô sang file EPUB chuẩn hóa, tối ưu hiển thị trên mọi thiết bị.
*   **Trải nghiệm đọc số:** Tích hợp bộ đọc trực tuyến (EPUB Reader) mượt mà trên giao diện Web, hỗ trợ bạn đọc khai thác tri thức 24/7 từ xa.
*   **Tìm kiếm thông minh:** Rút ngắn thời gian tra cứu từ trung bình 30 phút tìm kiếm thủ công xuống còn dưới 2 giây nhờ cơ chế lập chỉ mục Elasticsearch nâng cao.
*   **Quản lý toàn diện:** Quản lý mượn/trả tài liệu kết hợp theo dõi số lượng tồn kho vật lý và lượt mượn sách số. Hệ thống phân quyền chặt chẽ theo vai trò (Admin, Librarian, Reader).
*   **Kiến trúc Cloud hiện đại:** Triển khai container hóa (Docker) trên hạ tầng đám mây (AWS/Azure) giúp tự động co giãn, đảm bảo độ ổn định và an toàn thông tin cao nhất.

**Kế hoạch tài chính & Lộ trình:**
Dự án được đề xuất triển khai theo 4 giai đoạn gating nghiêm ngặt, kết hợp phương pháp Agile/Scrum cho phần kỹ thuật.
*   **Tổng chi phí đầu tư một lần (CapEx):** Ước tính từ **$45.000 đến $85.000** (bao gồm phát triển phần mềm custom, thiết lập hạ tầng cloud ban đầu và chi phí chạy OCR/chuẩn hóa thử nghiệm).
*   **Chi phí vận hành định kỳ (OpEx):** Ước tính từ **$8.000 đến $18.000/năm** tùy thuộc vào dung lượng lưu trữ cloud và băng thông sử dụng của bạn đọc.

---

## 2. Business case (Câu chuyện bối cảnh & Lý do đầu tư)

### 2.1. Câu chuyện từ thực tế vận hành

Để hiểu rõ sự cấp thiết của dự án, hãy nhìn vào trải nghiệm thực tế hàng ngày của bạn đọc và thủ thư tại một thư viện truyền thống:

![Sơ đồ Hiện trạng (As-is) vs Tương lai (To-be)](file:///d:/Project/hcmus-projectmanage--lab/docs/images/as_is_to_be_workflow.svg)

#### Câu chuyện thứ nhất: Sự bất tiện của bạn đọc Nguyễn Văn A
Bạn đọc Nguyễn Văn A là một nhà nghiên cứu cần tham khảo tài liệu kỹ thuật cũ xuất bản từ năm 1995. Tài liệu này chỉ có duy nhất một bản cứng lưu tại kho lưu trữ của thư viện trung tâm.
1.  **Di chuyển:** A phải di chuyển quãng đường xa trong giờ hành chính để đến thư viện.
2.  **Tra cứu thủ công:** A tìm kiếm mã sách trên phần mềm tra cứu cũ kỹ của thư viện nhưng chỉ có thông tin tiêu đề, tác giả. Không có cách nào để biết cuốn sách đó có chứa nội dung A cần hay không.
3.  **Chờ thủ thư lấy sách:** Thủ thư phải đi sâu vào các kệ kho bám đầy bụi để tìm tài liệu gốc.
4.  **Đọc giới hạn tại chỗ:** Cuốn sách đã quá cũ, giấy ngả vàng và dễ rách. Thư viện cấm photocopy để bảo vệ tài liệu. A phải ngồi chép tay các bảng số liệu phức tạp mất cả buổi chiều.
5.  **Mất mát vật lý:** Bản gốc duy nhất đang xuống cấp trầm trọng. Nếu bạn đọc tiếp theo vô tình làm rách hoặc ẩm ốc, nguồn tri thức quý báu này sẽ vĩnh viễn biến mất.

#### Câu chuyện thứ hai: Áp lực vận hành của thủ thư Mai
Thủ thư Mai hàng ngày phải đối mặt với khối lượng lớn tài liệu mượn/trả và áp lực bảo tồn tài liệu vật lý:
1.  **Quá tải kho bãi:** Không gian chứa sách ngày càng thu hẹp trong khi số lượng sách nhập mới tăng liên tục.
2.  **Quản lý mượn/trả thủ công:** Phải ghi chép sổ sách, kiểm tra hiện trạng sách khi trả, nhắc nhở quá hạn mượn. Quy trình này tốn nhiều công sức và dễ xảy ra sai sót dữ liệu.
3.  **Số hóa manh mún:** Thư viện từng thử quét một số tài liệu sang file ảnh (PNG/JPEG) hoặc PDF dạng ảnh scan, nhưng bạn đọc không thể tìm kiếm nội dung bên trong, dung lượng file rất lớn và không thể đọc được trên điện thoại màn hình nhỏ vì bị vỡ chữ.
4.  **Thiếu báo cáo thống kê:** Không thể đo lường chính xác cuốn sách nào đang được mượn nhiều nhất, nhóm độc giả nào hoạt động tích cực nhất để tối ưu ngân sách mua sách mới.

### 2.2. Vấn đề được giải quyết như thế nào?

Ý tưởng xây dựng **Hệ thống Quản lý Số hóa Thư viện (LibDMS)** được đề xuất nhằm giải quyết triệt để các nút thắt trên thông qua một chu trình khép kín số hóa và quản trị hiện đại:

*   **Tự động hóa số hóa sang EPUB:** Hỗ trợ nhập ảnh scan (PNG, JPEG) hoặc PDF dạng ảnh scan, chạy OCR tiếng Việt để tách text và xuất bản thành file EPUB chuẩn. Định dạng EPUB tự động thích ứng với mọi kích thước màn hình (Reflowable) hoặc giữ nguyên layout gốc (Fixed-Layout) tùy theo sự lựa chọn của thủ thư khi nhập bài.
*   **Trình đọc trực tuyến (EPUB Reader):** Bạn đọc không cần tải file về máy cá nhân (giảm thiểu rò rỉ bản quyền) mà đọc trực tiếp qua trình duyệt web trên điện thoại, máy tính bảng với các chức năng chỉnh kích thước font, đổi màu nền.
*   **Tìm kiếm toàn văn thông minh:** Tận dụng sức mạnh của Elasticsearch để lập chỉ mục toàn bộ text thu được sau OCR. Bạn đọc có thể gõ một từ khóa bất kỳ để tìm ra ngay trang sách chứa từ khóa đó trong chưa đầy 2 giây.
*   **Phân loại khoa học bằng Category và Tag:** Không còn phụ thuộc vào hệ thống phân loại tủ sách cứng nhắc, tài liệu số được phân loại đa chiều qua Category (Danh mục chính) và các thẻ Tag linh hoạt, cho phép gom nhóm tài liệu theo nhiều tiêu chí.
*   **Phân quyền chặt chẽ (RBAC):** Định nghĩa rõ ràng 3 nhóm vai trò:
    *   *Admin:* Cấu hình hệ thống, quản lý tài khoản người dùng, giám sát bảo mật.
    *   *Librarian (Thủ thư):* Thực hiện số hóa (upload, OCR, hiệu đính), phân loại category/tag, quản lý quy trình mượn/trả vật lý và phê duyệt lượt mượn trực tuyến.
    *   *Reader (Bạn đọc):* Tìm kiếm, đọc trực tuyến sách được phép, gửi yêu cầu mượn/trả tài liệu.
*   **Hiện đại hóa quản lý mượn/trả và thống kê:** Hỗ trợ theo dõi cả tài liệu số lẫn tài liệu vật lý. Hệ thống tự động ghi nhận lịch sử, xuất báo cáo biểu đồ trực quan về hiệu suất mượn sách, xu hướng quan tâm của bạn đọc.

---

## 3. Giải pháp đề xuất

### 3.1. Mô tả tổng quan

Giải pháp đề xuất là xây dựng một nền tảng **Custom Library Digitization Management System (LibDMS)** dựa trên kiến trúc hiện đại, tập trung vào việc xử lý chuyển đổi tài liệu tự động và quản lý nghiệp vụ thư viện toàn diện.

### 3.2. Năng lực cốt lõi (Core Capabilities)

*   **Pipeline Số hóa tự động (Digitization Pipeline):**
    *   Người dùng (Librarian) tải lên các file PDF (dạng scan), ảnh PNG, JPEG của tài liệu.
    *   Hệ thống gọi API dịch vụ OCR (Tesseract) để nhận diện văn bản tiếng Việt.
    *   Hệ thống chuyển đổi và đóng gói sang file chuẩn `.epub` (Fixed-Layout bảo toàn hình ảnh hoặc Reflowable text-based).
*   **EPUB Reader trực tuyến:** Tích hợp thư viện đọc sách EPUB ngay trên web browser, hỗ trợ bookmark, ghi chú, điều chỉnh hiển thị.
*   **Quản lý Category & Tag linh hoạt:** Cho phép thiết lập cây danh mục đa cấp và gán nhãn tags tự do cho từng tài liệu để phục vụ bộ lọc tìm kiếm.
*   **Quản lý người dùng và Phân quyền (RBAC):** Phân chia rõ vai trò Admin, Librarian, Reader. Tích hợp xác thực JWT bảo mật.
*   **Tìm kiếm nâng cao (Elasticsearch):** Tìm kiếm toàn văn (full-text search) có hỗ trợ phân tích ngôn ngữ tiếng Việt (Vietnamese analyzer), tìm theo danh mục, nhãn và metadata.
*   **Chatbot tra cứu tài liệu thông minh (RAG Chatbot):** Tích hợp chatbot hỏi đáp trực tiếp, cho phép bạn đọc đặt câu hỏi tự nhiên về nội dung tài liệu và nhận câu trả lời trích xuất chính xác từ kho sách đã số hóa (RAG).
*   **Nghiệp vụ Mượn/Trả sách:** Quản lý vòng đời mượn/trả sách giấy và đăng ký đọc sách điện tử có giới hạn số lượt truy cập đồng thời.
*   **Báo cáo Thống kê:** Bảng điều khiển (Dashboard) hiển thị số lượng tài liệu số hóa thành công, lượt đọc trực tuyến, sách mượn nhiều nhất và thống kê hoạt động của bạn đọc.

### 3.3. Định hướng kiến trúc (Architectural Direction)

Kiến trúc hệ thống ưu tiên sử dụng mô hình **Containerized Microservices/Modular Architecture** để triển khai trên môi trường điện toán đám mây (AWS/Azure).

![Mô hình kiến trúc hệ thống (System Architecture)](file:///d:/Project/hcmus-projectmanage--lab/docs/images/system_architecture.svg)

*   **Frontend Application:** Viết bằng **Next.js** (React) giúp tối ưu hóa SEO cho trang tra cứu công khai, giao diện Responsive tương thích tốt với thiết bị di động.
*   **Backend API Services:** Viết bằng **FastAPI (Python)** cung cấp hệ thống REST API nhanh, nhẹ, hiệu năng cao, dễ tích hợp các thư viện xử lý ngôn ngữ tự nhiên và AI.
*   **Database chính:** **PostgreSQL** để lưu trữ thông tin có cấu trúc như thông tin tài liệu, người dùng, lịch sử mượn/trả, phân loại category/tag.
*   **File Storage trong CSDL:** Sử dụng trường **BYTEA của PostgreSQL** để lưu trữ trực tiếp tệp tin EPUB và ảnh thô gốc, đảm bảo bảo mật và nhất quán dữ liệu.
*   **OCR Engine:** Container độc lập chạy **Tesseract OCR** để nhận dạng văn bản tiếng Việt từ ảnh thô.
*   **EPUB Converter:** Dịch vụ vệ tinh chạy lệnh của **Calibre/Pandoc** để chuyển đổi định dạng tài liệu sang EPUB.
*   **Search Engine:** **Elasticsearch** dùng để lưu trữ chỉ mục văn bản sau OCR phục vụ tìm kiếm toàn văn tốc độ cao.
*   **Hạ tầng triển khai:** Đóng gói Docker, quản lý bởi Docker Compose cho môi trường Staging và Kubernetes (AWS EKS hoặc Azure AKS) cho môi trường Production, kết hợp CI/CD tự động hóa.

### 3.4. Phạm vi loại trừ (Out of scope)

*   **Thiết bị phần cứng scan tài liệu:** Dự án chỉ phát triển phần mềm tiếp nhận file đầu vào, không cung cấp máy quét vật lý hay nhân sự thực hiện quét tài liệu.
*   **Thanh toán trực tuyến phí mượn sách:** Hệ thống tập trung vào quản lý nghiệp vụ thư viện cơ bản, các tính năng thanh toán phạt trễ hạn hoặc phí đọc sách sẽ được tách thành dự án nâng cấp sau.
*   **Giải quyết bản quyền bên ngoài:** Thư viện chịu trách nhiệm pháp lý về nguồn tài liệu đưa lên hệ thống. Hệ thống chỉ cung cấp công cụ kỹ thuật để kiểm soát quyền truy cập của người dùng.

---

## 4. Phân tích Chi phí – Lợi ích (Cost-Benefit Analysis)

### 4.1. Ước tính chi phí (Investment)

Dự án phân bổ ngân sách theo CapEx (Đầu tư hạ tầng và phát triển ban đầu) và OpEx (Phí duy trì dịch vụ cloud hàng năm).

![Phân rã Ngân sách Đầu tư một lần (CapEx)](file:///d:/Project/hcmus-projectmanage--lab/docs/images/capex_breakdown.svg)

> [!NOTE]
> Ngân sách chi tiết được phân rã cụ thể tại [Mục 11. Ước tính chi phí (USD)](#11-ước-tính-chi-phí-usd) của tài liệu này.

### 4.2. Lợi ích định lượng & định tính

| Đối tượng thụ hưởng | Lợi ích định lượng | Lợi ích định tính |
| :--- | :--- | :--- |
| **Ban quản lý Thư viện** | • Tiết kiệm tới **70%** không gian kho chứa cho tài liệu số hóa.<br>• Giảm **85%** thời gian thủ thư xử lý thủ tục mượn/trả sách giấy nhờ hệ thống số hóa hỗ trợ. | • Bảo tồn vĩnh viễn nội dung tài liệu quý hiếm, tránh rách hỏng.<br>• Có số liệu trực quan phục vụ tối ưu hóa mua sắm tài liệu. |
| **Bạn đọc (Reader)** | • Rút ngắn thời gian tra cứu tài liệu từ **30 phút** xuống **dưới 2 giây**.<br>• Tiếp cận tài liệu số **24/7** từ xa mà không cần di chuyển vật lý. | • Trải nghiệm đọc EPUB mượt mà trên smartphone, tự tùy chỉnh font/size chữ.<br>• Tìm kiếm sâu vào nội dung sách thay vì chỉ tìm được tên sách. |
| **Bộ phận Vận hành** | • Giảm thiểu sai sót kiểm kê tài liệu vật lý nhờ tích hợp module quản lý tồn kho số. | • Chuẩn hóa quy trình nghiệp vụ số hóa thư viện.<br>• Dễ dàng bảo trì và tự động co giãn tài nguyên cloud. |

---

## 5. Rủi ro & Biện pháp giảm thiểu

Dưới đây là ma trận rủi ro trọng yếu được nhận diện kèm biện pháp giảm thiểu:

| Nhóm rủi ro | Chi tiết rủi ro | Mức độ | Biện pháp giảm thiểu | Risk Owner |
| :--- | :--- | :--- | :--- | :--- |
| **Chất lượng OCR tiếng Việt** | Bản scan cũ, mờ dẫn đến OCR bị lỗi font, mất chữ, làm hỏng file EPUB Reflowable. | **Cao** | Thiết lập luồng kiểm duyệt và hiệu đính (Edit/Correction workflow) cho thủ thư sửa lỗi text trước khi đóng gói EPUB. Mặc định dùng Fixed-Layout cho các tài liệu có cấu trúc quá phức tạp. | **Trưởng nhóm Kỹ thuật** |
| **Bảo mật & Bản quyền tài liệu** | Tài liệu nội bộ bị cào quét (scraping) hoặc tải hàng loạt về phát tán bên ngoài. | **Trung bình** | Sử dụng Signed URL thời hạn ngắn (15 phút) cho tài nguyên. Trình đọc EPUB Reader trực tuyến chặn chuột phải copy và chặn download file trực tiếp. | **Kỹ sư Bảo mật** |
| **Sự chấp nhận của người dùng** | Bạn đọc ngại sử dụng trình đọc online, thủ thư gặp khó khăn khi vận hành pipeline số hóa mới. | **Trung bình** | Thiết kế UI/UX đơn giản, trực quan. Biên soạn video hướng dẫn ngắn, tài liệu FAQ chi tiết. Tổ chức các buổi tập huấn vận hành thực tế. | **Trưởng nhóm Triển khai** |
| **Chi phí Cloud vượt tầm kiểm soát** | Lưu trữ số lượng lớn file ảnh thô và thực hiện OCR liên tục trên Cloud làm tăng đột biến chi phí AWS/Azure. | **Trung bình** | Thiết lập chính sách vòng đời dữ liệu (Lifecycle Policy): Tự động nén/xóa ảnh thô sau khi đã chuyển đổi sang EPUB thành công. Giới hạn dung lượng upload. | **Kỹ sư Cloud/DevOps** |

---

## 6. Lộ trình triển khai theo giai đoạn (Roadmap)

Dự án được triển khai theo 4 giai đoạn rõ ràng với các điểm đánh giá gating nghiêm ngặt:

![Sơ đồ lộ trình triển khai theo giai đoạn](file:///d:/Project/hcmus-projectmanage--lab/docs/images/project_roadmap.svg)

*   **Giai đoạn 0 — Khảo sát & Chuẩn bị (Tháng 1):**
    *   *Trọng tâm:* Đánh giá mẫu chất lượng OCR trên các loại tài liệu thực tế của thư viện, thống nhất danh mục category/tag mẫu, thiết kế kiến trúc chi tiết trên Cloud.
    *   *Kết quả:* Tài liệu đặc tả kỹ thuật hệ thống, Baseline chỉ số chất lượng OCR, Bản vẽ kiến trúc Cloud được phê duyệt.
*   **Giai đoạn 1 — Xây dựng MVP & Thí điểm (Tháng 2–4):**
    *   *Trọng tâm:* Triển khai Next.js frontend và FastAPI backend, xây dựng pipeline số hóa (Upload → OCR → EPUB), tích hợp Elasticsearch tìm kiếm toàn văn, quản lý category/tag và phân quyền RBAC cơ bản.
    *   *Kết quả:* Hệ thống MVP vận hành thử nghiệm với tập dữ liệu khoảng 1.000 tài liệu mẫu.
*   **Giai đoạn 2 — Mở rộng Tính năng (Tháng 5–6):**
    *   *Trọng tâm:* Hoàn thiện trình đọc EPUB Reader online trên web, xây dựng module mượn/trả sách giấy, phát triển **Chatbot tra cứu tài liệu thông minh (RAG Chatbot)**, phát triển dashboard thống kê báo cáo trực quan cho thủ thư và ban quản lý.
    *   *Kết quả:* Hệ thống LibDMS đầy đủ chức năng phục vụ chạy thử nghiệm quy mô lớn.
*   **Giai đoạn 3 — Production & Cloud Scale (Tháng 7):**
    *   *Trọng tâm:* Đưa hệ thống lên Production trên AWS/Azure, tối ưu hóa Auto-scaling, thiết lập hệ thống giám sát Prometheus/Grafana, kiểm tra bảo mật xâm nhập (Penetration Test) và go-live chính thức.
    *   *Kết quả:* Hệ thống vận hành ổn định trên Cloud với khả năng phục vụ hàng ngàn bạn đọc đồng thời.

---

## 7. Tiêu chí thành công (KPIs)

Hệ thống LibDMS sẽ được đánh giá hiệu quả dựa trên các tiêu chí sau:

1.  **Tỷ lệ OCR chính xác:** Độ chính xác của văn bản sau OCR tiếng Việt đạt tối thiểu **85%** đối với tài liệu in rõ ràng, sạch sẽ.
2.  **Thời gian xử lý chuyển đổi:** Pipeline số hóa tự động hoàn thành chuyển đổi một tài liệu 200 trang sang EPUB trong thời gian dưới **5 phút**.
3.  **Tốc độ tìm kiếm:** Thời gian phản hồi cho truy vấn tìm kiếm toàn văn dưới **2 giây** dưới tải trọng 100 người dùng đồng thời.
4.  **Tỷ lệ chấp nhận:** Trên **80%** cán bộ thư viện đánh giá quy trình số hóa mới tiện lợi hơn phương pháp lưu trữ cũ.
5.  **Uptime SLA:** Đạt tối thiểu **99.9%** tính sẵn sàng của hệ thống trên môi trường Production Cloud.

---

## 8. Các bên liên quan & Phân vai (Stakeholders & RACI)

### 8.1. Stakeholder Register

*   **Sponsor (Nhà tài trợ):** Ban quản lý/Ban giám đốc Thư viện. Vai trò: Cấp ngân sách, chỉ đạo định hướng và duyệt go-live.
*   **Project Manager (Quản lý dự án):** Chịu trách nhiệm điều phối tiến độ, quản lý rủi ro và kết nối các nhóm nghiệp vụ với nhóm kỹ thuật.
*   **Business Analyst (Nghiệp vụ):** Thủ thư trưởng. Vai trò: Đặc tả quy trình mượn/trả sách, hệ thống phân loại category/tag và kiểm duyệt chất lượng metadata.
*   **Technical Team:** Nhóm phát triển phần mềm (Frontend, Backend, DevOps, OCR Specialists).
*   **End Users:** Bạn đọc (Reader) và cán bộ thư viện vận hành trực tiếp (Librarian).

### 8.2. Ma trận Trách nhiệm (RACI Matrix)

*   **R** (Responsible): Người thực hiện.
*   **A** (Accountable): Người chịu trách nhiệm cuối cùng.
*   **C** (Consulted): Người được tham vấn.
*   **I** (Informed): Người nhận thông tin.

| Gói công việc (WBS) | Sponsor | Project Manager | Thủ thư trưởng | Technical Team | Cán bộ thư viện | Bạn đọc |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **WP1 — Khảo sát & Thiết kế** | I | **A** | R | R | C | - |
| **WP2 — Hạ tầng & Core API** | I | C | - | **A** / R | - | - |
| **WP3 — Phát triển Pipeline & UI** | I | R | C | **A** / R | C | I |
| **WP4 — Tích hợp OCR & EPUB** | I | C | - | **A** / R | - | - |
| **WP5 — Nghiệp vụ mượn/trả & Thống kê**| I | R | **A** / R | R | R | I |
| **WP6 — Kiểm thử, Triển khai Cloud** | I | C | C | **A** / R | R | C |

---

## 9. Các đầu việc chính (Work Breakdown Structure - WBS)

Dự án được chia thành 6 gói công việc chính:

*   **WP1 — Khảo sát & Thiết kế:**
    *   Khảo sát mẫu định dạng tài liệu đầu vào (PDF scan, ảnh).
    *   Đặc tả yêu cầu nghiệp vụ quản lý danh mục, tags, mượn/trả.
    *   Thiết kế kiến trúc hệ thống và mô hình dữ liệu PostgreSQL.
*   **WP2 — Hạ tầng Cloud & Core API:**
    *   Thiết lập VPC, Subnet, VM và Container Registry trên AWS/Azure.
    *   Cài đặt PostgreSQL (cấu hình phân tách table lưu trữ BYTEA), Elasticsearch.
    *   Xây dựng Core API FastAPI (quản lý user, auth JWT, phân quyền RBAC).
*   **WP3 — Giao diện & Pipeline số hóa:**
    *   Xây dựng giao diện Next.js cho Admin/Librarian và Portal tra cứu cho Reader.
    *   Lập trình luồng upload tài liệu và quản lý metadata Dublin Core.
*   **WP4 — OCR Engine & EPUB Generator:**
    *   Cấu hình container Tesseract OCR tối ưu cho tiếng Việt.
    *   Tích hợp Calibre/Pandoc pipeline để tự động xuất bản file EPUB.
    *   Xây dựng giao diện hiệu đính text (correction dashboard) cho thủ thư.
*   **WP5 — Nghiệp vụ Thư viện nâng cao:**
    *   Phát triển module mượn/trả sách (vật lý & số).
    *   Xây dựng trình đọc sách EPUB Reader tích hợp trên giao diện web.
    *   Tích hợp dịch vụ **Chatbot RAG** hỏi đáp dựa trên nội dung tài liệu.
    *   Thiết kế màn hình Dashboard thống kê báo cáo (biểu đồ Recharts/Chart.js).
*   **WP6 — Kiểm thử & Triển khai Production:**
    *   Kiểm thử tích hợp hệ thống, đo lường tốc độ Elasticsearch và chất lượng OCR.
    *   Thiết lập CI/CD pipeline tự động build docker image và deploy lên cloud.
    *   Đào tạo hướng dẫn sử dụng cho thủ thư và vận hành chính thức.

---

## 10. Ước tính thời gian (Timeline)

Thời gian triển khai dự án dự kiến kéo dài **7 tháng** để đưa hệ thống lên trạng thái Production Cloud hoàn chỉnh:

![Sơ đồ tiến độ chi tiết (Gantt Chart)](file:///d:/Project/hcmus-projectmanage--lab/docs/images/project_timeline.svg)

- **Tháng 1 (WP1):** Khảo sát hiện trạng tài liệu và hoàn thành thiết kế hệ thống.
- **Tháng 2 - 3 (WP2 & WP3):** Thiết lập hạ tầng cloud ban đầu, lập trình backend API và xây dựng giao diện portal cơ bản.
- **Tháng 4 (WP4):** Nghiên cứu tích hợp OCR tiếng Việt và pipeline chuyển đổi EPUB tự động. Go-live phiên bản MVP thí điểm.
- **Tháng 5 - 6 (WP5):** Phát triển trình đọc EPUB Reader online, module quản lý mượn/trả, màn hình thống kê dữ liệu.
- **Tháng 7 (WP6):** Kiểm thử tải, vá lỗi bảo mật, triển khai chính thức lên AWS/Azure Production và bàn giao dự án.

---

## 11. Ước tính chi phí (USD)

### 11.1. Chi phí đầu tư một lần (CapEx)

Ngân sách CapEx dùng để xây dựng hệ thống phần mềm custom, mua sắm bản quyền (nếu có) và thiết lập ban đầu:

| Hạng mục đầu tư | Chi tiết cơ sở ước tính | Khoảng giá (USD) |
| :--- | :--- | :---: |
| **Phát triển phần mềm custom** | Nhóm phát triển gồm 5 kỹ sư (Frontend, Backend, DevOps, QA, OCR specialist) thực hiện trong 5 tháng phát triển chính. | $35.000 – $60.000 |
| **Thiết lập hạ tầng Cloud ban đầu** | Đăng ký dịch vụ, cấu hình mạng bảo mật VPC, thiết lập Kubernetes Cluster và PostgreSQL Database ban đầu. | $3.000 – $6.000 |
| **Kiểm thử chất lượng & Pen-test** | Thuê đánh giá độc lập về hiệu năng tìm kiếm Elasticsearch, chất lượng OCR tiếng Việt và kiểm tra lỗ hổng bảo mật Web. | $3.000 – $7.000 |
| **Đào tạo, chuyển giao công nghệ** | Biên soạn tài liệu hướng dẫn số hóa, video tập huấn thủ thư, hỗ trợ trực tiếp tuần đầu vận hành. | $1.000 – $3.000 |
| **Dự phòng phát sinh (15%)** | Chi phí dự phòng cho các thay đổi về phạm vi hoặc biến động tỷ giá/dịch vụ cloud. | $3.000 – $9.000 |
| **TỔNG CAPEX** | **Tổng mức đầu tư một lần** | **≈ $45.000 – $85.000** |

### 11.2. Chi phí vận hành định kỳ (OpEx / năm)

Chi phí duy trì hệ thống trên Cloud hoạt động ổn định hàng năm (bắt đầu từ năm thứ 2):

| Hạng mục vận hành | Chi tiết cơ sở ước tính | Khoảng giá (USD/năm) |
| :--- | :--- | :---: |
| **Hạ tầng Cloud duy trì** | Chi phí máy chủ ảo EC2/VM, PostgreSQL Database instance (bao gồm cả dung lượng lưu trữ BYTEA), Elasticsearch Cluster trên AWS/Azure. | $4.000 – $8.000 |
| **Bảo trì & Hỗ trợ kỹ thuật** | Vá lỗi bảo mật định kỳ, cập nhật phiên bản thư viện, hỗ trợ kỹ thuật mức độ 2 (1 nhân sự CNTT bán thời gian). | $3.000 – $7.000 |
| **Băng thông & Dịch vụ phụ trợ** | Chi phí băng thông truyền tải file EPUB tới bạn đọc (Data Transfer Out), dịch vụ gửi email thông báo, giám sát cloud. | $1.000 – $3.000 |
| **TỔNG OPEX / NĂM** | **Chi phí vận hành hàng năm** | **≈ $8.000 – $18.000** |

---

## 12. Kết luận & Khuyến nghị

### 12.1. Kết luận

Dự án xây dựng **Hệ thống Quản lý Số hóa Thư viện (LibDMS)** giải quyết triệt để vấn đề quá tải vật lý và giới hạn địa lý của mô hình thư viện truyền thống. Việc chuyển đổi từ DSpace sang một **Custom Modern Stack (Next.js + FastAPI)** chạy containerized trên Cloud là quyết định kỹ thuật đắn, giúp đáp ứng linh hoạt các nghiệp vụ đặc thù như: Pipeline OCR tự động tạo EPUB, trình đọc EPUB Reader online, chatbot hỏi đáp RAG, phân loại đa chiều category/tags, và tích hợp mượn/trả tiện lợi.

Dự án có tính khả thi kỹ thuật cao nhờ tận dụng các thư viện và công cụ mã nguồn mở chất lượng cao (Tesseract, Elasticsearch, LangChain), đồng thời thiết kế sẵn khả năng mở rộng quy mô lớn trên AWS/Azure.

### 12.2. Khuyến nghị hành động

Nhóm dự án kiến nghị Ban quản lý Thư viện phê duyệt các bước sau để khởi động dự án:
1.  **Phê duyệt ngân sách cho Giai đoạn 0 (Khảo sát & Thiết kế):** Cấp kinh phí ban đầu để tiến hành đánh giá mẫu chất lượng OCR trên nhiều loại giấy/tài liệu khác nhau và hoàn thiện hồ sơ thiết kế kiến trúc chi tiết.
2.  **Thông qua mô hình MVP cuốn chiếu:** Đồng ý phát hành phiên bản MVP thí điểm với quy mô 1.000 tài liệu mẫu sau 4 tháng triển khai để kiểm nghiệm hiệu năng thực tế trước khi hoàn thiện toàn bộ các tính năng mượn/trả và thống kê.
3.  **Lập kế hoạch chuẩn bị hạ tầng Cloud:** Phối hợp với Phòng CNTT đăng ký tài khoản AWS/Azure của đơn vị để chuẩn bị sẵn sàng môi trường triển khai ngay khi dự án được phê duyệt triển khai kỹ thuật.
