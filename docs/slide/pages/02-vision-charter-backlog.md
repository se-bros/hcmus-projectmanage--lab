---
layout: default
class: bg-slate-50
---

<div class="relative flex flex-col justify-center h-full p-8 overflow-hidden">
  <div class="absolute right-4 top-1/2 -translate-y-1/2 text-[15rem] font-extrabold leading-none select-none pointer-events-none opacity-[0.08] font-mono text-emerald-900">02</div>
  <div class="z-10">
    <div class="text-xs uppercase tracking-widest text-amber-600 font-extrabold mb-2 font-mono">Phần 02</div>
    <h1 class="text-4xl font-black text-slate-900 leading-tight mb-4">Vision & Scope · Charter · Backlog</h1>
    <div class="w-16 h-1 bg-emerald-600 rounded mb-6"></div>
    <p class="text-slate-600 text-sm max-w-xl leading-relaxed mb-6 font-semibold">Đối chuẩn quy trình nghiệp vụ với 3 phương án thay thế (thủ công, kết hợp công cụ, đối thủ), phân tích bên liên quan theo RACI/Power-Interest/Khả năng tiếp cận, và tiêu chí chấp nhận cho từng yêu cầu backlog.</p>
    <div class="flex gap-2 flex-wrap">
      <span class="text-[10px] font-bold text-slate-800 bg-white border border-slate-200 px-3 py-1 rounded-full shadow-sm">Định Vị</span>
      <span class="text-[10px] font-bold text-slate-800 bg-white border border-slate-200 px-3 py-1 rounded-full shadow-sm">Đối Chuẩn 3 Phương Án</span>
      <span class="text-[10px] font-bold text-slate-800 bg-white border border-slate-200 px-3 py-1 rounded-full shadow-sm">RACI & Ảnh Hưởng</span>
      <span class="text-[10px] font-bold text-slate-800 bg-white border border-slate-200 px-3 py-1 rounded-full shadow-sm">Tiêu Chí Chấp Nhận</span>
    </div>
  </div>
</div>

---

# Phát Biểu Định Vị Sản Phẩm

<div class="grid grid-cols-3 gap-4 mt-3 text-xs">
  <!-- Cột 1: Đối Tượng & Thử Thách -->
  <div class="col-span-1 space-y-3">
    <div class="p-3.5 rounded-xl bg-slate-50 border border-slate-200 shadow-sm flex flex-col justify-between h-[105px]">
      <div>
        <span class="text-[9px] uppercase tracking-wider text-emerald-800 font-extrabold block mb-1">Đối Tượng Phục Vụ</span>
        <strong class="text-slate-900 block text-xs leading-snug">Sinh viên, giảng viên và thủ thư Trường ĐH Khoa học Tự nhiên (ĐHQG-HCM)</strong>
      </div>
    </div>
    <div class="p-3.5 rounded-xl bg-red-50/50 border border-red-200 shadow-sm flex flex-col justify-between h-[150px]">
      <div>
        <span class="text-[9px] uppercase tracking-wider text-red-800 font-extrabold block mb-1">Thử Thách Hiện Tại</span>
        <strong class="text-slate-900 block text-xs leading-snug mb-1">Cản trở tri thức</strong>
        <p class="text-slate-600 text-[10px] leading-relaxed">Giáo trình độc bản bị hao mòn vật lý, rào cản di chuyển địa lý 15km và đọc PDF tĩnh vỡ nét trên di động.</p>
      </div>
    </div>
  </div>
  <!-- Cột 2: Hệ Thống & Điểm Khác Biệt -->
  <div class="col-span-1 space-y-3">
    <div class="p-3.5 rounded-xl bg-emerald-50/50 border border-emerald-200 shadow-sm flex flex-col justify-between h-[105px]">
      <div>
        <span class="text-[9px] uppercase tracking-wider text-emerald-800 font-extrabold block mb-1">Giải Pháp HCMUS-LDMS</span>
        <strong class="text-slate-900 block text-xs leading-snug">Hệ thống web nội bộ quản lý và số hóa tài liệu học thuật tập trung</strong>
      </div>
    </div>
    <div class="p-3.5 rounded-xl bg-slate-50 border border-slate-200 shadow-sm flex flex-col justify-between h-[150px]">
      <div>
        <span class="text-[9px] uppercase tracking-wider text-amber-800 font-extrabold block mb-1">Khác Biệt Vượt Trội</span>
        <strong class="text-slate-900 block text-xs leading-snug mb-1">So với PDF scan tĩnh & OPAC cũ</strong>
        <p class="text-slate-600 text-[10px] leading-relaxed">Loại bỏ PDF scan ảnh tĩnh. Tự động hóa co giãn dòng (EPUB reflowable), phân quyền đăng nhập trường và bảo mật DRM.</p>
      </div>
    </div>
  </div>
  <!-- Cột 3: Giá Trị Cốt Lõi -->
  <div class="col-span-1 p-4.5 rounded-xl bg-gradient-to-br from-emerald-400 to-cyan-500 text-black shadow-sm flex flex-col justify-between h-[268px]">
    <div>
      <span class="text-[9px] uppercase tracking-wider text-black font-extrabold block mb-1.5">Giá Trị Cốt Lõi</span>
      <h3 class="text-sm font-black leading-tight mb-2.5">Số Hóa Khép Kín & Bảo Mật Tuyệt Đối</h3>
      <ul class="space-y-2 text-[10px] text-black list-none p-0 m-0">
        <li class="flex items-start gap-1.5">
          <span><strong>Quét → OCR → EPUB 3.0:</strong> Quy trình tự động hóa khép kín có soát lỗi human-in-the-loop.</span>
        </li>
        <li class="flex items-start gap-1.5">
          <span><strong>Tra cứu FTS &lt; 3s:</strong> Tìm kiếm toàn văn thông minh đến từng trang sách.</span>
        </li>
        <li class="flex items-start gap-1.5">
          <span><strong>Bảo mật DRM:</strong> Đường dẫn Signed URL tự hủy 15m, chặn tải sách gốc.</span>
        </li>
      </ul>
    </div>
  </div>
</div>

---

# Quy Trình Hiện Tại (As-Is): Vận Hành Thủ Công

<div class="grid grid-cols-2 gap-4 mt-3 text-[11px]">

<div class="p-4 rounded-xl bg-red-50/80 border border-red-200 shadow-sm">
  <h3 class="text-red-900 font-bold text-xs mb-2 border-b border-red-200 pb-1.5">Vai trò Thủ Thư</h3>
  <ol class="list-decimal pl-4 space-y-1.5 text-slate-700">
    <li>Tiếp nhận sách giấy, xếp lên kệ lưu trữ thô sơ, không đánh giá hiện trạng/chống ẩm mốc.</li>
    <li>Quét thủ công từng trang bằng máy photocopy văn phòng → PDF ảnh tĩnh (image-only).</li>
    <li>Đăng tải bừa bãi lên thư mục chia sẻ công cộng hoặc Google Drive cá nhân, không phân quyền.</li>
  </ol>
</div>

<div class="p-4 rounded-xl bg-amber-50/80 border border-amber-200 shadow-sm">
  <h3 class="text-amber-900 font-bold text-xs mb-2 border-b border-amber-200 pb-1.5">Vai trò Sinh Viên / Độc Giả</h3>
  <ol class="list-decimal pl-4 space-y-1.5 text-slate-700">
    <li>Tra mã sách trên OPAC cũ, di chuyển 15km đến kệ vật lý; hết sách phải chờ đợi.</li>
    <li>Photocopy dịch vụ bên ngoài trường hoặc chụp ảnh từng trang bằng điện thoại.</li>
    <li>Ghi chú/highlight bằng bút dạ quang trên giấy — không tìm kiếm được từ khóa khi ôn thi.</li>
  </ol>
</div>

</div>

<div class="mt-3 p-3 rounded-xl bg-slate-100 text-slate-900 text-[10.5px] leading-relaxed">
  <strong class="text-red-900 font-bold block mb-1">4 Nút Thắt Nghiêm Trọng (Critical Bottlenecks)</strong>
  <ul class="space-y-1.5 mt-2">
    <li class="flex items-start gap-1.5">
      <span><strong>Vi phạm bản quyền:</strong> DRM bằng 0, sách bị phát tán tự do qua Google Drive công khai.</span>
    </li>
    <li class="flex items-start gap-1.5">
      <span><strong>Trải nghiệm mỏi mắt:</strong> Dạng PDF ảnh cố định kích thước, sinh viên phải zoom thủ công trên thiết bị di động.</span>
    </li>
    <li class="flex items-start gap-1.5">
      <span><strong>Mất khả năng tra cứu:</strong> Không thể tìm kiếm từ khóa nội dung; phải đọc quét toàn trang để tìm thông tin.</span>
    </li>
    <li class="flex items-start gap-1.5">
      <span><strong>Metadata rời rạc:</strong> Thủ thư chỉ nhập tên file, không có chuẩn Dublin Core thống nhất, hệ thống không phân loại được thể loại sách tự động.</span>
    </li>
  </ul>
</div>

---

# Quy Trình Tương Lai (To-Be): Số Hóa Khép Kín Có AI Hỗ Trợ

<div class="grid grid-cols-2 gap-4 mt-3 text-xs">
  <div class="p-4 rounded-xl bg-slate-50 border border-slate-200 shadow-sm">
    <h3 class="text-emerald-900 font-bold text-sm mb-3 border-b border-slate-200 pb-2">Quy Trình Từng Bước Đơn Giản</h3>
    <ol class="list-decimal pl-4 space-y-1.5 text-slate-700">
      <li><strong>Quét sách giấy:</strong> Thủ thư dùng máy quét chữ V (không tháo gáy) để chụp trang giáo trình.</li>
      <li><strong>Điền metadata:</strong> Thủ thư nhập tiêu đề, tác giả, vị trí kệ (Dublin Core rút gọn).</li>
      <li><strong>AI OCR tự động:</strong> FastAPI BackgroundTasks gọi Tesseract dịch ảnh → văn bản thô theo trang.</li>
      <li><strong>Sửa lỗi Split-screen:</strong> Biên tập viên đối chiếu ảnh gốc/text song song, sửa lỗi cực nhanh.</li>
      <li><strong>Đóng gói EPUB:</strong> Thủ thư duyệt chất lượng rồi bấm nút; Pandoc tự sinh EPUB 3.0.</li>
      <li><strong>Đọc sách bảo mật:</strong> Sinh viên đọc mượt trên di động qua Signed URL, khóa tải/copy.</li>
    </ol>
  </div>
  <div class="space-y-3">
    <div class="p-4 bg-emerald-50/80 rounded-xl border border-emerald-200 shadow-sm h-[135px]">
      <strong class="text-emerald-900 text-sm block mb-1">Cán Bộ Thư Viện (Thủ Thư)</strong>
      <p class="text-slate-700 leading-relaxed">Chịu trách nhiệm quét sách, nhập metadata cơ bản và bấm nút duyệt cuối cùng để xuất bản sách lên ứng dụng đọc trực tuyến.</p>
    </div>
    <div class="p-4 bg-blue-50/80 rounded-xl border border-blue-200 shadow-sm h-[135px]">
      <strong class="text-blue-900 text-sm block mb-1">Cộng Tác Viên (Sinh Viên) & AI</strong>
      <p class="text-slate-700 leading-relaxed">AI tự động dịch ảnh thành chữ. Sinh viên CTV chỉ tập trung rà soát/chỉnh sửa lỗi chính tả thô trước khi gửi phê duyệt.</p>
    </div>
  </div>
</div>

---

# So Sánh: Quy Trình Đề Xuất vs Quy Trình Thủ Công (As-Is)

<div class="grid grid-cols-2 gap-4 mt-3 text-[11px]">

<div class="p-4 rounded-xl bg-red-50/60 border border-red-200 shadow-sm space-y-2">
  <strong class="text-red-900 text-xs block border-b border-red-200 pb-1">Quy Trình Thủ Công 100% (As-Is)</strong>
  <ul class="space-y-1.5 text-slate-700 list-disc pl-4">
    <li>Quét bằng máy photocopy văn phòng, đặt tên file tùy tiện, không metadata chuẩn.</li>
    <li>Không có bước OCR — giữ nguyên ảnh quét tĩnh, không thể tìm kiếm nội dung.</li>
    <li>Phân phối qua link Drive chia sẻ trực tiếp — không kiểm soát được điểm đến tệp.</li>
    <li>Tốc độ số hóa rất chậm (~3 giờ/cuốn), nỗ lực vận hành 100% thủ công.</li>
  </ul>
</div>

<div class="p-4 rounded-xl bg-emerald-50/60 border border-emerald-200 shadow-sm space-y-2">
  <strong class="text-emerald-900 text-xs block border-b border-emerald-200 pb-1">Quy Trình Đề Xuất (HCMUS-LDMS)</strong>
  <ul class="space-y-1.5 text-slate-700 list-disc pl-4">
    <li>Máy scan chữ V + đẩy file tự động, nhập Dublin Core rút gọn trực tiếp trên hệ thống.</li>
    <li>OCR Tesseract chạy nền (BackgroundTasks), sinh văn bản có thể tra cứu toàn văn.</li>
    <li>MinIO Signed URL hết hạn 15 phút, chặn Ctrl+C/Ctrl+P, không hiện nút Download.</li>
    <li>Tốc độ ~30 phút/cuốn qua web, nỗ lực vận hành rất thấp nhờ tự động hóa.</li>
  </ul>
</div>

</div>

<div class="mt-3 p-3 rounded-xl bg-slate-100 text-slate-900 text-[10.5px] leading-relaxed">
  <strong class="text-emerald-900 font-bold block mb-1">Kết luận</strong>
  <ul class="space-y-1.5 mt-2">
    <li class="flex items-start gap-1.5">
      <span><strong>Triệt tiêu 4 nút thắt:</strong> Quy trình đề xuất xử lý được vấn đề bản quyền, trải nghiệm đọc, tra cứu nội dung và metadata rời rạc.</span>
    </li>
    <li class="flex items-start gap-1.5">
      <span><strong>Giảm thời gian:</strong> Thời gian số hóa giảm từ ~3 giờ xuống ~30 phút/cuốn nhờ tự động hóa.</span>
    </li>
  </ul>
</div>

---

# So Sánh: Quy Trình Đề Xuất vs Đối Thủ Cạnh Tranh

<div class="grid grid-cols-2 gap-4 mt-3 text-[11px]">

<div class="p-4 rounded-xl bg-amber-50/60 border border-amber-200 shadow-sm space-y-2">
  <strong class="text-amber-900 text-xs block border-b border-amber-200 pb-1">Giải Pháp Thương Mại (Lạc Việt Vebrary / DSpace)</strong>
  <ul class="space-y-1.5 text-slate-700 list-disc pl-4">
    <li>Chi phí triển khai lớn — vượt ngân sách trần 100 triệu VNĐ của dự án.</li>
    <li>Khó tùy biến theo quy trình nghiệp vụ đặc thù của thư viện trường.</li>
    <li>Không tích hợp sẵn cơ chế soát lỗi OCR tiếng Việt kiểu Split-screen.</li>
    <li>Tìm kiếm cơ bản hoặc cần hạ tầng Elasticsearch đắt đỏ để đạt tốc độ tốt.</li>
    <li>Thường phân phối cả file PDF/EPUB gốc → dễ bị cào dữ liệu qua API.</li>
  </ul>
</div>

<div class="p-4 rounded-xl bg-emerald-50/60 border border-emerald-200 shadow-sm space-y-2">
  <strong class="text-emerald-900 text-xs block border-b border-emerald-200 pb-1">Quy Trình Đề Xuất (HCMUS-LDMS)</strong>
  <ul class="space-y-1.5 text-slate-700 list-disc pl-4">
    <li>Chi phí CapEx 75–95 triệu + OpEx 15–30 triệu/năm, nằm trong trần ngân sách.</li>
    <li>Tự phát triển (React + FastAPI), tùy biến hoàn toàn theo quy trình thư viện HCMUS.</li>
    <li>Split-screen Editor chuyên biệt cho soát lỗi OCR tiếng Việt.</li>
    <li>PostgreSQL FTS &lt; 3 giây, không cần hạ tầng search rời riêng biệt.</li>
    <li>Không expose file gốc — chỉ Signed URL 15 phút, chặn thao tác tải/copy.</li>
  </ul>
</div>

</div>

<div class="mt-3 p-3 rounded-xl bg-slate-100 text-slate-900 text-[10.5px] leading-relaxed">
  <strong class="text-amber-900 font-bold block mb-1">Kết luận</strong>
  <ul class="space-y-1.5 mt-2">
    <li class="flex items-start gap-1.5">
      <span>Đối thủ thương mại vượt ngân sách và thiếu khả năng tùy biến nghiệp vụ đặc thù; giải pháp tự phát triển đánh đổi thời gian đội ngũ để đạt chi phí thấp hơn và độ khớp nghiệp vụ cao hơn.</span>
    </li>
    <li class="flex items-start gap-1.5">
      <span class="text-slate-500"><em>* Số liệu chi phí/tính năng đối thủ trong tài liệu nguồn chỉ ở mức định tính — xem mục "Khoảng trống tài liệu" cuối phần.</em></span>
    </li>
  </ul>
</div>

---

# So Sánh: Quy Trình Đề Xuất vs Kết Hợp Công Cụ Có Sẵn Thủ Công

<div class="grid grid-cols-2 gap-4 mt-3 text-[11px]">

<div class="p-4 rounded-xl bg-blue-50/60 border border-blue-200 shadow-sm space-y-2">
  <strong class="text-blue-900 text-xs block border-b border-blue-200 pb-1">Kết Hợp Công Cụ Rời Rạc (Abbyy FineReader + Google Drive)</strong>
  <ul class="space-y-1.5 text-slate-700 list-disc pl-4">
    <li>Scan máy văn phòng → upload thủ công lên Drive, không hỗ trợ Dublin Core.</li>
    <li>Chạy OCR offline bằng Abbyy → xuất text → soát lỗi thủ công trên Word.</li>
    <li>Convert sang EPUB thủ công bằng Calibre — dễ lỗi font, vỡ ảnh.</li>
    <li>Tìm theo tên tệp trên Drive — không tìm được nội dung bên trong sách.</li>
    <li>Drive không chặn tải tệp gốc, dễ bị sinh viên copy và phát tán link công khai.</li>
    <li>Tốn 2–3 giờ/cuốn, các bước gửi email rời rạc giữa nhiều người.</li>
  </ul>
</div>

<div class="p-4 rounded-xl bg-emerald-50/60 border border-emerald-200 shadow-sm space-y-2">
  <strong class="text-emerald-900 text-xs block border-b border-emerald-200 pb-1">Quy Trình Đề Xuất (HCMUS-LDMS)</strong>
  <ul class="space-y-1.5 text-slate-700 list-disc pl-4">
    <li>Đẩy file tự động sau khi scan, nhập Dublin Core nhanh ngay trên hệ thống.</li>
    <li>OCR chạy nền tự động (Tesseract qua BackgroundTasks), không cần phần mềm rời.</li>
    <li>Pandoc tự động biên dịch EPUB 3.0 reflowable chỉ bằng 1 nút nhấn.</li>
    <li>PostgreSQL FTS tìm nội dung toàn văn trực tiếp trong database.</li>
    <li>MinIO Signed URL (15 phút) + chặn chuột phải, Ctrl+C/Ctrl+P.</li>
    <li>Một quy trình khép kín trong 1 hệ thống, không cần chuyển đổi qua email/nhiều phần mềm.</li>
  </ul>
</div>

</div>

<div class="mt-3 p-3 rounded-xl bg-slate-100 text-slate-900 text-[10.5px] leading-relaxed">
  <strong class="text-slate-900">Kết luận:</strong> Ghép nối công cụ rời rạc vẫn tốn nỗ lực vận hành "rất cao" tương đương thủ công thuần túy, chỉ khác là có thêm bước OCR offline — không giải quyết được rủi ro DRM và tính rời rạc quy trình.
</div>

---

# Bảng Tổng Hợp Đối Chuẩn 4 Phương Án (Workflow Benchmarking)

<table class="w-full text-left border-collapse text-[6.3px] mt-2 leading-tight">
  <thead>
    <tr class="bg-slate-900 text-white font-bold">
      <th class="p-1 border border-slate-700">Tiêu chí đối chiếu</th>
      <th class="p-1 border border-slate-700">Thủ công (As-Is)</th>
      <th class="p-1 border border-slate-700">Kết hợp công cụ<br>(Abbyy + Drive)</th>
      <th class="p-1 border border-slate-700">Đối thủ thương mại<br>(Lạc Việt/DSpace)</th>
      <th class="p-1 border border-slate-700 bg-emerald-800 text-emerald-50">Đề xuất<br>(HCMUS-LDMS)</th>
    </tr>
  </thead>
  <tbody>
    <tr class="bg-white">
      <td class="p-1 border border-slate-200 font-bold">Quét & Metadata</td>
      <td class="p-1 border border-slate-200 text-red-600">Photocopy thô, đặt tên tùy tiện, không metadata</td>
      <td class="p-1 border border-slate-200 text-amber-600">Scan VP → upload thủ công, không Dublin Core</td>
      <td class="p-1 border border-slate-200 text-slate-600">Nhập metadata trên module quản trị cồng kềnh</td>
      <td class="p-1 border border-slate-200 font-bold bg-emerald-50 text-emerald-800">Máy chữ V → đẩy tự động → Dublin Core nhanh</td>
    </tr>
    <tr class="bg-slate-50">
      <td class="p-1 border border-slate-200 font-bold">OCR & Soát lỗi</td>
      <td class="p-1 border border-slate-200 text-red-600">Không có (giữ ảnh tĩnh)</td>
      <td class="p-1 border border-slate-200 text-amber-600">Abbyy offline → soát lỗi trên Word thủ công</td>
      <td class="p-1 border border-slate-200 text-slate-600">Không tích hợp OCR tiếng Việt chuyên sâu</td>
      <td class="p-1 border border-slate-200 font-bold bg-emerald-50 text-emerald-800">Tesseract nền + Split-screen Workspace</td>
    </tr>
    <tr class="bg-white">
      <td class="p-1 border border-slate-200 font-bold">Đóng gói đầu ra</td>
      <td class="p-1 border border-slate-200 text-red-600">PDF ảnh tĩnh, không co giãn</td>
      <td class="p-1 border border-slate-200 text-amber-600">Calibre thủ công, dễ lỗi font/ảnh</td>
      <td class="p-1 border border-slate-200 text-slate-600">PDF/EPUB tĩnh, không tối ưu hiển thị</td>
      <td class="p-1 border border-slate-200 font-bold bg-emerald-50 text-emerald-800">Pandoc → EPUB 3.0 reflowable, 1 nút nhấn</td>
    </tr>
    <tr class="bg-slate-50">
      <td class="p-1 border border-slate-200 font-bold">Tìm kiếm</td>
      <td class="p-1 border border-slate-200 text-red-600">Không hỗ trợ (tra kệ vật lý)</td>
      <td class="p-1 border border-slate-200 text-red-600">Theo tên tệp, không nội dung</td>
      <td class="p-1 border border-slate-200 text-slate-600">Cơ bản hoặc ES (đắt đỏ)</td>
      <td class="p-1 border border-slate-200 font-bold bg-emerald-50 text-emerald-800">PostgreSQL FTS toàn văn &lt; 3s</td>
    </tr>
    <tr class="bg-white">
      <td class="p-1 border border-slate-200 font-bold">Bảo mật DRM</td>
      <td class="p-1 border border-slate-200 text-red-600">Không có</td>
      <td class="p-1 border border-slate-200 text-red-600">Drive không chặn tải, dễ lộ link</td>
      <td class="p-1 border border-slate-200 text-slate-600">Chặn copy cơ bản, vẫn phân phối file gốc</td>
      <td class="p-1 border border-slate-200 font-bold bg-emerald-50 text-emerald-800">Signed URL 15m + chặn Copy/Print</td>
    </tr>
    <tr class="bg-slate-50">
      <td class="p-1 border border-slate-200 font-bold">Nỗ lực vận hành</td>
      <td class="p-1 border border-slate-200 text-red-600">Rất cao (~3h/cuốn)</td>
      <td class="p-1 border border-slate-200 text-amber-600">Rất cao (2-3h/cuốn, rời rạc)</td>
      <td class="p-1 border border-slate-200 text-slate-600">Trung bình</td>
      <td class="p-1 border border-slate-200 font-bold bg-emerald-50 text-emerald-800">Rất thấp (~30p/cuốn, tự động hóa)</td>
    </tr>
  </tbody>
</table>

<div class="mt-2 text-[9px] text-slate-500 leading-normal border-t border-slate-200 pt-1.5">
  • <strong>DRM (Digital Rights Management):</strong> Quản lý bản quyền số, ngăn chặn tải lậu sách gốc. • <strong>FTS (Full-Text Search):</strong> Tìm kiếm toàn văn trong nội dung sách.
</div>

---

# Chân Dung Các Bên Liên Quan & Người Dùng

<div class="grid grid-cols-2 gap-4 mt-4 text-xs">

<div class="p-4 rounded-xl bg-slate-50 border border-slate-200 shadow-sm space-y-2">
  <strong class="text-emerald-900 text-sm block border-b border-slate-200 pb-1">Nhóm Quản Trị & Ban Dự Án</strong>
  <ul class="space-y-1.5 text-slate-700">
    <li><strong>Nhà Tài Trợ:</strong> Ban Giám hiệu HCMUS — phê duyệt ngân sách CapEx/OpEx & quy chế thư viện số.</li>
    <li><strong>Bên Thụ Hưởng Nghiệp Vụ:</strong> Ban Giám đốc Thư viện — chất lượng số hóa & kiểm soát bản quyền.</li>
    <li><strong>Bên Thụ Hưởng Kỹ Thuật:</strong> Phòng CNTT — hạ tầng ảo hóa VMware & an toàn thông tin.</li>
  </ul>
</div>

<div class="p-4 rounded-xl bg-slate-50 border border-slate-200 shadow-sm space-y-2">
  <strong class="text-emerald-900 text-sm block border-b border-slate-200 pb-1">Nhóm Trực Tiếp Thao Tác (Người Dùng Cuối)</strong>
  <ul class="space-y-1.5 text-slate-700">
    <li><strong>Độc giả (SV/GV):</strong> Truy cập di động đọc sách trực tuyến 24/7 từ xa.</li>
    <li><strong>Thủ thư / Biên tập viên:</strong> Quét sách, kiểm duyệt OCR & soát lỗi văn bản.</li>
    <li><strong>Quản trị viên hệ thống:</strong> Quản lý danh mục, phân quyền tài khoản & giám sát server.</li>
  </ul>
</div>

</div>

---

# Phân Tích Trách Nhiệm: Ma Trận RACI Theo Gói Công Việc

<table class="w-full text-left border-collapse text-[7.5px] mt-2 leading-tight">
  <thead>
    <tr class="bg-slate-900 text-white font-bold">
      <th class="p-1 border border-slate-700">Gói công việc (WBS)</th>
      <th class="p-1 border border-slate-700">Thư viện</th>
      <th class="p-1 border border-slate-700">Phòng CNTT</th>
      <th class="p-1 border border-slate-700">Giáo vụ Khoa</th>
      <th class="p-1 border border-slate-700">Pháp chế</th>
      <th class="p-1 border border-slate-700">Ban Giám hiệu</th>
      <th class="p-1 border border-slate-700">Độc giả</th>
    </tr>
  </thead>
  <tbody>
    <tr class="bg-white"><td class="p-1 border border-slate-200 font-bold">WP1 — Khảo sát & Bản quyền</td><td class="p-1 border border-slate-200 font-bold text-emerald-700">A / R</td><td class="p-1 border border-slate-200">R</td><td class="p-1 border border-slate-200">C</td><td class="p-1 border border-slate-200">C</td><td class="p-1 border border-slate-200">I</td><td class="p-1 border border-slate-200">–</td></tr>
    <tr class="bg-slate-50"><td class="p-1 border border-slate-200 font-bold">WP2 — Hạ tầng Backend & DB</td><td class="p-1 border border-slate-200">C</td><td class="p-1 border border-slate-200 font-bold text-emerald-700">A / R</td><td class="p-1 border border-slate-200">–</td><td class="p-1 border border-slate-200">–</td><td class="p-1 border border-slate-200">I</td><td class="p-1 border border-slate-200">–</td></tr>
    <tr class="bg-white"><td class="p-1 border border-slate-200 font-bold">WP3 — Giao diện & OCR/EPUB</td><td class="p-1 border border-slate-200">C</td><td class="p-1 border border-slate-200 font-bold text-emerald-700">A / R</td><td class="p-1 border border-slate-200">–</td><td class="p-1 border border-slate-200">–</td><td class="p-1 border border-slate-200">I</td><td class="p-1 border border-slate-200">C</td></tr>
    <tr class="bg-slate-50"><td class="p-1 border border-slate-200 font-bold">WP4 — Số hóa 500 tài liệu</td><td class="p-1 border border-slate-200 font-bold text-emerald-700">A / R</td><td class="p-1 border border-slate-200">C</td><td class="p-1 border border-slate-200">C</td><td class="p-1 border border-slate-200">C</td><td class="p-1 border border-slate-200">I</td><td class="p-1 border border-slate-200">–</td></tr>
    <tr class="bg-white"><td class="p-1 border border-slate-200 font-bold">WP5 — Kiểm thử & UAT</td><td class="p-1 border border-slate-200">R</td><td class="p-1 border border-slate-200 font-bold text-emerald-700">A / R</td><td class="p-1 border border-slate-200">–</td><td class="p-1 border border-slate-200">–</td><td class="p-1 border border-slate-200">I</td><td class="p-1 border border-slate-200">C</td></tr>
    <tr class="bg-slate-50"><td class="p-1 border border-slate-200 font-bold">WP6 — Triển khai & Vận hành</td><td class="p-1 border border-slate-200 font-bold text-emerald-700">A / R</td><td class="p-1 border border-slate-200">R</td><td class="p-1 border border-slate-200">C</td><td class="p-1 border border-slate-200">–</td><td class="p-1 border border-slate-200">I</td><td class="p-1 border border-slate-200">I</td></tr>
  </tbody>
</table>

<div class="mt-2 text-[9px] text-slate-500 leading-normal border-t border-slate-200 pt-1">
  <strong>WP (Work Package):</strong> gói công việc chính trong cơ cấu phân rã công việc (Work Breakdown Structure).
  <br>
  <strong>R (Responsible):</strong> Bộ phận thực hiện. <br>
  <strong>A (Accountable):</strong> Bộ phận chịu trách nhiệm giải trình cuối cùng (chỉ 1 chủ thể / gói). <br>
  <strong>C (Consulted):</strong> Được tham vấn. <br>
  <strong>I (Informed):</strong> Được thông báo. 
</div>

---

# Ma Trận Quyền Lực – Quan Tâm – Khả Năng Tiếp Cận – Ảnh Hưởng

<table class="w-full text-left border-collapse text-[8px] mt-2 leading-tight">
  <thead>
    <tr class="bg-slate-900 text-white font-bold">
      <th class="p-1 border border-slate-700">Bên liên quan</th>
      <th class="p-1 border border-slate-700">Quyền lực (Power)</th>
      <th class="p-1 border border-slate-700">Mức quan tâm (Interest)</th>
      <th class="p-1 border border-slate-700">Khả năng tiếp cận (Access)</th>
      <th class="p-1 border border-slate-700">Mức độ ảnh hưởng lên dự án</th>
    </tr>
  </thead>
  <tbody>
    <tr class="bg-white"><td class="p-1 border border-slate-200 font-bold">Ban Giám hiệu</td><td class="p-1 border border-slate-200 text-emerald-700 font-bold">Cao</td><td class="p-1 border border-slate-200">Trung bình</td><td class="p-1 border border-slate-200">Thấp — chỉ qua báo cáo Gating định kỳ</td><td class="p-1 border border-slate-200">Rất cao — duyệt ngân sách & phạm vi &gt;5%</td></tr>
    <tr class="bg-slate-50"><td class="p-1 border border-slate-200 font-bold">Ban GĐ Thư viện</td><td class="p-1 border border-slate-200 text-emerald-700 font-bold">Cao</td><td class="p-1 border border-slate-200 text-emerald-700 font-bold">Cao</td><td class="p-1 border border-slate-200">Cao — họp Weekly Review trực tiếp</td><td class="p-1 border border-slate-200">Rất cao — Accountable WP1, WP4, WP6</td></tr>
    <tr class="bg-white"><td class="p-1 border border-slate-200 font-bold">Phòng CNTT (PM)</td><td class="p-1 border border-slate-200 text-emerald-700 font-bold">Cao</td><td class="p-1 border border-slate-200 text-emerald-700 font-bold">Cao</td><td class="p-1 border border-slate-200">Rất cao — Daily Standup hàng ngày</td><td class="p-1 border border-slate-200">Rất cao — Accountable WP2, WP3, WP5</td></tr>
    <tr class="bg-slate-50"><td class="p-1 border border-slate-200 font-bold">Bộ phận Pháp chế</td><td class="p-1 border border-slate-200 text-emerald-700 font-bold">Cao</td><td class="p-1 border border-slate-200">Trung bình</td><td class="p-1 border border-slate-200">Thấp — chỉ tham vấn theo yêu cầu (C)</td><td class="p-1 border border-slate-200">Trung bình — rủi ro pháp lý SHTT</td></tr>
    <tr class="bg-white"><td class="p-1 border border-slate-200 font-bold">Giảng viên</td><td class="p-1 border border-slate-200">Thấp</td><td class="p-1 border border-slate-200 text-emerald-700 font-bold">Cao</td><td class="p-1 border border-slate-200">Trung bình — khảo sát & UAT định kỳ</td><td class="p-1 border border-slate-200">Trung bình — cung cấp/consent bản quyền giáo trình</td></tr>
    <tr class="bg-slate-50"><td class="p-1 border border-slate-200 font-bold">Sinh viên (Độc giả)</td><td class="p-1 border border-slate-200">Thấp</td><td class="p-1 border border-slate-200 text-emerald-700 font-bold">Cao</td><td class="p-1 border border-slate-200">Cao — kênh CTV/khảo sát trực tiếp</td><td class="p-1 border border-slate-200">Thấp — phản hồi UAT, không quyết định phạm vi</td></tr>
    <tr class="bg-white"><td class="p-1 border border-slate-200 font-bold">Thủ thư / BTV</td><td class="p-1 border border-slate-200">Trung bình</td><td class="p-1 border border-slate-200 text-emerald-700 font-bold">Cao</td><td class="p-1 border border-slate-200">Rất cao — người vận hành trực tiếp hệ thống</td><td class="p-1 border border-slate-200">Cao — Responsible WP1/WP4, kiểm duyệt xuất bản</td></tr>
  </tbody>
</table>

<div class="mt-2 text-[9px] text-slate-500 leading-normal border-t border-slate-200 pt-1">
  Chiến lược ứng xử: Power cao/Interest cao → <em>quản trị sát sao</em>; Power cao/Interest vừa → <em>giữ hài lòng</em>; Power thấp/Interest cao → <em>thông báo đầy đủ</em>. Cột "Khả năng tiếp cận" và cột cuối là nội dung <strong>bổ sung</strong> — xem mục Khoảng trống tài liệu.
</div>

---

# Phân Tích Tác Động Quy Trình Cũ và Mới Theo Vai Trò

| Vai Trò                 | Trạng Thái Hiện Tại (As-Is)                                 | Trạng Thái Tương Lai (To-Be)                                          |
| :---------------------- | :---------------------------------------------------------- | :-------------------------------------------------------------------- |
| **Độc Giả (Sinh Viên)** | Di chuyển 15km, chép tay thủ công, đọc PDF mỏi mắt.         | Đọc trực tuyến tương thích 24/7 trên smartphone, FTS < 3s.            |
| **Thủ Thư**             | Kho quá tải, tốn phần lớn thời gian tìm và ghi sổ thủ công. | Tự động hóa kiểm kê, quản lý file sách tập trung.                     |
| **Biên Tập Viên / CTV** | Sửa lỗi thủ công rời rạc trên nhiều file Word/PDF.          | Giao diện Split-screen soát lỗi nhanh (+60% năng suất).               |
| **Ban Giám Hiệu**       | Lo lắng rò rỉ bản quyền & kho bãi vật lý quá tải.           | Đạt mốc Đại học số ĐHQG-HCM, bảo mật DRM tuyệt đối.                   |
| **Ban GĐ Thư viện**     | Tốn chi phí bảo quản, ngại chia sẻ vì sợ vi phạm bản quyền. | Thu hồi phần lớn mặt bằng kho kệ; kiểm soát bản quyền qua Signed URL. |

---

# Phạm Vi Sản Phẩm: Tính Năng Cốt Lõi vs Mở Rộng

<div class="grid grid-cols-2 gap-4 mt-4 text-xs">

<div class="p-4 bg-emerald-50/80 rounded-xl border border-emerald-200 shadow-sm space-y-2">
  <div class="flex items-center justify-between border-b border-emerald-200 pb-1">
    <strong class="text-emerald-900 text-sm">Phạm Vi Khả Thi Tối Giản (MVP)</strong>
    <span class="badge bg-emerald-700 text-white text-[10px] px-2 py-0.5 font-bold rounded">16 Must + 7 Should</span>
  </div>
  <ul class="space-y-1 text-slate-700 list-disc pl-4">
    <li>Đăng nhập tài khoản trường Google OAuth 2.0 / Mock Auth.</li>
    <li>Tải tài liệu & quy trình OCR Tesseract bất đồng bộ.</li>
    <li>Giao diện chia đôi màn hình biên tập text/ảnh (Split-screen).</li>
    <li>Đóng gói định dạng EPUB 3.0 co giãn dòng (Pandoc).</li>
    <li>Tìm kiếm toàn văn PostgreSQL FTS < 3 giây.</li>
    <li>Trình đọc Web Reader bảo mật Signed URL 15m (chặn Copy).</li>
  </ul>
</div>

<div class="p-4 bg-slate-50 rounded-xl border border-slate-200 shadow-sm space-y-2">
  <div class="flex items-center justify-between border-b border-slate-200 pb-1">
    <strong class="text-slate-900 text-sm">Phạm Vi Có Thể Có / Loại Trừ</strong>
    <span class="badge bg-slate-400 text-white text-[10px] px-2 py-0.5 font-bold rounded">3 Could + Loại trừ</span>
  </div>
  <ul class="space-y-1 text-slate-700 list-disc pl-4">
    <li>Tags, Highlight/ghi chú, trích dẫn tự động APA/IEEE (Could-have).</li>
    <li>Tìm kiếm Elasticsearch nâng cao khi FTS không còn đủ tải (Could-have).</li>
    <li>Loại trừ: Tích hợp chống đạo văn Turnitin, AI RAG hỏi đáp nội dung sách.</li>
    <li>Loại trừ: Số hóa tài liệu hành chính trường, thanh lý sách giấy cũ.</li>
  </ul>
</div>

</div>

---

# Yêu Cầu Phi Chức Năng Trọng Yếu

<div class="grid grid-cols-3 gap-4 mt-4 text-xs">

<div class="p-4 rounded-xl bg-slate-50 border border-slate-200 shadow-sm">
  <strong class="text-emerald-900 text-sm block mb-1">Hiệu Năng</strong>
  <p class="text-slate-700">Tìm kiếm toàn văn < 3s cho 500 người dùng đồng thời. Trình đọc web tải trang < 2s.</p>
</div>

<div class="p-4 rounded-xl bg-slate-50 border border-slate-200 shadow-sm">
  <strong class="text-emerald-900 text-sm block mb-1">Bảo Mật</strong>
  <p class="text-slate-700">Đăng nhập tài khoản trường, đường dẫn bảo mật tự hủy 15m, 0 sự cố rò lọt tệp gốc.</p>
</div>

<div class="p-4 rounded-xl bg-slate-50 border border-slate-200 shadow-sm">
  <strong class="text-emerald-900 text-sm block mb-1">Độ Tin Cậy</strong>
  <p class="text-slate-700">Sao lưu tự động 01:00 hàng ngày, RPO < 24h, retry OCR tối đa 3 lần.</p>
</div>

</div>

<div class="grid grid-cols-2 gap-4 mt-4 text-xs">

<div class="p-3 bg-slate-50 rounded-lg border border-slate-200 text-slate-700">
  <strong>Giao Diện & Tương Thích:</strong> Responsive co giãn 100% từ 320px di động đến 2560px desktop, Accessibility Score ≥ 90 (Lighthouse).
</div>

<div class="p-3 bg-slate-50 rounded-lg border border-slate-200 text-slate-700">
  <strong>Pháp Lý & Ngân Sách:</strong> Tuân thủ Luật Sở hữu trí tuệ Việt Nam. Tổng ngân sách CapEx+OpEx năm đầu < 100 Triệu VNĐ.
</div>

</div>

---

# Quy Tắc Vận Hành Yêu Cầu: Kanban & DoD

<div class="grid grid-cols-3 gap-4 mt-4 text-xs">

<div class="p-4 rounded-xl bg-slate-50 border border-slate-200 shadow-sm">
  <strong class="text-emerald-900 text-sm block mb-2">Nguyên Tắc Bảng Kanban</strong>
  <ul class="space-y-1.5 text-slate-700">
    <li>Giới hạn công việc đang làm = 1 yêu cầu/người (tránh phân tán).</li>
    <li>Đo lường năng suất thực tế (throughput = số yêu cầu Done/tuần).</li>
    <li>Không dùng điểm ước lượng (Story Point) để ép tiến độ.</li>
  </ul>
</div>

<div class="p-4 rounded-xl bg-slate-50 border border-slate-200 shadow-sm">
  <strong class="text-emerald-900 text-sm block mb-2">Định Nghĩa Hoàn Thành (DoD)</strong>
  <ul class="space-y-1.5 text-slate-700">
    <li>Vượt qua 100% các Tiêu Chí Chấp Nhận (AC) của card.</li>
    <li>Mã nguồn được duyệt qua Pull Request và chạy ổn định trên local.</li>
    <li>Cập nhật README module và ghi log effort/token AI.</li>
  </ul>
</div>

<div class="p-4 rounded-xl bg-slate-50 border border-slate-200 shadow-sm">
  <strong class="text-emerald-900 text-sm block mb-2">Phân Bổ Mức Độ Ưu Tiên (26 Yêu Cầu)</strong>
  <ul class="space-y-1.5 text-slate-700">
    <li><strong>Bắt buộc có (Must-have):</strong> 16 yêu cầu (Cốt lõi MVP)</li>
    <li><strong>Nên có (Should-have):</strong> 7 yêu cầu (Trải nghiệm tốt)</li>
    <li><strong>Có thể có (Could-have):</strong> 3 yêu cầu (Mở rộng)</li>
  </ul>
</div>

</div>

---

# Phân Tích Tiêu Chí Chấp Nhận: Tổng Quan Toàn Bộ Backlog

<table class="w-full text-left border-collapse text-[8px] mt-2 leading-tight">
  <thead>
    <tr class="bg-slate-900 text-white font-bold">
      <th class="p-1 border border-slate-700">Epic</th>
      <th class="p-1 border border-slate-700">Số Story</th>
      <th class="p-1 border border-slate-700">Số AC (tổng)</th>
      <th class="p-1 border border-slate-700">Loại AC bao phủ chủ yếu</th>
    </tr>
  </thead>
  <tbody>
    <tr class="bg-white"><td class="p-1 border border-slate-200 font-bold">D — Nền tảng (Platform)</td><td class="p-1 border border-slate-200">1</td><td class="p-1 border border-slate-200">4</td><td class="p-1 border border-slate-200">Health-check, cấu hình env, thông báo lỗi rõ ràng khi thiếu biến bắt buộc.</td></tr>
    <tr class="bg-slate-50"><td class="p-1 border border-slate-200 font-bold">A — Xác thực & Phân quyền</td><td class="p-1 border border-slate-200">3</td><td class="p-1 border border-slate-200">11</td><td class="p-1 border border-slate-200">Cấp/kiểm token theo role, chặn truy cập không hợp lệ, không hardcode secret.</td></tr>
    <tr class="bg-white"><td class="p-1 border border-slate-200 font-bold">B — Số hóa & Xuất bản</td><td class="p-1 border border-slate-200">13</td><td class="p-1 border border-slate-200">47</td><td class="p-1 border border-slate-200">Luồng upload → OCR → sửa lỗi → publish; chặn publish thiếu metadata/content.</td></tr>
    <tr class="bg-slate-50"><td class="p-1 border border-slate-200 font-bold">C — Tra cứu & Đọc sách</td><td class="p-1 border border-slate-200">9</td><td class="p-1 border border-slate-200">27</td><td class="p-1 border border-slate-200">Render EPUB, snippet tìm kiếm, Signed URL hết hạn, cá nhân hóa reader theo user.</td></tr>
    <tr class="bg-white font-bold"><td class="p-1 border border-slate-200">Tổng cộng</td><td class="p-1 border border-slate-200">26</td><td class="p-1 border border-slate-200">~89 AC</td><td class="p-1 border border-slate-200">100% story có AC kiểm tra được (verify được), theo DoD chung.</td></tr>
  </tbody>
</table>

<div class="mt-2 text-[9px] text-slate-500 leading-normal border-t border-slate-200 pt-1">
  Mọi AC đều theo nguyên tắc: quan sát/verify được qua API hoặc UI, có kịch bản lỗi (edge-case) đi kèm kịch bản thành công. Nguồn: Product Backlog v4.0 §2.
</div>

---

# Phân Tích AC Chi Tiết: LDMS-002 (Tải Tệp Scan Gốc)

<div class="p-5 rounded-xl bg-slate-50 border border-slate-200 shadow-sm text-xs space-y-3 mt-2">

<div class="flex items-center justify-between border-b border-slate-200 pb-2">
  <span class="font-bold text-emerald-900 text-sm">LDMS-002: Tải Lên Tệp Scan Gốc</span>
  <div class="flex gap-2">
    <span class="badge bg-emerald-700 text-white text-[10px] px-2 py-0.5 rounded font-bold">Bắt Buộc Có</span>
    <span class="badge bg-slate-200 text-slate-800 text-[10px] px-2 py-0.5 rounded font-bold">Kích Thước M</span>
  </div>
</div>

<p class="text-slate-700 italic">"Là thủ thư, tôi muốn tải lên tệp PDF hoặc ảnh scan sách giấy gốc để hệ thống bắt đầu xử lý luồng số hóa."</p>

<div class="space-y-1.5 text-slate-800">
  <strong class="text-emerald-900 block">Tiêu Chí Chấp Nhận (AC):</strong>
  <p><strong>AC1:</strong> Upload file <code>.pdf</code>/<code>.jpg</code>/<code>.png</code> hợp lệ → trả về <code>document_id</code> thành công.</p>
  <p><strong>AC2:</strong> Upload định dạng không hỗ trợ (<code>.exe</code>, <code>.docx</code>) → trả lỗi rõ ràng, không tạo document (kịch bản biên/negative test).</p>
  <p><strong>AC3:</strong> <code>GET /documents/{id}</code> trả đủ <code>id</code>, <code>original_filename</code>, <code>status</code>, <code>created_at</code>.</p>
  <p><strong>AC4:</strong> File lưu trên MinIO, đọc lại được bytes theo <code>document_id</code> (kiểm tra tính toàn vẹn lưu trữ).</p>
  <p><strong>AC5:</strong> <code>GET</code> với id không tồn tại → trả lỗi "không tìm thấy" thay vì lỗi hệ thống 500.</p>
</div>

</div>

---

# Phân Tích AC Chi Tiết: LDMS-003 (Hàng Đợi OCR)

<div class="p-5 rounded-xl bg-slate-50 border border-slate-200 shadow-sm text-xs space-y-3 mt-2">

<div class="flex items-center justify-between border-b border-slate-200 pb-2">
  <span class="font-bold text-emerald-900 text-sm">LDMS-003: Hàng Đợi OCR Và Trạng Thái Xử Lý</span>
  <div class="flex gap-2">
    <span class="badge bg-emerald-700 text-white text-[10px] px-2 py-0.5 rounded font-bold">Bắt Buộc Có</span>
    <span class="badge bg-slate-200 text-slate-800 text-[10px] px-2 py-0.5 rounded font-bold">Kích Thước M</span>
  </div>
</div>

<p class="text-slate-700 italic">"Là cán bộ thủ thư, tôi muốn hệ thống chạy nhận dạng chữ OCR dưới nền và theo dõi được trạng thái xử lý để không phải chờ đợi trên giao diện."</p>

<div class="space-y-1.5 text-slate-800">
  <strong class="text-emerald-900 block">Tiêu Chí Chấp Nhận (AC):</strong>
  <p><strong>AC1:</strong> Khi kích hoạt OCR, tác vụ được khởi tạo ở trạng thái ban đầu <code>pending</code> (chờ xử lý).</p>
  <p><strong>AC2:</strong> Tác vụ tự động chuyển đổi trạng thái: <code>processing</code> → <code>completed</code> hoặc <code>failed</code>.</p>
  <p><strong>AC3:</strong> API kích hoạt trả về nhanh, xử lý bất đồng bộ, không khóa luồng nghiệp vụ chính.</p>
  <p><strong>AC4:</strong> Nếu tác vụ <code>failed</code>, hệ thống bắt buộc ghi lại <code>error_message</code> không rỗng.</p>
</div>

</div>

---

# Phân Tích AC Chi Tiết: LDMS-015 (Tìm Kiếm Toàn Văn FTS)

<div class="p-5 rounded-xl bg-slate-50 border border-slate-200 shadow-sm text-xs space-y-3 mt-2">

<div class="flex items-center justify-between border-b border-slate-200 pb-2">
  <span class="font-bold text-emerald-900 text-sm">LDMS-015: Tìm Kiếm Toàn Văn (PostgreSQL FTS)</span>
  <div class="flex gap-2">
    <span class="badge bg-emerald-700 text-white text-[10px] px-2 py-0.5 rounded font-bold">Bắt Buộc Có</span>
    <span class="badge bg-slate-200 text-slate-800 text-[10px] px-2 py-0.5 rounded font-bold">Kích Thước M</span>
  </div>
</div>

<p class="text-slate-700 italic">"Là độc giả, tôi muốn tìm sách theo từ khóa trong tiêu đề/tác giả/nội dung đã OCR."</p>

<div class="space-y-1.5 text-slate-800">
  <strong class="text-emerald-900 block">Tiêu Chí Chấp Nhận (AC):</strong>
  <p><strong>AC1:</strong> Document có title chứa từ khóa → <code>GET /search?q=...</code> trả về document đó.</p>
  <p><strong>AC2:</strong> Từ khóa chỉ nằm trong nội dung trang (không ở title) → vẫn tìm thấy được (full-text thực sự, không chỉ tìm theo tiêu đề).</p>
  <p><strong>AC3:</strong> Query rỗng/whitespace → trả lỗi hoặc mảng rỗng theo convention nhất quán (không crash).</p>
  <p><strong>AC4:</strong> Query hợp lệ thông thường không gây lỗi server (đảm bảo tính ổn định của tính năng lõi MVP).</p>
</div>

</div>

---

# Kế Hoạch Thực Hiện Yêu Cầu Backlog

<div class="space-y-2.5 mt-4 text-xs">

<div class="p-3 bg-slate-50 rounded-lg border border-slate-200 flex justify-between items-center">
  <span><strong class="text-emerald-900">Giai Đoạn 1: Nền Tảng & Luồng Dữ Liệu</strong> — LDMS-001 (Compose), 002 (Upload), 003 (OCR nền), 004 (Text theo trang), 005 (API sửa text)</span>
  <span class="badge bg-emerald-700 text-white text-[10px] px-2 py-0.5 font-bold rounded">Tuần 1–7</span>
</div>

<div class="p-3 bg-slate-50 rounded-lg border border-slate-200 flex justify-between items-center">
  <span><strong class="text-emerald-900">Giai Đoạn 2: Biên Tập & Xuất Bản</strong> — LDMS-006 (UI sửa text), 011 (Metadata), 007 (Xuất EPUB), 013 (Publish gate), 008 (Reader)</span>
  <span class="badge bg-emerald-700 text-white text-[10px] px-2 py-0.5 font-bold rounded">Tuần 8–11</span>
</div>

<div class="p-3 bg-slate-50 rounded-lg border border-slate-200 flex justify-between items-center">
  <span><strong class="text-emerald-900">Giai Đoạn 3: Xác Thực & Tra Cứu</strong> — LDMS-009 (Auth), 010 (Access control), 012 (Category), 015 (FTS), 016 (Snippet), 026 (Document List)</span>
  <span class="badge bg-emerald-700 text-white text-[10px] px-2 py-0.5 font-bold rounded">Tuần 12–17</span>
</div>

<div class="p-3 bg-slate-50 rounded-lg border border-slate-200 flex justify-between items-center">
  <span><strong class="text-emerald-900">Giai Đoạn 4–5: Nâng Cao Trải Nghiệm & Hoàn Thiện</strong> — Split-screen, Signed URL, Google OAuth, Bookmark, Tags, Highlight, Citation, Elasticsearch</span>
  <span class="badge bg-emerald-700 text-white text-[10px] px-2 py-0.5 font-bold rounded">Tuần 18–20</span>
</div>

</div>

---

# Cơ Chế Quản Trị & Chỉ Số KPI Thành Công

<div class="grid grid-cols-2 gap-4 mt-4 text-xs">

<div class="p-4 rounded-xl bg-slate-50 border border-slate-200 shadow-sm space-y-2">
  <strong class="text-emerald-900 text-sm block border-b border-slate-200 pb-1">Cơ Cấu Quản Trị Dự Án</strong>
  <p class="text-slate-700">Ban Giám hiệu (Nhà tài trợ) → Ban Giám đốc Thư viện (Nghiệp vụ) → Phòng CNTT (Quản trị kỹ thuật, PM) → Technical Lead → Đội phát triển.</p>
  <p class="text-slate-700"><strong>Kiểm soát thay đổi:</strong> Thay đổi vượt quá 5% ngân sách hoặc phạm vi bắt buộc phải trình phê duyệt liên tịch từ PM và Giám đốc Thư viện trước khi trình Ban Giám hiệu.</p>
</div>

<div class="p-4 rounded-xl bg-emerald-50/80 border border-emerald-200 shadow-sm space-y-2">
  <strong class="text-emerald-900 text-sm block border-b border-emerald-200 pb-1">5 Chỉ Số KPI Thành Công Cốt Lõi</strong>
  <ul class="space-y-1 text-slate-800 font-medium">
    <li>1. Số hóa đạt tỷ lệ ≥ 90% giáo trình trọng yếu trong 12 tháng.</li>
    <li>2. Tốc độ tra cứu toàn văn < 3 giây dưới điều kiện vận hành bình thường.</li>
    <li>3. Độ chính xác nhận dạng chữ OCR tiếng Việt ≥ 85%.</li>
    <li>4. Tuyệt đối hạn chế tối đa sự cố rò rỉ tệp sách gốc ra ngoài.</li>
    <li>5. Mức độ hài lòng của độc giả và thủ thư đạt ≥ 85%.</li>
  </ul>
</div>

</div>

---

# Quy Trình Thẩm Định Backlog Giữa AI và Con Người

<div class="grid grid-cols-2 gap-4 mt-4 text-xs">

<div class="p-4 bg-blue-50/80 rounded-xl border border-blue-200 shadow-sm space-y-2">
  <strong class="text-blue-900 text-sm block">1. Trợ Lý AI Rà Soát Yêu Cầu</strong>
  <p class="text-slate-700">AI tự động quét danh sách yêu cầu (Backlog), đối chiếu định nghĩa hoàn thành (DoD), gợi ý bổ sung tiêu chí chấp nhận cho trường hợp biên và kiểm tra tính phụ thuộc giữa các yêu cầu.</p>
</div>

<div class="p-4 bg-emerald-50/80 rounded-xl border border-emerald-200 shadow-sm space-y-2">
  <strong class="text-emerald-900 text-sm block">2. Người Quản Lý (PM / Tech Lead) Phê Duyệt</strong>
  <p class="text-slate-700">Người quản lý xem xét các gợi ý của trợ lý AI, đánh giá tính khả thi theo năng lực thực tế của đội ngũ kỹ sư trước khi chuyển yêu cầu sang trạng thái Sẵn Sàng Triển Khai.</p>
</div>

</div>