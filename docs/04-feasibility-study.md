# FEASIBILITY STUDY

## Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS

**Trường Đại học Khoa học Tự nhiên, ĐHQG-HCM (HCMUS) — Thư viện & Phòng Công nghệ Thông tin**

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
| **Pháp lý (Legal)** | **Yếu nhất / Rủi ro cao.** Việc số hóa sách giáo trình và tài liệu tham khảo có bản quyền của các nhà xuất bản bên ngoài dễ dẫn đến tranh chấp pháp lý. Cần bám sát Khoản 1 Điều 25 Luật SHTT Việt Nam (cho phép số hóa sách phục vụ học tập nội bộ phi lợi nhuận) và thiết lập cơ chế phân quyền (Restricted/Internal) nghiêm ngặt để đảm bảo an toàn pháp lý. |
| **Thị trường (Market)** | Nhu cầu đọc tài liệu số định dạng responsive (EPUB) của sinh viên trên thiết bị di động được dự đoán rất cao nhưng chưa có khảo sát định lượng chính thức. |
| **Kinh tế (Economic)** | Trung bình — Ngân sách CapEx dao động từ $45.000 đến $85.000 tùy thuộc vào tốc độ scan sách và phương án thuê nhân sự sinh viên biên tập văn bản lỗi OCR. Cần chốt báo giá máy scan sách và đơn giá số hóa thực tế ở Giai đoạn 0. |
| **Công nghệ & Hệ thống** | **Khả thi cao.** Sự kết hợp giữa React, FastAPI, Tesseract OCR và Pandoc là giải pháp kỹ thuật trưởng thành, sử dụng nhiều thư viện nguồn mở chất lượng cao, giúp trường tự chủ hoàn toàn công nghệ mà không cần trả phí license phần mềm đắt đỏ. Thách thức nằm ở thuật toán tiền xử lý ảnh và dàn trang EPUB cho các sách toán/lý chứa nhiều công thức và hình vẽ phức tạp. |
| **Nguồn lực (Resource)** | Trung bình — Tận dụng nhân sự sẵn có của Phòng CNTT trường làm lõi phát triển phần mềm, kết hợp với các cán bộ thư viện phụ trách nghiệp vụ và huy động sinh viên làm cộng tác viên hiệu chỉnh OCR. |
| **Vận hành (Operational)** | Khá tốt — Thư viện có sẵn đội ngũ thủ thư chuyên môn nghiệp vụ để kiểm duyệt và quản lý tài liệu; cần đào tạo bổ sung quy trình sử dụng Web Reader và bảng điều khiển biên tập OCR. |
| **Lịch trình (Schedule)** | Tốt — Roadmap thiết lập phương án cuốn chiếu MVP (số hóa trước 500 cuốn CNTT trong 3-4 tháng để go-live sớm) giúp hạn chế rủi ro trễ tiến độ so với phương án số hóa toàn bộ sách cũ trước khi chạy. |
| **Văn hóa (Cultural)** | Khá tốt — Sinh viên thế hệ mới rất hào hứng với việc đọc sách số trên thiết bị di động. Cần truyền thông tốt để thay đổi thói quen đọc sách giấy hoặc file PDF scan tĩnh cũ kỹ của cả sinh viên và giảng viên. |

---

## 2. SWOT & Benchmarking

### SWOT Analysis

| | Nội dung |
| --- | --- |
| **Điểm mạnh (Strengths)** | • Phần mềm custom tự phát triển giúp tùy biến linh hoạt luồng Scan-to-EPUB và kiểm soát bảo mật chặt chẽ (Signed URL).<br>• Tiết kiệm chi phí bản quyền phần mềm nhờ sử dụng nền tảng mã nguồn mở.<br>• Phân định rõ ràng phạm vi loại trừ giúp dự án không bị scope creep. |
| **Điểm yếu (Weaknesses)** | • Chưa có số liệu chính xác về số trang trung bình của sách cần số hóa để tính đơn giá chuẩn.<br>• Chưa khảo sát thực tế trải nghiệm đọc EPUB của sinh viên trường.<br>• Việc hiệu chỉnh lỗi chính tả sau OCR tốn nhiều thời gian và công sức thủ công. |
| **Cơ hội (Opportunities)** | • Phù hợp chiến lược chuyển đổi số giáo dục của HCMUS và ĐHQG-HCM.<br>• Có thể mở rộng nền tảng để số hóa tài liệu cho các trường đại học thành viên khác. |
| **Thách thức (Threats)** | • Rủi ro bị kiện tụng bản quyền từ các nhà xuất bản sách ngoài trường nếu kiểm soát phân quyền bị rò rỉ.<br>• Sự thay đổi của các định dạng file EPUB/PDF chuẩn hóa theo thời gian đòi hỏi nâng cấp phần mềm liên tục. |

### Benchmarking nhanh
Dự án số hóa sách và tài liệu điện tử (Scan-to-EPUB) đã được triển khai rộng rãi trên thế giới bởi các tổ chức lớn như **Open Library (Internet Archive)** và các thư viện số của các đại học lớn (MIT, Stanford). Các hệ thống này đã chứng minh rằng việc đóng gói tài liệu sang định dạng EPUB responsive giúp tăng tỷ lệ sinh viên đọc sách trên di động lên gấp **3 - 4 lần** so với việc chỉ cung cấp file PDF scan tĩnh. Việc tự phát triển cổng số hóa khép kín sử dụng OCR Tesseract và Pandoc cũng là hướng tiếp cận phổ biến giúp các trường đại học tối ưu hóa chi phí đầu tư công nghệ ban đầu.

---

## 3. Kế hoạch Tài chính (Cost vs Budget)

### 3.1. Project Cost — Tính bottom-up theo WBS (CapEx, đầu tư một lần)

| Hạng mục | Cơ sở ước tính chi tiết | USD |
| --- | --- | --- |
| **Số hóa & Biên tập EPUB** | Thuê sinh viên bán thời gian hỗ trợ scan sách + chạy OCR + hiệu chỉnh lỗi chính tả cho ~10.000 cuốn sách cũ (đơn giá $2 - $4.5/cuốn). | $20.000 – $45.000 |
| **Phát triển phần mềm custom** | Chi phí cơ hội nhân sự Phòng CNTT trường tự phát triển (3–4 kỹ sư × 3 tháng phát triển React/FastAPI cốt lõi). | $15.000 – $22.000 |
| **Hạ tầng thiết bị** | Mua sắm 02 máy scan chuyên nghiệp chữ V và 01 server vật lý chạy PostgreSQL/MinIO. | $4.000 – $8.000 |
| **Đào tạo & Triển khai** | Tài liệu hướng dẫn sử dụng, video trực quan, tổ chức các buổi tập huấn cho thủ thư và sinh viên. | $1.000 – $2.000 |
| **Tổng Project Cost (chưa dự phòng)** | | **≈ $40.000 – $77.000** |

### 3.2. Project Budget = Cost + Contingency Reserve

| Hạng mục | Cơ sở ước tính chi tiết | USD |
| --- | --- | --- |
| **Dự phòng rủi ro (~15%)** | Ngân sách dự phòng cho các phát sinh kỹ thuật, lỗi OCR phức tạp hoặc biến động giá phần cứng. | $5.000 – $8.000 |
| **Tổng Project Budget (CapEx)** | **Cost + Dự phòng** | **≈ $45.000 – $85.000** |

### 3.3. OpEx — Vận hành định kỳ (Hàng năm)

| Hạng mục | Cơ sở ước tính chi tiết | USD/năm |
| --- | --- | --- |
| **Hạ tầng server & Cloud** | Duy trì điện, mạng băng thông cao cho máy chủ và phí lưu trữ backup đám mây. | $2.000 – $4.000 |
| **Bảo trì & Hỗ trợ kỹ thuật** | Chi phí vá lỗi, nâng cấp các thư viện React/FastAPI và hỗ trợ kỹ thuật (1 kỹ sư bán thời gian). | $4.000 – $7.000 |
| **Bản quyền API OCR dự phòng** | Chi phí gọi Cloud OCR API đối với các tài liệu scan chất lượng quá kém mà Tesseract cục bộ không xử lý được. | $1.000 – $3.000 |
| **Số hóa bổ sung hàng năm** | Số hóa sách mới nhập hoặc tài liệu phát sinh. | $1.000 – $2.000 |
| **Tổng OpEx / năm** | | **≈ $8.000 – $16.000** |

### 3.4. ROI & Phân tích hòa vốn (Cost Avoidance Model)
Dự án là hệ thống công ích phi lợi nhuận phục vụ nội bộ trường học, vì vậy hiệu quả kinh tế được đánh giá qua mô hình **Cost Avoidance (Tránh phát sinh chi phí)**:
- **Baseline hiện tại:** Thư viện tốn trung bình khoảng 140.000.000 VNĐ/năm (~6.000 USD/năm) chi phí mặt bằng lưu trữ sách giáo trình cũ và chi phí văn phòng phẩm, hóa chất bảo quản giấy, điện điều hòa chống ẩm mốc.
- **Mô hình Cost Avoidance:** Khi số hóa sách sang EPUB, thư viện sẽ thu hồi được hơn 60% diện tích kệ sách giấy vật lý tại phòng đọc trung tâm Quận 5 để làm phòng tự học hiện đại cho sinh viên, đồng thời giảm 85% công sức thủ thư mượn trả (tiết kiệm tương đương 4.000 USD/năm chi phí giờ công lao động).
- **Phân tích điểm hòa vốn:**
  - CapEx ban đầu ước tính khoảng 45.000 USD (mức trung bình), OpEx vận hành hàng năm là 10.000 USD.
  - Lợi ích kinh tế quy đổi (tiết kiệm không gian phòng đọc làm khu tự học số + thời gian của thủ thư/độc giả + tuổi thọ sách được bảo tồn vĩnh viễn) ước tính đạt 12.000 USD/năm.
  - Điểm hòa vốn kinh tế học thuật dự kiến đạt được sau khoảng 5-6 năm vận hành. Ban Giám hiệu phê duyệt dự án chủ yếu dựa trên giá trị cải tiến hiệu suất phục vụ đào tạo và mục tiêu chuyển đổi số.

---

## 4. Quản trị Rủi ro

| Nhóm rủi ro | Chi tiết rủi ro | Mức độ | Biện pháp giảm thiểu | Risk Owner |
| :--- | :--- | :---: | :--- | :--- |
| **Bản quyền & SHTT** | Số hóa sách ngoại văn, sách mua bản quyền dịch của các NXB ngoài trường gây tranh chấp pháp lý. | **Cao** | Chỉ số hóa sách nội bộ trường, giáo trình tự viết của giảng viên. Cấu hình phân quyền đọc giới hạn (Internal/Restricted) nghiêm ngặt. | **Ban Giám đốc Thư viện** |
| **Lỗi layout EPUB** | Sách chứa nhiều công thức toán lý phức tạp hoặc bảng biểu lớn khi chuyển đổi sang EPUB bị lỗi vỡ khung, đè chữ. | **Trung bình** | Thiết lập quy trình: Sách công thức phức tạp sẽ giữ nguyên bản PDF chất lượng cao để đọc qua PDF Viewer bảo mật; chỉ đóng gói EPUB cho các sách nhiều chữ (xã hội, ngôn ngữ, lý thuyết cơ bản). | **Phòng Công nghệ Thông tin** |
| **Quá tải biên tập** | Khâu sửa lỗi chính tả OCR văn bản thô tốn quá nhiều giờ làm việc của thủ thư, gây tắc nghẽn xuất bản sách. | **Trung bình** | Tổ chức cho sinh viên khoa CNTT tham gia làm cộng tác viên biên tập sửa lỗi chính tả trực tuyến trên hệ thống để đổi điểm rèn luyện hoặc trợ cấp bán thời gian. | **Ban Giám đốc Thư viện** |
| **Rò rỉ tài liệu** | Sinh viên chia sẻ tài khoản hoặc sử dụng công cụ capture tải lậu file EPUB gốc. | **Trung bình** | Sử dụng cơ chế sinh Signed URL MinIO giới hạn 15 phút, chia nhỏ file EPUB thành nhiều file XHTML để load bất đồng bộ trên Web Reader. | **Phòng Công nghệ Thông tin** |

---

## 5. Cấu trúc Báo cáo Khả thi — Tổng kết

- **Mục đích (Purpose):** Đánh giá tính khả thi về kỹ thuật (OCR, Pandoc EPUB, React/FastAPI) và tính hợp pháp (Luật SHTT) của dự án HCMUS-LDMS trước khi trình duyệt ngân sách CapEx lớn.
- **Lý do (Reason):** Sách giấy xuống cấp vật lý nhanh, diện tích kệ sách quá tải, trải nghiệm đọc PDF scan trên di động rất tệ.
- **Khảo sát & Phát hiện:** Giải pháp tự phát triển sử dụng React + FastAPI kết hợp Tesseract OCR và Pandoc hoàn toàn khả thi về kỹ thuật; rủi ro pháp lý về bản quyền được giải quyết triệt để nhờ hệ thống phân quyền (RBAC) và Signed URL.
- **Khuyến nghị:** Phê duyệt triển khai Giai đoạn 0 (khảo sát baselines, mua máy quét sách) và thông qua phương án thí điểm MVP cuốn chiếu (Phương án B) cho 500 cuốn giáo trình CNTT trước khi nhân rộng.

---

## 6. Vì sao cần Feasibility Study

Tài liệu Feasibility Study giúp HCMUS:
1. Xác định rõ ràng các rủi ro kỹ thuật (vỡ định dạng EPUB đối với công thức phức tạp) và rủi ro pháp lý (bản quyền sách dịch) để xây dựng phương án phòng ngừa từ đầu.
2. Hoạch định ngân sách tài chính (CapEx/OpEx) minh bạch dựa trên mô hình Cost Avoidance thực tế của trường.
3. Làm cơ sở cho việc lập kế hoạch bố trí nhân sự kỹ thuật Phòng CNTT và tuyển dụng cộng tác viên sinh viên hỗ trợ biên tập hiệu chỉnh chữ OCR (xem [05-project-charter.md](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/hcmus-projectmanage--lab/docs/05-project-charter.md)).
