# BẰNG CHỨNG NỘP KÈM — CÂU 6: CHỨNG MINH Ý TƯỞNG (PROOF OF CONCEPT)

**Mã câu hỏi:** `CÂU-06` | **Chủ đề:** Proof of Concept (PoC)

## 1. Đề bài và Yêu cầu nộp kèm từ Đề thi vấn đáp

> Trình bày quá trình hình thành và phương pháp đánh giá sản phẩm Chứng minh ý tưởng (Proof of Concept) của nhóm. _(Sinh viên nộp kèm bản in giao diện thể hiện đầu vào và đầu ra khi chạy mã nguồn Chứng minh ý tưởng của nhóm.)_

## 2. Danh mục tài liệu / bằng chứng cần nộp kèm khi thi

| STT | Tên tài liệu / Bằng chứng nộp kèm                                                               | Loại tài liệu                 | Nguồn tệp Markdown                                                         | Nguồn tệp PDF / Ảnh chụp                                                     | Mô tả chi tiết                                                                                                                     |
| :-: | ----------------------------------------------------------------------------------------------- | ----------------------------- | -------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
|  1  | **Bản in giao diện thể hiện đầu vào và đầu ra khi chạy mã nguồn PoC 1 (OCR tiếng Việt)**        | `Bản in giao diện / Ảnh chụp` | [README.md](final-exam/preparation/3_Architecture_PoC_Prototype/README.md) | [README.pdf](final-exam/preparation/3_Architecture_PoC_Prototype/README.pdf) | Ảnh chụp Input (Ảnh scan/PDF giáo trình mẫu) và Output (Văn bản tiếng Việt có dấu trích xuất kèm điểm số confidence).              |
|  2  | **Bản in giao diện thể hiện đầu vào và đầu ra khi chạy mã nguồn PoC 2 (Trình đọc EPUB Reader)** | `Bản in giao diện / Ảnh chụp` | [README.md](final-exam/preparation/3_Architecture_PoC_Prototype/README.md) | [README.pdf](final-exam/preparation/3_Architecture_PoC_Prototype/README.pdf) | Ảnh chụp Input (Tệp EPUB số hóa) và Output (Trình đọc ePub.js render nội dung mượt mà, phân trang, không lộ direct download link). |

## 3. Các bằng chứng & số liệu then chốt cần chỉ ra trên tài liệu

- **PoC 1 (OCR Engine):** Đánh giá Tesseract 5 với bộ ngôn ngữ vie.traineddata, xử lý tiền xử lý ảnh (Deskew, Binarization) đạt độ chính xác > 85%.
- **PoC 2 (EPUB Reader Web):** Đánh giá thư viện ePub.js, stream dữ liệu từ MinIO qua Presigned URL, ngăn chặn hành vi tải tệp gốc.
- **Tiêu chí nghiệm thu PoC:** Thời gian xử lý < 30s/trang, tiêu tốn RAM < 512MB.

## 4. Khung hướng dẫn trả lời vấn đáp (WHAT — HOW — WHY — EVIDENCE)

- **WHAT (Khái niệm & Nội dung):** Thực nghiệm kỹ thuật quy mô nhỏ nhằm kiểm chứng các rủi ro công nghệ lớn nhất trước khi xây dựng toàn hệ thống.
- **HOW (Quy trình thực hiện):** Nhận diện 2 rủi ro kỹ thuật cao nhất (OCR & EPUB Reader) → Xây dựng mã nguồn PoC độc lập → Chạy thử nghiệm với dữ liệu mẫu → Đo lường kết quả → Đánh giá Go/No-go.
- **WHY (Lý do & Giá trị):** Giảm thiểu rủi ro kiến trúc thất bại ở giai đoạn muộn của dự án.
- **EVIDENCE (Minh chứng chỉ tay):** Chỉ vào Ảnh chụp Input/Output của PoC OCR và PoC EPUB Reader.

## 5. Liên kết tệp nguồn và tài liệu liên quan

- [Phiếu ôn tập Câu 6 (final-exam/preparation/3_Architecture_PoC_Prototype/README.md)](../../../final-exam/preparation/3_Architecture_PoC_Prototype/README.md)
- [docs.1/md/05-software-architecture.md](../../md/05-software-architecture.md)
