# Project Proposal (WHY) — hướng dẫn chi tiết

Đọc file này trước khi viết tài liệu **Project Proposal** — trả lời câu hỏi WHY (vì sao làm dự án này), tương đương nội dung Business Requirements / Executive Summary.

## Mục lục
1. Câu hỏi tư duy bắt buộc
2. Capture Initial Artifacts
3. Phân loại nguồn gốc yêu cầu (RFP Classification)
4. Stakeholders
5. Problem Definition
6. Business Goals
7. High-Level Features & Expected Deliverables
8. Context Diagram
9. Customer Discovery
10. Elevator Pitch
11. Checklist nội dung Project Proposal

## 1. Câu hỏi tư duy bắt buộc
Xuất khối `> 🧠 **Tư duy của Agent:**` trả lời các câu hỏi sau trước khi viết:
- Input thuộc loại RFP nào (xem mục 3)?
- Nếu "xây hệ thống mới cho client": xuất phát điểm là quy trình thủ công / giải pháp thô sơ hiện có / công nghệ lạc hậu / yêu cầu tuân thủ / hệ thống đối thủ? Nếu "nâng cấp hệ thống cũ": xuất phát điểm là bug / lỗ hổng bảo mật / hiệu năng / tuân thủ / tích hợp? — hai nhánh dùng bộ câu hỏi khác nhau.
- Đây là hệ thống nội bộ cho 1 client, hay sản phẩm thương mại? (quyết định cách viết Business Goals và có cần Customer Discovery không)
- Vấn đề cốt lõi thuộc nhóm nào: Pain / Fear / Boredom / Money / Time Cost?
- Đâu là các miền quan tâm (Domains of Interest)? Gạch chân danh từ chủ đề lặp lại trong input.
- Sponsor / Client / Customer / User có trùng nhau không hay là 4 nhóm khác biệt?
- Nếu không làm gì cả, tổ chức mất gì (chi phí ẩn, mất khách hàng, tụt hậu)?

## 2. Capture Initial Artifacts
Liệt kê ngắn gọn nguồn dữ kiện đã dùng để suy luận ra tài liệu: email, slide, proposal, hệ thống hiện có/tương tự, hướng dẫn sử dụng, feature list, đặc tả yêu cầu ban đầu — dựa trên nội dung prompt của người dùng.

## 3. Phân loại nguồn gốc yêu cầu (RFP Classification)
Chọn đúng 1 trong 4 nhánh, vì mỗi nhánh có bộ câu hỏi khám phá khác nhau:

| Nhánh | Đặc điểm | Việc cần làm |
|---|---|---|
| RFP có vấn đề cụ thể | Client đã nêu rõ vấn đề | Xác nhận vấn đề, tìm hiểu hệ thống hiện tại, soạn solution + customer journey map + cost |
| RFP không có vấn đề cụ thể | Client biết cần đổi nhưng chưa rõ vấn đề | Xác định đây là **xây mới** hay **nâng cấp** (xem câu hỏi ở mục 1), rồi mới khám phá vấn đề |
| RFP nghiên cứu | Client muốn khảo sát công nghệ/xu hướng | Xác định công nghệ đối thủ đang/sắp dùng, đề xuất khả năng áp dụng |
| Cơ hội tự phát hiện (không có RFP) | Tự nhận ra pain point | Xác định sponsor tiềm năng, kiểm tra vấn đề có phổ biến trong ngành không (tham chiếu ≥2 trường hợp tương tự) |

## 4. Stakeholders
Tách RÕ RÀNG, không gộp:
- **Sponsor** — tài trợ ngân sách (tổ chức/nhóm/cá nhân)
- **Client** — trả tiền cho việc phát triển
- **Customer** — mua sản phẩm
- **User** — vận hành sản phẩm

Phân loại thêm **External stakeholder** (bên ngoài tổ chức) vs **Internal stakeholder** (nội bộ). Nếu có đủ dữ kiện, mô tả ngắn một Stakeholder Map (ai liên quan/bị ảnh hưởng, mối quan hệ, động lực từng nhóm).

Danh sách này là đầu vào cho **Stakeholder Analysis** đầy đủ (Register + Power/Interest Grid + Engagement Strategy) ở tài liệu Project Charter (`05-project-charter.md`) — ở đây chỉ cần xác định vai trò, chưa cần phân tích Power/Interest.

## 5. Problem Definition
Viết theo mẫu: *"Chúng ta không thể... / Việc này khó vì... / Chi phí quá cao vì..."*, sau đó diễn giải thành khoảng cách giữa trạng thái hiện tại (As-is) và trạng thái mục tiêu (To-be). Liệt kê chỉ số nền (Baseline Metrics) và tác động nếu không hành động (Impact of Inaction).

## 6. Business Goals
Với mỗi mục tiêu: **Purpose** (mục đích) → **Advantage** (lợi ích) → **Measurement** (chỉ số đo, tuỳ chọn) → kiểm tra bằng **SMART** (Cụ thể/Đo lường được/Khả thi/Liên quan/Có thời hạn).

- Hệ thống nội bộ cho client → mô tả vấn đề nghiệp vụ/quy trình cần cải thiện + môi trường sử dụng.
- Sản phẩm thương mại → mô tả cơ hội thị trường, so sánh với sản phẩm hiện có, lý do sản phẩm hấp dẫn.

Tham khảo nhóm mục tiêu phổ biến: giảm chi phí/thời gian, cải thiện dịch vụ khách hàng, cải thiện giao tiếp/ra quyết định, tăng cường quan hệ đối tác, hỗ trợ yêu cầu pháp lý mới, tạo sản phẩm/dịch vụ mới.

## 7. High-Level Features & Expected Deliverables
Danh sách tính năng mức cao (business-level) + danh mục sản phẩm/dịch vụ kỳ vọng: đặc tả yêu cầu, đặc tả kiểm thử, đặc tả thiết kế, hướng dẫn sử dụng/quản trị, môi trường production, công cụ migrate dữ liệu, source code, kế hoạch phát triển.

## 8. Context Diagram
Mô tả bằng lời hệ thống như một tiến trình duy nhất, xung quanh là các hệ thống liền kề (adjacent systems) — nêu ranh giới trách nhiệm giữa hệ thống và các bên liên quan; xác định phạm vi nghiên cứu (in-scope) và phần không nghiên cứu (out-of-scope).

## 9. Customer Discovery
Chỉ áp dụng nếu là sản phẩm thương mại: Ai được khảo sát (bạn bè, đồng nghiệp cũ, nhà đầu tư, khách hàng hiện tại)? Ở đâu (trường học, hội nghị, mạng xã hội)? Hỏi gì (nỗi đau, nhu cầu, lý do)? Bằng cách nào (survey, demo, bản dùng thử)?

## 10. Elevator/Evaluator Pitch
Công thức: Đối với [khách hàng mục tiêu] có [vấn đề], [sản phẩm] là [loại giải pháp] mang lại [lợi ích chính]; khác với [đối thủ/giải pháp hiện tại] ở điểm [khác biệt].

## 11. Checklist nội dung Project Proposal
Đảm bảo tài liệu bao trùm đủ: thị trường/đối tượng mục tiêu, ngân sách & tiến độ, pain points, giải pháp (core business use case), đối thủ/điểm yếu/khác biệt, rủi ro/điểm mạnh/cơ hội/tầm nhìn, mục tiêu kinh doanh & lợi ích dự kiến, báo cáo customer discovery (nếu có), tính năng cấp cao, sơ đồ ngữ cảnh, elevator pitch.
