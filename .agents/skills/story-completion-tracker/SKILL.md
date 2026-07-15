---
name: StoryCompletionTracker
description: Kích hoạt khi một thành viên trong nhóm báo đã hoàn thành (xong, done, complete) một story, user story, hoặc task trong Product Backlog. Skill ghi nhận dòng log vào file project_log.md và cập nhật tổng cộng cho cả nhóm.
---

# Ghi nhận hoàn thành Story cho nhóm Dev

## Phạm vi duy nhất

Skill này CHỈ làm hai việc:

1. Thêm một dòng log khi thành viên báo hoàn thành story.
2. Cộng lại tổng 3 cột số cho cả nhóm.

Skill này KHÔNG tính velocity, KHÔNG dự báo tiến độ dự án, KHÔNG tính chi phí. Nếu người dùng hỏi về những việc đó, trả lời: *"Việc tổng hợp velocity, dự báo tiến độ và chi phí nằm ngoài phạm vi skill này. Bạn có thể tự tính từ dữ liệu trong file project_log.md."*

## File dùng chung

- Tên file cố định: `project_log.md`
- Một file duy nhất dùng chung cho cả nhóm (không phải mỗi người một file).
- File chứa một bảng duy nhất với các cột:

| Ngày hoàn thành | Dev | Story ID | Tên Story | Story Points | Thời gian làm (giờ) | Token AI đã dùng | Ghi chú |

- Dòng cuối cùng của bảng luôn là dòng **"Tổng cộng (cả nhóm)"** — chỉ cộng 3 cột số: Story Points, Thời gian làm (giờ), Token AI đã dùng.

## Quy trình khi thành viên báo "vừa xong story"

### Bước 1 — Tìm hoặc tạo file

- Tìm file `project_log.md` trong thư mục gốc của dự án.
- **Nếu đã có:** mở và cập nhật trực tiếp file đó. Tuyệt đối không tạo file mới.
- **Nếu chưa có:** sao chép từ template tại đường dẫn tương đối `.agents/skills/story-completion-tracker/templates/project_log.md`, đặt vào thư mục gốc dự án với đúng tên `project_log.md`.

### Bước 2 — Thu thập thông tin

Hỏi người dùng các thông tin sau. Không hỏi lại trường nào đã biết rõ:

| Trường | Mô tả | Bắt buộc |
|---|---|---|
| Ngày hoàn thành | Ngày story được hoàn thành (mặc định là ngày hôm nay nếu người dùng xác nhận) | Có |
| Dev | Tên thành viên thực hiện | Có |
| Story ID | Mã định danh story trong backlog | Có |
| Tên Story | Tên mô tả ngắn gọn của story | Có |
| Story Points | Điểm ước lượng của story | Có |
| Thời gian làm (giờ) | Số giờ thực tế dev tự khai | Có |
| Token AI đã dùng | Số token AI dev tự khai | Có |
| Ghi chú | Tool AI nào đã dùng, hoặc ghi chú khác | Không (để trống nếu không có) |

**Nguyên tắc bao trùm:** Nếu bất kỳ trường bắt buộc nào thiếu hoặc mơ hồ — PHẢI hỏi lại để làm rõ. Không tự đoán, không tự bịa số, không điền giá trị mặc định cho các trường số (Story Points, Thời gian làm, Token AI).

### Bước 3 — Thêm dòng mới

- Chèn dòng mới ngay **phía trên** dòng "Tổng cộng (cả nhóm)".
- **Không sửa**, **không xoá**, **không sắp xếp lại** bất kỳ dòng cũ nào của thành viên khác.

### Bước 4 — Cập nhật tổng

- Cộng lại toàn bộ giá trị trên **tất cả các dòng** cho 3 cột: Story Points, Thời gian làm (giờ), Token AI đã dùng.
- Ghi đè dòng "Tổng cộng (cả nhóm)" bằng tổng mới.

### Bước 5 — Xác nhận

- Xác nhận ngắn gọn với người dùng:
  - Dòng vừa thêm (hiển thị đầy đủ các trường).
  - Số tổng mới của 3 cột.
- **Không tự tính thêm bất kỳ chỉ số nào khác** (không velocity, không ngày dự kiến hoàn thành, không chi phí).

## Ràng buộc quan trọng

1. **Không đè lên dòng của thành viên khác.** Mỗi lần chỉ thêm dòng mới và cập nhật dòng tổng.
2. **Thiếu thông tin → hỏi lại.** Không bao giờ tự bịa số liệu.
3. **Ngoài phạm vi → từ chối lịch sự.** Gợi ý người dùng tự tính từ dữ liệu có sẵn.
4. **Giữ skill đơn giản.** Không thêm workflow, tính năng, hoặc bảng phụ nào ngoài log + cộng tổng.
