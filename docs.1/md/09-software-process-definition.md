# ĐỊNH NGHĨA QUY TRÌNH PHÁT TRIỂN PHẦN MỀM

## Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS (HCMUS-LDMS)

### Thông tin tài liệu

| Trường thông tin  | Nội dung                                 |
| ----------------- | ---------------------------------------- |
| Mã tài liệu       | `HCMUS-LDMS-SPD`                         |
| Tên tài liệu      | Định nghĩa quy trình phát triển phần mềm |
| Đơn vị thực hiện  | Nhóm Sebros                              |
| Người phụ trách   | Mạch Quốc Tấn — Đại diện nhóm Sebros     |
| Người xem xét     | Các thành viên nhóm Sebros               |
| Trạng thái        | Baseline nội bộ đã được nhóm xác nhận    |
| Thời gian áp dụng | 11 tuần                                  |
| Mục đích          | Phục vụ học tập và quản lý dự án môn học |

### Lịch sử phiên bản

| Phiên bản | Ngày       | Mô tả thay đổi                                                                                 | Người thực hiện |
| --------- | ---------- | ---------------------------------------------------------------------------------------------- | --------------- |
| 1.0       | 21/08/2026 | Xây dựng quy trình Kanban, vai trò, điều kiện sẵn sàng, điều kiện hoàn thành và cách đo lường. | Mạch Quốc Tấn   |
| 2.0       | 22/08/2026 | Đồng bộ sáu trạng thái Kanban, giới hạn công việc, nhánh chính và bằng chứng hoàn thành.       | Mạch Quốc Tấn   |
| 3.0       | 24/08/2026 | Đồng bộ baseline 15/6/5, nhóm sáu thành viên, PoC và cách triển khai thực tế.                  | Mạch Quốc Tấn   |
| 3.1       | 24/08/2026 | Bổ sung quyền quyết định, coding agent, kiểm tra tuân thủ và bảo đảm tiến độ.                  | Mạch Quốc Tấn   |
| 3.2       | 24/08/2026 | Rút gọn cấu trúc, đơn giản hóa câu chữ và giữ lại các quy tắc bắt buộc của quy trình.          | Mạch Quốc Tấn   |
| 3.3       | 24/08/2026 | Bổ sung quy trình tạo Pull Request và yêu cầu Technical Lead xem xét trước khi hợp nhất.       | Mạch Quốc Tấn   |
| 3.4       | 24/08/2026 | Đồng bộ ước lượng theo kết quả làm thử, điểm tương đối và hệ số dự phòng rủi ro 2,5.           | Mạch Quốc Tấn   |
| 3.5       | 24/08/2026 | Đồng bộ phân công Technical Lead, Backend, DevOps và QA theo Hợp đồng nhóm.                    | Mạch Quốc Tấn   |

### Tóm tắt quy trình

| Nội dung   | Quy định                                                                               |
| ---------- | -------------------------------------------------------------------------------------- |
| Mô hình    | Kanban theo luồng liên tục, không chia đợt nước rút cố định.                           |
| Phạm vi    | 15 Bắt buộc; 6 Nên có và 5 Có thể xem xét được quản lý ngoài baseline.                 |
| Luồng      | Ý tưởng → Đã sẵn sàng → Đang thực hiện → Đang xem xét → Chờ xác nhận → Hoàn thành.     |
| Giới hạn   | Mỗi thành viên 1 việc đang thực hiện; toàn nhóm 6 việc thực hiện và 4 việc xem xét.    |
| Chất lượng | Mã nguồn phải có Pull Request, được Technical Lead xem xét, kiểm thử và có bằng chứng. |
| Ước lượng  | Baseline 26 điểm; phần chưa triển khai thử còn 11 điểm, lập kế hoạch thành 4 ngày.     |
| Tiến độ    | Baseline được bảo đảm trong 11 tuần; coding agent hỗ trợ tăng năng suất.               |
| Truy vết   | YC → LDMS → thay đổi → kiểm thử → kết quả → xác nhận hoàn thành.                       |

## Mục lục

- [1. Mục đích và nguyên tắc](#1-mục-đích-và-nguyên-tắc)
- [2. Vai trò](#2-vai-trò)
- [3. Bảng Kanban](#3-bảng-kanban)
- [4. Quy trình thực hiện](#4-quy-trình-thực-hiện)
- [5. Điều kiện sẵn sàng và hoàn thành](#5-điều-kiện-sẵn-sàng-và-hoàn-thành)
- [6. Phát triển, xem xét và kiểm thử](#6-phát-triển-xem-xét-và-kiểm-thử)
- [7. Xử lý lỗi, công việc bị chặn và thay đổi](#7-xử-lý-lỗi-công-việc-bị-chặn-và-thay-đổi)
- [8. Truy vết, đo lường và cải tiến](#8-truy-vết-đo-lường-và-cải-tiến)
- [9. Sử dụng coding agent](#9-sử-dụng-coding-agent)
- [10. Tài liệu tham khảo](#10-tài-liệu-tham-khảo)

---

## 1. Mục đích và nguyên tắc

Tài liệu quy định cách nhóm Sebros chọn, thực hiện, xem xét, kiểm thử và hoàn thành công việc. Quy trình áp dụng cho mã nguồn, kiểm thử, cấu hình, tài liệu, sửa lỗi và công việc quản lý trong 11 tuần.

### 1.1. Phạm vi

| Priority       | Cách xử lý                                                            |
| -------------- | --------------------------------------------------------------------- |
| Bắt buộc       | Thuộc baseline và được ưu tiên hoàn thành trong 11 tuần.              |
| Nên có         | Chỉ thực hiện khi không ảnh hưởng đến hạng mục Bắt buộc.              |
| Có thể xem xét | Ngoài baseline; chỉ thực hiện sau khi nhóm xác nhận thay đổi phạm vi. |

### 1.2. Nguyên tắc

1. Hoàn thành việc đang làm trước khi nhận việc mới.
2. Không chuyển trạng thái chỉ để phù hợp ngày dự kiến.
3. Mỗi hạng mục có một người phụ trách và ít nhất một người xem xét khác.
4. Trạng thái Hoàn thành phải dựa trên kiểm thử và bằng chứng thực tế.
5. Không hạ yêu cầu bảo mật, dữ liệu hoặc chất lượng để đạt tiến độ.
6. PoC hỗ trợ quyết định kỹ thuật nhưng không thay thế kiểm thử sản phẩm.
7. Coding agent giúp tăng tốc nhưng không tự phê duyệt hoặc xác nhận chất lượng.
8. Thời gian tính theo tốc độ làm thử phải được nhân hệ số dự phòng rủi ro 2,5 trước khi đưa vào kế hoạch.

### 1.3. Thuật ngữ

| Thuật ngữ          | Cách hiểu                                                           |
| ------------------ | ------------------------------------------------------------------- |
| Baseline           | 15 hạng mục Bắt buộc đã được xác nhận cho 11 tuần.                  |
| DoR                | Điều kiện một hạng mục phải đạt trước khi được đưa vào thực hiện.   |
| DoD                | Điều kiện một hạng mục phải đạt trước khi được ghi nhận Hoàn thành. |
| Giới hạn công việc | Số việc tối đa được phép thực hiện đồng thời.                       |
| Công việc bị chặn  | Việc không thể tiếp tục vì phụ thuộc, lỗi hoặc thiếu thông tin.     |
| Thời gian chu kỳ   | Thời gian từ lúc bắt đầu thực hiện đến lúc hoàn thành.              |
| Thông lượng        | Số hạng mục hoàn thành trong một khoảng thời gian.                  |
| Coding agent       | Trợ lý lập trình AI hoạt động dưới sự kiểm soát của thành viên.     |
| Bằng chứng         | Kết quả thực tế dùng để xác nhận kiểm thử hoặc hoàn thành.          |
| Pull Request       | Yêu cầu xem xét và hợp nhất thay đổi mã nguồn vào nhánh chính.      |
| Technical Lead     | Người chịu trách nhiệm xem xét kỹ thuật và phê duyệt Pull Request.  |
| Điểm               | Đơn vị so sánh độ lớn tương đối: Nhỏ = 1, Vừa = 2, Lớn = 3.         |

## 2. Vai trò

### 2.1. Phân công chính

| Thành viên            | Vai trò chính              | Trách nhiệm chính                                          |
| --------------------- | -------------------------- | ---------------------------------------------------------- |
| Mạch Quốc Tấn         | Quản lý dự án; máy chủ     | Baseline, bảng Kanban, phụ thuộc, quyết định và tài liệu.  |
| Ân Tiến Nguyên An     | DevOps; đảm bảo chất lượng | Môi trường, CI/CD, kiểm thử, lỗi và bằng chứng kiểm thử.   |
| Ngô Nguyễn Thế Khoa   | Phụ trách giao diện        | Giao diện, hiệu chỉnh và trình đọc.                        |
| Nguyễn Tuấn Anh       | Technical Lead             | Kiến trúc, xem xét Pull Request và phê duyệt kỹ thuật.     |
| Nguyễn Quang Thái     | Máy chủ                    | API, dữ liệu, xác thực, phân quyền, OCR, EPUB và tìm kiếm. |
| Nguyễn Lê Hồ Anh Khoa | Giao diện                  | Trình đọc, khả năng sử dụng và kiểm thử giao diện.         |

### 2.2. Quy tắc trách nhiệm

- Mỗi hạng mục có đúng một người phụ trách chính.
- Người xem xét phải khác người phụ trách.
- Pull Request có thay đổi mã nguồn phải được Technical Lead xem xét trước khi hợp nhất.
- Một thành viên có thể kiêm nhiều vai trò.
- Nhóm Sebros xác nhận nội bộ cho dự án học tập.
- Đại diện thư viện hoặc người dùng bên ngoài chỉ là nguồn tham khảo khi dự án được mở rộng.

### 2.3. Quyền quyết định

| Loại quyết định                               | Người xác nhận                                         |
| --------------------------------------------- | ------------------------------------------------------ |
| Chi tiết trong hạng mục đã duyệt              | Người phụ trách và người xem xét.                      |
| Kỹ thuật ảnh hưởng một mô-đun                 | Phụ trách kiến trúc, người phụ trách và người xem xét. |
| Quy trình nội bộ không đổi baseline           | Tối thiểu 4/6 thành viên.                              |
| Thay đổi baseline, 11 tuần hoặc vai trò chính | 6/6 thành viên.                                        |
| Quyền sử dụng tài liệu khi mở rộng            | Đơn vị có thẩm quyền; nhóm không tự thay thế xác nhận. |

## 3. Bảng Kanban

Luồng thống nhất:

`Ý tưởng → Đã sẵn sàng → Đang thực hiện → Đang xem xét → Chờ xác nhận → Hoàn thành`

### 3.1. Ý nghĩa trạng thái

| Trạng thái     | Ý nghĩa                                                    | Điều kiện chuyển tiếp                                |
| -------------- | ---------------------------------------------------------- | ---------------------------------------------------- |
| Ý tưởng        | Công việc đã được ghi nhận nhưng chưa đủ thông tin.        | Làm rõ yêu cầu và đạt DoR.                           |
| Đã sẵn sàng    | Công việc có thể được kéo vào thực hiện.                   | Còn năng lực và không vượt giới hạn.                 |
| Đang thực hiện | Người phụ trách đang tạo mã nguồn, kiểm thử hoặc tài liệu. | Tự kiểm tra xong và có kết quả để xem xét.           |
| Đang xem xét   | Thành viên khác đang xem xét và kiểm thử.                  | Đạt kiểm tra hoặc trả lại Đang thực hiện để sửa.     |
| Chờ xác nhận   | Kiểm tra kỹ thuật đã đạt, đang chờ xác nhận cuối.          | Được xác nhận hoặc trả lại để chỉnh sửa.             |
| Hoàn thành     | Hạng mục đã đạt DoD và có bằng chứng.                      | Chỉ mở lại khi có lỗi hoặc thay đổi được chấp thuận. |

Tuần hoàn thành là một trường của hạng mục, không tạo cột Hoàn thành riêng cho từng tuần.

### 3.2. Giới hạn

| Phạm vi                         | Tối đa |
| ------------------------------- | -----: |
| Mỗi thành viên ở Đang thực hiện |      1 |
| Toàn nhóm ở Đang thực hiện      |      6 |
| Toàn nhóm ở Đang xem xét        |      4 |

Khi đạt giới hạn, nhóm xem xét, kiểm thử, sửa lỗi hoặc gỡ công việc bị chặn trước khi nhận thêm việc.

### 3.3. Thông tin của hạng mục

Mỗi hạng mục cần có:

- Mã `LDMS-xxx` hoặc mã công việc phù hợp.
- Tiêu đề và mô tả.
- Priority và ước lượng.
- Tiêu chí chấp nhận.
- Người phụ trách và người xem xét.
- Phụ thuộc, trạng thái và thời điểm.
- Công việc bị chặn khi có.
- Bằng chứng hoàn thành.

## 4. Quy trình thực hiện

### Bước 1 — Tiếp nhận

1. Ghi nhu cầu, lỗi hoặc yêu cầu thay đổi.
2. Xác định người dùng, vấn đề và kết quả mong muốn.
3. Đối chiếu với Yêu cầu phần mềm và Product Backlog.
4. Đưa công việc chưa đủ thông tin vào Ý tưởng.

### Bước 2 — Chuẩn bị

1. Viết mô tả và tiêu chí chấp nhận.
2. Xác định dữ liệu, phụ thuộc, rủi ro và môi trường.
3. Gắn Priority, mức ước lượng, số điểm, người phụ trách và người xem xét.
4. Chuyển sang Đã sẵn sàng khi đạt DoR.

### Bước 3 — Thực hiện

1. Kiểm tra giới hạn công việc.
2. Kéo hạng mục Bắt buộc có Priority cao nhất và đã hết phụ thuộc.
3. Ghi ngày bắt đầu.
4. Phát triển, tự kiểm tra và cập nhật tài liệu.
5. Khi hoàn tất mã nguồn, đẩy nhánh công việc và tạo Pull Request vào `main`.
6. Gắn mã hạng mục, mô tả thay đổi, kết quả kiểm thử và yêu cầu Technical Lead xem xét.
7. Chuyển sang Đang xem xét khi Pull Request đã sẵn sàng.

### Bước 4 — Xem xét và kiểm thử

1. Technical Lead xem xét Pull Request theo tiêu chí tại Mục 6.2.
2. Kiểm tra tiêu chí chấp nhận, bảo mật, dữ liệu và ảnh hưởng tài liệu.
3. Technical Lead phê duyệt hoặc yêu cầu chỉnh sửa trực tiếp trên Pull Request.
4. Người phụ trách sửa, cập nhật kiểm thử và yêu cầu xem xét lại khi cần.
5. Chỉ hợp nhất vào `main` khi Technical Lead đã phê duyệt và các kiểm tra bắt buộc đều đạt.
6. Chuyển sang Chờ xác nhận sau khi thay đổi đã được hợp nhất.

### Bước 5 — Hoàn thành

1. Đối chiếu từng tiêu chí chấp nhận.
2. Kiểm tra tài liệu, truy vết và bằng chứng.
3. Ghi người xác nhận, ngày và tuần hoàn thành.
4. Chuyển sang Hoàn thành.
5. Ghi sự kiện hoàn thành trong Nhật ký dự án.

## 5. Điều kiện sẵn sàng và hoàn thành

### 5.1. Điều kiện sẵn sàng (DoR)

Một hạng mục đạt DoR khi:

- Có mã, tiêu đề và mô tả rõ.
- Có tiêu chí chấp nhận kiểm thử được.
- Có Priority, mức ước lượng và số điểm.
- Có người phụ trách và người xem xét.
- Phụ thuộc, dữ liệu và môi trường đã rõ.
- Không còn câu hỏi làm thay đổi đáng kể phạm vi.

### 5.2. Điều kiện hoàn thành (DoD)

Một hạng mục đạt DoD khi:

- Tất cả tiêu chí chấp nhận đạt.
- Pull Request đã được Technical Lead xem xét và phê duyệt.
- Kiểm thử phù hợp đã chạy và có kết quả thực tế.
- Không còn lỗi nghiêm trọng chưa xử lý.
- Thay đổi mã nguồn đã được tích hợp vào `main`.
- Các kiểm tra tự động đã cấu hình đều đạt.
- Tài liệu và truy vết đã cập nhật.
- Có bằng chứng, người xác nhận và ngày hoàn thành.

PoC đạt không tự động làm hạng mục sản phẩm đạt DoD.

## 6. Phát triển, xem xét và kiểm thử

### 6.1. Mã nguồn

- `main` là nhánh tích hợp chính.
- Nhánh công việc dùng dạng `task/LDMS-xxx-mo-ta` hoặc `fix/mo-ta`.
- Mỗi thay đổi tập trung vào một mục đích.
- Thành viên tự kiểm tra trước khi yêu cầu xem xét.
- Không đẩy trực tiếp thay đổi mã nguồn vào `main`.
- Không đưa khóa bí mật, tệp môi trường hoặc dữ liệu thật vào mã nguồn.

### 6.2. Pull Request và xem xét kỹ thuật

Sau khi hoàn tất mã nguồn và tự kiểm tra, người phụ trách phải tạo Pull Request vào `main`. Pull Request cần có:

- mã và tiêu đề hạng mục;
- mô tả ngắn về thay đổi;
- tiêu chí chấp nhận liên quan;
- kết quả kiểm thử đã chạy;
- ảnh hưởng đến dữ liệu, bảo mật, kiến trúc hoặc tài liệu;
- bằng chứng phù hợp khi có thay đổi giao diện hoặc hành vi hệ thống.

Người phụ trách yêu cầu Technical Lead xem xét. Technical Lead kiểm tra:

- Đúng phạm vi và tiêu chí chấp nhận.
- Đúng quy tắc nghiệp vụ và kiến trúc.
- Kiểm tra quyền được thực hiện tại máy chủ.
- Dữ liệu được bảo toàn khi có lỗi.
- Kiểm thử bao phủ luồng chính và trường hợp lỗi phù hợp.
- Tài liệu và bằng chứng đã được cập nhật.

Nếu chưa đạt, Technical Lead yêu cầu chỉnh sửa trên Pull Request. Người phụ trách cập nhật cùng Pull Request và yêu cầu xem xét lại. Chỉ Technical Lead hoặc người được Technical Lead ủy quyền rõ ràng mới được phê duyệt kỹ thuật. Người tạo Pull Request không tự phê duyệt Pull Request của mình.

### 6.3. Kiểm thử

| Loại kiểm thử    | Mục đích                                               |
| ---------------- | ------------------------------------------------------ |
| Đơn vị           | Kiểm tra hàm hoặc thành phần độc lập.                  |
| Tích hợp         | Kiểm tra API, cơ sở dữ liệu, kho tệp và công cụ xử lý. |
| Chức năng        | Đối chiếu với tiêu chí chấp nhận.                      |
| Giao diện        | Kiểm tra thao tác, trạng thái và hiển thị.             |
| Phân quyền       | Kiểm tra hợp lệ, không xác thực và sai quyền.          |
| Hồi quy          | Xác nhận thay đổi không làm hỏng luồng đã đạt.         |
| Chấp nhận nội bộ | Xác nhận kết quả phù hợp mục tiêu học tập.             |

Trước bàn giao, nhóm kiểm tra luồng tải lên → OCR → hiệu chỉnh → tạo EPUB → xuất bản → tìm kiếm → đọc, cùng quyền truy cập và các trường hợp lỗi chính.

## 7. Xử lý lỗi, công việc bị chặn và thay đổi

### 7.1. Lỗi

| Mức độ       | Cách xử lý                                           |
| ------------ | ---------------------------------------------------- |
| Nghiêm trọng | Dừng hoàn thành; ưu tiên sửa và kiểm thử hồi quy.    |
| Cao          | Sửa trước khi xác nhận hoặc có ngoại lệ được ghi rõ. |
| Trung bình   | Xếp thứ tự xử lý và theo dõi trước bàn giao.         |
| Thấp         | Ghi nhận và xử lý theo năng lực còn lại.             |

Mỗi lỗi cần có môi trường, dữ liệu, bước tái hiện, kết quả mong đợi, kết quả thực tế, mức độ và người phụ trách.

### 7.2. Công việc bị chặn

Khi một hạng mục không thể tiếp tục, cần ghi:

- Thời điểm bắt đầu.
- Nguyên nhân và ảnh hưởng.
- Người hỗ trợ.
- Hành động tiếp theo.
- Thời điểm gỡ chặn và tổng thời gian bị chặn.

Thành viên báo trong ngày phát hiện. Nếu bị chặn quá hai ngày, quản lý dự án phải đổi phụ thuộc, thứ tự công việc, phạm vi hoặc năng lực.

### 7.3. Thay đổi phạm vi

Thay đổi baseline phải nêu:

- Lý do.
- Yêu cầu và hạng mục bị ảnh hưởng.
- Tác động đến tiến độ, nguồn lực, kiến trúc, kiểm thử và rủi ro.
- Phương án xử lý.
- Người xác nhận và ngày hiệu lực.

Không hạ DoD hoặc tiêu chí chấp nhận để bù tiến độ. Coding agent giúp bảo đảm tiến độ 11 tuần nhưng không phải lý do tự động tăng phạm vi.

## 8. Truy vết, đo lường và cải tiến

### 8.1. Truy vết

`YC-xxx → LDMS-xxx → Thay đổi → Kiểm thử → Kết quả → Hoàn thành`

Mã `YC-001`–`YC-026` tương ứng một-một với `LDMS-001`–`LDMS-026`. Yêu cầu phi chức năng dùng mã `YCP`.

Bằng chứng phải:

- Là kết quả thực tế.
- Xác định được hạng mục, người thực hiện và thời điểm.
- Không chứa khóa bí mật hoặc dữ liệu chưa được phép.
- Được gọi bằng mã hoặc tên tài liệu, không phụ thuộc đường dẫn thư mục trong bản in.

### 8.2. Chỉ số

| Chỉ số                 | Cách ghi nhận                                        |
| ---------------------- | ---------------------------------------------------- |
| Số việc đang thực hiện | Số việc ở Đang thực hiện và Đang xem xét.            |
| Thời gian chu kỳ       | Từ lúc vào Đang thực hiện đến lúc Hoàn thành.        |
| Thông lượng            | Số việc Hoàn thành trong một tuần.                   |
| Điểm Hoàn thành        | Tổng điểm của các hạng mục đã đạt DoD.               |
| Điểm còn lại           | Tổng điểm của các hạng mục chưa đạt DoD.             |
| Thời gian bị chặn      | Tổng thời gian hạng mục không thể tiếp tục.          |
| Tuổi công việc         | Thời gian việc đang ở trạng thái hiện tại.           |
| Công việc làm lại      | Công sức sửa do yêu cầu, thiết kế hoặc mã chưa đúng. |
| Lỗi sau hoàn thành     | Lỗi được phát hiện sau khi hạng mục đã Hoàn thành.   |

### 8.3. Nhịp theo dõi

| Hoạt động           | Tần suất              | Nội dung                                   |
| ------------------- | --------------------- | ------------------------------------------ |
| Cập nhật trạng thái | Mỗi ngày có làm việc  | Việc đã làm, việc tiếp theo và điểm chặn.  |
| Xem xét luồng       | Hai lần mỗi tuần      | Giới hạn, việc kéo dài và điểm chặn.       |
| Xem xét tuần        | Cuối tuần             | Hoàn thành, tiến độ, rủi ro và thay đổi.   |
| Cải tiến            | Khi có vấn đề lặp lại | Nguyên nhân, hành động và người phụ trách. |

Cuối mỗi tuần, nhóm kiểm tra một số hạng mục Hoàn thành để xác nhận DoR, DoD, giới hạn công việc, xem xét, kiểm thử, truy vết và bằng chứng đã được tuân thủ.

### 8.4. Cập nhật ước lượng

Baseline gồm 15 hạng mục Bắt buộc, tương ứng 26 điểm. Kết quả làm thử ngày 16 và 17 tháng 07 năm 2026 đã triển khai 15 điểm Bắt buộc. Phần chưa được triển khai thử còn 11 điểm.

Ước lượng được tính theo công thức:

`11 điểm ÷ 7,5 điểm/ngày × 2,5 = 3,68 ngày`

Nhóm làm tròn thành 4 ngày làm việc tương đương cho phần chưa được triển khai thử. Kết quả làm thử không tự động được tính là Hoàn thành. Khi có thêm hạng mục đạt DoD, nhóm cập nhật điểm Hoàn thành, điểm còn lại và dự báo nhưng vẫn giữ hệ số dự phòng 2,5 cho phần chưa thực hiện.

## 9. Sử dụng coding agent

Coding agent hỗ trợ phân tích, viết mã, tạo kiểm thử, rà soát, cập nhật tài liệu và xử lý lỗi. Công cụ giúp giảm thao tác lặp lại và hỗ trợ bảo đảm tiến độ baseline.

### 9.1. Quy tắc

- Không đưa khóa bí mật, dữ liệu cá nhân hoặc tài liệu chưa được phép vào công cụ.
- Thành viên phải đọc, hiểu và kiểm tra toàn bộ kết quả.
- Không dùng câu trả lời của coding agent thay cho kết quả kiểm thử.
- Không tạo số liệu, nhật ký, bằng chứng hoặc chữ ký không có thật.
- Chỉ ghi token, chi phí hoặc thời gian khi có số đo đáng tin cậy.
- Coding agent không tự phê duyệt, xác nhận hoàn thành hoặc đổi Priority.

### 9.2. Luồng sử dụng

1. Thành viên xác định mục tiêu, phạm vi và dữ liệu được phép dùng.
2. Coding agent hỗ trợ tạo hoặc sửa kết quả.
3. Thành viên đọc và loại bỏ nội dung sai hoặc ngoài phạm vi.
4. Thành viên chạy định dạng, kiểm tra và kiểm thử.
5. Thành viên tạo Pull Request và yêu cầu Technical Lead xem xét.
6. Technical Lead phê duyệt hoặc yêu cầu chỉnh sửa.
7. Ghi kết quả thực tế làm bằng chứng.
8. Chỉ hợp nhất hoặc hoàn thành khi đạt DoD.

## 10. Tài liệu tham khảo

- Đề xuất dự án.
- Viễn cảnh và phạm vi.
- Ủy nhiệm dự án.
- Yêu cầu phần mềm.
- Product Backlog.
- Kiến trúc phần mềm.
- Báo cáo nghiên cứu khả thi.
- Ước lượng dự án.
- Kế hoạch dự án.
- Bản mô tả công việc.
- Kế hoạch kiểm thử.
- Kế hoạch quản lý chất lượng.
- Kế hoạch quản lý rủi ro.
- Hợp đồng nhóm.
- Nhật ký dự án.
