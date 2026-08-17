# ĐỀ CƯƠNG ÔN TẬP — NGƯỜI 1: KHỞI TẠO, ĐIỀU LỆ & TÍNH KHẢ THI

- **Phạm vi phụ trách:** **Câu 1, Câu 3, Câu 8**
- **Tài liệu tham chiếu chính trong dự án:**
  - [`docs/01-initiation/01-project-idea.md`](../../../docs/01-initiation/01-project-idea.md)
  - [`docs/01-initiation/02-project-proposal.md`](../../../docs/01-initiation/02-project-proposal.md)
  - [`docs/01-initiation/03-feasibility-study.md`](../../../docs/01-initiation/03-feasibility-study.md)
  - [`docs/01-initiation/04-project-charter.md`](../../../docs/01-initiation/04-project-charter.md)
- **Hạn chót hoàn thành đề cương (Bước 1):** **20:00, Thứ Năm (20/08/2026)**
- **Bản in cần nộp kèm khi thi:** Bản in file `02-project-proposal.md` và `04-project-charter.md`.

---

## CÂU 1: ĐỀ XUẤT DỰ ÁN (PROJECT PROPOSAL)

> **Câu hỏi chính:** Trình bày quá trình hình thành và phương pháp đánh giá tài liệu Đề xuất dự án (Project Proposal) của nhóm.

### 1. Dàn ý trả lời 4 câu hỏi vàng:
* **WHAT (Là gì?):** Là tài liệu đầu tiên nhằm thuyết phục các bên liên quan (Nhà trường, Ban Giám đốc Thư viện, Khoa CNTT) về lý do vì sao nên đầu tư dự án HCMUS-LDMS, giải quyết bài toán gì và lợi thế vượt trội so với giải pháp khác.
* **HOW (Cách nhóm thực hiện):**
  1. *Thu thập đầu vào:* Khảo sát thực trạng tại Thư viện CS1 (Quận 5) và CS2 (Thủ Đức) $\rightarrow$ xác định 40% giáo trình cũ bị mục nát và sinh viên CS2 phải đi 15km để mượn sách.
  2. *Xây dựng Persona:* Độc giả (SV Nguyễn Văn Linh), Thủ thư (Cô Mai), Nhà tài trợ (Ban Giám hiệu).
  3. *Đối chuẩn giải pháp:* So sánh với hệ thống thương mại (Lạc Việt, DSpace) và quy trình ghép công cụ rời rạc (Abbyy + Calibre + GDrive).
  4. *Đánh giá đề xuất:* Sử dụng kỹ thuật Prompt Engineering (RACFT) kết hợp AI phản biện chéo (Claude $\leftrightarrow$ ChatGPT) để lọc bỏ các giả định thiếu căn cứ, sau đó họp nhóm review kỹ thuật.
* **WHY (Tại sao cần làm?):** Đề xuất dự án giúp định hình giá trị nghiệp vụ (Business Case), ngăn ngừa việc phát triển sản phẩm không ai cần, và làm tiền đề xin phê duyệt ngân sách.
* **EVIDENCE (Minh chứng dự án):** Ngân sách đề xuất ~18.5M VNĐ (tiết kiệm hơn 90% so với 300M–1 tỷ của phần mềm thương mại), đáp ứng giải quyết trực tiếp 3 nỗi đau lớn của thư viện trường.

### 2. Các câu hỏi thường gặp (FAQ):
- *Dự án phần mềm là gì? Phân biệt với Operation, Program, Portfolio:* Project là nỗ lực tạm thời tạo ra sản phẩm độc bản duy nhất; Operation là hoạt động vận hành lặp đi lặp lại; Program là tập hợp các dự án liên quan; Portfolio là danh mục đầu tư chiến lược.
- *Nguyên nhân khiến dự án thất bại:* Thiếu sự tham gia của Stakeholders, Scope creep (phình phạm vi), ước lượng phi thực tế, thiếu quy trình kiểm soát chất lượng.

---

## CÂU 3: ỦY NHIỆM DỰ ÁN (PROJECT CHARTER)

> **Câu hỏi chính:** Trình bày quá trình hình thành và phương pháp đánh giá tài liệu Ủy nhiệm dự án (Project Charter) của nhóm.

### 1. Dàn ý trả lời 4 câu hỏi vàng:
* **WHAT (Là gì?):** Bản điều lệ chính thức công nhận sự tồn tại của dự án, trao quyền cho Project Manager (PM), xác lập ranh giới phạm vi, mục tiêu SMART và ma trận phân công trách nhiệm RACI.
* **HOW (Cách nhóm thực hiện):**
  1. Căn cứ trên Project Proposal và Feasibility Study đã được phê duyệt.
  2. Định nghĩa mục tiêu SMART: Số hóa 500 giáo trình độc bản, hỗ trợ hiển thị reflowable trên 100% thiết bị, thời gian tra cứu < 2s.
  3. Xác lập ranh giới: Ngân sách trần **100.000.000 VNĐ**, thời gian hoàn thành **20 tuần** (với mốc MVP 7 tuần môn học).
  4. Lập ma trận RACI phân định rõ quyền hạn của Sponsor, PM, Lead Dev, Thủ thư và Sinh viên.
* **WHY (Tại sao cần làm?):** Ngăn chặn tranh chấp quyền hạn, làm căn cứ pháp lý để PM điều phối nhân sự và nguồn lực kỹ thuật.
* **EVIDENCE (Minh chứng dự án):** Mã tài liệu `HCMUS-LDMS-04`, ký cam kết giữa PM và các Trưởng nhóm chức năng.

---

## CÂU 8: BÁO CÁO TÍNH KHẢ THI (FEASIBILITY STUDY REPORT)

> **Câu hỏi chính:** Trình bày quá trình hình thành và phương pháp đánh giá tài liệu Báo cáo tính khả thi của nhóm.

### 1. Dàn ý trả lời 4 câu hỏi vàng:
* **WHAT (Là gì?):** Báo cáo thẩm định toàn diện 5 khía cạnh cốt lõi trước khi quyết định đầu tư: Kỹ thuật (Technical), Kinh tế (Economic), Vận hành (Operational), Pháp lý (Legal) và Lịch trình (Schedule) — viết tắt là TELOS.
* **HOW (Cách nhóm thực hiện):**
  1. *Khả thi Kỹ thuật:* Đánh giá engine Tesseract OCR tiếng Việt, hạ tầng Docker trên máy ảo VMware của trường.
  2. *Khả thi Kinh tế:* Phân tích TCO (Total Cost of Ownership), Capex ~12.5M, Opex ~1.2M/tháng $\rightarrow$ Tổng 18.5M $\ll$ 100M giới hạn.
  3. *Khả thi Pháp lý:* Phân tích Luật Sở hữu Trí tuệ & Bản quyền học liệu nội bộ, thiết kế cơ chế bảo vệ DRM Signed URL (15 phút).
  4. *Khả thi Vận hành:* Đánh giá khả năng làm quen của thủ thư với giao diện biên tập Split-screen.
* **WHY (Tại sao cần làm?):** Là "bộ lọc" quan trọng nhất để loại bỏ các dự án không khả thi hoặc có rủi ro pháp lý/tài chính vượt tầm kiểm soát.
* **EVIDENCE (Minh chứng dự án):** Mã tài liệu `HCMUS-LDMS-03`, phân tích 5 khía cạnh chi tiết kèm ma trận rủi ro.
