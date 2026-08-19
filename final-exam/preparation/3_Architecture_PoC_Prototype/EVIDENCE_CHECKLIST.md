# CHECKLIST THU THẬP BẢN IN NỘP KÈM — NGƯỜI 3 (CÂU 5, 6, 7)

- **Người thực hiện:** Nguyễn Lê Hồ Anh Khoa (23127211)
- **Phiếu bài làm:** [`README.md`](./README.md)
- **Hạn hoàn thành:** trước **20:00 Thứ Năm 20/08/2026** (kịp đọc chéo Thứ Sáu – Thứ Bảy)

> **Quy chế cần nhớ:** Thi vấn đáp cho **2 phút** để chọn bản in nộp kèm. Thiếu bản in liên quan → **tối đa 8 điểm**. Vì vậy mỗi tờ in **phải ghi số câu to, rõ ở góc trên bên phải** (`[Câu 5]`, `[Câu 6]`, `[Câu 7]`) và xếp thành 3 kẹp riêng.
>
> Bản in **không được dùng trong 10 phút viết giấy A4** — chúng chỉ để nộp kèm và để giải thích khi vấn đáp. Nên đừng phụ thuộc vào chúng khi học.

---

## BẢNG TỔNG HỢP TIẾN ĐỘ

| # | Bản in | Cho câu | Trạng thái | Cách lấy |
| :-: | :-- | :-: | :-: | :-- |
| 1 | Tài liệu Kiến trúc phần mềm `02-architecture.md` | 5 | ⬜ Chưa in | Mục A bên dưới |
| 2 | Sơ đồ kiến trúc tổng thể (SVG đã render) | 5 | ⬜ Chưa in | Mục A |
| 3 | Log terminal chạy PoC 1 — OCR (đầu vào PDF → đầu ra text) | 6 | ⬜ **Chưa có, phải chạy** | Mục B |
| 4 | Kết quả PoC 2 — EPUB sinh ra + Signed URL | 6 | ⬜ **Chưa có, phải chạy** | Mục C |
| 5 | Kết quả `pytest` cho test của PoC | 6 | ⬜ Chưa có | Mục D |
| 6 | Ảnh chụp màn hình Split-screen Editor | 7 | ⬜ **Chưa có, phải chụp** | Mục E.1 |
| 7 | Ảnh chụp màn hình Web Reader (Epub.js) | 7 | ⬜ Chưa chụp (route đã nối xong 19/08) | Mục E.2 |
| 8 | Phác thảo wireframe ban đầu 2 màn hình | 7 | ⬜ **Chưa có, phải vẽ** | Mục F |
| 9 | Trích nhật ký 3 vòng tiến hóa Prototype | 7 | ⬜ Chưa in | Mục F |

---

## A. BẢN IN CHO CÂU 5 — KIẾN TRÚC PHẦN MỀM

### A.1 Đồng bộ tài liệu với mã nguồn — ✅ ĐÃ XONG (19/08/2026)

Xem bảng "⭐ BA ĐIỂM LỆCH" trong [`README.md`](./README.md). Các việc sau **đã thực hiện**, bản in sẽ khớp mã nguồn:

- [x] Sửa mục 9.2: đổi mô tả `loop.run_in_executor` / `ThreadPoolExecutor` thành `BackgroundTasks` + threadpool của Starlette (khớp `app/api/ocr.py:72`); bổ sung bước 6 về `attempt`, `409 Conflict` và `recover_interrupted_ocr_jobs()`.
- [x] Xóa đoạn 4.7.1 tồn dư (còn ghi Keycloak SSO / Celery / Elasticsearch), giữ bản đúng.
- [x] Thêm dòng **v3.1** vào bảng Revision History (19/08/2026, Nguyễn Lê Hồ Anh Khoa).
- [x] Thêm 1 dòng log vào [`docs/03-execution-monitoring/02-project-log.md`](../../../docs/03-execution-monitoring/02-project-log.md) (2026-08-19, 45min, 35K token).
- [ ] **Việc còn lại của bạn:** đọc lại mục 9.2 và 4.7.1 sau khi sửa để nắm đúng nội dung mình sẽ trình bày.

### A.2 In tài liệu

- [ ] In `docs/02-planning/02-architecture.md`. Nếu cần rút gọn, **ưu tiên các mục sau** (đây là những mục Thầy sẽ chỉ vào):
  - Bảng Document Control + Revision History (chứng minh 3 phiên bản)
  - Mục 2 (mục tiêu & ràng buộc), Mục 3 (Use Case = góc nhìn +1)
  - Mục 4.1 (vì sao Modular Monolith, vì sao không DSpace) + Mục 4.2 (bảng Tech Stack)
  - Mục 4.5 (C4 Container), Mục 4.6 (Sequence Signed URL)
  - Mục 6 (Deployment View), Mục 7.1–7.2 (cây thư mục), **Mục 7.3 (phản biện — rất ăn điểm)**
  - Mục 8 (mã CI + GitFlow), Mục 9 (PoC)
- [ ] Có thể xuất PDF đẹp bằng skill `md-to-pdf` hoặc `doc_generator` để bản in có sơ đồ render sẵn.
- [ ] In file SVG sơ đồ kiến trúc: `docs/assets/images/system_architecture.svg` và `context_diagram.svg` (mở bằng browser → Print).
- [ ] Ghi `[Câu 5]` góc trên phải mọi tờ.

---

## B. BẢN IN CHO CÂU 6 — POC 1: PIPELINE OCR (ĐẦU VÀO → ĐẦU RA)

> Đề bài đòi hỏi **"bản in giao diện thể hiện đầu vào và đầu ra khi chạy mã nguồn PoC"** — nên bản in phải thấy rõ **cả input lẫn output**, không phải chỉ một đoạn code.

### B.1 Khởi động hệ thống

```bash
cd src/backend
cp .env.example .env          # ENABLE_MOCK_AUTH=true đã có sẵn
docker compose up -d --build
docker compose exec api uv run --no-dev alembic upgrade head
```

- [ ] Chụp màn hình **`docker compose ps`** — chứng minh 3 container `api` / `postgres` / `minio` đang chạy (đây là bằng chứng hạ tầng của PoC).

### B.2 Lấy token quyền `editor`

```bash
TOKEN=$(curl -s -X POST http://localhost:8000/auth/dev-token \
  -H 'Content-Type: application/json' \
  -d '{"role":"editor"}' | python3 -c 'import sys,json;print(json.load(sys.stdin)["access_token"])')
echo "$TOKEN"
```

### B.3 ĐẦU VÀO — upload file PDF scan thật

```bash
curl -s -X POST http://localhost:8000/documents \
  -H "Authorization: Bearer $TOKEN" \
  -F 'file=@../../samples/two-page.pdf;type=application/pdf' | tee /tmp/upload.json
```

- [ ] Chụp màn hình lệnh này + response `201 {document_id}`.
- [ ] **Chụp riêng 1 ảnh trang đầu của `samples/two-page.pdf`** (mở file PDF ra) — đây chính là "đầu vào" trực quan nhất, Thầy sẽ muốn thấy tờ giấy scan gốc trông thế nào.

```bash
DOC=$(python3 -c 'import json;print(json.load(open("/tmp/upload.json"))["document_id"])')
echo "$DOC"
```

### B.4 Bằng chứng bất đồng bộ — HTTP 202 và trạng thái job

```bash
# Xem job OCR (upload đã tự tạo job nền)
curl -s -w '\nHTTP %{http_code} — thoi gian: %{time_total}s\n' \
  http://localhost:8000/documents/$DOC/ocr -H "Authorization: Bearer $TOKEN"
```

- [ ] Chụp màn hình cho thấy `status` chuyển `pending` → `processing` → `completed` khi gọi lại vài lần.
- [ ] **Điểm ăn điểm:** nếu job đã `completed`, gọi lại `POST /documents/$DOC/ocr` sẽ trả **409 Conflict** (`ConflictError` chống chạy trùng) — chụp luôn cái này, nó chứng minh PoC đã lường trước lỗi thật:

```bash
curl -s -w '\nHTTP %{http_code}\n' -X POST http://localhost:8000/documents/$DOC/ocr \
  -H "Authorization: Bearer $TOKEN"
```

### B.5 ĐẦU RA — text tiếng Việt được trích xuất

```bash
curl -s http://localhost:8000/documents/$DOC/pages \
  -H "Authorization: Bearer $TOKEN" | python3 -m json.tool | head -40
```

- [ ] Chụp màn hình JSON có `page_number` và `text_content` **chứa tiếng Việt có dấu** — đây là bằng chứng quan trọng nhất của Câu 6.
- [ ] Lưu ảnh preview PNG do Poppler render + Tesseract đọc:

```bash
curl -s http://localhost:8000/documents/$DOC/pages/1/image \
  -H "Authorization: Bearer $TOKEN" -o /tmp/page-1.png
```

- [ ] In `/tmp/page-1.png` cạnh JSON text — cặp ảnh/text này thể hiện trực quan "đầu vào ảnh → đầu ra văn bản".

### B.6 Log worker phía server

```bash
docker compose logs api --tail 80
```

- [ ] Chụp log cho thấy worker `run_ocr_job` chạy (và các dòng `logger.exception` nếu có lỗi, kèm cách khắc phục — nếu kể được một lần gặp lỗi thật thì càng thuyết phục).
- [ ] Chụp **MinIO Console** tại `http://localhost:9003` → bucket `ldms` → đường dẫn `documents/{id}/pages/1.png` để chứng minh file thật đã nằm trên object storage.

---

## C. BẢN IN CHO CÂU 6 — POC 2: PANDOC EPUB + SIGNED URL (E2E)

### C.1 Gán metadata bắt buộc (cửa chặn trước khi xuất bản)

```bash
curl -s -X PUT http://localhost:8000/documents/$DOC/metadata \
  -H "Authorization: Bearer $TOKEN" -H 'Content-Type: application/json' \
  -d '{"title":"Tai lieu thu nghiem PoC","author":"Nhom HCMUS-LDMS"}' | python3 -m json.tool
```

- [ ] **Nên chụp cả trường hợp lỗi trước:** gọi `POST /documents/$DOC/publish` **khi chưa có metadata** → trả lỗi `Required metadata is missing` kèm `missing_fields`. Ảnh này chứng minh PoC có **cổng kiểm soát chất lượng (quality gate)**, rất ăn điểm nếu bị hỏi chéo sang Câu 19.

### C.2 Xuất bản EPUB bằng Pandoc

```bash
curl -s -w '\nHTTP %{http_code}\n' -X POST http://localhost:8000/documents/$DOC/publish \
  -H "Authorization: Bearer $TOKEN"
sleep 5
curl -s http://localhost:8000/documents/$DOC/publish \
  -H "Authorization: Bearer $TOKEN" | python3 -m json.tool
```

- [ ] Chụp `202 Accepted` rồi `status: completed`.
- [ ] Chụp MinIO Console tại `documents/{id}/epub/{job_id}.epub` — **file EPUB thật đã được sinh ra**. Đây đúng điều Thầy nói ở Buổi 10: *"chỉ cần input pdf ra được cái epub"*.

### C.3 Signed URL 15 phút

```bash
curl -s http://localhost:8000/documents/$DOC/reader \
  -H "Authorization: Bearer $TOKEN" | python3 -m json.tool
```

- [ ] Chụp response có `epub_url` (thấy rõ query string `X-Amz-Expires`) và **`expires_in: 900`** — chứng minh con số 15 phút trong tài liệu kiến trúc là thật, không phải nói suông.
- [ ] **Bằng chứng bảo mật rất mạnh:** lấy token role `reader` khác và gọi cùng endpoint để thấy RBAC chặn:

```bash
RTOKEN=$(curl -s -X POST http://localhost:8000/auth/dev-token -H 'Content-Type: application/json' \
  -d '{"role":"reader"}' | python3 -c 'import sys,json;print(json.load(sys.stdin)["access_token"])')
curl -s -w '\nHTTP %{http_code}\n' -X POST http://localhost:8000/documents/$DOC/ocr \
  -H "Authorization: Bearer $RTOKEN"
```

- [ ] Chụp kết quả **403 Forbidden** — chứng minh `require_roles("editor","admin")` hoạt động.

---

## D. BẢN IN CHO CÂU 6 — KIỂM THỬ TỰ ĐỘNG CỦA POC

```bash
cd src/backend
uv run pytest tests/workers/test_ocr.py tests/api/test_ocr.py -v
uv run pytest -q            # toàn bộ 19 file test
```

- [ ] Chụp kết quả pass. Đây là bằng chứng cho câu hỏi *"PoC đã được đánh giá thế nào"* — trả lời: **được đánh giá bằng kiểm thử tự động, không chỉ chạy tay một lần**.
- [ ] Ghi `[Câu 6]` góc trên phải toàn bộ bản in mục B, C, D.

> **Gợi ý trình bày bản in Câu 6:** ghép thành **1 tờ A4 duy nhất theo cặp trái–phải**: bên trái là ảnh trang scan gốc (đầu vào), bên phải là JSON text tiếng Việt (đầu ra). Tờ này nói được toàn bộ câu 6 trong 3 giây. Các bản in còn lại xếp phía sau làm phụ lục.

---

## E. BẢN IN CHO CÂU 7 — ẢNH CHỤP PROTOTYPE CHẠY THẬT

```bash
cd src/frontend
npm install
npm run dev          # http://localhost:5173
```

Hoặc chạy cả hệ thống một lệnh: `./scripts/run.sh`

### E.1 Màn hình Split-screen Editor — quan trọng nhất

- [ ] Đăng nhập với quyền `editor`, mở `http://localhost:5173/documents/{id}` (tài liệu đã OCR ở mục B).
- [ ] Chụp **toàn màn hình** thấy rõ khối `scan-split-view`: bên trái pane "Ảnh scan", bên phải pane "Văn bản OCR" với `<textarea>` sửa được, bộ đếm `N ký tự`, nút "Lưu trang".
- [ ] Chụp thêm 1 ảnh sau khi sửa text mà chưa lưu → thấy dòng **"Có thay đổi chưa lưu"**; và 1 ảnh sau khi bấm Lưu → **"Đã lưu trang."** Hai ảnh này chứng minh prototype **có hành vi thật**, khác hoàn toàn mockup tĩnh (trả lời trực tiếp câu hỏi phụ số 2 của Câu 7).
- [ ] Chụp giao diện khi đăng nhập bằng quyền `reader` → khối `page-text-readonly`, không có ô nhập. Chứng minh prototype phản ánh RBAC.

### E.2 Màn hình Web Reader (Epub.js) — ✅ ROUTE ĐÃ ĐƯỢC NỐI (19/08/2026)

> **Bối cảnh:** `ReaderPage.tsx` trước đó có đủ code + test nhưng **thiếu khai báo route** trong `App.tsx`, khiến liên kết `/reader/{id}` từ `DocumentsPage.tsx:164` bị chuyển hướng về trang Tải lên. Route `<Route path="/reader/:documentId" element={<ReaderPage />} />` đã được thêm vào `App.tsx`, nên giờ chụp được màn hình bình thường. Xem bảng "⭐ BA ĐIỂM LỆCH" mục 3 trong [`README.md`](./README.md) để biết cách kể câu chuyện này khi vấn đáp.
>
> Lưu ý: `SearchPage.tsx` và `DocumentListPage.tsx` **vẫn chưa có route** — nếu bị hỏi thì thừa nhận đây là hạng mục còn lại.

- [ ] Vào `/documents`, bấm vào một tài liệu **đã publish** ở mục C (thẻ tài liệu sẽ tự trỏ sang `/reader/{id}`), hoặc mở trực tiếp `http://localhost:5173/reader/{id}`.
- [ ] Chụp EPUB đang render trong khối `reader-epub`, thấy rõ nội dung sách + thanh điều hướng chương.
- [ ] Chụp chức năng **highlight + ghi chú** (LDMS-021) — bằng chứng "prototype tiến hóa sinh ra yêu cầu mới".
- [ ] Chụp DevTools tab Network cho thấy request tải EPUB đi tới **Signed URL của MinIO** (thấy tham số `X-Amz-Expires`), không phải URL công khai. Đây là ảnh nối liền Câu 6 (PoC 2) với Câu 7 (Prototype) và Câu 5 (bảo mật DRM).
- [ ] In kèm mã nguồn `pages/ReaderPage.tsx` dòng 3 (`import ePub ... from 'epubjs'`) và dòng 120 (`const book = ePub(reader.epub_url)`) — chứng minh dùng thư viện thật, không phải mockup.

> **⚠️ Lưu ý môi trường:** `npm run lint` (oxlint) và `npx vitest run` hiện **không chạy được trong WSL** vì `node_modules` được cài từ Windows nên thiếu native binding cho Linux (`rolldown-binding.linux-x64-gnu.node`, `oxlint` bindings). Route mới đã được xác minh bằng `npx tsc -b --noEmit` (typecheck sạch). Nếu cần chụp ảnh kết quả test cho bản in, chạy `npm install` rồi `npm run test` **trong Windows** (hoặc cài lại `node_modules` trong WSL, nhưng khi đó sẽ không chạy được từ Windows nữa).

### E.3 Dashboard OCR (tùy chọn, nếu còn chỗ in)

- [ ] Chụp trang Dashboard liệt kê job OCR (`GET /ocr/jobs`) — hữu ích nếu bị hỏi chéo sang Câu 17 (theo dõi & kiểm soát công việc).

---

## F. BẢN IN CHO CÂU 7 — PHÁC THẢO BAN ĐẦU & BẰNG CHỨNG TIẾN HÓA

> Đề bài Câu 7 ghi rõ: *"nộp kèm bản in **phác thảo giao diện ban đầu**"*. Ảnh chụp sản phẩm hoàn thiện **không thay thế được** phác thảo ban đầu — phải có cả hai để thể hiện quá trình tiến hóa.

- [ ] **Wireframe 2 màn hình chính.** Nếu không còn file gốc, vẽ lại bằng tay trên A4 (hoàn toàn hợp lệ và thậm chí thuyết phục hơn):
  - _Màn hình 1 — Split-screen Editor:_ khung chia đôi, trái ghi "ẢNH SCAN trang N", phải ghi "TEXT OCR (sửa được)", dưới có nút "Lưu trang", trên có thanh chọn trang.
  - _Màn hình 2 — Web Reader:_ khung đọc sách, thanh chương bên trái, vùng nội dung giữa, nút chỉnh font/nền, biểu tượng highlight.
  - Ghi chú tay lên wireframe những chỗ đã thay đổi sau khi có phản hồi — **đây chính là bằng chứng "tiến hóa" trực quan nhất**.
- [ ] **In sơ đồ luồng nghiệp vụ đã render sẵn** (workflow text → diagram theo lời dặn Buổi 05): `docs/assets/images/as_is_to_be_workflow.svg` và `submission_workflow.svg`.
- [ ] **In trích nhật ký dự án** — 3 dòng chứng minh 3 vòng tiến hóa, lấy từ `docs/03-execution-monitoring/02-project-log.md`:

  | Ngày | Story | Nội dung | Giờ | Token |
  | :-- | :-- | :-- | --: | --: |
  | 2026-07-16 | LDMS-008/026 | Reader/Search placeholder & Document List | 2 | 40K |
  | 2026-07-18 | LDMS-008/014/015/016/019/020/026 | Search reader experience (7 SP) | 6 | 100K |
  | 2026-08-13 | LDMS-021 | Highlight và ghi chú | 2 | 40K |

- [ ] Chụp kết quả test frontend làm bằng chứng đánh giá prototype:

```bash
cd src/frontend
npm run test        # hoặc: npx vitest run
```

- [ ] Ghi `[Câu 7]` góc trên phải toàn bộ bản in mục E, F.

---

## G. KIỂM TRA CUỐI TRƯỚC KHI ĐI THI

- [ ] 3 kẹp tài liệu riêng biệt, mỗi tờ có số câu ghi to góc trên phải bằng bút dạ.
- [ ] Mỗi kẹp có **1 tờ chủ lực đặt trên cùng** (tờ nói được cả câu trong 3 giây):
  - Câu 5 → sơ đồ C4 Container hoặc sơ đồ kiến trúc tổng thể
  - Câu 6 → tờ ghép "ảnh scan (input) | JSON text tiếng Việt (output)"
  - Câu 7 → tờ ghép "wireframe phác thảo | ảnh chụp màn hình thật"
- [ ] Thuộc các con số then chốt (viết được ngay không cần nhìn): **900 giây / 15 phút** Signed URL · **300 DPI** · **`vie+eng`** · **timeout OCR 60s, Pandoc 120s** · **HTTP 202** · **19 test backend / 18 test frontend** · **tài liệu kiến trúc có 4 phiên bản (v1.0 → v3.1)** · **RPO 24h / RTO 4h** · **14h05m và 730K token toàn dự án tính đến 13/08/2026** · **126 UCP / 10.4 PM** (số của Người 4, nên biết để trả lời chéo).
- [ ] Thuộc 2 câu trả lời cho **bảng điểm lệch tài liệu vs mã nguồn** trong [`README.md`](./README.md).
- [ ] Đọc chéo phiếu của **Người 2** (Câu 4 — Backlog là đầu vào của kiến trúc) và **Người 5** (Câu 13–15 — CI/CD dùng chính Docker/GitFlow mô tả ở mục 6 và 8 của tài liệu kiến trúc).
- [ ] Giấy A4 trắng + bút mang theo (đề thi yêu cầu tự chuẩn bị).
- [ ] Tập viết thử 1 lần trong đúng **10 phút** cho mỗi câu 5, 6, 7 — theo khung WHAT / HOW / WHY / EVIDENCE + 1 sơ đồ.
