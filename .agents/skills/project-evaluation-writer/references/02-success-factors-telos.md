# Phần III–IV — Yếu tố Thành công & TELOS: hướng dẫn chi tiết

Đọc file này trước khi viết **Phần III. Yếu tố Quyết định Thành công** và **Phần IV. Khả thi trước triển khai (TELOS)**.

## Mục lục
1. Câu hỏi tư duy bắt buộc
2. Nhóm III — Yếu tố Quyết định Thành công (Pinto & Slevin; Standish CHAOS)
3. Nhóm IV — Khả thi trước triển khai (TELOS)
4. Cảnh báo Rủi ro trọng yếu

## 1. Câu hỏi tư duy bắt buộc

- Tài liệu có phân biệt rõ "khảo sát người dùng thật" với "persona/câu chuyện minh họa giả định" không? Đây là điểm dễ bị đánh giá quá cao nếu không tra kỹ.
- Hỗ trợ quản lý cấp cao là cam kết thực tế (chữ ký, văn bản phê duyệt) hay chỉ nằm trong danh sách vai trò dự kiến?
- Rủi ro pháp lý (bản quyền, quyền riêng tư, tuân thủ luật) đã có quy trình xử lý cụ thể chưa, hay chỉ được "liệt kê" trong bảng rủi ro mà chưa có giải pháp?
- Sau khi chấm xong 2 nhóm này, có tiêu chí nào ≤4/10 thuộc loại rủi ro "có thể sụp đổ cả dự án" không (xem mục 4)?

## 2. Nhóm III — Yếu tố Quyết định Thành công (Pinto & Slevin; Standish CHAOS)

_Nguồn tham chiếu: mô hình 10 yếu tố của Pinto & Slevin; các yếu tố thành công theo báo cáo CHAOS của Standish Group._

| Tiêu chí | Câu hỏi đánh giá |
|---|---|
| Sứ mệnh dự án | Có rõ ràng, được nêu ngay từ phần đầu tài liệu không? |
| Hỗ trợ quản lý cấp cao | Có cam kết/phê duyệt thực tế (chữ ký, văn bản) hay chỉ nằm trong bảng phân vai dự kiến? |
| Lịch trình / kế hoạch | Có WBS và timeline chi tiết theo từng gói công việc không? |
| **Tham vấn người dùng** | Có dữ liệu khảo sát/phỏng vấn người dùng thật không, hay chỉ persona giả định? Theo CHAOS Report đây là yếu tố quan trọng NHẤT cho thành công dự án CNTT — nếu chỉ có persona giả định, chấm ≤3-4/10 và ghi rõ đây là điểm yếu chí mạng, không chấm điểm khoan hồng vì "có nêu ra vấn đề". |
| Nhân sự | Có xác nhận năng lực và thời gian rảnh thực tế của đội ngũ thực thi không, hay chỉ giả định? |
| Giám sát & phản hồi | Có cơ chế báo cáo định kỳ cụ thể (ai báo cáo, tần suất bao lâu) không? |
| Giao tiếp | Có kế hoạch truyền thông chi tiết giữa các bên liên quan trong quá trình triển khai không, hay chỉ có bảng danh sách stakeholder? |
| Xử lý sự cố | Có bảng rủi ro với risk owner cụ thể cho từng mục không? |

## 3. Nhóm IV — Khả thi trước triển khai (TELOS)

| Tiêu chí | Câu hỏi đánh giá |
|---|---|
| Kỹ thuật | Công nghệ đề xuất đã được kiểm chứng rộng rãi (rủi ro thấp) hay còn thử nghiệm/rủi ro cao? |
| Kinh tế | Có báo giá thực tế hay chỉ ước lượng với biên độ quá rộng để dùng phê duyệt ngân sách chính thức? |
| **Pháp lý** | Thường là điểm rủi ro dễ bị bỏ sót nhất. Kiểm tra: có vấn đề bản quyền/quyền riêng tư/tuân thủ pháp luật nào được liệt kê là rủi ro nhưng CHƯA có quy trình xử lý cụ thể (vd: cơ chế đồng ý/consent, xử lý dữ liệu cá nhân theo luật) không? Nếu có → chấm thấp (≤3-4/10) và cảnh báo rõ đây là loại rủi ro có thể CHẶN ĐỨNG dự án, cần giải quyết TRƯỚC khi triển khai, không phải xử lý song song. |
| Vận hành | Có kế hoạch đào tạo, truyền thông VÀ cam kết nhân sự vận hành lâu dài sau go-live không? |
| Tiến độ | Có phương án linh hoạt (toàn bộ vs. thí điểm/phân kỳ) không? |

## 4. Cảnh báo Rủi ro trọng yếu

Sau khi chấm xong Nhóm III và IV: nếu có ≥2 tiêu chí điểm ≤4/10 thuộc loại rủi ro có thể sụp đổ cả dự án bất kể chất lượng kỹ thuật/chiến lược tốt đến đâu (thường rơi vào Tham vấn người dùng và Pháp lý, nhưng không giới hạn — có thể là Kinh tế hoặc Hỗ trợ cấp cao tuỳ dự án cụ thể), PHẢI xuất một khối cảnh báo riêng ngay sau bảng điểm, dạng:

> **Rủi ro trọng yếu:** [nêu đích danh các tiêu chí điểm thấp và lý do vì sao chúng có thể chặn đứng dự án bất kể điểm tổng thể ra sao].

Không để điểm số tự nói — người đọc báo cáo (thường là ban lãnh đạo) cần một câu cảnh báo tường minh không thể bỏ sót.
