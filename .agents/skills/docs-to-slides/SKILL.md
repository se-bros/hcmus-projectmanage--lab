---
name: doc-to-slide-deck
description: Chuyển một bộ tài liệu dự án (project idea, proposal, vision & scope, charter, architecture, backlog, cost/time) thành nội dung + thiết kế slide thuyết trình, sẵn sàng đưa vào công cụ AI tạo slide (Gamma, Tome, Canva Magic Design, Napkin, hoặc Claude/GPT tạo .pptx).
when_to_use: Khi có ≥1 tài liệu dạng báo cáo/markdown/docx về một dự án (feasibility study, proposal, charter, backlog...) và cần tạo bài thuyết trình cho một thời lượng cụ thể (vd. 20-25 phút) trước một đối tượng cụ thể (Ban Giám hiệu, hội đồng, khách hàng, giảng viên...).
---

# SKILL: Doc-to-Slide-Deck

Skill này mô tả quy trình lặp lại được để biến N tài liệu dự án dài thành 1 file Markdown chứa đầy đủ nội dung + hướng dẫn thiết kế cho từng slide — không tự tạo file .pptx, mà tạo "bản thiết kế" (spec) để đưa vào công cụ AI-slide-generator khác.

## Bước 1 — Thu thập & đọc toàn bộ tài liệu nguồn
- Đọc **hết** từng file được cung cấp, không chỉ file "quan trọng nhất". Với dự án phần mềm, thứ tự tài liệu thường là:
  `01-idea → 02-proposal → 03-vision-scope → 04-feasibility → 05-charter → 06-architecture → 07-backlog → 08-cost-time-resource`
- Với mỗi tài liệu, trích ra 3 loại thông tin để dùng cho slide:
  1. **Con số neo (anchor numbers):** % , VNĐ, tuần, giây, người — đây là thứ khán giả nhớ nhất
  2. **Câu chuyện/persona:** quote thực tế, pain point cụ thể — dùng để mở đầu chương
  3. **Sơ đồ có sẵn:** workflow, kiến trúc, ma trận (SWOT, RACI, As-is/To-be) — ưu tiên trực quan hóa thay vì liệt kê chữ

## Bước 2 — Hỏi/nắm rõ 3 tham số bắt buộc trước khi soạn
Nếu người dùng chưa nói rõ, hỏi 1 câu duy nhất (không hỏi dồn dập):
1. **Thời lượng trình bày** (vd: 10 phút / 20-25 phút / 45 phút) → quyết định số slide (~1 slide/45-70 giây)
2. **Đối tượng khán giả** (Ban Giám hiệu ra quyết định ngân sách / hội đồng bảo vệ đồ án / khách hàng kỹ thuật) → quyết định tỷ trọng slide kỹ thuật vs slide kinh doanh
3. **Mục tiêu cuối (call-to-action)** của bài nói (xin phê duyệt ngân sách / trình bày học thuật / demo sản phẩm)

## Bước 3 — Dựng khung chương (không quá 5-6 chương)
Khung chuẩn cho dự án phần mềm/CNTT (điều chỉnh theo nội dung thực tế):
1. Vấn đề & Bối cảnh (why)
2. Giải pháp & Giá trị đề xuất (what + differentiation/MOAT)
3. Công nghệ & Kiến trúc (how, chỉ nêu mức cần thiết theo khán giả)
4. Khả thi & Hiệu quả kinh tế (proof — SWOT, benchmarking, cost-benefit)
5. Kế hoạch triển khai & Rủi ro (roadmap, RACI, risk)
6. Kết luận & Khuyến nghị hành động (luôn kết bằng 2-3 hành động cụ thể, có deadline)

Mỗi chương mở bằng 1 "slide chuyển chương" (nền tối, số thứ tự lớn) để tạo nhịp nghỉ.

## Bước 4 — Viết từng slide theo khuôn cố định
Với mỗi slide, luôn viết đủ 4 phần sau (đừng bỏ phần Design/Ghi chú):
```
### Slide N — TIÊU ĐỀ VIẾT NHƯ MỘT KẾT LUẬN (không phải chủ đề chung chung)
**Layout:** [mô tả bố cục cụ thể: số cột, vị trí hình/chart, kiểu sơ đồ]
**Nội dung:** [bullet cực ngắn hoặc bảng — KHÔNG copy nguyên đoạn văn dài từ tài liệu gốc, phải rút gọn thành slide-ready text]
**Ghi chú thuyết trình:** [1 câu định hướng người nói nên nhấn điều gì trong ~X giây]
```
Nguyên tắc tiêu đề: "Sinh viên phải di chuyển 15km để đọc 1 cuốn sách" tốt hơn "Vấn đề hiện trạng".

## Bước 5 — Thiết kế Design System TRƯỚC khi liệt kê slide
Luôn mở đầu file bằng 1 Design System gồm:
- Bảng màu (Primary/Accent/Cảnh báo) kèm mã hex — chọn màu phản ánh **ngành/chủ đề** của dự án (thư viện → xanh navy+vàng hổ phách "tri thức"; fintech → xanh lá+đen; y tế → xanh dương+trắng...)
- Font chữ (ưu tiên font hỗ trợ tiếng Việt tốt nếu nội dung tiếng Việt: Be Vietnam Pro, Inter)
- Nguyên tắc bố cục (1 thông điệp/slide, tỷ lệ 80/15/5 màu, số trang, header bar)
- Danh sách các sơ đồ/biểu đồ cần chuẩn bị trước (liệt kê rõ loại chart: Gantt, radar, 2x2 matrix, funnel...)

## Bước 6 — Kết thúc bằng bảng phân bổ thời gian
Luôn có 1 bảng: Chương | Số slide | Thời gian ước tính — để người trình bày tự luyện tập đúng thời lượng, và để kiểm tra tổng số slide có hợp lý không (quy tắc ngón tay cái: 45-70 giây/slide đối với slide có dữ liệu, 5-10 giây cho slide chuyển chương).

## Lỗi thường gặp cần tránh
- ❌ Copy nguyên bảng/đoạn dài từ tài liệu gốc vào slide — luôn rút gọn, slide không phải tài liệu để đọc
- ❌ Tiêu đề slide là danh từ chung ("Kiến trúc hệ thống") thay vì thông điệp ("Modular Monolith giúp 4 kỹ sư kiêm nhiệm vẫn kịp tiến độ")
- ❌ Thiếu phần Design/Layout cho từng slide — nếu chỉ liệt kê nội dung, công cụ AI-slide-generator sẽ tự chọn bố cục ngẫu nhiên, không nhất quán
- ❌ Quên mục "Ghi chú thuyết trình" — người trình bày cần biết nhấn ý nào trong thời gian ngắn
- ❌ Số slide không khớp thời lượng yêu cầu (quá nhiều slide cho 10 phút, quá ít cho 45 phút)

## Cách dùng output với công cụ AI-slide
- **Gamma / Tome / Napkin AI:** paste toàn bộ nội dung Phần 2 (từng slide) vào ô "Paste in text/outline", giữ nguyên heading `### Slide N —` để công cụ tách đúng slide
- **Canva Magic Design:** tách riêng Design System (Phần 1) làm brief màu sắc/font, sau đó paste nội dung từng slide
- **Claude/GPT tạo file .pptx trực tiếp:** đưa cả file này kèm yêu cầu "hãy dùng skill pptx để tạo file PowerPoint theo đúng nội dung và bố cục mô tả trong file, dùng bảng màu và font đã khai báo ở Design System"
