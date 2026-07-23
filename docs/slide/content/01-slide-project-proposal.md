# SLIDE DECK — PHẦN 1: PROJECT PROPOSAL
## Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS (HCMUS-LDMS)

> Nguồn nội dung: `02-project-proposal.md`, `01-project-idea.md`, `04-feasibility-study.md`
> Số lượng slide đề xuất: **13 slide**

---

## Slide 1 — Trang bìa

**Loại slide:** Title Slide

**Nội dung:**
- Tên dự án: **HCMUS-LDMS** — Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS
- Phân hệ tài liệu: Project Proposal
- Đơn vị: Thư viện & Phòng Công nghệ Thông tin — Trường ĐH Khoa học Tự nhiên (ĐHQG-HCM)
- Nhóm thực hiện / ngày trình bày (để trống — điền khi thuyết trình)

**Gợi ý thiết kế:**
- Layout: full-bleed, ảnh nền mờ (overlay tối 60%) là kệ sách thư viện chuyển động sang giao diện số (ẩn dụ chuyển đổi số)
- Màu chủ đạo: xanh navy HCMUS + nhấn vàng gold; font tiêu đề dày (Bold, Serif nhẹ) thể hiện tính học thuật
- Logo trường + logo thư viện góc trên; badge trạng thái "Under Review" góc dưới phải

**Ghi chú thuyết trình:** Giới thiệu nhanh bối cảnh: đây là đề xuất dự án cần Ban Giám hiệu phê duyệt chủ trương và ngân sách.

---

## Slide 2 — Vấn đề: Nỗi đau thực tế (Persona-driven)

**Loại slide:** Problem / Storytelling

**Nội dung:**
- Câu chuyện 1 — **Sinh viên Nguyễn Văn Linh** (Linh Trung): di chuyển 15km/3 giờ chỉ để mượn 1 cuốn sách độc bản ở Quận 5; PDF scan tĩnh không responsive, giảm 80% hiệu suất học tập khi đọc trên điện thoại
- Câu chuyện 2 — **Thủ thư Mai** (Quận 5): kho sách quá tải 100% diện tích thiết kế; 85% thời gian làm việc dành cho mượn/trả thủ công; nguy cơ hư hại tài liệu vĩnh viễn
- 3 con số nền tảng: **40%** giáo trình cũ xuống cấp · **100%** công suất kho quá tải · **92%** sinh viên muốn chuyển sang đọc số trên smartphone

**Gợi ý thiết kế:**
- Layout 2 cột song song (split-screen) — mỗi bên là 1 persona với avatar minh họa + 1 câu trích dẫn in nghiêng lớn
- 3 con số nổi bật đặt thành dải thống kê (stat strip) cuối slide, dùng số to + icon
- Tông màu ấm (đỏ cam nhạt) để truyền tải "nỗi đau", tương phản với các slide giải pháp sau (tông xanh mát)

**Ghi chú thuyết trình:** Đây là "hook" mở đầu — nhấn mạnh vấn đề có thật, đã được khảo sát định lượng, không phải giả định.

---

## Slide 3 — Tại sao nên thực hiện dự án này?

**Loại slide:** Why / Business Case

**Nội dung:**
- 3 thách thức cốt lõi: (1) xuống cấp vật lý tri thức, (2) quá tải hạ tầng lưu trữ, (3) trải nghiệm đọc số nghèo nàn
- Động lực chiến lược: Chiến lược Đại học số ĐHQG-HCM giai đoạn 2026–2030 (mục tiêu >90% học liệu số hóa)
- Value proposition cốt lõi: *"Bảo tồn tri thức học thuật giấy tĩnh sang học liệu số reflowable, thông qua số hóa khép kín tự động + kiểm soát bản quyền DRM Signed URL 15 phút"*
- Mức độ ưu tiên: **Cao (High Priority)** — cần MVP trước khai giảng năm học 2026

**Gợi ý thiết kế:**
- Layout: tiêu đề lớn bên trái "TẠI SAO?", bên phải 3 thẻ (card) thách thức xếp dọc, mỗi thẻ 1 icon (sách rách, kho đầy, điện thoại mỏi mắt)
- Câu value proposition đặt trong khung trích dẫn (quote box) nổi bật ở cuối, nền màu nhấn
- Có thể dùng Visualizer để vẽ sơ đồ "3 vấn đề → 1 giải pháp"

**Ghi chú thuyết trình:** Liên kết trực tiếp 3 vấn đề ở slide trước với lý do đầu tư — đây là cầu nối logic giữa "pain" và "solution".

---

## Slide 4 — Giải pháp đề xuất: Scan-to-EPUB khép kín

**Loại slide:** Solution Overview

**Nội dung:**
- Luồng tự động: Scan (300 DPI) → Tesseract OCR tiếng Việt → Split-screen Editor (soát lỗi) → Pandoc đóng gói EPUB 3.0 reflowable → PostgreSQL FTS index → Đọc online qua Signed URL (MinIO, 15 phút)
- Trải nghiệm đọc: co giãn chữ 80–200%, đổi font (Roboto/Inter/OpenDyslexic), 3 chế độ nền (Light/Sepia/Dark)
- Bảo vệ bản quyền: chặn chuột phải/copy/in ấn, không có nút tải file gốc
- Kết quả kỳ vọng: giải phóng 60–70% diện tích kệ sách giấy Quận 5

**Gợi ý thiết kế:**
- Diagram dạng pipeline ngang (6 bước, icon + mũi tên) — rất phù hợp dùng Visualizer để vẽ sơ đồ luồng
- Layout: sơ đồ chiếm 2/3 slide trên, 1/3 dưới là 2 cột nhỏ "Trải nghiệm đọc" và "Bảo mật"
- Icon nhất quán theo bộ icon flat outline; màu pipeline chuyển dần từ xám (giấy) sang xanh dương (số hóa)

**Ghi chú thuyết trình:** Đây là slide "trái tim" của giải pháp — nên dành thời gian giải thích kỹ từng bước trong pipeline.

---

## Slide 5 — So sánh với đối thủ cạnh tranh (Giải pháp thương mại)

**Loại slide:** Competitive Comparison

**Nội dung:**
| Tiêu chí | Giải pháp thương mại (Lạc Việt Vebrary, DSpace) | HCMUS-LDMS (đề xuất) |
|---|---|---|
| Chi phí | 300 triệu – hơn 1 tỷ VNĐ | Dưới 100 triệu VNĐ (CapEx 75–95tr) |
| Tùy biến OCR tiếng Việt Split-screen | Rất khó / không hỗ trợ | Xây dựng riêng, tối ưu chuyên ngành |
| DRM Signed URL liên kết LDAP trường | Không hỗ trợ | Có (MinIO Signed URL 15 phút) |
| Làm chủ mã nguồn | Không (vendor lock-in) | Có (100% mã nguồn nội bộ) |

**Gợi ý thiết kế:**
- Dùng bảng so sánh 2 cột kiểu "VS" với cột HCMUS-LDMS được highlight màu nhấn + khung viền nổi bật
- Thêm badge "Tiết kiệm > 200 triệu VNĐ" dạng huy hiệu tròn cạnh bảng
- Icon check (✓) màu xanh / cross (✗) màu đỏ nhạt cho từng dòng để dễ quét mắt

**Ghi chú thuyết trình:** Nhấn mạnh: đối thủ thương mại không sở hữu "Exclusive Content" của HCMUS dù có công nghệ tốt hơn — dẫn vào slide MOAT.

---

## Slide 6 — So sánh với phương án kết hợp công cụ có sẵn (thủ công)

**Loại slide:** Alternative Comparison

**Nội dung:**
- Phương án thủ công: Máy scan văn phòng → Abbyy FineReader (offline) → Calibre (đóng gói EPUB) → chia sẻ qua Google Drive/OneDrive
- 3 nút thắt lớn:
  1. Quy trình rời rạc — tốn 2–3 giờ lao động thủ công/đầu sách
  2. Rủi ro bản quyền nghiêm trọng — Drive không chặn tải xuống, không Signed URL hết hạn
  3. Tra cứu hạn chế — không lập chỉ mục toàn văn đến từng trang
- HCMUS-LDMS giải quyết cả 3: tự động hóa pipeline, DRM Signed URL, PostgreSQL FTS <3 giây

**Gợi ý thiết kế:**
- Layout dạng "trước/sau" (before-after) — bên trái sơ đồ công cụ rời rạc (biểu tượng đứt gãy, mũi tên đỏ cảnh báo), bên phải sơ đồ khép kín liền mạch (mũi tên xanh liên tục)
- Có thể dùng Visualizer để vẽ 2 pipeline cạnh nhau minh họa sự khác biệt về tính liên kết

**Ghi chú thuyết trình:** Đây là câu trả lời trực tiếp cho câu hỏi "sao không ghép các tool có sẵn cho nhanh, rẻ hơn?" — làm rõ bằng chi phí ẩn (thời gian, rủi ro rò rỉ).

---

## Slide 7 — Lợi thế cạnh tranh bền vững (MOAT Analysis)

**Loại slide:** Strategic Analysis

**Nội dung:**
- 5 lớp MOAT: (1) Nội dung độc quyền ⭐⭐⭐⭐⭐, (2) Chi phí chuyển đổi cao ⭐⭐⭐⭐⭐, (3) Hiệu ứng mạng lưới, (4) Lợi thế chi phí (mã nguồn mở), (5) Data MOAT (kho EPUB + FTS tích lũy)
- Kết luận đối chuẩn: đối thủ thương mại có công nghệ nhưng **không có Exclusive Content** của HCMUS; phương án ghép công cụ rời rạc **không có MOAT nào**

**Gợi ý thiết kế:**
- Biểu đồ radar/hoa 5 cánh (5 yếu tố MOAT) hoặc 5 thẻ xếp vòng cung, mỗi thẻ có mức sao phòng thủ
- Dùng Visualizer để tạo biểu đồ radar minh họa mức độ phòng thủ từng yếu tố
- Màu: mỗi lớp MOAT một màu riêng trong bảng màu đồng bộ

**Ghi chú thuyết trình:** MOAT là lý do dự án bền vững lâu dài, không chỉ là "làm cho xong MVP".

---

## Slide 8 — Phân tích các bên liên quan (Stakeholders) làm rõ tính khả thi

**Loại slide:** Stakeholder Analysis

**Nội dung:**
- Sponsor: Ban Giám hiệu HCMUS — phê duyệt ngân sách, định hướng chiến lược
- Client nghiệp vụ: Ban Giám đốc Thư viện — kiểm soát chất lượng OCR/EPUB, tổ chức CTV
- Client kỹ thuật: Phòng CNTT — hạ tầng ảo hóa, tích hợp OAuth, quản lý FTS
- Cố vấn pháp lý: Bộ phận Pháp chế — thẩm định quy chế bản quyền
- Người dùng cuối: Sinh viên & Giảng viên
- RACI theo 6 gói công việc (WP1–WP6): Thư viện và Phòng CNTT luân phiên giữ vai trò Accountable tùy giai đoạn

**Gợi ý thiết kế:**
- Layout: sơ đồ hình cây (org chart) 5 nhóm stakeholder ở trên, bảng RACI rút gọn ở dưới (6 dòng WP x 6 cột vai trò)
- Màu theo vai trò: A = đỏ đậm, R = xanh dương, C = vàng, I = xám nhạt — giúp quét nhanh bằng mắt
- Có thể tách bảng RACI đầy đủ sang slide phụ nếu cần chi tiết hơn (xem Phần 2)

**Ghi chú thuyết trình:** Khẳng định: tính khả thi không chỉ nằm ở công nghệ mà ở việc mọi vai trò then chốt đã có chủ sở hữu rõ ràng (Accountable duy nhất mỗi WP).

---

## Slide 9 — Phân tích Chi phí – Lợi ích & Điểm hòa vốn

**Loại slide:** Cost-Benefit / Financial

**Nội dung:**
- CapEx: 75.000.000 – 95.000.000 VNĐ | OpEx: 15.000.000 – 30.000.000 VNĐ/năm
- Mô hình Cost Avoidance: tiết kiệm 20 triệu/năm (kho bãi) + 15 triệu/năm (giờ công thủ thư) = 35 triệu/năm
- Thời gian hòa vốn: **2.5 – 3.8 năm**
- Lợi ích định tính: bảo tồn học liệu gốc, nâng thương hiệu đại học số, làm chủ mã nguồn

**Gợi ý thiết kế:**
- Biểu đồ cột (bar chart) CapEx vs OpEx, kèm đường breakeven timeline dạng biểu đồ tích lũy dòng tiền (line chart cắt trục 0 tại năm ~3)
- Dùng Chart trong Visualizer (data_viz module) để trực quan hóa điểm hòa vốn
- 2 con số CapEx/OpEx đặt to, nổi bật ở góc trên như KPI card

**Ghi chú thuyết trình:** Đây là slide thuyết phục tài chính then chốt cho Ban Giám hiệu — nhấn mạnh ngân sách nằm trong giới hạn <100 triệu VNĐ.

---

## Slide 10 — Lộ trình triển khai cấp cao (Roadmap 20 tuần)

**Loại slide:** Roadmap / Timeline

**Nội dung:**
- GĐ 0 (Tuần 1–2): Khảo sát & Bản quyền
- GĐ 1 (Tuần 3–12): Xây dựng MVP & thí điểm 500 cuốn sách CNTT
- GĐ 2 (Tuần 13–18): Số hóa diện rộng 2.000 giáo trình
- GĐ 3 (Tuần 19–20): Nghiệm thu UAT, pentest, go-live toàn trường
- Mô hình Gating Checkpoints kiểm soát ngân sách theo từng giai đoạn

**Gợi ý thiết kế:**
- Timeline ngang dạng milestone (4 cột mốc trên 1 thanh 20 tuần), mỗi giai đoạn 1 màu khác nhau
- Đánh dấu cổng kiểm soát (gate) bằng biểu tượng cổng/khóa tại điểm chuyển giai đoạn
- Rất phù hợp dùng Visualizer diagram module cho timeline trực quan

**Ghi chú thuyết trình:** Nhấn mạnh mô hình cuốn chiếu MVP giảm rủi ro — không đợi 20 tuần mới có sản phẩm dùng được.

---

## Slide 11 — Demo: Đánh giá tài liệu với AI hỗ trợ và xem xét bởi con người

**Loại slide:** Live Demo / Process Illustration

**Nội dung:**
- Mô hình Human-in-the-loop: Tesseract OCR (AI) chạy bất đồng bộ qua FastAPI BackgroundTasks → sinh văn bản thô → con người (BTV/thủ thư/CTV) soát lỗi trên giao diện Split-screen → Thủ thư phê duyệt xuất bản cuối cùng
- Mục tiêu demo: cho thấy AI xử lý phần lặp lại tốn công (nhận dạng ký tự), con người đảm bảo độ chính xác học thuật 100% trước khi publish
- Kịch bản demo gợi ý: tải 1 trang giáo trình mẫu → xem kết quả OCR thô → chỉnh sửa trên Split-screen → so sánh trước/sau

**Gợi ý thiết kế:**
- Layout demo: khung screenshot/video lớn ở giữa (placeholder "LIVE DEMO"), 2 nhãn nhỏ 2 bên "AI xử lý" và "Con người kiểm duyệt"
- Dùng màu tương phản để phân biệt phần AI (xanh dương công nghệ) và phần con người (cam ấm)
- Nếu trình bày trực tiếp: chuyển sang màn hình demo thật ở đây, slide chỉ là bìa dẫn nhập

**Ghi chú thuyết trình:** Đây là điểm nhấn "wow" của phần trình bày — cần chuẩn bị sẵn 1 tài liệu mẫu để demo trực tiếp giao diện Split-screen.

---

## Slide 12 — Danh mục rủi ro kinh doanh & Biện pháp giảm thiểu

**Loại slide:** Risk Register

**Nội dung:**
- Bản quyền & SHTT (Cao) → chỉ số hóa sách nội bộ, phân quyền Internal/Restricted
- Chất lượng OCR (Trung bình) → tiền xử lý ảnh, MVP ưu tiên sách in rõ từ 2010+
- Rò rỉ tài liệu (Trung bình) → Signed URL 15 phút, chặn copy/in ấn
- Quá tải nhân sự (Trung bình) → cam kết phân bổ 50% thời gian chính thức, dùng Docker CI/CD

**Gợi ý thiết kế:**
- Ma trận rủi ro 2 trục (xác suất x mức độ ảnh hưởng) với 4 điểm rủi ro đặt vào đúng ô — trực quan hơn bảng liệt kê
- Màu theo mức độ: đỏ (Cao), vàng (Trung bình), xanh (Thấp)

**Ghi chú thuyết trình:** Không né tránh rủi ro — cho thấy nhóm đã lường trước và có phương án cụ thể, tăng độ tin cậy với Ban Giám hiệu.

---

## Slide 13 — Kết luận và Khuyến nghị hành động

**Loại slide:** Conclusion / Call to Action

**Nội dung:**
1. Phê duyệt chủ trương & ngân sách khởi động **Giai đoạn 0 (Khảo sát)**
2. Thông qua phương án **thí điểm cuốn chiếu MVP** (Khoa CNTT) trước khi mở rộng
3. Giao Pháp chế + Thư viện hoàn thiện quy chế bản quyền số hóa trước Tuần 3
4. Cho phép tuyển sinh viên CTV bán thời gian hỗ trợ biên tập OCR

**Gợi ý thiết kế:**
- Layout dạng checklist 4 mục lớn với số thứ tự nổi bật (numbered list, font size lớn)
- Nền chuyển màu gradient sang tông "quyết định" (xanh đậm → vàng gold) để tạo cảm giác chốt lại vấn đề
- CTA button-style cuối slide: "Đề nghị phê duyệt Giai đoạn 0"

**Ghi chú thuyết trình:** Kết thúc bằng đúng 1 câu hỏi cần Ban Giám hiệu trả lời: có phê duyệt Giai đoạn 0 hay không.
