# ĐỀ CƯƠNG ÔN TẬP — NGƯỜI 4: ƯỚC LƯỢNG, LẬP KẾ HOẠCH & QUY TRÌNH

- **Phạm vi phụ trách:** **Câu 9, Câu 10, Câu 11**
- **Tài liệu tham chiếu chính trong dự án:**
  - [`docs/02-planning/04-cost-time-resource.md`](../../docs/02-planning/04-cost-time-resource.md)
  - [`docs/03-execution-monitoring/01-sprint-plan.md`](../../docs/03-execution-monitoring/01-sprint-plan.md)
  - [`docs/02-planning/03-product-backlog.md`](../../docs/02-planning/03-product-backlog.md) (Mục Quy trình Kanban & DoD)
- **Bản in cần nộp kèm khi thi:** Bản in file `04-cost-time-resource.md` (mục UCP & COCOMO II) và `01-sprint-plan.md`.

---

## CÂU 9: ĐỊNH NGHĨA QUY TRÌNH PHÁT TRIỂN PHẦN MỀM

> **Câu hỏi chính:** Trình bày quá trình hình thành và phương pháp đánh giá tài liệu Định nghĩa quy trình phát triển phần mềm của nhóm.

### 1. Dàn ý trả lời 4 câu hỏi vàng:
* **WHAT (Là gì?):** Là tài liệu quy định phương pháp luận phát triển mà nhóm áp dụng: Mô hình **Agile/Kanban Spec-Driven kết hợp AI Coding Assistant**.
* **HOW (Cách nhóm thực hiện):**
  1. *Quy tắc Kanban:* Giới hạn công việc đang làm (WIP Limit = 1 card/người), kéo việc theo nhu cầu (Pull System) thay vì giao việc cứng nhắc.
  2. *Quy trình Spec-Driven 4 bước:* Viết Spec $\rightarrow$ Prompt AI Coding $\rightarrow$ Chạy Unit Test/Kiểm thử tự động $\rightarrow$ Human Code Review & Merge.
  3. *Chốt chặn chất lượng (Gating):* Định nghĩa rõ ràng DoD (Definition of Done) 5 tiêu chí trước khi card được chuyển sang cột `Done`.
* **WHY (Tại sao cần làm?):** Tối ưu hóa sự phối hợp giữa người và AI, tránh tình trạng tạo ra quá nhiều code AI mà không kiểm soát được chất lượng hoặc nghẽn ở khâu review.
* **EVIDENCE (Minh chứng dự án):** Quy tắc Kanban trong `03-product-backlog.md` mục 1.1, phân công Sprint 1 trong `01-sprint-plan.md`.

---

## CÂU 10: ƯỚC LƯỢNG DỰ ÁN (PROJECT ESTIMATE)

> **Câu hỏi chính:** Trình bày quá trình hình thành và phương pháp đánh giá tài liệu Ước lượng dự án của nhóm.

### 1. Dàn ý trả lời 4 câu hỏi vàng:
* **WHAT (Là gì?):** Là quá trình tính toán khoa học về Nỗ lực (Effort), Thời gian (Schedule) và Chi phí (Cost) cần thiết để hoàn thành dự án bằng cách kết hợp 2 phương pháp đối chuẩn: Top-Down (Use Case Points) và Bottom-Up (COCOMO II).
* **HOW (Cách nhóm thực hiện):**
  1. *Phương pháp Top-Down (Use Case Points - UCP):*
     - Đánh giá độ phức tạp Actor: UAW = 12.
     - Đánh giá độ phức tạp Use Case: UUCW = 130 $\rightarrow$ UUCP = 142.
     - Tính hệ số kỹ thuật TCF = 1.13, hệ số môi trường ECF = 0.785.
     - **AUCP (Điểm hiệu chỉnh) = 142 × 1.13 × 0.785 ≈ 126 UCP**.
     - Nỗ lực thô: 126 UCP × 20 giờ = 2.520 giờ ≈ 15.75 Person-Months. Trừ 40% tái sử dụng open-source $\rightarrow$ **~5.0 tháng của 4 dev kiêm nhiệm 50% (2 FTE)**.
  2. *Phương pháp Bottom-Up (COCOMO II - Early Design):*
     - Quy mô code viết mới: 3.5 KLOC (Backend FastAPI + Frontend React).
     - Công thức: $Effort = 2.94 \times (Size)^{1.05} \times EAF = 2.94 \times (3.5)^{1.05} \times 0.95 \approx \mathbf{10.4\text{ Person-Months}}$.
  3. *Đối chuẩn kết quả:* Hai phương pháp độc lập cho ra kết quả tương thích cao (~10.4 PM và 9.5 PM sau trừ reuse), khẳng định dự án có thể hoàn thành trong lộ trình 20 tuần.
* **WHY (Tại sao cần làm?):** Giúp dự toán ngân sách chính xác, tránh việc "hứa lèo" với khách hàng hoặc thiếu hụt kinh phí giữa chừng.
* **EVIDENCE (Minh chứng dự án):** Bảng tính UCP và COCOMO II chi tiết trong file `04-cost-time-resource.md`.

---

## CÂU 11: KẾ HOẠCH DỰ ÁN (PROJECT PLAN)

> **Câu hỏi chính:** Trình bày quá trình hình thành và phương pháp đánh giá tài liệu Kế hoạch dự án của nhóm.

### 1. Dàn ý trả lời 4 câu hỏi vàng:
* **WHAT (Là gì?):** Là bản kế hoạch phân rã công việc (Work Breakdown Structure - WBS), xác định trình tự thực hiện, các mốc thời gian bàn giao (Milestones) và nhận diện **Đường găng (Critical Path)** của dự án.
* **HOW (Cách nhóm thực hiện):**
  1. *Phân rã 6 Gói công việc (WBS):*
     - WP1: Khảo sát & Bản quyền (Tuần 1–3)
     - WP2: CSDL & Backend API (Tuần 4–7)
     - WP3: Giao diện React & Reader (Tuần 8–11)
     - **WP4: Số hóa tài liệu [Đường găng] (Tuần 12–17)**
     - WP5: Kiểm thử & UAT (Tuần 18–19)
     - WP6: Triển khai & Ra mắt (Tuần 20)
  2. *Xác định Đường găng:* WP4 (Số hóa 500 giáo trình và soát lỗi OCR) là khâu dài nhất (6 tuần) và phụ thuộc vào năng suất người quét sách. Sự chậm trễ ở WP4 sẽ trực tiếp làm trễ hạn toàn bộ dự án.
* **WHY (Tại sao cần làm?):** Giúp PM chủ động phân bổ nguồn lực vào các công việc thuộc đường găng để không bị trễ deadline bàn giao.
* **EVIDENCE (Minh chứng dự án):** Kế hoạch Sprint 1 trong `01-sprint-plan.md` và Sơ đồ WBS trong `04-cost-time-resource.md`.
