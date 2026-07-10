# Phần VII–VIII — DORA & Post-Implementation Review: hướng dẫn chi tiết

Đọc file này trước khi viết **Phần VII. Chỉ số kỹ thuật/DevOps (DORA)** và **Phần VIII. Hậu triển khai (PIR)**.

## Mục lục
1. Câu hỏi tư duy bắt buộc
2. Trường hợp dự án CHƯA triển khai
3. Trường hợp dự án ĐANG triển khai
4. Trường hợp dự án ĐÃ hoàn thành/go-live

## 1. Câu hỏi tư duy bắt buộc

- Giai đoạn dự án (xác định ở Phần 0) là gì — quyết định 2 nhóm này N/A toàn bộ, N/A một phần, hay chấm đầy đủ?
- Nếu N/A, tài liệu đầu vào đã có sẵn bộ KPI/tiêu chí thành công để làm cơ sở đối chiếu khi PIR diễn ra sau này chưa? Đây là điểm cộng đáng ghi nhận dù nhóm chính N/A.

## 2. Trường hợp dự án CHƯA triển khai (chưa có dòng code/deploy nào)

Đánh dấu N/A toàn bộ Nhóm VII và VIII — nêu rõ đây là điều BÌNH THƯỜNG ở giai đoạn hiện tại, KHÔNG phải điểm trừ, vì chưa có dữ liệu vận hành thực tế để đo (deploy frequency, mật độ lỗi, đối chiếu kết quả thật).

Thay vào đó, chấm 1 tiêu chí phụ duy nhất: **"Mức độ sẵn sàng của kế hoạch KPI/PIR"** — dựa trên việc tài liệu đầu vào đã có sẵn bộ KPI/tiêu chí thành công cụ thể (không chỉ định tính) để làm cơ sở đối chiếu khi PIR diễn ra sau này hay chưa.

## 3. Trường hợp dự án ĐANG triển khai (có code/deploy một phần, chưa go-live toàn bộ)

- Chấm Nhóm VII dựa trên dữ liệu thực tế nếu có sẵn — 4 chỉ số DORA chuẩn:
  - **Deployment Frequency** — tần suất triển khai lên production.
  - **Lead Time for Changes** — thời gian từ commit đến khi chạy trên production.
  - **Change Failure Rate** — tỷ lệ thay đổi gây lỗi/phải rollback.
  - **Mean Time to Restore (MTTR)** — thời gian trung bình khôi phục sau sự cố.
- Nhóm VIII vẫn N/A cho đến khi go-live toàn bộ, vì PIR cần đối chiếu kết quả cuối với mục tiêu ban đầu.

## 4. Trường hợp dự án ĐÃ hoàn thành / đã go-live

Chấm đầy đủ cả 2 nhóm:

- **Nhóm VII (DORA):** dùng dữ liệu vận hành thực tế đã tích lũy được.
- **Nhóm VIII (PIR):** theo checklist chuẩn — đối chiếu mục tiêu ban đầu (Business Goals, KPI đã đề ra) với kết quả thật đạt được; ghi nhận bài học kinh nghiệm (lessons learned); kết luận có nên nhân rộng/tiếp tục đầu tư giai đoạn tiếp theo hay không.
