# Feasibility Study — hướng dẫn chi tiết

Đọc file này trước khi viết tài liệu **Feasibility Study**.

## Mục lục

1. Câu hỏi tư duy bắt buộc
2. 8 Khía cạnh Khả thi
3. SWOT & Benchmarking
4. Kế hoạch Tài chính (Cost vs Budget)
5. Quản trị Rủi ro
6. Cấu trúc Báo cáo Khả thi chuẩn
7. Vì sao cần Feasibility Study

## 1. Câu hỏi tư duy bắt buộc

- Trong 8 yếu tố khả thi, dự án này yếu nhất ở điểm nào?
- Cost khác Budget như thế nào trong bối cảnh này? Khoản nào thuộc CapEx, khoản nào thuộc OpEx?
- So với đối thủ/giải pháp thay thế, điểm mạnh/yếu (SWOT) của phương án này là gì?
- Rủi ro lớn nhất thuộc kỹ thuật hay vận hành/dự án?

## 2. 8 Khía cạnh Khả thi

Pháp lý (Legal), Thị trường (Market — cung/cầu), Kinh tế (Economic), Công nghệ & Hệ thống (Technology & System), Nguồn lực (Resource), Vận hành (Operational), Lịch trình (Schedule), Văn hóa (Cultural).

## 3. SWOT & Benchmarking

Điểm mạnh/Điểm yếu/Cơ hội/Thách thức của giải pháp đề xuất; so sánh nhanh với 1-2 giải pháp/đối thủ tương đương.

## 4. Kế hoạch Tài chính (Cost vs Budget)

Tách rõ 2 khái niệm — KHÔNG dùng lẫn:

- **Project Cost** (chi phí dự án) — tính **bottom-up theo WBS**:
  - Chi phí nhân sự (giờ công dev/design/QA/BA)
  - Chi phí hạ tầng & license (server, cloud, bản quyền bên thứ 3)
  - Chi phí triển khai (đào tạo, truyền thông, di trú dữ liệu)
- **Project Budget** (ngân sách dự án) = Project Cost + Quỹ dự phòng rủi ro (Contingency Reserve) + Trượt giá/Lạm phát.
- Phân loại dòng tiền: **CapEx** (đầu tư một lần) vs **OpEx** (vận hành/bảo trì hàng năm).
- **Project Profit Graph:** mô tả bằng lời đường lợi ích tích lũy so với đường chi phí tích lũy theo thời gian, xác định điểm hoà vốn.
- Chỉ số tài chính:
  - **ROI = (Benefit – Cost) / Cost** — nếu ROI âm hoặc có phương án khác ROI cao hơn → khuyến nghị không đầu tư.
  - **Payback Period** — thời gian hoàn vốn ước tính.

Nếu không có cơ sở số liệu từ input người dùng, để `[Cần xác nhận với stakeholder]` thay vì bịa số cụ thể.

## 5. Quản trị Rủi ro

Bảng rủi ro chia 2 nhóm:

- **Rủi ro kỹ thuật** — nền tảng không tương thích, khó mở rộng, lỗi dữ liệu khi migration.
- **Rủi ro vận hành/dự án** — trễ tiến độ, vượt ngân sách, người dùng từ chối sử dụng (low adoption rate).

Kèm **Biện pháp giảm thiểu (Mitigation Plan)** cho từng rủi ro lớn.

## 6. Cấu trúc Báo cáo Khả thi chuẩn

Trình bày tổng kết theo khung: Mục đích (Purpose), Lý do (Reason), Thông tin nền (Background information), Tiêu chí đánh giá (Evaluation criteria), Kết quả nghiên cứu (Study findings), Khuyến nghị (Recommendations).

## 7. Vì sao cần Feasibility Study

Giúp phân tích đầy đủ yêu cầu, nhận diện & lập kế hoạch rủi ro, phân tích chi phí/lợi ích, và **lập kế hoạch đào tạo đội ngũ triển khai hệ thống**.
