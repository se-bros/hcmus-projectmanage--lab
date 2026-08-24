# KẾ HOẠCH QUẢN LÝ CHẤT LƯỢNG

## Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS (HCMUS-LDMS)

### Thông tin tài liệu

| Trường thông tin  | Nội dung                                |
| ----------------- | --------------------------------------- |
| Mã tài liệu       | `HCMUS-LDMS-QMP`                        |
| Tên tài liệu      | Kế hoạch quản lý chất lượng             |
| Người phụ trách   | Mạch Quốc Tấn                           |
| Người xem xét     | Các thành viên nhóm Sebros              |
| Người xác nhận    | Mạch Quốc Tấn — Quản lý dự án           |
| Trạng thái        | Baseline nội bộ đã được nhóm xác nhận   |
| Thời gian áp dụng | 11 tuần                                 |
| Phạm vi           | 15 hạng mục Bắt buộc, tổng cộng 26 điểm |

### Lịch sử phiên bản

| Phiên bản | Ngày       | Mô tả thay đổi                                                             | Người thực hiện |
| --------- | ---------- | -------------------------------------------------------------------------- | --------------- |
| 1.0       | 22/08/2026 | Xây dựng thuộc tính chất lượng, cổng kiểm soát và chỉ số theo dõi.         | Mạch Quốc Tấn   |
| 2.0       | 24/08/2026 | Viết lại theo baseline, Pull Request, Technical Lead, DoD và coding agent. | Mạch Quốc Tấn   |
| 2.1       | 24/08/2026 | Xác nhận Mạch Quốc Tấn là người viết và phụ trách tài liệu.                | Mạch Quốc Tấn   |
| 2.2       | 24/08/2026 | Đồng bộ Technical Lead, Backend, DevOps và QA theo Hợp đồng nhóm.          | Mạch Quốc Tấn   |
| 2.3       | 24/08/2026 | Loại bỏ tham chiếu tới tài liệu vận hành chưa thuộc bộ hồ sơ hiện tại.     | Mạch Quốc Tấn   |

## Mục lục

- [1. Mục đích và nguyên tắc](#1-mục-đích-và-nguyên-tắc)
- [2. Mục tiêu chất lượng](#2-mục-tiêu-chất-lượng)
- [3. Vai trò và trách nhiệm](#3-vai-trò-và-trách-nhiệm)
- [4. Cổng kiểm soát chất lượng](#4-cổng-kiểm-soát-chất-lượng)
- [5. Xem xét mã nguồn và tài liệu](#5-xem-xét-mã-nguồn-và-tài-liệu)
- [6. Kiểm thử và quản lý lỗi](#6-kiểm-thử-và-quản-lý-lỗi)
- [7. Truy vết và bằng chứng](#7-truy-vết-và-bằng-chứng)
- [8. Chỉ số và báo cáo](#8-chỉ-số-và-báo-cáo)
- [9. Ngoại lệ và cải tiến](#9-ngoại-lệ-và-cải-tiến)
- [10. Điều kiện hoàn thành chất lượng](#10-điều-kiện-hoàn-thành-chất-lượng)
- [11. Tài liệu tham khảo](#11-tài-liệu-tham-khảo)

---

## 1. Mục đích và nguyên tắc

Tài liệu quy định cách nhóm bảo đảm sản phẩm đáp ứng yêu cầu, bảo toàn dữ liệu, kiểm soát đúng quyền, hoạt động ổn định và có đủ bằng chứng để xác nhận kết quả.

Nguyên tắc:

1. Chất lượng được kiểm soát trong từng hạng mục, không dồn đến cuối dự án.
2. Người tạo thay đổi không tự phê duyệt Pull Request của mình.
3. Mọi thay đổi mã nguồn phải được Technical Lead xem xét trước khi hợp nhất vào `main`.
4. Không ghi Hoàn thành khi chưa đạt tiêu chí chấp nhận và DoD.
5. Kiểm thử phải dùng kết quả thực tế; không đổi “Chưa chạy” thành “Đạt”.
6. Không giảm mức độ lỗi để giữ tiến độ.
7. Coding agent hỗ trợ tạo mã, kiểm thử và tài liệu nhưng không thay thế việc kiểm tra của thành viên.
8. Chỉ công bố chỉ số khi có dữ liệu, phương pháp đo và thời điểm đo rõ ràng.

## 2. Mục tiêu chất lượng

| Thuộc tính                | Mục tiêu đối với baseline                                         | Cách kiểm tra                                         |
| ------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------- |
| Đúng chức năng            | 15 hạng mục Bắt buộc đạt tiêu chí chấp nhận.                      | Kiểm thử chức năng và kiểm thử chấp nhận nội bộ.      |
| Bảo mật và quyền riêng tư | Quyền được kiểm tra tại máy chủ; không lộ tệp hay khóa bí mật.    | Kiểm thử sai quyền, rà soát mã nguồn và cấu hình.     |
| Toàn vẹn dữ liệu          | Tệp gốc và nội dung đã lưu không bị mất hoặc ghi đè ngoài ý muốn. | Kiểm thử lỗi, xử lý lại và khôi phục.                 |
| Độ tin cậy                | Tác vụ OCR và EPUB có trạng thái rõ, xử lý được trường hợp lỗi.   | Kiểm thử tích hợp, khởi động lại và xử lý lại.        |
| Khả năng sử dụng          | Luồng chính rõ ràng trên máy tính và thiết bị di động.            | Kiểm thử giao diện và kiểm thử chấp nhận nội bộ.      |
| Khả năng bảo trì          | Mã nguồn dễ đọc, thay đổi nhỏ và có kiểm thử phù hợp.             | Technical Lead xem xét Pull Request.                  |
| Khả năng triển khai       | Môi trường cục bộ có thể thiết lập và chạy lại theo hướng dẫn.    | Thiết lập sạch và kiểm tra nhanh các chức năng chính. |
| Khả năng truy vết         | Yêu cầu được nối với thay đổi, kiểm thử và xác nhận.              | Rà soát chuỗi truy vết và bằng chứng DoD.             |

Các ngưỡng chi tiết của yêu cầu phi chức năng được trình bày trong tài liệu **Yêu cầu phần mềm** và **Kế hoạch kiểm thử**.

## 3. Vai trò và trách nhiệm

| Vai trò                  | Trách nhiệm                                                       |
| ------------------------ | ----------------------------------------------------------------- |
| Quản lý dự án            | Xác nhận baseline, giải quyết ngoại lệ và điều phối cải tiến.     |
| Technical Lead           | Xem xét, yêu cầu sửa và phê duyệt kỹ thuật cho Pull Request.      |
| Đảm bảo chất lượng       | Lập kế hoạch kiểm thử, theo dõi lỗi và rà soát bằng chứng.        |
| Người phụ trách hạng mục | Tự kiểm tra, tạo Pull Request, sửa lỗi và cung cấp bằng chứng.    |
| Người xem xét tài liệu   | Kiểm tra nội dung, thuật ngữ, số liệu và tính nhất quán.          |
| Các thành viên           | Báo lỗi, không che giấu kết quả chưa đạt và hỗ trợ kiểm thử chéo. |

Nguyễn Tuấn Anh giữ vai trò Technical Lead. Ân Tiến Nguyên An phụ trách đảm bảo chất lượng và DevOps. Nguyễn Quang Thái phụ trách Backend. Mạch Quốc Tấn chịu trách nhiệm xác nhận nội bộ đối với kế hoạch chất lượng.

## 4. Cổng kiểm soát chất lượng

### 4.1. Cổng theo trạng thái hạng mục

| Cổng | Chuyển trạng thái             | Điều kiện bắt buộc                                                          | Người xác nhận                  |
| ---- | ----------------------------- | --------------------------------------------------------------------------- | ------------------------------- |
| G0   | Ý tưởng → Đã sẵn sàng         | Có mô tả, Priority, điểm, tiêu chí chấp nhận, phụ thuộc và người phụ trách. | Quản lý dự án; QA khi cần.      |
| G1   | Đã sẵn sàng → Đang thực hiện  | Không vượt giới hạn công việc; dữ liệu và môi trường đã rõ.                 | Người phụ trách; Quản lý dự án. |
| G2   | Đang thực hiện → Đang xem xét | Đã tự kiểm tra, tạo Pull Request và ghi kết quả kiểm thử.                   | Người phụ trách.                |
| G3   | Đang xem xét → Chờ xác nhận   | Technical Lead phê duyệt; kiểm thử bắt buộc đạt; lỗi được phân loại.        | Technical Lead; QA.             |
| G4   | Chờ xác nhận → Hoàn thành     | Đạt tiêu chí chấp nhận, DoD, truy vết và bằng chứng; không còn lỗi chặn.    | QA; Quản lý dự án.              |

Nếu không đạt một cổng, hạng mục được trả về trạng thái phù hợp để sửa. Không được bỏ qua cổng chỉ vì đã đến ngày dự kiến.

### 4.2. Cổng theo mốc dự án

| Mốc     | Điều kiện chất lượng chính                                      | Kết quả xác nhận                      |
| ------- | --------------------------------------------------------------- | ------------------------------------- |
| Tuần 1  | Baseline, môi trường, dữ liệu mẫu và trách nhiệm được xác định. | Sẵn sàng bắt đầu thực hiện.           |
| Tuần 4  | Nền tảng, phân quyền, tải lên và OCR được tích hợp bước đầu.    | Tiếp tục hoặc sửa phần tích hợp.      |
| Tuần 8  | Toàn bộ chức năng Bắt buộc đã có kết quả để kiểm thử đầu cuối.  | Chuyển sang kiểm thử hồi quy.         |
| Tuần 9  | Luồng đầu cuối chạy được; lỗi được ghi nhận và phân loại.       | Tiếp tục sửa lỗi và hoàn thiện.       |
| Tuần 10 | Không còn lỗi nghiêm trọng; bộ tài liệu phản ánh đúng sản phẩm. | Sẵn sàng kiểm thử chấp nhận nội bộ.   |
| Tuần 11 | 15 hạng mục Bắt buộc đạt DoD và có bằng chứng.                  | Xác nhận baseline và bàn giao nội bộ. |

## 5. Xem xét mã nguồn và tài liệu

### 5.1. Xem xét Pull Request

Người phụ trách phải tạo Pull Request sau khi hoàn tất mã nguồn và tự kiểm tra. Pull Request cần có:

- mã và tiêu đề hạng mục;
- mô tả thay đổi;
- tiêu chí chấp nhận liên quan;
- kết quả kiểm thử đã chạy;
- ảnh hưởng đến dữ liệu, bảo mật, kiến trúc hoặc tài liệu;
- bằng chứng giao diện khi hành vi hiển thị thay đổi.

Technical Lead kiểm tra:

- thay đổi đúng phạm vi và tiêu chí chấp nhận;
- quyền được kiểm tra tại máy chủ;
- không có khóa bí mật hoặc dữ liệu không được phép;
- dữ liệu được bảo toàn khi có lỗi;
- mã nguồn rõ ràng và phù hợp kiến trúc;
- kiểm thử bao phủ luồng chính và trường hợp lỗi quan trọng;
- tài liệu liên quan đã được cập nhật.

Pull Request chỉ được hợp nhất khi Technical Lead phê duyệt và các kiểm tra bắt buộc đạt. Nếu Technical Lead ủy quyền người khác xem xét, việc ủy quyền phải được ghi rõ.

### 5.2. Xem xét tài liệu

Tài liệu được xem xét theo các tiêu chí:

- đúng mục đích của tài liệu;
- câu rõ nghĩa, không dài dòng và không tạo cam kết ngoài phạm vi;
- dùng thống nhất baseline, tên vai trò và số liệu;
- không có liên kết tệp hoặc thư mục trong nội dung bản in;
- không tuyên bố “Đạt”, “Hoàn thành” hoặc “Đã xác nhận” khi thiếu căn cứ;
- bảng, mục lục và tiêu đề phản ánh đúng nội dung;
- Markdown đạt kiểm tra định dạng của dự án.

## 6. Kiểm thử và quản lý lỗi

### 6.1. Loại kiểm thử

| Loại kiểm thử    | Mục đích                                            |
| ---------------- | --------------------------------------------------- |
| Đơn vị           | Kiểm tra hàm hoặc thành phần độc lập.               |
| Tích hợp         | Kiểm tra API, dữ liệu, kho tệp và công cụ xử lý.    |
| Chức năng        | Đối chiếu hành vi với tiêu chí chấp nhận.           |
| Giao diện        | Kiểm tra thao tác, trạng thái lỗi và hiển thị.      |
| Phân quyền       | Kiểm tra người hợp lệ, chưa đăng nhập và sai quyền. |
| Hồi quy          | Xác nhận thay đổi không làm hỏng chức năng đã đạt.  |
| Chấp nhận nội bộ | Xác nhận sản phẩm phù hợp mục tiêu học tập.         |

### 6.2. Mức độ lỗi

| Mức độ       | Ý nghĩa                                                       | Cách xử lý                               |
| ------------ | ------------------------------------------------------------- | ---------------------------------------- |
| Nghiêm trọng | Mất dữ liệu, lộ quyền hoặc luồng chính không hoạt động.       | Chặn xác nhận; sửa và kiểm thử lại ngay. |
| Cao          | Hạng mục Bắt buộc không đạt hoặc có thể ảnh hưởng nhiều phần. | Sửa trước khi đạt DoD.                   |
| Trung bình   | Hành vi cục bộ sai nhưng có cách xử lý tạm thời.              | Ghi người phụ trách và thời điểm sửa.    |
| Thấp         | Lỗi trình bày không ảnh hưởng tiêu chí chấp nhận.             | Ghi nhận và xử lý theo thứ tự ưu tiên.   |

Mỗi lỗi cần có mã, môi trường, dữ liệu, bước tái hiện, kết quả mong đợi, kết quả thực tế, mức độ, người phụ trách, trạng thái và kết quả kiểm thử lại.

## 7. Truy vết và bằng chứng

Một hạng mục Hoàn thành phải có chuỗi truy vết:

`Yêu cầu → Hạng mục → Pull Request → Kiểm thử → Technical Lead xem xét → Xác nhận → Hoàn thành`

Bằng chứng phải:

- là kết quả thực tế;
- ghi mã hạng mục, thời điểm và người thực hiện;
- cho biết môi trường và dữ liệu kiểm thử khi cần;
- không chứa khóa bí mật hoặc dữ liệu chưa được phép;
- đủ để người khác kiểm tra lại kết luận.

Số token, số commit, thời gian làm việc hoặc câu trả lời của coding agent không tự chứng minh hạng mục đã đạt.

Kết quả làm thử ngày 16 và 17 tháng 07 năm 2026 đã triển khai 11 hạng mục, tương ứng 18 điểm. Các kết quả này chưa tự động được tính là Hoàn thành vì chưa có đầy đủ bằng chứng DoD trong Nhật ký dự án.

## 8. Chỉ số và báo cáo

| Chỉ số                | Cách tính hoặc ghi nhận                                | Ngưỡng hành động                                      |
| --------------------- | ------------------------------------------------------ | ----------------------------------------------------- |
| Hạng mục Hoàn thành   | Số hạng mục đạt DoD.                                   | Hạng mục thiếu bằng chứng bị trả khỏi Hoàn thành.     |
| Điểm Hoàn thành       | Tổng điểm của các hạng mục đạt DoD.                    | So sánh với baseline 26 điểm.                         |
| Mức đạt tiêu chí      | Tiêu chí đạt chia tổng tiêu chí đã kiểm tra.           | Baseline cần đạt 100% hoặc có ngoại lệ hợp lệ.        |
| Trạng thái kiểm thử   | Đạt, Không đạt, Bị chặn hoặc Chưa chạy theo phiên bản. | Lỗi nghiêm trọng hoặc cao chặn xác nhận.              |
| Mức đầy đủ bằng chứng | Hạng mục đủ bằng chứng chia số hạng mục được rà soát.  | Thiếu trường bắt buộc thì chưa đạt DoD.               |
| Công việc làm lại     | Công sức sửa do yêu cầu, thiết kế hoặc mã chưa đúng.   | Tăng liên tiếp hai tuần thì phải cải tiến.            |
| Thời gian bị chặn     | Thời gian hạng mục không thể tiếp tục.                 | Quá hai ngày phải điều phối lại.                      |
| Lỗi sau Hoàn thành    | Lỗi phát hiện sau khi hạng mục đã đạt G4.              | Lỗi nghiêm trọng hoặc cao phải phân tích nguyên nhân. |

Khi chưa có dữ liệu, báo cáo ghi “Chưa có dữ liệu”, không ghi 0 hoặc Đạt. Báo cáo chất lượng được xem xét cuối mỗi tuần và trước các mốc tuần 8, 10 và 11.

## 9. Ngoại lệ và cải tiến

### 9.1. Ngoại lệ chất lượng

Ngoại lệ phải ghi:

- mã ngoại lệ;
- yêu cầu hoặc cổng bị ảnh hưởng;
- lý do và tác động;
- rủi ro liên quan;
- biện pháp tạm thời;
- người chấp nhận;
- thời hạn và điều kiện đóng.

Không chấp nhận ngoại lệ làm lộ dữ liệu, bỏ kiểm tra quyền hoặc che giấu mất dữ liệu. Ngoại lệ thay đổi baseline phải được sáu thành viên nhóm Sebros xác nhận.

### 9.2. Cải tiến

Khi lỗi, công việc làm lại hoặc điểm chặn lặp lại, nhóm:

1. Xác định nguyên nhân.
2. Chọn một thay đổi có thể thực hiện.
3. Giao người phụ trách và thời hạn.
4. Chọn chỉ số để đánh giá.
5. Kiểm tra kết quả ở lần xem xét tiếp theo.

Không tuyên bố cải tiến thành công khi chưa có kết quả quan sát được.

## 10. Điều kiện hoàn thành chất lượng

Baseline đạt yêu cầu chất lượng khi:

1. Cả 15 hạng mục Bắt buộc đạt tiêu chí chấp nhận và DoD.
2. Tổng điểm Hoàn thành của baseline đạt 26 điểm.
3. Mọi thay đổi mã nguồn có Pull Request được Technical Lead phê duyệt.
4. Không còn lỗi nghiêm trọng hoặc cao chưa xử lý.
5. Kiểm thử phân quyền, toàn vẹn dữ liệu và luồng đầu cuối đạt.
6. Tài liệu phản ánh đúng sản phẩm và không mâu thuẫn về phạm vi, tiến độ hoặc vai trò.
7. Mỗi hạng mục có đầy đủ truy vết và bằng chứng.
8. Nhóm hoàn tất kiểm thử chấp nhận nội bộ và ghi nhận kết quả thực tế.

## 11. Tài liệu tham khảo

- Yêu cầu phần mềm.
- Product Backlog.
- Kiến trúc phần mềm.
- Định nghĩa quy trình phát triển phần mềm.
- Ước lượng dự án.
- Kế hoạch dự án.
- Bản mô tả công việc.
- Kế hoạch quản lý rủi ro.
- Kế hoạch kiểm thử.
- Hợp đồng nhóm.
- Nhật ký dự án.
