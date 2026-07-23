# SLIDE DECK — PHẦN 4: DEVELOPMENT METHOD
## Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS (HCMUS-LDMS)

> Nguồn nội dung: `05-project-charter.md` (mục 9), `06-architecture.md` (mục 8–9), `07-product-backlog.md` (mục 1.1)
> Số lượng slide đề xuất: **10 slide**
> Lưu ý: Tài liệu nguồn không mô tả chi tiết công cụ AI Coding Assistant cụ thể hay quy trình tích hợp mã nguồn từng bước — các phần này để **placeholder**, cần nhóm bổ sung khi thuyết trình thực tế (dựa trên `project_log.md` và kinh nghiệm triển khai thật).

---

## Slide 1 — Trang bìa

**Loại slide:** Title Slide

**Nội dung:**
- Tiêu đề: Phương pháp Phát triển (Development Method)
- Phụ đề: "Hybrid: Gating Checkpoints + Kanban — AI Coding Assistant hỗ trợ đội ngũ kiêm nhiệm"

**Gợi ý thiết kế:**
- Giữ tông kỹ thuật đồng bộ với Phần 3 (blueprint/grid nền)
- Thêm icon robot/AI nhỏ góc trang để báo hiệu nội dung có yếu tố AI-assisted

**Ghi chú thuyết trình:** Nêu bối cảnh: đội ngũ 4 kỹ sư kiêm nhiệm 50% thời gian, cần phương pháp linh hoạt nhưng vẫn kiểm soát được tiến độ tổng thể.

---

## Slide 2 — Phương pháp luận Hybrid: Gating + Kanban

**Loại slide:** Methodology Overview

**Nội dung:**
- Tầng vĩ mô: **Gating Checkpoints** — kiểm soát ngân sách và chuyển giai đoạn (cuối tuần 2, 12, 18) trình Ban Giám hiệu phê duyệt
- Tầng vi mô: **Kanban** — WIP = 1 card/người (hoặc /agent AI), đo throughput (story Done/tuần) để forecast
- Quy tắc phối hợp: Daily Standup 15 phút, Weekly Review (đếm story Done, cập nhật throughput), Gating Review (chốt chuyển pha)

**Gợi ý thiết kế:**
- Sơ đồ 2 tầng: tầng trên là 4 cổng gating (icon cổng/khóa) dọc theo timeline 20 tuần; tầng dưới là board Kanban mini lặp lại liên tục bên trong mỗi giai đoạn
- Dùng Visualizer diagram module để minh họa mối quan hệ "vĩ mô bọc vi mô" này

**Ghi chú thuyết trình:** Giải thích tại sao không chọn thuần Scrum (sprint cố định) — đội kiêm nhiệm khó cam kết sprint đều đặn, nên Kanban theo throughput thực tế linh hoạt hơn.

---

## Slide 3 — Quy tắc Kanban chi tiết: WIP, DoR, DoD

**Loại slide:** Kanban Rules

**Nội dung:**
- WIP (Work In Progress) = 1 card/người: tránh phân tán, đảm bảo hoàn thành trước khi nhận việc mới
- Definition of Ready (DoR): card chỉ vào "In Progress" khi có ID, AC rõ ràng, `depends_on` đã Done, size ≤ M (2 ngày)
- Definition of Done (DoD): AC pass, code merge qua PR, chạy được local, README cập nhật, log effort + token AI

**Gợi ý thiết kế:**
- Board Kanban 3 cột (Ready → In Progress → Done) minh họa trực quan, mỗi cột chú thích điều kiện chuyển card (DoR ở đầu vào, DoD ở đầu ra)
- Dùng Visualizer để dựng mini Kanban board tương tác nếu muốn nhấn mạnh phần trình bày

**Ghi chú thuyết trình:** Đây là kỷ luật kỹ thuật giúp đo throughput chính xác — nếu không giới hạn WIP, số liệu forecast sẽ sai lệch.

---

## Slide 4 — Chiến lược nhánh Git (GitFlow) cho đội 4 người

**Loại slide:** Git Branching Strategy

**Nội dung:**
- `main`: nhánh production ổn định nhất, chỉ merge từ `release/*` qua PR có phê duyệt Tech Lead, tự động tag version
- `develop`: nhánh tích hợp chính mỗi Sprint/giai đoạn
- `feature/*`: nhánh tính năng riêng lẻ (VD: `feature/ocr-integration`, `feature/epub-reader`), tạo từ `develop`, merge lại sau unit test
- `release/*`: chuẩn bị phát hành (VD: `release/v1.0-MVP`), phục vụ UAT và fix lỗi cuối
- `hotfix/*`: sửa lỗi khẩn cấp trực tiếp từ `main`, merge đồng thời vào `main` và `develop`

**Gợi ý thiết kế:**
- Sơ đồ nhánh Git kinh điển (đường ngang phân nhánh/hợp nhánh theo màu: main=đen, develop=xanh dương, feature=xanh lá, release=cam, hotfix=đỏ)
- Dùng Visualizer diagram module để vẽ Git graph chuẩn GitFlow

**Ghi chú thuyết trình:** Đây là nền tảng cho slide tiếp theo về tích hợp mã nguồn giữa các thành viên.

---

## Slide 5 — Quản lý cấu hình phần mềm (SCM) & Quy tắc định danh

**Loại slide:** Configuration Management

**Nội dung:**
- Quy tắc mã định danh CI: `LDMS_[LOẠI_CI]_[TRẠNG_THÁI]X.Y` — VD: `LDMS_SDD_R3.0.md` (tài liệu kiến trúc), `LDMS_SRC_B1.0` (mã nguồn backend)
- Phân loại: PLN (kế hoạch), SRD (yêu cầu), SDD (thiết kế), SRC (mã nguồn), TSP (kế hoạch test)
- Trạng thái: R (Release), A (Alpha), B (Beta)

**Gợi ý thiết kế:**
- Bảng phân rã công thức đặt tên thành các khối màu (giống chú giải ký hiệu bản đồ), giúp người xem tự giải mã được 1 tên file mẫu ngay tại chỗ
- Có thể làm dạng "giải mã từng ký tự" tương tác (click từng phần để hiện nghĩa) nếu trình bày dạng số

**Ghi chú thuyết trình:** Việc chuẩn hóa định danh giúp truy vết phiên bản dễ dàng giữa 4 thành viên làm việc song song — tránh nhầm lẫn file nào là bản mới nhất.

---

## Slide 6 — Demo: Tạo mã nguồn với sự trợ giúp của AI Coding Assistant

**Loại slide:** Live Demo — AI-Assisted Coding

**Nội dung (placeholder — cần nhóm bổ sung dựa trên thực tế triển khai):**
- Kịch bản demo gợi ý: dùng AI Coding Assistant (VD: Claude Code) để sinh 1 module/tính năng cụ thể trong backlog — ví dụ **LDMS-007 Đóng gói & xuất EPUB** (gọi Pandoc biên dịch Markdown → EPUB 3.0)
- Các bước demo nên trình bày: (1) đưa prompt/yêu cầu kèm ngữ cảnh kiến trúc, (2) AI sinh code theo cấu trúc thư mục đã định nghĩa (`services/epub.py`), (3) chạy thử cục bộ để xác minh Acceptance Criteria (AC1–AC4 của LDMS-007)
- Ghi nhận: thời gian thực hiện + token AI đã dùng vào `project_log.md` theo đúng cơ chế Session Logging (xem Phần 5)

**Gợi ý thiết kế:**
- Khung demo lớn (screenshot/video call-out) ở giữa slide, ghi rõ "LIVE DEMO — [Tên Story]"
- 3 bước demo hiển thị dạng stepper ngang phía dưới khung demo

**Ghi chú thuyết trình:** ⚠️ Cần thay bằng ví dụ thực tế nhóm đã làm (module cụ thể, AI assistant cụ thể) trước khi thuyết trình chính thức — tài liệu nguồn chỉ đề cập việc dùng AI Coding Assistant nói chung, không có kịch bản demo cụ thể sẵn.

---

## Slide 7 — Demo: Tích hợp mã nguồn giữa các thành viên trong nhóm

**Loại slide:** Live Demo — Team Code Integration

**Nội dung (placeholder — cần nhóm bổ sung dựa trên thực tế triển khai):**
- Kịch bản demo gợi ý: 2 thành viên cùng phát triển 2 `feature/*` branch độc lập (VD: `feature/ocr-integration` và `feature/epub-reader`) → tạo Pull Request vào `develop` → Tech Lead review → merge
- Nhấn mạnh: card Kanban tuân thủ WIP=1, mỗi story chỉ 1 người phụ trách nhưng code review là bước bắt buộc trước merge (theo DoD "Code merge qua PR")
- Có thể minh họa xung đột merge (merge conflict) đơn giản và cách xử lý nếu muốn tăng tính thực tế

**Gợi ý thiết kế:**
- Sơ đồ 2 nhánh feature hội tụ vào `develop` qua 1 PR review gate (icon con mắt kiểm duyệt)
- Nếu demo trực tiếp: dùng GitHub/GitLab thật, chiếu màn hình Pull Request có comment review thực tế

**Ghi chú thuyết trình:** ⚠️ Tương tự Slide 6 — cần ví dụ PR thực tế của nhóm để tăng độ thuyết phục thay vì chỉ mô tả lý thuyết GitFlow.

---

## Slide 8 — Vai trò AI trong toàn bộ chu trình phát triển

**Loại slide:** AI Integration Summary

**Nội dung:**
- Giai đoạn thiết kế: AI hỗ trợ soạn thảo tài liệu (Vision, Charter, Backlog) — con người rà soát trước khi chốt (Human-in-the-loop, xem Phần 1 & 2)
- Giai đoạn code: AI Coding Assistant hỗ trợ sinh code theo kiến trúc đã định — dev review & test AC trước khi merge
- Giai đoạn vận hành: AI (Tesseract OCR) xử lý nhận dạng ký tự — biên tập viên/thủ thư soát lỗi và phê duyệt xuất bản
- Giai đoạn báo cáo: ghi nhận token AI sử dụng mỗi phiên vào `project_log.md` để kiểm soát chi phí (xem Phần 5)

**Gợi ý thiết kế:**
- Sơ đồ vòng lặp 4 giai đoạn (Thiết kế → Code → Vận hành → Báo cáo) dạng vòng tròn khép kín, mỗi giai đoạn có 2 nhãn nhỏ "AI làm gì" / "Con người làm gì"
- Đây là slide tổng hợp — có thể dùng làm slide "trục xuyên suốt" nối các phần đã trình bày

**Ghi chú thuyết trình:** Nhấn mạnh đây là nguyên tắc nhất quán toàn dự án: AI luôn đóng vai trò tăng tốc, con người luôn giữ vai trò kiểm duyệt cuối cùng.

---

## Slide 9 — Định nghĩa Hoàn thành (DoD) áp dụng cho mã nguồn

**Loại slide:** Definition of Done — Code

**Nội dung:**
- 1. AC pass — toàn bộ Acceptance Criteria của card đã kiểm tra đạt
- 2. Code merge — qua Pull Request, có self-review checklist
- 3. Chạy local — `docker compose up` + `npm run dev` hoạt động
- 4. README cập nhật — endpoint/trang mới được ghi chú
- 5. Log effort — thời gian thực hiện + token AI đã dùng (phục vụ throughput & chi phí AI)

**Gợi ý thiết kế:**
- Checklist 5 mục dạng thẻ tick lớn, có thể numbered rõ ràng — đây là "quy chuẩn chất lượng" cần lặp lại nhất quán với Phần 2 (đã giới thiệu DoD)
- Icon tick xanh cho mỗi mục đã hoàn thành minh họa

**Ghi chú thuyết trình:** Liên hệ lại Phần 2 (Backlog) — DoD ở đây chính là DoD đã trình bày, nhấn mạnh tính nhất quán xuyên suốt tài liệu.

---

## Slide 10 — Tổng kết Phần 4

**Loại slide:** Summary

**Nội dung:**
- Phương pháp Hybrid phù hợp đội kiêm nhiệm: kiểm soát vĩ mô chặt (Gating) + linh hoạt vi mô (Kanban)
- GitFlow + quy tắc định danh CI đảm bảo truy vết phiên bản rõ ràng giữa 4 thành viên
- AI đóng vai trò trợ lý tăng tốc ở mọi giai đoạn, luôn có con người kiểm duyệt cuối
- Chuyển tiếp: mọi effort/token AI được ghi nhận để phục vụ ước lượng và giám sát ở Phần 5

**Gợi ý thiết kế:**
- 4 dòng tóm tắt dạng bullet lớn, nền chuyển màu báo hiệu chuyển sang Phần 5 (Estimation/Planning/Monitoring)

**Ghi chú thuyết trình:** Chuyển ý: "Vậy toàn bộ effort và chi phí AI này được ước lượng, lên kế hoạch và giám sát ra sao?" → dẫn vào Phần 5.
