---
name: DocToPdfGenerator
description: Triggers when the user requests to write, create, update, or design any document, proposal, report, charter, idea, or specification, and requires generating both a markdown (.md) and a PDF (.pdf) file.
---

# Hướng dẫn tạo tài liệu đồng thời dưới dạng Markdown và PDF

Khi người dùng yêu cầu viết, tạo, cập nhật hoặc biên soạn một tài liệu nào đó (ví dụ: báo cáo, đề xuất dự án, điều lệ dự án, kiến trúc hệ thống, hoặc bất kỳ tài liệu đặc tả nào), hãy thực hiện quy trình sau:

## Quy trình Thực hiện

1. **Khởi tạo và chỉnh sửa file Markdown (.md):**
   * Viết nội dung tài liệu đầy đủ, chuyên nghiệp, nghiêm túc bằng định dạng Markdown (.md) tại đường dẫn yêu cầu.
   * **Bắt buộc có Mục lục (Table of Contents):** Ngay dưới tiêu đề chính và thông tin phiên bản của tài liệu, phải chèn một phần **## Mục lục** chứa các liên kết nhảy (anchor links) đến các đề mục chính trong tài liệu để người đọc dễ dàng định vị nhanh thông tin.
   * **Quy chuẩn thiết kế và chèn Sơ đồ/Hình ảnh:**
     * **Sử dụng định dạng Vector SVG:** Tất cả các sơ đồ (ví dụ: Mermaid) phải được biên dịch sang định dạng vector SVG (`.svg`) thay vì PNG để khi nhúng vào tài liệu PDF sẽ hiển thị rõ nét tuyệt đối ở mọi mức độ phóng to (zoom). Biên dịch bằng lệnh: `npx @mermaid-js/mermaid-cli -i <so_do.mmd> -o <anh_so_do.svg>`.
     * **Khắc phục chồng chéo chữ (đặc biệt là biểu đồ Gantt):** Khi thiết kế biểu đồ Gantt bằng Mermaid, bắt buộc phải thêm directive khởi tạo ở dòng đầu tiên của file `.mmd` để nới rộng không gian hiển thị nhãn công việc: `%%{init: { 'gantt': { 'leftPadding': 180 } } }%%`. Ngoài ra, nhãn công việc phải viết ngắn gọn, cô đọng để không tràn lề.
     * **Cấm sử dụng sơ đồ ASCII hardcode:** Tuyệt đối không vẽ sơ đồ trực quan bằng các ký tự văn bản thô sơ (như `├──`, `└──`, mũi tên `│` `▼` trong khối code code block). Tất cả phải được thiết kế bằng mã Mermaid/PlantUML chuyên nghiệp, biên dịch ra file hình ảnh vector SVG rồi chèn liên kết hình ảnh vào tài liệu.
   * Đảm bảo cấu trúc tài liệu rõ ràng, sử dụng các tiêu đề (`#`, `##`, `###`), danh sách, bảng biểu và sơ đồ (Mermaid) phù hợp.

2. **Biên dịch sang PDF (.pdf):**
   * Ngay sau khi hoàn thành hoặc cập nhật file `.md`, hãy chạy lệnh sau trong terminal thông qua công cụ `run_command` để tự động tạo file PDF tương ứng trong cùng thư mục bằng tập lệnh Python đi kèm của Skill:
     ```bash
     python g:/HCMUS/NAM3-HK3/Management/Lab/W5/.agents/skills/doc_generator/scripts/md_to_pdf.py <path_to_markdown_file.md> <path_to_pdf_file.pdf>
     ```
     *(Ví dụ: nếu file markdown là `docs/01-project-idea.md`, lệnh biên dịch sẽ là `python g:/HCMUS/NAM3-HK3/Management/Lab/W5/.agents/skills/doc_generator/scripts/md_to_pdf.py docs/01-project-idea.md docs/01-project-idea.pdf`)*
   * Đảm bảo đường dẫn đích hoàn toàn trùng khớp với file markdown gốc, chỉ thay đổi phần mở rộng từ `.md` sang `.pdf`.

3. **Xác nhận và báo cáo:**
   * Sau khi biên dịch thành công, kiểm tra xem file PDF đã được tạo chưa bằng cách sử dụng `list_dir` hoặc kiểm tra nhật ký chạy lệnh.
   * Thông báo rõ ràng cho người dùng về cả hai tệp tin đã được tạo/cập nhật (kèm theo đường dẫn liên kết nhấp chuột được `file://` cho cả hai tệp `.md` và `.pdf`).
