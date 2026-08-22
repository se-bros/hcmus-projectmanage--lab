# ĐỊNH NGHĨA QUY TRÌNH PHÁT TRIỂN PHẦN MỀM

## Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS (HCMUS-LDMS)

### THÔNG TIN TÀI LIỆU

| Trường thông tin | Nội dung |
|---|---|
| Mã tài liệu | `HCMUS-LDMS-SPD` |
| Tên tài liệu | Định nghĩa quy trình phát triển phần mềm |
| Dự án | HCMUS-LDMS |
| Đơn vị soạn thảo | Sebros – Nhóm sinh viên đề xuất dự án |
| Người thực hiện | Mạch Quốc Tấn |
| Người xem xét | Đại diện nhóm Sebros và Đại diện nghiệp vụ Thư viện |
| Trạng thái tài liệu | Bản dự thảo để xem xét |
| Phạm vi áp dụng | Phiên bản đầu tiên trong 11 tuần |

### LỊCH SỬ PHIÊN BẢN

| Phiên bản | Ngày | Mô tả thay đổi | Người thực hiện |
|---|---|---|---|
| 1.0 | 21/08/2026 | Xây dựng lại tài liệu theo quy trình Kanban của dự án; bổ sung vai trò, luồng công việc, đầu vào/đầu ra, điều kiện sẵn sàng, điều kiện hoàn thành, đo lường và cải tiến. | Mạch Quốc Tấn |
| 2.0 | 22/08/2026 | Đồng bộ sáu cột Kanban, WIP, Trunk-Based, evidence và loại bỏ tham chiếu kế hoạch không tồn tại. | Mạch Quốc Tấn |

## Mục lục

- [Mục đích và phạm vi](#1-mục-đích-và-phạm-vi)
- [Mô hình quy trình được lựa chọn](#2-mô-hình-quy-trình-được-lựa-chọn)
- [Vai trò và trách nhiệm](#3-vai-trò-và-trách-nhiệm)
- [Luồng công việc](#4-luồng-công-việc)
- [Đầu vào, hoạt động và đầu ra](#5-đầu-vào-hoạt-động-và-đầu-ra)
- [Điều kiện sẵn sàng và hoàn thành](#6-điều-kiện-sẵn-sàng-và-hoàn-thành)
- [Kiểm thử, tích hợp và phát hành](#7-kiểm-thử-tích-hợp-và-phát-hành)
- [Đo lường và cải tiến](#8-đo-lường-và-cải-tiến)
- [Truy vết và tài liệu tham khảo](#9-truy-vết-và-tài-liệu-tham-khảo)

## 1. Mục đích và phạm vi

Tài liệu mô tả cách nhóm Sebros tổ chức và kiểm soát hoạt động phát triển HCMUS-LDMS. Quy trình giúp các thành viên biết công việc được đưa vào từ đâu, ai chịu trách nhiệm, kết quả nào cần tạo ra và khi nào một công việc được xem là hoàn thành.

Quy trình áp dụng cho phiên bản đầu tiên trong 11 tuần, gồm các công việc: làm rõ yêu cầu, lập danh mục công việc, thiết kế kiến trúc, phát triển, kiểm thử, tích hợp, triển khai thử nghiệm và nghiệm thu. Quy trình không quy định chi tiết mã nguồn hoặc thay thế kế hoạch dự án.

## 2. Mô hình quy trình được lựa chọn

### 2.1. Mô hình Kanban

Nhóm sử dụng Kanban vì phạm vi có thể được làm rõ dần, công việc có nhiều phụ thuộc và nhóm cần ưu tiên luồng hoàn thành thay vì chia thời gian thành các Sprint cố định. Kanban trực quan hóa công việc trên bảng, giới hạn số việc đang làm và khuyến khích kéo việc mới chỉ khi còn năng lực.

Kanban không có nghĩa là làm việc không có kế hoạch. Nhóm vẫn có mục tiêu, phạm vi, mốc tham chiếu 11 tuần, tiêu chí nghiệm thu và kế hoạch điều chỉnh; thứ tự công việc có thể thay đổi theo phụ thuộc, rủi ro và phản hồi.

### 2.2. Các cột trên bảng

| Cột | Ý nghĩa và điều kiện chuyển |
|---|---|
| Ý tưởng | Nhu cầu đã ghi nhận nhưng chưa đủ điều kiện sẵn sàng. |
| Đã sẵn sàng | Đạt DoR, có owner/reviewer và phụ thuộc chính đã xử lý. |
| Đang thực hiện | Owner đang phát triển; có ngày bắt đầu và cập nhật trạng thái. |
| Đang xem xét | Có kết quả để review và kiểm thử theo AC. |
| Chờ xác nhận | Kiểm tra kỹ thuật đạt, đang chờ xác nhận nghiệp vụ/tài liệu khi cần. |
| Hoàn thành | Đạt DoD và có evidence. Tuần hoàn thành là field, không tạo cột mới. |

WIP: tối đa 1 card `Đang thực hiện` mỗi thành viên, 6 card toàn nhóm ở `Đang thực hiện` và 4 card ở `Đang xem xét`. Khi có việc bị chặn, nhóm ghi nguyên nhân, người hỗ trợ, hành động tiếp theo và blocked time; không nhận thêm việc để che giấu điểm nghẽn.

## 3. Vai trò và trách nhiệm

Nhóm gồm 6 sinh viên chuyên ngành Kỹ thuật phần mềm. Một thành viên có thể kiêm nhiệm nhiều vai trò, nhưng mỗi công việc phải có người chịu trách nhiệm chính và người xem xét rõ ràng.

| Vai trò | Trách nhiệm chính |
|---|---|
| Đại diện nhóm Sebros | Điều phối bảng Kanban, ưu tiên công việc, xử lý phụ thuộc và ghi nhận quyết định. |
| Đại diện nghiệp vụ Thư viện | Làm rõ nhu cầu, xem xét tiêu chí chấp nhận và xác nhận kết quả nghiệp vụ. |
| Phụ trách yêu cầu | Làm rõ yêu cầu, cập nhật câu chuyện người dùng, tiêu chí chấp nhận và truy vết. |
| Phụ trách kiến trúc | Đề xuất quyết định kỹ thuật, kiểm tra sự phù hợp với tài liệu kiến trúc và các yêu cầu phi chức năng. |
| Thành viên phát triển | Phân tích, thiết kế chi tiết, lập trình, tự kiểm tra và cập nhật mã công việc. |
| Thành viên kiểm thử và tích hợp | Chuẩn bị dữ liệu, kiểm thử, ghi lỗi, kiểm tra hồi quy và xác nhận điều kiện trước bàn giao. |

## 4. Luồng công việc

### 4.1. Luồng từ yêu cầu đến hoàn thành

1. **Ý tưởng:** ghi vấn đề, người sử dụng, kết quả mong muốn và nguồn yêu cầu.
2. **Đã sẵn sàng:** làm rõ phạm vi, AC, dữ liệu, rủi ro, owner/reviewer và phụ thuộc.
3. **Đang thực hiện:** thiết kế vừa đủ, phát triển, tự kiểm tra và cập nhật tài liệu.
4. **Đang xem xét:** review mã/tài liệu, chạy kiểm thử, ghi và sửa lỗi.
5. **Chờ xác nhận:** lấy xác nhận nghiệp vụ hoặc tài liệu khi DoD yêu cầu.
6. **Hoàn thành:** đạt DoD, có evidence và ghi ngày/tuần hoàn thành thực tế.

### 4.2. Quy tắc kéo việc

- Chỉ kéo việc từ **Đã sẵn sàng** khi có thành viên đủ năng lực và cột **Đang thực hiện** còn WIP.
- Ưu tiên hoàn thành việc đang làm trước khi nhận việc mới.
- Khi hoàn thành một công việc, ghi ngày và tuần hoàn thành vào card; không tạo cột Done theo tuần.
- Nếu công việc kéo dài do lịch học hoặc phụ thuộc, giữ ở **Đang thực hiện**, cập nhật lý do; không chuyển sang **Hoàn thành** theo lịch dự kiến.
- Ghi tuần hoàn thành, ngày hoàn thành và liên kết đến bằng chứng kiểm thử hoặc nghiệm thu trong bảng công việc hoặc nhật ký dự án.
- Việc có phụ thuộc chưa được giải quyết phải được đánh dấu chờ và ghi rõ người xử lý phụ thuộc trước khi đưa sang **Đang thực hiện**.
- Công việc phát sinh ngoài phạm vi phải được xem xét tác động trước khi đưa vào bảng.
- Các chức năng chỉ xem xét sau phiên bản đầu tiên không được lấy vào luồng khi phạm vi bắt buộc chưa ổn định.

## 5. Đầu vào, hoạt động và đầu ra

| Hoạt động | Đầu vào | Hoạt động chính | Đầu ra |
|---|---|---|---|
| Làm rõ yêu cầu | Đề xuất, viễn cảnh và phạm vi, phản hồi nghiệp vụ | Xác định người dùng, nhu cầu, quy tắc và phạm vi | Yêu cầu được cập nhật, câu chuyện người dùng, tiêu chí chấp nhận |
| Chuẩn bị công việc | Yêu cầu phần mềm và danh mục công việc | Ưu tiên, ước lượng cỡ, nhận diện phụ thuộc và kiểm tra điều kiện sẵn sàng | Hạng mục ở cột Đã sẵn sàng |
| Thiết kế | Yêu cầu đã sẵn sàng, tài liệu kiến trúc | Chọn cách thực hiện, cập nhật quyết định kỹ thuật và dữ liệu | Thiết kế hoặc quyết định kỹ thuật đủ để phát triển |
| Phát triển | Thiết kế, mã công việc, môi trường phát triển | Lập trình, tự kiểm tra, cập nhật cấu hình và tài liệu | Thay đổi mã nguồn có thể kiểm thử |
| Kiểm thử | Bản dựng, dữ liệu thử nghiệm, tiêu chí chấp nhận | Chạy kiểm thử, ghi kết quả, báo lỗi và kiểm tra lại | Kết quả kiểm thử, lỗi và bằng chứng sửa lỗi |
| Tích hợp | Thay đổi đã xem xét và kiểm thử | Hợp nhất theo Trunk-Based, chạy kiểm tra hồi quy phù hợp | Bản dựng tích hợp để tiếp tục xem xét/xác nhận |
| Nghiệm thu | Bản dựng, tiêu chí chấp nhận và hướng dẫn | Trình bày, nhận phản hồi và xác nhận kết quả | Xác nhận hoàn thành hoặc yêu cầu chỉnh sửa |

## 6. Điều kiện sẵn sàng và hoàn thành

### 6.1. Điều kiện sẵn sàng

Một hạng mục chỉ được đưa vào **Đã sẵn sàng** khi:

- Có người sử dụng, nhu cầu và kết quả mong muốn rõ ràng.
- Có mô tả đủ để nhóm hiểu thống nhất và ước lượng cỡ công việc.
- Có tiêu chí chấp nhận kiểm thử được, gồm trường hợp hợp lệ và không hợp lệ khi cần.
- Có mức độ ưu tiên, phụ thuộc chính, dữ liệu đầu vào và người xem xét.
- Không còn câu hỏi quan trọng có thể làm thay đổi đáng kể phạm vi.

### 6.2. Điều kiện hoàn thành

Một hạng mục chỉ được chuyển sang **Hoàn thành** khi:

- Mã nguồn hoặc sản phẩm cần thiết đã hoàn thiện và được xem xét.
- Kiểm thử phù hợp đã thực hiện; tiêu chí chấp nhận đạt.
- Không còn lỗi nghiêm trọng chưa xử lý trong phạm vi hạng mục.
- Thay đổi đã được tích hợp theo quy tắc quản lý mã nguồn của nhóm.
- Truy vết, hướng dẫn và tài liệu liên quan đã được cập nhật.
- Kết quả đã được Đại diện nghiệp vụ Thư viện hoặc người được ủy quyền xác nhận khi có yêu cầu.
- Có liên kết commit/PR, test evidence, reviewer và completion event trong [Nhật ký dự án](17-project-log.md).

## 7. Kiểm thử, tích hợp và phát hành

### 7.1. Kiểm thử

Kiểm thử được thực hiện xuyên suốt luồng, không đợi đến cuối 11 tuần. Tùy hạng mục, nhóm dùng kiểm thử đơn vị, kiểm thử tích hợp, kiểm thử chức năng, kiểm thử giao diện, kiểm thử quyền truy cập và kiểm thử nghiệm thu. Mỗi kết quả cần ghi dữ liệu, thao tác, kết quả mong đợi, kết quả thực tế và trạng thái theo [Kế hoạch kiểm thử và UAT](20-test-plan.md) và các gate trong [Kế hoạch quản lý chất lượng](19-quality-management-plan.md).

### 7.2. Tích hợp theo Trunk-Based

- Nhánh `main` là nơi tích hợp trung tâm.
- Nhánh `task/LDMS-xxx-mo-ta` hoặc `fix/mo-ta` chỉ tồn tại trong thời gian ngắn.
- Thành viên cập nhật từ `main`, thực hiện thay đổi nhỏ, tự kiểm tra và yêu cầu xem xét.
- Chỉ hợp nhất khi kiểm tra phù hợp đạt và không làm hỏng luồng hiện có.
- Sau khi hợp nhất, nhóm chạy lại các kiểm tra cần thiết và cập nhật bảng Kanban.

### 7.3. Phát hành phiên bản đầu tiên

Phiên bản đầu tiên được triển khai theo cấu hình đã thống nhất trong [Tài liệu kiến trúc phần mềm](05-software-architecture.md): frontend trên Vercel, backend trên Render, cơ sở dữ liệu PostgreSQL trên Neon và tệp trên Cloudflare R2. Thông tin bí mật được cấu hình bằng biến môi trường; không đưa khóa truy cập vào mã nguồn hoặc giao diện frontend.

Trước khi bàn giao, nhóm kiểm tra luồng tải lên → nhận dạng → hiệu chỉnh → tạo EPUB → xuất bản → tìm kiếm → đọc; kiểm tra quyền, dữ liệu lỗi, khả năng khởi động lại và hướng dẫn sử dụng.

## 8. Đo lường và cải tiến

Nhóm theo dõi các chỉ số để phát hiện điểm nghẽn, không dùng một chỉ số đơn lẻ để xếp hạng cá nhân:

| Chỉ số | Ý nghĩa |
|---|---|
| Thời gian chu kỳ | Thời gian từ khi bắt đầu thực hiện đến khi hoàn thành một hạng mục. |
| Thông lượng | Số hạng mục hoàn thành trong một khoảng thời gian. |
| Số việc đang làm | Mức độ công việc đồng thời và nguy cơ quá tải. |
| Thời gian bị chặn | Thời gian hạng mục không thể tiếp tục do phụ thuộc hoặc lỗi. |
| Tỷ lệ đạt lần đầu | Mức độ hạng mục đạt tiêu chí sau lần kiểm thử đầu tiên. |
| Lỗi lọt qua | Lỗi phát hiện sau khi hạng mục đã chuyển sang hoàn thành hoặc sau nghiệm thu. |
| Công việc làm lại | Phần công việc phải sửa do yêu cầu, thiết kế hoặc triển khai chưa đúng. |

Sau mỗi mốc rà soát, nhóm xem các điểm nghẽn, lỗi lặp lại, việc chờ lâu và thủ tục không cần thiết. Nhóm chọn một hoặc hai thay đổi quy trình có tác động rõ, áp dụng thử, theo dõi kết quả rồi cập nhật tài liệu nếu thay đổi được chấp thuận. Không tự tạo số liệu khi chưa thực sự đo.

## 9. Truy vết và tài liệu tham khảo

Quy trình được liên kết với các yêu cầu và hạng mục sau:

| Nội dung quy trình | Tài liệu liên quan |
|---|---|
| Phạm vi, vai trò và mục tiêu | [Đề xuất dự án](01-project-proposal.md), [Tài liệu viễn cảnh và phạm vi](02-vision-and-scope.md), [Ủy nhiệm dự án](03-project-charter.md) |
| Yêu cầu, điều kiện sẵn sàng và hoàn thành | [Yêu cầu phần mềm](04-software-requirements.md), [Danh mục công việc](04-product-backlog.md) |
| Kiến trúc, công nghệ và triển khai | [Tài liệu kiến trúc phần mềm](05-software-architecture.md) |
| Thời gian và mốc thực hiện | [Ước lượng dự án](10-project-estimate.md), [Bản mô tả công việc](12-statement-of-work.md) |

### Tài liệu tham khảo

- [Đề xuất dự án](01-project-proposal.md)
- [Tài liệu viễn cảnh và phạm vi](02-vision-and-scope.md)
- [Ủy nhiệm dự án](03-project-charter.md)
- [Yêu cầu phần mềm](04-software-requirements.md)
- [Danh mục công việc](04-product-backlog.md)
- [Tài liệu kiến trúc phần mềm](05-software-architecture.md)
- [Ước lượng dự án](10-project-estimate.md)
- [Bản mô tả công việc](12-statement-of-work.md)
- [Hợp đồng nhóm](16-team-contract.md)
- [Nhật ký dự án](17-project-log.md)
- [Sổ đăng ký rủi ro](18-risk-management-plan.md)
- [Kế hoạch quản lý chất lượng](19-quality-management-plan.md)
- [Kế hoạch kiểm thử và UAT](20-test-plan.md)
- [Kế hoạch vận hành và bảo mật](15-devops-and-operations.md)
