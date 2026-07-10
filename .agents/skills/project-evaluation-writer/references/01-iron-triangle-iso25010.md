# Phần I–II — Tam giác sắt mở rộng & ISO/IEC 25010: hướng dẫn chi tiết

Đọc file này trước khi viết **Phần I. Tam giác sắt mở rộng** và **Phần II. Chất lượng sản phẩm phần mềm (ISO/IEC 25010)**.

## Mục lục
1. Câu hỏi tư duy bắt buộc
2. Nhóm I — Tam giác sắt mở rộng (Chow & Cao)
3. Nhóm II — Chất lượng sản phẩm (ISO/IEC 25010)

## 1. Câu hỏi tư duy bắt buộc

- Tài liệu có lộ trình/WBS/critical path cụ thể không, hay chỉ ước lượng "vài tuần/vài tháng" chung chung?
- Chi phí đưa ra là báo giá thực tế hay ước lượng minh họa với biên độ dao động lớn?
- Có mục "Out of scope" tường minh không — dấu hiệu tốt hiếm gặp, giúp tránh scope creep?
- Nếu dự án chưa có sản phẩm thực (giai đoạn business case), nhóm II chỉ chấm được theo ĐỊNH HƯỚNG kiến trúc mô tả trong tài liệu, không phải đo lường trực tiếp — phải nói rõ điều này trước khi vào bảng điểm.

## 2. Nhóm I — Tam giác sắt mở rộng (Chow & Cao)

_Nguồn tham chiếu: Chow & Cao; Stankovic và cộng sự — mở rộng tam giác Thời gian–Chi phí–Phạm vi bằng Chất lượng, Sự hài lòng khách hàng và Mục tiêu kinh doanh._

Chấm 6 tiêu chí, mỗi tiêu chí kèm bằng chứng trích dẫn cụ thể:

| Tiêu chí | Câu hỏi đánh giá |
|---|---|
| Thời gian | Có lộ trình/WBS/critical path xác định không? Có phương án rút ngắn (thí điểm/phân kỳ) không? Ước tính có buffer rủi ro (vd nhân sự kiêm nhiệm, phụ thuộc bên thứ 3) không? |
| Chi phí | Có bảng chi phí chi tiết theo hạng mục (TCO) không? Là báo giá thực tế hay ước lượng minh họa? Biên độ dao động rộng hay hẹp? |
| Phạm vi | Có mục Out-of-scope tường minh không? Tiêu chí gồm/loại trừ đã rõ ràng chưa, tránh scope creep? |
| Chất lượng | Có ngưỡng chất lượng đo lường được không (vd % độ chính xác, tỷ lệ pass test), hay chỉ nói "phải tốt/ổn định"? |
| Sự hài lòng khách hàng | Có KPI khảo sát mức hài lòng không? Dựa trên khảo sát người dùng thật hay chỉ persona/giả định chủ quan? |
| Mục tiêu kinh doanh | Có khớp rõ với chiến lược/định hướng tổ chức không? Có quy đổi lợi ích tài chính (ROI) hay chủ động bỏ qua vì lý do gì? |

## 3. Nhóm II — Chất lượng sản phẩm (ISO/IEC 25010)

_Chấm theo định hướng kiến trúc đã mô tả trong tài liệu nếu chưa có sản phẩm thực để đo lường trực tiếp._

| Tiêu chí | Câu hỏi đánh giá |
|---|---|
| Functional suitability | Đặc tả chức năng đủ chi tiết để kiểm chứng "đúng, đủ" chưa, hay chỉ liệt kê tên tính năng? |
| Performance efficiency | Có yêu cầu phi chức năng cụ thể không (SLA, thời gian phản hồi, số người dùng đồng thời)? |
| Compatibility | Có xác nhận tương thích với hệ thống hiện có chưa, hay chỉ "dự kiến tích hợp"? |
| Usability | Có kế hoạch kiểm thử usability với người dùng thật không, hay chỉ UAT chung chung? |
| Reliability | Có SLA uptime hay kế hoạch khôi phục thảm họa (DR) cụ thể không, hay chỉ nói "có sao lưu"? |
| Security | Rủi ro bảo mật/dữ liệu cá nhân có giải pháp kỹ thuật cụ thể không, hay chỉ nói chung chung ("rà soát", "bảo mật tốt")? |
| Maintainability | Lựa chọn công nghệ có giảm phụ thuộc vendor, dễ bảo trì lâu dài không (vd nền tảng mã nguồn mở trưởng thành)? |
| Portability | Kiến trúc có vendor lock-in nặng không? |
