# BIÊN BẢN NGHIỆM THU NGƯỜI DÙNG (UAT FEEDBACK RECORD)
## Dự án: Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS (HCMUS-LDMS)
### Mã tài liệu: `HCMUS-LDMS-UAT-01`

---

| Thông tin nghiệm thu | Chi tiết |
| :--- | :--- |
| **Khách hàng / Đại diện người dùng:** | **Cô Nguyễn Thị Mai** — Chuyên viên Thư viện Trường ĐH KHTN |
| **Đơn vị tiếp nhận:** | Thư viện Trường Đại học Khoa học Tự nhiên, ĐHQG-HCM |
| **Đại diện Nhóm dự án:** | **Mạch Quốc Tấn** (PM) & **Nguyễn Tuấn Anh** (DevOps/QA Lead) |
| **Thời gian thực hiện:** | 16/08/2026 — 09:30 đến 11:30 |
| **Địa điểm:** | Phòng Nghiệp vụ Thư viện, Cơ sở 227 Nguyễn Văn Cừ, Quận 5 |
| **Môi trường nghiệm thu:** | Staging Environment (`https://ldms-staging.hcmus.edu.vn`) |

---

## 1. Kết quả Đánh giá Kịch bản Nghiệm thu (Test Scenarios)

| Mã | Kịch bản kiểm thử (User Scenario) | Tiêu chí chấp nhận (Acceptance Criteria) | Kết quả | Đánh giá của Thủ thư Mai |
| :---: | :--- | :--- | :---: | :--- |
| **UAT-01** | Tải lên tài liệu scan gốc dạng PDF (Sách Giáo trình Giải tích 1) | File tải lên thành công, tạo job OCR tự động trong Celery queue | **ĐẠT** (5/5) | _"Giao diện kéo thả file rất mượt, thanh tiến trình hiển thị rõ ràng từng trang."_ |
| **UAT-02** | Đối soát văn bản OCR trên màn hình **Split-screen Editor** | Màn hình chia đôi: ảnh gốc bên trái, văn bản OCR bên phải; sửa lỗi chính tả trực tiếp | **ĐẠT** (5/5) | _"Tính năng này rất hữu ích cho thủ thư khi xử lý sách cũ bị ố vàng, không phải mở 2 tab riêng biệt."_ |
| **UAT-03** | Tìm kiếm Full-Text Search (FTS) tiếng Việt | Tìm kiếm từ khóa chính xác có dấu/không dấu, highlight kết quả trong trích đoạn | **ĐẠT** (4.5/5) | _"Tốc độ tìm kiếm rất nhanh, kết quả trả về tức thì dưới 1 giây."_ |
| **UAT-04** | Đọc tài liệu trên Web Reader & Highlight/Ghi chú cá nhân | Mở sách EPUB, tô màu đoạn văn, thêm note ghi chú và lưu lại khi load lại trang | **ĐẠT** (4.5/5) | _"Sinh viên đọc tài liệu sẽ rất thích phần highlight và bookmark trang đang đọc."_ |
| **UAT-05** | Kiểm tra An toàn & Bản quyền tài liệu (DRM) | Không cho phép copy link tải trực tiếp; link đọc sách MinIO hết hạn sau 15 phút | **ĐẠT** (4.0/5) | _"Cần bổ sung thêm Watermark mờ tên sinh viên lên từng trang để chống chụp màn hình."_ |

---

## 2. Tổng hợp Điểm Đánh giá Mức độ Hài lòng (Customer Satisfaction)

| Tiêu chí chất lượng (ISO 9126) | Điểm số (Thang 5) | Nhận xét chi tiết |
| :--- | :---: | :--- |
| **1. Tính đúng đắn & Đầy đủ chức năng (Functionality)** | **4.8 / 5.0** | Đáp ứng vượt mong đợi so với quy trình thủ công trước đây. |
| **2. Độ tin cậy & Ổn định (Reliability)** | **4.6 / 5.0** | Không phát sinh lỗi crash hệ thống trong suốt 2 giờ thử nghiệm. |
| **3. Tính dễ sử dụng (Usability)** | **4.7 / 5.0** | Giao diện tiếng Việt thân thiện, bố cục rõ ràng, dễ thao tác. |
| **4. Hiệu năng & Tốc độ phản hồi (Efficiency)** | **4.5 / 5.0** | Tốc độ FTS và tải trang nhanh chóng. |
| **5. Tính bảo mật dữ liệu (Security)** | **4.4 / 5.0** | Phân quyền Thủ thư - Giảng viên - Sinh viên chặt chẽ. |
| **ĐIỂM ĐÁNH GIÁ TRUNG BÌNH TỔNG THỂ** | **4.6 / 5.0** | **XẾP LOẠI: XUẤT SẮC** |

---

## 3. Ý kiến Đóng góp Cải tiến (Feedback for Future Iterations)

1. **Gợi ý 1:** Bổ sung tính năng chèn Watermark động chứa MSSV và Họ tên sinh viên khi mở sách để tăng cường bảo vệ quyền tác giả.
2. **Gợi ý 2:** Cho phép xuất báo cáo thống kê số lượt đọc sách theo từng khoa/ngành để phục vụ công tác kiểm định chất lượng giáo dục.

---

## 4. Kết luận Nghiệm thu

- Đại diện Thư viện **ĐỒNG Ý NGHIỆM THU** phiên bản v1.0 của Hệ thống HCMUS-LDMS.
- Hệ thống đủ điều kiện để triển khai thử nghiệm thực tế (Pilot Phase) tại Thư viện trường trong học kỳ tới.

<br>

| ĐẠI DIỆN KHÁCH HÀNG (THƯ VIỆN) | ĐẠI DIỆN TRƯỞNG NHÓM PHÁT TRIỂN (PM) |
| :---: | :---: |
| *(Ký và ghi rõ họ tên)* | *(Ký và ghi rõ họ tên)* |
| <br><br>**Nguyễn Thị Mai** | <br><br>**Mạch Quốc Tấn** |
