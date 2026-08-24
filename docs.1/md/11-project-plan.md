# KẾ HOẠCH DỰ ÁN

## Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS (HCMUS-LDMS)

### Thông tin tài liệu

| Trường thông tin | Nội dung                                    |
| ---------------- | ------------------------------------------- |
| Mã tài liệu      | `HCMUS-LDMS-PLAN`                           |
| Tên tài liệu     | Kế hoạch dự án                              |
| Người phụ trách  | Mạch Quốc Tấn — Quản lý dự án               |
| Người xem xét    | Các thành viên nhóm Sebros                  |
| Trạng thái       | Baseline nội bộ đã được nhóm xác nhận       |
| Thời gian        | 11 tuần                                     |
| Phạm vi          | 15 hạng mục Bắt buộc                        |
| Cơ sở ước lượng  | Kết quả làm thử và điểm của Product Backlog |

### Lịch sử phiên bản

| Phiên bản | Ngày       | Mô tả thay đổi                                                                  | Người thực hiện |
| --------- | ---------- | ------------------------------------------------------------------------------- | --------------- |
| 1.0       | 22/08/2026 | Xây dựng kế hoạch 11 tuần theo phạm vi, công sức và nguồn lực ban đầu.          | Mạch Quốc Tấn   |
| 2.0       | 24/08/2026 | Đồng bộ phương pháp ước lượng theo kết quả làm thử, điểm và hệ số dự phòng 2,5. | Mạch Quốc Tấn   |
| 2.1       | 24/08/2026 | Đồng bộ Technical Lead, Backend, DevOps và QA theo Hợp đồng nhóm.               | Mạch Quốc Tấn   |

## Mục lục

- [1. Mục đích](#1-mục-đích)
- [2. Baseline của dự án](#2-baseline-của-dự-án)
- [3. Cơ sở lập kế hoạch](#3-cơ-sở-lập-kế-hoạch)
- [4. Phân chia công việc](#4-phân-chia-công-việc)
- [5. Kế hoạch 11 tuần](#5-kế-hoạch-11-tuần)
- [6. Nguồn lực và trách nhiệm](#6-nguồn-lực-và-trách-nhiệm)
- [7. Quy trình thực hiện hạng mục](#7-quy-trình-thực-hiện-hạng-mục)
- [8. Chất lượng và kiểm thử](#8-chất-lượng-và-kiểm-thử)
- [9. Theo dõi tiến độ](#9-theo-dõi-tiến-độ)
- [10. Rủi ro và thay đổi](#10-rủi-ro-và-thay-đổi)
- [11. Điều kiện hoàn thành dự án](#11-điều-kiện-hoàn-thành-dự-án)
- [12. Tài liệu tham khảo](#12-tài-liệu-tham-khảo)

---

## 1. Mục đích

Tài liệu xác định phạm vi, lịch thực hiện, phân công, cách kiểm soát chất lượng và điều kiện hoàn thành dự án trong 11 tuần. Kế hoạch phục vụ mục đích học tập và quản lý công việc của nhóm Sebros.

Dự án ưu tiên hoàn thành luồng chính:

`Tải tài liệu → OCR → Hiệu chỉnh → Tạo EPUB → Xuất bản → Tìm kiếm → Đọc trực tuyến`

## 2. Baseline của dự án

| Yếu tố           | Baseline đã xác nhận                                                      |
| ---------------- | ------------------------------------------------------------------------- |
| Phạm vi          | 15 hạng mục Bắt buộc, tổng cộng 26 điểm.                                  |
| Thời gian        | 11 tuần.                                                                  |
| Nhân sự          | 6 sinh viên thuộc nhóm Sebros.                                            |
| Phương pháp      | Kanban theo luồng liên tục.                                               |
| Kiểm soát mã     | Mỗi thay đổi mã nguồn được thực hiện qua Pull Request.                    |
| Xem xét kỹ thuật | Technical Lead xem xét và phê duyệt trước khi hợp nhất vào `main`.        |
| Chất lượng       | Chỉ ghi Hoàn thành khi hạng mục đạt Tiêu chí hoàn thành (DoD).            |
| Công cụ hỗ trợ   | Coding agent hỗ trợ phát triển, kiểm thử, rà soát, tài liệu và xử lý lỗi. |
| Chi phí          | 0 VNĐ tiền mặt nếu sử dụng thiết bị và các gói dịch vụ sẵn có.            |

Sáu hạng mục Nên có và năm hạng mục Có thể xem xét không thuộc cam kết baseline. Các hạng mục này chỉ được thực hiện khi không ảnh hưởng đến 15 hạng mục Bắt buộc.

## 3. Cơ sở lập kế hoạch

### 3.1. Kết quả làm thử

Nhóm thực hiện làm thử trong ngày 16 và 17 tháng 07 năm 2026.

| Nội dung                                 | Kết quả |
| ---------------------------------------- | ------: |
| Số ngày làm thử                          |  2 ngày |
| Số hạng mục đã được triển khai thử       |      11 |
| Tổng số điểm đã được triển khai thử      |      18 |
| Hạng mục Bắt buộc đã được triển khai thử |       9 |
| Điểm Bắt buộc đã được triển khai thử     |      15 |

Các hạng mục làm thử đã tạo được kết quả kỹ thuật nhưng chưa mặc định được xem là Hoàn thành. Mỗi hạng mục vẫn phải có Pull Request, kết quả kiểm thử, Technical Lead xem xét và bằng chứng đạt DoD.

### 3.2. Ước lượng phần baseline còn lại

Baseline có 26 điểm. Giai đoạn làm thử đã triển khai 15 điểm Bắt buộc, vì vậy phần chưa được triển khai thử còn:

`26 điểm - 15 điểm = 11 điểm`

Tốc độ triển khai thử đối với hạng mục Bắt buộc:

`15 điểm ÷ 2 ngày = 7,5 điểm/ngày`

Thời gian tính theo tốc độ làm thử:

`11 điểm ÷ 7,5 điểm/ngày = 1,47 ngày`

Nhóm áp dụng hệ số dự phòng rủi ro 2,5:

`1,47 ngày × 2,5 = 3,68 ngày`

Kết quả được làm tròn thành **4 ngày làm việc tương đương của nhóm** cho sáu hạng mục Bắt buộc chưa được triển khai thử. Hệ số dự phòng bao gồm xem xét Pull Request, kiểm thử, tích hợp, sửa lỗi, tài liệu, công việc bị chặn và sai lệch so với giai đoạn làm thử.

Kế hoạch vẫn sử dụng 11 tuần vì ngoài việc tạo mã nguồn, nhóm phải hoàn thiện cả 15 hạng mục theo DoD, phối hợp giữa sáu thành viên, thực hiện công việc quản lý và bảo đảm phù hợp với lịch học.

## 4. Phân chia công việc

| Nhóm công việc                | Hạng mục hoặc nội dung chính            | Kết quả cần đạt                                |
| ----------------------------- | --------------------------------------- | ---------------------------------------------- |
| Quản lý dự án                 | Phạm vi, kế hoạch, rủi ro, thay đổi     | Baseline và trạng thái được cập nhật.          |
| Nền tảng và phân quyền        | LDMS-001, LDMS-009, LDMS-010            | Hệ thống chạy được và kiểm soát đúng quyền.    |
| Tiếp nhận và OCR              | LDMS-002, LDMS-003, LDMS-004            | Tải tệp, xử lý OCR và xem kết quả theo trang.  |
| Hiệu chỉnh và thông tin mô tả | LDMS-005, LDMS-011, LDMS-026            | Lưu nội dung, quản lý mô tả và trạng thái.     |
| Xuất bản và đọc               | LDMS-007, LDMS-013, LDMS-008, LDMS-014  | Tạo EPUB, kiểm tra xuất bản và đọc đúng quyền. |
| Tìm kiếm                      | LDMS-015, LDMS-016                      | Tìm kiếm toàn văn và hiển thị kết quả.         |
| Chất lượng và bàn giao        | Kiểm thử, sửa lỗi, tài liệu và xác nhận | Baseline đạt DoD và có bằng chứng.             |

## 5. Kế hoạch 11 tuần

| Tuần | Trọng tâm                             | Hạng mục chính               | Kết quả cuối tuần                                  |
| ---: | ------------------------------------- | ---------------------------- | -------------------------------------------------- |
|    1 | Xác nhận baseline và chuẩn bị         | Toàn bộ baseline             | Phạm vi, vai trò, môi trường và dữ liệu được chốt. |
|    2 | Nền tảng, đăng nhập và phân quyền     | LDMS-001, LDMS-009, LDMS-010 | Nền tảng chạy được; quyền được kiểm thử.           |
|    3 | Tải lên và danh sách tài liệu         | LDMS-002, LDMS-026           | Tệp được lưu an toàn; danh sách đúng quyền.        |
|    4 | OCR và kết quả theo trang             | LDMS-003, LDMS-004           | Tác vụ OCR và kết quả theo trang hoạt động.        |
|    5 | Hiệu chỉnh và thông tin mô tả         | LDMS-005, LDMS-011           | Nội dung hiệu chỉnh và thông tin mô tả được lưu.   |
|    6 | Tạo EPUB và kiểm tra xuất bản         | LDMS-007, LDMS-013           | EPUB hợp lệ; tài liệu thiếu điều kiện bị chặn.     |
|    7 | Tìm kiếm và hiển thị kết quả          | LDMS-015, LDMS-016           | Tìm kiếm đúng dữ liệu và đúng quyền.               |
|    8 | Đọc trực tuyến và bảo vệ quyền đọc    | LDMS-008, LDMS-014           | Nội dung đọc được và không lộ tệp riêng tư.        |
|    9 | Tích hợp và kiểm thử hồi quy          | Toàn bộ 15 hạng mục          | Luồng đầu cuối hoạt động; lỗi được ghi nhận.       |
|   10 | Sửa lỗi và hoàn thiện tài liệu        | Lỗi còn lại và bộ tài liệu   | Không còn lỗi nghiêm trọng; tài liệu đồng bộ.      |
|   11 | Kiểm thử chấp nhận nội bộ và bàn giao | Toàn bộ baseline             | Có kết quả xác nhận, bằng chứng và tổng kết.       |

Hạng mục có thể được thực hiện sớm hơn khi còn năng lực. Việc thay đổi thứ tự không làm thay đổi tiêu chí chấp nhận hoặc DoD.

## 6. Nguồn lực và trách nhiệm

| Thành viên            | Vai trò chính              | Trách nhiệm chính                                          |
| --------------------- | -------------------------- | ---------------------------------------------------------- |
| Mạch Quốc Tấn         | Quản lý dự án; máy chủ     | Baseline, kế hoạch, điều phối, máy chủ và tài liệu.        |
| Ân Tiến Nguyên An     | DevOps; đảm bảo chất lượng | Môi trường, CI/CD, kiểm thử, lỗi và bằng chứng kiểm thử.   |
| Ngô Nguyễn Thế Khoa   | Phụ trách giao diện        | Giao diện, hiệu chỉnh và tìm kiếm.                         |
| Nguyễn Tuấn Anh       | Technical Lead             | Kiến trúc, xem xét Pull Request và phê duyệt kỹ thuật.     |
| Nguyễn Quang Thái     | Máy chủ                    | API, dữ liệu, xác thực, phân quyền, OCR, EPUB và tìm kiếm. |
| Nguyễn Lê Hồ Anh Khoa | Giao diện                  | Trình đọc, trải nghiệm sử dụng và hỗ trợ tích hợp.         |

Mỗi hạng mục có một người phụ trách chính. Người tạo thay đổi không tự phê duyệt Pull Request của mình. Technical Lead có thể ủy quyền xem xét khi cần, nhưng việc ủy quyền phải được ghi rõ.

## 7. Quy trình thực hiện hạng mục

Mỗi hạng mục đi qua các trạng thái:

`Ý tưởng → Đã sẵn sàng → Đang thực hiện → Đang xem xét → Chờ xác nhận → Hoàn thành`

Quy trình thực hiện:

1. Chọn hạng mục Bắt buộc có mức ưu tiên cao nhất và không còn phụ thuộc.
2. Xác nhận mô tả, tiêu chí chấp nhận, người phụ trách và ước lượng.
3. Phát triển, tự kiểm tra và cập nhật tài liệu liên quan.
4. Tạo Pull Request vào `main` khi mã nguồn đã sẵn sàng.
5. Yêu cầu Technical Lead xem xét.
6. Sửa các nội dung được yêu cầu và chạy lại kiểm thử.
7. Chỉ hợp nhất khi Technical Lead phê duyệt và các kiểm tra bắt buộc đạt.
8. Xác nhận tiêu chí chấp nhận, bằng chứng và DoD trước khi ghi Hoàn thành.

Giới hạn công việc:

- mỗi thành viên chỉ có tối đa một hạng mục ở trạng thái Đang thực hiện;
- toàn nhóm có tối đa sáu hạng mục Đang thực hiện;
- toàn nhóm có tối đa bốn hạng mục Đang xem xét.

## 8. Chất lượng và kiểm thử

Một hạng mục chỉ được ghi Hoàn thành khi:

- tất cả tiêu chí chấp nhận đều đạt;
- Pull Request đã được Technical Lead xem xét và phê duyệt;
- kiểm thử phù hợp đã chạy và có kết quả;
- không còn lỗi nghiêm trọng chưa xử lý;
- thay đổi đã được hợp nhất vào `main`;
- tài liệu và truy vết đã được cập nhật;
- có người xác nhận và ngày hoàn thành.

Các loại kiểm thử chính gồm kiểm thử đơn vị, tích hợp, chức năng, giao diện, phân quyền, hồi quy và chấp nhận nội bộ. Trước khi bàn giao, nhóm kiểm tra toàn bộ luồng từ tải tài liệu đến đọc trực tuyến.

## 9. Theo dõi tiến độ

### 9.1. Nhịp theo dõi

| Hoạt động               | Tần suất             | Nội dung                                           |
| ----------------------- | -------------------- | -------------------------------------------------- |
| Cập nhật hạng mục       | Mỗi ngày có làm việc | Trạng thái, kết quả, việc tiếp theo và điểm chặn.  |
| Xem xét luồng công việc | Hai lần mỗi tuần     | Giới hạn công việc, hạng mục kéo dài và phụ thuộc. |
| Xem xét tiến độ         | Cuối mỗi tuần        | Điểm hoàn thành, mốc, lỗi, rủi ro và điều chỉnh.   |
| Tổng kết                | Tuần 11              | Baseline, chất lượng, bài học và bàn giao.         |

### 9.2. Chỉ số theo dõi

| Chỉ số                   | Cách sử dụng                                             |
| ------------------------ | -------------------------------------------------------- |
| Hạng mục Hoàn thành      | Chỉ tính khi đạt DoD và có bằng chứng.                   |
| Điểm Hoàn thành          | Tổng điểm của các hạng mục đạt DoD.                      |
| Công việc đang thực hiện | Dùng để kiểm soát giới hạn và tránh nhận quá nhiều việc. |
| Thời gian bị chặn        | Dùng để ưu tiên gỡ phụ thuộc.                            |
| Lỗi còn lại              | Theo dõi mức độ, người xử lý và trạng thái kiểm thử lại. |
| Sai lệch so với kế hoạch | So sánh kết quả thực tế với mục tiêu từng tuần.          |

Kết quả làm thử không được tự động tính là điểm Hoàn thành. Điểm chỉ được ghi nhận sau khi hạng mục đạt DoD.

## 10. Rủi ro và thay đổi

### 10.1. Rủi ro chính

| Rủi ro                             | Cách xử lý                                                           |
| ---------------------------------- | -------------------------------------------------------------------- |
| Tích hợp nhiều công nghệ           | Hoàn thành theo từng luồng nhỏ và kiểm thử sớm.                      |
| Sai quyền truy cập                 | Kiểm tra quyền tại máy chủ và thực hiện kiểm thử trường hợp sai.     |
| Công việc bị chặn                  | Ghi rõ nguyên nhân, người xử lý và ưu tiên gỡ trong tuần.            |
| Pull Request chờ xem xét lâu       | Technical Lead xem xét theo lịch; ủy quyền rõ khi không sẵn sàng.    |
| Coding agent tạo kết quả chưa đúng | Thành viên đọc, kiểm tra và chạy kiểm thử trước khi yêu cầu xem xét. |
| Phạm vi tăng ngoài kế hoạch        | Không đưa hạng mục tùy chọn vào thực hiện khi baseline chưa ổn định. |

Hệ số dự phòng 2,5 đã được dùng trong ước lượng để giảm ảnh hưởng của các rủi ro kỹ thuật và phối hợp thông thường.

### 10.2. Quản lý thay đổi

Thay đổi baseline phải nêu rõ:

- nội dung và lý do thay đổi;
- hạng mục và tài liệu bị ảnh hưởng;
- tác động đến điểm, lịch, nguồn lực, chất lượng và rủi ro;
- phương án xử lý;
- kết quả xác nhận của nhóm Sebros.

Không tự ý giảm tiêu chí chấp nhận, kiểm thử hoặc DoD để giữ tiến độ.

## 11. Điều kiện hoàn thành dự án

Dự án đạt baseline khi:

1. Cả 15 hạng mục Bắt buộc đều đạt DoD.
2. Luồng tải tài liệu, OCR, hiệu chỉnh, tạo EPUB, xuất bản, tìm kiếm và đọc hoạt động với dữ liệu mẫu.
3. Quyền truy cập được kiểm tra tại máy chủ và các trường hợp sai quyền bị từ chối.
4. Không còn lỗi nghiêm trọng chưa xử lý.
5. Tài liệu dự án được cập nhật đầy đủ và nhất quán.
6. Nhóm hoàn tất kiểm thử chấp nhận nội bộ và ghi nhận kết quả.
7. Có bằng chứng cho Pull Request, kiểm thử, người xem xét và ngày hoàn thành.

Sáu thành viên nhóm Sebros xác nhận kết quả nội bộ cho phạm vi dự án học tập. Đại diện thư viện hoặc bên ngoài chỉ tham gia tham khảo khi dự án được mở rộng.

## 12. Tài liệu tham khảo

- Đề xuất dự án.
- Viễn cảnh và phạm vi.
- Ủy nhiệm dự án.
- Yêu cầu phần mềm.
- Product Backlog.
- Kiến trúc phần mềm.
- Báo cáo nghiên cứu tính khả thi.
- Định nghĩa quy trình phát triển phần mềm.
- Ước lượng dự án.
- Bản mô tả công việc.
- Kế hoạch quản lý rủi ro.
- Kế hoạch quản lý chất lượng.
- Kế hoạch kiểm thử.
- Nhật ký dự án.
