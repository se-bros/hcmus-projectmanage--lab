# VIỄN CẢNH VÀ PHẠM VI DỰ ÁN

## Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS (HCMUS-LDMS)

### Thông tin tài liệu

| Trường thông tin | Nội dung |
| :--- | :--- |
| **Mã tài liệu** | `HCMUS-LDMS-VSD` |
| **Tên tài liệu** | Viễn cảnh và phạm vi dự án |
| **Tên dự án** | HCMUS-LDMS |
| **Đơn vị soạn thảo** | Sebros - Nhóm sinh viên đề xuất dự án |
| **Người xem xét** | Trưởng Phòng Công nghệ Thông tin và Giám đốc Thư viện |
| **Người phê duyệt** | Ban Giám hiệu Trường Đại học Khoa học Tự nhiên |
| **Cấp độ bảo mật** | Nội bộ |
| **Trạng thái tài liệu** | Chờ phê duyệt |

### Lịch sử phiên bản

| Phiên bản | Ngày phát hành | Mô tả thay đổi | Người thực hiện |
| :---: | :---: | :--- | :--- |
| 1.0 | 07/07/2026 | Khởi tạo tài liệu viễn cảnh và phạm vi. | Mạch Quốc Tấn |
| 2.0 | 14/07/2026 | Chuẩn hóa cấu trúc, thuật ngữ và mô tả quy trình hiện tại/tương lai. | Mạch Quốc Tấn |
| 3.0 | 17/07/2026 | Cập nhật vai trò người dùng, công nghệ và phạm vi theo đề xuất dự án. | Ân Tiến Nguyên An |
| 4.0 | 21/08/2026 | Việt hóa toàn bộ, đồng bộ với Đề xuất dự án đã chấp thuận, giới hạn phạm vi cho phiên bản đầu tiên trong 11 tuần, bổ sung phạm vi công việc, phương pháp đánh giá và cách cập nhật tài liệu, loại bỏ mục mô tả quá trình hình thành tài liệu và thống nhất cách gọi tài liệu Ủy nhiệm dự án trong nội dung tham chiếu. | Mạch Quốc Tấn |

## Mục lục

- [1. Giới thiệu](#1-giới-thiệu)
- [2. Viễn cảnh và định vị sản phẩm](#2-viễn-cảnh-và-định-vị-sản-phẩm)
- [3. Người dùng và nhu cầu](#3-người-dùng-và-nhu-cầu)
- [4. Quy trình hiện tại và quy trình đề xuất](#4-quy-trình-hiện-tại-và-quy-trình-đề-xuất)
- [5. Phạm vi sản phẩm](#5-phạm-vi-sản-phẩm)
- [6. Yêu cầu phi chức năng](#6-yêu-cầu-phi-chức-năng)
- [7. Sản phẩm bàn giao và nội dung loại trừ](#7-sản-phẩm-bàn-giao-và-nội-dung-loại-trừ)
- [8. Giả định, phụ thuộc và ràng buộc](#8-giả-định-phụ-thuộc-và-ràng-buộc)
- [9. Tiêu chí thành công](#9-tiêu-chí-thành-công)
- [10. Tài liệu tham chiếu](#10-tài-liệu-tham-chiếu)

---

## 1. Giới thiệu

Tài liệu này xác định viễn cảnh, người dùng, nhu cầu, phạm vi và các yêu cầu định hướng của HCMUS-LDMS. Hệ thống hỗ trợ thư viện số hóa tài liệu giấy, biên tập nội dung nhận dạng ký tự, xuất bản tài liệu EPUB và cung cấp chức năng tìm kiếm, đọc tài liệu trực tuyến cho người dùng nội bộ.

Tài liệu này được xây dựng từ [Đề xuất dự án](01-project-proposal.md). Các yêu cầu chi tiết, điều kiện chấp nhận và thứ tự ưu tiên được quản lý trong [Danh mục công việc](04-product-backlog.md).

### 1.1 Căn cứ và tài liệu liên quan

- Đề xuất dự án HCMUS-LDMS.
- Nhu cầu tiếp cận và bảo quản tài liệu học thuật của thư viện.
- Quy định pháp luật liên quan đến quyền tác giả và số hóa tài liệu.
- Định hướng kỹ thuật trong [Tài liệu kiến trúc](05-software-architecture.md).
- Các yêu cầu, điều kiện chấp nhận và tiêu chí hoàn thành trong [Danh mục công việc](04-product-backlog.md).

## 2. Viễn cảnh và định vị sản phẩm

### 2.1 Viễn cảnh

HCMUS-LDMS giúp thư viện chuyển một phần tài liệu giấy phù hợp thành tài liệu số có thể tìm kiếm, đọc trực tuyến và quản lý tập trung. Hệ thống hướng tới việc giảm trở ngại khi sinh viên tiếp cận học liệu, hỗ trợ thủ thư kiểm soát quy trình số hóa và bảo vệ tài liệu trong phạm vi quyền sử dụng được chấp thuận.

### Mục tiêu của dự án

- Cung cấp một phiên bản đầu tiên trong 11 tuần, tập trung vào quy trình tiếp nhận, nhận dạng ký tự, hiệu chỉnh, phê duyệt, xuất bản và đọc tài liệu.
- Giúp người dùng nội bộ tìm kiếm và đọc tài liệu số thuận tiện hơn.
- Giúp thư viện quản lý tập trung trạng thái tài liệu, chất lượng nội dung và quyền truy cập.
- Tạo nền tảng có thể tiếp tục mở rộng sau phiên bản đầu tiên mà không làm thay đổi phạm vi đã được chấp thuận.

### 2.2 Định vị sản phẩm

- **Dành cho:** sinh viên, giảng viên, nghiên cứu viên, thủ thư, biên tập viên và quản trị viên của HCMUS.
- **Đang gặp vấn đề:** khó tiếp cận tài liệu giấy ở cơ sở khác, khó tìm nội dung trong tệp ảnh quét, tài liệu có nguy cơ xuống cấp và quy trình số hóa còn nhiều thao tác thủ công.
- **HCMUS-LDMS là:** hệ thống trực tuyến nội bộ quản lý quy trình số hóa, xuất bản và đọc tài liệu.
- **Sản phẩm mang lại:** quy trình tiếp nhận ảnh quét, nhận dạng ký tự, hiệu chỉnh, phê duyệt, xuất bản EPUB, tìm kiếm toàn văn và đọc tài liệu có kiểm soát quyền truy cập.
- **Khác với:** việc lưu trữ tệp ảnh hoặc PDF rời rạc, không có bước hiệu chỉnh tập trung và khó tìm kiếm nội dung.

## 3. Người dùng và nhu cầu

### 3.1 Các bên liên quan

| Bên liên quan | Mối quan tâm hoặc trách nhiệm |
| :--- | :--- |
| Ban Giám hiệu | Phê duyệt chủ trương và định hướng đầu tư. |
| Ban Giám đốc Thư viện và thủ thư | Xác nhận quy trình nghiệp vụ, quản lý tài liệu nguồn và phê duyệt xuất bản. |
| Phòng Công nghệ Thông tin | Phát triển, triển khai, bảo trì và hỗ trợ kỹ thuật. |
| Bộ phận Pháp chế | Rà soát quyền số hóa, quyền sử dụng và chính sách truy cập. |
| Người đọc | Tìm kiếm, đọc tài liệu và phản hồi về khả năng sử dụng. |

### 3.2 Nhóm người dùng

| Nhóm người dùng | Nhu cầu chính |
| :--- | :--- |
| **Người đọc** | Đăng nhập, tìm kiếm thông tin hoặc nội dung tài liệu, đọc trên nhiều kích thước màn hình và lưu dấu vị trí đọc nếu chức năng được chấp thuận. |
| **Thủ thư** | Tiếp nhận tài liệu, nhập thông tin mô tả, theo dõi trạng thái số hóa, kiểm tra và phê duyệt xuất bản. |
| **Biên tập viên** | Đối chiếu ảnh quét với văn bản nhận dạng, sửa lỗi và gửi tài liệu chờ phê duyệt. |
| **Quản trị viên** | Quản lý tài khoản, vai trò, danh mục và cấu hình hệ thống. |

### 3.3 Môi trường sử dụng

- Thủ thư, biên tập viên và quản trị viên sử dụng máy tính kết nối mạng tại thư viện hoặc môi trường được nhà trường cho phép.
- Sinh viên, giảng viên và nghiên cứu viên truy cập hệ thống trên máy tính hoặc thiết bị di động thông qua mạng phù hợp với chính sách của nhà trường.
- Phiên bản đầu tiên tập trung vào giao diện trực tuyến; không bao gồm ứng dụng đọc ngoại tuyến riêng cho điện thoại.

### 3.4 Nhu cầu và cách đáp ứng

| Nhóm người dùng | Nhu cầu | Cách hệ thống đáp ứng |
| :--- | :--- | :--- |
| Người đọc | Tìm và đọc tài liệu thuận tiện hơn. | Tìm kiếm thông tin, tìm kiếm toàn văn và trình đọc trực tuyến. |
| Thủ thư | Quản lý quy trình số hóa và kiểm soát chất lượng. | Quản lý trạng thái, thông tin mô tả, hiệu chỉnh và phê duyệt. |
| Biên tập viên | Sửa văn bản nhận dạng nhanh và chính xác hơn. | Màn hình đối chiếu ảnh gốc với văn bản nhận dạng. |
| Quản trị viên | Quản lý người dùng và quyền truy cập. | Quản lý tài khoản, vai trò và quyền theo chức năng. |

## 4. Quy trình hiện tại và quy trình đề xuất

### 4.1 Hạn chế của quy trình hiện tại

Theo bối cảnh được mô tả trong Đề xuất dự án, người đọc có thể phải đến nơi lưu tài liệu giấy hoặc tự xử lý ảnh chụp, trong khi thủ thư phải quản lý tài liệu và yêu cầu số hóa bằng nhiều thao tác rời rạc. Tài liệu ảnh quét khó đọc trên màn hình nhỏ và không thuận tiện cho việc tìm kiếm nội dung.

Các hạn chế chính là:

- Khó tiếp cận tài liệu khi người đọc ở khác cơ sở.
- Tài liệu giấy có nguy cơ xuống cấp và chiếm không gian lưu trữ.
- Ảnh quét hoặc PDF tĩnh khó đọc và khó tìm kiếm toàn văn.
- Việc nhận dạng, hiệu chỉnh, phê duyệt và xuất bản chưa được quản lý trong một quy trình thống nhất.
- Quyền truy cập và việc phát hành tài liệu số cần được kiểm soát chặt chẽ hơn.

### 4.2 Quy trình đề xuất

Quy trình dự kiến gồm các bước:

1. Thủ thư tiếp nhận tài liệu và tải ảnh quét lên hệ thống.
2. Thủ thư bổ sung thông tin mô tả cho tài liệu.
3. Hệ thống nhận dạng ký tự và tạo văn bản thô.
4. Biên tập viên đối chiếu ảnh gốc, sửa lỗi và gửi tài liệu chờ phê duyệt.
5. Thủ thư kiểm tra, phê duyệt hoặc yêu cầu chỉnh sửa.
6. Hệ thống đóng gói tài liệu đã duyệt thành EPUB và lập chỉ mục tìm kiếm.
7. Người đọc đăng nhập, tìm kiếm và đọc tài liệu theo quyền được cấp.

Quy trình chi tiết, trạng thái công việc và điều kiện hoàn thành được quản lý trong [Danh mục công việc](04-product-backlog.md). Quyết định kỹ thuật liên quan được trình bày trong [Tài liệu kiến trúc](05-software-architecture.md).

## 5. Phạm vi sản phẩm

### 5.1 Trong phạm vi phiên bản đầu tiên

- Đăng nhập và quản lý quyền truy cập người dùng nội bộ.
- Quản lý tài liệu và thông tin mô tả cơ bản.
- Tải ảnh quét hoặc tệp tài liệu lên hệ thống.
- Nhận dạng ký tự tiếng Việt ở mức phù hợp với bộ tài liệu thử nghiệm.
- Đối chiếu, hiệu chỉnh và gửi nội dung chờ phê duyệt.
- Phê duyệt và xuất bản tài liệu EPUB.
- Tìm kiếm theo thông tin tài liệu và tìm kiếm toàn văn.
- Đọc tài liệu trực tuyến trên máy tính và thiết bị di động.
- Quản lý trạng thái tài liệu; nhật ký thao tác chi tiết được thực hiện khi hạng mục `LDMS-023` được đưa vào phạm vi.
- Kiểm thử, triển khai phiên bản đầu tiên và hướng dẫn sử dụng cơ bản.

### 5.2 Có thể xem xét sau phiên bản đầu tiên

- Đọc tài liệu ngoại tuyến bằng ứng dụng riêng.
- Trích dẫn tài liệu tự động theo nhiều mẫu.
- Tìm kiếm ngữ nghĩa và hỗ trợ tóm tắt bằng trí tuệ nhân tạo.
- Tích hợp với hệ thống chống đạo văn hoặc các hệ thống đào tạo khác.
- Mở rộng quy mô số hóa sang toàn bộ kho tài liệu.

Các chức năng cụ thể chỉ được đưa vào phạm vi khi có trong [Danh mục công việc](04-product-backlog.md) và được nhóm chấp thuận.

### 5.3 Phạm vi công việc của dự án

Phạm vi sản phẩm mô tả những gì HCMUS-LDMS cung cấp cho người dùng. Phạm vi công việc mô tả những việc nhóm cần thực hiện để tạo ra và bàn giao sản phẩm đó, gồm:

- Phân tích nhu cầu, xác nhận phạm vi và lập danh mục công việc.
- Thiết kế giao diện, kiến trúc và mô hình dữ liệu phù hợp với phiên bản đầu tiên.
- Phát triển chức năng, tích hợp các mô-đun và cấu hình môi trường triển khai.
- Kiểm thử, sửa lỗi, nghiệm thu với đại diện nghiệp vụ và kiểm tra quyền truy cập.
- Viết tài liệu, hướng dẫn sử dụng, triển khai và bàn giao phiên bản đầu tiên.

Các hoạt động vận hành lâu dài, số hóa toàn bộ kho tài liệu và phát triển các chức năng mở rộng không thuộc phạm vi công việc của phiên bản đầu tiên.

## 6. Yêu cầu phi chức năng

### 6.1 Hiệu năng

- Kết quả tìm kiếm toàn văn phải được đo trên bộ dữ liệu và môi trường được ghi nhận; ngưỡng chấp nhận được chốt trước UAT thay vì dùng số liệu chưa đo.
- Các thao tác chính như mở danh sách, xem thông tin và mở trình đọc phải được kiểm thử với dữ liệu, trình duyệt và thời gian phản hồi được ghi lại.
- Tác vụ nhận dạng ký tự có thể chạy nền để không buộc người dùng chờ trên cùng một màn hình.

### 6.2 Khả năng sử dụng

- Giao diện hiển thị được trên máy tính, máy tính bảng và điện thoại.
- Các bước tải tài liệu, hiệu chỉnh, phê duyệt, tìm kiếm và đọc phải có trạng thái rõ ràng.
- Màn hình hiệu chỉnh phải giúp người dùng đối chiếu ảnh gốc với văn bản nhận dạng.
- Giao diện và tài liệu hướng dẫn sử dụng bằng tiếng Việt.

### 6.3 Bảo mật và quyền riêng tư

- Người dùng phải đăng nhập trước khi truy cập chức năng hoặc tài liệu được bảo vệ.
- Quyền truy cập được phân theo vai trò và trạng thái tài liệu.
- Tệp gốc không được cung cấp công khai; đường dẫn truy cập tài liệu phải có thời hạn và được kiểm soát.
- Việc số hóa và phát hành tài liệu phải tuân thủ quyền sử dụng đã được xác nhận.

### 6.4 Độ tin cậy và khả năng phục hồi

- Hệ thống phải ghi nhận lỗi của các tác vụ chính và cho phép xử lý lại khi phù hợp.
- Dữ liệu và tệp quan trọng phải có phương án sao lưu theo điều kiện hạ tầng thực tế.
- Trạng thái tài liệu không được mất khi một tác vụ nhận dạng hoặc xuất bản thất bại.

### 6.5 Khả năng bảo trì và mở rộng

- Mã nguồn, cấu hình và hướng dẫn triển khai phải được quản lý trong kho mã nguồn của dự án.
- Các mô-đun chính cần có ranh giới rõ để có thể thay đổi hoặc mở rộng.
- Công nghệ và cấu hình triển khai phải phù hợp với nguồn lực của nhóm và hạ tầng được cấp.

### 6.6 Tương thích và tài liệu

- Hệ thống hoạt động trên các trình duyệt phổ biến ở phiên bản được nhóm hỗ trợ.
- Có tài liệu hướng dẫn cho người đọc, thủ thư và biên tập viên.
- Có tài liệu kỹ thuật đủ để cài đặt, kiểm thử và bàn giao hệ thống.

## 7. Sản phẩm bàn giao và nội dung loại trừ

### 7.1 Sản phẩm bàn giao

- Mã nguồn giao diện và máy chủ của hệ thống.
- Cấu hình local bằng Docker Compose/PostgreSQL/MinIO; cấu hình demo cloud Vercel/Render/Neon/R2 nếu môi trường này được dùng và smoke test đạt.
- Phiên bản đầu tiên có các chức năng trong phạm vi được chấp thuận.
- Bộ tài liệu hướng dẫn sử dụng, tài liệu kỹ thuật và hướng dẫn triển khai.
- Bộ tài liệu mẫu đã được phép sử dụng để trình diễn và nghiệm thu.

Danh sách sản phẩm bàn giao, chức năng và điều kiện nghiệm thu chi tiết xem [Bản mô tả công việc](12-statement-of-work.md).

### 7.2 Nội dung loại trừ

- Ứng dụng đọc sách ngoại tuyến riêng cho điện thoại.
- Thanh toán, thương mại hóa hoặc bán bản quyền tài liệu.
- Tự động hóa hoàn toàn phần cứng máy quét.
- Số hóa toàn bộ kho tài liệu trong phiên bản đầu tiên.
- Tích hợp với hệ thống bên ngoài nếu chưa được đưa vào danh mục công việc.

## 8. Giả định, phụ thuộc và ràng buộc

### 8.1 Giả định

- Nhà trường cung cấp hoặc cho phép sử dụng bộ tài liệu mẫu phù hợp với mục đích thử nghiệm.
- Các tài liệu đưa vào thử nghiệm đã được xác nhận quyền sử dụng.
- Thư viện cử người đại diện để xác nhận quy trình và nghiệm thu.
- Nhóm có thể sử dụng hạ tầng và công cụ mã nguồn mở phù hợp với phạm vi phiên bản đầu tiên.

### 8.2 Phụ thuộc

- Tiến độ phụ thuộc vào việc thống nhất quyền số hóa và quyền đọc tài liệu.
- Chất lượng nhận dạng phụ thuộc vào chất lượng ảnh quét và loại tài liệu.
- Việc triển khai phụ thuộc vào hạ tầng máy chủ, lưu trữ và tài khoản xác thực được cấp.
- Các yêu cầu chi tiết phụ thuộc vào thứ tự ưu tiên và khả năng thực hiện của nhóm.

### 8.3 Ràng buộc

- Thời gian thực hiện phiên bản đầu tiên là 11 tuần.
- Nhóm quản lý công việc theo luồng liên tục, ưu tiên hạng mục bắt buộc và giới hạn số việc đang thực hiện.
- Phạm vi phải được kiểm soát để không vượt quá nguồn lực, thời gian và hạ tầng được chấp thuận.
- Các nội dung liên quan đến bản quyền phải được xác nhận trước khi phát hành tài liệu thật.

### 8.4 Kiểm soát thay đổi phạm vi

- Mọi yêu cầu bổ sung hoặc loại bỏ chức năng phải được ghi nhận trong danh mục công việc.
- Nhóm phân tích ảnh hưởng của thay đổi đối với mục tiêu, thời gian 11 tuần, nguồn lực, chi phí, chất lượng và các tài liệu liên quan.
- Thay đổi làm ảnh hưởng đáng kể đến phạm vi phiên bản đầu tiên phải được đại diện nhóm và các bên có thẩm quyền xem xét, chấp thuận trước khi thực hiện.
- Sau khi được chấp thuận, nhóm cập nhật danh mục công việc, tài liệu liên quan và lịch sử quyết định; các hạng mục chưa cần thiết được chuyển sang giai đoạn sau.

## 9. Tiêu chí thành công

Phiên bản đầu tiên được xem là đạt mục tiêu khi:

- Quy trình tiếp nhận, nhận dạng, hiệu chỉnh, phê duyệt và xuất bản hoạt động trên bộ tài liệu thử nghiệm.
- Người dùng nội bộ có thể tìm kiếm và đọc tài liệu đã xuất bản.
- Vai trò và quyền truy cập chính được kiểm tra trước nghiệm thu.
- Tài liệu mẫu được bảo vệ theo quyền sử dụng đã được xác nhận.
- Hệ thống được kiểm thử, trình diễn, hướng dẫn sử dụng và bàn giao trong 11 tuần.

Tiêu chí chấp nhận chi tiết của từng chức năng xem [Danh mục công việc](04-product-backlog.md). Các chỉ số và điều kiện nghiệm thu của sản phẩm bàn giao xem [Bản mô tả công việc](12-statement-of-work.md).

### Cách đánh giá tài liệu và phạm vi

Tài liệu được đánh giá bằng cách đối chiếu với Đề xuất dự án và nhu cầu của các nhóm người dùng. Nhóm kiểm tra các điểm sau:

- Viễn cảnh và mục tiêu có giải quyết đúng vấn đề đã nêu hay không.
- Người dùng, nhu cầu và cách hệ thống đáp ứng có rõ ràng hay không.
- Phạm vi trong và ngoài dự án có đủ cụ thể để tránh mở rộng không kiểm soát hay không.
- Các yêu cầu phi chức năng, giả định, phụ thuộc và ràng buộc có phù hợp với lộ trình 11 tuần hay không.
- Tiêu chí thành công có thể kiểm tra được trong quá trình nghiệm thu hay không.

Kết quả đánh giá được dùng để cập nhật tài liệu, danh mục công việc và các tài liệu lập kế hoạch trước khi nhóm thực hiện các hạng mục liên quan.

### Cách sử dụng và cập nhật tài liệu

Sau khi được chấp thuận, tài liệu này được dùng làm căn cứ để xây dựng danh mục công việc, kiến trúc, ước lượng chi phí và kế hoạch thực hiện. Trong quá trình làm việc, nhóm dùng tài liệu để kiểm tra yêu cầu mới có phù hợp với viễn cảnh và phạm vi đã thống nhất hay không.

Khi có thay đổi về người dùng, nhu cầu, chức năng, thời gian hoặc ràng buộc, nhóm phân tích ảnh hưởng, xin chấp thuận nếu cần, cập nhật lịch sử phiên bản và đồng bộ các tài liệu liên quan. Những chức năng chưa cần thiết cho phiên bản đầu tiên được giữ trong danh mục công việc để xem xét ở giai đoạn sau.

## 10. Tài liệu tham chiếu

- [Đề xuất dự án](01-project-proposal.md): vấn đề, cơ hội, giá trị và quyết định đầu tư.
- [Nghiên cứu khả thi](08-feasibility-study.md): đánh giá khả thi về kỹ thuật, vận hành, pháp lý, nguồn lực và tài chính.
- [Ủy nhiệm dự án](03-project-charter.md): mục tiêu, vai trò, quyền hạn và ràng buộc của dự án.
- [Kiến trúc](05-software-architecture.md): các quyết định kỹ thuật, mô-đun, dữ liệu và triển khai.
- [Danh mục công việc](04-product-backlog.md): chức năng người dùng, điều kiện chấp nhận, mức độ ưu tiên và tiêu chí hoàn thành.
- [Chi phí, thời gian và nguồn lực](10-project-estimate.md): ước lượng và phân bổ nguồn lực.
- [Bản mô tả công việc](12-statement-of-work.md): sản phẩm bàn giao và điều kiện nghiệm thu.
