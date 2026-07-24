---
theme: tahta
themeConfig:
  variant: notebook
  mark: false
highlighter: shiki
drawings:
  persist: false
transition: slide-left
mermaid:
  theme: base
  themeVariables:
    edgeLabelBackground: '#ffffff'
    labelBackground: '#ffffff'
    primaryTextColor: '#475569'
---

<style>
.foot > span:first-child,
.slidev-layout .foot > span:first-child,
footer span:first-of-type,
.slidev-nav {
  display: none !important;
  opacity: 0 !important;
  visibility: hidden !important;
  pointer-events: none !important;
}
</style>

<div class="flex flex-col items-center justify-center h-full text-center p-6">
  <div class="text-xs uppercase tracking-widest text-amber-500 font-mono font-bold mb-4 font-bold">Báo cáo dự án · Tài liệu trình bày chính thức</div>
  <h1 class="text-3xl font-black text-slate-900 leading-tight max-w-3xl">Hệ thống Quản lý và Số hóa Tài liệu<br><span class="text-emerald-800">Thư viện Trường Đại học Khoa học Tự nhiên</span></h1>
  <div class="text-sm italic text-slate-500 mt-2 font-medium">HCMUS Library Document Management & Digitization System</div>
  <div class="w-16 h-0.5 bg-slate-300 my-6"></div>
  <div class="inline-block bg-slate-100 text-slate-800 text-xs font-bold px-4 py-1.5 rounded-full mb-6 font-mono font-bold font-bold">Mã dự án: HCMUS-LDMS</div>
  <div class="text-sm text-slate-600 leading-relaxed font-semibold">Thư viện & Phòng Công nghệ Thông tin<br>Trường Đại học Khoa học Tự nhiên — Đại học Quốc gia TP.HCM</div>
  <div class="flex gap-6 justify-center mt-8 text-xs text-slate-500 border-t border-slate-100 pt-6 w-full max-w-xl">
    <span><b>Cấp độ bảo mật:</b> Nội bộ trường</span>
    <span><b>Đội ngũ phát triển:</b> Nhóm 3</span>
  </div>
</div>

---
layout: default
---

<div class="flex flex-col h-full justify-between">
  <div>
    <div class="text-xs uppercase tracking-widest text-emerald-700 font-bold mb-1">Cấu trúc báo cáo</div>
    <h2 class="text-2xl font-black text-slate-900 leading-tight mb-4">Năm phần trình bày, bám sát bộ tài liệu dự án</h2>
    <div class="flex flex-col gap-2">
      <!-- Row 1 -->
      <div class="flex items-center gap-4 bg-slate-50 border border-slate-100 rounded-xl p-2.5 hover:bg-slate-100 transition-colors">
        <span class="text-xl font-extrabold text-emerald-700 w-8 text-center font-mono">01</span>
        <div class="flex-1">
          <h4 class="font-extrabold text-slate-900 text-sm">Project Proposal</h4>
          <p class="text-slate-500 text-[11px] mt-0.5">Lý do đầu tư, đối chuẩn đối thủ & công cụ sẵn có, bên liên quan</p>
        </div>
      </div>
      <!-- Row 2 -->
      <div class="flex items-center gap-4 bg-slate-50 border border-slate-100 rounded-xl p-2.5 hover:bg-slate-100 transition-colors">
        <span class="text-xl font-extrabold text-emerald-700 w-8 text-center font-mono">02</span>
        <div class="flex-1">
          <h4 class="font-extrabold text-slate-900 text-sm">Vision & Scope · Charter · Backlog</h4>
          <p class="text-slate-500 text-[11px] mt-0.5">Quy trình nghiệp vụ, bên liên quan, tiêu chí chấp nhận</p>
        </div>
      </div>
      <!-- Row 3 -->
      <div class="flex items-center gap-4 bg-slate-50 border border-slate-100 rounded-xl p-2.5 hover:bg-slate-100 transition-colors">
        <span class="text-xl font-extrabold text-emerald-700 w-8 text-center font-mono">03</span>
        <div class="flex-1">
          <h4 class="font-extrabold text-slate-900 text-sm">Architecture & Proof of Concept</h4>
          <p class="text-slate-500 text-[11px] mt-0.5">Kiến trúc, minh chứng kỹ thuật, bài toán khó nhất</p>
        </div>
      </div>
      <!-- Row 4 -->
      <div class="flex items-center gap-4 bg-slate-50 border border-slate-100 rounded-xl p-2.5 hover:bg-slate-100 transition-colors">
        <span class="text-xl font-extrabold text-emerald-700 w-8 text-center font-mono">04</span>
        <div class="flex-1">
          <h4 class="font-extrabold text-slate-900 text-sm">Development Method</h4>
          <p class="text-slate-500 text-[11px] mt-0.5">Kanban, AI Coding Assistant, tích hợp mã nguồn nhóm</p>
        </div>
      </div>
      <!-- Row 5 -->
      <div class="flex items-center gap-4 bg-slate-50 border border-slate-100 rounded-xl p-2.5 hover:bg-slate-100 transition-colors">
        <span class="text-xl font-extrabold text-emerald-700 w-8 text-center font-mono">05</span>
        <div class="flex-1">
          <h4 class="font-extrabold text-slate-900 text-sm">Estimation, Planning & Monitoring</h4>
          <p class="text-slate-500 text-[11px] mt-0.5">Ước lượng UCP/COCOMO, kế hoạch, giám sát & báo cáo</p>
        </div>
      </div>
    </div>
  </div>
</div>

---
src: ./pages/01-project-proposal.md
hide: true
---

---
src: ./pages/02-vision-charter-backlog.md
hide: true
---

---
src: ./pages/03-architecture-poc.md
hide: true
---

---
src: ./pages/04-development-method.md
hide: false
---

---
src: ./pages/05-estimation-planning-monitoring.md
hide: true
---

