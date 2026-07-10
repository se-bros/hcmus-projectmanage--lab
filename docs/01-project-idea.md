# PROJECT IDEA

## Hệ thống Quản lý Số hóa Thư viện (LibDMS)

**Thư viện hiện đại & Ban Công nghệ Thông tin**

Phiên bản 1.0 • Tháng 7/2026 • One-pager trước khi đầu tư viết Project Proposal

## Mục lục

* [1. Tên ý tưởng](#tên-ý-tưởng)
* [2. Nguồn gốc (Origin)](#nguồn-gốc-origin)
* [3. Vấn đề/Cơ hội](#vấn-đềcơ-hội)
* [4. Đối tượng hưởng lợi dự kiến](#đối-tượng-hưởng-lợi-dự-kiến)
* [5. Giá trị cốt lõi (Core Value Proposition)](#giá-trị-cốt-lõi-core-value-proposition)
* [6. Giả định cần kiểm chứng (Assumptions to validate)](#giả-định-cần-kiểm-chứng-assumptions-to-validate)
* [7. Mức độ ưu tiên/khẩn cấp sơ bộ](#mức-độ-ưu-tiênkhẩn-cấp-sơ-bộ)
* [8. Bước tiếp theo đề xuất (Next Step)](#bước-tiếp-theo-đề-xuất-next-step)

---

## Tên ý tưởng

**Hệ thống Quản lý Số hóa Thư viện (Library Digitization Management System - LibDMS)**

## Nguồn gốc (Origin)

Đề xuất phối hợp giữa **Bộ phận Quản lý Thư viện** và **Phòng Công nghệ Thông tin**, xuất phát từ nhu cầu tối ưu hóa và hiện đại hóa quy trình nghiệp vụ số hóa, lưu trữ và cung cấp tài liệu số tới bạn đọc (không phải RFP bên ngoài).

## Vấn đề/Cơ hội

- **Thách thức:** Kho tài liệu giấy, sách, báo cáo chuyên đề và tài liệu tham khảo vật lý đang chiếm không gian lớn, dễ bị ẩm mốc, xuống cấp. Quy trình lưu kho và cho mượn truyền thống tốn nhiều nhân lực.
- **Hạn chế:** Bạn đọc gặp khó khăn khi tiếp cận tài liệu từ xa, đặc biệt là các tài liệu quý hiếm hoặc bản gốc độc bản.
- **Cơ hội:** Việc xây dựng một hệ thống số hóa tự động chuyển đổi tài liệu thô (ảnh scan, PDF, JPEG, v.v.) sang định dạng sách điện tử chuẩn (EPUB) kết hợp công nghệ OCR tiếng Việt sẽ mở rộng khả năng tiếp cận tri thức 24/7, tối ưu hóa diện tích kho bãi vật lý và hiện đại hóa trải nghiệm đọc.

## Đối tượng hưởng lợi dự kiến

- **Cán bộ thư viện (Librarian):** Tự động hóa luồng chuyển đổi số từ scan sang EPUB, quản lý danh mục (category) và thẻ (tag) khoa học, tối ưu hóa theo dõi mượn/trả.
- **Bạn đọc (Reader):** Đọc tài liệu trực tuyến (EPUB Reader), tìm kiếm toàn văn thông minh, tra cứu nhanh chóng mọi lúc mọi nơi.
- **Ban quản trị (Admin):** Quản lý phân quyền người dùng (RBAC), báo cáo thống kê hiệu suất sử dụng tài liệu phục vụ hoạch định ngân sách.

## Giá trị cốt lõi (Core Value Proposition)

Chuyển đổi quy trình số hóa thủ công đơn lẻ thành một **chu trình khép kín tự động**: Nhập tài liệu (PDF, PNG, JPEG, scan) → OCR → Tạo file EPUB → Quản lý & Cấp phát tài liệu theo vai trò → Đọc trực tuyến & Tra cứu thông minh.

## Giả định cần kiểm chứng (Assumptions to validate)

- Chất lượng của công cụ OCR tiếng Việt nguồn mở (Tesseract) đủ tốt để chuyển đổi các bản scan chất lượng thấp sang text reflowable của EPUB mà không tốn quá nhiều công biên tập lại.
- Bạn đọc có xu hướng thích đọc định dạng EPUB linh hoạt trên thiết bị di động hơn là file PDF cố định trang.
- Quy chế bản quyền của thư viện cho phép lưu hành nội bộ hoặc công khai các tài liệu sau khi số hóa.

## Mức độ ưu tiên/khẩn cấp sơ bộ

**Mức độ ưu tiên:** Cao. Dự án nằm trong kế hoạch nâng cấp hạ tầng số của thư viện, cần nhanh chóng xây dựng phiên bản MVP để chạy thử nghiệm quy trình số hóa và chức năng đọc trực tuyến trước khi mở rộng quy mô toàn bộ tài nguyên thư viện.

## Bước tiếp theo đề xuất (Next Step)

Tiến hành viết **Project Proposal** đầy đủ (xem [02-project-proposal.md](file:///d:/Project/hcmus-projectmanage--lab/docs/02-project-proposal.md)) — xác định chi tiết Business Goals, phân loại Stakeholder, ngân sách ước tính và thiết kế sơ bộ hệ thống.
