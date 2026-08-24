# BIÊN BẢN HỌP NHÓM — RÚT RA BÀI HỌC KINH NGHIỆM

## (MEETING MINUTES — LESSONS LEARNED & SPRINT RETROSPECTIVE)

### Dự án: Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS (HCMUS-LDMS)

---

### THÔNG TIN QUẢN TRỊ BIÊN BẢN (DOCUMENT CONTROL)

| Trường thông tin               | Nội dung chi tiết                                                     |
| ------------------------------ | --------------------------------------------------------------------- |
| **Mã biên bản (Document ID):** | `HCMUS-LDMS-MM02`                                                     |
| **Tên biên bản:**              | Biên bản Họp Rút ra Bài học Kinh nghiệm & Tổng kết Dự án              |
| **Thời gian họp:**             | 15:15 – 17:00, Thứ Bảy ngày 22/08/2026                                |
| **Hình thức / Địa điểm:**      | Kênh thoại Discord server `SE Bros` kết hợp Không gian sinh hoạt nhóm |
| **Chủ tọa (Meeting Chair):**   | **Mạch Quốc Tấn** (Project Manager)                                   |
| **Thư ký (Secretary):**        | **Ân Tiến Nguyên An**                                                 |
| **Thành phần tham dự:**        | Đầy đủ 6/6 thành viên nhóm Sebros                                     |

---

### DANH SÁCH THÀNH VIÊN THAM DỰ

| STT | Họ và tên thành viên      | Mã số sinh viên | Vai trò trong dự án                           | Tình trạng tham dự |
| :-: | ------------------------- | :-------------: | --------------------------------------------- | :----------------: |
|  1  | **Mạch Quốc Tấn**         |   `23127115`    | Trưởng nhóm / Quản lý dự án (Project Manager) |   Có mặt (15:15)   |
|  2  | **Ngô Nguyễn Thế Khoa**   |   `23127065`    | Frontend Lead / Kỹ sư giao diện & OCR         |   Có mặt (15:15)   |
|  3  | **Ân Tiến Nguyên An**     |   `23127048`    | DevOps & QA / Kiến trúc phần mềm & Tài liệu   |   Có mặt (15:15)   |
|  4  | **Nguyễn Lê Hồ Anh Khoa** |   `23127211`    | Kỹ sư Frontend & Trải nghiệm người dùng (UX)  |   Có mặt (15:15)   |
|  5  | **Nguyễn Quang Thái**     |   `23127116`    | Kỹ sư Backend & Phân tích Yêu cầu             |   Có mặt (15:15)   |
|  6  | **Nguyễn Tuấn Anh**       |   `23127152`    | Technical Lead / Kỹ sư Hệ thống & Kiểm thử    |   Có mặt (15:15)   |

---

## 1. Mục đích & Chương trình cuộc họp (Meeting Objectives & Agenda)

1. **Mục đích cuộc họp:**
   - Đánh giá, tổng kết toàn diện quá trình thực hiện dự án môn học Quản lý Dự án Phần mềm qua 11 tuần triển khai.
   - Lắng nghe ý kiến tự đánh giá (Self-reflection), ghi nhận các khó khăn, vướng mắc thực tế của từng cá nhân.
   - Phân tích nguyên nhân gốc rễ (Root Cause Analysis) và đúc kết bài học kinh nghiệm sâu sắc.
   - Thống nhất các hành động cải tiến để chuẩn bị hoàn thiện toàn bộ hồ sơ bằng chứng nộp kèm cho kỳ thi vấn đáp cuối kỳ.

2. **Chương trình nghị sự:**
   - `15:15 – 15:25`: Chủ tọa khai mạc, nêu mục tiêu và nguyên tắc Retrospective (Blameless - Không đổ lỗi, tập trung vào giải pháp và cải tiến).
   - `15:25 – 16:30`: Từng thành viên lần lượt trình bày khó khăn, bài học và đề xuất.
   - `16:30 – 16:50`: Thảo luận nhóm, phản biện và chuẩn hóa bài học kinh nghiệm chung.
   - `16:50 – 17:00`: Chủ tọa tổng kết, thông qua nghị quyết và phân công cập nhật tài liệu.

---

## 2. Ý kiến phản hồi & Đánh giá chi tiết của từng thành viên

### 2.1. Ngô Nguyễn Thế Khoa (Frontend Lead)

- **Vấn đề / Khó khăn:** Không có nhiều vấn đề kỹ thuật lớn phát sinh trong phạm vi phụ trách. Các luồng xử lý giao diện biên tập OCR và tích hợp kho MinIO Storage được triển khai ổn định theo đúng thiết kế ban đầu.
- **Bài học rút ra:** Việc xây dựng sớm mã nguồn PoC độc lập ở tuần đầu đã giúp loại bỏ hầu hết rủi ro tích hợp thư viện xử lý ảnh ở giai đoạn sau.

### 2.2. Nguyễn Tuấn Anh (Technical Lead)

- **Vấn đề phát sinh:** Các sản phẩm (tài liệu và cấu hình) ban đầu của Tuấn Anh chưa đạt chất lượng cao khi đưa ra cho các thành viên trong nhóm review chéo.
- **Phân tích nguyên nhân:** Quá trình sử dụng AI hỗ trợ soạn thảo gặp tình trạng prompt thiếu kiến thức chuyên sâu của bài toán và thiếu ngữ cảnh (context) đầy đủ của hệ thống, dẫn đến AI sinh ra nội dung chung chung (generic), chưa bám sát nghiệp vụ thực tế của dự án thư viện.
- **Hành động khắc phục & Bài học rút ra:**
  - Khi prompt cho AI, bắt buộc phải cung cấp đầy đủ tài liệu ngữ cảnh, đặc tả chi tiết và các ràng buộc cụ thể để tránh mất nhiều thời gian sửa chữa về sau.
  - Phải luôn chủ động rà soát, đối chiếu kỹ lưỡng sản phẩm của AI với các tài liệu và quy chuẩn chính thức của môn học trước khi submit cho nhóm.

### 2.3. Ân Tiến Nguyên An (DevOps & QA)

- **Vấn đề phát sinh:** Tốn rất nhiều thời gian để xác định khi nào một tài liệu đạt độ hoàn chỉnh, đúng chuẩn cấu trúc và đáp ứng đầy đủ rubric đánh giá của giảng viên.
- **Phân tích nguyên nhân & Giải pháp:** Trước đây việc tự đánh giá còn mang tính chủ quan, thiếu công cụ phản biện độc lập.
- **Hành động khắc phục & Bài học rút ra:**
  - Phải nắm vững và áp dụng chặt chẽ các phương pháp đánh giá chuẩn mực từ tài liệu, slide bài giảng môn học.
  - Áp dụng kỹ thuật mở một phiên làm việc mới (fresh session) hoặc dùng mô hình AI khác đóng vai trò phản biện độc lập (Devil's Advocate) để kiểm tra chéo, phát hiện các lỗ hổng logic và hoàn thiện tài liệu một cách sâu sắc, toàn diện.

### 2.4. Nguyễn Quang Thái (Backend & Requirements)

- **Vấn đề phát sinh:** Giai đoạn đầu gặp nhiều khó khăn, bỡ ngỡ trong việc sử dụng các công cụ AI để thực hiện các hoạt động quản lý dự án theo chuẩn yêu cầu môn học.
- **Bài học rút ra & Tiến bộ đạt được:** Qua quá trình thực chiến và hướng dẫn của nhóm, đã học được phương pháp làm chủ và khai thác AI hiệu quả hơn, đặc biệt trong việc phân rã cấu trúc công việc (WBS), lập kế hoạch, ước lượng tiến độ và xây dựng tài liệu phát triển phần mềm theo quy trình chuẩn.

### 2.5. Nguyễn Lê Hồ Anh Khoa (Frontend & UX)

- **Vấn đề / Khó khăn:** Không có vấn đề tồn đọng; giao diện người dùng cho độc giả và luồng đọc sách EPUB trực tuyến được hoàn thiện tốt, đáp ứng đúng yêu cầu bản mẫu (Prototype).

### 2.6. Mạch Quốc Tấn (Project Manager / Chủ tọa)

- **Vấn đề / Khó khăn:** Không có vấn đề phát sinh về công tác điều phối; tiến độ và sự phối hợp giữa 6 thành viên được duy trì liên tục và minh bạch.
- **Đóng góp & Kết luận:** Ghi nhận đầy đủ, trung thực toàn bộ ý kiến phản hồi của các thành viên để chuyển giao vào tài liệu **Báo cáo Bài học Kinh nghiệm** (`21-lessons-learned.md`) và hồ sơ bằng chứng nộp kèm [Câu 16](file:///g:/HCMUS/NAM3-HK3/Management/Final/hcmus-projectmanage--lab/docs.1/evidence/16/README.md) & [Câu 21](file:///g:/HCMUS/NAM3-HK3/Management/Final/hcmus-projectmanage--lab/docs.1/evidence/21/README.md).

---

## 3. Tổng kết các bài học kinh nghiệm cốt lõi của nhóm (Key Takeaways)

1. **Làm chủ kỹ thuật Prompting với đầy đủ Context:** Tuyệt đối không giao việc cho AI bằng các câu lệnh ngắn, thiếu bối cảnh. Cần cung cấp đầy đủ tài liệu nguồn, tiêu chí nghiệm thu (Acceptance Criteria) và rubric môn học.
2. **Cơ chế Phản biện chéo đa chiều (Multi-model / Multi-agent Review):** Sử dụng các phiên làm việc độc lập của AI để đóng vai trò thanh tra, phản biện tài liệu trước khi nộp.
3. **Đánh giá dựa trên chuẩn mực chính thức:** Lấy tài liệu bài giảng và hướng dẫn của giảng viên làm thước đo chân lý tối thượng cho mọi sản phẩm bàn giao.
4. **Văn hóa cởi mở và minh bạch:** Thẳng thắn nhìn nhận thiếu sót trong các buổi họp Retrospective giúp nhóm nâng cao năng lực nhanh chóng và gắn kết chặt chẽ.

---

## 4. Nghị quyết & Biểu quyết thông qua (Decisions & Sign-off)

Cuộc họp kết thúc lúc **17:00 ngày 22/08/2026**. Toàn bộ 6/6 thành viên có mặt đã biểu quyết **đồng thuận 100% (6/6)** thông qua các nội dung trong biên bản này.

### Chữ ký xác nhận của các thành viên

| STT | Thành viên                | Vai trò                       | Trạng thái ký xác nhận |
| :-: | ------------------------- | ----------------------------- | :--------------------: |
|  1  | **Mạch Quốc Tấn**         | Chủ tọa / Project Manager     | _Đã ký duyệt điện tử_  |
|  2  | **Ân Tiến Nguyên An**     | Thư ký cuộc họp / DevOps & QA | _Đã ký duyệt điện tử_  |
|  3  | **Ngô Nguyễn Thế Khoa**   | Frontend Lead                 | _Đã ký duyệt điện tử_  |
|  4  | **Nguyễn Lê Hồ Anh Khoa** | Kỹ sư Frontend & UX           | _Đã ký duyệt điện tử_  |
|  5  | **Nguyễn Quang Thái**     | Kỹ sư Backend & Requirements  | _Đã ký duyệt điện tử_  |
|  6  | **Nguyễn Tuấn Anh**       | Technical Lead                | _Đã ký duyệt điện tử_  |
