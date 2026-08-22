# DANH MỤC CÔNG VIỆC

## Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS (HCMUS-LDMS)

### THÔNG TIN TÀI LIỆU

| Trường thông tin             | Nội dung                                            |
| ---------------------------- | --------------------------------------------------- |
| Mã tài liệu                  | `HCMUS-LDMS-PBL`                                    |
| Tên tài liệu                 | Danh mục công việc                                  |
| Đơn vị soạn thảo             | Sebros – Nhóm sinh viên đề xuất dự án               |
| Người thực hiện              | Mạch Quốc Tấn                                       |
| Người xem xét                | Đại diện nhóm Sebros và Đại diện nghiệp vụ Thư viện |
| Trạng thái tài liệu          | Bản dự thảo để xem xét                              |
| Cách tổ chức                 | Kanban, luồng công việc liên tục                    |
| Thời gian phiên bản đầu tiên | 11 tuần                                             |

### LỊCH SỬ PHIÊN BẢN

| Phiên bản | Ngày       | Mô tả thay đổi                                                                                                                                                                                 | Người thực hiện |
| --------- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| 1.0       | 11/07/2026 | Khởi tạo danh mục công việc.                                                                                                                                                                   | Mạch Quốc Tấn   |
| 2.0       | 14/07/2026 | Bổ sung câu chuyện người dùng, tiêu chí chấp nhận và mức độ ưu tiên.                                                                                                                           | Mạch Quốc Tấn   |
| 3.0       | 15/07/2026 | Cập nhật phụ thuộc, quy tắc hoàn thành và nhóm chức năng.                                                                                                                                      | Mạch Quốc Tấn   |
| 4.0       | 21/08/2026 | Rà soát toàn bộ danh mục theo yêu cầu phần mềm, loại bỏ cách chia theo đợt cố định, sửa nội dung trùng lặp, thống nhất Kanban 11 tuần và phân biệt phạm vi bắt buộc với chức năng xem xét sau. | Mạch Quốc Tấn   |
| 5.0       | 22/08/2026 | Đồng bộ SOW 15/6/5, workflow Kanban, cỡ effort, evidence và điều kiện đưa chức năng tùy chọn vào phạm vi. | Mạch Quốc Tấn |

## Mục lục

- [Mục đích và cách quản lý](#1-mục-đích-và-cách-quản-lý)
- [Điều kiện sẵn sàng và hoàn thành](#2-điều-kiện-sẵn-sàng-và-hoàn-thành)
- [Mức độ ưu tiên và trường thông tin](#3-mức-độ-ưu-tiên-và-trường-thông-tin)
- [Danh sách câu chuyện người dùng](#4-danh-sách-câu-chuyện-người-dùng)
- [Luồng Kanban trong 11 tuần](#5-luồng-kanban-trong-11-tuần)
- [Truy vết và quản lý thay đổi](#6-truy-vết-và-quản-lý-thay-đổi)
- [Tài liệu tham khảo](#7-tài-liệu-tham-khảo)

## 1. Mục đích và cách quản lý

Danh mục công việc chuyển các yêu cầu trong [Yêu cầu phần mềm](04-software-requirements.md) thành các câu chuyện người dùng có thể thực hiện, kiểm thử và nghiệm thu. Danh mục là tài liệu sống: nhóm liên tục lấy công việc phù hợp từ cột chờ thực hiện, giới hạn số việc đang làm, đưa việc đã đạt tiêu chí sang hoàn thành và cập nhật mức ưu tiên khi có quyết định mới.

Các cột Kanban được sử dụng: **Ý tưởng**, **Đã sẵn sàng**, **Đang thực hiện**, **Đang xem xét**, **Chờ xác nhận**, **Hoàn thành**. Một công việc chỉ được chuyển sang cột tiếp theo khi đáp ứng điều kiện của cột đó. Không chia công việc theo các đợt phát triển cố định hoặc khẳng định tất cả chức năng tùy chọn sẽ hoàn thành trong 11 tuần.

Tài liệu này là baseline nội dung; trạng thái vận hành nằm trên board. Mỗi card trên board phải có owner, reviewer, ngày bắt đầu, blocked reason khi có, ngày hoàn thành và liên kết evidence. Không suy trạng thái Done từ việc mã story xuất hiện trong [Nhật ký dự án](17-project-log.md).

Nhóm thực hiện gồm 6 sinh viên chuyên ngành Kỹ thuật phần mềm. Người xem xét nghiệp vụ là Đại diện nghiệp vụ Thư viện; người điều phối và chịu trách nhiệm cập nhật danh mục là Đại diện nhóm Sebros.

## 2. Điều kiện sẵn sàng và hoàn thành

### Điều kiện đưa vào cột Đã sẵn sàng

- Có người sử dụng, nhu cầu và kết quả mong muốn rõ ràng.
- Có tiêu chí chấp nhận kiểm thử được.
- Có mức độ ưu tiên, cỡ công việc và phụ thuộc chính.
- Đã xác định yêu cầu phần mềm liên quan và người xem xét.
- Không còn câu hỏi quan trọng có thể làm nhóm hiểu khác nhau về phạm vi.

### Điều kiện chuyển sang Hoàn thành

- Đã hoàn thành mã nguồn hoặc tài liệu cần thiết và đã được xem xét.
- Kiểm thử phù hợp đã chạy; các tiêu chí chấp nhận đều đạt.
- Không còn lỗi nghiêm trọng chưa xử lý trong phạm vi câu chuyện người dùng.
- Đã cập nhật hướng dẫn, yêu cầu, truy vết hoặc cấu hình liên quan.
- Đã trình bày kết quả cho người có trách nhiệm xác nhận.
- Có liên kết commit/PR, kiểm thử và xác nhận tương ứng; trường hợp ngoại lệ đã được phê duyệt bằng văn bản.

## 3. Mức độ ưu tiên và trường thông tin

Mức độ ưu tiên được dùng để quyết định thứ tự lấy việc, không phải cam kết tuyệt đối về thời điểm hoàn thành:

- **Bắt buộc:** cần cho phạm vi phiên bản đầu tiên.
- **Nên có:** có giá trị rõ ràng nhưng có thể lùi nếu ảnh hưởng đến phạm vi 11 tuần.
- **Có thể xem xét:** ứng viên sau khi phạm vi bắt buộc đã hoàn thành; không đưa vào cam kết cơ sở.

Mỗi câu chuyện người dùng có mã, vai trò, nhu cầu, kết quả, mức độ, cỡ, phụ thuộc, yêu cầu liên quan và tiêu chí chấp nhận. Cỡ công việc dùng cùng quy ước với [Ước lượng dự án](10-project-estimate.md): Nhỏ = 4–8 giờ-người, Vừa = 8–16 giờ-người, Lớn = 16–32 giờ-người và phải phân rã hoặc PoC trước khi kéo. Effort bao gồm test, review, sửa lỗi và tài liệu để đạt DoD.

## 4. Danh sách câu chuyện người dùng

### 4.1. Nền tảng, tài khoản và phân quyền

| Mã       | Câu chuyện người dùng                                                                                                  | Mức độ   | Cỡ  | Phụ thuộc | Truy vết                     |
| -------- | ---------------------------------------------------------------------------------------------------------------------- | -------- | --- | --------- | ---------------------------- |
| LDMS-001 | Là thành viên nhóm, tôi muốn có cấu trúc mã nguồn và môi trường chạy thống nhất để phát triển và kiểm thử.             | Bắt buộc | Vừa | Không     | YC-PN-07, YC-PN-09           |
| LDMS-009 | Là người dùng phát triển, tôi muốn đăng nhập bằng dữ liệu mô phỏng để kiểm thử các luồng chính.                        | Bắt buộc | Nhỏ | LDMS-001  | YC-HT-01, YC-HT-02           |
| LDMS-018 | Là người dùng, tôi muốn đăng nhập bằng Google OAuth 2.0 khi môi trường triển khai hỗ trợ để sử dụng tài khoản phù hợp. | Nên có   | Vừa | LDMS-009  | YC-HT-01                     |
| LDMS-010 | Là quản trị viên, tôi muốn gán vai trò và quyền để kiểm soát chức năng được phép sử dụng.                              | Bắt buộc | Vừa | LDMS-009  | YC-HT-03, YC-HT-04, YC-PN-01 |

### 4.2. Tiếp nhận, nhận dạng ký tự và hiệu chỉnh

| Mã       | Câu chuyện người dùng                                                                                 | Mức độ   | Cỡ  | Phụ thuộc          | Truy vết                     |
| -------- | ----------------------------------------------------------------------------------------------------- | -------- | --- | ------------------ | ---------------------------- |
| LDMS-002 | Là thủ thư, tôi muốn tải tài liệu gốc lên và nhận thông báo kết quả để bắt đầu số hóa.                | Bắt buộc | Vừa | LDMS-001, LDMS-010 | YC-TL-01, YC-TL-02, YC-TL-03 |
| LDMS-003 | Là thủ thư, tôi muốn yêu cầu nhận dạng ký tự và theo dõi trạng thái để biết tài liệu đang ở bước nào. | Bắt buộc | Vừa | LDMS-002           | YC-ND-01, YC-ND-02, YC-PN-03 |
| LDMS-004 | Là biên tập viên, tôi muốn xem kết quả nhận dạng theo từng trang để đối chiếu với bản gốc.            | Bắt buộc | Vừa | LDMS-003           | YC-ND-03, YC-ND-04           |
| LDMS-005 | Là biên tập viên, tôi muốn lưu văn bản đã hiệu chỉnh để giữ lại kết quả sửa lỗi.                      | Bắt buộc | Vừa | LDMS-004           | YC-ND-05, YC-PN-08           |
| LDMS-006 | Là biên tập viên, tôi muốn xem song song bản gốc và văn bản để sửa lỗi chính xác hơn.                 | Nên có   | Vừa | LDMS-004           | YC-ND-06, YC-PN-05           |
| LDMS-017 | Là biên tập viên, tôi muốn chuyển nhanh giữa các trang khi hiệu chỉnh để xử lý tài liệu thuận tiện.   | Nên có   | Nhỏ | LDMS-006           | YC-ND-06                     |
| LDMS-022 | Là biên tập viên, tôi muốn yêu cầu xử lý lại tác vụ thất bại và xem lỗi chính để tiếp tục công việc.  | Nên có   | Nhỏ | LDMS-003           | YC-ND-07, YC-QL-02           |

### 4.3. Siêu dữ liệu, danh mục và xuất bản

| Mã       | Câu chuyện người dùng                                                                                                     | Mức độ   | Cỡ  | Phụ thuộc          | Truy vết                     |
| -------- | ------------------------------------------------------------------------------------------------------------------------- | -------- | --- | ------------------ | ---------------------------- |
| LDMS-026 | Là thủ thư, tôi muốn xem danh sách tài liệu cùng trạng thái để quản lý hồ sơ đang xử lý.                                  | Bắt buộc | Nhỏ | LDMS-002           | YC-TL-06                     |
| LDMS-011 | Là thủ thư, tôi muốn nhập và sửa thông tin mô tả tài liệu để độc giả nhận biết đúng tài liệu.                         | Bắt buộc | Vừa | LDMS-002           | YC-TL-04                     |
| LDMS-012 | Là quản trị viên, tôi muốn quản lý danh mục để tài liệu được phân loại thống nhất.                                        | Nên có   | Vừa | LDMS-010           | YC-TL-05, YC-QL-01           |
| LDMS-007 | Là biên tập viên, tôi muốn tạo bản EPUB từ nội dung đã hiệu chỉnh để chuẩn bị xuất bản.                                   | Bắt buộc | Vừa | LDMS-005, LDMS-011 | YC-PH-04, YC-PN-03           |
| LDMS-013 | Là biên tập viên, tôi muốn hệ thống kiểm tra điều kiện trước khi xuất bản để tránh đưa tài liệu chưa hoàn chỉnh ra ngoài. | Bắt buộc | Nhỏ | LDMS-007, LDMS-011 | YC-PH-01, YC-PH-02, YC-PH-03 |
| LDMS-023 | Là quản trị viên, tôi muốn xem nhật ký thao tác quan trọng để hỗ trợ kiểm tra và truy vết.                                | Nên có   | Nhỏ | LDMS-010           | YC-QL-03, YC-PN-10           |

### 4.4. Tìm kiếm và đọc trực tuyến

| Mã       | Câu chuyện người dùng                                                                                        | Mức độ         | Cỡ  | Phụ thuộc          | Truy vết                               |
| -------- | ------------------------------------------------------------------------------------------------------------ | -------------- | --- | ------------------ | -------------------------------------- |
| LDMS-015 | Là độc giả, tôi muốn tìm kiếm toàn văn trong tài liệu đã xuất bản để tìm nội dung cần đọc.                   | Bắt buộc       | Vừa | LDMS-007, LDMS-013 | YC-TC-01, YC-TC-02, YC-TC-03, YC-PN-04 |
| LDMS-016 | Là độc giả, tôi muốn thấy thông tin phù hợp trong kết quả tìm kiếm để chọn đúng tài liệu.                    | Bắt buộc       | Nhỏ | LDMS-015, LDMS-011 | YC-TC-04                               |
| LDMS-008 | Là độc giả, tôi muốn đọc tài liệu EPUB đã xuất bản trên trình đọc trực tuyến.                                | Bắt buộc       | Vừa | LDMS-013           | YC-PH-05, YC-TC-05                     |
| LDMS-014 | Là độc giả, tôi muốn hệ thống kiểm tra quyền và không hiển thị nút tải tệp EPUB gốc để tài liệu được bảo vệ. | Bắt buộc       | Vừa | LDMS-008, LDMS-010 | YC-PH-06, YC-TC-06, YC-PN-02           |
| LDMS-019 | Là độc giả, tôi muốn điều chỉnh một số thiết lập đọc cơ bản để đọc thuận tiện hơn.                           | Có thể xem xét | Nhỏ | LDMS-008           | YC-TC-07                               |

### 4.5. Ứng viên sau phạm vi phiên bản đầu tiên

Các công việc sau không thuộc cam kết cơ sở 11 tuần. Chỉ đưa vào luồng khi Đại diện nhóm Sebros và Đại diện nghiệp vụ Thư viện xác nhận phạm vi bắt buộc đã ổn định:

| Mã       | Câu chuyện người dùng                                                    | Mức độ         | Lý do chưa đưa vào phạm vi cơ sở                                                                        |
| -------- | ------------------------------------------------------------------------ | -------------- | ------------------------------------------------------------------------------------------------------- |
| LDMS-020 | Là độc giả, tôi muốn lưu vị trí đọc để quay lại sau.                     | Có thể xem xét | Không thiết yếu cho luồng số hóa và đọc tối thiểu.                                                      |
| LDMS-021 | Là độc giả, tôi muốn đánh dấu hoặc ghi chú nội dung.                     | Có thể xem xét | Cần thống nhất cách lưu và quyền riêng tư của ghi chú.                                                  |
| LDMS-024 | Là độc giả, tôi muốn tạo trích dẫn từ tài liệu.                          | Có thể xem xét | Cần chốt quy tắc định dạng và dữ liệu thư mục.                                                          |
| LDMS-025 | Là quản trị viên, tôi muốn mở rộng công cụ tìm kiếm khi kho dữ liệu lớn. | Có thể xem xét | Phiên bản đầu tiên dùng tìm kiếm toàn văn của PostgreSQL; chưa có dữ liệu chứng minh cần công cụ riêng. |

### 4.6. Tiêu chí chấp nhận theo mã

| Mã | Tiêu chí chấp nhận trọng tâm |
|---|---|
| LDMS-001 | Thành viên có thể cài đặt, khởi chạy và kiểm tra hệ thống theo hướng dẫn thống nhất. |
| LDMS-009 | Tài khoản thử nghiệm đăng nhập được; thông tin xác thực sai hoặc thiếu bị từ chối. |
| LDMS-018 | Khi được cấu hình, người dùng đăng nhập được bằng Google OAuth 2.0; lỗi xác thực được thông báo rõ. |
| LDMS-010 | Quản trị viên gán được vai trò; người không đủ quyền bị từ chối ở cả giao diện và máy chủ. |
| LDMS-002 | Tệp hợp lệ được tiếp nhận và lưu; tệp sai loại hoặc vượt giới hạn bị từ chối kèm lý do. |
| LDMS-003 | Người có quyền khởi chạy nhận dạng ký tự; trạng thái chờ, đang xử lý, hoàn tất hoặc thất bại được hiển thị. |
| LDMS-004 | Kết quả văn bản gắn đúng tài liệu hoặc trang và có thể đối chiếu với bản gốc. |
| LDMS-005 | Nội dung đã sửa được lưu, mở lại vẫn giữ đúng thay đổi và không làm mất bản gốc. |
| LDMS-006 | Màn hình hiển thị được nội dung gốc và văn bản tương ứng để người biên tập đối chiếu. |
| LDMS-017 | Người biên tập chuyển được giữa các trang mà không mất phần đang lưu. |
| LDMS-022 | Tác vụ thất bại có thông tin lỗi; người có quyền có thể yêu cầu xử lý lại. |
| LDMS-026 | Danh sách hiển thị đúng tài liệu người dùng được phép quản lý và trạng thái hiện tại. |
| LDMS-011 | Siêu dữ liệu bắt buộc được kiểm tra; dữ liệu hợp lệ được lưu và hiển thị lại chính xác. |
| LDMS-012 | Quản trị viên tạo, sửa hoặc ẩn được danh mục; tài liệu được gắn danh mục phù hợp. |
| LDMS-007 | Nội dung đã hiệu chỉnh tạo được tệp EPUB mở được bằng trình đọc hỗ trợ. |
| LDMS-013 | Tài liệu thiếu nội dung hoặc thông tin mô tả tài liệu bắt buộc không thể xuất bản và nêu được lý do. |
| LDMS-023 | Thao tác quan trọng được ghi nhận tối thiểu người thực hiện, hành động và thời điểm. |
| LDMS-015 | Từ khóa tìm được nội dung trong tài liệu đã xuất bản; tài liệu chưa xuất bản không xuất hiện. |
| LDMS-016 | Kết quả hiển thị thông tin nhận biết và liên kết mở tài liệu phù hợp. |
| LDMS-008 | Người có quyền mở được tài liệu EPUB đã xuất bản trên trình đọc trực tuyến. |
| LDMS-014 | Người không có quyền không đọc được; giao diện độc giả không có nút tải tệp EPUB gốc. |
| LDMS-019 | Nếu được đưa vào phiên bản triển khai, thiết lập đọc được lưu trong phiên đọc và không ảnh hưởng nội dung gốc. |
| LDMS-020, LDMS-021, LDMS-024, LDMS-025 | Chỉ thực hiện sau khi được chấp thuận bổ sung; phải có tiêu chí chi tiết riêng trước khi chuyển sang Đã sẵn sàng. |

### 4.7. Mô tả chi tiết từng hạng mục

Phần này là thông tin chi tiết dùng để đưa từng hạng mục vào bảng Kanban. Mỗi hạng mục có đủ vai trò, nhu cầu, kết quả, ưu tiên, cỡ, phụ thuộc, yêu cầu liên quan và tiêu chí chấp nhận.

#### LDMS-001 — Chuẩn bị môi trường và cấu trúc mã nguồn

- **Vai trò:** Thành viên nhóm phát triển.
- **Nhu cầu:** Có cấu trúc mã nguồn và môi trường chạy thống nhất.
- **Kết quả:** Thành viên có thể cài đặt, khởi chạy và kiểm tra hệ thống.
- **Mức độ:** Bắt buộc.
- **Cỡ:** Vừa.
- **Phụ thuộc:** Không có.
- **Yêu cầu liên quan:** YC-PN-07, YC-PN-09.
- **Tiêu chí chấp nhận:**
  - Mã nguồn giao diện, máy chủ và cấu hình chạy được tổ chức rõ ràng.
  - Thành viên mới có thể chạy hệ thống theo hướng dẫn.
  - Môi trường phát triển và dữ liệu thử nghiệm được tách khỏi dữ liệu thật.

#### LDMS-009 — Đăng nhập bằng dữ liệu mô phỏng

- **Vai trò:** Người dùng phát triển.
- **Nhu cầu:** Đăng nhập nhanh để kiểm thử các luồng chính.
- **Kết quả:** Tài khoản thử nghiệm tạo được phiên làm việc hợp lệ.
- **Mức độ:** Bắt buộc.
- **Cỡ:** Nhỏ.
- **Phụ thuộc:** LDMS-001.
- **Yêu cầu liên quan:** YC-HT-01, YC-HT-02.
- **Tiêu chí chấp nhận:**
  - Tài khoản thử nghiệm hợp lệ đăng nhập được.
  - Thông tin xác thực sai hoặc thiếu bị từ chối.
  - Người dùng có thể kết thúc phiên làm việc.

#### LDMS-018 — Đăng nhập bằng Google OAuth 2.0

- **Vai trò:** Người dùng hệ thống.
- **Nhu cầu:** Đăng nhập bằng tài khoản phù hợp khi môi trường triển khai hỗ trợ.
- **Kết quả:** Người dùng được xác thực và tạo phiên làm việc.
- **Mức độ:** Nên có.
- **Cỡ:** Vừa.
- **Phụ thuộc:** LDMS-009.
- **Yêu cầu liên quan:** YC-HT-01.
- **Tiêu chí chấp nhận:**
  - Người dùng đăng nhập được khi thông tin cấu hình hợp lệ.
  - Thông tin xác thực không hợp lệ không tạo được phiên.
  - Lỗi xác thực được thông báo mà không làm lộ thông tin nhạy cảm.

#### LDMS-010 — Phân quyền theo vai trò

- **Vai trò:** Quản trị viên.
- **Nhu cầu:** Gán vai trò và quyền để kiểm soát chức năng được sử dụng.
- **Kết quả:** Người dùng chỉ thực hiện được thao tác phù hợp với quyền.
- **Mức độ:** Bắt buộc.
- **Cỡ:** Vừa.
- **Phụ thuộc:** LDMS-009.
- **Yêu cầu liên quan:** YC-HT-03, YC-HT-04, YC-PN-01.
- **Tiêu chí chấp nhận:**
  - Quản trị viên gán và thay đổi được vai trò.
  - Người không đủ quyền bị từ chối ở cả giao diện và máy chủ.
  - Việc thay đổi quyền có hiệu lực cho các yêu cầu tiếp theo.

#### LDMS-002 — Tải tài liệu gốc lên hệ thống

- **Vai trò:** Thủ thư hoặc biên tập viên.
- **Nhu cầu:** Đưa tài liệu vào hệ thống để bắt đầu số hóa.
- **Kết quả:** Tệp hợp lệ được tiếp nhận và lưu an toàn.
- **Mức độ:** Bắt buộc.
- **Cỡ:** Vừa.
- **Phụ thuộc:** LDMS-001, LDMS-010.
- **Yêu cầu liên quan:** YC-TL-01, YC-TL-02, YC-TL-03.
- **Tiêu chí chấp nhận:**
  - Người có quyền tải được tệp đúng loại và trong giới hạn cho phép.
  - Tệp sai loại hoặc vượt giới hạn bị từ chối kèm lý do.
  - Tệp được lưu mà không làm mất hoặc ghi đè tệp gốc khác.

#### LDMS-003 — Khởi chạy và theo dõi nhận dạng ký tự

- **Vai trò:** Thủ thư hoặc biên tập viên.
- **Nhu cầu:** Chuyển nội dung trong bản quét thành văn bản và biết tiến độ xử lý.
- **Kết quả:** Tác vụ nhận dạng có trạng thái rõ ràng.
- **Mức độ:** Bắt buộc.
- **Cỡ:** Vừa.
- **Phụ thuộc:** LDMS-002.
- **Yêu cầu liên quan:** YC-ND-01, YC-ND-02, YC-PN-03.
- **Tiêu chí chấp nhận:**
  - Người có quyền khởi chạy tác vụ cho tài liệu đã tiếp nhận.
  - Trạng thái chờ xử lý, đang xử lý, hoàn tất hoặc thất bại được hiển thị.
  - Tác vụ chạy nền không làm treo thao tác giao diện chính.

#### LDMS-004 — Xem kết quả nhận dạng theo trang

- **Vai trò:** Biên tập viên.
- **Nhu cầu:** Đối chiếu văn bản nhận dạng với bản gốc.
- **Kết quả:** Văn bản được gắn đúng tài liệu và trang tương ứng.
- **Mức độ:** Bắt buộc.
- **Cỡ:** Vừa.
- **Phụ thuộc:** LDMS-003.
- **Yêu cầu liên quan:** YC-ND-03, YC-ND-04.
- **Tiêu chí chấp nhận:**
  - Người dùng mở được ảnh hoặc PDF gốc.
  - Văn bản nhận dạng hiển thị đúng tài liệu và trang.
  - Trường hợp không có kết quả phải có thông báo rõ ràng.

#### LDMS-005 — Lưu văn bản đã hiệu chỉnh

- **Vai trò:** Biên tập viên.
- **Nhu cầu:** Sửa lỗi nhận dạng và giữ lại nội dung đã sửa.
- **Kết quả:** Nội dung hiệu chỉnh được lưu và mở lại chính xác.
- **Mức độ:** Bắt buộc.
- **Cỡ:** Vừa.
- **Phụ thuộc:** LDMS-004.
- **Yêu cầu liên quan:** YC-ND-05, YC-PN-08.
- **Tiêu chí chấp nhận:**
  - Người dùng sửa và lưu được văn bản.
  - Nội dung đã lưu vẫn giữ nguyên khi mở lại.
  - Việc lưu văn bản không làm mất bản gốc.

#### LDMS-006 — Hiệu chỉnh song song bản gốc và văn bản

- **Vai trò:** Biên tập viên.
- **Nhu cầu:** So sánh trực tiếp bản gốc với văn bản nhận dạng.
- **Kết quả:** Giao diện hỗ trợ hiệu chỉnh chính xác hơn.
- **Mức độ:** Nên có.
- **Cỡ:** Vừa.
- **Phụ thuộc:** LDMS-004.
- **Yêu cầu liên quan:** YC-ND-06, YC-PN-05.
- **Tiêu chí chấp nhận:**
  - Bản gốc và văn bản tương ứng cùng hiển thị trên một màn hình.
  - Người dùng xác định được trang đang đối chiếu.
  - Việc chuyển trang không làm mất nội dung chưa lưu nếu hệ thống đã cảnh báo.

#### LDMS-017 — Chuyển trang khi hiệu chỉnh

- **Vai trò:** Biên tập viên.
- **Nhu cầu:** Xử lý nhiều trang liên tục mà không phải mở lại tài liệu.
- **Kết quả:** Người dùng chuyển được giữa các trang một cách thuận tiện.
- **Mức độ:** Nên có.
- **Cỡ:** Nhỏ.
- **Phụ thuộc:** LDMS-006.
- **Yêu cầu liên quan:** YC-ND-06.
- **Tiêu chí chấp nhận:**
  - Người dùng chuyển đến trang trước và trang sau.
  - Hệ thống hiển thị đúng nội dung của trang được chọn.
  - Nội dung đã lưu trước đó không bị thay đổi.

#### LDMS-022 — Xử lý lại tác vụ thất bại

- **Vai trò:** Biên tập viên.
- **Nhu cầu:** Tiếp tục xử lý khi nhận dạng ký tự gặp lỗi.
- **Kết quả:** Tác vụ thất bại có thể được yêu cầu chạy lại.
- **Mức độ:** Nên có.
- **Cỡ:** Nhỏ.
- **Phụ thuộc:** LDMS-003.
- **Yêu cầu liên quan:** YC-ND-07, YC-QL-02.
- **Tiêu chí chấp nhận:**
  - Hệ thống hiển thị nguyên nhân lỗi ở mức phù hợp.
  - Người có quyền yêu cầu xử lý lại.
  - Kết quả xử lý lại cập nhật trạng thái mới và không làm mất tệp gốc.

#### LDMS-026 — Xem danh sách và trạng thái tài liệu

- **Vai trò:** Thủ thư hoặc biên tập viên.
- **Nhu cầu:** Theo dõi các tài liệu đang tiếp nhận và xử lý.
- **Kết quả:** Danh sách hiển thị đúng tài liệu người dùng được phép quản lý.
- **Mức độ:** Bắt buộc.
- **Cỡ:** Nhỏ.
- **Phụ thuộc:** LDMS-002.
- **Yêu cầu liên quan:** YC-TL-06.
- **Tiêu chí chấp nhận:**
  - Danh sách hiển thị tên, trạng thái và thời điểm cập nhật cơ bản.
  - Người dùng không thấy tài liệu ngoài phạm vi quyền.
  - Trạng thái thay đổi sau các bước tiếp nhận và xử lý.

#### LDMS-011 — Quản lý thông tin mô tả tài liệu

- **Vai trò:** Thủ thư.
- **Nhu cầu:** Nhập thông tin giúp nhận biết và tìm đúng tài liệu.
- **Kết quả:** Thông tin mô tả được lưu và hiển thị chính xác.
- **Mức độ:** Bắt buộc.
- **Cỡ:** Vừa.
- **Phụ thuộc:** LDMS-002.
- **Yêu cầu liên quan:** YC-TL-04.
- **Tiêu chí chấp nhận:**
  - Người có quyền nhập và sửa được các trường bắt buộc.
  - Người có quyền gán tài liệu vào một danh mục đã có; danh mục không tồn tại bị từ chối rõ ràng.
  - Dữ liệu thiếu hoặc không hợp lệ được thông báo.
  - Thông tin đã lưu được dùng trong kết quả tìm kiếm và màn hình tài liệu.

#### LDMS-012 — Quản lý danh mục tài liệu

- **Vai trò:** Quản trị viên.
- **Nhu cầu:** Phân loại tài liệu thống nhất.
- **Kết quả:** Danh mục có thể tạo, sửa, sắp xếp hoặc ẩn.
- **Mức độ:** Nên có.
- **Cỡ:** Vừa.
- **Phụ thuộc:** LDMS-010.
- **Yêu cầu liên quan:** YC-TL-05, YC-QL-01.
- **Tiêu chí chấp nhận:**
  - Quản trị viên tạo và cập nhật được danh mục.
  - Tài liệu có thể gắn với danh mục phù hợp.
  - Danh mục bị ẩn không xuất hiện trong lựa chọn mới nhưng không làm mất dữ liệu cũ.

#### LDMS-007 — Tạo bản EPUB

- **Vai trò:** Biên tập viên.
- **Nhu cầu:** Chuyển nội dung đã hiệu chỉnh thành định dạng đọc trực tuyến.
- **Kết quả:** Hệ thống tạo được tệp EPUB từ nội dung hợp lệ.
- **Mức độ:** Bắt buộc.
- **Cỡ:** Vừa.
- **Phụ thuộc:** LDMS-005, LDMS-011.
- **Yêu cầu liên quan:** YC-PH-04, YC-PN-03.
- **Tiêu chí chấp nhận:**
  - Nội dung hợp lệ tạo được tệp EPUB.
  - Tệp EPUB mở được bằng trình đọc hỗ trợ.
  - Lỗi tạo tệp được hiển thị và không làm mất nội dung đã hiệu chỉnh.

#### LDMS-013 — Kiểm tra điều kiện xuất bản

- **Vai trò:** Biên tập viên.
- **Nhu cầu:** Ngăn tài liệu chưa hoàn chỉnh được đưa ra sử dụng.
- **Kết quả:** Hệ thống kiểm tra và chặn xuất bản khi thiếu điều kiện.
- **Mức độ:** Bắt buộc.
- **Cỡ:** Nhỏ.
- **Phụ thuộc:** LDMS-007, LDMS-011.
- **Yêu cầu liên quan:** YC-PH-01, YC-PH-02, YC-PH-03.
- **Tiêu chí chấp nhận:**
  - Hệ thống kiểm tra nội dung, thông tin mô tả và tệp EPUB.
  - Tài liệu thiếu điều kiện không thể xuất bản và nêu rõ lý do.
  - Người có quyền xác nhận xuất bản khi mọi điều kiện đạt.

#### LDMS-023 — Ghi nhật ký thao tác quan trọng

- **Vai trò:** Quản trị viên.
- **Nhu cầu:** Kiểm tra ai đã thực hiện thao tác quan trọng.
- **Kết quả:** Nhật ký có thể dùng để truy vết.
- **Mức độ:** Nên có.
- **Cỡ:** Nhỏ.
- **Phụ thuộc:** LDMS-010.
- **Yêu cầu liên quan:** YC-QL-03, YC-PN-10.
- **Tiêu chí chấp nhận:**
  - Thao tác tải lên, sửa nội dung và xuất bản được ghi nhận.
  - Nhật ký có người thực hiện, hành động và thời điểm.
  - Người không có quyền không được sửa hoặc xóa nhật ký.

#### LDMS-015 — Tìm kiếm toàn văn

- **Vai trò:** Độc giả.
- **Nhu cầu:** Tìm nội dung trong các tài liệu đã xuất bản.
- **Kết quả:** Từ khóa trả về các tài liệu phù hợp và được phép xem.
- **Mức độ:** Bắt buộc.
- **Cỡ:** Vừa.
- **Phụ thuộc:** LDMS-007, LDMS-013.
- **Yêu cầu liên quan:** YC-TC-01, YC-TC-02, YC-TC-03, YC-PN-04.
- **Tiêu chí chấp nhận:**
  - Tìm kiếm được theo thông tin mô tả và nội dung văn bản.
  - Tài liệu chưa xuất bản không xuất hiện.
  - Kết quả không chứa tài liệu ngoài quyền truy cập của người dùng.

#### LDMS-016 — Hiển thị kết quả tìm kiếm

- **Vai trò:** Độc giả.
- **Nhu cầu:** Nhận biết tài liệu phù hợp trước khi mở.
- **Kết quả:** Kết quả hiển thị thông tin nhận biết và đường dẫn đọc.
- **Mức độ:** Bắt buộc.
- **Cỡ:** Nhỏ.
- **Phụ thuộc:** LDMS-015, LDMS-011.
- **Yêu cầu liên quan:** YC-TC-04.
- **Tiêu chí chấp nhận:**
  - Kết quả hiển thị tên và thông tin mô tả chính của tài liệu.
  - Từ khóa tìm kiếm được thể hiện phù hợp khi có thể.
  - Người dùng mở được tài liệu từ kết quả hợp lệ.

#### LDMS-008 — Đọc tài liệu trực tuyến

- **Vai trò:** Độc giả.
- **Nhu cầu:** Đọc tài liệu đã xuất bản mà không cần tải tệp gốc.
- **Kết quả:** Tài liệu EPUB hiển thị được trên trình đọc trực tuyến.
- **Mức độ:** Bắt buộc.
- **Cỡ:** Vừa.
- **Phụ thuộc:** LDMS-013.
- **Yêu cầu liên quan:** YC-PH-05, YC-TC-05.
- **Tiêu chí chấp nhận:**
  - Độc giả có quyền mở được tài liệu đã xuất bản.
  - Nội dung hiển thị đúng và có thể chuyển trang.
  - Giao diện đọc phù hợp với màn hình máy tính và thiết bị di động.

#### LDMS-014 — Bảo vệ quyền đọc tài liệu

- **Vai trò:** Độc giả và quản trị viên.
- **Nhu cầu:** Chỉ người được phép mới đọc được tài liệu và không tải tệp EPUB gốc từ giao diện.
- **Kết quả:** Hệ thống kiểm tra quyền trước khi cung cấp nội dung.
- **Mức độ:** Bắt buộc.
- **Cỡ:** Vừa.
- **Phụ thuộc:** LDMS-008, LDMS-010.
- **Yêu cầu liên quan:** YC-PH-06, YC-TC-06, YC-PN-02.
- **Tiêu chí chấp nhận:**
  - Người không có quyền bị từ chối khi mở tài liệu.
  - Giao diện độc giả không hiển thị nút tải tệp EPUB gốc.
  - Tệp riêng tư không được cung cấp bằng liên kết công khai lâu dài.

#### LDMS-019 — Thiết lập đọc cơ bản

- **Vai trò:** Độc giả.
- **Nhu cầu:** Điều chỉnh cách hiển thị để đọc thuận tiện hơn.
- **Kết quả:** Một số thiết lập đọc được áp dụng trong phiên đọc.
- **Mức độ:** Có thể xem xét.
- **Cỡ:** Nhỏ.
- **Phụ thuộc:** LDMS-008.
- **Yêu cầu liên quan:** YC-TC-07.
- **Tiêu chí chấp nhận:**
  - Nếu được đưa vào phiên bản triển khai, người đọc thay đổi được các thiết lập đã thống nhất.
  - Thiết lập không làm thay đổi nội dung gốc.
  - Chức năng được loại khỏi luồng nếu phạm vi bắt buộc chưa hoàn thành.

#### LDMS-020 — Lưu vị trí đọc

- **Vai trò:** Độc giả.
- **Nhu cầu:** Quay lại vị trí đang đọc ở lần sau.
- **Kết quả:** Vị trí đọc được lưu cho tài khoản phù hợp.
- **Mức độ:** Có thể xem xét.
- **Cỡ:** Nhỏ.
- **Phụ thuộc:** LDMS-008.
- **Yêu cầu liên quan:** Chưa thuộc yêu cầu cơ sở phiên bản đầu tiên.
- **Tiêu chí chấp nhận:** Chỉ đưa vào luồng sau khi thống nhất dữ liệu lưu, quyền riêng tư và tiêu chí chi tiết.

#### LDMS-021 — Đánh dấu và ghi chú

- **Vai trò:** Độc giả.
- **Nhu cầu:** Lưu lại nội dung cần xem lại.
- **Kết quả:** Đánh dấu hoặc ghi chú được lưu theo tài khoản.
- **Mức độ:** Có thể xem xét.
- **Cỡ:** Vừa.
- **Phụ thuộc:** LDMS-008.
- **Yêu cầu liên quan:** Chưa thuộc yêu cầu cơ sở phiên bản đầu tiên.
- **Tiêu chí chấp nhận:** Chỉ đưa vào luồng sau khi thống nhất cách lưu, chỉnh sửa, xóa và bảo vệ ghi chú.

#### LDMS-024 — Tạo trích dẫn

- **Vai trò:** Độc giả.
- **Nhu cầu:** Tạo thông tin trích dẫn từ tài liệu.
- **Kết quả:** Trích dẫn được tạo theo định dạng đã thống nhất.
- **Mức độ:** Có thể xem xét.
- **Cỡ:** Vừa.
- **Phụ thuộc:** LDMS-011, LDMS-008.
- **Yêu cầu liên quan:** Chưa thuộc yêu cầu cơ sở phiên bản đầu tiên.
- **Tiêu chí chấp nhận:** Chỉ đưa vào luồng sau khi thống nhất nguồn thông tin và định dạng trích dẫn.

#### LDMS-025 — Mở rộng công cụ tìm kiếm

- **Vai trò:** Quản trị viên.
- **Nhu cầu:** Mở rộng khả năng tìm kiếm khi quy mô kho tài liệu tăng.
- **Kết quả:** Công cụ tìm kiếm mới được lựa chọn dựa trên dữ liệu thực tế.
- **Mức độ:** Có thể xem xét.
- **Cỡ:** Vừa.
- **Phụ thuộc:** LDMS-015 và kết quả đánh giá quy mô dữ liệu.
- **Yêu cầu liên quan:** Chưa thuộc yêu cầu cơ sở phiên bản đầu tiên.
- **Tiêu chí chấp nhận:** Chỉ thực hiện sau khi có dữ liệu chứng minh công cụ hiện tại không đáp ứng và có phương án được chấp thuận.

## 5. Luồng Kanban trong 11 tuần

Các mốc dưới đây là mốc điều phối tham chiếu, không khóa nhóm vào các đợt phát triển cố định. Công việc được kéo qua các cột khi đủ điều kiện; nhóm có thể điều chỉnh thứ tự theo phụ thuộc và phản hồi.

| Thời gian | Trọng tâm đưa vào luồng                                                            | Kết quả cần kiểm tra                                             |
| --------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| Tuần 1    | Rà soát yêu cầu, tạo môi trường, cấu trúc mã nguồn và chuẩn bị dữ liệu thử nghiệm. | Danh mục có tiêu chí rõ; môi trường nhóm chạy được.              |
| Tuần 2–3  | Tài khoản, vai trò, tải tài liệu và quản lý danh sách.                             | Có thể đăng nhập, tải và theo dõi tài liệu theo quyền.           |
| Tuần 4–6  | Nhận dạng ký tự, lưu kết quả, xem bản gốc và hiệu chỉnh.                           | Có thể xử lý một tài liệu mẫu từ đầu đến khi lưu văn bản.        |
| Tuần 7–8  | Siêu dữ liệu, danh mục, tạo EPUB, kiểm tra và xuất bản.                            | Tài liệu đạt điều kiện được xuất bản, tài liệu chưa đạt bị chặn. |
| Tuần 9–10 | Tìm kiếm toàn văn, đọc trực tuyến và bảo vệ quyền truy cập.                        | Độc giả tìm và đọc được tài liệu đã xuất bản đúng quyền.         |
| Tuần 11   | Tích hợp, kiểm thử hồi quy, sửa lỗi, nghiệm thu và bàn giao.                       | Có kết quả kiểm thử, hướng dẫn sử dụng và xác nhận phạm vi.      |

## 6. Truy vết và quản lý thay đổi

Mỗi câu chuyện người dùng phải truy ngược được đến nhóm yêu cầu trong [Yêu cầu phần mềm](04-software-requirements.md), tài liệu nền liên quan và tiêu chí nghiệm thu. Các yêu cầu phi chức năng được kiểm tra trong tiêu chí chấp nhận của câu chuyện người dùng, trong kiểm thử tích hợp hoặc trong tài liệu kiến trúc; không tách thành lời hứa độc lập nếu chưa có cách đo.

Khi có thay đổi, người đề xuất ghi nội dung, lý do, nguồn, mức ưu tiên và tác động. Đại diện nhóm Sebros phối hợp với Đại diện nghiệp vụ Thư viện quyết định một trong ba hướng: cập nhật công việc đang chờ, đưa vào danh sách xem xét sau hoặc loại bỏ. Sau quyết định, nhóm cập nhật yêu cầu phần mềm, tiêu chí chấp nhận, phụ thuộc và thứ tự trên bảng Kanban.

Các chức năng đã nêu trong phương án cạnh tranh hoặc tài liệu kiến trúc nhưng chưa có câu chuyện người dùng và tiêu chí chấp nhận không được xem là phạm vi đã cam kết. Những con số hiệu năng, chi phí hoặc quy mô chỉ được dùng khi có nguồn hoặc kết quả đo tương ứng.

## 7. Tài liệu tham khảo

- [Đề xuất dự án](01-project-proposal.md)
- [Tài liệu viễn cảnh và phạm vi](02-vision-and-scope.md)
- [Ủy nhiệm dự án](03-project-charter.md)
- [Yêu cầu phần mềm](04-software-requirements.md)
- [Tài liệu kiến trúc phần mềm](05-software-architecture.md)
- [Nghiên cứu tính khả thi](08-feasibility-study.md)
