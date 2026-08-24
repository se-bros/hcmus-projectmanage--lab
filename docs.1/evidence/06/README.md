# BẰNG CHỨNG NỘP KÈM — CÂU 6: CHỨNG MINH Ý TƯỞNG (PROOF OF CONCEPT)

**Mã câu hỏi:** `CÂU-06` | **Chủ đề:** Proof of Concept (PoC)

## 1. Đề bài và Yêu cầu nộp kèm từ Đề thi vấn đáp

> Trình bày quá trình hình thành và phương pháp đánh giá sản phẩm Chứng minh ý tưởng (Proof of Concept) của nhóm. _(Sinh viên nộp kèm bản in giao diện thể hiện đầu vào và đầu ra khi chạy mã nguồn Chứng minh ý tưởng của nhóm.)_

## 2. Danh mục tài liệu / bằng chứng cần nộp kèm khi thi

| STT | Tên tài liệu / Bằng chứng nộp kèm                                           | Loại tài liệu          | Tệp đính kèm tại thư mục này                               | Nguồn tài liệu PDF | Mô tả chi tiết                                                                                                          |
| :-: | --------------------------------------------------------------------------- | ---------------------- | ---------------------------------------------------------- | ------------------ | ----------------------------------------------------------------------------------------------------------------------- |
|  1  | **Bản in giao diện đầu vào/đầu ra PoC 1 (OCR tiếng Việt) và MinIO Storage** | `Ảnh chụp thực nghiệm` | [poc1_split-screen-view.png](./poc1_split-screen-view.png) | N/A                | Tập hợp 8 ảnh chụp màn hình thực nghiệm PoC 1: input scan, xử lý OCR, kết quả trích xuất văn bản và lưu trữ MinIO.      |
|  2  | **Bản in giao diện đầu vào/đầu ra PoC 2 (Trình đọc EPUB Reader & Stream)**  | `Ảnh chụp thực nghiệm` | [poc2_epub-exported.png](./poc2_epub-exported.png)         | N/A                | Tập hợp 5 ảnh chụp màn hình thực nghiệm PoC 2: đóng gói EPUB, stream dữ liệu qua presigned URL 900s và hiển thị reader. |
|  3  | **Ảnh chụp kết quả chạy kiểm thử tự động PoC (Pytest Pass)**                | `Ảnh chụp console`     | [test-passed.png](./test-passed.png)                       | N/A                | Minh chứng toàn bộ unit tests kiểm chứng PoC chạy thành công 100%.                                                      |

## 3. Các bằng chứng & số liệu then chốt cần chỉ ra trên tài liệu

- **PoC 1 (OCR Engine):** Đánh giá Tesseract 5 với bộ ngôn ngữ `vie.traineddata`, xử lý tiền xử lý ảnh đạt độ chính xác > 85%.
- **PoC 2 (EPUB Reader Web):** Đánh giá thư viện ePub.js, stream dữ liệu từ MinIO qua Presigned URL 900s.
- **Tiêu chí nghiệm thu PoC:** Thời gian xử lý < 30s/trang, RAM < 512MB, không lộ direct download link.

## 4. Khung hướng dẫn trả lời vấn đáp (WHAT — HOW — WHY — EVIDENCE)

- **WHAT (Khái niệm & Nội dung):** Thực nghiệm kỹ thuật quy mô nhỏ nhằm kiểm chứng các rủi ro công nghệ lớn nhất trước khi xây dựng toàn hệ thống.
- **HOW (Quy trình thực hiện):** Nhận diện 2 rủi ro kỹ thuật cao nhất (OCR & EPUB Reader) → Xây dựng mã nguồn PoC độc lập → Chạy thử nghiệm với dữ liệu mẫu → Đo lường kết quả → Đánh giá Go/No-go.
- **WHY (Lý do & Giá trị):** Giảm thiểu rủi ro kiến trúc thất bại ở giai đoạn muộn của dự án.
- **EVIDENCE (Minh chứng chỉ tay):** Chỉ vào Ảnh chụp Input/Output của PoC OCR và PoC EPUB Reader trong thư mục evidence.

## 5. Liên kết tệp nguồn và tài liệu liên quan

- [Mục 8 PoC trong Kiến trúc phần mềm (docs.1/md/05-software-architecture.md)](../../md/05-software-architecture.md)
- [Phiếu ôn tập Câu 6 (final-exam/preparation/3_Architecture_PoC_Prototype/README.md)](../../../final-exam/preparation/3_Architecture_PoC_Prototype/README.md)
