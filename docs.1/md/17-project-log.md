# NHẬT KÝ DỰ ÁN

## Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS (HCMUS-LDMS)

### Thông tin tài liệu

| Trường      | Nội dung                                                           |
| ----------- | ------------------------------------------------------------------ |
| Mã tài liệu | `HCMUS-LDMS-LOG`                                                   |
| Chủ sở hữu  | Project Manager — Mạch Quốc Tấn                                    |
| Trạng thái  | Đang sử dụng; dữ liệu lịch sử cần xác minh bằng chứng              |
| Phạm vi     | Nhật ký công sức, sự kiện hoàn thành, quyết định và số liệu Kanban |

### Lịch sử phiên bản

| Phiên bản |    Ngày    | Thay đổi                                                                                              |
| --------: | :--------: | ----------------------------------------------------------------------------------------------------- |
|       1.0 | 16/07/2026 | Khởi tạo bảng ghi các phiên làm việc và hạng mục.                                                     |
|       2.0 | 22/08/2026 | Tách công sức khỏi sự kiện hoàn thành, loại bỏ cách cộng trùng điểm và bổ sung yêu cầu về bằng chứng. |
|       2.1 | 22/08/2026 | Ghi nhận cuộc họp rút kinh nghiệm, kết luận và các hành động cải thiện của nhóm.                      |
|       2.2 | 24/08/2026 | Việt hóa thuật ngữ, ghi đầy đủ tên thành viên và đồng bộ quyết định baseline đã được nhóm xác nhận.   |

## Mục lục

- [1. Quy tắc ghi nhận](#1-quy-tắc-ghi-nhận)
- [2. Nhật ký công sức lịch sử](#2-nhật-ký-công-sức-lịch-sử)
- [3. Tổng hợp dữ liệu lịch sử](#3-tổng-hợp-dữ-liệu-lịch-sử)
- [4. Danh sách xác minh hoàn thành](#4-danh-sách-xác-minh-hoàn-thành)
- [5. Mẫu dòng mới](#5-mẫu-dòng-mới)
- [6. Chỉ số Kanban](#6-chỉ-số-kanban)
- [7. Quyết định và thay đổi](#7-quyết-định-và-thay-đổi)
- [8. Cuộc họp rút kinh nghiệm](#8-cuộc-họp-rút-kinh-nghiệm)

---

## 1. Quy tắc ghi nhận

### 1.1. Ba loại dữ liệu

| Loại bản ghi       | Mục đích                                                |             Có thể lặp mã hạng mục?             | Dùng tính tốc độ hoàn thành? |
| ------------------ | ------------------------------------------------------- | :---------------------------------------------: | :--------------------------: |
| Nhật ký công sức   | Ghi phiên làm việc và công sức thực tế                  |                       Có                        |            Không             |
| Sự kiện hoàn thành | Ghi lần hạng mục đạt Điều kiện hoàn thành (DoD)         | Không, trừ khi hạng mục được mở lại và làm xong |              Có              |
| Bằng chứng         | Chứng minh tiêu chí chấp nhận, kiểm thử và việc xem xét |                 Có thể có nhiều                 |       Không trực tiếp        |

### 1.2. Nguyên tắc

- Không cộng điểm của cùng một hạng mục nhiều lần để báo phạm vi đã hoàn thành.
- Dòng có nhiều hạng mục chỉ ghi tổng công sức của phiên làm việc; không chia đều khi không có bản ghi thời gian riêng.
- Chỉ ghi `Hoàn thành` khi đạt điều kiện hoàn thành quy định trong tài liệu **Hợp đồng nhóm**.
- Mỗi sự kiện hoàn thành phải có Pull Request hoặc cam kết mã nguồn, bằng chứng kiểm thử, người xem xét và ngày hoàn thành.
- Token và mô hình AI chỉ được ghi khi có số đo; nếu không có, ghi `Không có số đo`.
- Số token không được dùng thay cho công sức hoặc chất lượng.
- Nội dung tạm, bản mẫu hoặc phần triển khai chưa đầy đủ không được ghi là hạng mục hoàn thành khi tiêu chí chấp nhận chưa đạt.

## 2. Nhật ký công sức lịch sử

Các dòng dưới đây được giữ lại từ nhật ký trước. Trường “phân bổ theo hạng mục” trước đây là giả định chia đều; từ phiên bản 2.0, nhóm không dùng giả định đó làm công sức thực tế của từng hạng mục.

| Ngày       | Thành viên            | Mã hạng mục                            | Mô tả phiên làm việc                                           |      Công sức | Token được ghi | Công cụ hoặc mô hình AI          | Tình trạng bằng chứng                                              |
| ---------- | --------------------- | -------------------------------------- | -------------------------------------------------------------- | ------------: | -------------: | -------------------------------- | ------------------------------------------------------------------ |
| 16/07/2026 | Nguyễn Lê Hồ Anh Khoa | LDMS-008, 026                          | Nội dung tạm cho giao diện đọc, tìm kiếm và danh sách tài liệu |         2 giờ |            40K | Claude Sonnet 5; Claude Opus 4.8 | Chưa liên kết đủ Pull Request, kiểm thử và DoD trong nhật ký       |
| 16/07/2026 | Ngô Nguyễn Thế Khoa   | LDMS-003, 004, 007                     | OCR, kết quả theo trang và tạo EPUB                            |       45 phút |           140K | Không ghi rõ theo từng hạng mục  | Chưa liên kết đủ Pull Request, kiểm thử và DoD trong nhật ký       |
| 16/07/2026 | Nguyễn Quang Thái     | LDMS-013, 022                          | Điều kiện xuất bản và xử lý lại tác vụ                         |       45 phút |           140K | Không ghi rõ theo từng hạng mục  | Chưa liên kết đủ Pull Request, kiểm thử và DoD trong nhật ký       |
| 17/07/2026 | Nguyễn Tuấn Anh       | LDMS-001, 009, 010, 018                | Nền tảng, định danh, phân quyền và đăng nhập Google            | 1 giờ 20 phút |           120K | Claude Sonnet 5                  | Chưa liên kết đủ Pull Request, kiểm thử và DoD trong nhật ký       |
| 22/07/2026 | Nguyễn Tuấn Anh       | LDMS-001, 009, 010, 018                | Xác thực cục bộ, RBAC, hồ sơ, yêu cầu vai trò và miền email    |         2 giờ |           150K | Claude Sonnet 5                  | Chưa liên kết đủ Pull Request, kiểm thử và DoD trong nhật ký       |
| 18/07/2026 | Nguyễn Lê Hồ Anh Khoa | LDMS-008, 014, 015, 016, 019, 020, 026 | Trải nghiệm tìm kiếm và đọc                                    |         6 giờ |           100K | Claude Sonnet 5; Claude Opus 4.8 | Chưa liên kết đủ Pull Request, kiểm thử và DoD trong nhật ký       |
| 13/08/2026 | Nguyễn Lê Hồ Anh Khoa | LDMS-021                               | Đánh dấu và ghi chú                                            |         2 giờ |            40K | Claude Opus 5                    | Có lịch sử Git; vẫn cần gắn kiểm thử và DoD vào sự kiện hoàn thành |

## 3. Tổng hợp dữ liệu lịch sử

| Chỉ số                           |                      Giá trị | Cách hiểu đúng                                                   |
| -------------------------------- | ---------------------------: | ---------------------------------------------------------------- |
| Số phiên làm việc đã ghi         |                            7 | Bảy dòng công sức, không phải bảy hạng mục.                      |
| Tổng công sức của các phiên      |               14 giờ 50 phút | Tổng theo dòng, có thể gồm triển khai một phần hoặc làm lại.     |
| Tổng token được ghi              |                         730K | Số liệu lịch sử chưa có nguồn đo hoặc mã phiên kèm theo.         |
| Tổng điểm theo cách cộng cũ      |                           37 | Không dùng làm điểm hoàn thành vì có hạng mục bị lặp.            |
| Mã hạng mục duy nhất được nhắc   |                           17 | Không đồng nghĩa 17 hạng mục đã Hoàn thành.                      |
| Sự kiện hoàn thành đủ bằng chứng | 0 trong phiên bản nhật ký cũ | Phải xác minh lại từ Git, kiểm thử và kiểm thử chấp nhận nội bộ. |

Danh sách 17 mã hạng mục duy nhất đã được nhắc:

`LDMS-001`, `LDMS-003`, `LDMS-004`, `LDMS-007`, `LDMS-008`, `LDMS-009`, `LDMS-010`, `LDMS-013`, `LDMS-014`, `LDMS-015`, `LDMS-016`, `LDMS-018`, `LDMS-019`, `LDMS-020`, `LDMS-021`, `LDMS-022`, `LDMS-026`.

## 4. Danh sách xác minh hoàn thành

Danh sách này không suy diễn trạng thái Hoàn thành từ nhật ký công sức. Nhóm phải xác minh từng hạng mục bằng kho mã nguồn và tiêu chí hiện hành.

| Hạng mục | Mức độ         | Trạng thái xác minh | Bằng chứng cần bổ sung                                                   | Người xác nhận          |
| -------- | -------------- | ------------------- | ------------------------------------------------------------------------ | ----------------------- |
| LDMS-001 | Bắt buộc       | Chưa xác minh DoD   | Pull Request hoặc cam kết mã nguồn, hướng dẫn chạy và kiểm tra nhanh     | PM và người xem xét     |
| LDMS-003 | Bắt buộc       | Chưa xác minh DoD   | Kiểm thử OCR, trạng thái tác vụ và việc khởi động lại                    | Backend và QA           |
| LDMS-004 | Bắt buộc       | Chưa xác minh DoD   | Kiểm thử ánh xạ trang và nội dung xem trước                              | Frontend, Backend và QA |
| LDMS-007 | Bắt buộc       | Chưa xác minh DoD   | Kiểm tra tính hợp lệ của EPUB và trường hợp tạo tệp thất bại             | Backend và QA           |
| LDMS-008 | Bắt buộc       | Chưa xác minh DoD   | Tiêu chí đọc, phân quyền và hiển thị thích ứng                           | Frontend và QA          |
| LDMS-009 | Bắt buộc       | Chưa xác minh DoD   | Kiểm thử xác thực và các trường hợp lỗi                                  | Backend và QA           |
| LDMS-010 | Bắt buộc       | Chưa xác minh DoD   | Ma trận vai trò và kiểm thử từ chối truy cập sai quyền                   | Backend và QA           |
| LDMS-013 | Bắt buộc       | Chưa xác minh DoD   | Kiểm thử điều kiện cho phép xuất bản                                     | Backend và QA           |
| LDMS-014 | Bắt buộc       | Chưa xác minh DoD   | Kiểm thử truy cập riêng tư, liên kết hết hạn và trường hợp sai quyền     | Backend và QA           |
| LDMS-015 | Bắt buộc       | Chưa xác minh DoD   | Bộ dữ liệu tìm kiếm toàn văn và kết quả đã lọc theo quyền                | Backend và QA           |
| LDMS-016 | Bắt buộc       | Chưa xác minh DoD   | Giao diện kết quả, trạng thái rỗng và trạng thái lỗi                     | Frontend và QA          |
| LDMS-018 | Nên có         | Chưa xác minh DoD   | Cấu hình OAuth, kiểm thử và bằng chứng trường hợp lỗi                    | Backend và QA           |
| LDMS-019 | Có thể xem xét | Chưa xác minh DoD   | Tiêu chí chấp nhận riêng nếu được bổ sung vào phạm vi                    | Frontend và nghiệp vụ   |
| LDMS-020 | Có thể xem xét | Chưa xác minh DoD   | Kiểm thử lưu dữ liệu và quyền riêng tư nếu được bổ sung vào phạm vi      | Frontend, Backend và QA |
| LDMS-021 | Có thể xem xét | Chưa xác minh DoD   | Pull Request, kiểm thử quyền riêng tư, xóa dữ liệu và quyết định phạm vi | Frontend và QA          |
| LDMS-022 | Nên có         | Chưa xác minh DoD   | Kiểm thử xử lý lại và trường hợp lỗi                                     | Backend và QA           |
| LDMS-026 | Bắt buộc       | Chưa xác minh DoD   | Kiểm thử danh sách, trạng thái và phân quyền                             | Frontend, Backend và QA |

Các hạng mục Bắt buộc chưa xuất hiện trong nhật ký công sức cũ (`LDMS-002`, `LDMS-005`, `LDMS-011`) vẫn phải được quản lý trên bảng Kanban và ghi sự kiện hoàn thành khi đạt DoD.

## 5. Mẫu dòng mới

### 5.1. Nhật ký công sức

| Ngày                | Thành viên    | Hạng mục      | Hoạt động     | Công sức thực | Bị chặn/Làm lại | Công cụ AI    | Token/chi phí | Bằng chứng    |
| ------------------- | ------------- | ------------- | ------------- | ------------: | --------------: | ------------- | ------------- | ------------- |
| Chưa có dữ liệu mới | Chưa ghi nhận | Chưa ghi nhận | Chưa ghi nhận | Chưa ghi nhận |   Chưa ghi nhận | Chưa ghi nhận | Chưa ghi nhận | Chưa ghi nhận |

### 5.2. Sự kiện hoàn thành

| Ngày hoàn thành                              | Hạng mục | Người phụ trách | Người xem xét | Pull Request/cam kết mã nguồn | Bằng chứng kiểm thử | Xác nhận nghiệp vụ | Công sức thực | Ghi chú |
| -------------------------------------------- | -------- | --------------- | ------------- | ----------------------------- | ------------------- | ------------------ | ------------: | ------- |
| Chưa có sự kiện hoàn thành được xác minh lại |          |                 |               |                               |                     |                    |               |         |

## 6. Chỉ số Kanban

Chỉ tính từ sự kiện hoàn thành đã được xác minh:

| Tuần                         | Hạng mục hoàn thành duy nhất | Điểm hoàn thành | Thời gian chu kỳ P50/P85 | Thời gian bị chặn | Thời gian làm lại | Ghi chú                           |
| ---------------------------- | ---------------------------: | --------------: | ------------------------ | ----------------: | ----------------: | --------------------------------- |
| Chưa có dữ liệu đủ điều kiện |                            0 |               0 | Chưa tính                |         Chưa tính |         Chưa tính | Không suy từ nhật ký công sức cũ. |

Dự báo chỉ được cập nhật khi có ít nhất ba sự kiện hoàn thành đủ bằng chứng hoặc dữ liệu ba tuần có chất lượng phù hợp.

## 7. Quyết định và thay đổi

| Ngày       | Mã      | Quyết định                                                                     | Lý do                                                                          | Người quyết định                            | Tài liệu ảnh hưởng                                               |
| ---------- | ------- | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------- | ---------------------------------------------------------------- |
| 22/08/2026 | DEC-001 | Dùng baseline 11 tuần, 15 Bắt buộc, 6 Nên có và 5 Có thể xem xét cho bộ hồ sơ. | Đồng bộ bộ tài liệu và thay thế kế hoạch cũ 20 tuần.                           | Nhóm Sebros xác nhận nội bộ ngày 24/08/2026 | Bản mô tả công việc, Hợp đồng nhóm, Ước lượng, Quy trình, README |
| 22/08/2026 | DEC-002 | Tách nhật ký công sức khỏi danh sách xác minh hoàn thành.                      | Tránh cộng trùng hạng mục và dùng dữ liệu thiếu bằng chứng làm tốc độ thực tế. | Mạch Quốc Tấn                               | Nhật ký dự án, Ước lượng dự án                                   |

Các quyết định trên là quyết định cập nhật hồ sơ của nhóm; nội dung cần phê duyệt bên ngoài vẫn giữ trạng thái chờ xác nhận.

Quyết định kỹ thuật có các lựa chọn, hệ quả và điều kiện kiểm chứng được quản lý trong tài liệu **Nhật ký quyết định và hồ sơ quyết định kiến trúc**. Nhật ký dự án chỉ ghi sự kiện và mã quyết định tương ứng để tránh sai lệch giữa các tài liệu.

## 8. Cuộc họp rút kinh nghiệm

### 8.1. Thông tin cuộc họp

| Nội dung       | Chi tiết                                                                                                           |
| -------------- | ------------------------------------------------------------------------------------------------------------------ |
| Thời gian      | 15:15, ngày 22/08/2026                                                                                             |
| Mục đích       | Rút ra bài học kinh nghiệm sau quá trình thực hiện dự án                                                           |
| Người tham gia | Mạch Quốc Tấn, Ngô Nguyễn Thế Khoa, Ân Tiến Nguyên An, Nguyễn Lê Hồ Anh Khoa, Nguyễn Quang Thái và Nguyễn Tuấn Anh |
| Tỷ lệ tham gia | 6/6 thành viên                                                                                                     |

### 8.2. Kết quả

- Tuấn Anh ghi nhận một số sản phẩm chưa đạt chất lượng khi được nhóm xem xét do câu lệnh cho AI thiếu kiến thức nền, bối cảnh và tài liệu tham khảo.
- Nguyên An ghi nhận việc đánh giá tài liệu đã đầy đủ và đúng định dạng môn học mất nhiều thời gian.
- Quang Thái ghi nhận khó khăn ban đầu khi dùng AI cho hoạt động môn học, đồng thời học được cách dùng AI để hỗ trợ lập kế hoạch và phát triển phần mềm.
- Quốc Tấn, Thế Khoa và Anh Khoa không ghi nhận vấn đề đáng kể tại cuộc họp.

Nhóm thống nhất rằng câu lệnh cho AI phải có đủ mục tiêu, bối cảnh và tài liệu liên quan. Kết quả phải được đối chiếu với tài liệu chính thức và được thành viên kiểm tra trước khi sử dụng.

### 8.3. Hành động cải thiện

| Mã    | Hành động                                                               | Người áp dụng     | Thời điểm áp dụng          |
| ----- | ----------------------------------------------------------------------- | ----------------- | -------------------------- |
| AC-01 | Cung cấp mục tiêu, bối cảnh và tài liệu liên quan trước khi dùng AI.    | Tất cả thành viên | Từ công việc tiếp theo     |
| AC-02 | Đối chiếu kết quả với yêu cầu và tài liệu môn học chính thức.           | Người phụ trách   | Trước khi yêu cầu xem xét  |
| AC-03 | Dùng phiên hoặc mô hình AI khác để phản biện khi nội dung còn nghi ngờ. | Người phụ trách   | Khi cần kiểm tra bổ sung   |
| AC-04 | Kiểm tra và chỉnh sửa kết quả AI trước khi đưa vào sản phẩm hoặc hồ sơ. | Tất cả thành viên | Trước khi tạo Pull Request |

Chi tiết ý kiến của từng thành viên được trình bày trong tài liệu **Báo cáo bài học kinh nghiệm**.
