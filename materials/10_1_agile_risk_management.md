# Quản lý rủi ro linh hoạt (Agile Risk Management)

**Giảng viên / Lecturer:** Ngô Huy Biên (Ngo Huy Bien) — nhbien@fit.hcmus.edu.vn
**Đơn vị / Department:** Bộ môn Kỹ thuật phần mềm, Khoa Công nghệ thông tin, Trường Đại học Khoa học Tự nhiên, ĐHQG-HCM
**Môn học / Course:** Quản lý Dự án Phần mềm (Software Project Management)

---

## 1. Mục tiêu bài học (Learning Objectives)

Sau bài học, người học có thể:

- Xác định rủi ro dự án.
  *(Identify project risks.)*
- Phân tích rủi ro dự án một cách khoa học.
  *(Analyze project risks.)*
- Đề xuất và lựa chọn các phản ứng rủi ro phù hợp.
  *(Propose and select risk responses.)*
- Lập kế hoạch quản lý rủi ro.
  *(Create risk management plan.)*
- Theo dõi và giám sát rủi ro dự án xuyên suốt.
  *(Monitor and track project risks.)*

## 2. Nội dung (Contents Overview)

| # | Chủ đề (VI) | Topic (EN) |
|---|---|---|
| I | Bản chất rủi ro & Đánh giá tiếp cận | Nature of Risk & Process Approach Evaluation |
| II | Xác định hệ số rủi ro | Determine Risk Multipliers |
| III | Nhận diện & Phân tích rủi ro dự án | Identify & Analyze Project Risks |
| IV | Ứng phó rủi ro | Respond to Risks |

---

## I. Bản chất rủi ro & Đánh giá tiếp cận (Nature of Risk & Process Evaluation) \[1\]

### 1.1 Tại sao dự án thất bại?
Vận tốc (velocity) của nhóm chỉ phản ánh những vấn đề thường gặp. Trong thực tế, cuộc sống luôn mang đến những biến cố bất ngờ (curve balls):
- Thành viên bị bệnh hoặc nghỉ phép.
- Ổ cứng bị hỏng.
- Bản sao lưu hoạt động tốt nhưng không thể khôi phục (restore) được.
- Phát sinh yêu cầu mới từ khách hàng.
- Công việc bị gián đoạn.

### 1.2 Đánh giá cách tiếp cận quy trình

| Tiếp cận quy trình Nghiêm ngặt (Rigorous Process) | Tiếp cận quy trình Rủi ro (Risky Process) |
|---|---|
| - Tuân thủ nghiêm ngặt "Định nghĩa hoàn thành" (Definition of Done).<br>- Vận tốc ổn định.<br>- Sửa tất cả các lỗi của lần lặp (iteration) trước.<br>- Hoàn thành trọn vẹn công việc của iteration. | - Không tuân thủ chặt chẽ quy trình chuẩn.<br>- Vận tốc không ổn định.<br>- Để lại lỗi từ các iteration trước không giải quyết triệt để.<br>- Chạy đua theo tiến độ bằng mọi giá. |

---

## II. Xác định hệ số rủi ro (Determine Risk Multipliers)

Để lập kế hoạch phát hành đáng tin cậy, ta cần áp dụng hệ số rủi ro vào vận tốc của nhóm dựa trên cách tiếp cận quy trình:

**Bảng hệ số rủi ro chung (Generic Risk Multipliers):**

| Khả năng hoàn thành đúng hạn | Hệ số quy trình Nghiêm ngặt | Hệ số quy trình Rủi ro | Ý nghĩa |
|---|---|---|---|
| **10%** | $\times 1.0$ | $\times 1.0$ | Hầu như không thể ("Ignore" - phớt lờ) |
| **50%** | $\times 1.4$ | $\times 2.0$ | Cơ hội 50-50 ("Stretch goal" - mục tiêu thách thức) |
| **90%** | $\times 1.8$ | $\times 4.0$ | Hầu như chắc chắn ("Commit" - cam kết) |

**Ví dụ áp dụng hệ số rủi ro:**
- Quy trình áp dụng: **Nghiêm ngặt** (Rigorous).
- Vận tốc trung bình của nhóm: **14 điểm** (Velocity = 14 points).
- Số lần lặp (Sprint) còn lại: **10** (Sprints left = 10).

*Dự toán số điểm câu chuyện có thể hoàn thành theo các mức tin cậy:*
- Mức tin cậy 10% (Không thể): $10 \text{ Sprints} \times 14 \text{ points} / 1.0 = \mathbf{140 \text{ points}}$
- Mức tin cậy 50% (Thách thức): $10 \text{ Sprints} \times 14 \text{ points} / 1.4 = \mathbf{100 \text{ points}}$
- Mức tin cậy 90% (Cam kết): $10 \text{ Sprints} \times 14 \text{ points} / 1.8 = \mathbf{78 \text{ points}}$

---

## III. Nhận diện & Phân tích rủi ro dự án (Identify & Analyze Project Risks)

### 3.1 Động não về rủi ro (Brainstorm Project-Specific Risks)
Hãy tự đặt các câu hỏi để nhận diện rủi ro:
- Điều gì về dự án khiến bạn lo lắng mất ngủ? *(What keeps you up at night?)*
- Một năm sau khi dự án thất bại thảm hại, bạn trả lời phỏng vấn thế nào về lý do đổ vỡ?
- Viết ra kịch bản ngược lại với những giấc mơ tốt đẹp nhất của bạn về dự án.
- Dự án thất bại mà không ai có lỗi bằng cách nào?
- Dự án sẽ thất bại thế nào nếu lỗi thuộc về: khách hàng? lập trình viên? QA? hay chính bạn?
- Dự án thành công nhưng để lại một stakeholder tức giận bằng cách nào?

**Các rủi ro phổ biến từ thực tế:** Thiếu thời gian; làm việc trên công nghệ mới; thiếu năng lực lãnh đạo; không thực hiện báo cáo trạng thái; yêu cầu không rõ ràng (thiếu kiến thức nghiệp vụ).

### 3.2 Phân tích rủi ro (Analyze Risks)
Đối với mỗi rủi ro được nhận diện, xác định:
- **Xác suất xảy ra (Probability):** Cao (High), Trung bình (Medium), Thấp (Low).
- **Tác động (Impact):** Thiệt hại cụ thể về tài chính, số ngày trễ hạn, hoặc hủy bỏ dự án.

---

## IV. Ứng phó rủi ro (Respond to Risks)

### 4.1 Các biện pháp phản ứng với rủi ro
1. **Tránh rủi ro (Avoid):** Không thực hiện hành động rủi ro đó nữa.
2. **Ngăn chặn rủi ro (Contain):** Dự trữ thêm thời gian hoặc ngân sách (như áp dụng hệ số rủi ro ở mục II).
3. **Giảm thiểu rủi ro (Mitigate):** Thực hiện các bước chủ động để giảm thiểu khả năng xảy ra hoặc giảm tác động của rủi ro.
*(Có thể kết hợp các biện pháp này với nhau).*

### 4.2 Thiết lập kế hoạch ứng phó rủi ro chi tiết
- **Chỉ báo chuyển tiếp (Transition Indicators):** Dấu hiệu nhận biết rủi ro đã trở thành hiện thực.
- **Hoạt động giảm thiểu (Mitigation Activities):** Viết thành các user story giảm thiểu rủi ro (Risk Mitigation Stories) và thêm vào kế hoạch phát hành.
- **Hoạt động dự phòng (Contingency Activities):** Các hành động chỉ kích hoạt nếu rủi ro thực sự xảy ra (Risk Contingency Stories).
- **Mức độ phơi bày rủi ro (Risk Exposure):** Phản ánh lượng thời gian/ngân sách cần thiết dự phòng để kiểm soát rủi ro.

---

## Tài liệu tham khảo (References)

1. James Shore & Shane Warden (2008). *The Art of Agile Development*. O'Reilly.
