# Cách dùng Spec-Kit trong dự án này

## Quy trình chuẩn (theo đúng thứ tự)

```
/speckit.constitution → /speckit.specify → /speckit.clarify → /speckit.plan
      → /speckit.tasks → /speckit.analyze → /speckit.checklist → /speckit.implement
```

## Từng bước

### 1. `/speckit.constitution`

Tạo/sửa nguyên tắc dự án tại `.specify/memory/constitution.md`. Dự án này **đã có sẵn** (v1.1.0) — chỉ cần dùng lệnh này khi muốn **sửa đổi** nguyên tắc (ví dụ thêm quy tắc mới, đổi tech stack).

```
/speckit.constitution Thêm nguyên tắc bắt buộc rate-limit cho API upload
```

### 2. `/speckit.specify "<mô tả feature>"`

Tạo branch mới (`00N-ten-feature`) + file `specs/00N-ten-feature/spec.md`. Đây là bước bắt đầu cho **mỗi feature mới**.

```
/speckit.specify Cho phép người dùng upload sách scan (PDF/ảnh) và hệ thống tự OCR ra EPUB
```

→ Sinh ra user stories (P1/P2/P3...), edge cases, functional requirements (FR-00X), success criteria (SC-00X). **Không** chứa chi tiết kỹ thuật (đó là việc của `/speckit.plan`).

### 3. `/speckit.clarify`

Rà lại `spec.md` vừa tạo, hỏi bạn từng câu để vá các chỗ mơ hồ (`[NEEDS CLARIFICATION]`, số liệu chưa đo được...). Chạy trước khi plan để tránh assumption sai lan sang các bước sau.

```
/speckit.clarify
```

### 4. `/speckit.plan`

Sinh `plan.md` + `research.md` + `data-model.md` + `contracts/` + `quickstart.md`. Có **Constitution Check** — đối chiếu với `constitution.md` (đặc biệt Principle IV — bảo mật file/MinIO signed URL là non-negotiable dù đang MVP).

```
/speckit.plan
```

Có thể thêm ràng buộc riêng: `/speckit.plan Dùng Tesseract cho OCR, chạy qua BackgroundTasks`

### 5. `/speckit.tasks`

Sinh `tasks.md` — danh sách task chia theo user story, có thứ tự phụ thuộc (Setup → Foundational → US1 → US2 → US3 → Polish), đánh dấu `[P]` cho task chạy song song được.

```
/speckit.tasks
```

### 6. `/speckit.analyze`

Đối chiếu chéo spec/plan/tasks — tìm requirement không có task tương ứng, task mồ côi, vi phạm constitution, mâu thuẫn thuật ngữ. **Chỉ đọc, không tự sửa** — sẽ hỏi bạn trước khi sửa gì.

```
/speckit.analyze
```

### 7. `/speckit.checklist "<loại>"` (tùy chọn)

Sinh checklist review riêng cho 1 khía cạnh (bảo mật, UX, chất lượng requirement...).

```
/speckit.checklist security checklist cho luồng upload/OCR
```

### 8. `/speckit.implement`

Thực thi `tasks.md` theo đúng thứ tự phase, dừng lại báo checkpoint sau mỗi user story để bạn xác nhận trước khi làm story tiếp theo. Tự tuân theo Definition of Done trong `CLAUDE.md` (lint/format/test) và constitution khi code.

```
/speckit.implement
/speckit.implement chỉ làm User Story 1
```

## Lưu ý

- Mỗi feature = 1 lần `/speckit.specify` → 1 branch mới `specs/00N-ten/`. Không chạy lại `/speckit.specify` cho cùng 1 feature.
- Có thể bỏ qua `/speckit.clarify`, `/speckit.analyze`, `/speckit.checklist` nếu feature đơn giản — chỉ `specify → plan → tasks → implement` là đủ chạy được.
- Toàn bộ file sinh ra nằm trong `specs/<branch>/` — xem lại bất cứ lúc nào bằng cách đọc trực tiếp, không cần chạy lại lệnh.
