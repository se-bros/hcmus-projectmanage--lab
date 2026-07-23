# SLIDE DECK — PHẦN 2: PROJECT VISION & SCOPE, PROJECT CHARTER, PRODUCT BACKLOG
## Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS (HCMUS-LDMS)

> Nguồn nội dung: `03-vision-and-scope.md`, `05-project-charter.md`, `07-product-backlog.md`
> Số lượng slide đề xuất: **16 slide**

---

## Slide 1 — Trang bìa

**Loại slide:** Title Slide

**Nội dung:**
- Tiêu đề: Tầm nhìn & Phạm vi · Điều lệ Dự án · Product Backlog
- Phụ đề: "Từ định vị sản phẩm đến từng tiêu chí chấp nhận"
- Dự án: HCMUS-LDMS

**Gợi ý thiết kế:**
- Layout chia 3 khối biểu tượng nhỏ trên cùng 1 hàng tương ứng 3 tài liệu (la bàn = Vision, con dấu = Charter, bảng Kanban = Backlog)
- Đồng bộ bảng màu với Phần 1 để giữ tính nhất quán bộ slide toàn dự án

**Ghi chú thuyết trình:** Nêu rõ 3 tài liệu này trả lời 3 câu hỏi khác nhau: làm gì (Vision), ai chịu trách nhiệm (Charter), làm chi tiết ra sao (Backlog).

---

## Slide 2 — Phát biểu định vị sản phẩm (Product Position Statement)

**Loại slide:** Positioning Statement

**Nội dung:**
- Dành cho: Sinh viên, giảng viên, cán bộ thư viện HCMUS
- Vấn đề: khó tra cứu/bảo quản giáo trình giấy độc bản, trải nghiệm đọc số kém trên di động
- Sản phẩm: hệ thống web nội bộ số hóa và quản lý tài liệu học thuật tập trung
- Khác biệt so với: PDF scan tĩnh và OPAC truyền thống

**Gợi ý thiết kế:**
- Dùng khuôn mẫu câu "Positioning Statement" kinh điển — mỗi vế (Dành cho / Vấn đề / Sản phẩm / Khác với / Chúng tôi) là 1 dòng có highlight màu khác nhau trong cùng 1 đoạn văn lớn
- Layout dạng "mad-libs" điền vào chỗ trống, tạo cảm giác dễ đọc như 1 công thức

**Ghi chú thuyết trình:** Đây là câu định vị 1 câu duy nhất mà cả nhóm phải nhớ nằm lòng khi ra quyết định thiết kế.

---

## Slide 3 — Quy trình As-Is: Vận hành thủ công hiện tại

**Loại slide:** Current State Process

**Nội dung:**
- Thủ thư: quét bằng máy photocopy văn phòng → PDF ảnh tĩnh → đăng tải bừa bãi lên Drive/thư mục chia sẻ (không phân quyền)
- Sinh viên: tra mã sách trên OPAC cũ → tìm sách giấy tại kệ → photocopy dịch vụ bên ngoài trường nếu cần mang về → đọc/ghi chú hoàn toàn thủ công (bút dạ quang)
- 4 vấn đề cốt lõi: (1) vi phạm bản quyền do phát tán tự do, (2) trải nghiệm đọc kém không responsive, (3) mất khả năng tra cứu nội dung, (4) không có chuẩn metadata

**Gợi ý thiết kế:**
- Sơ đồ luồng (flow diagram) dạng PlantUML activity đã có sẵn trong tài liệu — chuyển thành diagram trực quan bằng Visualizer (diagram module)
- Tông màu xám/nâu nhạt (giấy cũ) để gợi cảm giác "cũ kỹ, thủ công"
- 4 vấn đề đặt thành 4 tag cảnh báo màu đỏ bên dưới sơ đồ

**Ghi chú thuyết trình:** Đây là baseline để so sánh — nhấn mạnh KHÔNG có bất kỳ kiểm soát bản quyền nào ở hiện trạng.

---

## Slide 4 — Quy trình To-Be: Số hóa khép kín có AI hỗ trợ

**Loại slide:** Future State Process

**Nội dung:**
- Sơ đồ Use Case To-Be: Đăng nhập → Quét (300 DPI) → Khai báo Metadata (Dublin Core) → OCR (BackgroundTasks) → Hiệu chỉnh Split-screen → Duyệt & Xuất bản EPUB (Pandoc) → Tìm kiếm & Đọc bảo mật (FTS + Signed URL)
- Phân vai rõ: Thủ thư (quét, metadata, duyệt) vs Biên tập viên/CTV (soát lỗi OCR)
- Tính năng mới nổi bật: DRM Signed URL, EPUB 3.0 reflowable, FTS Elasticsearch/Postgres, Split-screen (+60% năng suất soát lỗi)

**Gợi ý thiết kế:**
- Cùng khung sơ đồ như slide As-Is (để so sánh song song khi lật slide) nhưng tông màu xanh dương/công nghệ tươi sáng
- Vẽ bằng Visualizer diagram module, giữ cùng bố cục ngang để người xem dễ đối chiếu trước/sau
- Đánh dấu rõ 2 "làn" song song: làn Thủ thư (trên) và làn Biên tập viên (dưới)

**Ghi chú thuyết trình:** Đối chiếu trực tiếp với slide 3 — mỗi vấn đề As-Is đều có 1 tính năng To-Be tương ứng giải quyết.

---

## Slide 5 — So sánh quy trình với thủ công & đối thủ (Workflow Benchmarking)

**Loại slide:** 4-Way Comparison Table

**Nội dung:**
Bảng đối chuẩn 6 tiêu chí x 4 phương án: **As-Is thủ công** | **Kết hợp công cụ rời rạc (Abbyy+Drive)** | **Giải pháp thương mại (Lạc Việt/DSpace)** | **HCMUS-LDMS**
- Quét & Metadata; Nhận dạng & Soát lỗi OCR; Đóng gói & Định dạng; Tìm kiếm & Tra cứu; Bảo mật & DRM; Nỗ lực vận hành
- Kết luận nhanh: HCMUS-LDMS là phương án duy nhất đạt "Nỗ lực vận hành: Rất thấp" trong khi vẫn có DRM chặt và FTS <3 giây

**Gợi ý thiết kế:**
- Bảng lớn 4 cột, cột HCMUS-LDMS ở ngoài cùng bên phải được tô nền màu nhấn + viền đậm để "thắng" rõ ràng bằng mắt
- Vì bảng khá dày dữ liệu — nên tách thành 2 slide phụ nếu trình bày cần đọc kỹ (1 slide 3 dòng đầu, 1 slide 3 dòng sau), hoặc dùng bảng có thể cuộn nếu trình bày dạng digital
- Icon nhỏ đầu mỗi dòng tiêu chí (kính lúp, ổ khóa, đồng hồ...)

**Ghi chú thuyết trình:** Đây là bằng chứng định lượng nhất cho câu hỏi "tại sao tự làm mà không mua/ghép sẵn" — nên dừng lại giải thích kỹ dòng "Nỗ lực vận hành".

---

## Slide 6 — Chân dung các bên liên quan & Người dùng

**Loại slide:** Stakeholder & User Personas

**Nội dung:**
- Bên liên quan: Ban Giám hiệu (Sponsor), Ban Giám đốc Thư viện, Phòng CNTT
- Người dùng: Độc giả (SV/GV), Thủ thư, Biên tập viên (CTV), Quản trị viên (Admin)
- Môi trường sử dụng: Thủ thư/BTV/Admin dùng PC văn phòng nội bộ; Sinh viên/GV dùng mobile/tablet từ xa

**Gợi ý thiết kế:**
- Layout dạng persona card 2 hàng: hàng trên "Stakeholders" (quyền lực/ra quyết định), hàng dưới "Users" (người thao tác trực tiếp hệ thống)
- Mỗi card: icon vai trò + 1 dòng "mối quan tâm chính"

**Ghi chú thuyết trình:** Phân biệt rõ Stakeholder (quan tâm đến kết quả) và User (trực tiếp thao tác) — tránh nhầm lẫn khi làm RACI sau đó.

---

## Slide 7 — Phân tích trách nhiệm: Responsibility, Accountability, Reach, Influence

**Loại slide:** RACI + Power/Interest Analysis

**Nội dung:**
- **RACI theo WBS** (từ Charter): mỗi gói công việc (WP1–WP6) có duy nhất 1 đơn vị **Accountable**; Thư viện = A/R cho WP1, WP4, WP6 (nghiệp vụ & số hóa); Phòng CNTT = A/R cho WP2, WP3, WP5 (kỹ thuật)
- **Power/Interest Grid** (khả năng tiếp cận & mức độ ảnh hưởng):
  - Power cao / Interest cao → Quản trị sát sao: Ban GĐ Thư viện, Trưởng phòng CNTT (PM)
  - Power cao / Interest trung bình → Giữ hài lòng: Ban Giám hiệu, Bộ phận Pháp chế
  - Power thấp / Interest cao → Thông báo đầy đủ: Giảng viên, Sinh viên

**Gợi ý thiết kế:**
- Chia đôi slide: trái là bảng RACI (6 dòng WP x 6 vai trò, màu theo R/A/C/I), phải là ma trận 2x2 Power/Interest với tên stakeholder đặt vào đúng góc phần tư
- Đây là nội dung dày — có thể tách thành 2 slide riêng (7a: RACI, 7b: Power/Interest) nếu cần không gian

**Ghi chú thuyết trình:** Nhấn mạnh nguyên tắc "mỗi gói công việc chỉ có 1 Accountable duy nhất" — tránh tình trạng "cha chung không ai khóc" trong dự án nội bộ trường.

---

## Slide 8 — Ma trận Tác nhân: Trước và Sau khi có hệ thống (As-is vs To-be)

**Loại slide:** Impact Analysis

**Nội dung:**
Bảng 4 dòng (Ban Giám hiệu, Ban GĐ Thư viện, Thủ thư/Editor, Độc giả) x 2 cột (As-is / To-be), ví dụ:
- Độc giả As-is: di chuyển 15km, chép tay, PDF khó đọc → To-be: đọc responsive 24/7, FTS <3 giây

**Gợi ý thiết kế:**
- Bảng "before/after" với mũi tên chuyển tiếp (→) lớn ở giữa mỗi dòng
- Màu As-is: xám; màu To-be: xanh lá/xanh dương tươi — tạo cảm giác "cải thiện"

**Ghi chú thuyết trình:** Bổ sung cho slide RACI — cho thấy lợi ích cụ thể của từng nhóm, không chỉ trách nhiệm.

---

## Slide 9 — Tính năng sản phẩm: MVP vs Mở rộng

**Loại slide:** Feature Scope (MoSCoW-style)

**Nội dung:**
- **MVP:** Đăng nhập Google OAuth/Mock Auth, Upload scan, OCR Pipeline, Split-screen Editor, Đóng gói EPUB, Tra cứu PostgreSQL FTS, Web Reader bảo mật
- **Mở rộng:** Tùy chỉnh giao diện đọc, Bookmark & Highlight, Citation Generator, Tìm kiếm AI/RAG, Tích hợp chống đạo văn (Turnitin)
- Phạm vi loại trừ: hệ thống chống đạo văn chuyên sâu, số hóa hồ sơ hành chính, tìm kiếm AI/RAG (hoãn Giai đoạn 3)

**Gợi ý thiết kế:**
- 2 cột: MVP (nền đậm, icon "must-have") vs Mở rộng (nền nhạt, icon "nice-to-have")
- Phần loại trừ đặt thành dải ghi chú nhỏ cuối slide với icon dấu cấm (⊘)

**Ghi chú thuyết trình:** Làm rõ ranh giới scope để tránh scope creep khi triển khai thực tế.

---

## Slide 10 — Yêu cầu phi chức năng (NFR) trọng yếu

**Loại slide:** Non-Functional Requirements

**Nội dung:**
- Hiệu năng: tìm kiếm FTS <3 giây, tải trang <2 giây
- Bảo mật: Google OAuth 2.0/Mock Auth, Signed URL 15 phút, không hiển thị nút Download
- Độ tin cậy: PgBackRest backup 01:00 hàng ngày, RPO <24 giờ, retry OCR tối đa 3 lần
- UI/UX: responsive 320px–2560px, Lighthouse Accessibility Score ≥ 90
- Ràng buộc ngoài: Ngân sách <100.000.000 VNĐ, tuân thủ Luật SHTT Việt Nam

**Gợi ý thiết kế:**
- Bố cục dạng "dashboard KPI" — mỗi NFR là 1 ô số liệu lớn (giống thẻ chỉ số) thay vì bullet list dài dòng
- Nhóm theo 5 icon: tốc độ (đồng hồ), khóa (bảo mật), khiên (tin cậy), mắt (UI/UX), cân (pháp lý/ngân sách)

**Ghi chú thuyết trình:** NFR thường bị bỏ qua khi thuyết trình — nên nhấn mạnh đây là các tiêu chí đo lường được, không phải mô tả chung chung.

---

## Slide 11 — Quy tắc tổ chức Backlog: Kanban, DoD, MoSCoW

**Loại slide:** Backlog Governance

**Nội dung:**
- Kanban: WIP = 1 card/người, đo throughput hàng tuần (story Done/tuần), không dùng Story Point để nhân lịch
- Definition of Done (DoD): AC pass, code merge qua PR, chạy local (`docker compose up`), README cập nhật, log effort + token AI
- MoSCoW: 16 Must-have · 7 Should-have · 3 Could-have (tổng 26 stories)
- 9 module: M0 Platform … M8 Identity

**Gợi ý thiết kế:**
- 3 khối ngang: Kanban (board mini-mockup 3 cột To Do/Doing/Done), DoD (checklist 5 mục), MoSCoW (biểu đồ tròn 16/7/3)
- Dùng Visualizer để dựng mini Kanban board minh họa trực quan nguyên tắc WIP=1

**Ghi chú thuyết trình:** Đây là "luật chơi" vận hành đội ngũ kiêm nhiệm bán thời gian — throughput đo thực tế thay vì ước lượng chủ quan.

---

## Slide 12 — Demo: Phân tích tiêu chí chấp nhận (Acceptance Criteria) cho 1 User Story

**Loại slide:** Deep-Dive Example

**Nội dung:**
- Ví dụ **LDMS-003 — Hàng đợi OCR và trạng thái job** (Module M2, Size M, Must-have)
  - User Story: "Là thủ thư, tôi muốn hệ thống chạy OCR nền và theo dõi được trạng thái xử lý"
  - AC1: kích hoạt OCR → job trạng thái ban đầu `pending`
  - AC2: job chuyển `processing` → `completed`/`failed`
  - AC3: API trả về nhanh, không chờ OCR xong trong cùng request (đảm bảo tính bất đồng bộ)
  - AC4: job `failed` phải có `error_message` không rỗng (đảm bảo xử lý lỗi tường minh)

**Gợi ý thiết kế:**
- Layout "card story" giống Jira/Trello: góc trên ID + Size + MoSCoW badge, giữa là User Story in nghiêng, dưới là 4 AC dạng checklist có thể tick
- Dùng màu trạng thái job (pending=xám, processing=vàng, completed=xanh, failed=đỏ) làm minh họa nhỏ bên cạnh AC2

**Ghi chú thuyết trình:** Giải thích AC không chỉ mô tả "làm gì" mà còn "làm sai thì sao" (AC4) — đây là điểm mạnh của backlog được siết chặt ở v3.1.

---

## Slide 13 — Bản đồ triển khai Backlog (Implementation Map)

**Loại slide:** Delivery Sequencing

**Nội dung:**
- 5 giai đoạn phát triển: (1) Nền tảng & luồng dữ liệu, (2) Biên tập & xuất bản, (3) Xác thực & tra cứu, (4) Nâng cao trải nghiệm, (5) Hoàn thiện
- Nguyên tắc cắt giảm nếu trễ tiến độ: Must → Should → Could
- Mỗi story có `depends_on` rõ ràng đảm bảo thứ tự thực hiện hợp lý (VD: LDMS-007 Xuất EPUB phụ thuộc LDMS-005 Sửa text)

**Gợi ý thiết kế:**
- Timeline 5 giai đoạn dạng bậc thang (staircase), mỗi bậc liệt kê 2-3 story ID tiêu biểu
- Dùng mũi tên phụ thuộc mảnh nối giữa các story quan trọng để minh họa `depends_on`

**Ghi chú thuyết trình:** Nhấn mạnh tính khả thi tiến độ: thứ tự đã được sắp xếp theo phụ thuộc kỹ thuật thực tế, không tùy tiện.

---

## Slide 14 — Governance & KPI theo Điều lệ Dự án (Charter)

**Loại slide:** Charter Governance Summary

**Nội dung:**
- Cơ cấu: Sponsor (BGH) → Client nghiệp vụ (BGĐ Thư viện) → PM (Trưởng phòng CNTT) → Technical Lead → Dev/DevOps Team
- Phương pháp luận: **Hybrid** — Gating Checkpoints (vĩ mô) + Kanban (vi mô)
- 5 KPI thành công: 90% học liệu số hóa, FTS <3s, CAR OCR ≥85%, không sự cố rò rỉ, 85% hài lòng người dùng
- Quy chế kiểm soát thay đổi: thay đổi >5% ngân sách/phạm vi cần tờ trình có chữ ký PM + Giám đốc Thư viện

**Gợi ý thiết kế:**
- Sơ đồ tổ chức (org chart) dọc bên trái, 5 KPI dạng đồng hồ đo (gauge chart) bên phải
- Dùng Visualizer chart module để vẽ 5 gauge KPI nếu muốn tăng tính trực quan số liệu

**Ghi chú thuyết trình:** Đây là bằng chứng dự án có cơ chế quản trị chính thức (chữ ký, tờ trình) chứ không vận hành tùy hứng.

---

## Slide 15 — Demo: Đánh giá tài liệu Vision/Charter/Backlog với AI hỗ trợ, con người xem xét

**Loại slide:** Live Demo / Process Illustration

**Nội dung:**
- Kịch bản demo: dùng AI (Claude) để rà soát 1 user story mới soạn — kiểm tra định dạng chuẩn (ID, Module, Size, AC), gợi ý bổ sung AC còn thiếu điều kiện lỗi
- Con người (PM/Tech Lead) xem xét lại gợi ý của AI trước khi đưa vào backlog chính thức — đối chiếu với DoD và nguyên tắc Kanban
- Mục tiêu: minh chứng quy trình rà soát tài liệu không phụ thuộc hoàn toàn vào AI, luôn có bước duyệt cuối bởi con người

**Gợi ý thiết kế:**
- Layout tương tự Slide 11 Phần 1: khung demo lớn ở giữa, 2 nhãn "AI rà soát nháp" và "Con người phê duyệt"
- Có thể trình chiếu trực tiếp 1 đoạn hội thoại mẫu với AI review một story trong `07-product-backlog.md`

**Ghi chú thuyết trình:** Liên kết với triết lý Human-in-the-loop đã nêu ở Phần 1 — áp dụng nhất quán cho cả việc số hóa sách lẫn việc soạn tài liệu quản lý dự án.

---

## Slide 16 — Tổng kết Phần 2

**Loại slide:** Summary

**Nội dung:**
- Vision & Scope: định vị rõ sản phẩm, quy trình To-Be giải quyết triệt để 4 vấn đề As-Is
- Charter: governance rõ ràng, KPI đo lường được, RACI không chồng chéo
- Backlog: 26 stories, kỷ luật Kanban + DoD nghiêm ngặt, sẵn sàng triển khai (status "Ready for Implementation")

**Gợi ý thiết kế:**
- 3 cột tóm tắt tương ứng 3 tài liệu, mỗi cột 1 icon + 1 câu chốt
- Nền chuyển tiếp sang phần kiến trúc kỹ thuật (Phần 3) để tạo mạch nối liền giữa các phần thuyết trình

**Ghi chú thuyết trình:** Chuyển ý sang Phần 3 — "Vậy các tài liệu quản lý này được hiện thực hóa về mặt kỹ thuật như thế nào?"
