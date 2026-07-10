# ĐỀ XUẤT DỰ ÁN (PROJECT PROPOSAL)

## Kho Lưu trữ Số Khóa luận Tốt nghiệp HCMUS
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

Trường Đại học Khoa học Tự nhiên (HCMUS) hiện đang lưu giữ hàng chục ngàn khóa luận tốt nghiệp của các thế hệ sinh viên hoàn toàn dưới dạng bản cứng (giấy). Phương thức lưu trữ truyền thống này hiện đang đối mặt với ba thách thức lớn: quá tải không gian kệ lưu trữ vật lý của thư viện, nguy cơ xuống cấp vật lý không thể phục hồi của tài liệu giấy theo thời gian, và quy trình tra cứu hoàn toàn thủ công tại chỗ khiến nguồn tài nguyên tri thức quý báu này gần như bị "đóng băng", không thể tiếp cận từ xa.

Tài liệu này đề xuất xây dựng hệ thống **Kho Lưu trữ Số Khóa luận Tốt nghiệp HCMUS (Digital Repository)**. Hệ thống sẽ số hóa, lưu trữ, quản lý tập trung và phân quyền truy cập linh hoạt đối với khóa luận tốt nghiệp, đồng thời cung cấp năng lực tìm kiếm toàn văn (Full-text Search). 

**Các kết quả chính mong đợi:**
*   Số hóa và đưa lên hệ thống toàn bộ kho khóa luận hiện có (~10.000+ cuốn) và 100% khóa luận mới từ khóa tốt nghiệp 2026.
*   Chuyển đổi quy trình nộp khóa luận của sinh viên và phê duyệt của Thư viện/Khoa sang hình thức trực tuyến 100%.
*   Rút ngắn thời gian tra cứu tài liệu từ trung bình 45 phút di chuyển và tìm thủ công xuống còn 3 giây trên hệ thống số.
*   Thiết lập cơ chế phân quyền truy cập an toàn (Công khai / Nội bộ mạng trường / Cấm vận có thời hạn) gắn liền với quy trình ký xác nhận đồng ý (consent) bản quyền của tác giả.

**Kế hoạch tài chính & Lộ trình:**
Dự án được đề xuất triển khai theo mô hình lai (Hybrid): kiểm soát gating theo 4 giai đoạn lớn (từ Giai đoạn 0 khảo sát đến Giai đoạn 3 nâng cao) kết hợp phát triển lặp Scrum cho phần kỹ thuật.
*   **Tổng chi phí đầu tư một lần (CapEx):** Ước tính từ **$40.000 đến $78.000** (trong đó chi phí quét và OCR chiếm tỷ trọng lớn nhất, khoảng 50%).
*   **Chi phí vận hành định kỳ (OpEx):** Ước tính từ **$7.000 đến $15.000/năm**.
*   **Các tính năng nâng cao (AI/RAG, Kiểm tra đạo văn):** Được tách thành các hạng mục tùy chọn ở giai đoạn sau nhằm giảm thiểu rủi ro ngân sách và kỹ thuật cho sản phẩm khả dụng tối thiểu (MVP).

**Khuyến nghị:** Ban Giám hiệu phê duyệt ngân sách và chủ trương triển khai **Giai đoạn 0 (Khảo sát & Chuẩn bị)** để chốt số liệu thực tế, ký duyệt quy chế bản quyền và hoàn tất báo giá nhà cung cấp. Sau đó, triển khai **MVP thí điểm cho 1-2 khoa** trước khi số hóa và áp dụng đại trà cho toàn trường nhằm tối ưu hóa chi phí và kiểm soát chất lượng thực tế.

---

## 2. Business case (Câu chuyện bối cảnh & Lý do đầu tư)

### 2.1. Câu chuyện từ thực tế vận hành

Để hiểu rõ vì sao dự án này không chỉ là một dự án phần mềm mà là một bước đi sống còn cho quản trị tri thức tại HCMUS, hãy nhìn vào trải nghiệm thực tế hàng ngày của hai bên thụ hưởng trực tiếp: sinh viên và cán bộ thư viện.

![Sơ đồ Hiện trạng (As-is) vs Tương lai (To-be)](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/docs/images/as_is_to_be_workflow.svg)

#### Câu chuyện thứ nhất: Cuộc hành trình gian nan của sinh viên Nguyễn Văn A
Nguyễn Văn A là sinh viên năm cuối Khoa Công nghệ Thông tin tại cơ sở Linh Trung (Thủ Đức). Để chuẩn bị đề tài tốt nghiệp về "Xử lý ngôn ngữ tự nhiên ứng dụng trong y tế", A cần tham khảo phương pháp luận của một khóa luận xuất sắc khóa trước. 
1.  **Di chuyển:** A phải bắt chuyến xe buýt dài hơn 15km trong thời tiết nắng nóng từ Linh Trung về cơ sở Nguyễn Văn Cừ (Quận 5), nơi đặt kho lưu trữ khóa luận giấy.
2.  **Tra cứu:** Đến nơi trong giờ hành chính, A phải tra cứu mã số trên cổng thông tin cũ kỹ, rồi điền phiếu yêu cầu bằng giấy.
3.  **Chờ đợi:** Cô thủ thư phải di chuyển vào sâu trong kho tối, lục tìm giữa hàng chục kệ gỗ bám đầy bụi để lấy ra cuốn khóa luận duy nhất.
4.  **Hạn chế tiếp cận:** Việc tra cứu phụ thuộc hoàn toàn vào một bản gốc độc nhất và A chỉ được phép đọc tại chỗ. A không được phép chụp hình, không được photocopy để bảo vệ bản quyền tác giả. A phải ngồi cắm cúi chép tay các đoạn công thức và thuật toán quan trọng suốt 3 tiếng đồng hồ. 
5.  **Mất mát vật lý:** Một tuần sau, khi A cần đối chiếu lại, cuốn khóa luận đó đã bị rách vài trang mục lục quan trọng do ẩm mốc và tần suất lật giở quá nhiều của các sinh viên khác. Nguồn tri thức học thuật quý giá đó đã bị hao mòn vật lý và không thể phục hồi.

#### Câu chuyện thứ hai: Áp lực vô hình của cô thủ thư Mai
Mỗi mùa tốt nghiệp, cô Mai – cán bộ thư viện lâu năm – lại đối mặt với một cơn ác mộng mang tên "tiếp nhận khóa luận". Hàng ngàn cuốn khóa luận tốt nghiệp bìa cứng mạ vàng của sinh viên các khoa đổ về. 
1.  **Quá tải không gian:** Diện tích kho lưu trữ thư viện có hạn nhưng số lượng khóa luận lại tăng lên tuyến tính theo từng năm. Cô Mai bất lực nhìn những dãy kệ sách đã chật kín chỗ, phải xếp chồng tài liệu lên nhau dưới đất, tạo điều kiện cho ẩm mốc và mối mọt phát triển.
2.  **Thao tác thủ công:** Quy trình kiểm kê thông tin, đối chiếu danh sách tốt nghiệp của Phòng Đào tạo, nhập dữ liệu mô tả (metadata) thủ công vào hệ thống quản lý cũ ngốn của cô Mai và các đồng nghiệp hàng trăm giờ lao động mỗi kỳ. 
3.  **Rủi ro bản quyền:** Cô liên tục phải từ chối yêu cầu sao chép tài liệu của sinh viên vì không có văn bản chấp thuận sử dụng (consent) chính thức của tác giả, dẫn đến việc thư viện sở hữu tri thức nhưng không thể chia sẻ rộng rãi vì sợ vi phạm pháp lý.

### 2.2. Vấn đề được giải quyết như thế nào?

Ý tưởng xây dựng **Kho Lưu trữ Số Khóa luận Tốt nghiệp HCMUS** được đề xuất nhằm giải quyết triệt để các nút thắt trên thông qua một chu trình số hóa khép kín:

*   **Chuyển đổi quy trình nộp đầu vào:** Thay vì in ấn đóng tập bản cứng đắt đỏ, sinh viên nộp bản mềm PDF trực tiếp lên hệ thống kèm theo thông tin mô tả và ký cam kết đồng ý chia sẻ bản quyền (consent) bằng chữ ký số hoặc xác thực SSO trường. Cán bộ thư viện kiểm duyệt và xuất bản chỉ trong tích tắc.
*   **Dân chủ hóa khả năng truy cập:** Hệ thống tự động gán mã định danh bền vững (Handle/DOI nội bộ) cho từng khóa luận. Sinh viên và giảng viên có thể truy cập hệ thống 24/7 từ bất kỳ đâu, tìm kiếm toàn văn (Elasticsearch) từng từ khóa trong nội dung tài liệu, thay vì chỉ tìm được tựa đề hoặc tên tác giả như trước đây.
*   **Bảo vệ bản quyền thông qua phân quyền tự động:** Hệ thống tự động áp dụng mức phân quyền (Công khai / Nội bộ / Embargo) dựa trên sự lựa chọn consent hợp pháp của tác giả lúc nộp bài, đảm bảo tính pháp lý tối đa cho Nhà trường.
*   **Tối ưu hóa không gian và bảo tồn vĩnh viễn:** Chuyển đổi khối tài liệu giấy tĩnh chiếm diện tích lớn thành kho dữ liệu số được sao lưu an toàn trên Cloud/Server của trường. Kho giấy vật lý có thể được di dời về kho lưu trữ thứ cấp giá rẻ hoặc giải phóng để làm không gian tự học hiện đại cho sinh viên.

---

## 3. Giải pháp đề xuất

### 3.1. Mô tả tổng quan

Giải pháp đề xuất là xây dựng một nền tảng **Digital Repository** chuyên dụng cho khóa luận tốt nghiệp đại học của HCMUS, đóng vai trò là kho lưu trữ tri thức số tập trung của nhà trường. Hệ thống quản lý toàn bộ vòng đời của một khóa luận từ khâu sinh viên nộp trực tuyến, qua khâu kiểm duyệt nghiệp vụ của Thư viện, đến lưu trữ bảo mật và phục vụ tra cứu toàn văn của độc giả trong và ngoài trường.

### 3.2. Năng lực cốt lõi (Core Capabilities)

*   **Workflow nộp & duyệt trực tuyến (Online Submission & Approval):** 
    *   Sinh viên nộp khóa luận (file PDF) cùng thông tin metadata trực tuyến.
    *   Cán bộ thư viện kiểm duyệt chất lượng metadata trước khi cho phép xuất bản lên kho số.
*   **Lưu trữ metadata chuẩn hóa:** Sử dụng chuẩn quốc tế **Dublin Core** để mô tả dữ liệu học thuật. Gắn mã định danh bền vững (**Handle/DOI nội bộ**) để đảm bảo liên kết trích dẫn học thuật không bị lỗi (broken links) theo thời gian.
*   **Cơ chế Phân quyền truy cập 3 mức (Alternative):** Mỗi khóa luận tại một thời điểm chỉ ở đúng 1 trong 3 trạng thái phân quyền sau:
    1.  *Công khai (Public):* Cho phép tất cả người dùng trong và ngoài trường truy cập toàn văn.
    2.  *Nội bộ (Internal):* Chỉ cho phép người dùng đăng nhập bằng tài khoản SSO của trường (sinh viên, giảng viên hiện tại) xem và tải toàn văn.
    3.  *Hạn chế/Cấm vận (Embargo):* Tạm ẩn toàn văn trong một khoảng thời gian xác định (ví dụ: 12-36 tháng theo yêu cầu của tác giả để đăng ký sáng chế hoặc bảo mật thông tin doanh nghiệp hợp tác). Sau khi hết thời gian embargo, hệ thống tự động chuyển về mức Công khai hoặc Nội bộ theo cấu hình trước đó.
*   **Tìm kiếm toàn văn hiệu năng cao (Full-text Search):** Sử dụng Elasticsearch/OpenSearch để chỉ mục hóa (index) toàn văn nội dung của file PDF sau khi qua bộ lọc OCR tiếng Việt, cho phép tra cứu sâu vào nội dung bài viết thay vì chỉ tìm kiếm theo tiêu đề hay tác giả.
*   **Quản lý cam kết bản quyền (Consent Management):** Thu thập và lưu trữ minh chứng đồng ý số hóa và công bố khóa luận của sinh viên tại thời điểm nộp bài để làm cơ sở pháp lý cho việc hiển thị tài liệu.

### 3.3. Định hướng kiến trúc (Architectural Direction)

Kiến trúc hệ thống ưu tiên sử dụng mô hình **Modular Monolith** xây dựng trên nền tảng mã nguồn mở chuyên dụng đã trưởng thành, kết hợp với các dịch vụ vệ tinh độc lập cho tìm kiếm và AI/RAG.

![Mô hình kiến trúc hệ thống (System Architecture)](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/docs/images/system_architecture.svg)


*   **Nền tảng lõi (Core Repository):** Kế thừa **DSpace** (viết bằng Java/Spring) hoặc **Invenio** (viết bằng Python/Flask) thay vì phát triển mới hoàn toàn từ đầu (build from scratch). Lựa chọn này giúp tận dụng kinh nghiệm tối ưu hóa thư viện số của cộng đồng quốc tế và loại bỏ rủi ro bảo trì phần mềm sau bàn giao.
*   **Tách lớp Tìm kiếm:** Elasticsearch/OpenSearch chạy độc lập để lập chỉ mục toàn văn, đảm bảo truy vấn phản hồi nhanh dưới 3 giây ngay cả khi số lượng tài liệu lên tới hàng chục ngàn cuốn.
*   **Xác thực người dùng:** Tích hợp trực tiếp hệ thống SSO/LDAP hiện tại của HCMUS để người dùng không cần đăng ký tài khoản mới.
*   **Kiến trúc AI/RAG độc lập (Hạng mục tùy chọn giai đoạn 3):** Tách biệt dịch vụ tìm kiếm ngữ nghĩa (Semantic Search) sử dụng Vector Database và mô hình embedding hỗ trợ tiếng Việt để đảm bảo nếu dịch vụ AI gặp sự cố, hệ thống thư viện lõi vẫn vận hành bình thường.

### 3.4. Phạm vi loại trừ (Out of scope)

Để đảm bảo dự án triển khai đúng hạn và tập trung nguồn lực, các hạng mục sau đây được xác định nằm ngoài phạm vi dự án:
*   **Hệ thống phát hiện đạo văn chuyên dụng (như Turnitin/DoIT):** Đây là một hệ thống có bản quyền riêng biệt và chi phí rất lớn. Dự án chỉ xây dựng cổng API mở để sẵn sàng tích hợp với các hệ thống này ở giai đoạn sau, không bao gồm bản quyền hoặc việc xây dựng công cụ so khớp đạo văn riêng.
*   **Số hóa các loại tài liệu khác:** Không áp dụng số hóa giáo trình, luận văn thạc sĩ, luận án tiến sĩ hoặc sách tham khảo ở giai đoạn MVP.
*   **Tiêu hủy bản cứng:** Việc tiêu hủy hay di dời bản cứng ra khỏi kho vật lý thuộc thẩm quyền phê duyệt của quy chế văn thư lưu trữ quốc gia và nhà trường, không nằm trong phạm vi công nghệ của dự án này.

---

## 4. Phân tích Chi phí – Lợi ích (Cost-Benefit Analysis)

### 4.1. Ước tính chi phí (Investment)

Dự án phân tách rõ hai nguồn ngân sách: Chi phí đầu tư một lần (CapEx) phục vụ xây dựng hệ thống và số hóa kho dữ liệu cũ; Chi phí vận hành định kỳ (OpEx) phục vụ hạ tầng và bảo trì hàng năm.

![Phân rã Ngân sách Đầu tư một lần (CapEx)](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/docs/images/capex_breakdown.svg)

> [!NOTE]
> Ngân sách chi tiết được phân rã cụ thể tại [Mục 11. Ước tính chi phí (USD)](#11-ước-tính-chi-phí-usd) của tài liệu này.

### 4.2. Lợi ích định lượng & định tính

| Đối tượng thụ hưởng | Lợi ích định lượng | Lợi ích định tính |
| :--- | :--- | :--- |
| **Thư viện HCMUS** | • Thu hồi khoảng **60-80%** diện tích kho vật lý chứa khóa luận cũ (khi quy chế di dời được thông qua).<br>• Giảm **80%** giờ công của thủ thư cho việc quản lý nộp bài và tìm kiếm thủ công. | • Bảo tồn an toàn tri thức học thuật, tránh rủi ro cháy nổ, ẩm mốc tài liệu giấy.<br>• Quy trình hóa nghiệp vụ theo chuẩn quốc tế. |
| **Sinh viên & Giảng viên** | • Thời gian tra cứu tài liệu từ **45 phút** giảm xuống dưới **3 giây**.<br>• Tiếp cận tài liệu **24/7** từ xa mà không cần di chuyển vật lý. | • Nâng cao trải nghiệm học tập, nghiên cứu trực tuyến.<br>• Kích thích trao đổi học thuật, kế thừa các đề tài nghiên cứu xuất sắc. |
| **Ban Giám hiệu / Nhà trường** | • Cung cấp báo cáo thống kê phục vụ kiểm định chất lượng giáo dục (AUN-QA, HCERES). | • Khẳng định vị thế chuyển đổi số giáo dục.<br>• Tăng chỉ số trích dẫn và uy tín học thuật của HCMUS trên môi trường số. |

### 4.3. Đánh giá rủi ro và các điểm lưu ý trong kỳ vọng dự án

Để đảm bảo tính khả thi và khách quan khi trình Ban Giám hiệu phê duyệt, các kỳ vọng về hiệu quả dự án được làm rõ như sau:

> [!WARNING]
> **Về việc "Giải phóng không gian kho":** Số hóa tài liệu không đồng nghĩa với việc được phép tiêu hủy ngay lập tức bản cứng gốc. Theo quy chế lưu trữ hiện hành, bản cứng khóa luận vẫn phải lưu trữ tại chỗ hoặc kho lưu trữ dự phòng của nhà trường. Lợi ích thực tế ở đây cần được phát biểu là: **"Giải quyết áp lực quá tải kho trung tâm bằng cách chuyển các bản cứng sang kho lưu trữ thứ cấp giá rẻ hơn, đồng thời giải phóng diện tích tại thư viện Quận 5 để làm không gian số cho sinh viên."**

> [!IMPORTANT]
> **Về khái niệm "Lưu trữ vĩnh viễn":** Lưu trữ số không có nghĩa là không mất chi phí. Dữ liệu số luôn đòi hỏi sao lưu đa vị trí, bảo trì định kỳ, nâng cấp máy chủ vật lý và di trú dữ liệu khi các định dạng tệp cũ bị lỗi thời. Nhà trường cần xác định đây là hoạt động **"Bảo quản số dài hạn có kế hoạch và có chi phí vận hành OpEx liên tục hàng năm"**.

> [!CAUTION]
> **Về khả năng "Ngăn chặn đạo văn":** Bản thân hệ thống repository không có khả năng tự động chống đạo văn. Nó chỉ đóng vai trò là một **nguồn cơ sở dữ liệu tập trung, minh bạch làm đầu vào** để cung cấp cho các công cụ so khớp. Lợi ích chống đạo văn chỉ thực sự đạt được khi tích hợp thêm công cụ chuyên dụng (như Turnitin/DoIT) ở Giai đoạn 3 và ban hành quy chế học thuật đi kèm.

---

## 5. Rủi ro & Biện pháp giảm thiểu

Dưới đây là ma trận rủi ro trọng yếu được nhận diện kèm theo chủ sở hữu rủi ro (Risk Owner) chịu trách nhiệm theo dõi và xử lý:

| Nhóm rủi ro | Chi tiết rủi ro | Mức độ | Biện pháp giảm thiểu | Risk Owner |
| :--- | :--- | :--- | :--- | :--- |
| **Pháp lý & Bản quyền** | Sinh viên hoặc GVHD không đồng ý số hóa và công bố khóa luận lên mạng internet dẫn đến tranh chấp pháp lý. | **Cao** | • Tích hợp điều khoản đồng ý (consent clause) rõ ràng vào mẫu đơn nộp khóa luận trực tuyến.<br>• Áp dụng quy tắc mặc định: Giới hạn truy cập nội bộ (chỉ xem trong mạng trường) nếu tác giả chưa ký consent công khai. | **Ban Giám đốc Thư viện** |
| **Chất lượng OCR tiếng Việt** | Bản scan tài liệu cũ có chất lượng kém, dẫn đến kết quả nhận dạng ký tự (OCR) bị lỗi font, không thể tìm kiếm toàn văn chính xác. | **Trung bình** | • Tổ chức Giai đoạn PoC (Proof of Concept) chạy thử nghiệm trên một mẫu tài liệu đa dạng.<br>• Sử dụng công cụ OCR chuyên dụng cho tiếng Việt và thiết lập quy trình duyệt thủ công đối với các tài liệu lỗi. | **Phòng Công nghệ Thông tin** |
| **Sự chấp nhận của người dùng (Adoption)** | Người dùng (sinh viên, giảng viên) ngại chuyển sang quy trình trực tuyến mới và tiếp tục đòi nộp bản cứng hoặc tra cứu thủ công. | **Trung bình** | • Ban hành văn bản quy chế bắt buộc nộp khóa luận trực tuyến từ Phòng Đào tạo làm điều kiện xét tốt nghiệp.<br>• Xây dựng tài liệu hướng dẫn trực quan, video ngắn và tổ chức các buổi tập huấn cho các Khoa. | **Phòng Đào tạo & Thư viện** |
| **Nguồn lực triển khai** | Đội ngũ kỹ thuật của Phòng CNTT bị quá tải do phải kiêm nhiệm nhiều dự án khác của trường, dẫn đến trễ tiến độ. | **Trung bình** | • Yêu cầu văn bản cam kết phân bổ nhân sự chính thức (từ 3-4 kỹ sư làm việc bán thời gian cố định) trước khi khởi động dự án.<br>• Chia nhỏ lộ trình và nghiệm thu theo từng sprint 2 tuần để kiểm soát tiến độ sớm. | **Trưởng phòng Công nghệ Thông tin** |
| **Chi phí AI/RAG vượt kiểm soát** | Việc tích hợp tìm kiếm ngữ nghĩa ở giai đoạn sau phát sinh chi phí hạ tầng cloud (Inference API, Vector Storage) vượt quá ngân sách của trường. | **Trung bình** | • Loại trừ hoàn toàn AI/RAG ra khỏi phạm vi MVP.<br>• Thiết kế kiến trúc dạng module độc lập để dễ dàng bật/tắt hoặc giới hạn lượt truy vấn AI của mỗi tài khoản sinh viên. | **Phòng Công nghệ Thông tin** |

---

## 6. Lộ trình triển khai theo giai đoạn (Roadmap)

Dự án được đề xuất triển khai theo 4 giai đoạn rõ ràng với các điểm Gating (quyết định Go/No-go) tại cuối mỗi giai đoạn:

![Sơ đồ lộ trình triển khai theo giai đoạn](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/docs/images/project_roadmap.svg)

*   **Giai đoạn 0 — Khảo sát & Chuẩn bị (Tháng 1–2):**
    *   *Trọng tâm:* Kiểm kê thực tế kho tài liệu, xây dựng quy chế bản quyền và biểu mẫu consent, chọn lựa chính thức nền tảng mã nguồn mở (DSpace/Invenio).
    *   *Kết quả:* Báo cáo khảo sát baseline, Quy chế số hóa được ký duyệt, Thiết kế mẫu consent được phê duyệt bởi Bộ phận Pháp chế.
*   **Giai đoạn 1 — Xây dựng MVP & Thí điểm (Tháng 3–5):**
    *   *Trọng tâm:* Cài đặt nền tảng lõi, tùy biến giao diện HCMUS, tích hợp SSO trường, xây dựng luồng nộp-duyệt trực tuyến, số hóa thí điểm 1 khoa (~1.000 khóa luận).
    *   *Kết quả:* Nền tảng repository hoạt động, nghiệm thu kiểm thử UAT với 1 khoa thí điểm, hoàn tất đánh giá độ chính xác OCR mẫu.
*   **Giai đoạn 2 — Mở rộng toàn trường (Tháng 6–9):**
    *   *Trọng tâm:* Tiến hành số hóa quy mô lớn cho toàn bộ số lượng khóa luận còn lại (~10.000 cuốn), chính thức áp dụng quy trình nộp trực tuyến bắt buộc cho khóa tốt nghiệp 2026.
    *   *Kết quả:* Toàn bộ kho khóa luận được đưa lên hệ thống, go-live chính thức toàn trường.
*   **Giai đoạn 3 — Nâng cao (Giai đoạn sau, tùy chọn):**
    *   *Trọng tâm:* Nghiên cứu tích hợp API công cụ chống đạo văn, triển khai PoC tìm kiếm ngữ nghĩa AI/RAG hỗ trợ truy vấn thông minh.

---

## 7. Tiêu chí thành công (KPIs)

Hệ thống sẽ được đánh giá hiệu quả dựa trên bộ chỉ số KPI đo lường cụ thể sau:

1.  **Tỷ lệ số hóa:** Đạt tối thiểu **95%** tổng số khóa luận cũ được kiểm kê đưa lên hệ thống trong vòng 18 tháng kể từ khi go-live.
2.  **Tỷ lệ áp dụng trực tuyến:** Đạt **100%** sinh viên tốt nghiệp từ khóa 2026 thực hiện nộp khóa luận và ký consent trực tuyến qua hệ thống.
3.  **Tần suất sử dụng:** Đạt trung bình tối thiểu **5.000 lượt truy cập/tra cứu** mỗi tháng sau 6 tháng vận hành chính thức.
4.  **Hiệu suất tra cứu:** Thời gian phản hồi trung bình cho một truy vấn tìm kiếm toàn văn dưới **3 giây**.
5.  **Mức độ hài lòng:** Đạt tối thiểu **85%** phản hồi hài lòng (mức 4/5 trở lên) từ sinh viên và giảng viên qua đợt khảo sát định kỳ hàng năm.
6.  **Tính an toàn pháp lý:** **0** xảy ra vụ việc tranh chấp bản quyền hoặc khiếu nại của tác giả liên quan đến việc hiển thị tài liệu trên kho số.

---

## 8. Các bên liên quan & Phân vai (Stakeholders & RACI)

### 8.1. Stakeholder Register

*   **Sponsor (Nhà tài trợ):** Ban Giám hiệu HCMUS. Vai trò: Bảo trợ dự án, phê duyệt chủ trương, ngân sách theo từng giai đoạn.
*   **Client (Chủ trì nghiệp vụ):** Ban Giám đốc Thư viện HCMUS. Vai trò: Quản lý quy trình duyệt xuất bản, kiểm soát chất lượng metadata, tổ chức vận hành kho số sau go-live.
*   **Client (Chủ trì kỹ thuật):** Phòng Công nghệ Thông tin. Vai trò: Triển khai hạ tầng máy chủ/lưu trữ, tùy biến phần mềm lõi, tích hợp SSO/LDAP, bảo mật và sao lưu.
*   **User (Người dùng cuối):** Sinh viên, Giảng viên, Phòng Đào tạo (gắn kết quy trình nộp khóa luận số vào thủ tục xét tốt nghiệp).
*   **Cố vấn Pháp lý:** Bộ phận Pháp chế & Lưu trữ của trường. Vai trò: Tư vấn quy chế bản quyền và đồng ý công khai.

### 8.2. Ma trận Trách nhiệm (RACI Matrix)

*   **R** (Responsible): Người thực hiện công việc.
*   **A** (Accountable): Người chịu trách nhiệm cuối cùng (Mỗi gói công việc chỉ có duy nhất **1** đơn vị Accountable).
*   **C** (Consulted): Người được tham vấn ý kiến.
*   **I** (Informed): Người được nhận thông tin kết quả.

| Gói công việc (WBS) | Thư viện | Phòng CNTT | Phòng Đào tạo | Pháp chế & Lưu trữ | Ban Giám hiệu | Sinh viên / Giảng viên |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **WP1 — Khảo sát & Khởi động** | **A** / R | R | C | C | I | - |
| **WP2 — Hạ tầng & Nền tảng** | C | **A** / R | - | - | I | - |
| **WP3 — Phát triển & Tùy biến** | C | **A** / R | - | - | I | C |
| **WP4 — Số hóa tài liệu** | **A** / R | C | - | C | I | - |
| **WP5 — Kiểm thử & Nghiệm thu** | R | **A** / R | - | - | I | C |
| **WP6 — Triển khai & Vận hành** | **A** / R | R | C | - | I | I |

---

## 9. Các đầu việc chính (Work Breakdown Structure - WBS)

Dự án được phân rã thành 6 gói công việc (Work Packages - WP) cốt lõi phục vụ xây dựng và đưa hệ thống vào vận hành thực tế:

*   **WP1 — Khảo sát & Khởi động:**
    *   Kiểm kê thực tế kho khóa luận giấy tại thư viện (số đầu, số trang trung bình, tình trạng tài liệu).
    *   Tổ chức 15-20 cuộc phỏng vấn sâu sinh viên và giảng viên để xác định nhu cầu tra cứu.
    *   Nghiên cứu các tiền lệ thư viện số (DSpace/Invenio) tại các trường Đại học thành viên ĐHQG-HCM.
    *   Thiết kế biểu mẫu đồng ý công bố (consent form) và quy trình xử lý pháp lý.
*   **WP2 — Hạ tầng & Nền tảng:**
    *   Cập nhật và cấp phát tài nguyên máy chủ ảo/Cloud nội bộ của trường.
    *   Thiết lập môi trường kỹ thuật chuẩn: Development, Staging và Production.
    *   Cài đặt phiên bản lõi của nền tảng đã chọn (DSpace hoặc Invenio), cấu hình cơ sở dữ liệu PostgreSQL.
    *   Cấu hình quy trình sao lưu (backup) tự động hàng ngày sang vùng lưu trữ độc lập.
*   **WP3 — Phát triển & Tùy biến:**
    *   Tùy biến giao diện (UI) theo nhận diện thương hiệu của HCMUS.
    *   Cấu hình lược đồ metadata theo chuẩn Dublin Core phục vụ mô tả khóa luận.
    *   Lập trình luồng nộp bài trực tuyến dành cho sinh viên và bảng điều khiển (dashboard) phê duyệt dành cho thủ thư.
    *   Tích hợp xác thực một lần (SSO/LDAP) của nhà trường.
    *   Thiết lập và cấu hình Elasticsearch cho chức năng tìm kiếm toàn văn.
*   **WP4 — Số hóa tài liệu (Gói công việc lớn nhất):**
    *   Phân loại tài liệu giấy, tháo gáy chuẩn bị quét.
    *   Thực hiện quét (scan) sang định dạng PDF chất lượng cao.
    *   Chạy nhận dạng ký tự quang học (OCR) tiếng Việt cho file PDF.
    *   Nhập metadata mô tả khóa luận dựa trên bản cứng.
    *   Hậu kiểm chất lượng file PDF và metadata trước khi import hàng loạt lên hệ thống.
*   **WP5 — Kiểm thử & Nghiệm thu:**
    *   Kiểm thử chức năng toàn hệ thống (luồng nộp, duyệt, tìm kiếm, phân quyền).
    *   Kiểm thử bảo mật cơ bản (kiểm tra quyền truy cập tệp tin khi không đăng nhập).
    *   Tổ chức đợt kiểm thử người dùng (UAT) với Thư viện và 1-2 khoa thí điểm.
    *   Vá lỗi và tối ưu hiệu năng tìm kiếm.
*   **WP6 — Triển khai & Vận hành:**
    *   Biên soạn tài liệu hướng dẫn sử dụng cho sinh viên, giảng viên và thủ thư.
    *   Tổ chức các buổi tập huấn sử dụng cho cán bộ Thư viện và Giáo vụ khoa.
    *   Phòng Đào tạo ban hành quy chế bắt buộc nộp bản mềm khóa luận từ kỳ tốt nghiệp gần nhất.
    *   Truyền thông ra mắt hệ thống, go-live chính thức.

---

## 10. Ước tính thời gian (Timeline)

Thời gian triển khai dự án phụ thuộc lớn vào phương án số hóa kho tài liệu cũ. Dưới đây là phân tích 2 phương án thực thi:

### 10.1. So sánh 2 phương án triển khai

*   **Phương án A (Số hóa toàn bộ trước khi release):** Tiến hành scan, OCR và import toàn bộ ~10.000 khóa luận cũ trước khi chạy chính thức hệ thống. 
    *   *Thời gian dự kiến:* **7–10 tháng** (Đường găng đi qua WP4 số hóa kéo dài từ 4-6 tháng).
    *   *Đánh giá:* Rủi ro cao do thời gian phản hồi từ người dùng chậm, dễ trễ tiến độ kỹ thuật vì phải chờ đợi số hóa.
*   **Phương án B (Thí điểm & Phát hành cuốn chiếu - Khuyến nghị):** Phát hành MVP hệ thống sau khi số hóa thí điểm xong 1 khoa (~1.000 cuốn) để phục vụ ngay khóa tốt nghiệp mới nộp bài trực tuyến. Kho tài liệu cũ của các khoa còn lại sẽ được số hóa cuốn chiếu song song với quá trình vận hành hệ thống.
    *   *Thời gian dự kiến:* **3–4 tháng** tới lúc go-live MVP.
    *   *Đánh giá:* Mang lại giá trị sớm cho nhà trường, giảm rủi ro dự án, cho phép tinh chỉnh lỗi hệ thống dựa trên phản hồi thực tế trước khi mở rộng.

### 10.2. Bảng tiến độ chi tiết (Theo Phương án B)

![Sơ đồ tiến độ chi tiết (Gantt Chart)](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/docs/images/project_timeline.svg)

*\*Chú thích: WP4 (Số hóa) chạy song song từ tuần thứ 5 để cung cấp dữ liệu thử nghiệm cho WP3 và WP5.*

---

## 11. Ước tính chi phí (USD)

Ngân sách dự án được chia làm 3 nhóm chính dưới đây. Mọi con số đều được xây dựng trên đơn giá thị trường ước lượng và mô hình tận dụng nhân lực nội bộ sẵn có của Phòng CNTT trường.

### 11.1. Đầu tư một lần (CapEx)

Ngân sách CapEx dùng để xây dựng hệ thống và thực hiện số hóa đợt đầu cho kho tài liệu hiện hữu (~10.000 cuốn).

| Hạng mục đầu tư | Cơ sở ước tính chi tiết | Khoảng giá (USD) |
| :--- | :--- | :---: |
| **Số hóa tài liệu cũ** | Thuê ngoài scan + OCR tiếng Việt + nhập metadata cho ~10.000 cuốn khóa luận cũ (ước tính đơn giá $2 - $4/cuốn tùy độ dày). | $20.000 – $40.000 |
| **Phát triển & Tùy biến** | Chi phí cơ hội nội bộ cho nhóm phát triển của Phòng CNTT (3–4 nhân sự kiêm nhiệm × 3 tháng phát triển cốt lõi). | $12.000 – $20.000 |
| **Thiết lập hạ tầng ban đầu** | Mua sắm bản quyền máy chủ ảo, chứng chỉ bảo mật SSL, thiết lập hệ thống lưu trữ và sao lưu dự phòng ban đầu. | $2.000 – $5.000 |
| **Đào tạo & Triển khai** | Biên soạn tài liệu, quay video hướng dẫn, tổ chức các buổi tập huấn trực tiếp, truyền thông ra mắt sinh viên. | $1.000 – $3.000 |
| **Dự phòng rủi ro (~15%)** | Ngân sách dự phòng cho các phát sinh kỹ thuật hoặc biến động đơn giá scan thực tế của nhà cung cấp. | $5.000 – $10.000 |
| **TỔNG CAPEX** | **Ước tính tổng mức đầu tư một lần** | **≈ $40.000 – $78.000** |

### 11.2. Vận hành định kỳ (OpEx / năm)

Chi phí duy trì hệ thống hoạt động ổn định hàng năm, bắt đầu tính từ năm thứ 2.

| Hạng mục vận hành | Cơ sở ước tính chi tiết | Khoảng giá (USD/năm) |
| :--- | :--- | :---: |
| **Hạ tầng máy chủ & Lưu trữ** | Chi phí điện, duy trì phần cứng server vật lý hoặc thuê Cloud lưu trữ tệp tin kèm băng thông tải file hàng tháng. | $2.000 – $5.000 |
| **Bảo trì & Hỗ trợ kỹ thuật** | Chi phí cập nhật bản vá bảo mật phần mềm lõi, hỗ trợ kỹ thuật vận hành (ước tính 1 nhân sự CNTT bán thời gian). | $4.000 – $8.000 |
| **Số hóa bổ sung hàng năm** | Số hóa các khóa luận không nộp trực tuyến hoặc tài liệu phát sinh khác. | $1.000 – $2.000 |
| **TỔNG OPEX / NĂM** | **Chi phí vận hành định kỳ hàng năm** | **≈ $7.000 – $15.000** |

### 11.3. Hạng mục tùy chọn (Giai đoạn sau)

Các chi phí này chỉ phát sinh khi nhà trường quyết định nâng cấp hệ thống lên Giai đoạn 3 và không nằm trong ngân sách MVP ban đầu.

*   **Hệ thống tìm kiếm ngữ nghĩa AI/RAG:** Ước tính phát sinh thêm từ **$3.000 – $8.000/năm** cho chi phí hạ tầng cơ sở dữ liệu vector và chi phí gọi API mô hình ngôn ngữ lớn (LLM).
*   **Bản quyền công cụ chống đạo văn:** Theo báo giá thực tế của đơn vị cung cấp (ví dụ: Turnitin tính theo số lượng tài khoản sinh viên hoạt động hàng năm).

---

## 12. Kết luận & Khuyến nghị

### 12.1. Kết luận

Dự án xây dựng **Kho Lưu trữ Số Khóa luận Tốt nghiệp HCMUS** giải quyết trực tiếp một vấn đề vận hành có thật và ngày càng cấp bách của Thư viện trường, đồng thời mang lại lợi ích to lớn cho hoạt động học tập, tra cứu của sinh viên và giảng viên. 

Việc lựa chọn xây dựng hệ thống trên nền tảng mã nguồn mở chuyên dụng (DSpace/Invenio) là hướng đi thực tế, giảm thiểu tối đa rủi ro kỹ thuật và tài chính so với việc tự phát triển từ đầu. Tuy nhiên, dự án vẫn chứa đựng hai điểm nghẽn phi kỹ thuật cực kỳ quan trọng là: **Ràng buộc pháp lý về bản quyền (consent)** và **Độ chính xác của việc OCR tiếng Việt**.

### 12.2. Khuyến nghị hành động

Để đảm bảo dự án triển khai thành công, tránh lãng phí ngân sách, Thư viện và Phòng CNTT kiến nghị Ban Giám hiệu phê duyệt các bước sau:

1.  **Phê duyệt triển khai Giai đoạn 0 (Khảo sát & Chuẩn bị):** Cấp ngân sách nhỏ ban đầu để thực hiện kiểm kê chính xác số lượng tài liệu, khảo sát nhu cầu người dùng thật, và đặc biệt là phối hợp với Bộ phận Pháp chế để hoàn thiện quy chế consent bản quyền của sinh viên trước khi ký hợp đồng quét số hóa.
2.  **Thông qua phương án triển khai MVP cuốn chiếu (Phương án B):** Cho phép triển khai thí điểm hệ thống tại 1-2 khoa trước trong vòng 3-4 tháng để đánh giá hiệu quả thực tế và độ chính xác của OCR mẫu, trước khi phê duyệt ngân sách số hóa hàng loạt cho toàn bộ kho khóa luận cũ của trường.
3.  **Tích hợp chính sách nộp bài trực tuyến:** Chỉ đạo Phòng Đào tạo ban hành văn bản chính thức tích hợp quy trình nộp khóa luận trực tuyến thành một bước bắt buộc trong quy chế xét tốt nghiệp của sinh viên kể từ kỳ tốt nghiệp năm 2026.
4.  **Tách biệt lộ trình AI:** Chưa đầu tư ngân sách cho các tính năng tìm kiếm AI/RAG và chống đạo văn ở giai đoạn này. Các tính năng này chỉ được xem xét sau khi hệ thống lưu trữ lõi đã vận hành ổn định và chứng minh được giá trị thực tế.
