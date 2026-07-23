# SLIDE DECK — PHẦN 3: ARCHITECTURE VÀ PROOF OF CONCEPT
## Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS (HCMUS-LDMS)

> Nguồn nội dung: `06-architecture.md`
> Số lượng slide đề xuất: **13 slide**

---

## Slide 1 — Trang bìa

**Loại slide:** Title Slide

**Nội dung:**
- Tiêu đề: Kiến trúc Phần mềm & Proof of Concept
- Phụ đề: "Modular Monolith — On-premise — Bảo mật DRM"
- Trạng thái tài liệu: Approved (đã duyệt)

**Gợi ý thiết kế:**
- Layout kỹ thuật: nền lưới (grid/blueprint) mờ gợi cảm giác sơ đồ kiến trúc
- Font tiêu đề dạng monospace nhẹ (kỹ thuật) khác với 2 phần trước (học thuật/quản lý)

**Ghi chú thuyết trình:** Đây là phần chuyển từ "quản lý dự án" sang "kỹ thuật thực thi" — đổi tông trình bày sang chi tiết, chứng minh bằng sơ đồ.

---

## Slide 2 — Mục tiêu & Ràng buộc Kiến trúc

**Loại slide:** Architecture Goals & Constraints

**Nội dung:**
- Mục tiêu: hiệu năng cao (FTS <3 giây), bảo mật bản quyền (Signed URL 15 phút, không nút Download), xử lý bất đồng bộ (BackgroundTasks không nghẽn luồng chính)
- Ràng buộc: hạ tầng on-premise (VMware vSphere sẵn có), ngân sách phát triển + thiết bị <100.000.000 VNĐ

**Gợi ý thiết kế:**
- 2 cột đối lập: "Mục tiêu" (icon mũi tên hướng lên, màu xanh) vs "Ràng buộc" (icon khung giới hạn, màu cam)
- Giữ ngắn gọn — đây là slide dẫn nhập cho toàn bộ phần kiến trúc

**Ghi chú thuyết trình:** Nhấn mạnh mọi quyết định kiến trúc sau đây đều bắt nguồn từ 2 ràng buộc này: ngân sách thấp và hạ tầng có sẵn.

---

## Slide 3 — Vì sao chọn Modular Monolith (không phải Microservices/DSpace)?

**Loại slide:** Architecture Decision Record (ADR)

**Nội dung:**
- Không dùng DSpace: chỉ là kho lưu trữ tĩnh, không hỗ trợ OCR động, Split-screen, hay biên dịch EPUB tự động
- Không dùng Microservices: đội chỉ 4 kỹ sư kiêm nhiệm (~2 full-time) — Microservices sẽ gây quá tải quản lý hạ tầng/CI-CD
- Chọn Modular Monolith: gộp logic (OCR, Editor, EPUB, Search, Reader) vào 1 khối nhưng chia module rõ ràng — dễ kiểm thử, dễ tách nhỏ sau này nếu cần scale

**Gợi ý thiết kế:**
- Sơ đồ so sánh 3 lựa chọn dạng "bàn cân" (scale/balance) — DSpace và Microservices ở 2 đầu, Modular Monolith ở giữa là điểm cân bằng được chọn
- Có thể minh họa bằng 3 icon kiến trúc khác nhau (kho tĩnh, lưới microservices phức tạp, khối module gọn)

**Ghi chú thuyết trình:** Đây là quyết định kiến trúc quan trọng nhất — cần giải thích rõ lý do "phù hợp quy mô đội ngũ" hơn là "công nghệ tốt nhất trên lý thuyết".

---

## Slide 4 — Ngăn xếp Công nghệ (Technology Stack)

**Loại slide:** Tech Stack Table

**Nội dung:**
| Lớp | Công nghệ | Lý do chọn |
|---|---|---|
| Frontend | React 18 + TypeScript, Epub.js | SPA phản hồi nhanh, type-safe, đọc EPUB responsive |
| Backend | FastAPI (Python 3.11) | Hiệu năng cao, async/await, tự sinh Swagger UI |
| Web Server | Nginx | Reverse proxy, SSL/TLS 1.3 |
| Database | PostgreSQL 16 (+ FTS) | RBAC, metadata, Full-Text Search tích hợp sẵn |
| OCR | Tesseract OCR 5.3+ | Mã nguồn mở, hỗ trợ gói tiếng Việt (`vie`) |
| EPUB Compiler | Pandoc & Calibre CLI | Biên dịch Markdown/HTML → EPUB 3.0 |
| Lưu trữ | MinIO (S3-compatible) | Object storage on-premise |
| Auth (MVP) | Google OAuth 2.0 | Tận dụng Gmail `@hcmus.edu.vn`, không cần self-host |
| Triển khai | Docker & Docker Compose | Đóng gói container, dễ vận hành trên VMware |

**Gợi ý thiết kế:**
- Bảng dài — nên trình bày dạng "stack diagram" xếp lớp từ trên xuống (Frontend → Gateway → Backend → Data) thay vì bảng thuần, mỗi lớp 1 logo công nghệ
- Giữ 1 dòng lý do ngắn gọn cạnh mỗi công nghệ, tránh nhồi nhét text

**Ghi chú thuyết trình:** Nhấn mạnh nguyên tắc chọn công nghệ: mã nguồn mở + đã quen thuộc với đội ngũ 4 kỹ sư, tránh học công nghệ mới giữa lịch trình gấp.

---

## Slide 5 — C4 Context Diagram: Hệ thống trong bối cảnh nghiệp vụ

**Loại slide:** C4 Model — Level 1 (Context)

**Nội dung:**
- 3 tác nhân: Độc giả (SV/GV), Thủ thư/Biên tập viên, Quản trị viên
- 1 hệ thống trung tâm: HCMUS-LDMS
- 1 hệ thống ngoài: Google OAuth 2.0 (xác thực danh tính)
- Quan hệ: Đọc/tìm kiếm bảo mật; Upload & xuất bản EPUB; Quản trị người dùng & danh mục

**Gợi ý thiết kế:**
- Vẽ đúng chuẩn C4 Context: hình người (actor) bao quanh 1 hình chữ nhật hệ thống trung tâm, hệ thống ngoài vẽ nhạt màu hơn
- Dùng Visualizer (diagram module) để dựng sơ đồ C4 Context chuẩn từ PlantUML có sẵn trong tài liệu

**Ghi chú thuyết trình:** Đây là góc nhìn "từ xa nhất" — dùng để giải thích cho người không rành kỹ thuật (VD: Ban Giám hiệu) trước khi đi sâu vào Container/Deployment.

---

## Slide 6 — C4 Container Diagram: Các thành phần độc lập

**Loại slide:** C4 Model — Level 2 (Container)

**Nội dung:**
- React SPA (Frontend) ↔ Nginx Reverse Proxy ↔ FastAPI Backend
- FastAPI Backend ↔ PostgreSQL (metadata + FTS) & MinIO (raw scan + EPUB)
- FastAPI Backend ↔ Google OAuth 2.0 (xác thực)
- BackgroundTasks tách riêng xử lý OCR/Pandoc bất đồng bộ, không chặn luồng request chính

**Gợi ý thiết kế:**
- Sơ đồ hộp-mũi tên chuẩn C4 Container, dùng màu khác nhau cho Frontend (xanh dương), Backend (xanh lá), Data stores (cam), hệ thống ngoài (xám)
- Vẽ bằng Visualizer diagram module theo đúng cấu trúc PlantUML C4_Container đã có

**Ghi chú thuyết trình:** Đây là sơ đồ kỹ thuật chính dùng để giải thích luồng dữ liệu tổng thể cho đội phát triển.

---

## Slide 7 — Góc nhìn Logic: Phân lớp trách nhiệm (Layered View)

**Loại slide:** Logical Layered Architecture

**Nội dung:**
- 5 lớp: Presentation (React/Epub.js) → API Gateway/Security (Nginx, Google OAuth) → Application Service (FastAPI Routers, BackgroundTasks) → Domain Logic (Document/OCR/EPUB/Search Service) → Data Access & Infrastructure (PostgreSQL, MinIO)
- Mục tiêu: cô lập thay đổi công nghệ tầng dưới mà không ảnh hưởng tầng trên

**Gợi ý thiết kế:**
- Sơ đồ xếp lớp ngang (horizontal layers) từ trên xuống dưới, mỗi lớp 1 dải màu riêng với mũi tên chỉ hướng phụ thuộc đi xuống
- Nhấn icon "khóa" ở lớp Gateway/Security để nhấn mạnh vai trò bảo mật

**Ghi chú thuyết trình:** Giải thích nguyên tắc dependency chỉ đi 1 chiều (trên phụ thuộc dưới) — nền tảng cho khả năng bảo trì lâu dài.

---

## Slide 8 — Sơ đồ tuần tự: Luồng đọc sách bảo mật (Sequence Diagram)

**Loại slide:** Sequence Diagram

**Nội dung:**
- Độc giả → Frontend → Nginx → Backend → Google OAuth (xác thực JWT) → PostgreSQL (kiểm tra RBAC) → MinIO (sinh Signed URL 15 phút) → trả về Frontend → hiển thị qua Epub.js
- Điểm mấu chốt: Signed URL chỉ được sinh SAU KHI xác thực + kiểm tra quyền thành công

**Gợi ý thiết kế:**
- Sơ đồ tuần tự chuẩn UML (các actor/participant dọc, mũi tên ngang theo thời gian từ trên xuống)
- Highlight bước sinh Signed URL bằng khung nổi bật màu vàng — đây là điểm bảo mật quan trọng nhất

**Ghi chú thuyết trình:** Dùng slide này để chứng minh: không có bước nào trong luồng đọc sách bỏ qua kiểm tra phân quyền.

---

## Slide 9 — Bảo mật, Sao lưu & Khôi phục thảm họa

**Loại slide:** Security & DR Strategy

**Nội dung:**
- Bảo mật: HTTPS/TLS 1.3 + HSTS, Signed URL 15 phút, vô hiệu hóa nút tải EPUB gốc
- Sao lưu: PgBackRest (incremental hàng ngày 02:00, full backup Chủ nhật, mã hóa AES-256); Restic đồng bộ MinIO sang NAS off-site hàng đêm
- Retention: bản ngày giữ 30 ngày, tuần giữ 12 tuần, tháng giữ 12 tháng
- DR Targets: **RPO ≤ 24 giờ**, **RTO ≤ 4 giờ**

**Gợi ý thiết kế:**
- 2 khối: "Bảo mật khi vận hành" (khiên/khóa icon) và "Sao lưu & Phục hồi" (đám mây/đĩa icon)
- RPO/RTO hiển thị dạng đồng hồ đếm ngược lớn — dễ ghi nhớ 2 con số quan trọng nhất

**Ghi chú thuyết trình:** Đây là câu trả lời cho câu hỏi "nếu server hỏng thì sao" — cần nhấn số liệu RPO/RTO cụ thể để tăng độ tin cậy.

---

## Slide 10 — Góc nhìn Triển khai: Sơ đồ Deployment trên VMware

**Loại slide:** C4 Deployment View

**Nội dung:**
- VMware vSphere (ESXi) → VM-Production (Ubuntu 22.04, Docker Compose: Nginx + FastAPI + PostgreSQL + MinIO) và VM-Staging (môi trường UAT/dev riêng biệt)
- Kết nối ngoài duy nhất: Google OAuth 2.0 API (qua HTTPS)
- Cấu hình phần cứng: VM-Production 8 vCPU/32GB RAM/2TB HDD+500GB SSD; VM-Staging 4 vCPU/16GB RAM/200GB SSD

**Gợi ý thiết kế:**
- Sơ đồ lồng hộp (nested boxes): VMware ngoài cùng → VM → Docker Compose → từng container bên trong
- Dùng màu nhạt dần theo độ sâu lồng nhau để thể hiện phân lớp hạ tầng vật lý → logic

**Ghi chú thuyết trình:** Nhấn mạnh: toàn bộ hạ tầng dùng lại tài nguyên sẵn có của trường, không phát sinh chi phí cloud.

---

## Slide 11 — Demo & Chứng minh: PoC 1 — Xử lý OCR bất đồng bộ (bài toán khó nhất)

**Loại slide:** PoC Demo — Hardest Core Feature

**Nội dung:**
- Mục tiêu kiểm chứng: tách tác vụ OCR (CPU-bound) khỏi luồng phản hồi HTTP (I/O-bound) để không làm nghẽn server
- Nguyên lý: Request → ghi file vào MinIO → đăng ký `run_ocr_task` vào `BackgroundTasks` → trả `202 Accepted` ngay lập tức → xử lý Tesseract trong `ThreadPoolExecutor` qua `loop.run_in_executor` → cập nhật `Processed` vào PostgreSQL
- Kịch bản demo gợi ý: gửi 1 request OCR thật, cho thấy API trả về ngay (không treo), sau đó theo dõi trạng thái job chuyển `pending → processing → completed`

**Gợi ý thiết kế:**
- Sơ đồ luồng dọc theo timeline: request tại t=0, response 202 gần như tức thì, xử lý nền kéo dài phía dưới cùng — trực quan hóa "phản hồi nhanh dù xử lý nặng chạy ngầm"
- Nếu demo trực tiếp: dùng terminal/Postman gọi API thật, chiếu song song 2 cửa sổ (request log và job status)

**Ghi chú thuyết trình:** Đây là "bài toán khó nhất" theo đúng yêu cầu đề bài — nhấn mạnh không dùng Celery/Redis mà chỉ dùng BackgroundTasks vẫn đạt mục tiêu bất đồng bộ ở quy mô MVP.

---

## Slide 12 — Demo & Chứng minh: PoC 2 — Tích hợp liên thông Tech Stack End-to-End

**Loại slide:** PoC Demo — E2E Integration

**Nội dung:**
- Kịch bản: Sinh viên bấm "Đọc sách" → xác thực JWT (Google OAuth/Mock Auth) → truy vấn PostgreSQL (metadata + quyền) → sinh Signed URL từ MinIO → Epub.js render sách trên trình duyệt
- Mục tiêu kiểm chứng: toàn bộ 5 lớp công nghệ (React → FastAPI → PostgreSQL → MinIO → Epub.js) kết nối thông suốt, không lưu file tạm trên máy người dùng
- Kết quả PoC (từ tài liệu Vision & Scope): OCR sách in từ 2010+ đạt CAR ≥88%; EPUB xuất bản vượt qua kiểm tra `epubcheck` chuẩn IDPF

**Gợi ý thiết kế:**
- Sơ đồ ngang 5 bước với icon từng công nghệ nối tiếp nhau bằng mũi tên, đánh số bước 1-4 khớp nguyên lý vận hành
- Nếu demo trực tiếp: mở thật trình duyệt, đăng nhập, bấm đọc sách mẫu để cả lớp thấy Signed URL hoạt động (có thể inspect Network tab trình duyệt để chứng minh)

**Ghi chú thuyết trình:** Đây là minh chứng "tech stack không chỉ đúng trên giấy mà chạy được thật" — nên ưu tiên demo trực tiếp thay vì chỉ trình bày sơ đồ nếu điều kiện cho phép.

---

## Slide 13 — Tổng kết Kiến trúc & Cấu trúc mã nguồn khung

**Loại slide:** Summary + Skeleton Structure

**Nội dung:**
- Cấu trúc repo: `backend/` (FastAPI: core, api, models, services) và `frontend/` (React: components, pages, services) trong cùng 1 monorepo
- Quản lý cấu hình: quy tắc đặt mã CI (`LDMS_[LOAI_CI]_[TRANG_THAI]X.Y`), GitFlow (`main`, `develop`, `feature/*`, `release/*`, `hotfix/*`)
- Kết luận: kiến trúc đơn giản hóa phù hợp đồ án — đã kiểm chứng qua 2 PoC, sẵn sàng chuyển sang giai đoạn phát triển

**Gợi ý thiết kế:**
- Cây thư mục (file tree) hiển thị dạng code block đúng font monospace, thu gọn chỉ hiển thị 2 cấp thư mục chính
- Sơ đồ nhánh Git (Gitflow) dạng đường nhánh ngang phía dưới cây thư mục

**Ghi chú thuyết trình:** Kết thúc phần kiến trúc bằng việc chuyển ý sang Phần 4 — "Vậy đội ngũ 4 kỹ sư sẽ cùng code trên cấu trúc này như thế nào?"
