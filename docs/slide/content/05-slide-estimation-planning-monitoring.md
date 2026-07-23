# SLIDE DECK — PHẦN 5: SOFTWARE PROJECT ESTIMATION, PLANNING, MONITORING & CONTROL
## Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS (HCMUS-LDMS)

> Nguồn nội dung: `08-cost-time-resource.md`, `05-project-charter.md` (mục 2 — Project Checklist)
> Số lượng slide đề xuất: **15 slide**

---

## Slide 1 — Trang bìa

**Loại slide:** Title Slide

**Nội dung:**
- Tiêu đề: Ước lượng, Lập kế hoạch & Giám sát Dự án
- Phụ đề: "UCP · COCOMO II · Velocity-based Forecast · AI Session Logging"

**Gợi ý thiết kế:**
- Giữ tông kỹ thuật/định lượng: nền dạng lưới số liệu (data grid) mờ, font số liệu rõ ràng (tabular figures)

**Ghi chú thuyết trình:** Đây là phần "đo lường" khép lại toàn bộ bộ tài liệu — trả lời câu hỏi "làm sao biết dự án đang đi đúng hướng và đúng ngân sách".

---

## Slide 2 — Lộ trình 4 giai đoạn & Đường găng (Critical Path)

**Loại slide:** Timeline + Critical Path

**Nội dung:**
- GĐ0 (Tuần 1–2): Khảo sát & Bản quyền
- GĐ1 (Tuần 3–12): Xây dựng MVP & thí điểm 500 sách CNTT
- GĐ2 (Tuần 13–18): Số hóa diện rộng 2.000 giáo trình
- GĐ3 (Tuần 19–20): UAT, pentest, go-live
- **Đường găng (Critical Path): WP4 — Số hóa tài liệu (Tuần 12–17)** — phụ thuộc năng suất con người (scan + soát lỗi), chậm trễ ở đây kéo lùi toàn bộ ngày bàn giao

**Gợi ý thiết kế:**
- Timeline Gantt đơn giản hóa, WP4 tô đậm màu đỏ/cam dọc theo đường găng để nổi bật giữa các WP khác (màu trung tính)
- Dùng Visualizer diagram module để dựng Gantt/timeline trực quan

**Ghi chú thuyết trình:** Nhấn mạnh: mọi nỗ lực quản lý rủi ro tiến độ nên tập trung vào WP4, đây là nút thắt cổ chai thực sự của cả dự án.

---

## Slide 3 — Ước lượng bằng phương pháp Use Case Points (UCP)

**Loại slide:** Estimation Method 1 — UCP

**Nội dung:**
- Bước 1: UAW (trọng số tác nhân) = 12
- Bước 2: UUCW (trọng số use case) = 130 (Simple 30 + Average 40 + Complex 60)
- Bước 3: UUCP chưa điều chỉnh = UAW + UUCW = **142 points**
- Bước 4–5: TCF (hệ số kỹ thuật) = 1.13; ECF (hệ số môi trường) = 0.785
- Bước 6: AUCP đã điều chỉnh = 142 × 1.13 × 0.785 ≈ **126 UCP**
- Bước 7: Effort = 126 × 20 người-giờ/UCP = 2.520 người-giờ ≈ 15.75 PM → điều chỉnh thực tế (tái sử dụng mã nguồn 40%) còn **10 PM** (~5 tháng)

**Gợi ý thiết kế:**
- Sơ đồ dạng "phễu tính toán" (funnel/waterfall số liệu) — mỗi bước là 1 tầng số liệu đổ xuống tầng kế tiếp, kết quả cuối cùng "10 PM" đặt to nhất ở đáy
- Vì có 7 bước tính toán — nên cân nhắc tách slide 3a (Bước 1-3: UAW/UUCW/UUCP) và 3b (Bước 4-7: TCF/ECF/AUCP/Effort) nếu cần không gian trình bày công thức rõ ràng

**Ghi chú thuyết trình:** Không cần đọc từng phép tính chi tiết trên slide — nêu bật kết quả cuối (10 PM) và giải thích ngắn gọn ý nghĩa từng hệ số (TCF = độ phức tạp kỹ thuật, ECF = độ phù hợp môi trường/đội ngũ).

---

## Slide 4 — Đối chuẩn bằng phương pháp COCOMO II

**Loại slide:** Estimation Method 2 — COCOMO II

**Nội dung:**
- Quy mô: ~8.5 KLOC dự kiến, sau tái sử dụng (60% qua MinIO/OAuth/thư viện có sẵn) còn **3.5 KLOC** viết mới
- Scale Factor B = 1.05; EAF = 0.95 (nhờ Docker + CI/CD)
- Effort thô = 2.94 × 0.95 × (8.5)^1.05 ≈ 26.3 PM
- Effort sau điều chỉnh tái sử dụng = 2.793 × (3.5)^1.05 ≈ **10.4 PM**

**Gợi ý thiết kế:**
- Đặt song song với slide UCP (dùng layout 2 cột nếu gộp chung 1 slide, hoặc giữ riêng và dùng cùng khung công thức nhất quán)
- Công thức toán học hiển thị dạng khối code/LaTeX rõ ràng, có chú thích từng biến số bên dưới

**Ghi chú thuyết trình:** Đây là bước "kiểm tra chéo" — một phương pháp độc lập khác để tăng độ tin cậy của con số ước lượng.

---

## Slide 5 — Đối chiếu kết quả & Kết luận nỗ lực thực tế

**Loại slide:** Estimation Reconciliation

**Nội dung:**
- UCP: **10.0 PM** | COCOMO II: **10.4 PM** → 2 phương pháp độc lập trùng khớp
- Quyết định: chọn **10.5 PM** làm cơ sở hoạch định nhân sự
- Với 4 kỹ sư kiêm nhiệm 50% (≈2 full-time): thời gian thực tế = 10.5/2 = **5.25 tháng (~21 tuần)** — khớp với lộ trình 20 tuần

**Gợi ý thiết kế:**
- Biểu đồ cột đôi (UCP vs COCOMO) gần như bằng nhau, kèm 1 đường ngang "10.5 PM chọn" ở giữa — trực quan hóa sự đồng thuận giữa 2 mô hình
- Sử dụng Chart (data_viz module trong Visualizer) cho biểu đồ so sánh này

**Ghi chú thuyết trình:** Đây là luận điểm thuyết phục quan trọng: ước lượng không phải "đoán" mà có 2 mô hình toán học độc lập cùng cho kết quả gần giống nhau.

---

## Slide 6 — Dự toán Chi phí đầu tư ban đầu (CapEx)

**Loại slide:** Cost Plan — CapEx

**Nội dung:**
- Số hóa & Biên tập EPUB: 30–40 triệu VNĐ (thuê CTV cho ~10.000 cuốn)
- Phát triển phần mềm: 25–35 triệu VNĐ (nhân lực 4 kỹ sư CNTT)
- Thiết bị scan & Server: 10–12 triệu VNĐ (2 máy scan chữ V + nâng cấp VMware)
- Đào tạo & Triển khai: 5–8 triệu VNĐ (giảm theo bản gốc Proposal: 2–4tr; theo Cost-Time-Resource: 5–8tr — **cần đối chiếu lại con số chính thức giữa 2 tài liệu trước khi trình bày**)
- Dự phòng rủi ro (~15%): 5–10 triệu VNĐ
- **TỔNG CAPEX: 75.000.000 – 95.000.000 VNĐ**

**Gợi ý thiết kế:**
- Biểu đồ tròn (pie/donut chart) phân bổ 5 hạng mục CapEx, hạng mục "Số hóa & EPUB" chiếm tỷ trọng lớn nhất nên đặt màu nổi bật nhất
- Ghi chú nhỏ dưới slide về việc đối chiếu số liệu giữa 2 tài liệu nguồn (Proposal vs Cost-Time-Resource) nếu có chênh lệch

**Ghi chú thuyết trình:** ⚠️ Lưu ý: mục "Đào tạo & Triển khai" có 2 khoảng giá trị khác nhau giữa `02-project-proposal.md` (2–4tr) và `08-cost-time-resource.md` (5–8tr) — nhóm nên thống nhất 1 con số chính thức trước khi trình bày chính thức.

---

## Slide 7 — Dự toán Chi phí vận hành định kỳ (OpEx)

**Loại slide:** Cost Plan — OpEx

**Nội dung:**
- Hạ tầng server & Cloud: 4–8 triệu VNĐ/năm
- Bảo trì phần mềm: 6–12 triệu VNĐ/năm
- Dịch vụ Cloud OCR bổ sung (dự phòng sách quá mờ): 3–6 triệu VNĐ/năm
- Số hóa bổ sung hàng năm: 2–4 triệu VNĐ/năm
- **TỔNG OPEX: 15.000.000 – 30.000.000 VNĐ/năm**

**Gợi ý thiết kế:**
- Biểu đồ cột xếp chồng (stacked bar) theo năm, thể hiện OpEx lặp lại hàng năm — đối lập trực quan với CapEx (chỉ 1 lần) ở slide trước
- Dùng cùng bảng màu 4 hạng mục để người xem liên hệ nhanh với slide CapEx

**Ghi chú thuyết trình:** Nhấn mạnh: OpEx là chi phí lặp lại — cần được Ban Giám hiệu phê duyệt như ngân sách thường niên, khác bản chất với CapEx một lần.

---

## Slide 8 — Kế hoạch phân bổ Nguồn lực Nhân sự & Thiết bị

**Loại slide:** Resource Allocation Plan

**Nội dung:**
- Nhân sự: PM/Solution Architect (1), Backend Dev (1), Frontend Dev (1), DevOps (1), Thủ thư (2), Sinh viên CTV (10–15 người bán thời gian)
- Thiết bị: 2 máy quét sách chữ V
- Phân vùng VMware: VM-Dev (4 vCPU/8GB/100GB), VM-Staging (4 vCPU/16GB/200GB), VM-Production (8 vCPU/32GB/2TB+500GB SSD)

**Gợi ý thiết kế:**
- 2 khối song song: "Nhân sự" (icon người theo vai trò, số lượng ghi cạnh mỗi icon) và "Hạ tầng" (3 khối VM kích thước tương ứng tỷ lệ theo cấu hình thực — VM-Production vẽ to nhất)

**Ghi chú thuyết trình:** Đây là câu trả lời cụ thể cho "ai làm gì, dùng máy nào" — bổ sung thực tế hóa cho các con số PM đã tính ở slide 3-5.

---

## Slide 9 — Ý nghĩa của Tài liệu Phát biểu Công việc (Project Checklist / SOW)

**Loại slide:** Statement of Work — Purpose & Meaning

**Nội dung:**
- Bản chất: Project Checklist trong Điều lệ Dự án (Charter) đóng vai trò như **Statement of Work (SOW)** — trả lời 5 câu hỏi nền tảng trước khi dự án chính thức khởi động:
  - **Why** (Tại sao cần?) — Kho quá tải, xuống cấp, sinh viên khó tiếp cận
  - **What** (Giải quyết gì?) — Tự động hóa số hóa, tăng tốc tra cứu, bảo mật bản quyền
  - **Deliverables** (Bàn giao gì?) — Web Portal, Dashboard OCR, 500 EPUB, hạ tầng, tài liệu hướng dẫn
  - **How** (Làm thế nào?) — Kỹ thuật (React/FastAPI/Postgres/MinIO) + Quản lý (Hybrid Gating+Kanban)
  - **When** (Khi nào xong?) — 20 tuần, MVP tuần 12
- Ý nghĩa: SOW là "hợp đồng nội bộ" ràng buộc phạm vi, ngăn scope creep và là căn cứ để đo lường thành công cuối dự án

**Gợi ý thiết kế:**
- 5 câu hỏi Why/What/Deliverables/How/When trình bày dạng 5W thành khung ngôi sao hoặc bánh xe (wheel) 5 cánh, mỗi cánh 1 câu trả lời ngắn
- Nhấn 1 câu định nghĩa SOW ở đầu slide bằng khung trích dẫn

**Ghi chú thuyết trình:** Giải thích rõ: tài liệu gốc không dùng thuật ngữ "SOW" trực tiếp, nhưng "Project Checklist" trong Charter thực hiện đúng chức năng của một SOW — cần nói rõ điều này khi thuyết trình để tránh gây hiểu lầm là trích dẫn nguyên văn.

---

## Slide 10 — Bộ chỉ số Giám sát Tiến độ (Development Progress Metrics)

**Loại slide:** Monitoring Metrics — Progress

**Nội dung:**
- **Throughput (T):** số story Done/tuần → dùng để forecast: Thời gian còn lại ≈ N(chưa Done)/T
- **Cycle Time:** ≤2 ngày (size S), ≤3 ngày (size M) — đo từ lúc "In Progress" đến "Done"
- **Forecast còn lại:** Dev weeks ≈ N/T, cập nhật mỗi Weekly Review
- **Tỷ lệ hoàn thành Backlog:** Done/26 stories × 100%, mục tiêu 100% Must-have trước tuần 12

**Gợi ý thiết kế:**
- Dashboard 4 KPI card ngang hàng, mỗi card 1 con số lớn + mini sparkline biểu diễn xu hướng theo tuần
- Có thể dùng Chart module trong Visualizer để mô phỏng dashboard giám sát thực tế

**Ghi chú thuyết trình:** Đây là các chỉ số PM theo dõi hàng tuần — khác với các chỉ số ước lượng 1 lần ở đầu dự án (Slide 3-5).

---

## Slide 11 — Bộ chỉ số Chi phí AI & Rủi ro Kỹ thuật

**Loại slide:** Monitoring Metrics — AI Cost & Technical Risk

**Nội dung:**
- Chi phí AI tích lũy: quy đổi token → VNĐ, cộng dồn theo tuần, hạn mức ≤5.000.000 VNĐ (trong CapEx)
- AI Productivity Factor: số story Done / tổng token AI đã dùng — phát hiện lãng phí token
- Rủi ro kỹ thuật: Kết quả PoC 1 (OCR nền — cảnh báo nếu timeout >60s hoặc block Event Loop), Kết quả PoC 2 (liên thông E2E), Tỷ lệ nhận dạng OCR (<85% → cần tiền xử lý ảnh)

**Gợi ý thiết kế:**
- 2 cột: "Chi phí AI" (biểu tượng đồng tiền/token) và "Rủi ro kỹ thuật" (biểu tượng cảnh báo/PoC), mỗi cột có ngưỡng cảnh báo tô màu đỏ rõ ràng

**Ghi chú thuyết trình:** Liên hệ lại Phần 4 (log effort + token AI trong DoD) — đây là nơi dữ liệu đó được tổng hợp thành chỉ số giám sát.

---

## Slide 12 — Demo: Cơ chế Thu thập Dữ liệu Báo cáo (Session Logging)

**Loại slide:** Live Demo — Data Collection Mechanism

**Nội dung:**
- Sau mỗi phiên làm việc với AI Coding Assistant, dev ghi 1 dòng vào `project_log.md`: Ngày hoàn thành, Dev, Story ID, Tên Story, Thời gian làm, Token AI đã dùng, Ghi chú (model AI + đặc điểm)
- PM tổng hợp file `project_log.md` mỗi cuối tuần để tính throughput, chi phí AI, forecast
- Kịch bản demo gợi ý: mở file `project_log.md` mẫu, chỉ ra 1 dòng log thực tế và cách PM dùng dữ liệu đó để tính throughput tuần

**Gợi ý thiết kế:**
- Bảng log mẫu hiển thị dạng spreadsheet/table thật với 1-2 dòng dữ liệu ví dụ (Ngày, Dev, Story ID, Thời gian, Token AI, Ghi chú)
- Mũi tên từ bảng log → "PM tổng hợp cuối tuần" → biểu đồ throughput (liên kết trực quan tới Slide 13)

**Ghi chú thuyết trình:** Đây là minh chứng cụ thể cho việc "thu thập dữ liệu dùng để báo cáo tình trạng dự án" — nên trình chiếu trực tiếp file log thật nếu có sẵn.

---

## Slide 13 — Demo: Snapshot Tiến độ Thực tế Tuần 1

**Loại slide:** Live Demo — Week 1 Real Data Snapshot

**Nội dung:**
- Stories hoàn thành: **12/26 (46%)** trong 2 ngày đầu
- Tổng thời gian dev thực tế: 4 giờ 05 phút (4 phiên làm việc của 4 dev)
- Tổng token AI đã dùng: **440.000 tokens** (Claude Sonnet 5 + Opus 4.8 + Claude Code)
- Throughput tuần 1 (T): **12 stories/tuần**
- Forecast: còn 14 stories (4 Must, 7 Should, 3 Could) → Optimistic (T=8): ~1.8 tuần (xong tuần 3) | Pessimistic (T=4): ~3.5 tuần (xong tuần 5) → **khoảng ước lượng: 2–4 tuần**
- Chi phí AI tuần 1: ~300.000 VNĐ (~6% hạn mức 5 triệu) → dự báo tổng dự án ~1.200.000 VNĐ

**Gợi ý thiết kế:**
- Dashboard số liệu thật dạng "báo cáo thực chiến" — nổi bật nhất nên là con số "12/26 (46%)" và "khoảng 2–4 tuần"
- Biểu đồ forecast dạng dải khoảng (range bar: optimistic–pessimistic) thay vì 1 con số cố định, thể hiện đúng bản chất "dự báo theo khoảng"

**Ghi chú thuyết trình:** Đây là dữ liệu **thật** đã thu thập được (không phải giả định) — nhấn mạnh điều này để tăng độ tin cậy: phương pháp giám sát không chỉ là lý thuyết mà đã vận hành từ tuần đầu tiên.

---

## Slide 14 — Quy chế Báo cáo Định kỳ (3 cấp độ)

**Loại slide:** Reporting Cadence

**Nội dung:**
- **Cấp 1 — Session (sau mỗi phiên AI):** dev tự ghi log — nội dung hoàn thành, token AI, thời gian, model dùng
- **Cấp 2 — Weekly Review (mỗi tuần):** PM tổng hợp gửi Ban GĐ Thư viện & Trưởng phòng CNTT — throughput, cycle time, chi phí AI tích lũy, forecast, rủi ro
- **Cấp 3 — Phase-Gating Report (cuối tuần 2, 12, 18):** báo cáo thẩm định chi tiết gửi Ban Giám hiệu để phê duyệt giải ngân CapEx theo giai đoạn

**Gợi ý thiết kế:**
- Sơ đồ kim tự tháp 3 tầng (Session ở đáy — tần suất cao nhất, Phase-Gating ở đỉnh — tần suất thấp nhất nhưng mức phê duyệt cao nhất)
- Mỗi tầng ghi rõ "người nhận báo cáo" bên cạnh

**Ghi chú thuyết trình:** Nhấn mạnh tính "từ dưới lên" — mọi báo cáo cấp cao đều bắt nguồn từ dữ liệu log chi tiết ở cấp Session, không có số liệu nào bị "bịa" giữa chừng.

---

## Slide 15 — Tổng kết Phần 5 & Toàn bộ Bộ Tài liệu

**Loại slide:** Final Summary

**Nội dung:**
- Ước lượng: 2 phương pháp độc lập (UCP, COCOMO II) hội tụ ở ~10.5 PM — có cơ sở khoa học, không phải đoán mò
- Kế hoạch: 20 tuần, 4 giai đoạn, đường găng rõ ràng (WP4), ngân sách trong hạn mức <100 triệu VNĐ
- Giám sát: cơ chế 3 cấp báo cáo dựa trên dữ liệu log thật, đã chứng minh hoạt động từ tuần 1 (46% backlog hoàn thành)
- Kết nối toàn bộ 5 phần: Ý tưởng → Đề xuất → Tầm nhìn/Điều lệ/Backlog → Kiến trúc → Phương pháp → Ước lượng/Giám sát — một chuỗi tài liệu quản lý dự án phần mềm đầy đủ, nhất quán, có AI hỗ trợ xuyên suốt và luôn có con người kiểm duyệt cuối cùng

**Gợi ý thiết kế:**
- Sơ đồ tổng kết dạng "chuỗi mắt xích" nối 5 phần đã trình bày (mỗi phần 1 icon nhỏ đã dùng ở trang bìa tương ứng) — tạo cảm giác khép lại trọn vẹn toàn bộ buổi thuyết trình
- Đây là slide cuối cùng của toàn bộ deck — nên dùng làm nền chuyển sang Q&A tổng thể

**Ghi chú thuyết trình:** Đây là slide chốt của TOÀN BỘ buổi thuyết trình (5 phần) — nên dành thời gian nhắc lại thông điệp xuyên suốt: dự án khả thi cả về pháp lý, kỹ thuật, tài chính và có cơ chế giám sát minh bạch dựa trên dữ liệu thật.
