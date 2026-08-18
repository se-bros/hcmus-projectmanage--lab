---
layout: default
class: bg-slate-50
---

<div class="relative flex flex-col justify-center h-full p-8 overflow-hidden">
  <div class="absolute right-4 top-1/2 -translate-y-1/2 text-[15rem] font-extrabold leading-none select-none pointer-events-none opacity-[0.08] font-mono text-emerald-900">04</div>
  <div class="z-10">
    <div class="text-xs uppercase tracking-widest text-amber-600 font-extrabold mb-2 font-mono">Phần 04</div>
    <h1 class="text-4xl font-black text-slate-900 leading-tight mb-4">Phương Pháp Thực Hiện Dự Án</h1>
    <div class="w-16 h-1 bg-emerald-600 rounded mb-6"></div>
    <p class="text-slate-600 text-sm max-w-xl leading-relaxed mb-6 font-semibold">Phần này giải thích nhóm tổ chức công việc hàng tuần như thế nào (Kanban theo hướng Spec-Driven, mỗi người sở hữu 1 Epic), cách dùng AI hỗ trợ viết mã nguồn, cách ghi lại nhật ký làm việc, và cách các thành viên gộp mã nguồn với nhau (Git Trunk-based).</p>
    <div class="flex gap-2 flex-wrap">
      <span class="text-[10px] font-bold text-slate-800 bg-white border border-slate-200 px-3 py-1 rounded-full shadow-sm">Kanban theo Epic + Trợ lý AI</span>
      <span class="text-[10px] font-bold text-slate-800 bg-white border border-slate-200 px-3 py-1 rounded-full shadow-sm">Spec-Driven Development</span>
      <span class="text-[10px] font-bold text-slate-800 bg-white border border-slate-200 px-3 py-1 rounded-full shadow-sm">Git Trunk-based</span>
      <span class="text-[10px] font-bold text-slate-800 bg-white border border-slate-200 px-3 py-1 rounded-full shadow-sm">Ghi nhận thực tế 5 phiên làm việc</span>
    </div>
  </div>
</div>

---

# Phương Pháp Vận Hành: Gating + Kanban Spec-Driven Theo Epic

<div class="grid grid-cols-2 gap-4 mt-2 text-[11px]">

<div class="p-3 rounded-lg bg-slate-50 border border-slate-200 shadow-sm space-y-1.5">
  <h3 class="text-emerald-900 font-bold text-xs border-b border-slate-200 pb-1">Tầng vĩ mô: Các mốc kiểm tra (Gate 0 → Gate 3)</h3>
  <ul class="space-y-1 text-slate-700 list-disc list-inside">
    <li>Dự án chia làm 4 cổng kiểm soát gắn với mốc ngân sách.</li>
    <li>Cần trình bày sản phẩm thực tế đã hoàn thành để giải ngân pha tiếp theo.</li>
    <li>Báo cáo tiến độ Ban Giám hiệu cuối Tuần 2, 12, 18 và 20.</li>
  </ul>
</div>

<div class="p-3 rounded-lg bg-emerald-50/80 border border-emerald-200 shadow-sm space-y-1.5">
  <h3 class="text-emerald-900 font-bold text-xs border-b border-emerald-200 pb-1">Tầng vi mô: Kanban Spec-Driven, mỗi người own 1 Epic</h3>
  <ul class="space-y-1 text-slate-700 list-disc list-inside">
    <li>Mỗi thành viên nhận toàn quyền sở hữu <strong>1 Epic</strong> (A/B/C/D), gồm nhiều User Story liên quan — không chia lẻ story ngẫu nhiên giữa các thành viên.</li>
    <li>Trong phạm vi Epic của mình, làm theo quy trình <strong>Spec-Driven</strong> (đặc tả yêu cầu → lập kế hoạch → chia task → triển khai) trước khi code, thay vì code trực tiếp theo cảm tính.</li>
  </ul>
</div>

</div>

<div class="grid grid-cols-3 gap-4 mt-3 text-[11px]">

<div class="p-3 rounded-lg bg-slate-50 border border-slate-200 shadow-sm">
  <strong class="text-emerald-900 text-xs block mb-1">1. Giới hạn 1 việc/lúc trong Epic (WIP = 1)</strong>
  <p class="text-slate-700 leading-relaxed">Mỗi thành viên nhận 1 Epic đã xác định trước các user story. Thành viên tự lên kế hoạch hoàn thành hoặc báo bị vướng.</p>
</div>

<div class="p-3 rounded-lg bg-slate-50 border border-slate-200 shadow-sm">
  <strong class="text-emerald-900 text-xs block mb-1">2. Điều kiện để bắt đầu làm (DoR)</strong>
  <p class="text-slate-700 leading-relaxed">Có mã số công việc rõ ràng, tiêu chí hoàn thành cụ thể, việc phụ thuộc đã xong, khối lượng không quá 2 ngày.</p>
</div>

<div class="p-3 rounded-lg bg-slate-50 border border-slate-200 shadow-sm">
  <strong class="text-emerald-900 text-xs block mb-1">3. Điều kiện để coi là xong (DoD theo Epic)</strong>
  <p class="text-slate-700 leading-relaxed">Người sở hữu Epic định nghĩa & chịu trách nhiệm DoD cho toàn bộ Epic đó: từng story con đạt 100% tiêu chí, mã nguồn review & gộp qua Pull Request, chạy tốt trên máy local, cập nhật tài liệu và ghi nhật ký thời gian/token AI — Epic chỉ "Done" khi mọi story con trong Epic đều đạt.</p>
</div>

</div>

<div class="mt-4 text-[9px] text-slate-500 leading-normal border-t border-slate-200 pt-1">
  <strong>Epic</strong>: nhóm User Story lớn theo cùng một mảng nghiệp vụ (VD: Epic B — Số hóa & Xuất bản), do 1 thành viên sở hữu xuyên suốt <br>
  <strong>Spec-Driven</strong>: quy trình viết đặc tả (spec) và kế hoạch trước khi code, dùng công cụ Spec Kit (specify → plan → tasks → implement) <br>
  <strong>WIP</strong>: Work In Progress (số việc đang làm dở cùng lúc) <br>
  <strong>DoR</strong>: Definition of Ready (điều kiện để bắt đầu làm) <br>
  <strong>DoD</strong>: Definition of Done (điều kiện để coi là xong)
</div>

---

# Quy Ước Nhánh Git Trunk-based Cho Đội 4 Người

<div class="p-3 bg-slate-50 border border-slate-200 shadow-sm rounded-lg text-xs text-slate-700 leading-relaxed mb-3">
  Nhóm dùng <strong>Trunk-based Development</strong>: chỉ có 1 nhánh chính (`main`), không dùng nhánh `develop` trung gian như GitFlow. Mọi nhánh Epic/story đều tách ra từ `main`, tồn tại trong thời gian ngắn, và gộp thẳng trở lại `main` qua Pull Request đã review + qua CI.
</div>

<div class="space-y-3 mt-4 text-xs">

<div class="p-3 bg-slate-50 rounded-lg border border-slate-200 flex items-center justify-between shadow-sm">
  <span><strong class="text-emerald-900">Nhánh `main` (trunk):</strong> Nhánh duy nhất, luôn ở trạng thái deploy được — mọi Epic/story sau khi merge vào đây coi như đã tích hợp xong, không có nhánh tích hợp trung gian.</span>
  <span class="badge bg-emerald-700 text-white font-bold px-2 py-0.5 rounded shrink-0 whitespace-nowrap">Được bảo vệ</span>
</div>

<div class="p-3 bg-slate-50 rounded-lg border border-slate-200 flex items-center justify-between shadow-sm">
  <span><strong class="text-emerald-900">Nhánh `epic/xxx` hoặc `feature/LDMS-xxx`:</strong> Nhánh ngắn hạn cho từng Epic hoặc từng story cụ thể (theo mã số công việc trên bảng Kanban), tách trực tiếp từ `main` và gộp thẳng lại `main` — không đi qua bước trung gian nào.</span>
  <span class="badge bg-slate-200 text-slate-800 font-bold px-2 py-0.5 rounded shrink-0 whitespace-nowrap">Ngắn hạn</span>
</div>

</div>

<div class="mt-4 p-3 bg-emerald-50 rounded-lg border border-emerald-200 text-xs text-slate-800 shadow-sm">
  <strong>Quy tắc kiểm tra mã nguồn:</strong> Mọi yêu cầu gộp mã nguồn (Pull Request) từ nhánh Epic/feature <strong>gộp thẳng vào `main`</strong> bắt buộc phải được ít nhất 1 Trưởng nhóm kỹ thuật (Solution Architect) xem lại trong vòng 24 giờ, và phải vượt qua toàn bộ bài kiểm thử tự động (CI). Merge thường xuyên, từng phần nhỏ để tránh nhánh sống quá lâu và xung đột mã nguồn lớn.
</div>

<div class="mt-4 text-[9px] text-slate-500 leading-normal border-t border-slate-200 pt-1">
  <strong>Trunk-based Development</strong>: mô hình nhánh Git chỉ dùng 1 nhánh chính (trunk/`main`), nhánh phụ tồn tại ngắn hạn và merge trực tiếp vào trunk — khác GitFlow (vốn có thêm nhánh `develop`, `release` trung gian) <br>
  <strong>Pull Request (PR)</strong>: yêu cầu đưa mã nguồn từ nhánh riêng vào nhánh chung, kèm bước người khác kiểm tra lại trước khi gộp
</div>

---

# Quy Trình Phát Triển Với Sự Hỗ Trợ Của AI

```mermaid
graph LR
    A[Soạn yêu cầu / prompt] --> B[Trợ lý AI viết mã]
    B --> C[Sinh mã nguồn & bài kiểm thử]
    C --> D[Con người kiểm tra lại]
    D --> E[Chạy thử trên máy local/Docker]
    E --> F[Gộp mã nguồn & ghi log]

    classDef default fill:#f8fafc,stroke:#cbd5e1,stroke-width:1px,color:#1e293b,font-size:10px,font-weight:bold;
    classDef start fill:#f0fdf4,stroke:#bbf7d0,stroke-width:1.5px,color:#166534,font-weight:bold;
    classDef main fill:#ecfdf5,stroke:#a7f3d0,stroke-width:1.5px,color:#065f46,font-weight:bold;
    classDef endNode fill:#fffbeb,stroke:#fef3c7,stroke-width:1.5px,color:#92400e,font-weight:bold;

    class A start;
    class B,C,D,E main;
    class F endNode;
```

<div class="grid grid-cols-2 gap-4 mt-3 text-[10.5px]">

<div class="p-3 bg-blue-50/80 rounded-xl border border-blue-200 shadow-sm space-y-1">
  <strong class="text-blue-900 text-xs block">AI hỗ trợ những việc gì?</strong>
  <p class="text-slate-700 leading-normal">Tự động viết khung mã nguồn lặp lại, hỗ trợ cấu hình Docker, gợi ý hàm xử lý dữ liệu, và viết bài kiểm thử nhanh hơn khoảng 3 lần so với viết tay.</p>
</div>

<div class="p-3 bg-emerald-50/80 rounded-xl border border-emerald-200 shadow-sm space-y-1">
  <strong class="text-emerald-900 text-xs block">Con người vẫn phải kiểm soát điều gì?</strong>
  <p class="text-slate-700 leading-normal">Đọc hiểu và review toàn bộ mã do AI sinh ra trước khi gộp; đảm bảo đúng kiến trúc Modular Monolith; và phải giải thích được đoạn mã đó khi được hỏi.</p>
</div>

</div>

<div class="mt-4 text-[9px] text-slate-500 leading-normal border-t border-slate-200 pt-1">
  <strong>AI Coding Assistant</strong>: công cụ trí tuệ nhân tạo hỗ trợ viết mã — trong dự án này con người luôn là người ra quyết định cuối cùng, AI chỉ là công cụ hỗ trợ
</div>

---

# Minh Chứng Thực Tế: 2 Cách Nhóm Đang Dùng AI Coding Assistant

<div class="p-3 bg-slate-50 border border-slate-200 shadow-sm rounded-lg text-xs text-slate-700 leading-relaxed">
    Đây là số liệu <strong>tổng hợp từ nhật ký làm việc thực tế</strong> của nhóm, Nhóm quan sát được 2 cách làm việc khác nhau, tùy thói quen từng thành viên — không có cách nào "đúng duy nhất", miễn là qua được bước con người kiểm tra lại.
</div>

<div class="grid grid-cols-2 gap-4 mt-4 text-xs">

<div class="p-4 rounded-xl bg-slate-50 border border-slate-200 shadow-sm space-y-2">
  <strong class="text-emerald-900 text-sm block border-b border-slate-200 pb-1">Cách 1 — Chuyển tiếp giữa 2 model (Khoa Nguyễn, phiên 16/07 & 18/07)</strong>
  <p class="text-slate-700">Dùng <strong>Claude Sonnet 5</strong> để đọc yêu cầu, phân tích tiêu chí hoàn thành và chia nhỏ công việc trước — sau đó chuyển sang <strong>Claude Opus 4.8</strong> để viết mã nguồn thật. Cách này giống như "một người lên kế hoạch, một người thi công".</p>
</div>

<div class="p-4 rounded-xl bg-emerald-50/90 border border-emerald-300 shadow-sm space-y-2">
  <strong class="text-emerald-900 text-sm block border-b border-emerald-300 pb-1">Cách 2 — Một trợ lý AI làm liên tục (Tuấn Anh, phiên 17/07 & 22/07)</strong>
  <p class="text-slate-700">Dùng <strong>Claude Sonnet 5 chạy trong Claude Code</strong> (công cụ AI dùng trực tiếp trên dòng lệnh), để một model xử lý liên tục từ đọc yêu cầu → viết mã → chạy kiểm thử trong cùng một phiên làm việc, không đổi model giữa chừng.</p>
</div>

</div>

<div class="mt-4 text-[9px] text-slate-500 leading-normal border-t border-slate-200 pt-1">
  <strong>Claude Code</strong>: công cụ dùng Claude trực tiếp trên dòng lệnh (CLI) để lập trình
</div>

---

# Minh Chứng Thực Tế: Số Liệu Từng Phiên Làm Việc Với AI

<table class="w-full text-left border-collapse text-[9px] mt-2 leading-tight">
  <thead>
    <tr class="bg-slate-900 text-white font-bold">
      <th class="p-1.5 border border-slate-700 text-center whitespace-nowrap">Phiên</th>
      <th class="p-1.5 border border-slate-700 whitespace-nowrap">Ngày</th>
      <th class="p-1.5 border border-slate-700 whitespace-nowrap">Người làm</th>
      <th class="p-1.5 border border-slate-700 whitespace-nowrap">Công việc (Story ID)</th>
      <th class="p-1.5 border border-slate-700 text-center whitespace-nowrap">Thời gian</th>
      <th class="p-1.5 border border-slate-700 text-right whitespace-nowrap">Token AI</th>
      <th class="p-1.5 border border-slate-700 whitespace-nowrap">Nội dung thực hiện</th>
    </tr>
  </thead>
  <tbody>
    <tr class="bg-white">
      <td class="p-1.5 border border-slate-200 text-center">1</td>
      <td class="p-1.5 border border-slate-200 text-slate-700">16/07</td>
      <td class="p-1.5 border border-slate-200 text-slate-900 font-semibold">Khoa Nguyễn</td>
      <td class="p-1.5 border border-slate-200 text-slate-700 font-mono text-[9px]">LDMS-008/026</td>
      <td class="p-1.5 border border-slate-200 text-center">2h</td>
      <td class="p-1.5 border border-slate-200 text-right text-emerald-800 font-semibold">40K</td>
      <td class="p-1.5 border border-slate-200 text-slate-700">Trang danh sách tài liệu & khung Tìm kiếm/Đọc sách</td>
    </tr>
    <tr class="bg-slate-50">
      <td class="p-1.5 border border-slate-200 text-center">2</td>
      <td class="p-1.5 border border-slate-200 text-slate-700">16/07</td>
      <td class="p-1.5 border border-slate-200 text-slate-900 font-semibold">Khoa Ngô & Thái</td>
      <td class="p-1.5 border border-slate-200 text-slate-700 font-mono text-[9px]">LDMS-003/004/007/013/022</td>
      <td class="p-1.5 border border-slate-200 text-center">45p</td>
      <td class="p-1.5 border border-slate-200 text-right text-emerald-800 font-semibold">280K</td>
      <td class="p-1.5 border border-slate-200 text-slate-700">Quy trình số hóa & xuất bản sách</td>
    </tr>
    <tr class="bg-white">
      <td class="p-1.5 border border-slate-200 text-center">3</td>
      <td class="p-1.5 border border-slate-200 text-slate-700">17/07</td>
      <td class="p-1.5 border border-slate-200 text-slate-900 font-semibold">Tuấn Anh</td>
      <td class="p-1.5 border border-slate-200 text-slate-700 font-mono text-[9px]">LDMS-001/009/010/018</td>
      <td class="p-1.5 border border-slate-200 text-center">1h 20p</td>
      <td class="p-1.5 border border-slate-200 text-right text-emerald-800 font-semibold">120K</td>
      <td class="p-1.5 border border-slate-200 text-slate-700">Đăng nhập, phân quyền, đăng nhập Google + giao diện</td>
    </tr>
    <tr class="bg-slate-50">
      <td class="p-1.5 border border-slate-200 text-center">4</td>
      <td class="p-1.5 border border-slate-200 text-slate-700">22/07</td>
      <td class="p-1.5 border border-slate-200 text-slate-900 font-semibold">Tuấn Anh</td>
      <td class="p-1.5 border border-slate-200 text-slate-700 font-mono text-[9px]">LDMS-001/009/010/018 (mở rộng)</td>
      <td class="p-1.5 border border-slate-200 text-center">2h</td>
      <td class="p-1.5 border border-slate-200 text-right text-emerald-800 font-semibold">150K</td>
      <td class="p-1.5 border border-slate-200 text-slate-700">Hoàn thiện đăng nhập, phân quyền theo vai trò</td>
    </tr>
    <tr class="bg-white">
      <td class="p-1.5 border border-slate-200 text-center">5</td>
      <td class="p-1.5 border border-slate-200 text-slate-700">18/07</td>
      <td class="p-1.5 border border-slate-200 text-slate-900 font-semibold">Khoa Nguyễn</td>
      <td class="p-1.5 border border-slate-200 text-slate-700 font-mono text-[9px]">LDMS-008/014/015/016/019/020/026</td>
      <td class="p-1.5 border border-slate-200 text-center">6h</td>
      <td class="p-1.5 border border-slate-200 text-right text-emerald-800 font-semibold">100K</td>
      <td class="p-1.5 border border-slate-200 text-slate-700">Trải nghiệm Tìm kiếm & Đọc sách</td>
    </tr>
    <tr class="bg-emerald-50/80 text-emerald-900 font-bold">
      <td class="p-1.5 border border-slate-200 text-center">Tổng</td>
      <td class="p-1.5 border border-slate-200"></td>
      <td class="p-1.5 border border-slate-200"></td>
      <td class="p-1.5 border border-slate-200"></td>
      <td class="p-1.5 border border-slate-200 text-center">12h 05p</td>
      <td class="p-1.5 border border-slate-200 text-right">690K</td>
      <td class="p-1.5 border border-slate-200"></td>
    </tr>
  </tbody>
</table>

<div class="mt-3 p-3 bg-slate-50 rounded-lg border border-slate-200 text-xs text-slate-700">
  <strong>Nhận xét thực tế:</strong> Phiên 2 dùng nhiều token nhất (280K, ~40% tổng token) dù chỉ làm trong 45 phút — vì xử lý cùng lúc 5 công việc thuộc quy trình số hóa/OCR. Ngược lại, phiên 5 mất nhiều thời gian nhất (6 giờ) nhưng chỉ dùng 100K token — cho thấy phần lớn thời gian là thao tác thủ công và kiểm thử giao diện, không phải "chat" liên tục với AI.
</div>

---

# Nhật Ký Phiên AI & Quy Trình Kiểm Thử Đảm Bảo Chất Lượng

<div class="grid grid-cols-2 gap-4 mt-3 text-xs">

<div class="p-3.5 rounded-xl bg-slate-50 border border-slate-200 shadow-sm space-y-2">
  <strong class="text-emerald-900 text-sm block border-b border-slate-200 pb-1">1. Ghi nhận nhật ký phiên AI (../../03-execution-monitoring/02-project-log.md)</strong>
  <p class="text-slate-700">Mỗi khi hoàn thành công việc, thành viên ghi lại một dòng theo mẫu thật sau:</p>
  <div class="p-2.5 bg-slate-800 text-emerald-400 font-mono text-[9px] rounded leading-tight">
    [2026-07-18] [LDMS-008/014/015/016/019/020/026] Khoa Nguyễn hoàn thành Search & Reader experience (Thời gian: 6h, Token AI: 100.000).
  </div>
  <ul class="space-y-1 text-slate-700 list-disc list-inside mt-2 text-[11px]">
    <li>Theo dõi chính xác thời gian thực tế so với ước tính.</li>
    <li>Đo lường mức độ AI đã giúp ích cho công việc.</li>
    <li>Làm minh chứng dữ liệu nghiệm thu tại các mốc Gate.</li>
  </ul>
</div>

<div class="p-3.5 rounded-xl bg-slate-50 border border-slate-200 shadow-sm space-y-2 text-[11px]">
  <strong class="text-emerald-900 text-sm block border-b border-slate-200 pb-1">2. Kiểm thử tự động & Đảm bảo chất lượng</strong>
  <ul class="space-y-2 text-slate-700">
    <li><strong>Kiểm thử từng phần (Unit Test):</strong> Kiểm tra độc lập từng chức năng nhỏ (Đăng nhập, OCR, Link bảo mật). Tỷ lệ đạt tối thiểu từ 95% trở lên.</li>
    <li><strong>Kiểm thử toàn trình (Playwright E2E):</strong> Tự động giả lập thao tác của người dùng thật trên trình duyệt để kiểm tra hiển thị giao diện.</li>
    <li><strong>Rà soát bảo mật:</strong> Tự động quét các lỗ hổng bảo mật, kiểm tra cơ chế hết hạn của link đọc sách và phân quyền truy cập.</li>
  </ul>
</div>

</div>

<div class="mt-4 text-[9px] text-slate-500 leading-normal border-t border-slate-200 pt-1">
  <strong>Token AI</strong>: đơn vị đo lượng "chữ" mà công cụ AI đã xử lý — dùng để ước tính chi phí/công sức sử dụng AI <br>
  <strong>E2E</strong>: End-to-End (kiểm thử toàn bộ luồng sử dụng từ đầu đến cuối, giống như người dùng thật sử dụng)
</div>
