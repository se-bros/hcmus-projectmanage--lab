# PHẦN 4: DEVELOPMENT METHOD
## Phương Pháp Phát Triển & Quy Trình Kỹ Thuật

<div class="mt-6 text-sm text-slate-700">
  <p class="text-base font-semibold text-emerald-900 mb-2">Phương Pháp Phát Triển & Quy Trình Kỹ Thuật</p>
  <p class="text-slate-600">Phương pháp luận Hybrid (Gating + Kanban WIP=1), chiến lược GitFlow, AI-Assisted Coding và QA Playwright.</p>
</div>

<div class="mt-8 flex gap-3">
  <span class="badge bg-emerald-700 text-white font-bold px-3 py-1 text-xs rounded-full shrink-0 whitespace-nowrap">Hybrid Methodology</span>
  <span class="badge bg-emerald-700 text-white font-bold px-3 py-1 text-xs rounded-full shrink-0 whitespace-nowrap">Kanban WIP=1</span>
  <span class="badge bg-slate-200 text-slate-800 font-bold px-3 py-1 text-xs rounded-full shrink-0 whitespace-nowrap">AI-Assisted Coding</span>
</div>

---

# Phương Pháp Luận Hybrid: Gating + Kanban

<div class="grid grid-cols-2 gap-6 mt-4 text-xs">

<div class="p-4 rounded-xl bg-slate-50 border border-slate-200 shadow-sm space-y-2">
  <h3 class="text-emerald-900 font-bold text-sm border-b border-slate-200 pb-1.5">Tầng Vĩ Mô: Gating Checkpoints</h3>
  <ul class="space-y-1.5 text-slate-700">
    <li>Khởi tạo 4 cổng kiểm soát (Gate 0 - Gate 3) gắn liền với milestone ngân sách.</li>
    <li>Mỗi cổng yêu cầu nghiệm thu sản phẩm thực tế trước khi giải ngân giai đoạn kế tiếp.</li>
    <li>Báo cáo định kỳ Ban Giám hiệu vào cuối Tuần 2, 12, 18 và 20.</li>
  </ul>
</div>

<div class="p-4 rounded-xl bg-emerald-50/80 border border-emerald-200 shadow-sm space-y-2">
  <h3 class="text-emerald-900 font-bold text-sm border-b border-emerald-200 pb-1.5">Tầng Vi Mô: Kanban Vận Hành hàng Tuần</h3>
  <ul class="space-y-1.5 text-slate-700">
    <li>Vận hành theo bảng Kanban linh hoạt, phù hợp lịch làm việc kiêm nhiệm.</li>
    <li>Thiết lập giới hạn WIP = 1 card/người (hoặc /agent AI) để tránh phân tán nguồn lực.</li>
    <li>Đo Throughput hàng tuần (số story Done/tuần) để dự báo tiến độ chính xác.</li>
  </ul>
</div>

</div>

---

# Quy Tắc Kanban Chi Tiết: WIP, DoR, DoD

<div class="grid grid-cols-3 gap-4 mt-4 text-xs">

<div class="p-4 rounded-xl bg-slate-50 border border-slate-200 shadow-sm">
  <strong class="text-emerald-900 text-sm block mb-1">Giới Hạn WIP = 1</strong>
  <p class="text-slate-700">Mỗi thành viên chỉ làm duy nhất 1 card tại một thời điểm. Card hiện tại phải `Done` hoặc bị `Block` rõ ràng mới được nhận việc mới.</p>
</div>

<div class="p-4 rounded-xl bg-slate-50 border border-slate-200 shadow-sm">
  <strong class="text-emerald-900 text-sm block mb-1">Definition of Ready (DoR)</strong>
  <p class="text-slate-700">Card vào `In Progress` phải có: ID story, Acceptance Criteria (AC) rõ ràng, `depends_on` đã Done, Size $\le$ M (tối đa 2 ngày).</p>
</div>

<div class="p-4 rounded-xl bg-slate-50 border border-slate-200 shadow-sm">
  <strong class="text-emerald-900 text-sm block mb-1">Definition of Done (DoD)</strong>
  <p class="text-slate-700">Pass 100% AC, Code được review & merge qua PR, test local thành công, README cập nhật và ghi log nỗ lực/token AI.</p>
</div>

</div>

---

# Chiến Lược Nhánh Git (GitFlow) Cho Đội 4 Người

<div class="space-y-3 mt-4 text-xs">

<div class="p-3 bg-slate-50 rounded-lg border border-slate-200 flex items-center justify-between shadow-sm">
  <span><strong class="text-emerald-900">`main` Branch:</strong> Nhánh sản phẩm chính thức, 100% code đã qua UAT, sẵn sàng deploy lên môi trường Production.</span>
  <span class="badge bg-emerald-700 text-white font-bold px-2 py-0.5 rounded shrink-0 whitespace-nowrap">Protected</span>
</div>

<div class="p-3 bg-slate-50 rounded-lg border border-slate-200 flex items-center justify-between shadow-sm">
  <span><strong class="text-emerald-900">`develop` Branch:</strong> Nhánh tích hợp liên tục, nơi gộp các tính năng mới đã hoàn thành của sprint/tuần.</span>
  <span class="badge bg-slate-200 text-slate-800 font-bold px-2 py-0.5 rounded shrink-0 whitespace-nowrap">CI Integration</span>
</div>

<div class="p-3 bg-slate-50 rounded-lg border border-slate-200 flex items-center justify-between shadow-sm">
  <span><strong class="text-emerald-900">`feature/LDMS-xxx` Branch:</strong> Nhánh tính năng cá nhân tạo riêng cho từng User Story ID trên Backlog.</span>
  <span class="badge bg-slate-200 text-slate-800 font-bold px-2 py-0.5 rounded shrink-0 whitespace-nowrap">Short-lived</span>
</div>

</div>

<div class="mt-4 p-3 bg-emerald-50 rounded-lg border border-emerald-200 text-xs text-slate-800 shadow-sm">
  <strong>Quy tắc Code Review:</strong> Mọi Pull Request (PR) từ `feature/` vào `develop` bắt buộc phải có ít nhất 1 Tech Lead review và pass toàn bộ tự động kiểm thử.
</div>

---

# Quy Trình Phối Hợp AI-Assisted Coding

```mermaid
graph LR
    A[Soạn Prompt Yêu Cầu] --> B[AI Coding Assistant]
    B --> C[Sinh Code / Unit Test]
    C --> D[Con Người Review Code]
    D --> E[Chạy Test Local Docker]
    E --> F[Commit & Ghi Log Token]
```

<div class="grid grid-cols-2 gap-4 mt-4 text-xs">

<div class="p-4 bg-blue-50/80 rounded-xl border border-blue-200 shadow-sm space-y-1">
  <strong class="text-blue-900 text-sm block">Vai Trò Của AI Coding Assistant</strong>
  <p class="text-slate-700">Tự động sinh boilerplate code, hỗ trợ cấu hình Docker Compose, gợi ý hàm xử lý dữ liệu và sinh unit test nhanh gấp 3 lần.</p>
</div>

<div class="p-4 bg-emerald-50/80 rounded-xl border border-emerald-200 shadow-sm space-y-1">
  <strong class="text-emerald-900 text-sm block">Kiểm Soát Của Kỹ Sư Con Người</strong>
  <p class="text-slate-700">Kỹ sư trực tiếp thẩm định logic, đảm bảo mã nguồn tuân thủ kiến trúc Modular Monolith và không đưa các lỗ hổng bảo mật vào dự án.</p>
</div>

</div>

---

# Quản Lý Tri Thức Dự Án & Project Log

<div class="grid grid-cols-2 gap-4 mt-4 text-xs">

<div class="p-4 rounded-xl bg-slate-50 border border-slate-200 shadow-sm space-y-2">
  <strong class="text-emerald-900 text-sm block border-b border-slate-200 pb-1">Cấu Trúc File Project Log (`project_log.md`)</strong>
  <p class="text-slate-700">Mỗi khi hoàn thành 1 User Story, thành viên nhóm ghi nhận 1 dòng log theo chuẩn:</p>
  <div class="p-2.5 bg-slate-800 text-emerald-400 font-mono text-[10px] rounded">
    [YYYY-MM-DD] [LDMS-xxx] Thành viên A đã hoàn thành story X (Effort: 4h, AI Token: 12k).
  </div>
</div>

<div class="p-4 rounded-xl bg-slate-50 border border-slate-200 shadow-sm space-y-2">
  <strong class="text-emerald-900 text-sm block border-b border-slate-200 pb-1">Lợi Ích Của Việc Ghi Log Tri Thức</strong>
  <ul class="space-y-1.5 text-slate-700">
    <li>Theo dõi chính xác nỗ lực thực tế (Actual Hours) vs ước lượng ban đầu.</li>
    <li>Đo lường mức độ đóng góp và hiệu quả ứng dụng AI Assistant.</li>
    <li>Tạo cơ sở dữ liệu số liệu phục vụ báo cáo Gating Checkpoint cho Ban Giám hiệu.</li>
  </ul>
</div>

</div>

---

# Kiểm Thử Tự Động & Đảm Bảo Chất Lượng (QA)

<div class="grid grid-cols-3 gap-4 mt-4 text-xs text-center">

<div class="p-4 rounded-xl bg-slate-50 border border-slate-200 shadow-sm">
  <strong class="text-emerald-900 block mb-1">Unit Test (Pytest)</strong>
  <p class="text-slate-700 text-[11px]">Kiểm thử độc lập từng module backend (Auth, Metadata, OCR Job, DRM URL). Pass rate $\ge 95\%$.</p>
</div>

<div class="p-4 rounded-xl bg-slate-50 border border-slate-200 shadow-sm">
  <strong class="text-emerald-900 block mb-1">Playwright E2E Audit</strong>
  <p class="text-slate-700 text-[11px]">Tự động giả lập thao tác người dùng duyệt web, kiểm tra responsive màn hình và rà soát lỗi giao diện.</p>
</div>

<div class="p-4 rounded-xl bg-slate-50 border border-slate-200 shadow-sm">
  <strong class="text-emerald-900 block mb-1">Security Audit Script</strong>
  <p class="text-slate-700 text-[11px]">Rà soát tự động các lỗ hổng bảo mật, kiểm tra thời gian hết hạn Signed URL và phân quyền API.</p>
</div>

</div>

---

# Quản Trị Rủi Ro Tiến Độ Trong Phát Triển

<div class="space-y-3 mt-4 text-xs">

<div class="p-3 bg-slate-50 rounded-lg border border-slate-200 shadow-sm">
  <strong class="text-emerald-900 text-sm block mb-1">1. Quản Lý Nguồn Lực Kiêm Nhiệm</strong>
  <p class="text-slate-700">Lịch làm việc được chốt cố định theo tuần. Khi có thành viên bị bận việc đột xuất, card đang làm được trả về trạng thái `Ready` để thành viên khác tiếp quản.</p>
</div>

<div class="p-3 bg-slate-50 rounded-lg border border-slate-200 shadow-sm">
  <strong class="text-emerald-900 text-sm block mb-1">2. Nguyên Tắc Cắt Scope Linh Hoạt (Descope Strategy)</strong>
  <p class="text-slate-700">Nếu tiến độ bị chậm trễ tại Giai đoạn 1, nhóm sẽ ưu tiên cắt giảm các tính năng `Could-Have` và `Should-Have` để đảm bảo 100% tính năng `Must-Have` MVP sẵn sàng đúng Tuần 12.</p>
</div>

</div>


