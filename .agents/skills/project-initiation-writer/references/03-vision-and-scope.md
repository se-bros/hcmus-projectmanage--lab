# Vision & Scope (WHAT) — hướng dẫn chi tiết

Đọc file này trước khi viết tài liệu **Project Vision & Scope** — trả lời câu hỏi WHAT (hệ thống làm gì cho user), thường được xuất bản dưới dạng PDF gửi cho stakeholder; ở đây tạo phần nội dung nguồn dạng Markdown.

## Mục lục

1. Câu hỏi tư duy bắt buộc
2. Glossary & Business Rules
3. Feature Model, Feature Tree & MVP
4. Vision — Black-box Solution (Current/Future Situation)
5. Project Scope Statement
6. Mockup, Prototype & PoC

## 1. Câu hỏi tư duy bắt buộc

- Ai là user thực sự, và vấn đề/nhu cầu/mục tiêu của họ là gì? Có phương án "không cần phần mềm" hoặc giải pháp black-box đơn giản hơn giải quyết được vấn đề không, trước khi mặc định cần xây hệ thống phức tạp?
- Chiến lược MVP là gì để tối ưu thời gian ra mắt?
- Từng nhóm tính năng nên biểu diễn bằng quan hệ nào — And / Alternative / Or / Mandatory / Optional? Nếu chỉ dùng AND xuyên suốt → đây là **Feature Tree** (đơn giản); nếu có Alternative/Or → phải trình bày như **Feature Model** đầy đủ (xem mục 3).
- Với mỗi feature định đưa vào tài liệu: nó có xuất phát từ 1 vấn đề thật (Spot the problem) không, có phổ biến ở nhiều khách hàng cùng ngành không (Talk to two — tìm 2 khách hàng khác cùng ngành xác nhận), hay chỉ là suy đoán chủ quan cần đánh dấu "đề xuất — cần xác thực"? Quy trình xác thực đầy đủ: Spot the problem → Talk to two → Understand it → Prototype it → Inspect them (theo dõi người dùng thật thao tác trên bản mẫu chạy được).
- Luồng UI/UX nào rủi ro nhất, cần làm mockup để người dùng thật xác nhận trước khi code?
- Vấn đề kỹ thuật/thuật toán (problem solving) nào khó nhất, không chắc khả thi, cần làm Proof of Concept trước khi cam kết kiến trúc?

## 2. Glossary & Business Rules

- **Glossary:** định nghĩa từ khóa quan trọng, kèm quy tắc hợp lệ/định dạng dữ liệu nếu liên quan (độ dài trường, định dạng mã...).
- **Business Rules:** với mỗi rule, nêu rõ **Source** (nguồn/luật/chính sách quy định) và mức độ biến động — ưu tiên (vd: "Cao — thay đổi hàng năm theo luật thuế"). Rule không rõ nguồn → đánh dấu `[Cần xác nhận nguồn]`.

## 3. Feature Model, Feature Tree & MVP

Phân biệt bắt buộc:

- **Feature Model** — đầy đủ 4 loại quan hệ cha-con: **And** (tất cả sub-feature bắt buộc), **Alternative** (chỉ chọn 1), **Or** (chọn ≥1), **Mandatory/Optional**.
- **Feature Tree** — phiên bản đơn giản hơn, CHỈ dùng quan hệ AND. Không gọi lẫn hai thứ này.

Mỗi feature quan trọng viết theo mẫu:

> User [ai] → Business goal [vấn đề cần giải] → Metric [đo bằng gì] → Action [tính năng đề xuất]

Chỉ định rõ nhóm tính năng nào thuộc MVP (Minimum Viable Product).

## 4. Vision — Black-box Solution (Current/Future Situation)

Vision & Scope mô tả hệ thống là một **"black-box solution"** — mô tả CÁI GÌ hệ thống làm cho người dùng, KHÔNG mô tả CÁCH nó được xây (đó là việc của tài liệu Architecture — `06-architecture.md`). Nội dung cần có đủ, theo đúng cặp Hiện tại → Tương lai:

- Bối cảnh/tổng quan
- **Current Situation** (Trạng thái hiện tại của user):
  - Business use case hiện tại — quy trình/workflow user đang thao tác thủ công hoặc trên hệ thống cũ
  - Domain model hiện tại
  - Vấn đề của user hiện tại và mục tiêu tương ứng
- **Future Situation** (Trạng thái tương lai sau dự án):
  - Business use case tương lai — workflow mới sau khi hệ thống ra đời
  - Domain model tương lai
  - Thành phần/tính năng SẼ phát triển để đạt mục tiêu đã nêu ở Current Situation
  - Thành phần/tính năng SẼ loại trừ (out of scope)
- Giả định, rủi ro
- Kết luận

## 5. Project Scope Statement

Mô tả phạm vi sản phẩm (product scope description), **Deliverables** (sản phẩm bàn giao), **Project Exclusions** (hạng mục loại trừ — những gì chắc chắn không làm), **Constraints** (ràng buộc), **Acceptance Criteria** (tiêu chí nghiệm thu), **Assumptions** (giả định). Phải nêu rõ dự án SẼ làm gì và KHÔNG làm gì — tránh scope creep.

## 6. Mockup, Prototype & PoC

Phần này trực quan hóa các workflow/feature đã mô tả ở mục 4 trước khi cam kết đầu tư phát triển đầy đủ:

- **Thiết kế Prototype:** các luồng UI/UX trọng yếu (thường là luồng thuộc Future Situation) cần trực quan hóa trước khi lập trình, để user thật xác nhận đúng nhu cầu.
- **Mục tiêu PoC:** giới hạn công nghệ/thuật toán cần thử nghiệm để chứng minh tính khả thi kỹ thuật trước khi đầu tư toàn bộ — đặc biệt với các feature mới, chưa có tiền lệ trong hệ thống hiện tại.
