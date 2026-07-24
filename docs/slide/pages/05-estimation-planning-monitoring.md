---
layout: default
class: bg-slate-50
---

<div class="relative flex flex-col justify-center h-full p-8 overflow-hidden">
  <div class="absolute right-4 top-1/2 -translate-y-1/2 text-[15rem] font-extrabold leading-none select-none pointer-events-none opacity-[0.08] font-mono text-emerald-900">05</div>
  <div class="z-10">
    <div class="text-xs uppercase tracking-widest text-amber-600 font-extrabold mb-2 font-mono">Phần 05</div>
    <h1 class="text-4xl font-black text-slate-900 leading-tight mb-4">Ước Lượng, Lập Kế Hoạch & Giám Sát Dự Án</h1>
    <div class="w-16 h-1 bg-emerald-600 rounded mb-6"></div>
    <p class="text-slate-600 text-sm max-w-xl leading-relaxed mb-6 font-semibold">Phần này giải thích: nhóm ước lượng thời gian/chi phí/nguồn lực bằng cách nào (có AI hỗ trợ), bản kế hoạch dự án gồm những gì, tài liệu "Phát biểu công việc" (SOW) có ý nghĩa gì, và cách nhóm thu thập số liệu thật để báo cáo tình trạng dự án.</p>
    <div class="flex gap-2 flex-wrap">
      <span class="text-[10px] font-bold text-slate-800 bg-white border border-slate-200 px-3 py-1 rounded-full shadow-sm">Ước lượng UCP & COCOMO II</span>
      <span class="text-[10px] font-bold text-slate-800 bg-white border border-slate-200 px-3 py-1 rounded-full shadow-sm">Kế hoạch & Đường găng</span>
      <span class="text-[10px] font-bold text-slate-800 bg-white border border-slate-200 px-3 py-1 rounded-full shadow-sm">Tài liệu SOW</span>
      <span class="text-[10px] font-bold text-slate-800 bg-white border border-slate-200 px-3 py-1 rounded-full shadow-sm">Số liệu giám sát thực tế</span>
    </div>
  </div>
</div>

<div class="mt-4 text-[9px] text-slate-500 leading-normal border-t border-slate-200 pt-1">
  <strong>UCP</strong>: Use Case Points (phương pháp ước lượng công sức dựa trên các use case) <br>
  <strong>COCOMO II</strong>: Constructive Cost Model II (phương pháp ước lượng công sức dựa trên dòng code KSLOC) <br>
  <strong>SOW</strong>: Statement of Work (tài liệu Phát biểu công việc)
</div>

---

# Vì Sao Cần Ước Lượng Trước Khi Làm?

<div class="mt-2 text-[12px] text-slate-900 leading-normal border-t border-slate-200 pt-1">
Trước khi bắt tay vào code, nhóm cần trả lời 3 câu hỏi: <strong>Dự án tốn bao nhiêu thời gian? Cần bao nhiêu người? Chi phí bao nhiêu?</strong> Ước lượng càng sát thực tế thì kế hoạch càng đáng tin, và Ban Giám hiệu càng dễ ra quyết định cấp ngân sách.
</div>

<div class="grid grid-cols-2 gap-4 mt-4 text-xs">

<div class="p-4 rounded-xl bg-emerald-50/80 border border-emerald-200 shadow-sm space-y-2">
  <strong class="text-emerald-900 text-sm block border-b border-emerald-200 pb-1">Nhóm dùng 2 phương pháp độc lập để đối chiếu</strong>
  <ul class="space-y-1.5 text-slate-700">
    <li><strong>UCP (Use Case Points):</strong> ước lượng dựa trên số lượng và độ phức tạp của các "ca sử dụng" (use case) — tức các chức năng người dùng sẽ dùng.</li>
    <li><strong>COCOMO II:</strong> ước lượng dựa trên quy mô mã nguồn dự kiến (số dòng code).</li>
  </ul>
  <p class="text-slate-700">Nếu 2 phương pháp cho ra kết quả gần nhau, độ tin cậy của con số ước lượng sẽ cao hơn nhiều so với chỉ dùng 1 phương pháp.</p>
</div>

<div class="p-4 rounded-xl bg-amber-50/80 border border-amber-200 shadow-sm space-y-2">
  <strong class="text-amber-900 text-sm block border-b border-amber-200 pb-1">Vai trò của AI trong việc ước lượng</strong>
  <ul class="space-y-1.5 text-slate-700">
    <li>AI Assistant giúp bóc tách nhanh danh sách use case, gợi ý mức độ phức tạp, và tính toán các công thức UCP/COCOMO không sai sót.</li>
    <li>Vì nhóm dùng AI Coding Assistant hỗ trợ viết code (làm nhanh hơn), nhóm điều chỉnh giảm nỗ lực thô tính ra từ công thức, thay vì áp dụng y nguyên số lý thuyết.</li>
  </ul>
</div>

</div>

---

# Lộ Trình 4 Giai Đoạn & Điểm Nghẽn Tiến Độ (Đường Găng)

<div class="mt-2 text-[12px] text-slate-900 leading-normal border-t border-slate-200 pt-1">
"Đường găng" (Critical Path) là chuỗi công việc mà nếu bị trễ dù chỉ 1 ngày, cả dự án sẽ bị trễ theo. Nhóm xác định trước điểm nghẽn để tập trung theo dõi sát nhất.
</div>

<div class="space-y-3 mt-4 text-xs">

<div class="p-3 bg-slate-50 rounded-lg border border-slate-200 shadow-sm flex justify-between items-center">
  <span><strong class="text-emerald-900">Giai đoạn 0 (Tuần 1–2): Khảo sát & Bản quyền</strong> — Ban hành quy chế sở hữu trí tuệ & khảo sát 2.500 tài liệu.</span>
  <span class="badge bg-slate-200 text-slate-800 font-bold px-2.5 py-0.5 rounded shrink-0 whitespace-nowrap">2 Tuần</span>
</div>

<div class="p-3 bg-slate-50 rounded-lg border border-slate-200 shadow-sm flex justify-between items-center">
  <span><strong class="text-emerald-900">Giai đoạn 1 (Tuần 3–12): Phát triển MVP & Thí điểm 500 sách</strong> — Xây hệ thống lõi & số hóa thí điểm 500 sách CNTT.</span>
  <span class="badge bg-slate-200 text-slate-800 font-bold px-2.5 py-0.5 rounded shrink-0 whitespace-nowrap">10 Tuần</span>
</div>

<div class="p-3 bg-red-50/90 rounded-lg border border-red-300 shadow-sm flex justify-between items-center">
  <span><strong class="text-red-900 font-bold">Giai đoạn 2 (Tuần 13–18): Số hóa 2.000 tài liệu [ĐIỂM NGHẼN]</strong> — Phụ thuộc năng suất scan & soát lỗi OCR thực tế.</span>
  <span class="badge bg-red-700 text-white font-bold px-2.5 py-0.5 rounded shrink-0 whitespace-nowrap">6 Tuần (Nút thắt)</span>
</div>

<div class="p-3 bg-slate-50 rounded-lg border border-slate-200 shadow-sm flex justify-between items-center">
  <span><strong class="text-emerald-900">Giai đoạn 3 (Tuần 19–20): Nghiệm thu & Vận hành toàn trường</strong> — Kiểm thử bảo mật, kiểm thử người dùng thật, bàn giao chính thức.</span>
  <span class="badge bg-slate-200 text-slate-800 font-bold px-2.5 py-0.5 rounded shrink-0 whitespace-nowrap">2 Tuần</span>
</div>

</div>

<div class="mt-4 p-3 bg-amber-50 rounded-lg border border-amber-200 text-xs text-slate-800 shadow-sm">
  <strong>Cảnh báo quản lý tiến độ:</strong> Giai đoạn 2 (số hóa tài liệu) là điểm nghẽn duy nhất. Mọi chậm trễ ở giai đoạn này sẽ kéo lùi ngày vận hành chính thức của toàn dự án.
</div>

<div class="mt-4 text-[9px] text-slate-500 leading-normal border-t border-slate-200 pt-1">
  <strong>MVP</strong>: Minimum Viable Product (phiên bản sản phẩm tối thiểu) <br>
  <strong>OCR</strong>: Optical Character Recognition (nhận dạng ký tự từ ảnh quét)
</div>

---

# Ước Lượng Theo Use Case Points (UCP) — Bước 1 đến 3

<div class="grid grid-cols-3 gap-4 mt-4 text-xs">

<div class="p-4 rounded-xl bg-slate-50 border border-slate-200 shadow-sm space-y-1.5">
  <strong class="text-emerald-900 text-sm block border-b border-slate-200 pb-1">Bước 1: Đếm tác nhân (UAW)</strong>
  <p class="text-slate-700">· <strong>Đơn giản (API/Hệ thống):</strong> 3 tác nhân (Keycloak, MinIO, Elasticsearch) → 3 × 1 = 3</p>
  <p class="text-slate-700">· <strong>Phức tạp (Giao diện đồ họa):</strong> 3 tác nhân (Độc giả, Biên tập viên, Admin) → 3 × 3 = 9</p>
  <div class="pt-1 text-emerald-800 font-bold text-sm border-t border-slate-100 mt-2">Tổng UAW = 12</div>
</div>

<div class="p-4 rounded-xl bg-slate-50 border border-slate-200 shadow-sm space-y-1.5">
  <strong class="text-emerald-900 text-sm block border-b border-slate-200 pb-1">Bước 2: Đếm ca sử dụng (UUCW)</strong>
  <p class="text-slate-700">· <strong>Đơn giản:</strong> 6 Use Cases (Đăng nhập, Phân quyền, Upload, Metadata...) → 6 × 5 = 30</p>
  <p class="text-slate-700">· <strong>Trung bình:</strong> 4 Use Cases (OCR ngầm, Custom Reader, Bookmark, Sprint) → 4 × 10 = 40</p>
  <p class="text-slate-700">· <strong>Phức tạp:</strong> 4 Use Cases (Split-screen, FTS Search, Epub DRM, Highlight) → 4 × 15 = 60</p>
  <div class="pt-1 text-emerald-800 font-bold text-sm border-t border-slate-100 mt-2">Tổng UUCW = 130</div>
</div>

<div class="p-4 rounded-xl bg-emerald-50/80 border border-emerald-200 shadow-sm space-y-1.5 text-center flex flex-col justify-between">
  <div>
    <strong class="text-emerald-900 text-sm block border-b border-emerald-200 pb-1">Bước 3: Cộng điểm thô (UUCP)</strong>
    <p class="text-slate-600 mt-2">Công thức:</p>
    <p class="text-slate-800 font-mono text-[11px]">UUCP = UAW + UUCW</p>
    <p class="text-slate-800 font-mono text-[11px]">= 12 + 130</p>
  </div>
  <div class="text-emerald-700 font-black text-2xl mt-auto">142 điểm</div>
</div>

</div>

---

# Ước Lượng Theo Use Case Points (UCP) — Bước 4 đến 7

<div class="grid grid-cols-2 gap-4 mt-4 text-xs">

<div class="p-4 rounded-xl bg-slate-50 border border-slate-200 shadow-sm space-y-2">
  <strong class="text-emerald-900 text-sm block border-b border-slate-200 pb-1">Bước 4 & 5: Điều chỉnh theo độ khó kỹ thuật & môi trường</strong>
  <p class="text-slate-700">· <strong>TCF (Độ khó kỹ thuật):</strong> 1.13 (hệ thống phân tán, bảo mật DRM động)</p>
  <p class="text-slate-700">· <strong>ECF (Môi trường):</strong> 0.785 (nhóm 4 dev quen thuộc công nghệ, động lực cao)</p>
  <p class="text-slate-800 font-bold mt-2 border-t border-slate-200 pt-2 text-[11px]">Điểm đã điều chỉnh (AUCP) = 142 × 1.13 × 0.785 ≈ <strong>126 UCP</strong></p>
</div>

<div class="p-4 rounded-xl bg-emerald-50/90 border border-emerald-300 shadow-sm space-y-2 text-center">
  <strong class="text-emerald-900 text-sm block border-b border-emerald-300 pb-1">Bước 6 & 7: Quy đổi nỗ lực phần mềm</strong>
  <p class="text-slate-700 text-[11px]">· Nỗ lực thô: 126 điểm × 20 giờ/UCP = 2.520 người-giờ ≈ 15.75 PM</p>
  <p class="text-slate-700 text-[11px] mt-1">· Trừ 40% tái sử dụng API open-source (MinIO, Postgres FTS, Google OAuth):</p>
  <div class="text-emerald-700 font-black text-3xl mt-1">10.0 PM</div>
  <span class="badge bg-emerald-700 text-white text-[10px] px-3 py-1 font-bold rounded-full">≈ 5.0 tháng làm việc của 4 kỹ sư kiêm nhiệm 50% (2 FTE)</span>
</div>

</div>

<div class="mt-4 text-[9px] text-slate-500 leading-normal border-t border-slate-200 pt-1">
  <strong>PM (Person-Month)</strong>: Người-Tháng (1 PM = 160 giờ làm việc). <strong>FTE (Full-time Equivalent)</strong>: Tương đương nhân sự toàn thời gian.
</div>

---

# Ước Lượng Theo Mô Hình COCOMO II

<div class="grid grid-cols-2 gap-4 mt-4 text-xs">

<div class="p-4 rounded-xl bg-slate-50 border border-slate-200 shadow-sm space-y-2">
  <strong class="text-emerald-900 text-sm block border-b border-slate-200 pb-1">Đầu vào: Quy mô mã nguồn (KLOC)</strong>
  <p class="text-slate-700">· Quy mô hệ thống dự kiến: **8.5 KLOC** (8.500 dòng code React & FastAPI).</p>
  <p class="text-slate-700">· Hệ số quy mô B = 1.05. Hệ số điều chỉnh tích hợp EAF = 0.95.</p>
  <p class="text-slate-700">· Nỗ lực lý thuyết thô: 2.94 × 0.95 × (8.5)^1.05 ≈ **26.3 PM**.</p>
</div>

<div class="p-4 rounded-xl bg-slate-50 border border-slate-200 shadow-sm space-y-2">
  <strong class="text-emerald-900 text-sm block border-b border-slate-200 pb-1">Nỗ lực thực tế viết mới</strong>
  <p class="text-slate-700">· Tái sử dụng 60% code nhờ tích hợp MinIO, Keycloak, Postgres FTS.</p>
  <p class="text-slate-700">· Khối lượng code viết mới thực tế chỉ cần: **3.5 KLOC**.</p>
  <p class="text-slate-700">· Công thức tính nỗ lực thực tế viết mới:</p>
  <div class="text-emerald-700 font-black text-2xl mt-1">10.4 PM</div>
  <p class="text-slate-500 text-[10px] mt-1">2.94 × 0.95 × (3.5)^1.05 ≈ 10.4 PM (khớp với UCP)</p>
</div>

</div>

---

# Đối Chiếu Kết Quả: Hai Phương Pháp Có Khớp Nhau Không?

<div class="grid grid-cols-2 gap-6 mt-4 text-xs">

<div class="p-5 rounded-xl bg-slate-50 border border-slate-200 shadow-sm text-center space-y-2 flex flex-col justify-between">
  <span class="text-slate-600 font-bold block">Phương pháp Use Case Points (UCP)</span>
  <span class="text-emerald-700 font-black text-3xl block my-2">10.0 PM</span>
  <p class="text-slate-600 text-[11px]">Góc nhìn <strong>Top-Down</strong>: Dựa trên ca sử dụng & độ phức tạp nghiệp vụ</p>
</div>

<div class="p-5 rounded-xl bg-slate-50 border border-slate-200 shadow-sm text-center space-y-2 flex flex-col justify-between">
  <span class="text-slate-600 font-bold block">Phương pháp COCOMO II</span>
  <span class="text-emerald-700 font-black text-3xl block my-2">10.4 PM</span>
  <p class="text-slate-600 text-[11px]">Góc nhìn <strong>Bottom-Up</strong>: Dựa trên quy mô mã nguồn thực tế viết mới</p>
</div>

</div>

<div class="mt-4 p-4 rounded-xl bg-emerald-50 border border-emerald-300 text-xs text-slate-800 shadow-sm text-center">
  <strong class="text-emerald-900 text-sm block">Hai mô hình ước lượng độc lập lệch nhau chỉ ~4% (10.0 vs 10.4 PM), khẳng định độ tin cậy cực cao của kế hoạch phát triển 20 tuần (10.5 PM / 2 FTE).</strong>
</div>

---

# Dự Toán Ngân Sách Chi Tiết: Chi Phí Đầu Tư Một Lần (CapEx)

| Hạng mục đầu tư CapEx (Theo SOW và CTR) | Giá trị dự toán (VNĐ) | Mô tả chi tiết |
| :-------------------------------------- | :-------------------- | :------------- |
| **Số hóa & Biên tập EPUB** (CTV SV) | 30.000.000 - 40.000.000 | Thuê sinh viên scan và soát lỗi OCR (~10.000 cuốn) |
| **Phát triển phần mềm** (4 kỹ sư) | 25.000.000 - 35.000.000 | Định mức khoán thù lao phát triển hệ thống |
| **Thiết bị scan & nâng cấp Server** | 10.000.000 - 12.000.000 | 02 máy scan chuyên dụng chữ V + linh kiện server |
| **Đào tạo, Triển khai & AI Tools** | 7.000.000 - 12.000.000 | Hướng dẫn sử dụng + phí bản quyền/AI API (≤5 triệu) |
| **Dự phòng rủi ro phát sinh (~15%)** | 5.000.000 - 10.000.000 | Buffer xử lý các lỗi hoặc phát sinh phần cứng |
| **Tổng dự toán CapEx đầu tư ban đầu** | **77M - 106M VNĐ** | **Cam kết dưới 100.000.000 VNĐ trong năm đầu** |

<div class="mt-4 text-[9px] text-slate-500 leading-normal border-t border-slate-200 pt-1">
  <strong>CapEx (Capital Expenditure)</strong>: Chi phí đầu tư ban đầu một lần để xây dựng và đưa hệ thống vào hoạt động.
</div>

---

# Dự Toán Ngân Sách Chi Tiết: Chi Phí Vận Hành Hàng Năm (OpEx)

| Hạng mục chi phí vận hành OpEx (Hàng năm) | Chi phí dự kiến (VNĐ/năm) | Ghi chú |
| :---------------------------------------- | :------------------------ | :------ |
| **Hạ tầng Server & Cloud** | 4.000.000 - 8.000.000 | Điện, mạng băng thông rộng, máy lạnh server room |
| **Bảo trì & Hỗ trợ kỹ thuật** | 6.000.000 - 12.000.000 | Vá lỗi bảo mật, nâng cấp thư viện code định kỳ |
| **Dịch vụ Cloud OCR dự phòng** | 3.000.000 - 6.000.000 | Dùng API đám mây khi gặp tài liệu quá mờ |
| **Số hóa bổ sung sách mới hàng năm** | 2.000.000 - 4.000.000 | Quy trình số hóa cuốn chiếu cho đầu sách mới nhập |
| **Tổng dự toán OpEx duy trì hàng năm** | **15.000.000 - 30.000.000 VNĐ** | Tiết kiệm chi phí kho lưu trữ vật lý của thư viện |

<div class="mt-4 text-[9px] text-slate-500 leading-normal border-t border-slate-200 pt-1">
  <strong>OpEx (Operational Expenditure)</strong>: Chi phí vận hành, bảo trì định kỳ hàng năm để duy trì hoạt động của hệ thống.
</div>

---

# Tài Liệu "Phát Biểu Công Việc" (Statement of Work — SOW) Là Gì?

<div class="mt-2 text-[12px] text-slate-900 leading-normal border-t border-slate-200 pt-1">
<strong>SOW là văn bản đánh dấu việc lập kế hoạch dự án đã xong</strong>, chuyển sang giai đoạn thực thi. Khi các bên ký vào SOW, nghĩa là mọi người đã <strong>đồng ý chung một bản kế hoạch duy nhất</strong> — không còn tranh cãi "ai yêu cầu gì, làm đến đâu, bao nhiêu tiền".
</div>

<div class="grid grid-cols-2 gap-4 mt-4 text-xs">

<div class="p-4 rounded-xl bg-emerald-50/80 border border-emerald-200 shadow-sm space-y-2">
  <strong class="text-emerald-900 text-sm block border-b border-emerald-200 pb-1">SOW ghi nhận sự đồng thuận về 5 điều</strong>
  <ul class="space-y-1.5 text-slate-700 list-disc list-inside">
    <li>Phạm vi công việc cụ thể sẽ làm, và những gì <strong>không</strong> làm.</li>
    <li>Công nghệ đã thống nhất sử dụng.</li>
    <li>Thời gian, chi phí và nguồn lực được cam kết.</li>
    <li>Quy chế xử lý khi có thay đổi phạm vi dự án.</li>
    <li>Vai trò của công cụ AI trong quá trình phát triển.</li>
  </ul>
</div>

<div class="p-4 rounded-xl bg-amber-50/80 border border-amber-200 shadow-sm space-y-2">
  <strong class="text-amber-900 text-sm block border-b border-amber-200 pb-1">Các bên tham gia ký kết</strong>
  <ul class="space-y-1.5 text-slate-700">
    <li><strong>Bên tài trợ:</strong> Ban Giám hiệu — phê duyệt chủ trương và cấp ngân sách.</li>
    <li><strong>Bên chủ trì nghiệp vụ:</strong> Ban Giám đốc Thư viện — xác nhận yêu cầu và nghiệm thu.</li>
    <li><strong>Bên phát triển:</strong> Phòng CNTT / nhóm sinh viên — thực hiện và bàn giao sản phẩm.</li>
  </ul>
</div>

</div>

<div class="mt-4 p-3 bg-slate-50 rounded-lg border border-slate-200 text-xs text-slate-800 shadow-sm">
  <strong>Lưu ý quan trọng:</strong> Sau khi SOW được ký, nếu muốn thay đổi phạm vi công việc thì tính năng, công nghệ, thời gian và chi phí cũng sẽ phải thay đổi theo — không thể chỉ đổi một phần mà giữ nguyên phần còn lại. Mọi thay đổi phải đi qua quy trình kiểm soát thay đổi chính thức.
</div>

---

# Bản Kế Hoạch Dự Án Gồm Những Gì?

<div class="mt-2 text-[12px] text-slate-900 leading-normal border-t border-slate-200 pt-1">
Một bản kế hoạch dự án đầy đủ không chỉ là "làm gì" mà còn phải trả lời rõ 5 câu hỏi sau — mỗi câu hỏi đã được trình bày trong các phần trước của buổi thuyết trình này.
</div>

<div class="grid grid-cols-3 gap-3 mt-4 text-xs">

<div class="p-3 bg-slate-50 rounded-lg border border-slate-200 shadow-sm">
  <strong class="text-emerald-900 block mb-1">Làm gì? (Scope)</strong>
  <p class="text-slate-700">26 user story trong Product Backlog, chia theo mức ưu tiên Bắt buộc / Nên có / Có thì tốt.</p>
</div>

<div class="p-3 bg-slate-50 rounded-lg border border-slate-200 shadow-sm">
  <strong class="text-emerald-900 block mb-1">Làm khi nào? (Schedule)</strong>
  <p class="text-slate-700">4 giai đoạn, 20 tuần, với Giai đoạn 2 là điểm nghẽn cần theo dõi sát.</p>
</div>

<div class="p-3 bg-slate-50 rounded-lg border border-slate-200 shadow-sm">
  <strong class="text-emerald-900 block mb-1">Tốn bao nhiêu? (Budget)</strong>
  <p class="text-slate-700">87 triệu VNĐ đầu tư ban đầu, 27 triệu VNĐ/năm chi phí vận hành.</p>
</div>

<div class="p-3 bg-slate-50 rounded-lg border border-slate-200 shadow-sm">
  <strong class="text-emerald-900 block mb-1">Ai làm? (Resources)</strong>
  <p class="text-slate-700">4 kỹ sư kiêm nhiệm + 2 cán bộ thư viện + cộng tác viên sinh viên, có AI Coding Assistant hỗ trợ.</p>
</div>

<div class="p-3 bg-slate-50 rounded-lg border border-slate-200 shadow-sm">
  <strong class="text-emerald-900 block mb-1">Theo dõi thế nào? (Monitoring)</strong>
  <p class="text-slate-700">Ghi nhật ký từng phiên làm việc, báo cáo hàng tuần, nghiệm thu tại 4 mốc kiểm tra (Gate).</p>
</div>

<div class="p-3 bg-emerald-50/80 rounded-lg border border-emerald-200 shadow-sm">
  <strong class="text-emerald-900 block mb-1">Thống nhất bằng gì? (SOW)</strong>
  <p class="text-slate-700">Tài liệu Phát biểu công việc (SOW) — nơi tất cả các câu trả lời trên được các bên ký xác nhận chính thức.</p>
</div>

</div>

---

# Demo Thu Thập Dữ Liệu Thật: Ảnh Chụp Nhanh Tiến Độ Tuần 1

<div class="mt-2 text-[12px] text-slate-900 leading-normal border-t border-slate-200 pt-1">
Đây là số liệu <strong>thật</strong>, không phải giả định, được nhóm thu thập từ 2 ngày làm việc đầu tiên (16–17/07/2026), tổng hợp từ nhật ký `project_log.md`.
</div>

<div class="grid grid-cols-2 gap-4 mt-4 text-xs">

<div class="p-4 rounded-xl bg-slate-50 border border-slate-200 shadow-sm space-y-2">
  <strong class="text-emerald-900 text-sm block border-b border-slate-200 pb-1">Bảng tổng hợp tiến độ thực tế</strong>
  <p class="text-slate-700">Số việc đã hoàn thành: <strong>12 / 26</strong> (46% tổng khối lượng công việc)</p>
  <p class="text-slate-700">Tổng thời gian dev thực tế: <strong>4 giờ 05 phút</strong> (4 phiên làm việc)</p>
  <p class="text-slate-700">Tổng token AI đã dùng: <strong>440.000 token</strong> (kết hợp Claude Sonnet 5 + Claude Opus 4.8 + Claude Code)</p>
  <p class="text-slate-700">Tốc độ hoàn thành đo được: <strong>12 việc/tuần</strong> (tuần đầu thường nhanh vì làm các phần nền tảng dễ hơn)</p>
</div>

<div class="p-4 rounded-xl bg-emerald-50/80 border border-emerald-200 shadow-sm space-y-2">
  <strong class="text-emerald-900 text-sm block border-b border-emerald-200 pb-1">Dự báo thời gian hoàn thành (dựa trên tốc độ đo được)</strong>
  <p class="text-slate-700">Còn lại: 26 − 12 = <strong>14 việc</strong>.</p>
  <p class="text-slate-700">Vì các việc còn lại độ khó không đều, nhóm đưa ra khoảng dự báo thay vì một con số cứng:</p>
  <p class="text-slate-700"><strong>Lạc quan:</strong> ~1.8 tuần (hoàn thành tuần 3)</p>
  <p class="text-slate-700"><strong>Thận trọng:</strong> ~3.5 tuần (hoàn thành tuần 5)</p>
  <p class="text-slate-800 font-bold">→ Ước lượng: 2–4 tuần để xong toàn bộ backlog MVP.</p>
</div>

</div>

<div class="mt-3 p-3 bg-slate-50/80 rounded-lg border border-slate-200 text-xs text-slate-700 flex justify-between items-center">
  <span><strong>Chi phí AI thực tế tuần 1:</strong> ~300.000 VNĐ, chỉ chiếm ~6% hạn mức 5 triệu VNĐ dành cho công cụ AI cả dự án.</span>
  <span class="badge bg-emerald-700 text-white font-bold px-2 py-1 rounded shrink-0 whitespace-nowrap">Trong ngân sách</span>
</div>

---

# Demo Thu Thập Dữ Liệu Thật: Đối Chiếu Với Mã Nguồn Thực Tế

<div class="mt-2 text-[12px] text-slate-900 leading-normal border-t border-slate-200 pt-1">
Đây là bằng chứng cho thấy nhóm không chỉ ghi log mà còn <strong>đối chiếu ngược lại với mã nguồn thật</strong> để đảm bảo số liệu báo cáo phản ánh đúng thực tế — tránh trường hợp "báo cáo đẹp nhưng không khớp code".
</div>

<div class="grid grid-cols-2 gap-4 mt-4 text-xs">

<div class="p-4 rounded-xl bg-slate-50 border border-slate-200 shadow-sm space-y-2">
  <strong class="text-emerald-900 text-sm block border-b border-slate-200 pb-1">Số liệu tổng hợp 5 phiên làm việc (16–22/07/2026)</strong>
  <p class="text-slate-700">Tổng thời gian đã ghi log: <strong>12 giờ 05 phút</strong></p>
  <p class="text-slate-700">Tổng token AI đã ghi log: <strong>690.000 token</strong></p>
  <p class="text-slate-700">Số thành viên tham gia ghi log: <strong>4 người</strong></p>
</div>

<div class="p-4 rounded-xl bg-amber-50/80 border border-amber-200 shadow-sm space-y-2">
  <strong class="text-amber-900 text-sm block border-b border-amber-200 pb-1">Phát hiện quan trọng khi đối chiếu</strong>
  <p class="text-slate-700">Kiểm tra thực tế trong mã nguồn: <strong>26/26 công việc đã hoàn thành</strong> (đã gộp mã nguồn, chạy được).</p>
  <p class="text-slate-700">Nhưng nhật ký mới ghi nhận đầy đủ thời gian/token cho <strong>16/26 công việc (~61.5%)</strong>.</p>
</div>

</div>

<div class="mt-3 p-3 bg-emerald-50 rounded-lg border border-emerald-200 text-xs text-slate-800 shadow-sm">
  <strong>Hành động khắc phục:</strong> Nhắc các thành viên còn thiếu bổ sung log cho 10 công việc chưa ghi nhận, để số liệu báo cáo phản ánh đúng 100% công sức và chi phí AI đã thực sự bỏ ra.
</div>

---

# Báo Cáo Giám Sát Tại Các Mốc Kiểm Tra (Gate)

<div class="grid grid-cols-2 gap-4 mt-4 text-xs">

<div class="p-3 bg-slate-50 rounded-lg border border-slate-200 space-y-1">
  <strong class="text-emerald-900 block">Gate 0 (Tuần 2): Khảo sát & Pháp lý</strong>
  <p class="text-slate-700">Nghiệm thu quy chế bản quyền số & danh mục 2.500 sách. Duyệt chi mua sắm đợt 1.</p>
</div>

<div class="p-3 bg-emerald-50/80 rounded-lg border border-emerald-200 space-y-1">
  <strong class="text-emerald-900 block">Gate 1 (Tuần 12): Nghiệm thu MVP</strong>
  <p class="text-slate-700">Nghiệm thu hệ thống lõi & 500 giáo trình đã số hóa. Kiểm tra tốc độ tìm kiếm dưới 3 giây & độ chính xác OCR ≥ 85%.</p>
</div>

<div class="p-3 bg-slate-50 rounded-lg border border-slate-200 space-y-1">
  <strong class="text-emerald-900 block">Gate 2 (Tuần 18): Số hóa diện rộng</strong>
  <p class="text-slate-700">Nghiệm thu 2.000 đầu sách mở rộng. Kiểm tra hệ thống lưu trữ & phân quyền đăng nhập.</p>
</div>

<div class="p-3 bg-slate-50 rounded-lg border border-slate-200 space-y-1">
  <strong class="text-emerald-900 block">Gate 3 (Tuần 20): Vận hành toàn trường</strong>
  <p class="text-slate-700">Nghiệm thu kiểm thử bảo mật, bàn giao chính thức cho Thư viện vận hành lâu dài.</p>
</div>

</div>

<div class="mt-3 p-3 bg-slate-50/80 rounded-lg border border-slate-200 text-xs text-slate-700">
  <strong>Ba tầng báo cáo:</strong> (1) Báo cáo sau mỗi phiên AI — ghi vào nhật ký; (2) Báo cáo hàng tuần — PM tổng hợp gửi Thư viện & Phòng CNTT; (3) Báo cáo chốt cổng — gửi Ban Giám hiệu để duyệt giải ngân giai đoạn kế tiếp.
</div>

---

# Quản Lý Thay Đổi Phạm Vi Dự Án

<div class="p-5 rounded-xl bg-slate-50 border border-slate-200 shadow-sm text-xs space-y-3 mt-4">

<strong class="text-emerald-900 text-sm block border-b border-slate-200 pb-1.5">Quy trình xử lý khi có yêu cầu thay đổi</strong>

<div class="grid grid-cols-3 gap-3 text-slate-700 text-center">
  <div class="p-2.5 bg-white border border-slate-200 rounded">
    <strong class="text-emerald-800 block mb-0.5">1. Tiếp nhận yêu cầu</strong>
    Ghi nhận yêu cầu thay đổi từ các bên liên quan vào danh sách công việc.
  </div>
  <div class="p-2.5 bg-white border border-slate-200 rounded">
    <strong class="text-emerald-800 block mb-0.5">2. Phân tích tác động</strong>
    Quản lý dự án đánh giá ảnh hưởng đến ngân sách (nếu vượt 5%) và mốc tiến độ Tuần 12.
  </div>
  <div class="p-2.5 bg-white border border-slate-200 rounded">
    <strong class="text-emerald-800 block mb-0.5">3. Trình phê duyệt</strong>
    Ký tờ trình thay đổi, có chữ ký của Quản lý dự án và Giám đốc Thư viện.
  </div>
</div>

</div>

---

# Hỏi & Đáp

<div class="text-center my-auto py-10 space-y-4">
  <h2 class="text-3xl font-extrabold text-emerald-900">CẢM ƠN THẦY VÀ CÁC BẠN ĐÃ LẮNG NGHE!</h2>
  <p class="text-slate-600 text-sm">Trường ĐH Khoa học Tự nhiên — ĐHQG-HCM (HCMUS-LDMS 2026)</p>
</div>
