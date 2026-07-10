# FEASIBILITY STUDY

## Hệ thống Quản lý Số hóa Thư viện (LibDMS)

**Thư viện hiện đại & Ban Công nghệ Thông tin**

Phiên bản 1.0 • Tháng 7/2026

## Mục lục

* [1. 8 Khía cạnh Khả thi](#1-8-khía-cạnh-khả-thi)
* [2. SWOT & Benchmarking](#2-swot--benchmarking)
* [3. Kế hoạch Tài chính (Cost vs Budget)](#3-kế-hoạch-tài-chính-cost-vs-budget)
* [4. Quản trị Rủi ro](#4-quản-trị-rủi-ro)
* [5. Cấu trúc Báo cáo Khả thi — Tổng kết](#5-cấu-trúc-báo-cáo-khả-thi--tổng-kết)
* [6. Vì sao cần Feasibility Study](#6-vì-sao-cần-feasibility-study)

---

## 1. 8 Khía cạnh Khả thi

| Khía cạnh | Đánh giá |
| --- | --- |
| **Pháp lý (Legal)** | **Trung bình.** Rủi ro về bản quyền tác giả đối với tài liệu được số hóa. Tuy nhiên, thư viện đóng vai trò là chủ sở hữu hoặc đơn vị được ủy quyền khai thác tài liệu. Hệ thống hỗ trợ cơ chế phân quyền RBAC và chặn sao chép/tải tệp trực tuyến để hạn chế tối đa vi phạm bản quyền. |
| **Thị trường (Market — cung/cầu)** | **Khả thi cao.** Nhu cầu tra cứu tài liệu và đọc sách trực tuyến của bạn đọc ngày càng tăng cao, đặc biệt sau xu hướng học tập/làm việc từ xa. Phía "cung" có rất nhiều thư viện, giải pháp OCR và định dạng EPUB mã nguồn mở trưởng thành trên thị trường. |
| **Kinh tế (Economic)** | **Khả thi.** Chi phí đầu tư ban đầu (CapEx) và chi phí vận hành hàng năm (OpEx) được tối ưu hóa bằng cách sử dụng các dịch vụ cloud-native trả tiền theo mức độ sử dụng (pay-as-you-go) trên AWS/Azure. |
| **Công nghệ & Hệ thống** | **Khả thi cao.** Việc xây dựng custom stack (Next.js, FastAPI, PostgreSQL, Elasticsearch) là những công nghệ phổ biến, dễ tuyển dụng nhân sự và có tài liệu hỗ trợ phong phú. Pipeline OCR (Tesseract) và EPUB generator (Calibre/Pandoc) đều đã được chứng minh hiệu quả trong các dự án tương tự. |
| **Nguồn lực (Resource)** | **Khả thi.** Đội ngũ kỹ thuật 5 người có đầy đủ kỹ năng phát triển frontend, backend, OCR và thiết lập hạ tầng Cloud. Các thủ thư sẵn sàng tham gia kiểm thử nghiệp vụ và hiệu đính dữ liệu. |
| **Vận hành (Operational)** | **Khá tốt.** Hệ thống tự động hóa phần lớn quy trình OCR và đóng gói EPUB, giúp thủ thư giảm thiểu công việc thủ công. Tuy nhiên, thủ thư cần được đào tạo kỹ năng hiệu đính văn bản trên hệ thống. |
| **Lịch trình (Schedule)** | **Khả thi.** Lộ trình 7 tháng chia nhỏ thành các chặng (sprints), với phiên bản MVP ra mắt ở tháng thứ 4 giúp kiểm chứng sớm hiệu năng hệ thống và chất lượng OCR thực tế. |
| **Văn hóa (Cultural)** | **Tốt.** Bạn đọc trẻ tuổi thích ứng rất nhanh với việc đọc sách điện tử (EPUB) trực tuyến trên các thiết bị di động. |

---

## 2. SWOT & Benchmarking

### SWOT Analysis

| Điểm mạnh (Strengths) | Điểm yếu (Weaknesses) |
| --- | --- |
| • Custom stack linh hoạt, giao diện Next.js hiện đại.<br>• Hỗ trợ tự động OCR tiếng Việt và sinh EPUB.<br>• Phân quyền người dùng RBAC chặt chẽ.<br>• Tìm kiếm toàn văn Elasticsearch tốc độ cao.<br>• Tích hợp chatbot hỏi đáp thông minh (RAG Chatbot). | • OCR phụ thuộc lớn vào chất lượng ảnh quét thô đầu vào.<br>• Chi phí Cloud lưu trữ ảnh thô dung lượng lớn ban đầu.<br>• Chưa tích hợp thanh toán phạt trễ hạn. |
| **Cơ hội (Opportunities)** | **Thách thức (Threats)** |
| • Xu hướng chuyển đổi số thư viện toàn quốc.<br>• Tiết kiệm diện tích kho bãi vật lý cho thư viện.<br>• Khả năng mở rộng thành sản phẩm SaaS cho các thư viện khác. | • Rò rỉ tài liệu nếu người dùng cố tình bypass qua devtools trình duyệt.<br>• Chi phí dịch vụ cloud (băng thông, lưu trữ) tăng nhanh khi lượng bạn đọc đột biến. |

### Benchmarking

Phần lớn các thư viện đại học và thư viện công cộng tại Việt Nam hiện tại đang sử dụng các phần mềm thư viện số cũ như DSpace (ví dụ: VNU-LIC, Thư viện Tạ Quang Bửu) hoặc các phần mềm quản lý thư viện truyền thống (Koha). 

*   **Hạn chế của DSpace/Koha:** Chỉ hỗ trợ lưu trữ tệp đính kèm thô (thường là PDF dạng scan rất nặng), không hỗ trợ đọc trực tuyến bảo mật tốt, giao diện khó tùy biến trên thiết bị di động và hoàn toàn không có pipeline OCR tự động chuyển sang EPUB.
*   **Ưu thế của LibDMS:** Khắc phục triệt để các nhược điểm trên bằng giải pháp **Custom Modern Stack**. Tự động chuyển đổi tài liệu thô thành EPUB Reflowable giúp tối ưu hóa màn hình đọc, giảm dung lượng tệp tin tải xuống (chỉ bằng 10% so với PDF scan gốc) và cung cấp trình đọc trực tuyến bảo mật cao cùng chatbot hỏi đáp RAG thông minh.

---

## 3. Kế hoạch Tài chính (Cost vs Budget)

### 3.1. Project Cost (CapEx, đầu tư một lần)

| Hạng mục | Cơ sở ước tính | USD |
| :--- | :--- | :---: |
| Phát triển phần mềm custom | Nhóm 5 kỹ sư kiêm nhiệm phát triển trong 5 tháng cốt lõi. | $35.000 – $60.000 |
| Thiết lập hạ tầng Cloud ban đầu | Đăng ký dịch vụ, cấu hình bảo mật VPC, Kubernetes, PostgreSQL. | $3.000 – $6.000 |
| Kiểm thử & Bảo mật (Pen-test) | Thuê đánh giá độc lập hiệu năng và lỗ hổng bảo mật. | $3.000 – $7.000 |
| Đào tạo & Chuyển giao | Video hướng dẫn, tài liệu vận hành và tập huấn thủ thư. | $1.000 – $3.000 |
| **Tổng Project Cost (chưa dự phòng)** | | **≈ $42.000–$76.000** |

### 3.2. Project Budget = Cost + Contingency Reserve

| Hạng mục | Cơ sở ước tính | USD |
| :--- | :--- | :---: |
| Dự phòng rủi ro phát sinh (~12%) | Chi phí dự phòng thay đổi phạm vi hoặc biến động giá. | $3.000 – $9.000 |
| **Tổng Project Budget (CapEx)** | **Cost + Dự phòng** | **≈ $45.000–$85.000** |

### 3.3. OpEx — Vận hành định kỳ (Hàng năm)

| Hạng mục | Cơ sở ước tính | USD/năm |
| :--- | :--- | :---: |
| Hạ tầng Cloud duy trì | Máy chủ EC2, PostgreSQL DB (bao gồm tệp nhị phân), Elasticsearch. | $4.000 – $8.000 |
| Bảo trì & Hỗ trợ kỹ thuật | Cập nhật bản vá bảo mật, vá lỗi ứng dụng định kỳ. | $3.000 – $7.000 |
| Băng thông & Email service | Chi phí Data Transfer Out cho bạn đọc và SMS/Email. | $1.000 – $3.000 |
| **Tổng OpEx** | | **≈ $8.000–$18.000** |

### 3.4. ROI & Phân tích điểm hòa vốn (Break-even Analysis)

Do hệ thống phục vụ công ích học thuật phi lợi nhuận trực tiếp, hiệu quả kinh tế được đánh giá qua mô hình **Cost Avoidance (Tiết kiệm và tránh chi phí)**:
*   **Tiết kiệm không gian kho bãi:** Số hóa 20.000 tài liệu giúp giảm áp lực kho kệ vật lý, thu hồi khoảng 100m² không gian phòng đọc thư viện (giá trị tương đương **$3.500/năm**).
*   **Tối ưu hóa nhân sự:** Quy trình mượn/trả tự động hóa giúp giảm tải 80% thời gian xử lý thủ công của thủ thư, tiết kiệm tương đương **$4.000/năm** chi phí giờ công lao động.
*   **Điểm hòa vốn:** Với mức đầu tư CapEx trung bình $50.000 và OpEx $10.000/năm, lợi ích quy đổi về mặt không gian và nhân lực ước tính khoảng $15.000/năm. Điểm hòa vốn kinh tế sẽ đạt được sau khoảng **5 - 6 năm** vận hành, đồng thời gia tăng đáng kể uy tín phục vụ bạn đọc của thư viện.

---

## 4. Quản trị Rủi ro

Dưới đây là các rủi ro kỹ thuật và vận hành được nhận diện:

| Nhóm rủi ro | Chi tiết rủi ro | Mức độ | Biện pháp giảm thiểu | Risk Owner |
| :--- | :--- | :---: | :--- | :--- |
| **Chất lượng OCR** | Bản scan quá cũ hoặc chữ viết tay làm OCR sai lệch nghiêm trọng. | **Cao** | Hệ thống tự động cảnh báo độ tin cậy thấp, yêu cầu thủ thư hiệu đính thủ công qua màn hình Dashboard; mặc định dùng Fixed-Layout cho tài liệu kém chất lượng. | **Technical Lead** |
| **Rò rỉ tài liệu** | Bạn đọc dùng tool download để lấy file EPUB trực tiếp. | **Trung bình** | Sử dụng Stream API bảo mật có xác thực token, mã hóa DRM cơ bản cho tệp EPUB được phục vụ trực tiếp từ database PostgreSQL. | **Security Engineer** |
| **Chi phí Cloud tăng nhanh** | Băng thông mượn đọc sách số lớn làm chi phí cloud EC2/PostgreSQL vượt ngân sách. | **Trung bình** | Áp dụng CDN (CloudFront/Cloudflare) để cache file EPUB tĩnh, tối ưu hóa kích thước ảnh nén và thiết lập cảnh báo vượt ngưỡng dung lượng lưu trữ trên AWS/Azure. | **DevOps Engineer** |
| **Sự chấp nhận của thủ thư** | Cán bộ thư viện ngại sử dụng công cụ OCR và mượn/trả trực tuyến mới. | **Trung bình** | Tổ chức đào tạo cuốn chiếu, khen thưởng các cán bộ số hóa xuất sắc, cử nhân viên kỹ thuật hỗ trợ trực tiếp tại quầy trong tháng đầu go-live. | **Project Manager** |

---

## 5. Cấu trúc Báo cáo Khả thi — Tổng kết

*   **Mục đích:** Đánh giá tính khả thi kinh tế, kỹ thuật, pháp lý của dự án LibDMS trước khi Ban giám đốc Thư viện phê duyệt ngân sách đầu tư toàn phần.
*   **Kết luận nghiên cứu:** Dự án hoàn toàn khả thi về mặt kỹ thuật nhờ sử dụng Next.js, FastAPI và OCR Tesseract. Khía cạnh pháp lý được bảo đảm qua hệ thống phân quyền RBAC và cơ chế đọc trực tuyến bảo mật. Lợi ích kinh tế quy đổi (Cost Avoidance) đạt điểm hòa vốn sau 5 năm.
*   **Khuyến nghị:** Phê duyệt triển khai dự án bắt đầu từ Giai đoạn 0 (Khảo sát thiết kế) để chốt kiến trúc hạ tầng Cloud và định vị chất lượng OCR trên tập tài liệu mẫu thực tế.

---

## 6. Vì sao cần Feasibility Study

Tài liệu Feasibility Study giúp ban giám đốc thư viện:
1.  **Nhìn rõ bức tranh tài chính:** Tránh rủi ro phát sinh chi phí cloud đột biến bằng cách hoạch định rõ cơ chế Lifecycle policy cho dữ liệu ảnh quét.
2.  **Giảm rủi ro kỹ thuật:** Xác định rõ giới hạn của công nghệ OCR Tesseract đối với chữ tiếng Việt và thiết lập sẵn luồng hiệu đính thủ công (Correction workflow) để đảm bảo chất lượng EPUB Reflowable đầu ra.
3.  **Bảo vệ tài sản trí tuệ:** Định hình các lớp bảo mật ngay từ khâu thiết kế kiến trúc để chống cào quét dữ liệu.
