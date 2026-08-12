# Phase 1 — Quickstart: Highlight và ghi chú (LDMS-021)

Cách chạy và kiểm chứng feature ở máy local.

---

## 1. Dựng môi trường

```bash
# Backend + PostgreSQL + MinIO
cd src/backend
cp .env.example .env
docker compose up -d --build
docker compose exec api uv run --no-dev alembic upgrade head

# Frontend
cd ../frontend
npm install
npm run dev
```

| Service | URL |
| :--- | :--- |
| Frontend | http://localhost:5173 |
| API | http://localhost:8000 |
| API docs | http://localhost:8000/docs |

---

## 2. Chạy migration của feature này

Trước khi có merge revision (R5), lệnh dưới đây **sẽ báo lỗi** — đó là trạng thái hiện tại của nhánh, không phải máy hỏng:

```bash
cd src/backend
uv run alembic heads
# 20260717_0007 (head)
# 20260721_0008 (head)     ← hai head, `upgrade head` sẽ từ chối chạy
```

Sau khi thêm `20260812_0009_merge_heads.py` và `20260812_0010_highlights.py`:

```bash
uv run alembic heads          # kỳ vọng: chỉ còn 20260812_0010 (head)
uv run alembic upgrade head
```

Kiểm bảng đã tạo:

```bash
docker compose exec postgres psql -U ldms -d ldms -c "\d highlights"
```

Cần thấy: index `ix_highlights_document_user`, FK `document_id` với `ON DELETE CASCADE`, và **không** có unique constraint nào (xem `data-model.md`).

---

## 3. Kiểm bằng API (nhanh nhất, không cần EPUB thật)

⚠️ **Bẫy hay gặp**: `POST /auth/dev-token` sinh `sub` ngẫu nhiên mới **mỗi lần gọi** (`app/api/auth.py:61`). Gọi lại lần nữa là thành một user khác và highlight vừa tạo sẽ "biến mất". Lưu token vào biến và dùng lại xuyên suốt.

```bash
API=http://localhost:8000

# Một user, dùng lại token này cho mọi lệnh bên dưới
TOKEN=$(curl -s -X POST $API/auth/dev-token -H 'Content-Type: application/json' \
  -d '{"role":"reader"}' | jq -r .access_token)

DOC=<document_id đã publish>

# AC 1 — tạo highlight
curl -s -X POST $API/documents/$DOC/highlights \
  -H "Authorization: Bearer $TOKEN" -H 'Content-Type: application/json' \
  -d '{"cfi_range":"epubcfi(/6/14[chap03]!/4/2,/1:12,/3:28)","selected_text":"đoạn văn mẫu"}' | jq

# AC 1 — đọc lại, phải còn
curl -s $API/documents/$DOC/highlights -H "Authorization: Bearer $TOKEN" | jq

HL=<id vừa tạo>

# AC 2 — gắn ghi chú rồi đọc lại
curl -s -X PATCH $API/documents/$DOC/highlights/$HL \
  -H "Authorization: Bearer $TOKEN" -H 'Content-Type: application/json' \
  -d '{"note":"ghi chú thử"}' | jq .note

# AC 3 — xóa, rồi GET phải không còn
curl -s -X DELETE $API/documents/$DOC/highlights/$HL -H "Authorization: Bearer $TOKEN" -w '%{http_code}\n'
curl -s $API/documents/$DOC/highlights -H "Authorization: Bearer $TOKEN" | jq 'length'
```

**Kiểm cô lập user (FR-012)** — đây là lúc *cố tình* xin token thứ hai:

```bash
TOKEN_B=$(curl -s -X POST $API/auth/dev-token -H 'Content-Type: application/json' \
  -d '{"role":"reader"}' | jq -r .access_token)

curl -s $API/documents/$DOC/highlights -H "Authorization: Bearer $TOKEN_B" | jq 'length'   # kỳ vọng 0
curl -s -X DELETE $API/documents/$DOC/highlights/$HL -H "Authorization: Bearer $TOKEN_B" -w '%{http_code}\n'  # kỳ vọng 404
```

**Kiểm các nhánh từ chối**:

```bash
# FR-015 — không token
curl -s -X POST $API/documents/$DOC/highlights -H 'Content-Type: application/json' \
  -d '{"cfi_range":"epubcfi(/6/14!/4/2,/1:0,/1:5)","selected_text":"x"}' -w '%{http_code}\n'   # 401

# FR-005b — CFI vắt chương (không có "!" trước dấu phẩy đầu tiên)
curl -s -X POST $API/documents/$DOC/highlights -H "Authorization: Bearer $TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"cfi_range":"epubcfi(/6,/14!/4/2/1:0,/16!/4/2/1:9)","selected_text":"x"}' -w '%{http_code}\n'  # 422

# FR-009 — ghi chú quá dài
curl -s -X PATCH $API/documents/$DOC/highlights/$HL -H "Authorization: Bearer $TOKEN" \
  -H 'Content-Type: application/json' \
  -d "{\"note\":\"$(head -c 2001 /dev/zero | tr '\0' 'a')\"}" -w '%{http_code}\n'   # 422
```

---

## 4. Kiểm trên giao diện

Cần một document `status = published` đã có EPUB (qua luồng LDMS-002 → 003 → 004 → 007).

1. Đăng nhập, mở `/reader/<document_id>`.
2. **AC 1** — bôi đen một đoạn → menu nổi hiện ra → bấm đánh dấu → đoạn được tô ngay. F5 → highlight còn nguyên đúng chỗ.
3. **AC 2** — bấm vào highlight (hoặc chọn trong sidebar) → nhập ghi chú → lưu. F5 → mở lại → ghi chú còn nguyên văn.
4. **AC 3** — xóa highlight → mất khỏi trang ngay. F5 → không quay lại.
5. **FR-004** — bôi đen một đoạn nằm *bên trong* highlight đã có rồi tạo tiếp → cả hai cùng tồn tại, phần giao đậm hơn. Xóa cái ngoài → cái trong còn nguyên kèm ghi chú.
6. **FR-014** — bấm `A+`/`A−` đổi cỡ chữ → highlight vẫn bám đúng đoạn văn cũ, không trôi.
7. **FR-005b** — thử kéo chọn vượt hết một chương: ở chế độ `flow: 'scrolled-doc'` mỗi chương nằm trong iframe riêng nên selection tự dừng ở ranh giới chương. Không kéo qua được là **đúng thiết kế** (R3), không phải lỗi.

**Kiểm FR-011 (vị trí hỏng)** — cần cố ý phá:

1. Tạo vài highlight, ghi chú đầy đủ.
2. Chạy lại luồng publish để sinh EPUB mới có cấu trúc chương khác (hoặc thay `epub_object_key` sang một EPUB khác để mô phỏng nhanh).
3. Mở lại Reader. Kỳ vọng: highlight nào không dựng được rơi xuống mục "Đánh dấu không còn định vị được", **kèm nguyên ghi chú**, và xóa được từ đó. Không bản ghi nào bị mất (SC-008).

---

## 5. Chạy test và lint trước khi mở PR

Story này là bản pick chính thức đủ AC → Nguyên tắc III áp dụng đầy đủ, và CI gate PR vào `develop` bất kể sao.

```bash
cd src/backend
uv run ruff format .
uv run ruff check .
uv run pytest

cd ../frontend
npm run format
npm run lint
npm test
```
