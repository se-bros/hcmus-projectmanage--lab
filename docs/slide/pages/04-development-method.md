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
    <p class="text-slate-600 text-sm max-w-xl leading-relaxed mb-6 font-semibold">Phần này giải thích nhóm tổ chức công việc hàng tuần như thế nào (Kanban), cách dùng AI hỗ trợ viết mã nguồn, cách ghi lại nhật ký làm việc, và cách các thành viên gộp mã nguồn với nhau (GitFlow).</p>
    <div class="flex gap-2 flex-wrap">
      <span class="text-[10px] font-bold text-slate-800 bg-white border border-slate-200 px-3 py-1 rounded-full shadow-sm">Bảng Kanban + Trợ lý AI</span>
      <span class="text-[10px] font-bold text-slate-800 bg-white border border-slate-200 px-3 py-1 rounded-full shadow-sm">Nhật ký làm việc</span>
      <span class="text-[10px] font-bold text-slate-800 bg-white border border-slate-200 px-3 py-1 rounded-full shadow-sm">Quy tắc nhánh Git</span>
      <span class="text-[10px] font-bold text-slate-800 bg-white border border-slate-200 px-3 py-1 rounded-full shadow-sm">Ghi nhận thực tế Tuần 1</span>
    </div>
  </div>
</div>

---

# Phương Pháp Vận Hành: Kết Hợp Gating & Kỷ Luật Kanban

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
  <h3 class="text-emerald-900 font-bold text-xs border-b border-emerald-200 pb-1">Tầng vi mô: Bảng Kanban vận hành hàng tuần</h3>
  <ul class="space-y-1 text-slate-700 list-disc list-inside">
    <li>Vận hành Kanban linh hoạt cho đội ngũ làm việc kiêm nhiệm.</li>
    <li>Thiết lập giới hạn WIP = 1 để tránh làm dở dang nhiều việc cùng lúc.</li>
    <li>Đo throughput thực tế hàng tuần để forecast tiến độ chính xác.</li>
  </ul>
</div>

</div>

<div class="grid grid-cols-3 gap-4 mt-3 text-[11px]">

<div class="p-3 rounded-lg bg-slate-50 border border-slate-200 shadow-sm">
  <strong class="text-emerald-900 text-xs block mb-1">1. Giới hạn WIP (WIP = 1)</strong>
  <p class="text-slate-700 leading-relaxed">Mỗi thành viên chỉ nhận 1 thẻ công việc cùng lúc. Hoàn thành hoặc báo bị vướng (Block) mới được nhận việc mới.</p>
</div>

<div class="p-3 rounded-lg bg-slate-50 border border-slate-200 shadow-sm">
  <strong class="text-emerald-900 text-xs block mb-1">2. Định nghĩa Sẵn sàng (DoR)</strong>
  <p class="text-slate-700 leading-relaxed">Có mã số công việc rõ ràng, tiêu chí hoàn thành cụ thể, việc phụ thuộc đã xong và khối lượng không quá 2 ngày (Size S/M).</p>
</div>

<div class="p-3 rounded-lg bg-slate-50 border border-slate-200 shadow-sm">
  <strong class="text-emerald-900 text-xs block mb-1">3. Định nghĩa Hoàn thành (DoD)</strong>
  <p class="text-slate-700 leading-relaxed">Đạt 100% tiêu chí AC, code đã review/merge qua PR, chạy tốt local, cập nhật tài liệu và ghi nhật ký thời gian/AI token.</p>
</div>

</div>

---

# Quy Ước Đặt Tên Nhánh Mã Nguồn (Git) Cho Đội 4 Người

<div class="space-y-3 mt-4 text-xs">

<div class="p-3 bg-slate-50 rounded-lg border border-slate-200 flex items-center justify-between shadow-sm">
  <span><strong class="text-emerald-900">Nhánh `main`:</strong> Nhánh chính thức của sản phẩm — mọi mã nguồn ở đây đều đã được kiểm thử người dùng (UAT) và sẵn sàng đưa vào sử dụng thật.</span>
  <span class="badge bg-emerald-700 text-white font-bold px-2 py-0.5 rounded shrink-0 whitespace-nowrap">Được bảo vệ</span>
</div>

<div class="p-3 bg-slate-50 rounded-lg border border-slate-200 flex items-center justify-between shadow-sm">
  <span><strong class="text-emerald-900">Nhánh `develop`:</strong> Nơi gộp chung các tính năng mới đã hoàn thành trong tuần, trước khi đưa lên nhánh chính thức.</span>
  <span class="badge bg-slate-200 text-slate-800 font-bold px-2 py-0.5 rounded shrink-0 whitespace-nowrap">Tích hợp liên tục</span>
</div>

<div class="p-3 bg-slate-50 rounded-lg border border-slate-200 flex items-center justify-between shadow-sm">
  <span><strong class="text-emerald-900">Nhánh `feature/LDMS-xxx`:</strong> Nhánh riêng cho từng công việc cụ thể (theo mã số công việc trên bảng Kanban), tồn tại trong thời gian ngắn rồi được gộp lại.</span>
  <span class="badge bg-slate-200 text-slate-800 font-bold px-2 py-0.5 rounded shrink-0 whitespace-nowrap">Ngắn hạn</span>
</div>

</div>

<div class="mt-4 p-3 bg-emerald-50 rounded-lg border border-emerald-200 text-xs text-slate-800 shadow-sm">
  <strong>Quy tắc kiểm tra mã nguồn:</strong> Mọi yêu cầu gộp mã nguồn (Pull Request) từ nhánh tính năng vào nhánh `develop` bắt buộc phải được ít nhất 1 Trưởng nhóm kỹ thuật (Tech Lead) xem lại, và phải vượt qua toàn bộ bài kiểm thử tự động.
</div>

<div class="mt-4 text-[9px] text-slate-500 leading-normal border-t border-slate-200 pt-1">
  <strong>UAT</strong>: User Acceptance Testing (kiểm thử nghiệm thu, do người dùng thật xác nhận sản phẩm đạt yêu cầu) <br>
  <strong>Pull Request (PR)</strong>: yêu cầu đưa mã nguồn từ nhánh riêng vào nhánh chung, kèm bước người khác kiểm tra lại trước khi gộp
</div>

---

# Phát Triển Với AI, Ghi Nhật Ký & Kiểm Thử Tự Động

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

<div class="grid grid-cols-3 gap-4 mt-3 text-[10.5px]">

<div class="p-3 bg-blue-50/80 rounded-xl border border-blue-200 shadow-sm space-y-1">
  <strong class="text-blue-900 text-xs block">1. Quy trình phát triển với AI</strong>
  <p class="text-slate-700 leading-normal">AI tự động viết khung code lặp lại, cấu hình Docker và sinh unit test nhanh hơn 3 lần. Kỹ sư con người trực tiếp review logic và bảo đảm cấu trúc Modular Monolith.</p>
</div>

<div class="p-3 bg-slate-50 rounded-xl border border-slate-200 shadow-sm space-y-1">
  <strong class="text-emerald-900 text-xs block">2. Nhật ký effort (project_log.md)</strong>
  <p class="text-slate-700 leading-normal">Bắt buộc ghi nhận sau mỗi session hoàn thành: <code>[Ngày] [Mã_Story] Dev (Thời gian thực tế, Lượng Token AI đã dùng)</code> để phục vụ giám sát tiến độ.</p>
</div>

<div class="p-3 bg-emerald-50/80 rounded-xl border border-emerald-200 shadow-sm space-y-1">
  <strong class="text-emerald-900 text-xs block">3. Kiểm thử tự động & Đảm bảo chất lượng</strong>
  <p class="text-slate-700 leading-normal">Kiểm thử từng phần (Unit Test đạt ≥ 95% độc lập), kiểm thử toàn trình (Playwright E2E giả lập trình duyệt) và tự động rà soát lỗ hổng bảo mật.</p>
</div>

</div>

<div class="mt-3 text-[9px] text-slate-500 leading-normal border-t border-slate-200 pt-1">
  <strong>Token AI</strong>: đơn vị đo lượng "chữ" mà công cụ AI đã xử lý — dùng để ước tính chi phí/công sức sử dụng AI <br>
  <strong>E2E</strong>: End-to-End (kiểm thử toàn bộ luồng sử dụng từ đầu đến cuối, giả lập người dùng thật)
</div>

---

# Bảng Chú Giải Thuật Ngữ & Từ Viết Tắt

<div class="grid grid-cols-2 gap-x-8 gap-y-1 mt-4 text-xs text-slate-700">

<div><strong>Kanban</strong> — phương pháp quản lý công việc bằng bảng thẻ, chia theo cột trạng thái (Sẵn sàng / Đang làm / Hoàn thành).</div>
<div><strong>WIP</strong> — Work In Progress: số công việc đang được làm dở cùng một lúc.</div>
<div><strong>DoR</strong> — Definition of Ready: điều kiện để một công việc đủ điều kiện bắt đầu làm.</div>
<div><strong>DoD</strong> — Definition of Done: điều kiện để một công việc được coi là hoàn thành.</div>
<div><strong>GitFlow</strong> — quy ước đặt tên và tổ chức các nhánh mã nguồn trong Git.</div>
<div><strong>PR</strong> — Pull Request: yêu cầu gộp mã nguồn từ nhánh riêng vào nhánh chung, có bước người khác kiểm tra lại.</div>
<div><strong>UAT</strong> — User Acceptance Testing: kiểm thử nghiệm thu bởi người dùng thật.</div>
<div><strong>CI/CD</strong> — Continuous Integration / Continuous Deployment: tự động kiểm tra và triển khai mã nguồn mỗi khi có thay đổi.</div>
<div><strong>AI Coding Assistant</strong> — công cụ trí tuệ nhân tạo hỗ trợ viết, gợi ý và kiểm tra mã nguồn.</div>
<div><strong>Token</strong> — đơn vị đo lượng dữ liệu chữ mà công cụ AI xử lý, dùng để ước tính công sức/chi phí dùng AI.</div>
<div><strong>Unit Test</strong> — bài kiểm thử cho từng phần nhỏ, độc lập của phần mềm.</div>
<div><strong>E2E Test</strong> — End-to-End: kiểm thử toàn bộ luồng sử dụng, từ đầu đến cuối.</div>
<div><strong>MVP</strong> — Minimum Viable Product: phiên bản sản phẩm tối thiểu, đủ dùng để đánh giá.</div>
<div><strong>Modular Monolith</strong> — kiến trúc một hệ thống duy nhất nhưng chia rõ thành nhiều module độc lập bên trong.</div>

</div>
