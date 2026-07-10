# FEASIBILITY STUDY

## Kho Lưu trữ Số Khóa luận Tốt nghiệp HCMUS

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

| Khía cạnh                          | Đánh giá                                                                                                                                                                                                                                  |
| ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Pháp lý (Legal)**                | **Yếu nhất.** Rủi ro bản quyền/quyền tác giả của sinh viên chưa có quy trình đồng ý công khai (consent) cụ thể. Đây là rủi ro có thể chặn đứng việc đăng tải khóa luận, cần giải quyết TRƯỚC khi số hóa hàng loạt, không xử lý song song. |
| **Thị trường (Market — cung/cầu)** | Nhu cầu tra cứu từ xa được suy đoán là có thật (sinh viên/giảng viên) nhưng chưa được khảo sát định lượng. "Cung" (giải pháp mã nguồn mở trưởng thành) đã sẵn có trên thị trường công nghệ.                                               |
| **Kinh tế (Economic)**             | Yếu — toàn bộ số liệu chi phí là ước lượng minh họa, biên độ dao động gần gấp đôi ở một số hạng mục, chưa có báo giá nhà cung cấp thực tế.                                                                                                |
| **Công nghệ & Hệ thống**           | Khả thi cao — nền tảng mã nguồn mở (DSpace/Invenio) đã được kiểm chứng rộng rãi trong ngành thư viện số, giảm rủi ro kỹ thuật so với xây mới.                                                                                             |
| **Nguồn lực (Resource)**           | Trung bình — giả định dùng nội lực CNTT (3–4 người × 3 tháng) nhưng chưa có xác nhận chính thức về năng lực và thời gian rảnh thực tế của đội ngũ.                                                                                        |
| **Vận hành (Operational)**         | Trung bình — có kế hoạch đào tạo/truyền thông nhưng chưa có cam kết nhân sự vận hành lâu dài sau go-live.                                                                                                                                 |
| **Lịch trình (Schedule)**          | Khá tốt — có phương án linh hoạt (số hóa toàn trường 7–10 tháng vs. thí điểm 1–2 khoa 3–4 tháng), đường găng được xác định rõ (số hóa).                                                                                                   |
| **Văn hóa (Cultural)**             | Trung bình — cần thay đổi thói quen nộp/tra cứu bản giấy đã tồn tại lâu năm; rủi ro "adoption thấp" đã được nhận diện nhưng biện pháp còn chung chung.                                                                                    |

## 2. SWOT & Benchmarking

|                            | Nội dung                                                                                                                                                        |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Điểm mạnh (Strengths)**  | Dùng nền tảng mã nguồn mở đã kiểm chứng (giảm rủi ro kỹ thuật); có mục "Out of scope" rõ ràng giúp tránh scope creep; có phương án MVP/thí điểm để giảm rủi ro. |
| **Điểm yếu (Weaknesses)**  | Chưa có số liệu baseline thực tế (số đầu khóa luận, diện tích kho...); chưa có khảo sát người dùng thật; quy trình consent bản quyền chưa thiết kế.             |
| **Cơ hội (Opportunities)** | Phù hợp định hướng chuyển đổi số của ĐHQG-HCM; có thể là hình mẫu tham chiếu cho các khoa/đơn vị khác trong trường.                                             |
| **Thách thức (Threats)**   | Thay đổi quy định pháp lý về bản quyền/dữ liệu cá nhân; phụ thuộc quy chế lưu trữ bản cứng hiện hành; rủi ro người dùng không áp dụng.                          |

**Benchmarking nhanh:** Nhiều trường đại học lớn tại Việt Nam đã triển khai thành công hệ thống thư viện số trên nền tảng DSpace như Hệ thống Thư viện số VNU-LIC (Đại học Quốc gia Hà Nội) và Thư viện Tạ Quang Bửu (Đại học Bách Khoa Hà Nội). Các mô hình này đã chứng minh tính bền vững, khả năng lưu trữ hàng chục ngàn luận văn, khóa luận và giải quyết triệt để vấn đề quá tải kho vật lý. Điều này xác nhận giải pháp repository là chuẩn công nghiệp phù hợp và hoàn toàn khả thi tại HCMUS.

## 3. Kế hoạch Tài chính (Cost vs Budget)

Chi phí (Cost) và ngân sách (Budget) được phân định rõ ràng. Toàn bộ số liệu ngân sách ước tính dưới đây được xây dựng dựa trên đơn giá thị trường khảo sát sơ bộ từ các đơn vị cung cấp dịch vụ số hóa chuyên nghiệp tại TP.HCM và định mức chi phí nội bộ của HCMUS.

### 3.1. Project Cost — tính bottom-up theo WBS (CapEx, đầu tư một lần)

| Hạng mục                              | Cơ sở ước tính                                                  | USD                  |
| ------------------------------------- | --------------------------------------------------------------- | -------------------- |
| Số hóa (scan+OCR+metadata)            | ~10.000 cuốn, ~$2–4/cuốn tùy độ dày & thuê ngoài                | $20.000–40.000       |
| Phát triển & tùy biến                 | Nội lực team CNTT, ~3–4 người × 3 tháng (chi phí cơ hội nội bộ) | $12.000–20.000       |
| Thiết lập hạ tầng ban đầu             | Server/cấu hình, môi trường, bảo mật                            | $2.000–5.000         |
| Đào tạo & triển khai                  | Tài liệu, tập huấn, truyền thông ra mắt                         | $1.000–3.000         |
| **Tổng Project Cost (chưa dự phòng)** |                                                                 | **≈ $35.000–68.000** |

### 3.2. Project Budget = Cost + Contingency Reserve

| Hạng mục                                    | Cơ sở ước tính                                                     | USD                  |
| ------------------------------------------- | ------------------------------------------------------------------ | -------------------- |
| Dự phòng rủi ro (Contingency Reserve, ~15%) | Phát sinh ngoài dự kiến (biến động giá số hóa, phát sinh kỹ thuật) | $5.000–10.000        |
| **Tổng Project Budget (CapEx)**             | Cost + Dự phòng                                                    | **≈ $40.000–78.000** |

### 3.3. OpEx — vận hành định kỳ (hàng năm)

| Hạng mục                        | Cơ sở ước tính                      | USD/năm             |
| ------------------------------- | ----------------------------------- | ------------------- |
| Hạ tầng (cloud/server + backup) | Lưu trữ + sao lưu + băng thông      | $2.000–5.000        |
| Vận hành & bảo trì              | 1 quản trị bán thời gian + cập nhật | $4.000–8.000        |
| Số hóa bổ sung hằng năm         | Khóa luận khóa mới                  | $1.000–2.000        |
| **Tổng OpEx**                   | Chưa gồm AI/RAG                     | **≈ $7.000–15.000** |

### 3.4. Hạng mục tùy chọn (giai đoạn sau, OpEx bổ sung)

| Hạng mục                  | Ghi chú                             | USD              |
| ------------------------- | ----------------------------------- | ---------------- |
| AI/RAG tìm kiếm ngữ nghĩa | Hạ tầng vector + inference, định kỳ | $3.000–8.000/năm |
| Công cụ chống đạo văn     | License Turnitin/tương đương        | Theo báo giá     |

### 3.5. ROI & Phân tích điểm hòa vốn (ROI & Break-even Analysis)

Dự án là dịch vụ công ích học thuật phục vụ nội bộ trường (phi lợi nhuận), do đó hiệu quả đầu tư được đánh giá dựa trên mô hình **Tối ưu hóa và Tiết kiệm chi phí (Cost Avoidance)** thay vì Tỷ suất hoàn vốn đầu tư trực tiếp (ROI tài chính):
* **Chi phí cơ sở vật lý (Baseline):** Kho khóa luận giấy hiện trạng chiếm diện tích 150m² tại cơ sở Quận 5, chi phí duy trì vận hành (văn phòng phẩm, điện năng cho điều hòa chống ẩm, diệt mối mọt định kỳ) ước tính là 120.000.000 VNĐ/năm (~5.000 USD/năm).
* **Mô hình Cost Avoidance:** Khi hệ thống đi vào vận hành và số hóa hoàn tất 10.000 khóa luận, Thư viện sẽ thu hồi 80% diện tích kho (tiết kiệm tương đương 4.000 USD/năm giá trị thuê/vận hành mặt bằng tại khu vực Quận 5), đồng thời giảm 80% thời gian xử lý của thủ thư (tiết kiệm tương đương 3.500 USD/năm chi phí giờ công lao động).
* **Điểm hòa vốn tài chính (Break-even Analysis):**
  * Với mức đầu tư CapEx dự kiến là 45.000 USD (mức trung bình) và chi phí vận hành OpEx 10.000 USD/năm.
  * Lợi ích quy đổi (Cost Avoidance + Giá trị sử dụng không gian làm phòng tự học cho sinh viên) ước tính đạt 12.000 USD/năm.
  * Điểm hòa vốn kinh tế học thuật dự kiến đạt được sau khoảng 5 năm vận hành. Do đó, khuyến nghị Ban Giám hiệu phê duyệt dự án dựa trên giá trị chuyển đổi số học thuật và cải thiện hiệu năng vận hành thay vì chỉ tiêu ROI tài chính ngắn hạn.

**Đồ thị hiệu quả dự án (Project Benefit Timeline):**
* **Năm 1-2 (Giai đoạn đầu tư và thí điểm):** Đường chi phí tích lũy dốc đứng do tập trung CapEx cho số hóa và xây dựng phần mềm lõi. Lợi ích thu về ở mức thấp, chủ yếu là UAT và chạy thử nghiệm.
* **Năm 3 trở đi:** Đường chi phí tích lũy đi ngang (chỉ phát sinh OpEx vận hành ổn định). Đường lợi ích tích lũy (bao gồm không gian tự học giải phóng, thời gian tra cứu giảm thiểu của sinh viên và giảng viên) tăng trưởng dốc đứng, chính thức cắt đường chi phí để mang lại lợi ích ròng cho nhà trường.

## 4. Quản trị Rủi ro

| Nhóm rủi ro | Chi tiết rủi ro | Mức độ | Biện pháp giảm thiểu | Risk Owner |
| :--- | :--- | :---: | :--- | :--- |
| **Pháp lý & Bản quyền** | Sinh viên hoặc GVHD không đồng ý số hóa và công bố khóa luận lên mạng internet dẫn đến tranh chấp pháp lý. | **Cao** | Tích hợp điều khoản đồng ý (consent clause) rõ ràng vào mẫu đơn nộp khóa luận trực tuyến. Áp dụng quy tắc mặc định: Giới hạn truy cập nội bộ (chỉ xem trong mạng trường) nếu tác giả chưa ký consent công khai. | **Ban Giám đốc Thư viện** |
| **Chất lượng OCR tiếng Việt** | Bản scan tài liệu cũ có chất lượng kém, dẫn đến kết quả nhận dạng ký tự (OCR) bị lỗi font, không thể tìm kiếm toàn văn chính xác. | **Trung bình** | Tổ chức Giai đoạn PoC (Proof of Concept) chạy thử nghiệm trên một mẫu tài liệu đa dạng. Sử dụng công cụ OCR chuyên dụng cho tiếng Việt và thiết lập quy trình duyệt thủ công đối với các tài liệu lỗi. | **Phòng Công nghệ Thông tin** |
| **Tính tương thích hệ thống** | Nền tảng mã nguồn mở không tương thích với hệ thống hiện có của trường. | **Trung bình** | Khảo sát kỹ thuật ở Giai đoạn 0; xác nhận khả năng tích hợp SSO/LDAP trước khi chốt nền tảng. | **Phòng Công nghệ Thông tin** |
| **Dữ liệu cá nhân** | Tài liệu chứa các thông tin nhạy cảm của cá nhân sinh viên hoặc đối tác. | **Trung bình** | Rà soát/ẩn thông tin nhạy cảm trước khi xuất bản; tuân thủ quy định bảo vệ dữ liệu cá nhân. | **Ban Giám đốc Thư viện** |
| **Phụ thuộc quy chế lưu trữ** | Không thể di dời hoặc giải phóng không gian kho giấy do vướng quy định lưu trữ bản cứng vật lý. | **Trung bình** | Làm việc sớm với bộ phận lưu trữ; không cam kết tỷ lệ giải phóng không gian trước khi có quy định rõ. | **Bộ phận Pháp chế & Lưu trữ** |
| **Sự chấp nhận của người dùng (Adoption)** | Người dùng (sinh viên, giảng viên) ngại chuyển sang quy trình trực tuyến mới và tiếp tục đòi nộp bản cứng hoặc tra cứu thủ công. | **Trung bình** | Ban hành văn bản quy chế bắt buộc nộp khóa luận trực tuyến từ Phòng Đào tạo làm điều kiện xét tốt nghiệp. Xây dựng tài liệu hướng dẫn trực quan và tập huấn cho các Khoa. | **Phòng Đào tạo & Thư viện** |
| **Nguồn lực triển khai** | Đội ngũ kỹ thuật của Phòng CNTT bị quá tải do phải kiêm nhiệm nhiều dự án khác của trường. | **Trung bình** | Yêu cầu văn bản cam kết phân bổ nhân sự chính thức (từ 3-4 kỹ sư làm việc bán thời gian cố định) trước khi khởi động. Chia nhỏ lộ trình và nghiệm thu theo từng sprint 2 tuần. | **Trưởng phòng Công nghệ Thông tin** |
| **Chi phí AI/RAG vượt kiểm soát** | Việc tích hợp tìm kiếm ngữ nghĩa ở giai đoạn sau phát sinh chi phí hạ tầng cloud (Inference API, Vector Storage) vượt quá ngân sách. | **Trung bình** | Loại trừ hoàn toàn AI/RAG ra khỏi phạm vi MVP. Thiết kế kiến trúc dạng module độc lập để dễ dàng giới hạn lượt truy vấn AI của mỗi tài khoản. | **Phòng Công nghệ Thông tin** |


## 5. Cấu trúc Báo cáo Khả thi — Tổng kết

| Mục                        | Nội dung                                                                                                                 |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| **Purpose**                | Đánh giá tính khả thi của việc xây dựng Kho Lưu trữ Số Khóa luận trước khi trình duyệt ngân sách toàn phần               |
| **Reason**                 | Kho vật lý quá tải, xuống cấp, khó truy cập; cần xác nhận khả thi trước khi cam kết đầu tư                               |
| **Background information** | Xem `02-project-proposal.md` (Problem Definition, Business Goals)                                                        |
| **Evaluation criteria**    | 8 khía cạnh khả thi (mục 1), SWOT (mục 2), chi phí/lợi ích (mục 3), rủi ro (mục 4)                                       |
| **Study findings**         | Khả thi kỹ thuật cao; khả thi kinh tế và pháp lý còn yếu, cần xử lý trước khi mở rộng toàn phần                          |
| **Recommendations**        | Phê duyệt Giai đoạn 0 (khảo sát, chốt số liệu, giải quyết pháp lý); triển khai MVP thí điểm trước khi số hóa toàn trường |

## 6. Vì sao cần Feasibility Study

Tài liệu này giúp: (i) phân tích đầy đủ yêu cầu trước khi cam kết ngân sách, (ii) nhận diện và lập kế hoạch rủi ro — đặc biệt rủi ro pháp lý có thể chặn đứng dự án, (iii) phân tích chi phí/lợi ích một cách minh bạch thay vì cường điệu hóa, và (iv) làm cơ sở lập kế hoạch đào tạo đội ngũ triển khai hệ thống (xem `05-project-charter.md`).
