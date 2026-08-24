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

| Phiên bản | Ngày       | Mô tả thay đổi                                                                                                      | Người thực hiện |
| --------- | ---------- | ------------------------------------------------------------------------------------------------------------------- | --------------- |
| 1.0       | 21/08/2026 | Xây dựng quy trình Kanban, vai trò, luồng công việc, điều kiện sẵn sàng, điều kiện hoàn thành và đo lường.          | Mạch Quốc Tấn   |
| 2.0       | 22/08/2026 | Đồng bộ sáu trạng thái Kanban, giới hạn công việc, phát triển dựa trên nhánh chính và bằng chứng hoàn thành.        | Mạch Quốc Tấn   |
| 3.0       | 24/08/2026 | Viết lại toàn diện theo baseline 15/6/5, nhóm sáu thành viên, PoC đã hoàn tất và cách triển khai thực tế của dự án. | Mạch Quốc Tấn   |

## Mục lục

- [1. Mục đích và phạm vi](#1-mục-đích-và-phạm-vi)
- [2. Nguyên tắc và mô hình quy trình](#2-nguyên-tắc-và-mô-hình-quy-trình)
- [3. Vai trò và trách nhiệm](#3-vai-trò-và-trách-nhiệm)
- [4. Bảng Kanban và giới hạn công việc](#4-bảng-kanban-và-giới-hạn-công-việc)
- [5. Quy trình từ yêu cầu đến hoàn thành](#5-quy-trình-từ-yêu-cầu-đến-hoàn-thành)
- [6. Điều kiện sẵn sàng và điều kiện hoàn thành](#6-điều-kiện-sẵn-sàng-và-điều-kiện-hoàn-thành)
- [7. Phát triển, xem xét và kiểm thử](#7-phát-triển-xem-xét-và-kiểm-thử)
- [8. Xử lý lỗi, công việc bị chặn và ngoại lệ](#8-xử-lý-lỗi-công-việc-bị-chặn-và-ngoại-lệ)
- [9. Quản lý phạm vi và thay đổi](#9-quản-lý-phạm-vi-và-thay-đổi)
- [10. Truy vết và bằng chứng](#10-truy-vết-và-bằng-chứng)
- [11. Đo lường và cải tiến](#11-đo-lường-và-cải-tiến)
- [12. Sử dụng công cụ hỗ trợ và AI](#12-sử-dụng-công-cụ-hỗ-trợ-và-ai)
- [13. Tài liệu tham khảo](#13-tài-liệu-tham-khảo)

---

## 1. Mục đích và phạm vi

Tài liệu quy định cách nhóm Sebros lựa chọn, thực hiện, xem xét, kiểm thử và xác nhận công việc của HCMUS-LDMS. Quy trình giúp mỗi thành viên biết công việc bắt đầu từ đâu, điều kiện chuyển trạng thái, người chịu trách nhiệm, kết quả phải tạo ra và bằng chứng cần có trước khi hoàn thành.

Quy trình áp dụng cho:

- 15 hạng mục Bắt buộc thuộc baseline 11 tuần.
- Sáu hạng mục Nên có khi không ảnh hưởng đến baseline.
- Năm hạng mục Có thể xem xét khi có quyết định bổ sung phạm vi.
- Mã nguồn, kiểm thử, cấu hình, tài liệu và công việc quản lý liên quan.
- Công việc sửa lỗi, làm lại và cập nhật phát sinh trong phạm vi đã xác nhận.

Quy trình không thay thế Yêu cầu phần mềm, Product Backlog, Kiến trúc phần mềm, Kế hoạch dự án hoặc Kế hoạch kiểm thử. Chi tiết của từng hạng mục được đọc trong tài liệu tương ứng; tài liệu này chỉ quy định cách công việc đi qua hệ thống quản lý của nhóm.

## 2. Nguyên tắc và mô hình quy trình

### 2.1. Mô hình Kanban

Nhóm sử dụng Kanban vì:

- Nhóm làm việc theo lịch học và năng lực có thể thay đổi theo tuần.
- Các hạng mục OCR, EPUB, tìm kiếm và đọc có quan hệ phụ thuộc.
- Nhóm cần ưu tiên hoàn thành công việc đang làm trước khi nhận thêm việc.
- Công việc cần được kéo theo năng lực thực tế thay vì buộc vào đợt nước rút cố định.
- Trạng thái, điểm nghẽn và thời gian bị chặn cần được nhìn thấy trên một bảng chung.

Kanban không có nghĩa là làm việc không có kế hoạch. Nhóm vẫn tuân theo baseline, mốc 11 tuần, mức độ ưu tiên, tiêu chí chấp nhận, giới hạn công việc và điều kiện hoàn thành.

### 2.2. Nguyên tắc thực hiện

1. Baseline và tiêu chí chấp nhận là cơ sở lựa chọn công việc.
2. Hoàn thành công việc đang làm trước khi kéo công việc mới.
3. Không chuyển trạng thái chỉ để phù hợp với ngày dự kiến.
4. Mọi công việc phải có người chịu trách nhiệm và người xem xét.
5. Người tạo thay đổi không phải người duy nhất xác nhận chất lượng thay đổi đó.
6. Bảo mật, tính toàn vẹn dữ liệu và tính trung thực của bằng chứng không được hạ thấp để đạt tiến độ.
7. Trạng thái hoàn thành phải dựa trên kết quả kiểm tra, không dựa trên nhận định chưa có bằng chứng.
8. Hạng mục ngoài baseline không được tự động đưa vào thực hiện.
9. PoC đã hoàn tất được dùng làm bằng chứng cho quyết định kỹ thuật, không thay thế kiểm thử của sản phẩm.
10. Chỉ số được dùng để cải tiến luồng công việc, không dùng riêng lẻ để xếp hạng cá nhân.

### 2.3. Phạm vi ưu tiên

| Priority       | Cách xử lý trong quy trình                                                     |
| -------------- | ------------------------------------------------------------------------------ |
| Bắt buộc       | Được ưu tiên lập kế hoạch, thực hiện, kiểm thử và xác nhận trong 11 tuần.      |
| Nên có         | Chỉ được kéo khi không làm chậm hạng mục Bắt buộc và nhóm còn đủ năng lực.     |
| Có thể xem xét | Nằm ngoài baseline; cần quyết định thay đổi trước khi đưa vào luồng thực hiện. |

## 3. Vai trò và trách nhiệm

### 3.1. Phân công chính

| Thành viên            | Vai trò chính                           | Trách nhiệm trong quy trình                                         |
| --------------------- | --------------------------------------- | ------------------------------------------------------------------- |
| Mạch Quốc Tấn         | Quản lý dự án; phát triển máy chủ       | Duy trì baseline, bảng Kanban, phụ thuộc, quyết định và tài liệu.   |
| Ân Tiến Nguyên An     | Kiến trúc giải pháp; máy chủ            | Xem xét kiến trúc, dữ liệu, OCR, EPUB, tìm kiếm và bảo mật.         |
| Ngô Nguyễn Thế Khoa   | Phụ trách giao diện                     | Điều phối giao diện, trải nghiệm hiệu chỉnh và trình đọc.           |
| Nguyễn Tuấn Anh       | Máy chủ; vận hành phát triển            | Phát triển API, xác thực, cấu hình môi trường và kiểm tra tích hợp. |
| Nguyễn Quang Thái     | Đảm bảo chất lượng; vận hành phát triển | Thiết kế kiểm thử, hồi quy, bằng chứng và đánh giá sẵn sàng.        |
| Nguyễn Lê Hồ Anh Khoa | Phát triển giao diện                    | Phát triển trình đọc, khả năng sử dụng và kiểm thử giao diện.       |

### 3.2. Trách nhiệm theo hoạt động

| Hoạt động                          | Người chịu trách nhiệm chính  | Người phối hợp hoặc xem xét                       |
| ---------------------------------- | ----------------------------- | ------------------------------------------------- |
| Duy trì baseline và thứ tự ưu tiên | Quản lý dự án                 | Toàn nhóm                                         |
| Làm rõ yêu cầu                     | Quản lý dự án                 | Thành viên liên quan; người dùng tham khảo khi có |
| Quyết định kiến trúc               | Phụ trách kiến trúc           | Người phát triển và người kiểm thử                |
| Phát triển giao diện               | Phụ trách giao diện           | Thành viên giao diện; người kiểm thử              |
| Phát triển máy chủ                 | Phụ trách máy chủ             | Thành viên máy chủ; người kiểm thử                |
| Thiết kế và thực hiện kiểm thử     | Phụ trách đảm bảo chất lượng  | Người phát triển; người xem xét                   |
| Cấu hình môi trường                | Phụ trách vận hành phát triển | Người phát triển và người kiểm thử                |
| Xác nhận hoàn thành                | Người xem xét được chỉ định   | Người chịu trách nhiệm hạng mục; quản lý dự án    |

Một thành viên có thể kiêm nhiệm nhiều vai trò, nhưng mỗi hạng mục phải có đúng một người chịu trách nhiệm chính và ít nhất một người xem xét khác.

### 3.3. Vai trò bên ngoài nhóm

Đại diện nghiệp vụ Thư viện, giảng viên hoặc người dùng đại diện là nguồn tham khảo khi có điều kiện tham gia. Trong phiên bản học tập, sự tham gia của họ không được giả định là phê duyệt vận hành thực tế. Nhóm Sebros chịu trách nhiệm xác nhận nội bộ đối với baseline và kết quả môn học.

## 4. Bảng Kanban và giới hạn công việc

### 4.1. Sáu trạng thái thống nhất

Luồng chính:

`Ý tưởng → Đã sẵn sàng → Đang thực hiện → Đang xem xét → Chờ xác nhận → Hoàn thành`

| Trạng thái     | Mục đích                                                      | Điều kiện vào                                                 | Điều kiện ra                                                |
| -------------- | ------------------------------------------------------------- | ------------------------------------------------------------- | ----------------------------------------------------------- |
| Ý tưởng        | Ghi nhận nhu cầu hoặc công việc chưa đủ thông tin.            | Có mô tả vấn đề hoặc nguồn yêu cầu.                           | Được làm rõ và đạt điều kiện sẵn sàng.                      |
| Đã sẵn sàng    | Tập hợp công việc có thể được kéo vào thực hiện.              | Đạt DoR, có người phụ trách, người xem xét và phụ thuộc rõ.   | Còn năng lực và không vượt giới hạn công việc.              |
| Đang thực hiện | Thực hiện thiết kế, mã nguồn, kiểm thử ban đầu hoặc tài liệu. | Người phụ trách đã bắt đầu và ghi thời điểm bắt đầu.          | Có kết quả đủ để xem xét; tự kiểm tra đã hoàn tất.          |
| Đang xem xét   | Xem xét thay đổi và chạy kiểm thử phù hợp.                    | Có thay đổi, mô tả cách kiểm tra và bằng chứng ban đầu.       | Đạt kiểm tra hoặc được trả lại để sửa.                      |
| Chờ xác nhận   | Chờ xác nhận kết quả nghiệp vụ, tài liệu hoặc bàn giao.       | Kiểm tra kỹ thuật đạt và không còn lỗi chặn.                  | Người có trách nhiệm xác nhận hoặc yêu cầu chỉnh sửa.       |
| Hoàn thành     | Ghi nhận công việc đã đạt DoD.                                | Có kết quả, xem xét, kiểm thử, truy vết và bằng chứng đầy đủ. | Chỉ mở lại khi phát hiện lỗi hoặc thay đổi được chấp thuận. |

Tuần hoàn thành là trường dữ liệu của hạng mục, không tạo thêm cột “Hoàn thành – Tuần X”.

### 4.2. Giới hạn công việc đang thực hiện

| Phạm vi                         | Giới hạn |
| ------------------------------- | -------: |
| Mỗi thành viên ở Đang thực hiện |        1 |
| Toàn nhóm ở Đang thực hiện      |        6 |
| Toàn nhóm ở Đang xem xét        |        4 |

Khi đạt giới hạn, thành viên ưu tiên:

1. Xem xét hoặc kiểm thử công việc đang chờ.
2. Hỗ trợ gỡ công việc bị chặn.
3. Hoàn thiện tài liệu và bằng chứng.
4. Sửa lỗi của hạng mục đang thực hiện.

Ngoại lệ giới hạn phải có lý do, người chịu trách nhiệm, thời hạn kết thúc và được quản lý dự án ghi nhận.

### 4.3. Thông tin bắt buộc của hạng mục

| Trường                  | Nội dung                                                          |
| ----------------------- | ----------------------------------------------------------------- |
| Mã nhận diện            | Mã `LDMS-xxx` hoặc mã công việc quản lý tương ứng.                |
| Tiêu đề                 | Kết quả cần đạt, diễn đạt ngắn gọn.                               |
| Mô tả                   | Câu chuyện người dùng hoặc mục đích của công việc.                |
| Priority                | Bắt buộc, Nên có hoặc Có thể xem xét.                             |
| Ước lượng               | Nhỏ, Vừa hoặc Lớn theo Ước lượng dự án.                           |
| Tiêu chí chấp nhận      | Các điều kiện kiểm thử được, đánh số rõ ràng.                     |
| Người chịu trách nhiệm  | Thành viên chính thực hiện.                                       |
| Người xem xét           | Thành viên khác chịu trách nhiệm xem xét.                         |
| Phụ thuộc               | Hạng mục, dữ liệu, môi trường hoặc quyết định cần có trước.       |
| Trạng thái và thời điểm | Trạng thái hiện tại, ngày bắt đầu, ngày hoàn thành khi có.        |
| Blocker                 | Nguyên nhân, người hỗ trợ, hành động tiếp theo và thời gian chặn. |
| Bằng chứng              | Kết quả kiểm thử, xem xét và xác nhận hoàn thành.                 |

## 5. Quy trình từ yêu cầu đến hoàn thành

### 5.1. Bước 1 — Tiếp nhận và phân loại

1. Ghi nhận nhu cầu, lỗi, yêu cầu thay đổi hoặc công việc quản lý.
2. Xác định nguồn, người dùng bị ảnh hưởng và kết quả mong muốn.
3. Đối chiếu với Yêu cầu phần mềm và Product Backlog.
4. Gắn Priority; công việc ngoài baseline chưa được chuyển sang Đã sẵn sàng.
5. Đưa công việc chưa đủ thông tin vào Ý tưởng.

### 5.2. Bước 2 — Làm rõ và chuẩn bị

1. Viết hoặc cập nhật mô tả và tiêu chí chấp nhận.
2. Nhận diện trường hợp hợp lệ, không hợp lệ, quyền truy cập và lỗi khi phù hợp.
3. Xác định dữ liệu, môi trường, phụ thuộc và ảnh hưởng kiến trúc.
4. Ước lượng công việc, chỉ định người chịu trách nhiệm và người xem xét.
5. Kiểm tra DoR; nếu đạt, chuyển sang Đã sẵn sàng.

### 5.3. Bước 3 — Kéo công việc

1. Kiểm tra giới hạn công việc và năng lực của thành viên.
2. Chọn hạng mục có Priority cao nhất mà các phụ thuộc đã sẵn sàng.
3. Ghi ngày bắt đầu và chuyển sang Đang thực hiện.
4. Không kéo hạng mục mới để thay cho việc xử lý blocker của hạng mục hiện tại.

### 5.4. Bước 4 — Phát triển và tự kiểm tra

1. Đọc yêu cầu, tiêu chí chấp nhận và quyết định kiến trúc liên quan.
2. Thiết kế vừa đủ cho phạm vi hạng mục.
3. Thực hiện thay đổi nhỏ, có thể xem xét và có thể kiểm thử.
4. Viết hoặc cập nhật kiểm thử phù hợp.
5. Tự chạy kiểm tra, cập nhật tài liệu và chuẩn bị mô tả thay đổi.
6. Chuyển sang Đang xem xét khi kết quả đủ điều kiện.

### 5.5. Bước 5 — Xem xét và kiểm thử

1. Người xem xét kiểm tra phạm vi, tiêu chí chấp nhận, bảo mật, dữ liệu và ảnh hưởng tài liệu.
2. Chạy kiểm thử phù hợp với loại thay đổi.
3. Ghi lỗi hoặc yêu cầu sửa bằng mô tả có thể tái hiện.
4. Nếu chưa đạt, chuyển lại Đang thực hiện và giữ lịch sử nhận xét.
5. Nếu đạt kiểm tra kỹ thuật, chuyển sang Chờ xác nhận hoặc Hoàn thành theo DoD.

### 5.6. Bước 6 — Xác nhận và hoàn thành

1. Đối chiếu từng tiêu chí chấp nhận với kết quả thực tế.
2. Kiểm tra truy vết, tài liệu và bằng chứng.
3. Ghi người xác nhận, ngày hoàn thành và tuần hoàn thành.
4. Chuyển sang Hoàn thành khi toàn bộ DoD đạt.
5. Ghi sự kiện hoàn thành trong Nhật ký dự án.

## 6. Điều kiện sẵn sàng và điều kiện hoàn thành

### 6.1. Điều kiện sẵn sàng (DoR)

Một hạng mục chỉ được chuyển sang **Đã sẵn sàng** khi:

- Có mã nhận diện và tiêu đề thống nhất.
- Người dùng, nhu cầu và kết quả mong muốn rõ ràng.
- Tiêu chí chấp nhận cụ thể, kiểm thử được và phù hợp phạm vi.
- Priority và ước lượng đã được xác định.
- Người chịu trách nhiệm và người xem xét đã được chỉ định.
- Phụ thuộc, dữ liệu và môi trường chính đã sẵn sàng hoặc có cách xử lý.
- Ảnh hưởng tới kiến trúc, bảo mật và tài liệu đã được nhận diện.
- Không còn câu hỏi có thể làm thay đổi đáng kể phạm vi.

Nếu thiếu một điều kiện quan trọng, hạng mục ở lại Ý tưởng hoặc được trả lại để làm rõ.

### 6.2. Điều kiện hoàn thành (DoD)

Một hạng mục chỉ được chuyển sang **Hoàn thành** khi:

- Tất cả tiêu chí chấp nhận đạt hoặc có ngoại lệ được nhóm xác nhận.
- Mã nguồn, cấu hình hoặc tài liệu đã được ít nhất một thành viên khác xem xét.
- Kiểm thử phù hợp đã chạy và kết quả thực tế được ghi nhận.
- Không còn lỗi nghiêm trọng chưa được chấp thuận trong phạm vi hạng mục.
- Thay đổi đã được tích hợp vào nhánh chính khi có thay đổi mã nguồn.
- Các kiểm tra tự động đã cấu hình cho phạm vi thay đổi đạt yêu cầu.
- Tài liệu, hướng dẫn và truy vết liên quan đã được cập nhật.
- Có bằng chứng xem xét, kiểm thử và người xác nhận.
- Ngày hoàn thành, tuần hoàn thành và sự kiện hoàn thành đã được ghi nhận.

PoC đạt yêu cầu không tự động làm một hạng mục đạt DoD. Hạng mục sản phẩm vẫn phải được phát triển và kiểm thử theo tiêu chí chấp nhận của chính hạng mục đó.

## 7. Phát triển, xem xét và kiểm thử

### 7.1. Quản lý mã nguồn

- `main` là nhánh tích hợp trung tâm và phải ở trạng thái có thể kiểm tra.
- Nhánh công việc tồn tại trong thời gian ngắn, dùng dạng `task/LDMS-xxx-mo-ta` hoặc `fix/mo-ta`.
- Mỗi thay đổi tập trung vào một mục đích và ghi mã hạng mục khi áp dụng.
- Thành viên cập nhật thay đổi từ `main`, tự kiểm tra và yêu cầu xem xét trước khi hợp nhất.
- Không đưa khóa bí mật, tệp môi trường, dữ liệu thật hoặc tài liệu chưa được phép vào mã nguồn.
- Trường hợp sửa khẩn cấp vẫn cần xem xét và kiểm thử hồi quy phù hợp.

### 7.2. Nội dung xem xét

Người xem xét kiểm tra:

- Thay đổi có đúng phạm vi và tiêu chí chấp nhận không.
- Quy tắc nghiệp vụ có đặt đúng thành phần không.
- Kiểm tra quyền có được thực hiện tại máy chủ không.
- Dữ liệu gốc và dữ liệu đã lưu có được bảo toàn khi lỗi không.
- Mã nguồn có rõ ràng, có thể kiểm thử và không lặp không cần thiết không.
- Kiểm thử có bao phủ luồng chính, lỗi và trường hợp quyền phù hợp không.
- Tài liệu hoặc quyết định kiến trúc có cần cập nhật không.
- Bằng chứng có phản ánh kết quả chạy thực tế không.

Người xem xét không chỉ kiểm tra định dạng. Nhận xét phải nêu vấn đề, tác động và điều kiện cần sửa.

### 7.3. Các mức kiểm thử

| Loại kiểm thử         | Mục đích                                                             | Thời điểm                              |
| --------------------- | -------------------------------------------------------------------- | -------------------------------------- |
| Đơn vị                | Kiểm tra hàm, quy tắc hoặc thành phần độc lập.                       | Trong khi phát triển.                  |
| Tích hợp              | Kiểm tra API, cơ sở dữ liệu, kho tệp và công cụ xử lý phối hợp.      | Trước khi hoàn tất thay đổi liên quan. |
| Chức năng             | Đối chiếu hành vi với tiêu chí chấp nhận.                            | Khi hạng mục vào Đang xem xét.         |
| Giao diện             | Kiểm tra trạng thái, thao tác và hiển thị chính.                     | Với hạng mục giao diện.                |
| Phân quyền và bảo mật | Kiểm tra hợp lệ, không xác thực, sai quyền và truy cập tệp riêng tư. | Với luồng có dữ liệu hoặc quyền.       |
| Hồi quy               | Xác nhận thay đổi không làm hỏng luồng đã đạt.                       | Trước xác nhận hoặc bàn giao.          |
| Chấp nhận nội bộ      | Xác nhận kết quả đáp ứng mục tiêu học tập và tiêu chí đã thống nhất. | Trước khi chuyển Hoàn thành.           |

Chi tiết trường hợp kiểm thử, dữ liệu, kết quả mong đợi và kết quả thực tế được trình bày trong Kế hoạch kiểm thử và bộ bằng chứng.

### 7.4. Tích hợp và bàn giao

- Chỉ hợp nhất thay đổi khi xem xét và kiểm tra bắt buộc đạt.
- Sau hợp nhất, chạy kiểm tra hồi quy phù hợp với ảnh hưởng của thay đổi.
- Môi trường baseline dùng cấu hình đã mô tả trong Kiến trúc phần mềm.
- Nginx hoặc môi trường đám mây chỉ được dùng khi cấu hình tương ứng được xác nhận.
- Không xem kiểm tra sức khỏe kỹ thuật là thay thế cho kiểm thử nghiệp vụ.
- Trước bàn giao, nhóm kiểm tra luồng tải lên → OCR → hiệu chỉnh → tạo EPUB → xuất bản → tìm kiếm → đọc, cùng quyền truy cập và trường hợp lỗi chính.

## 8. Xử lý lỗi, công việc bị chặn và ngoại lệ

### 8.1. Phân loại lỗi

| Mức độ       | Cách hiểu                                                              | Cách xử lý                                                  |
| ------------ | ---------------------------------------------------------------------- | ----------------------------------------------------------- |
| Nghiêm trọng | Mất dữ liệu, lộ dữ liệu, không thể dùng luồng bắt buộc hoặc sai quyền. | Dừng hoàn thành hạng mục; ưu tiên sửa và kiểm thử hồi quy.  |
| Cao          | Chức năng bắt buộc sai nhưng có cách tránh tạm thời.                   | Sửa trước khi xác nhận hoặc có quyết định ngoại lệ rõ ràng. |
| Trung bình   | Ảnh hưởng một trường hợp nhưng không chặn luồng chính.                 | Đưa vào thứ tự ưu tiên và theo dõi trước bàn giao.          |
| Thấp         | Lỗi trình bày hoặc cải tiến nhỏ không ảnh hưởng kết quả chính.         | Ghi nhận và xử lý theo năng lực còn lại.                    |

### 8.2. Quy trình xử lý lỗi

1. Ghi mô tả, môi trường, dữ liệu, bước tái hiện, kết quả mong đợi và thực tế.
2. Xác định mức độ, hạng mục liên quan và người chịu trách nhiệm.
3. Sửa lỗi trên nhánh ngắn và bổ sung kiểm thử ngăn lỗi tái diễn khi phù hợp.
4. Người khác xem xét thay đổi.
5. Chạy lại trường hợp lỗi và kiểm thử hồi quy liên quan.
6. Cập nhật bằng chứng và trạng thái lỗi.

### 8.3. Công việc bị chặn

Một hạng mục được đánh dấu bị chặn khi không thể tiếp tục do phụ thuộc, lỗi môi trường, thiếu dữ liệu, thiếu quyết định hoặc cần hỗ trợ ngoài khả năng của người phụ trách.

Thông tin bắt buộc:

- Thời điểm bắt đầu bị chặn.
- Nguyên nhân và ảnh hưởng.
- Người có thể hỗ trợ.
- Hành động tiếp theo và thời hạn kiểm tra lại.
- Thời điểm gỡ chặn và tổng thời gian bị chặn.

Thành viên báo blocker trong ngày phát hiện. Nhóm ưu tiên gỡ blocker trước khi kéo thêm việc. Nếu bị chặn quá hai ngày lịch, quản lý dự án phải điều chỉnh phụ thuộc, đổi thứ tự thực hiện hoặc đề xuất thay đổi phạm vi hay năng lực.

### 8.4. Ngoại lệ quy trình

Ngoại lệ phải ghi:

- Quy tắc được xin ngoại lệ.
- Lý do và thời hạn.
- Rủi ro phát sinh.
- Người chấp thuận.
- Biện pháp bù và điều kiện kết thúc.

Ngoại lệ không được dùng để bỏ qua kiểm tra quyền, bảo vệ dữ liệu hoặc tạo bằng chứng không đúng thực tế.

## 9. Quản lý phạm vi và thay đổi

### 9.1. Thay đổi trong hạng mục đã duyệt

Người phụ trách có thể điều chỉnh chi tiết triển khai khi không làm thay đổi mục tiêu, Priority, tiêu chí chấp nhận hoặc kiến trúc đã xác nhận. Thay đổi vẫn phải được người xem xét kiểm tra.

### 9.2. Thay đổi ảnh hưởng baseline

Đề xuất thay đổi phải nêu:

- Vấn đề và lý do.
- Hạng mục, yêu cầu và tài liệu bị ảnh hưởng.
- Tác động tới 11 tuần, 190 giờ-người kế hoạch và 8 giờ-người dự phòng.
- Tác động tới kiến trúc, kiểm thử, rủi ro và chất lượng.
- Phương án chấp thuận, hoãn, thay thế hoặc từ chối.
- Người xác nhận và ngày hiệu lực.

Không tự hạ DoD hoặc tiêu chí chấp nhận để bù tiến độ. Khi năng lực dự báo không đủ 190 giờ-người, nhóm phải xem xét giảm phạm vi được phép hoặc điều chỉnh năng lực trước khi thay đổi chất lượng.

### 9.3. Hạng mục ngoài baseline

- Hạng mục Nên có chỉ được kéo khi các hạng mục Bắt buộc không bị ảnh hưởng.
- Hạng mục Có thể xem xét cần quyết định bổ sung phạm vi.
- Có mã nguồn thử nghiệm không đồng nghĩa hạng mục đã được đưa vào baseline.
- PoC không làm thay đổi Priority hoặc trạng thái hoàn thành của Product Backlog.

## 10. Truy vết và bằng chứng

### 10.1. Chuỗi truy vết

`YC-xxx → LDMS-xxx → Thay đổi → Trường hợp kiểm thử → Kết quả → Xác nhận hoàn thành`

| Thành phần         | Nội dung cần truy vết                                           |
| ------------------ | --------------------------------------------------------------- |
| Yêu cầu            | Mã `YC-xxx` và `YCP-xx` liên quan.                              |
| Product Backlog    | Mã `LDMS-xxx`, Priority, ước lượng và tiêu chí chấp nhận.       |
| Thay đổi           | Nhánh, thay đổi mã nguồn, cấu hình hoặc tài liệu.               |
| Kiểm thử           | Mã trường hợp, dữ liệu, kết quả mong đợi và kết quả thực tế.    |
| Xem xét            | Người xem xét, nhận xét và kết quả xử lý.                       |
| Bằng chứng         | Kết quả chạy, ảnh giao diện, nhật ký hoặc biên bản khi phù hợp. |
| Sự kiện hoàn thành | Ngày, tuần, người xác nhận và tài liệu bị ảnh hưởng.            |

Mã `YC-001`–`YC-026` truy vết một-một với `LDMS-001`–`LDMS-026` cùng số thứ tự. Yêu cầu phi chức năng dùng mã `YCP` và được gắn vào kiểm thử liên quan.

### 10.2. Yêu cầu đối với bằng chứng

Bằng chứng phải:

- Được tạo từ kết quả thực tế, không từ dự đoán.
- Có thể xác định hạng mục, người thực hiện và thời điểm.
- Thể hiện đủ điều kiện cần xác nhận.
- Không chứa khóa bí mật, dữ liệu cá nhân hoặc tài liệu chưa được phép.
- Được mô tả bằng tên tài liệu hoặc mã bằng chứng, không phụ thuộc vào đường dẫn thư mục trong bản in.

## 11. Đo lường và cải tiến

### 11.1. Chỉ số

| Chỉ số                       | Cách tính hoặc ghi nhận                                              | Mục đích                                           |
| ---------------------------- | -------------------------------------------------------------------- | -------------------------------------------------- |
| Số việc đang thực hiện       | Số hạng mục ở Đang thực hiện và Đang xem xét.                        | Phát hiện quá tải và vi phạm giới hạn.             |
| Thời gian chu kỳ             | Từ lúc vào Đang thực hiện đến lúc vào Hoàn thành.                    | Đánh giá tốc độ hoàn thành luồng.                  |
| Thông lượng                  | Số hạng mục chuyển Hoàn thành trong một tuần.                        | Theo dõi khả năng bàn giao của nhóm.               |
| Thời gian bị chặn            | Tổng thời gian hạng mục ở trạng thái bị chặn.                        | Nhận diện phụ thuộc và điểm nghẽn.                 |
| Tuổi công việc               | Thời gian hạng mục hiện tại đã ở Đang thực hiện hoặc Đang xem xét.   | Phát hiện công việc kéo dài bất thường.            |
| Tỷ lệ đạt lần đầu            | Số hạng mục đạt lần xem xét đầu chia số hạng mục được xem xét.       | Phát hiện thiếu sót khi chuẩn bị hoặc tự kiểm tra. |
| Công việc làm lại            | Công sức sửa do yêu cầu, thiết kế, mã nguồn hoặc kiểm thử chưa đúng. | Tìm nguyên nhân gây lãng phí.                      |
| Lỗi phát hiện sau hoàn thành | Số lỗi được ghi sau khi hạng mục đã Hoàn thành.                      | Đánh giá hiệu quả DoD và kiểm thử hồi quy.         |

### 11.2. Nhịp theo dõi

| Hoạt động           | Tần suất                                          | Nội dung                                                 |
| ------------------- | ------------------------------------------------- | -------------------------------------------------------- |
| Cập nhật trạng thái | Mỗi ngày có làm dự án                             | Việc đã làm, việc tiếp theo và blocker.                  |
| Xem xét luồng       | Hai lần mỗi tuần hoặc khi có blocker nghiêm trọng | Giới hạn công việc, tuổi việc, thời gian chặn và hỗ trợ. |
| Xem xét tuần        | Cuối tuần                                         | Thông lượng, hoàn thành, dự báo, rủi ro và thay đổi.     |
| Cải tiến quy trình  | Khi có lỗi lặp lại hoặc sau mốc quan trọng        | Nguyên nhân, hành động, người phụ trách và thời hạn.     |

### 11.3. Cách cải tiến

1. Chọn vấn đề dựa trên dữ liệu luồng hoặc lỗi lặp lại.
2. Xác định nguyên nhân có thể kiểm chứng.
3. Chọn một thay đổi quy trình nhỏ.
4. Ghi người phụ trách và thời gian đánh giá.
5. So sánh kết quả trước và sau.
6. Giữ thay đổi nếu có lợi; hoàn nguyên hoặc điều chỉnh nếu không hiệu quả.
7. Cập nhật tài liệu khi thay đổi trở thành quy tắc chung.

## 12. Sử dụng công cụ hỗ trợ và AI

### 12.1. Công cụ quản lý và phát triển

- Bảng Kanban là nguồn trạng thái công việc đang thực hiện.
- Product Backlog là nguồn Priority, ước lượng và tiêu chí chấp nhận.
- Hệ thống quản lý mã nguồn ghi thay đổi và hoạt động xem xét.
- Bộ kiểm thử ghi trường hợp và kết quả kiểm tra.
- Nhật ký dự án ghi sự kiện hoàn thành, quyết định và thay đổi quan trọng.

Khi thông tin khác nhau, nhóm phải xác định tài liệu nguồn theo loại dữ liệu và cập nhật các bản ghi bị ảnh hưởng; không duy trì hai trạng thái khác nhau cho cùng một hạng mục.

### 12.2. Sử dụng AI

AI có thể hỗ trợ phân tích, thiết kế, viết mã, viết kiểm thử, rà soát, gỡ lỗi và viết tài liệu. Thành viên sử dụng AI vẫn chịu trách nhiệm về kết quả.

Quy tắc bắt buộc:

- Không đưa khóa bí mật, dữ liệu cá nhân hoặc tài liệu chưa được phép vào công cụ AI.
- Nội dung do AI tạo phải được con người đọc, kiểm tra và xem xét.
- Không dùng tuyên bố của AI thay cho kết quả chạy kiểm thử.
- Không tạo số liệu, nhật ký, bằng chứng hoặc chữ ký không có thật.
- Chỉ ghi token, chi phí hoặc thời gian khi có số đo đáng tin cậy.
- Thành viên phải có khả năng giải thích thay đổi trước khi hợp nhất hoặc xác nhận.

## 13. Tài liệu tham khảo

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
