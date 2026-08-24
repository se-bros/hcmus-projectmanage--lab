# HỢP ĐỒNG NHÓM (TEAM CONTRACT)

## Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS (HCMUS-LDMS)

### Thông tin tài liệu

| Trường thông tin | Nội dung                        |
| ---------------- | ------------------------------- |
| Mã tài liệu      | `HCMUS-LDMS-TCT`                |
| Đơn vị soạn thảo | Nhóm Sebros                     |
| Người phụ trách  | Mạch Quốc Tấn — Project Manager |
| Người phê duyệt  | Toàn bộ 6 thành viên            |
| Trạng thái       | Có hiệu lực                     |
| Phạm vi áp dụng  | MVP trong 11 tuần               |

### Lịch sử phiên bản

| Phiên bản |    Ngày    | Nội dung thay đổi                                                                                  | Người thực hiện   |
| --------: | :--------: | -------------------------------------------------------------------------------------------------- | ----------------- |
|       1.0 | 24/07/2026 | Khởi tạo Hợp đồng nhóm.                                                                            | Ân Tiến Nguyên An |
|       2.0 | 22/08/2026 | Đồng bộ cách làm việc, quản lý mã nguồn và sử dụng AI.                                             | Mạch Quốc Tấn     |
|       2.1 | 24/08/2026 | Cập nhật phân công: Tuấn Anh là Technical Lead, Thái phụ trách Backend, An phụ trách QA và DevOps. | Mạch Quốc Tấn     |

## 1. Mục đích và hiệu lực

Hợp đồng này thống nhất cách 6 thành viên phối hợp để hoàn thành MVP trong 11 tuần. Tài liệu quy định vai trò, cách làm việc, yêu cầu chất lượng và cách giải quyết vấn đề trong nhóm.

Hợp đồng có hiệu lực từ ngày 24/08/2026 sau khi được 6/6 thành viên xác nhận.

## 2. Thành viên và trách nhiệm

| Thành viên            | Vai trò chính            | Trách nhiệm chính                                                          |
| --------------------- | ------------------------ | -------------------------------------------------------------------------- |
| Mạch Quốc Tấn         | Project Manager; Backend | Điều phối dự án, quản lý phạm vi, tiến độ, rủi ro, tài liệu và hỗ trợ API. |
| Ân Tiến Nguyên An     | DevOps; QA               | Quản lý môi trường, CI/CD, kiểm thử, lỗi và bằng chứng kiểm thử.           |
| Ngô Nguyễn Thế Khoa   | Frontend Lead            | Phụ trách giao diện, trải nghiệm người dùng và điều phối Frontend.         |
| Nguyễn Tuấn Anh       | Technical Lead           | Thống nhất kỹ thuật, kiến trúc và phê duyệt Pull Request.                  |
| Nguyễn Quang Thái     | Backend                  | Phát triển API, dữ liệu, xác thực, phân quyền, OCR, EPUB và tìm kiếm.      |
| Nguyễn Lê Hồ Anh Khoa | Frontend                 | Phát triển giao diện và trình đọc tài liệu.                                |

Mạch Quốc Tấn chịu trách nhiệm điều phối chung. Nguyễn Tuấn Anh chịu trách nhiệm cuối cùng về kỹ thuật. Khi thay đổi vai trò, nhóm phải cập nhật Hợp đồng nhóm và các tài liệu liên quan.

## 3. Nguyên tắc làm việc

- Hoàn thành công việc đang làm trước khi nhận việc mới.
- Cập nhật trạng thái và báo trở ngại sớm.
- Nếu dự kiến không thể hoàn thành đúng thời hạn, thành viên phải báo cho nhóm trước ít nhất 12 giờ, nêu rõ lý do và thời gian hoàn thành dự kiến mới.
- Không ghi nhận công việc, kiểm thử hoặc số liệu chưa thực hiện.
- Không đưa thông tin bí mật, dữ liệu cá nhân hoặc tài liệu chưa được phép vào mã nguồn và công cụ AI.
- Mọi thay đổi phải có người khác xem xét; im lặng không được xem là phê duyệt.
- Thành viên chịu trách nhiệm về phần việc của mình và phải giải thích được kết quả đã thực hiện.

## 4. Quản lý công việc

Nhóm sử dụng Kanban với luồng:

`Ý tưởng` → `Đã sẵn sàng` → `Đang thực hiện` → `Đang xem xét` → `Chờ xác nhận` → `Hoàn thành`.

### 4.1. Giới hạn công việc

- Mỗi thành viên có tối đa 1 hạng mục ở trạng thái `Đang thực hiện`.
- Toàn nhóm có tối đa 6 hạng mục đang thực hiện và 4 hạng mục đang xem xét.
- Khi đạt giới hạn, nhóm ưu tiên hoàn thành, xem xét, kiểm thử hoặc gỡ trở ngại trước khi nhận việc mới.

### 4.2. Điều kiện bắt đầu

Một hạng mục chỉ được bắt đầu khi:

- có mã, mô tả và tiêu chí chấp nhận rõ ràng;
- có mức ưu tiên, ước lượng và người phụ trách;
- đã xác định người xem xét, phụ thuộc và dữ liệu cần thiết;
- không còn câu hỏi lớn làm thay đổi phạm vi.

### 4.3. Điều kiện hoàn thành

Một hạng mục chỉ được đánh dấu `Hoàn thành` khi:

- đạt các tiêu chí chấp nhận;
- đã kiểm thử và lưu kết quả;
- mã nguồn đã được Technical Lead hoặc người được ủy quyền phê duyệt qua Pull Request;
- không còn lỗi nghiêm trọng chưa được chấp thuận;
- đã tích hợp vào nhánh `main` và các kiểm tra tự động cần thiết đạt yêu cầu;
- tài liệu và bằng chứng liên quan đã được cập nhật.

## 5. Giao tiếp

| Kênh                | Mục đích                        | Thời gian phản hồi dự kiến |
| ------------------- | ------------------------------- | -------------------------- |
| Nhóm chat           | Trao đổi nhanh và báo trở ngại  | Trong 12 giờ               |
| Bảng công việc      | Cập nhật nhiệm vụ và trạng thái | Trong 24 giờ               |
| Pull Request        | Xem xét mã nguồn và tài liệu    | Trong 24 giờ làm việc      |
| Email hoặc biên bản | Trao đổi chính thức             | Theo thời hạn thống nhất   |

Nhóm cập nhật tiến độ trong ngày có làm dự án và rà soát công việc ít nhất hai lần mỗi tuần. Cuộc họp chỉ được tổ chức khi cần phối hợp hoặc giải quyết vấn đề.

## 6. Quản lý mã nguồn

- `main` là nhánh tích hợp chính.
- Mỗi công việc được thực hiện trên nhánh ngắn, sau đó tạo Pull Request.
- Pull Request phải nêu nội dung thay đổi, cách kiểm tra và rủi ro liên quan.
- Nguyễn Tuấn Anh, với vai trò Technical Lead, xem xét và phê duyệt Pull Request trước khi hợp nhất.
- Tác giả không tự phê duyệt Pull Request của mình.
- Khi Technical Lead vắng mặt, người được ủy quyền phải được ghi rõ trên Pull Request.
- Không đưa mật khẩu, khóa truy cập, tệp môi trường hoặc dữ liệu thật vào kho mã nguồn.

## 7. Sử dụng công cụ AI

Công cụ AI có thể hỗ trợ phân tích, viết mã, kiểm thử và viết tài liệu. Thành viên sử dụng AI vẫn chịu trách nhiệm về kết quả.

- Không cung cấp thông tin bí mật, dữ liệu cá nhân hoặc nội dung chưa được phép cho AI.
- Nội dung do AI tạo phải được con người đọc, kiểm tra và chỉnh sửa.
- Không dùng kết quả AI thay cho kiểm thử thực tế.
- Không tự tạo số liệu về thời gian, chi phí, token hoặc mức đóng góp.

## 8. Ra quyết định và giải quyết bất đồng

- Người phụ trách và người xem xét quyết định trong phạm vi hạng mục đã duyệt.
- Technical Lead quyết định vấn đề kỹ thuật sau khi tham khảo người phụ trách liên quan.
- Thay đổi quy trình nội bộ cần ít nhất 4/6 thành viên đồng ý.
- Thay đổi Project Manager, Technical Lead, phạm vi Bắt buộc hoặc kế hoạch 11 tuần cần 6/6 thành viên đồng ý.

Khi có bất đồng, nhóm ghi rõ vấn đề, so sánh các lựa chọn và ưu tiên tìm đồng thuận. Nếu chưa thống nhất, nhóm áp dụng tỷ lệ biểu quyết tương ứng ở trên và lưu lại quyết định.

## 9. Xử lý vi phạm

| Mức độ     | Ví dụ                                               | Cách xử lý                                             |
| ---------- | --------------------------------------------------- | ------------------------------------------------------ |
| Nhẹ        | Quên cập nhật công việc một lần                     | Nhắc nhở và bổ sung trong ngày làm việc tiếp theo.     |
| Trung bình | Lặp lại việc chậm cập nhật hoặc vắng mà không báo   | Thống nhất hành động khắc phục và thời hạn hoàn thành. |
| Nặng       | Làm giả bằng chứng, làm lộ dữ liệu hoặc bỏ nhiệm vụ | Báo giảng viên và ghi nhận trong đánh giá đóng góp.    |

Thành viên được quyền giải trình. Mọi xử lý phải dựa trên bằng chứng và tập trung khắc phục ảnh hưởng đến dự án.

## 10. Sửa đổi hợp đồng

Mọi sửa đổi phải nêu lý do, nội dung thay đổi và ngày áp dụng. Khi thay đổi nghĩa vụ hoặc vai trò, toàn bộ thành viên phải xác nhận lại.

## 11. Xác nhận của thành viên

| Thành viên            | MSSV     | Xác nhận    | Ngày       |
| --------------------- | -------- | ----------- | ---------- |
| Mạch Quốc Tấn         | 23127115 | Đã xác nhận | 24/08/2026 |
| Ân Tiến Nguyên An     | 23127048 | Đã xác nhận | 24/08/2026 |
| Ngô Nguyễn Thế Khoa   | 23127065 | Đã xác nhận | 24/08/2026 |
| Nguyễn Tuấn Anh       | 23127152 | Đã xác nhận | 24/08/2026 |
| Nguyễn Quang Thái     | 23127116 | Đã xác nhận | 24/08/2026 |
| Nguyễn Lê Hồ Anh Khoa | 23127211 | Đã xác nhận | 24/08/2026 |

Tất cả 6/6 thành viên cam kết thực hiện Hợp đồng nhóm.

## 12. Tài liệu tham chiếu

- Ủy nhiệm dự án.
- Danh mục công việc.
- Định nghĩa quy trình phát triển.
- Kế hoạch dự án.
