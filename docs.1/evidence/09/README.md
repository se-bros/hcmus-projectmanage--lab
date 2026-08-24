# BẰNG CHỨNG NỘP KÈM — CÂU 9: ĐỊNH NGHĨA QUY TRÌNH PHÁT TRIỂN PHẦN MỀM (SOFTWARE PROCESS DEFINITION)

**Mã câu hỏi:** `CÂU-09` | **Chủ đề:** Software Process Definition

## 1. Đề bài và Yêu cầu nộp kèm từ Đề thi vấn đáp

> Trình bày quá trình hình thành và phương pháp đánh giá tài liệu Định nghĩa quy trình phát triển phần mềm (Software Process Definition) của nhóm. _(Sinh viên nộp kèm bản in tài liệu Định nghĩa quy trình phát triển phần mềm của nhóm.)_

## 2. Danh mục tài liệu / bằng chứng cần nộp kèm khi thi

| STT | Tên tài liệu / Bằng chứng nộp kèm                            | Loại tài liệu    | Tệp đính kèm tại thư mục này                                               | Nguồn tài liệu PDF                                                                 | Mô tả chi tiết                                                                                                                        |
| :-: | ------------------------------------------------------------ | ---------------- | -------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
|  1  | **Bản in tài liệu Định nghĩa quy trình phát triển phần mềm** | `Tài liệu in A4` | [09-software-process-definition.pdf](./09-software-process-definition.pdf) | [09-software-process-definition.pdf](../../pdf/09-software-process-definition.pdf) | Quy định quy trình Kanban 6 cột, chính sách giới hạn WIP (WIP Limits), quy tắc DoR / DoD và chiến lược nhánh Trunk-Based Development. |

## 3. Các bằng chứng & số liệu then chốt cần chỉ ra trên tài liệu

- **Bảng Kanban 6 cột:** Backlog → Ready → In Progress → In Review → Testing → Done.
- **WIP Limits nghiêm ngặt:** In Progress ≤ 3, In Review ≤ 2, Testing ≤ 2 nhằm tránh nghẽn luồng và tăng thông lượng.
- **Quy tắc chuyển cột:** Tiêu chí đầu vào DoR và tiêu chí hoàn thành DoD rõ ràng cho từng bước.
- **Chiến lược phân nhánh Trunk-Based Development:** Nhánh `main` luôn deploy được, nhánh tính năng tồn tại ngắn < 2 ngày.

## 4. Khung hướng dẫn trả lời vấn đáp (WHAT — HOW — WHY — EVIDENCE)

- **WHAT (Khái niệm & Nội dung):** Văn bản hóa toàn bộ quy chuẩn làm việc, luồng di chuyển công việc và quy tắc phối hợp kỹ thuật của đội ngũ phát triển.
- **HOW (Quy trình thực hiện):** Phân tích đặc thù dự án 11 tuần → Chọn mô hình Agile/Kanban kết hợp Trunk-Based → Thiết lập bảng 6 cột và WIP limits → Ban hành DoR/DoD → Tích hợp vào GitHub Project.
- **WHY (Lý do & Giá trị):** Chuẩn hóa cách làm việc, giảm thời gian lãng phí, phát hiện sớm điểm nghẽn và duy trì nhịp độ phát triển bền vững.
- **EVIDENCE (Minh chứng chỉ tay):** Chỉ vào Bảng Kanban 6 cột kèm WIP limits (Mục 3) và Quy tắc Trunk-Based (Mục 5) trong bản in Quy trình.

## 5. Liên kết tệp nguồn và tài liệu liên quan

- [Tài liệu Markdown (docs.1/md/09-software-process-definition.md)](../../md/09-software-process-definition.md)
- [Tài liệu PDF (docs.1/pdf/09-software-process-definition.pdf)](../../pdf/09-software-process-definition.pdf)
- [Phiếu ôn tập Câu 9 (final-exam/preparation/4_Estimation_Planning_Process/README.md)](../../../final-exam/preparation/4_Estimation_Planning_Process/README.md)
