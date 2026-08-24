# BẢN MÔ TẢ CÔNG VIỆC (STATEMENT OF WORK — SOW)

## Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS (HCMUS-LDMS)

### Thông tin tài liệu

| Trường thông tin        | Nội dung                                              |
| ----------------------- | ----------------------------------------------------- |
| Mã tài liệu             | `HCMUS-LDMS-SOW`                                      |
| Tên tài liệu            | Bản mô tả công việc                                   |
| Dự án                   | HCMUS-LDMS                                            |
| Đơn vị thực hiện        | Nhóm Sebros                                           |
| Người phụ trách         | Mạch Quốc Tấn — Đại diện nhóm Sebros                  |
| Người xem xét           | Các thành viên nhóm Sebros; giảng viên nếu có yêu cầu |
| Người xác nhận baseline | Sáu thành viên nhóm Sebros                            |
| Trạng thái              | Baseline nội bộ đã được nhóm xác nhận                 |
| Baseline                | Sản phẩm khả dụng tối thiểu của môn học trong 11 tuần |

### Lịch sử phiên bản

| Phiên bản |    Ngày    | Mô tả thay đổi                                                                                                                                    | Người thực hiện   |
| --------: | :--------: | ------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
|       1.0 | 24/07/2026 | Khởi tạo SOW.                                                                                                                                     | Ân Tiến Nguyên An |
|       2.0 | 22/08/2026 | Tái lập baseline 11 tuần; đồng bộ 15 hạng mục Bắt buộc, dữ liệu mẫu, ngân sách môn học, kiến trúc và tiêu chí hoàn thành có truy vết.             | Mạch Quốc Tấn     |
|       3.0 | 24/08/2026 | Xác định dự án phục vụ học tập; phân biệt thành phần tham gia thực tế với bên liên quan tham khảo; rút gọn nội dung trùng và chuẩn hóa thuật ngữ. | Mạch Quốc Tấn     |
|       3.1 | 24/08/2026 | Dùng thống nhất thuật ngữ baseline, đổi tên tài liệu rủi ro được dẫn chiếu, giải thích thuật ngữ và ghi nhận xác nhận nội bộ của sáu thành viên.  | Mạch Quốc Tấn     |
|       3.2 | 24/08/2026 | Loại bỏ đường dẫn tệp khỏi nội dung bản in; chuẩn hóa cách gọi hoạt động chạy thử, đánh giá và kiểm chứng kết quả.                                | Mạch Quốc Tấn     |

## Mục lục

- [1. Mục đích và phạm vi áp dụng](#1-mục-đích-và-phạm-vi-áp-dụng)
- [2. Thành phần tham gia và bên liên quan tham khảo](#2-thành-phần-tham-gia-và-bên-liên-quan-tham-khảo)
- [3. Baseline và phạm vi](#3-baseline-và-phạm-vi)
- [4. Định hướng kỹ thuật và môi trường](#4-định-hướng-kỹ-thuật-và-môi-trường)
- [5. Sản phẩm bàn giao](#5-sản-phẩm-bàn-giao)
- [6. Tiến độ 11 tuần](#6-tiến-độ-11-tuần)
- [7. Nguồn lực và chi phí](#7-nguồn-lực-và-chi-phí)
- [8. Tiêu chí hoàn thành](#8-tiêu-chí-hoàn-thành)
- [9. Bằng chứng và truy vết](#9-bằng-chứng-và-truy-vết)
- [10. Kiểm soát thay đổi](#10-kiểm-soát-thay-đổi)
- [11. Giả định, ràng buộc và phụ thuộc](#11-giả-định-ràng-buộc-và-phụ-thuộc)
- [12. Rủi ro chính](#12-rủi-ro-chính)
- [13. Xác nhận baseline](#13-xác-nhận-baseline)
- [14. Tài liệu tham chiếu](#14-tài-liệu-tham-chiếu)

---

## 1. Mục đích và phạm vi áp dụng

HCMUS-LDMS là dự án học tập nhằm giúp nhóm Sebros áp dụng kiến thức quản lý dự án phần mềm và phát triển một sản phẩm khả dụng tối thiểu để minh họa quy trình số hóa tài liệu. Sản phẩm được dùng cho học tập, đánh giá môn học và kiểm chứng kết quả kỹ thuật trong phạm vi nhóm.

Tài liệu này xác định công việc, phạm vi, sản phẩm bàn giao, thời gian, nguồn lực, tiêu chí hoàn thành và cơ chế kiểm soát thay đổi của dự án trong 11 tuần. Đây là baseline nội bộ để nhóm lập kế hoạch, phân công, theo dõi và đánh giá kết quả; tài liệu không tạo nghĩa vụ triển khai đối với Nhà trường, Thư viện hoặc các đơn vị được nhắc đến trong kịch bản mở rộng.

Trong tài liệu này, **baseline** là tập hợp phạm vi, thời gian, nguồn lực và sản phẩm bàn giao đã được nhóm thống nhất để làm mốc quản lý. Các mức **Bắt buộc**, **Nên có** và **Có thể xem xét** thể hiện thứ tự ưu tiên của hạng mục. Chi tiết yêu cầu và tiêu chí chấp nhận được trình bày trong tài liệu **Yêu cầu phần mềm** và **Danh mục công việc**.

SOW không thay thế các tài liệu **Yêu cầu phần mềm**, **Danh mục công việc**, **Kiến trúc phần mềm** hoặc **Kế hoạch kiểm thử**. Khi thay đổi baseline, nhóm phải cập nhật đồng thời các tài liệu liên quan theo Mục 10.

## 2. Thành phần tham gia và bên liên quan tham khảo

### 2.1. Thành phần tham gia thực tế

| Thành phần                  | Vai trò trong dự án                                                                            |
| --------------------------- | ---------------------------------------------------------------------------------------------- |
| Nhóm Sebros gồm 6 sinh viên | Phân tích, lập kế hoạch, thiết kế, phát triển, kiểm thử, đánh giá và lập tài liệu.             |
| Đại diện nhóm Sebros        | Điều phối baseline, tiến độ, thay đổi, rủi ro và việc xác nhận kết quả nội bộ.                 |
| Giảng viên, nếu có yêu cầu  | Đánh giá kết quả học tập hoặc cung cấp phản hồi theo yêu cầu môn học; không vận hành hệ thống. |

### 2.2. Bên liên quan tham khảo khi mở rộng

| Bên liên quan                                   | Vai trò có thể có trong một giai đoạn triển khai riêng                         |
| ----------------------------------------------- | ------------------------------------------------------------------------------ |
| Đại diện nghiệp vụ Thư viện                     | Làm rõ quy trình, dữ liệu mẫu, tiêu chí chấp nhận và nhu cầu vận hành.         |
| Đại diện Phòng Công nghệ Thông tin              | Xem xét hạ tầng, bảo mật, tích hợp và khả năng vận hành.                       |
| Đại diện Pháp chế hoặc người được ủy quyền      | Xem xét quyền số hóa, lưu trữ và cung cấp tài liệu thật.                       |
| Ban Giám hiệu hoặc đơn vị tài trợ               | Xem xét chủ trương, nguồn lực và phạm vi triển khai nếu dự án được mở rộng.    |
| Sinh viên, giảng viên, thủ thư và biên tập viên | Cung cấp nhu cầu và phản hồi về khả năng sử dụng trong một đợt đánh giá riêng. |

Các bên trong Mục 2.2 không được xem là đã tham gia, phê duyệt hoặc nghiệm thu dự án hiện tại. Nếu dự án được mở rộng để triển khai thực tế, cần lập SOW mới, xác định đại diện cụ thể và ghi nhận sự chấp thuận phù hợp.

## 3. Baseline và phạm vi

### 3.1. Baseline

| Thuộc tính         | Giá trị                                                                  |
| ------------------ | ------------------------------------------------------------------------ |
| Mục tiêu chính     | Áp dụng kiến thức quản lý dự án phần mềm và hoàn thiện sản phẩm minh họa |
| Phiên bản          | Sản phẩm khả dụng tối thiểu phục vụ học tập và đánh giá kết quả          |
| Thời gian          | 11 tuần                                                                  |
| Nhân sự phát triển | 6 sinh viên kiêm nhiệm                                                   |
| Phương pháp        | Kanban, luồng liên tục và giới hạn công việc đang thực hiện              |
| Phạm vi baseline   | 15 hạng mục Bắt buộc                                                     |
| Phạm vi điều kiện  | 6 hạng mục Nên có, chỉ thực hiện khi baseline ổn định                    |
| Ngoài baseline     | 5 hạng mục Có thể xem xét                                                |
| Dữ liệu            | Bộ tài liệu mẫu có nguồn và quyền sử dụng phù hợp                        |
| Khả năng mở rộng   | Chỉ là định hướng tham khảo, không thuộc cam kết hiện tại                |

Danh sách hạng mục Bắt buộc: `LDMS-001`, `LDMS-002`, `LDMS-003`, `LDMS-004`, `LDMS-005`, `LDMS-007`, `LDMS-008`, `LDMS-009`, `LDMS-010`, `LDMS-011`, `LDMS-013`, `LDMS-014`, `LDMS-015`, `LDMS-016`, `LDMS-026`. Nội dung và tiêu chí chấp nhận chi tiết được quản lý trong tài liệu **Danh mục công việc**.

Chi tiết cách áp dụng Kanban, giới hạn công việc đang thực hiện và điều kiện hoàn thành được trình bày trong tài liệu **Định nghĩa quy trình phát triển**.

### 3.2. Trong phạm vi

- Chuẩn bị môi trường và cấu trúc mã nguồn thống nhất.
- Đăng nhập trong môi trường phát triển hoặc chạy thử và phân quyền phía máy chủ.
- Tiếp nhận PDF/ảnh hợp lệ, bảo toàn tệp gốc và quản lý trạng thái tài liệu.
- Khởi chạy, theo dõi và xem kết quả nhận dạng ký tự theo trang.
- Hiệu chỉnh và lưu văn bản đã nhận dạng.
- Nhập thông tin mô tả tối thiểu cho tài liệu.
- Tạo EPUB, kiểm tra điều kiện và xác nhận xuất bản.
- Tìm kiếm theo thông tin mô tả và nội dung toàn văn của tài liệu đã xuất bản.
- Đọc EPUB trực tuyến và kiểm tra quyền trước khi cung cấp nội dung.
- Kiểm thử, triển khai phiên bản chạy thử, hoàn thiện hướng dẫn và tổng kết dự án.

### 3.3. Ngoài phạm vi

- Số hóa toàn bộ kho tài liệu hoặc cam kết số lượng tài liệu thương mại.
- Ứng dụng đọc ngoại tuyến gốc cho iOS hoặc Android.
- Thanh toán, thương mại hóa hoặc bán bản quyền tài liệu.
- Tìm kiếm ngữ nghĩa, hệ thống truy xuất kết hợp sinh nội dung (RAG), chống đạo văn hoặc tích hợp hệ thống đào tạo.
- Mua sắm máy quét, máy chủ hoặc phần mềm thương mại.
- Vận hành toàn trường, kiểm thử xâm nhập chính thức hoặc cam kết mức dịch vụ dài hạn.
- Các hạng mục `LDMS-019`, `LDMS-020`, `LDMS-021`, `LDMS-024`, `LDMS-025` nếu chưa có quyết định bổ sung phạm vi.

## 4. Định hướng kỹ thuật và môi trường

Sản phẩm sử dụng React và TypeScript cho giao diện, FastAPI và Python cho dịch vụ phía máy chủ (API), PostgreSQL cho dữ liệu và tìm kiếm toàn văn, Tesseract cho nhận dạng ký tự, công cụ tạo EPUB, Epub.js cho trình đọc và kho lưu trữ tệp tương thích S3. Chi tiết thành phần, phiên bản, luồng xử lý và các thuật ngữ kỹ thuật được trình bày trong tài liệu **Kiến trúc phần mềm**; lý do lựa chọn được trình bày trong tài liệu **Nhật ký quyết định và ADR**.

| Môi trường                         | Mục đích                                                                |
| ---------------------------------- | ----------------------------------------------------------------------- |
| Phát triển và kiểm thử cục bộ      | Chạy, phát triển và kiểm thử bằng cấu hình trong kho mã nguồn.          |
| Chạy thử trên đám mây, nếu sử dụng | Kiểm chứng sản phẩm sau khi triển khai và kiểm tra nhanh thành công.    |
| Môi trường vận hành thực tế        | Ngoài phạm vi; cần kiến trúc, chi phí, bảo mật, phê duyệt và SOW riêng. |

Kết quả ở một môi trường không được dùng để khẳng định môi trường khác đã sẵn sàng.

## 5. Sản phẩm bàn giao

| Mã    | Sản phẩm             | Nội dung tối thiểu                                                                    | Thời điểm mục tiêu     |
| ----- | -------------------- | ------------------------------------------------------------------------------------- | ---------------------- |
| DL-01 | Mã nguồn             | Giao diện, dịch vụ phía máy chủ, tệp cập nhật cơ sở dữ liệu, cấu hình và lịch sử Git. | Tuần 11                |
| DL-02 | Bản dựng chạy thử    | Các luồng Bắt buộc có thể chạy và được đánh giá trên môi trường đã chọn.              | Tuần 10–11             |
| DL-03 | Hướng dẫn triển khai | Hướng dẫn chạy cục bộ và cấu hình môi trường chạy thử nếu được sử dụng.               | Tuần 10                |
| DL-04 | Dữ liệu mẫu          | Tài liệu mẫu có nguồn và quyền sử dụng được ghi nhận.                                 | Tuần 3                 |
| DL-05 | Bộ tài liệu dự án    | Các tài liệu quản lý, kỹ thuật và hướng dẫn đã được rà soát thống nhất.               | Liên tục, chốt tuần 11 |
| DL-06 | Hướng dẫn sử dụng    | Hướng dẫn các luồng chính theo vai trò ở mức sản phẩm tối thiểu.                      | Tuần 10                |
| DL-07 | Bằng chứng kiểm thử  | Kết quả kiểm thử, lỗi còn lại và ngoại lệ được ghi nhận.                              | Tuần 10–11             |
| DL-08 | Báo cáo tổng kết     | Kết quả, sản phẩm hoàn thành, hạn chế và bài học kinh nghiệm.                         | Tuần 11                |

## 6. Tiến độ 11 tuần

| Thời gian | Trọng tâm                                            | Điều kiện kiểm tra                                           |
| --------- | ---------------------------------------------------- | ------------------------------------------------------------ |
| Tuần 1    | Chốt phạm vi, quy tắc hoàn thành và dữ liệu mẫu.     | Baseline được ghi nhận; môi trường cục bộ chạy được.         |
| Tuần 2–3  | Xác thực, phân quyền, tải lên và danh sách tài liệu. | Luồng đầu vào hoạt động đúng quyền.                          |
| Tuần 4–6  | Nhận dạng ký tự, kết quả theo trang và hiệu chỉnh.   | Tài liệu mẫu đi đến văn bản đã lưu.                          |
| Tuần 7–8  | Thông tin mô tả, EPUB và xuất bản.                   | Thiếu điều kiện bị chặn; tài liệu hợp lệ được xuất bản.      |
| Tuần 9–10 | Tìm kiếm, đọc và bảo vệ quyền.                       | Người dùng đúng quyền tìm và đọc được; quyền sai bị từ chối. |
| Tuần 11   | Kiểm thử hồi quy, sửa lỗi và tổng kết.               | Có bằng chứng kết quả và danh sách sản phẩm hoàn thành.      |

Đây là các mốc điều phối, không phải chu kỳ phát triển cố định. Một hạng mục chỉ được ghi Hoàn thành khi đạt điều kiện hoàn thành và có bằng chứng. Chi tiết lịch, phụ thuộc và phân công được trình bày trong tài liệu **Kế hoạch dự án**.

## 7. Nguồn lực và chi phí

Nhóm Sebros gồm 6 sinh viên kiêm nhiệm các vai trò quản lý, phân tích, kiến trúc, phát triển giao diện, phát triển máy chủ, kiểm thử và vận hành môi trường chạy thử. Phân công và cơ chế phối hợp chi tiết được trình bày trong tài liệu **Hợp đồng nhóm** và **Kế hoạch dự án**.

Dự án không có ngân sách tiền mặt được phê duyệt. Nhóm sử dụng thiết bị, tài nguyên và gói dịch vụ sẵn có hoặc miễn phí; công sức được theo dõi bằng giờ để phục vụ quản lý và đánh giá học tập. Mọi chi phí triển khai, mua sắm hoặc vận hành thực tế nằm ngoài phạm vi và phải được lập dự toán riêng trong một giai đoạn mở rộng.

Chi tiết phương pháp ước lượng, năng lực khả dụng và chi phí được trình bày trong tài liệu **Ước lượng dự án**.

## 8. Tiêu chí hoàn thành

### 8.1. Điều kiện hoàn thành dự án môn học

- 15 hạng mục Bắt buộc có trạng thái Hoàn thành, hoặc nhóm xác nhận danh sách ngoại lệ theo quy trình thay đổi.
- Mỗi hạng mục Hoàn thành có liên kết tới thay đổi mã nguồn hoặc tài liệu, kết quả kiểm thử, người xem xét và ngày xác nhận.
- Luồng tải lên → nhận dạng ký tự → hiệu chỉnh → tạo EPUB → xuất bản → tìm kiếm → đọc chạy được trên bộ dữ liệu mẫu.
- Phân quyền được kiểm tra phía máy chủ; người không đủ quyền bị từ chối.
- Tài liệu chưa xuất bản không xuất hiện trong kết quả tìm kiếm dành cho người đọc.
- Tệp gốc không bị ghi đè; giao diện người đọc không cung cấp chức năng tải trực tiếp EPUB gốc.
- Không còn lỗi nghiêm trọng chưa được ghi nhận và chấp thuận như một ngoại lệ.
- Hướng dẫn triển khai và sử dụng phản ánh đúng phiên bản được đánh giá.

### 8.2. Chỉ số cần đo

Các chỉ số về thời gian tìm kiếm, chất lượng nhận dạng ký tự, thời gian khởi động và khả năng tương thích chỉ được công bố khi có dữ liệu, môi trường, phương pháp đo và kết quả tương ứng. Ngưỡng và quy trình đo được trình bày trong tài liệu **Yêu cầu phần mềm** và **Kế hoạch kiểm thử**.

## 9. Bằng chứng và truy vết

Mỗi hạng mục Hoàn thành phải truy được tới mã yêu cầu hoặc hạng mục công việc, thay đổi mã nguồn hoặc tài liệu, kết quả kiểm thử, môi trường thực hiện, người xem xét và ngày xác nhận. Cấu trúc chi tiết được trình bày trong tài liệu **Nhật ký dự án** và **Kế hoạch kiểm thử**.

Số token, số commit hoặc thời gian làm việc không tự chứng minh rằng một yêu cầu đã đạt.

## 10. Kiểm soát thay đổi

| Loại thay đổi | Ví dụ                                                                   | Người xác nhận                                 |
| ------------- | ----------------------------------------------------------------------- | ---------------------------------------------- |
| Biên tập      | Chính tả, liên kết hoặc định dạng không làm thay đổi ý nghĩa            | Chủ sở hữu tài liệu và người xem xét           |
| Nhỏ           | Làm rõ tiêu chí, điều chỉnh thứ tự nhưng không đổi baseline             | Đại diện nhóm và người phụ trách nội dung      |
| Baseline      | Đổi 15 hạng mục Bắt buộc, 11 tuần, nguồn lực hoặc sản phẩm bàn giao     | Nhóm Sebros theo quy tắc trong Hợp đồng nhóm   |
| Mở rộng       | Triển khai cho đơn vị thật, dùng tài liệu thật hoặc phát sinh ngân sách | Cần đề xuất, SOW và thẩm quyền phê duyệt riêng |

Quy trình thay đổi gồm: ghi yêu cầu và lý do; phân tích tác động; xác định người có thẩm quyền; ghi nhận quyết định; cập nhật đồng thời SOW và các tài liệu bị ảnh hưởng. Im lặng không được xem là đồng ý.

## 11. Giả định, ràng buộc và phụ thuộc

### Giả định

- Nhóm duy trì 6 thành viên và thời gian tham gia phù hợp với kế hoạch môn học.
- Có bộ tài liệu mẫu được phép sử dụng.
- Thiết bị và gói dịch vụ sẵn có đủ cho việc phát triển, chạy thử và đánh giá ở quy mô nhỏ.

### Ràng buộc

- Thời gian thực hiện là 11 tuần và phụ thuộc lịch học của thành viên.
- Không có ngân sách tiền mặt được phê duyệt.
- Không dùng hoặc phát hành tài liệu thật khi chưa xác nhận quyền sử dụng.
- Hạng mục tùy chọn không được làm giảm khả năng hoàn thành phạm vi baseline.

### Phụ thuộc

- Chất lượng ảnh đầu vào và kết quả nhận dạng ký tự.
- Tài khoản, hạn mức và tính sẵn sàng của dịch vụ dùng cho môi trường chạy thử.
- Chuỗi xử lý nhận dạng → hiệu chỉnh → EPUB → xuất bản → tìm kiếm và đọc.
- Khả năng cung cấp bằng chứng kiểm thử và hoàn thành của nhóm.

Việc có đại diện Thư viện, Phòng Công nghệ Thông tin hoặc Pháp chế tham gia là điều kiện của một giai đoạn mở rộng, không phải giả định của dự án học tập hiện tại.

## 12. Rủi ro chính

Tài liệu **Kế hoạch quản lý rủi ro** trình bày chi tiết mã rủi ro, người phụ trách, dấu hiệu kích hoạt, biện pháp ứng phó và trạng thái. SOW chỉ tóm tắt các rủi ro ảnh hưởng trực tiếp tới baseline.

| Rủi ro                            | Mức        | Hướng xử lý chính                                                  |
| --------------------------------- | ---------- | ------------------------------------------------------------------ |
| Phạm vi vượt quá khả năng 11 tuần | Cao        | Giữ 15 hạng mục Bắt buộc; hoãn hạng mục tùy chọn.                  |
| Thành viên thiếu thời gian        | Cao        | Giới hạn công việc đang thực hiện và điều phối lại nhiệm vụ.       |
| Luồng cốt lõi hoặc phân quyền lỗi | Cao        | Ưu tiên sửa, kiểm thử hồi quy và không dùng kết quả chưa đạt.      |
| Thiếu bằng chứng hoàn thành       | Cao        | Không ghi Hoàn thành; bổ sung thay đổi, kiểm thử và người xem xét. |
| Môi trường chạy thử không ổn định | Trung bình | Duy trì môi trường cục bộ đã kiểm chứng làm phương án dự phòng.    |

Rủi ro về quyền tài liệu, hạ tầng và vận hành toàn trường phải được đánh giá lại trước bất kỳ giai đoạn mở rộng nào.

## 13. Xác nhận baseline

| Vai trò                | Họ và tên             | Hình thức xác nhận | Ngày       |
| ---------------------- | --------------------- | ------------------ | ---------- |
| Đại diện nhóm Sebros   | Mạch Quốc Tấn         | Xác nhận nội bộ    | 24/08/2026 |
| Thành viên nhóm Sebros | Ân Tiến Nguyên An     | Xác nhận nội bộ    | 24/08/2026 |
| Thành viên nhóm Sebros | Ngô Nguyễn Thế Khoa   | Xác nhận nội bộ    | 24/08/2026 |
| Thành viên nhóm Sebros | Nguyễn Tuấn Anh       | Xác nhận nội bộ    | 24/08/2026 |
| Thành viên nhóm Sebros | Nguyễn Quang Thái     | Xác nhận nội bộ    | 24/08/2026 |
| Thành viên nhóm Sebros | Nguyễn Lê Hồ Anh Khoa | Xác nhận nội bộ    | 24/08/2026 |

Baseline này được ghi nhận là xác nhận nội bộ của nhóm Sebros. Việc xác nhận không đại diện cho Nhà trường, Thư viện hoặc giảng viên. Nếu dự án được mở rộng cho một đơn vị thực tế, nhóm phải lập SOW mới với các bên, trách nhiệm, nguồn lực và thẩm quyền phê duyệt tương ứng.

## 14. Tài liệu tham chiếu

- Đề xuất dự án.
- Viễn cảnh và phạm vi.
- Ủy nhiệm dự án.
- Yêu cầu phần mềm.
- Danh mục công việc.
- Kiến trúc phần mềm.
- Nghiên cứu khả thi.
- Định nghĩa quy trình phát triển.
- Ước lượng dự án.
- Kế hoạch dự án.
- Kế hoạch vận hành và bảo mật.
- Hợp đồng nhóm.
- Nhật ký dự án.
- Kế hoạch quản lý rủi ro.
- Kế hoạch quản lý chất lượng.
- Kế hoạch kiểm thử.
- Nhật ký quyết định và ADR.
