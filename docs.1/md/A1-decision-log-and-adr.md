# NHẬT KÝ QUYẾT ĐỊNH VÀ HỒ SƠ QUYẾT ĐỊNH KIẾN TRÚC

## Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS (HCMUS-LDMS)

### Thông tin tài liệu

| Trường          | Nội dung                                                                    |
| --------------- | --------------------------------------------------------------------------- |
| Mã tài liệu     | `HCMUS-LDMS-ADR`                                                            |
| Chủ sở hữu      | Technical Lead — Nguyễn Tuấn Anh                                            |
| Người điều phối | Project Manager — Mạch Quốc Tấn                                             |
| Phiên bản       | 1.1 — 24/08/2026                                                            |
| Trạng thái      | Baseline nội bộ đã được nhóm xác nhận; mức kiểm chứng được ghi tại từng ADR |

### Lịch sử phiên bản

| Phiên bản |    Ngày    | Thay đổi                                                                                     | Người cập nhật |
| --------: | :--------: | -------------------------------------------------------------------------------------------- | -------------- |
|       1.1 | 24/08/2026 | Chuẩn hóa nhật ký quyết định và mười hồ sơ quyết định kiến trúc.                             | Mạch Quốc Tấn  |
|       1.2 | 24/08/2026 | Đồng bộ baseline, Việt hóa thuật ngữ và loại bỏ tham chiếu tới tài liệu chưa thuộc bộ hồ sơ. | Mạch Quốc Tấn  |

## Mục lục

- [1. Mục đích và quy tắc](#1-mục-đích-và-quy-tắc)
- [2. Nhật ký quyết định](#2-nhật-ký-quyết-định)
- [3. ADR-001 Kiến trúc nguyên khối mô-đun](#3-adr-001-kiến-trúc-nguyên-khối-mô-đun)
- [4. ADR-002 Xử lý OCR và EPUB bằng tác vụ nền](#4-adr-002-xử-lý-ocr-và-epub-bằng-tác-vụ-nền)
- [5. ADR-003 Tách PostgreSQL và kho đối tượng](#5-adr-003-tách-postgresql-và-kho-đối-tượng)
- [6. ADR-004 PostgreSQL full-text search cho MVP](#6-adr-004-postgresql-full-text-search-cho-mvp)
- [7. ADR-005 RBAC phía máy chủ và tệp riêng tư](#7-adr-005-rbac-phía-máy-chủ-và-tệp-riêng-tư)
- [8. ADR-006 Tách môi trường cục bộ và môi trường đám mây chạy thử](#8-adr-006-tách-môi-trường-cục-bộ-và-môi-trường-đám-mây-chạy-thử)
- [9. ADR-007 Trunk-Based Development](#9-adr-007-trunk-based-development)
- [10. ADR-008 Chỉ xác nhận hoàn thành khi có bằng chứng](#10-adr-008-chỉ-xác-nhận-hoàn-thành-khi-có-bằng-chứng)
- [11. ADR-009 Bộ dữ liệu mẫu thay vì sản lượng quy mô lớn](#11-adr-009-bộ-dữ-liệu-mẫu-thay-vì-sản-lượng-quy-mô-lớn)
- [12. ADR-010 Chưa chọn mô hình triển khai vận hành thực tế](#12-adr-010-chưa-chọn-mô-hình-triển-khai-vận-hành-thực-tế)
- [13. Quy trình thay thế quyết định](#13-quy-trình-thay-thế-quyết-định)

## 1. Mục đích và quy tắc

Tài liệu lưu lý do, phương án thay thế, hệ quả và điều kiện kiểm chứng của các quyết định ảnh hưởng đến nhiều thành phần. `Chấp nhận cho baseline` nghĩa là quyết định được dùng làm nguồn chuẩn của bộ hồ sơ; không có nghĩa mọi phần triển khai và kiểm thử đều đã hoàn tất. Kết quả kiểm chứng ý tưởng kỹ thuật được trình bày trong tài liệu **Nghiên cứu tính khả thi**; bằng chứng triển khai và kiểm thử được ghi trong **Nhật ký dự án** và **Kế hoạch kiểm thử**.

Trạng thái dùng trong tài liệu:

- `Đề xuất`: đang xem xét.
- `Chấp nhận cho baseline`: nguồn chuẩn hiện hành của bộ hồ sơ.
- `Đã kiểm chứng`: có bằng chứng kỹ thuật đủ để kiểm tra lại.
- `Đã thay thế`: đã được ADR mới thay thế.
- `Đã bác bỏ`: không dùng, nhưng giữ lý do.

ADR không được sửa để xóa lịch sử quyết định. Khi đổi hướng, tạo ADR mới và đánh dấu ADR cũ `Đã thay thế`.

Chủ sở hữu theo vai trò: Nguyễn Tuấn Anh là Technical Lead, Nguyễn Quang Thái phụ trách Backend, Ân Tiến Nguyên An phụ trách DevOps và QA.

## 2. Nhật ký quyết định

| ADR     | Quyết định                                                            | Trạng thái             | Người phụ trách                 | Bằng chứng hoặc điều kiện còn thiếu                   |
| ------- | --------------------------------------------------------------------- | ---------------------- | ------------------------------- | ----------------------------------------------------- |
| ADR-001 | Dùng kiến trúc nguyên khối mô-đun cho phiên bản đầu tiên              | Chấp nhận cho baseline | Technical Lead                  | Xem xét ranh giới mô-đun và khả năng kiểm thử         |
| ADR-002 | OCR và EPUB chạy bằng tác vụ nền, có trạng thái và khả năng xử lý lại | Chấp nhận cho baseline | Backend                         | Kiểm thử khởi động lại, quá thời gian và xử lý lại    |
| ADR-003 | PostgreSQL lưu dữ liệu mô tả; kho đối tượng lưu tệp nguồn và EPUB     | Chấp nhận cho baseline | Technical Lead                  | Kiểm thử toàn vẹn và khôi phục                        |
| ADR-004 | Dùng tìm kiếm toàn văn của PostgreSQL cho phiên bản đầu tiên          | Chấp nhận cho baseline | Backend                         | Bộ dữ liệu và kết quả đo hiệu năng                    |
| ADR-005 | Kiểm tra quyền tại máy chủ, dùng kho riêng tư và liên kết có thời hạn | Chấp nhận cho baseline | Backend                         | Kiểm thử phân quyền và bảo mật                        |
| ADR-006 | Tách môi trường cục bộ và môi trường đám mây chạy thử                 | Chấp nhận cho baseline | DevOps                          | Kiểm tra nhanh trên môi trường đám mây                |
| ADR-007 | Dùng Trunk-Based Development với nhánh công việc ngắn                 | Chấp nhận cho baseline | PM và Technical Lead            | Bằng chứng từ Git và CI khi CI được áp dụng           |
| ADR-008 | Chỉ xác nhận Hoàn thành khi có đủ bằng chứng                          | Chấp nhận cho baseline | PM và QA                        | Sự kiện hoàn thành đầu tiên có đủ bằng chứng          |
| ADR-009 | Nghiệm thu bằng bộ dữ liệu mẫu có quyền sử dụng                       | Chấp nhận cho baseline | PM và người phụ trách nghiệp vụ | Danh mục dữ liệu mẫu được nhóm xác nhận               |
| ADR-010 | Chưa chọn mô hình triển khai vận hành thực tế cho phiên bản đầu tiên  | Chấp nhận cho baseline | PM và Technical Lead            | Nghiên cứu mở rộng, mô hình đe dọa và phê duyệt riêng |

## 3. ADR-001 Kiến trúc nguyên khối mô-đun

**Bối cảnh:** Nhóm có 6 sinh viên và 11 tuần. Baseline gồm 15 hạng mục Bắt buộc, tương ứng 26 điểm. Kiến trúc vi dịch vụ làm tăng khối lượng triển khai, theo dõi, bảo đảm tính nhất quán và vận hành.

**Quyết định:** Dùng một ứng dụng máy chủ FastAPI gồm các mô-đun theo nghiệp vụ, một ứng dụng giao diện React/TypeScript và ranh giới rõ giữa giao diện lập trình ứng dụng (API), nghiệp vụ và dữ liệu. Cách tổ chức này được gọi là kiến trúc nguyên khối mô-đun (`modular monolith`).

**Lựa chọn đã xem xét:** kiến trúc vi dịch vụ; tích hợp DSpace; ứng dụng nguyên khối không phân mô-đun.

**Hệ quả tích cực:** ít đơn vị triển khai; dễ cài đặt; giao dịch dữ liệu và gỡ lỗi đơn giản hơn.

**Đánh đổi:** lỗi tiến trình có thể ảnh hưởng nhiều mô-đun; cần kiểm soát quan hệ phụ thuộc; tiến trình xử lý nền có thể phải tách riêng khi hệ thống mở rộng.

**Điều kiện xem lại:** số liệu tải, mức xử lý đồng thời hoặc chu kỳ phát hành cho thấy cần tách; quan hệ phụ thuộc giữa các mô-đun cản trở kiểm thử độc lập.

## 4. ADR-002 Xử lý OCR và EPUB bằng tác vụ nền

**Bối cảnh:** OCR và tạo EPUB có thể kéo dài; xử lý đồng bộ sẽ giữ yêu cầu HTTP quá lâu và làm giảm độ tin cậy của trải nghiệm sử dụng.

**Quyết định:** API tạo tác vụ có các trạng thái Chờ xử lý, Đang xử lý, Hoàn tất hoặc Thất bại; đồng thời lưu số lần thử, lỗi và tài liệu liên quan. Phiên bản đầu tiên có thể chạy tiến trình xử lý nền cùng ứng dụng máy chủ vì kết quả kiểm chứng ý tưởng kỹ thuật đã đạt yêu cầu.

**Lựa chọn đã xem xét:** xử lý đồng bộ; dùng hàng đợi và tiến trình xử lý riêng ngay từ đầu; dùng dịch vụ OCR bên ngoài.

**Hệ quả:** giao diện theo dõi được trạng thái và cho phép xử lý lại; hệ thống cần giới hạn thời gian, phục hồi và tránh tạo kết quả ngoài ý muốn khi yêu cầu được lặp lại. Việc chạy cùng ứng dụng máy chủ chỉ phù hợp với phạm vi hiện tại, không được xem là hàng đợi bền vững cho môi trường vận hành thực tế.

**Điều kiện xác minh:** khởi động lại khi đang xử lý, quá thời gian, xử lý lại nhiều lần, tác vụ trùng và bảo toàn tệp nguồn cùng văn bản đã hiệu chỉnh.

## 5. ADR-003 Tách PostgreSQL và kho đối tượng

**Bối cảnh:** Dữ liệu mô tả và trạng thái cần được truy vấn theo quan hệ; tệp PDF, ảnh và EPUB lớn không phù hợp để lưu trực tiếp trong bảng dữ liệu của phiên bản đầu tiên.

**Quyết định:** PostgreSQL lưu bản ghi, quyền, tác vụ, dữ liệu mô tả, khóa đối tượng, phiên bản và mã kiểm tra. MinIO được dùng trong môi trường cục bộ; Cloudflare R2 được xem xét cho môi trường đám mây chạy thử. Các tệp đều được lưu riêng tư.

**Hệ quả:** linh hoạt giữa các môi trường và tránh làm cơ sở dữ liệu tăng kích thước không cần thiết; đổi lại phải bảo đảm tính nhất quán giữa cơ sở dữ liệu và kho đối tượng, dọn dữ liệu thừa, đối soát và khôi phục đúng ánh xạ.

**Điều kiện xác minh:** tải lên thất bại giữa chừng, tệp không có bản ghi, bản ghi trỏ tới tệp bị thiếu, mã kiểm tra không khớp và khả năng khôi phục.

## 6. ADR-004 PostgreSQL full-text search cho MVP

**Bối cảnh:** Chưa có dữ liệu chứng minh cần Elasticsearch hoặc OpenSearch; bổ sung một dịch vụ tìm kiếm riêng sẽ làm tăng phạm vi.

**Quyết định:** Dùng khả năng full-text search của PostgreSQL và lọc quyền trong truy vấn phía máy chủ.

**Hệ quả:** giảm thành phần phải vận hành; khả năng xếp hạng kết quả, hỗ trợ ngôn ngữ và quy mô có giới hạn. Không công bố ngưỡng tốc độ khi chưa đo trên bộ dữ liệu DS-07.

**Điều kiện xem lại:** phân vị 95 không đạt ngưỡng kiểm thử chấp nhận trên bộ dữ liệu đã xác nhận; yêu cầu xếp hạng, tìm gần đúng hoặc quy mô tìm kiếm vượt khả năng PostgreSQL.

## 7. ADR-005 RBAC phía máy chủ và tệp riêng tư

**Bối cảnh:** Ẩn nút trên giao diện không đủ để bảo vệ API hoặc liên kết trực tiếp đến tệp.

**Quyết định:** Ứng dụng máy chủ kiểm tra phiên đăng nhập, vai trò và quyền ở mọi thao tác được bảo vệ. Kho tệp là riêng tư; chỉ ứng dụng máy chủ tạo liên kết truy cập tạm thời sau khi kiểm tra quyền. Tài liệu nháp hoặc riêng tư bị loại khỏi kết quả tìm kiếm nếu người dùng không đủ quyền.

**Hệ quả:** chính sách được kiểm soát tập trung và có thể kiểm thử; cần ma trận vai trò, thời hạn liên kết, khả năng thu hồi và nhật ký cho hành động quan trọng. Hệ thống không tuyên bố cung cấp cơ chế quản lý bản quyền số tuyệt đối.

**Điều kiện xác minh:** gọi API trực tiếp, truy cập tệp ẩn danh hoặc bằng liên kết hết hạn, thay đổi vai trò, tìm kiếm tài liệu nháp và thử truy cập đối tượng không thuộc quyền.

## 8. ADR-006 Tách môi trường cục bộ và môi trường đám mây chạy thử

**Bối cảnh:** Kho mã nguồn có Docker Compose, PostgreSQL và MinIO; phương án đám mây có thể dùng Vercel, Render, Neon và Cloudflare R2. Hai môi trường phục vụ các mục đích khác nhau.

**Quyết định:** Môi trường cục bộ là nguồn chuẩn để phát triển và kiểm thử. Môi trường đám mây chạy thử chỉ được xem là sẵn sàng sau khi triển khai và kiểm tra nhanh thành công. Kết quả chạy thử không được dùng để kết luận hệ thống đã sẵn sàng vận hành thực tế hoặc triển khai tại chỗ.

**Hệ quả:** giảm mâu thuẫn cấu hình và có phương án dự phòng khi giới thiệu sản phẩm; phải giữ cấu hình tương thích, bảo vệ thông tin bí mật riêng cho từng môi trường và không dùng kết quả cục bộ thay cho bằng chứng trên đám mây.

**Điều kiện xác minh:** cài đặt mới thành công trên môi trường cục bộ và kiểm tra nhanh thành công trên đám mây với cùng cấu trúc cấu hình.

## 9. ADR-007 Trunk-Based Development

**Bối cảnh:** Nhóm nhỏ và lịch ngắn; nhánh tồn tại lâu hoặc GitFlow làm tăng thời gian chờ hợp nhất mã nguồn.

**Quyết định:** `main` là nhánh tích hợp; dùng `task/LDMS-xxx-mo-ta` hoặc `fix/mo-ta` ngắn; merge khi review/test phù hợp đạt.

**Hệ quả:** phản hồi nhanh và giảm khác biệt giữa các nhánh; đổi lại thay đổi phải nhỏ, nhánh `main` phải ổn định và cần bảo vệ nhánh cùng CI khi nhóm áp dụng CI.

**Điều kiện xem lại:** kho mã nguồn hoặc giảng viên yêu cầu quy trình khác; hoặc quy định triển khai yêu cầu nhánh phát hành riêng.

## 10. ADR-008 Chỉ xác nhận hoàn thành khi có bằng chứng

**Bối cảnh:** Nhật ký công sức cũ nhắc nhiều hạng mục nhưng chưa có đủ Pull Request, kiểm thử và kiểm thử chấp nhận nội bộ; cộng lặp điểm làm sai tốc độ hoàn thành.

**Quyết định:** Công sức và sự kiện hoàn thành là hai loại bản ghi riêng. Hạng mục chỉ được ghi Hoàn thành khi có Pull Request hoặc cam kết mã nguồn, bằng chứng kiểm thử, người xem xét, tiêu chí chấp nhận và xác nhận nghiệp vụ khi cần.

**Hệ quả:** số liệu phản ánh đúng thực tế nhưng phạm vi đã hoàn thành ban đầu có thể thấp; nhóm phải duy trì danh mục bằng chứng và không xác nhận hồi tố khi thiếu căn cứ.

**Điều kiện xác minh:** Danh sách hoàn thành có bản ghi đủ trường và việc kiểm tra ngẫu nhiên có thể mở được bằng chứng liên quan.

## 11. ADR-009 Bộ dữ liệu mẫu thay vì sản lượng quy mô lớn

**Bối cảnh:** Baseline không có nguồn lực và quyền sử dụng dữ liệu để cam kết xử lý 500 hoặc 2.000 tài liệu.

**Quyết định:** Nghiệm thu luồng trên bộ dữ liệu mẫu có quyền sử dụng, gồm đủ trường hợp thành công và lỗi để kiểm tra OCR, tìm kiếm và phân quyền.

**Hệ quả:** phù hợp với dự án môn học nhưng không chứng minh khả năng vận hành ở quy mô thực tế. Bộ dữ liệu phải ghi nguồn, quyền sử dụng, mã kiểm tra và kết quả chuẩn khi đo OCR.

**Điều kiện xem lại:** có dự án triển khai thực tế, ngân sách, người chịu trách nhiệm dữ liệu và kế hoạch số hóa được phê duyệt.

## 12. ADR-010 Chưa chọn mô hình triển khai vận hành thực tế

**Bối cảnh:** Môi trường đám mây chạy thử không bao quát tính sẵn sàng cao, tuân thủ, giám sát, sao lưu, xử lý sự cố, năng lực hệ thống và chi phí dài hạn.

**Quyết định:** Không xem Vercel, Render, Neon và Cloudflare R2 là baseline vận hành thực tế. Phương án vận hành thực tế hoặc triển khai tại chỗ phải được đánh giá và phê duyệt riêng khi dự án mở rộng.

**Hệ quả:** tránh cam kết vượt quá phạm vi nhưng vẫn cho phép chạy thử có kiểm soát. Không tuyên bố hệ thống sẵn sàng vận hành thực tế khi chưa có mô hình đe dọa, diễn tập khôi phục, giám sát, đánh giá năng lực và phê duyệt.

**Điều kiện xem lại:** đơn vị tài trợ hoặc Thư viện khởi tạo giai đoạn triển khai thực tế.

## 13. Quy trình thay thế quyết định

1. Ghi vấn đề, nguồn và ADR bị ảnh hưởng.
2. So sánh tối thiểu hai lựa chọn theo phạm vi, tiến độ, chất lượng, bảo mật, dữ liệu, vận hành và chi phí.
3. Thực hiện kiểm chứng ý tưởng kỹ thuật nếu quyết định phụ thuộc vào giả định kỹ thuật quan trọng.
4. Technical Lead đề xuất; PM đánh giá baseline; người phụ trách Backend, DevOps, QA hoặc nghiệp vụ tham gia khi có tác động tương ứng.
5. Tạo ADR mới, cập nhật trạng thái ADR cũ và các tài liệu nguồn trong cùng yêu cầu thay đổi.
6. Chạy kiểm tra định dạng, liên kết và cập nhật bằng chứng.

Tài liệu liên quan gồm **Kiến trúc phần mềm**, **Yêu cầu phần mềm**, **Kế hoạch quản lý rủi ro**, **Kế hoạch quản lý chất lượng** và **Định nghĩa quy trình phát triển phần mềm**.
