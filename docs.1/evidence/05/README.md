# BẰNG CHỨNG NỘP KÈM — CÂU 5: KIẾN TRÚC PHẦN MỀM (SOFTWARE ARCHITECTURE)

**Mã câu hỏi:** `CÂU-05` | **Chủ đề:** Software Architecture

## 1. Đề bài và Yêu cầu nộp kèm từ Đề thi vấn đáp

> Trình bày quá trình hình thành và phương pháp đánh giá tài liệu Kiến trúc phần mềm (Software Architecture) của nhóm. _(Sinh viên nộp kèm bản in tài liệu Kiến trúc phần mềm của nhóm.)_

## 2. Danh mục tài liệu / bằng chứng cần nộp kèm khi thi

| STT | Tên tài liệu / Bằng chứng nộp kèm                                       | Loại tài liệu    | Nguồn tệp Markdown                                                   | Nguồn tệp PDF / Ảnh chụp                                                | Mô tả chi tiết                                                                                                                            |
| :-: | ----------------------------------------------------------------------- | ---------------- | -------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
|  1  | **Bản in tài liệu Kiến trúc phần mềm (Software Architecture Document)** | `Tài liệu in A4` | [05-software-architecture.md](docs.1/md/05-software-architecture.md) | [05-software-architecture.pdf](docs.1/pdf/05-software-architecture.pdf) | Tài liệu kiến trúc C4 Model, Tech Stack, sơ đồ tuần tự Upload/OCR, mô hình bảo mật JWT/RBAC/Presigned URL và 10 quyết định kiến trúc ADR. |

## 3. Các bằng chứng & số liệu then chốt cần chỉ ra trên tài liệu

- **Mô hình C4:** Context Diagram (Hệ thống trong môi trường ĐH KHTN), Container Diagram (Frontend Next.js, API FastAPI, PostgreSQL, MinIO, Redis).
- **Tech Stack:** Backend Python FastAPI, Frontend React/Next.js, Worker Celery/Redis, OCR Tesseract, Storage MinIO (S3-compatible).
- **Bảo mật:** Xác thực JWT token, phân quyền RBAC ở máy chủ, bảo vệ tệp EPUB bằng Presigned URLs có hạn ngạch ngắn.
- **10 Quyết định kiến trúc ADR (ADR-01 đến ADR-10) giải thích lý do lựa chọn công nghệ.:**

## 4. Khung hướng dẫn trả lời vấn đáp (WHAT — HOW — WHY — EVIDENCE)

- **WHAT (Khái niệm & Nội dung):** Bản thiết kế cấu trúc hệ thống, phân rã thành phần, giao tiếp giữa các module và cơ chế bảo mật.
- **HOW (Quy trình thực hiện):** Phân tích NFR từ SRS → Lựa chọn Tech Stack phù hợp → Vẽ mô hình C4 → Thiết kế sơ đồ tuần tự và bảo mật → Ghi nhận ADR.
- **WHY (Lý do & Giá trị):** Đảm bảo tính mở rộng, hiệu năng, bảo mật và tính khả thi trong việc tích hợp nhiều thành phần phức tạp (OCR, EPUB, CSDL).
- **EVIDENCE (Minh chứng chỉ tay):** Chỉ vào Sơ đồ C4 Container (Mục 3) và Sơ đồ tuần tự Upload-OCR trong bản in Kiến trúc phần mềm.

## 5. Liên kết tệp nguồn và tài liệu liên quan

- [docs.1/md/05-software-architecture.md](../../md/05-software-architecture.md)
- [docs.1/md/A1-decision-log-and-adr.md](../../md/A1-decision-log-and-adr.md)
- [docs.1/pdf/05-software-architecture.pdf](../../pdf/05-software-architecture.pdf)
- [Phiếu ôn tập Câu 5 (final-exam/preparation/3_Architecture_PoC_Prototype/README.md)](../../../final-exam/preparation/3_Architecture_PoC_Prototype/README.md)
