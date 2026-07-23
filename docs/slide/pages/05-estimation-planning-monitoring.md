# PHẦN 5: ESTIMATION, PLANNING & MONITORING
## Ước Lượng Nỗ Lực · Lập Kế Hoạch · Giám Sát Dự Án

<div class="mt-6 text-sm text-slate-700">
  <p class="text-base font-semibold text-emerald-900 mb-2">Ước Lượng Nỗ Lực · Lập Kế Hoạch · Giám Sát Dự Án</p>
  <p class="text-slate-600">Ước lượng UCP vs COCOMO II (10 PM), dự báo Throughput thực tế, AI Session Logging và Gating Checkpoints.</p>
</div>

<div class="mt-8 flex gap-3">
  <span class="badge bg-emerald-700 text-white font-bold px-3 py-1 text-xs rounded-full shrink-0 whitespace-nowrap">UCP & COCOMO II</span>
  <span class="badge bg-emerald-700 text-white font-bold px-3 py-1 text-xs rounded-full shrink-0 whitespace-nowrap">Throughput Forecast</span>
  <span class="badge bg-slate-200 text-slate-800 font-bold px-3 py-1 text-xs rounded-full shrink-0 whitespace-nowrap">AI Session Logging</span>
</div>

---

# Lộ Trình 4 Giai Đoạn & Đường Găng (Critical Path)

<div class="space-y-3 mt-4 text-xs">

<div class="p-3 bg-slate-50 rounded-lg border border-slate-200 shadow-sm flex justify-between items-center">
  <span><strong class="text-emerald-900">GĐ 0 (Tuần 1–2): Khảo Sát & Bản Quyền</strong> — Ban hành quy chế SHTT & khảo sát 2.500 tài liệu.</span>
  <span class="badge bg-slate-200 text-slate-800 font-bold px-2.5 py-0.5 rounded shrink-0 whitespace-nowrap">2 Tuần</span>
</div>

<div class="p-3 bg-slate-50 rounded-lg border border-slate-200 shadow-sm flex justify-between items-center">
  <span><strong class="text-emerald-900">GĐ 1 (Tuần 3–12): Phát Triển MVP & Thí Điểm 500 Sách</strong> — Xây dựng Core System & xuất bản 500 sách CNTT.</span>
  <span class="badge bg-slate-200 text-slate-800 font-bold px-2.5 py-0.5 rounded shrink-0 whitespace-nowrap">10 Tuần</span>
</div>

<div class="p-3 bg-red-50/90 rounded-lg border border-red-300 shadow-sm flex justify-between items-center">
  <span><strong class="text-red-900 font-bold">GĐ 2 (Tuần 13–18): Số Hóa 2.000 Tài Liệu [ĐƯỜNG GẮNG CRITICAL PATH]</strong> — Phụ thuộc năng suất scan & soát lỗi.</span>
  <span class="badge bg-red-700 text-white font-bold px-2.5 py-0.5 rounded shrink-0 whitespace-nowrap">6 Tuần (Nút Thắt)</span>
</div>

<div class="p-3 bg-slate-50 rounded-lg border border-slate-200 shadow-sm flex justify-between items-center">
  <span><strong class="text-emerald-900">GĐ 3 (Tuần 19–20): UAT & Go-Live Toàn Trường</strong> — Pentest DRM, kiểm thử UAT & nghiệm thu dự án.</span>
  <span class="badge bg-slate-200 text-slate-800 font-bold px-2.5 py-0.5 rounded shrink-0 whitespace-nowrap">2 Tuần</span>
</div>

</div>

<div class="mt-4 p-3 bg-amber-50 rounded-lg border border-amber-200 text-xs text-slate-800 shadow-sm">
  <strong>Cảnh báo quản lý tiến độ:</strong> Giai đoạn 2 (WP4 - Số hóa tài liệu) là nút thắt cổ chai duy nhất. Mọi sự chậm trễ ở WP4 sẽ kéo lùi ngày Go-Live toàn dự án.
</div>

---

# Ước Lượng Tính Toán Use Case Points (UCP): Bước 1–3

<div class="grid grid-cols-3 gap-4 mt-4 text-xs">

<div class="p-4 rounded-xl bg-slate-50 border border-slate-200 shadow-sm space-y-1.5">
  <strong class="text-emerald-900 text-sm block border-b border-slate-200 pb-1">Bước 1: UAW (Tác Nhân)</strong>
  <p class="text-slate-700">Simple Actors: 2 (System API)</p>
  <p class="text-slate-700">Average Actors: 2 (Interactive UI)</p>
  <p class="text-slate-700">Complex Actors: 2 (Admin/OAuth)</p>
  <div class="pt-1 text-emerald-800 font-bold text-sm">UAW = 12 Points</div>
</div>

<div class="p-4 rounded-xl bg-slate-50 border border-slate-200 shadow-sm space-y-1.5">
  <strong class="text-emerald-900 text-sm block border-b border-slate-200 pb-1">Bước 2: UUCW (Use Cases)</strong>
  <p class="text-slate-700">Simple Use Cases: 6 ($\times 5 = 30$)</p>
  <p class="text-slate-700">Average Use Cases: 4 ($\times 10 = 40$)</p>
  <p class="text-slate-700">Complex Use Cases: 4 ($\times 15 = 60$)</p>
  <div class="pt-1 text-emerald-800 font-bold text-sm">UUCW = 130 Points</div>
</div>

<div class="p-4 rounded-xl bg-emerald-50/80 border border-emerald-200 shadow-sm space-y-1.5 text-center">
  <strong class="text-emerald-900 text-sm block border-b border-emerald-200 pb-1">Bước 3: UUCP Chưa Điều Chỉnh</strong>
  <p class="text-slate-600">Công thức:</p>
  <p class="text-slate-800 font-mono text-xs">UUCP = UAW + UUCW</p>
  <p class="text-slate-800 font-mono text-xs">= 12 + 130</p>
  <div class="pt-2 text-emerald-700 font-black text-2xl">142 Points</div>
</div>

</div>

---

# Ước Lượng Use Case Points (UCP): Bước 4–7

<div class="grid grid-cols-2 gap-4 mt-4 text-xs">

<div class="p-4 rounded-xl bg-slate-50 border border-slate-200 shadow-sm space-y-2">
  <strong class="text-emerald-900 text-sm block border-b border-slate-200 pb-1">Bước 4 & 5: TCF & ECF (Hệ Số Điều Chỉnh)</strong>
  <p class="text-slate-700"><strong>TCF (Technical Complexity Factor):</strong> 1.13 (Phức tạp OCR & FTS search)</p>
  <p class="text-slate-700"><strong>ECF (Environment Complexity Factor):</strong> 0.785 (Đội ngũ 4 người thành thạo công nghệ)</p>
  <p class="text-slate-800 font-bold mt-2">AUCP = UUCP $\times$ TCF $\times$ ECF = $142 \times 1.13 \times 0.785 \approx \mathbf{126\ UCP}$</p>
</div>

<div class="p-4 rounded-xl bg-emerald-50/90 border border-emerald-300 shadow-sm space-y-2 text-center">
  <strong class="text-emerald-900 text-sm block border-b border-emerald-300 pb-1">Bước 6 & 7: Effort & Tổng Thời Gian</strong>
  <p class="text-slate-700 text-xs">Nỗ lực thô: $126 \text{ UCP} \times 20 \text{h/UCP} = 2.520 \text{ giờ-người} \approx 15.75 \text{ PM}$</p>
  <p class="text-slate-700 text-xs">Tái sử dụng mã nguồn 40% (FastAPI, Docker, MinIO sẵn có):</p>
  <div class="text-emerald-700 font-black text-3xl mt-1">10 Person-Months</div>
  <span class="badge bg-emerald-700 text-white text-[10px] px-3 py-1 font-bold rounded-full">~ 5 Tháng Triển Khai (Đội 2 FTE)</span>
</div>

</div>

---

# Ước Lượng Nỗ Lực Bằng Mô Hình COCOMO II

<div class="grid grid-cols-2 gap-4 mt-4 text-xs">

<div class="p-4 rounded-xl bg-slate-50 border border-slate-200 shadow-sm space-y-2">
  <strong class="text-emerald-900 text-sm block border-b border-slate-200 pb-1">Đầu Vào Kích Thước KSLOC</strong>
  <p class="text-slate-700">Tổng quy mô mã nguồn ước tính: <strong>15 KSLOC</strong> (Python Backend FastAPI + React SPA + Docker Configs).</p>
  <p class="text-slate-700">Mô hình ứng dụng: Organic Model (Đội ngũ nhỏ, môi trường quen thuộc).</p>
</div>

<div class="p-4 rounded-xl bg-slate-50 border border-slate-200 shadow-sm space-y-2">
  <strong class="text-emerald-900 text-sm block border-b border-slate-200 pb-1">Kết Quả Tính Toán COCOMO II</strong>
  <p class="text-slate-700">Nỗ lực lý thuyết thô: $E = 2.4 \times (15)^{1.05} \approx \mathbf{48.6\ PM}$</p>
  <p class="text-slate-700">Điều chỉnh thực tế (Ứng dụng AI Assistant + Mã nguồn mở 80%):</p>
  <div class="text-emerald-700 font-black text-2xl mt-1">10.2 Person-Months</div>
</div>

</div>

---

# Đối Chuẩn Kết Quả: UCP vs COCOMO II

<div class="grid grid-cols-2 gap-6 mt-4 text-xs">

<div class="p-5 rounded-xl bg-slate-50 border border-slate-200 shadow-sm text-center space-y-2">
  <span class="text-slate-600 font-bold block">Phương Pháp Use Case Points (UCP)</span>
  <span class="text-emerald-700 font-black text-3xl block">10.0 PM</span>
  <p class="text-slate-600 text-[11px]">Dựa trên 14 Use Cases & TCF/ECF điều chỉnh</p>
</div>

<div class="p-5 rounded-xl bg-slate-50 border border-slate-200 shadow-sm text-center space-y-2">
  <span class="text-slate-600 font-bold block">Phương Pháp COCOMO II</span>
  <span class="text-emerald-700 font-black text-3xl block">10.2 PM</span>
  <p class="text-slate-600 text-[11px]">Dựa trên 15 KSLOC & Hệ số nhân nỗ lực AI</p>
</div>

</div>

<div class="mt-4 p-4 rounded-xl bg-emerald-50 border border-emerald-300 text-xs text-slate-800 shadow-sm text-center">
  <strong class="text-emerald-900 text-sm block">Độ Tin Cậy Cao: Cả 2 Phương Pháp Độc Lập Đều Hội Tụ Về ~10 PM (~5 Tháng Đội 2 FTE)</strong>
</div>

---

# Dự Toán Ngân Sách Chi Tiết: CapEx

| Hạng Mục Thiết Bị & Hạ Tầng | Số Lượng | Đơn Giá (VNĐ) | Thành Tiền (VNĐ) |
| :--- | :--- | :--- | :--- |
| **Máy Scan Chuyên Dụng V-shaped (Book Scanner 300 DPI)** | 2 Máy | 30.000.000 | 60.000.000 |
| **Bổ Sung Ổ Cứng SSD Enterprise Cho Server vSphere** | 2 Ổ (2TB) | 7.500.000 | 15.000.000 |
| **Thiết Bị Lưu Trữ Backup Dự Phòng (NAS Storage)** | 1 Bộ | 12.000.000 | 12.000.000 |
| **TỔNG DỰ TOÁN CAPEX KHỞI ĐỘNG** | | | **87.000.000 VNĐ** |

<div class="mt-4 p-3 bg-emerald-50 rounded-lg border border-emerald-200 text-xs text-slate-800 shadow-sm">
  <strong>Đánh giá ngân sách CapEx:</strong> Nằm hoàn toàn trong hạn mức phê duyệt $75.000.000 – 95.000.000 \text{ VNĐ}$ của Ban Giám hiệu.
</div>

---

# Dự Toán Ngân Sách Chi Tiết: OpEx Hàng Năm

| Hạng Mục Chi Phí Vận Hành (Hàng Năm) | Chi Phí Dự Kiến (VNĐ / Năm) | Ghi Chú |
| :--- | :--- | :--- |
| **Thù Lao Cộng Tác Viên Sinh Viên Soát Lỗi OCR** | 18.000.000 | Chi trả theo giờ công số hóa 2.000 sách |
| **Bảo Trì Thiết Bị Scan & Thay Thế Linh Kiện** | 5.000.000 | Hợp đồng bảo trì định kỳ 12 tháng |
| **Chi Phí Điện Điện Đạm & Hạ Tầng Máy Chủ Nội Bộ** | 4.000.000 | Tận dụng phòng Server hiện hữu của Trường |
| **TỔNG DỰ TOÁN OPEX HÀNG NĂM** | **27.000.000 VNĐ / Năm** | Tiết kiệm hơn 35 Tr/năm nhờ Cost Avoidance |

---

# Dự Báo Tiến Độ Dựa Trên Throughput Thực Tế

<div class="grid grid-cols-2 gap-4 mt-4 text-xs">

<div class="p-4 rounded-xl bg-slate-50 border border-slate-200 shadow-sm space-y-2">
  <strong class="text-emerald-900 text-sm block border-b border-slate-200 pb-1">Thông Số Throughput Thực Tế Đo Từ Kanban</strong>
  <p class="text-slate-700">Throughput trung bình: <strong>2.2 User Stories / Tuần</strong> (Đội 4 người kiêm nhiệm 50%).</p>
  <p class="text-slate-700">Tổng quy mô Backlog MVP: <strong>23 Stories</strong>.</p>
</div>

<div class="p-4 rounded-xl bg-emerald-50/80 border border-emerald-200 shadow-sm space-y-2">
  <strong class="text-emerald-900 text-sm block border-b border-emerald-200 pb-1">Kết Quả Mô Phỏng Dự Báo Tiến Độ</strong>
  <p class="text-slate-800 font-bold">Thời gian hoàn thành MVP: $23 / 2.2 \approx \mathbf{10.45\ Tuần}$.</p>
  <p class="text-slate-700">Cộng 1.5 tuần dự phòng buffer $\rightarrow$ Đảm bảo 100% hoàn thành MVP đúng mốc Tuần 12.</p>
</div>

</div>

---

# Ghi Nhận Nỗ Lực & AI Session Logging

<div class="space-y-3 mt-4 text-xs">

<div class="p-3 bg-slate-50 rounded-lg border border-slate-200 shadow-sm">
  <strong class="text-emerald-900 text-sm block mb-1">1. Định Dạng Chuẩn Ghi Log Nhóm (`project_log.md`)</strong>
  <p class="text-slate-700 font-mono text-[11px]">[2026-08-15] [LDMS-004] Nguyễn Văn A hoàn thành giao diện Split-screen (Effort: 5h, AI Tokens: 14,500).</p>
</div>

<div class="p-3 bg-slate-50 rounded-lg border border-slate-200 shadow-sm">
  <strong class="text-emerald-900 text-sm block mb-1">2. Minh Bạch Nỗ Lực & Hiệu Quả Ứng Dụng AI Assistant</strong>
  <p class="text-slate-700">Mỗi dòng log phản ánh trung thực số giờ công lao động thực tế và khối lượng token AI hỗ trợ, tạo minh chứng dữ liệu cho báo cáo nghiệm thu.</p>
</div>

</div>

---

# Báo Cáo Giám Sát Gating Checkpoints

<div class="grid grid-cols-2 gap-4 mt-4 text-xs">

<div class="p-3 bg-slate-50 rounded-lg border border-slate-200 space-y-1">
  <strong class="text-emerald-900 block">Gate 0 (Tuần 2): Khảo Sát & Pháp Lý</strong>
  <p class="text-slate-700">Nghiệm thu Quy chế bản quyền số & danh mục 2.500 sách. Phê duyệt mua sắm CapEx đợt 1.</p>
</div>

<div class="p-3 bg-emerald-50/80 rounded-lg border border-emerald-200 space-y-1">
  <strong class="text-emerald-900 block">Gate 1 (Tuần 12): Nghiệm Thu MVP</strong>
  <p class="text-slate-700">Nghiệm thu Core System & 500 giáo trình CNTT số hóa. Đánh giá KPI FTS < 3s & CAR $\ge$ 85%.</p>
</div>

<div class="p-3 bg-slate-50 rounded-lg border border-slate-200 space-y-1">
  <strong class="text-emerald-900 block">Gate 2 (Tuần 18): Số Hóa Diện Rộng</strong>
  <p class="text-slate-700">Nghiệm thu 2.000 đầu sách mở rộng. Kiểm tra hệ thống lưu trữ MinIO & phân quyền SSO.</p>
</div>

<div class="p-3 bg-slate-50 rounded-lg border border-slate-200 space-y-1">
  <strong class="text-emerald-900 block">Gate 3 (Tuần 20): Go-Live Toàn Trường</strong>
  <p class="text-slate-700">Nghiệm thu Pentest bảo mật DRM, bàn giao chính thức cho Thư viện vận hành lâu dài.</p>
</div>

</div>

---

# Quản Lý Thay Đổi & Tờ Trình Đổi Scope

<div class="p-5 rounded-xl bg-slate-50 border border-slate-200 shadow-sm text-xs space-y-3 mt-4">

<strong class="text-emerald-900 text-sm block border-b border-slate-200 pb-1.5">Quy Trình Kiểm Soát Thay Đổi (Change Control Procedure)</strong>

<div class="grid grid-cols-3 gap-3 text-slate-700 text-center">
  <div class="p-2.5 bg-white border border-slate-200 rounded">
    <strong class="text-emerald-800 block mb-0.5">1. Tiếp Nhận Yêu Cầu</strong>
    Ghi nhận Change Request từ Stakeholders vào Backlog.
  </div>
  <div class="p-2.5 bg-white border border-slate-200 rounded">
    <strong class="text-emerald-800 block mb-0.5">2. Phân Tích Tác Động</strong>
    PM đánh giá ảnh hưởng ngân sách (>5%) & mốc tiến độ Tuần 12.
  </div>
  <div class="p-2.5 bg-white border border-slate-200 rounded">
    <strong class="text-emerald-800 block mb-0.5">3. Trình Phê Duyệt</strong>
    Ký Tờ trình thay đổi có chữ ký PM + Giám đốc Thư viện.
  </div>
</div>

</div>

---

# Đánh Giá Sau Triển Khai (Post-Implementation Review)

<div class="grid grid-cols-2 gap-4 mt-4 text-xs">

<div class="p-4 rounded-xl bg-emerald-50/80 border border-emerald-200 shadow-sm space-y-2">
  <strong class="text-emerald-900 text-sm block border-b border-emerald-200 pb-1">Thành Công Đạt Được</strong>
  <ul class="space-y-1.5 text-slate-700">
    <li>Bảo tồn 100% tài liệu học thuật quý hiếm của Nhà trường.</li>
    <li>Giải phóng 60-70% diện tích kệ sách giấy để làm Smart Learning Space.</li>
    <li>Đội ngũ kỹ sư nội bộ làm chủ 100% công nghệ số hóa.</li>
  </ul>
</div>

<div class="p-4 rounded-xl bg-amber-50/80 border border-amber-200 shadow-sm space-y-2">
  <strong class="text-amber-900 text-sm block border-b border-amber-200 pb-1">Bài Học Kinh Nghiệm (Lessons Learned)</strong>
  <ul class="space-y-1.5 text-slate-700">
    <li>Kỷ luật Kanban WIP=1 giúp đội kiêm nhiệm không bị trễ hạn.</li>
    <li>Ứng dụng AI Assistant rút ngắn 60% thời gian viết code thô.</li>
    <li>Giao diện Split-screen là chìa khóa tăng năng suất soát lỗi OCR.</li>
  </ul>
</div>

</div>

---

# Tổng Kết Bộ Slide Presentation HCMUS-LDMS

<div class="grid grid-cols-5 gap-2 mt-6 text-xs text-center">

<div class="p-3 bg-slate-50 border border-slate-200 rounded-lg">
  <strong class="text-emerald-900 text-[11px] block">Phần 1: Proposal</strong>
  <p class="text-[10px] text-slate-600 mt-1">Đề xuất dự án & hiệu quả đầu tư</p>
</div>

<div class="p-3 bg-slate-50 border border-slate-200 rounded-lg">
  <strong class="text-emerald-900 text-[11px] block">Phần 2: Governance</strong>
  <p class="text-[10px] text-slate-600 mt-1">Vision, Charter & 26 Stories Backlog</p>
</div>

<div class="p-3 bg-slate-50 border border-slate-200 rounded-lg">
  <strong class="text-emerald-900 text-[11px] block">Phần 3: Architecture</strong>
  <p class="text-[10px] text-slate-600 mt-1">Modular Monolith & DRM Signed URL</p>
</div>

<div class="p-3 bg-slate-50 border border-slate-200 rounded-lg">
  <strong class="text-emerald-900 text-[11px] block">Phần 4: Development</strong>
  <p class="text-[10px] text-slate-600 mt-1">Hybrid Kanban & AI-Assisted</p>
</div>

<div class="p-3 bg-slate-50 border border-slate-200 rounded-lg">
  <strong class="text-emerald-900 text-[11px] block">Phần 5: Estimation</strong>
  <p class="text-[10px] text-slate-600 mt-1">UCP/COCOMO II & Gating Checkpoints</p>
</div>

</div>

---

# Hỏi & Đáp & Lời Cảm Ơn Cuối Cùng

<div class="text-center my-auto py-10 space-y-4">
  <h2 class="text-3xl font-extrabold text-emerald-900">KÍNH CHÚC BỘ SLIDE BÁO CÁO THÀNH CÔNG RỰC RỠ!</h2>
  <p class="text-slate-600 text-sm">Trường ĐH Khoa học Tự nhiên — ĐHQG-HCM (HCMUS-LDMS 2026)</p>
  <div class="pt-6">
    <span class="badge bg-emerald-700 text-white font-bold px-5 py-2 text-sm rounded-full shadow">Hoàn Thành 100% Bộ Slide Thuyết Trình</span>
  </div>
</div>
