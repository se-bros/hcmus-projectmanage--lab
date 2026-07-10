# PROJECT CHARTER (WHO)

## Kho Lưu trữ Số Khóa luận Tốt nghiệp HCMUS

**Trường Đại học Khoa học Tự nhiên, ĐHQG-HCM (HCMUS) — Thư viện & Phòng Công nghệ Thông tin**

Phiên bản 1.0 • Tháng 7/2026

## Mục lục

* [1. Tổng quan & Phạm vi](#1-tổng-quan--phạm-vi)
* [2. Stakeholder Analysis](#2-stakeholder-analysis)
* [3. Cơ sở Vật chất & Nguồn lực](#3-cơ-sở-vật-chất--nguồn-lực)
* [4. Ma trận Trách nhiệm (RACI)](#4-ma-trận-trách-nhiệm-raci)
* [5. Lộ trình (Roadmap)](#5-lộ-trình-roadmap)

---

## 1. Tổng quan & Phạm vi

**Bối cảnh:** HCMUS hiện lưu trữ khóa luận tốt nghiệp dưới dạng bản cứng, gây quá tải không gian, rủi ro xuống cấp tài liệu, và phụ thuộc hoàn toàn vào thao tác thủ công. Dự án xây dựng một nền tảng kho lưu trữ số tập trung để số hóa, lưu trữ, phân quyền và quản lý khóa luận, kèm năng lực tìm kiếm toàn văn (chi tiết đầy đủ về vấn đề và giải pháp tại `02-project-proposal.md` và `03-vision-and-scope.md`).

**Phạm vi (tóm tắt):** MVP gồm nộp & duyệt trực tuyến, lưu trữ chuẩn hóa (Dublin Core), phân quyền 3 mức, tìm kiếm toàn văn, số hóa thí điểm 1 khoa; mở rộng số hóa toàn trường và tích hợp xác thực toàn trường ở pha sau; tìm kiếm ngữ nghĩa AI/RAG và công cụ chống đạo văn là hạng mục tùy chọn giai đoạn cuối.

**Ma trận Tác nhân, Trách nhiệm và Tác động Trước - Sau (Stakeholder Responsibility & Impact Matrix):**

| Tác nhân / Vai trò | Trách nhiệm trong dự án | Tác động TRƯỚC khi có hệ thống (Before / As-is) | Tác động SAU khi có hệ thống (After / To-be) |
| :--- | :--- | :--- | :--- |
| **Ban Giám hiệu**<br>*(Sponsor)* | • Phê duyệt chủ trương đầu tư và cấp ngân sách theo các giai đoạn.<br>• Ký ban hành quy chế về bản quyền số và quy chế tốt nghiệp sửa đổi. | • Thiếu công cụ đo lường và thực hiện chỉ tiêu chuyển đổi số cấp trường.<br>• Đối mặt với rủi ro thất thoát tài sản trí tuệ và rủi ro tranh chấp bản quyền học thuật. | • Đạt chỉ tiêu chuyển đổi số thư viện học thuật.<br>• Nâng cao vị thế và uy tín khoa học của nhà trường.<br>• Tối ưu hóa ngân sách dài hạn (giảm chi phí đầu tư kho vật lý). |
| **Ban Giám đốc Thư viện**<br>*(Client - Nghiệp vụ)* | • Chủ trì xây dựng yêu cầu nghiệp vụ và chuẩn hóa metadata (Dublin Core).<br>• Chỉ đạo công tác số hóa khóa luận cũ.<br>• Tiếp nhận bàn giao và quản lý vận hành hệ thống. | • Đau đầu vì kho chứa khóa luận giấy bị quá tải không gian lưu trữ.<br>• Gánh chịu chi phí bảo quản tài liệu vật lý lớn chống mối mọt, ẩm mốc.<br>• Khó khăn trong việc phục vụ độc giả từ xa do ràng buộc địa lý. | • Giải phóng diện tích kho bãi vật lý để làm phòng tự học cho sinh viên.<br>• Bảo tồn vĩnh viễn tài nguyên số an toàn trên hệ thống máy chủ.<br>• Quản lý và khai thác tri thức tập trung theo đúng chính sách bản quyền. |
| **Thủ thư / Cán bộ Thư viện**<br>*(User Nghiệp vụ)* | • Trực tiếp kiểm duyệt thông tin metadata và định dạng file PDF sinh viên nộp trực tuyến.<br>• Thiết lập thời hạn embargo hoặc mức phân quyền cho từng khóa luận. | • Mất hàng trăm giờ lao động thủ công mỗi mùa tốt nghiệp để nhận sách cứng và nhập liệu giấy.<br>• Mất thời gian đi vào các kệ kho bám bụi để tìm kiếm khóa luận giấy cho độc giả mượn đọc.<br>• Chịu áp lực đối chiếu thông tin tốt nghiệp thủ công dễ sai sót. | • Nghiệp vụ chuyển đổi hoàn toàn sang môi trường số qua Dashboard kiểm duyệt trực tuyến.<br>• Thời gian xử lý hồ sơ tốt nghiệp giảm từ vài ngày xuống còn vài phút.<br>• Không còn phải vận chuyển, sắp xếp và tìm kiếm sách cứng thủ công. |
| **Trưởng phòng CNTT**<br>*(Client - Kỹ thuật / PM)* | • Quản trị tiến độ dự án, điều phối nguồn lực phát triển kỹ thuật.<br>• Chuẩn bị hạ tầng máy chủ, mạng và cấu hình bảo mật.<br>• Thiết lập hệ thống sao lưu và khôi phục thảm họa (Backup & DR). | • Quản lý hạ tầng CNTT thư viện manh mún, thiếu tập trung.<br>• Khó kiểm soát an toàn thông tin khi sinh viên chia sẻ tài liệu số qua các kênh không chính thống.<br>• Chịu trách nhiệm nếu dữ liệu học thuật bị mất mát do lỗi phần cứng. | • Sở hữu nền tảng Repository số chuẩn quốc tế DSpace, dễ dàng tích hợp và mở rộng.<br>• Làm chủ cơ chế sao lưu tự động (PgBackRest, Restic) và an toàn thông tin (Keycloak, Signed URL).<br>• Tối ưu hóa hạ tầng máy chủ của trường. |
| **Đội ngũ kỹ thuật Phòng CNTT**<br>*(Dev & Network Engineer)* | • Cài đặt, cấu hình nền tảng DSpace 7.x/8.0 (Angular, Tomcat).<br>• Custom giao diện theo thương hiệu trường.<br>• Tích hợp SSO Keycloak, Solr, Elasticsearch, MinIO.<br>• Xây dựng CI/CD và vận hành kỹ thuật. | • Thường xuyên phải hỗ trợ kỹ thuật cho các phần mềm cũ lỗi thời, khó bảo trì.<br>• Thiếu kinh nghiệm thực tế triển khai hệ thống lưu trữ số quy mô lớn và các công cụ tìm kiếm mạnh mẽ. | • Làm chủ các công nghệ hiện đại (Docker, Elasticsearch, MinIO, Keycloak).<br>• Nhàn nhã hơn trong khâu bảo trì nhờ kiến trúc Modular Monolith ổn định và tự động hóa. |
| **Phòng Đào tạo / Sau đại học**<br>*(Bên liên quan quy chế)* | • Cung cấp danh sách sinh viên tốt nghiệp chính thức để hệ thống đối chiếu tự động.<br>• Đưa quy định nộp khóa luận số vào quy chế công nhận tốt nghiệp bắt buộc. | • Quy trình xét tốt nghiệp và thủ tục ra trường của sinh viên bị kéo dài do khâu đối chiếu thủ công liên phòng ban.<br>• Khó kiểm soát việc sinh viên đã thực sự hoàn thành nghĩa vụ nộp khóa luận hay chưa. | • Quy trình nộp và xác nhận hoàn thành nghĩa vụ tốt nghiệp diễn ra hoàn toàn tự động trên hệ thống.<br>• Giảm tải thủ tục hành chính, rút ngắn thời gian cấp bằng tốt nghiệp. |
| **Bộ phận Pháp chế & Lưu trữ**<br>*(Tư vấn rủi ro)* | • Thẩm định và ký duyệt biểu mẫu cam kết bản quyền số (Digital Consent Form).<br>• Giám sát tính pháp lý của việc phân quyền truy cập và chia sẻ tài liệu số. | • Lo ngại rủi ro pháp lý lớn khi nhà trường công bố các nghiên cứu mà không có sự đồng ý bằng văn bản của tác giả.<br>• Gặp khó khăn trong kiểm soát bản quyền tài liệu số. | • Triệt tiêu hoàn toàn rủi ro vi phạm bản quyền nhờ cơ chế ký Consent Form trực tuyến có bằng chứng số định danh SSO.<br>• Các mức phân quyền tự động nghiêm ngặt bảo vệ quyền sở hữu trí tuệ. |
| **Sinh viên tốt nghiệp**<br>*(Tác giả khóa luận)* | • Khai báo thông tin metadata khóa luận theo chuẩn Dublin Core.<br>• Tải file PDF khóa luận lên hệ thống.<br>• Ký số Consent Form và tự chọn mức phân quyền truy cập tài liệu. | • Tốn kém nhiều chi phí in ấn và đóng tập bìa cứng mạ vàng đắt đỏ.<br>• Phải di chuyển trực tiếp giữa các cơ sở để nộp sách cứng.<br>• Lo sợ nghiên cứu của mình bị đạo văn hoặc phát tán bất hợp pháp khi không có phân quyền. | • Tiết kiệm 100% chi phí in ấn khóa luận tốt nghiệp.<br>• Thực hiện nộp bài trực tuyến từ xa nhanh chóng trong 5-10 phút.<br>• Chủ động kiểm soát quyền tiếp cận nghiên cứu của mình (embargo tối đa 36 tháng).<br>• Có mã trích dẫn bền vững Handle ID để ghi vào CV. |
| **Độc giả**<br>*(Sinh viên, GV, Độc giả ngoài)* | • Tra cứu, tìm kiếm toàn văn và khai thác thông tin khoa học phục vụ học tập, nghiên cứu. | • Phải di chuyển trực tiếp đến thư viện Q5 trong giờ hành chính.<br>• Tìm kiếm khó khăn qua thẻ mục lục giấy nghèo nàn, chỉ đọc được bản cứng duy nhất tại chỗ và phải chép tay.<br>• Nghiên cứu bị gián đoạn nếu tài liệu bị rách hỏng. | • Tra cứu và tiếp cận nguồn tri thức học thuật 24/7 từ bất kỳ đâu qua Internet.<br>• Tìm kiếm toàn văn thông minh chính xác tới từng từ khóa.<br>• Tự động trích xuất trích dẫn (APA, IEEE) chuẩn xác trong 1 click chuột.<br>• Trải nghiệm đọc trực tuyến mượt mà. |

## 2. Stakeholder Analysis

### Stakeholder Register

| Tên/Nhóm | Vai trò | External/Internal | Mối quan tâm chính (Vested Interest) | Power | Interest |
| --- | --- | --- | --- | --- | --- |
| Ban Giám hiệu | Sponsor | Internal | Chỉ tiêu chuyển đổi số, hiệu quả ngân sách | Cao | Thấp–Trung |
| Thư viện | Client (chủ trì nghiệp vụ) | Internal | Giảm tải vận hành, quản lý metadata/bản quyền | Cao | Cao |
| Phòng Công nghệ Thông tin | Client (chủ trì kỹ thuật) | Internal | Triển khai đúng hạn, đúng ngân sách, hạ tầng ổn định | Cao | Cao |
| Phòng Đào tạo/Sau ĐH | User/liên quan quy chế | Internal | Gắn quy trình nộp khóa luận vào quy chế tốt nghiệp | Trung | Trung |
| Bộ phận pháp chế/lưu trữ | Tư vấn/kiểm soát rủi ro | Internal | Tuân thủ bản quyền, quy chế lưu trữ | Cao (có thể chặn dự án) | Thấp (tự nhiên) |
| Khoa / GVHD / Sinh viên | User cuối | Internal | Trải nghiệm nộp/tra cứu thuận tiện | Thấp | Cao |
| Nhà cung cấp scan/OCR thuê ngoài (nếu có) | Nhà cung cấp | **External** | Hợp đồng dịch vụ số hóa | Thấp | Thấp |

### Power/Interest Grid

| | Interest thấp | Interest cao |
| --- | --- | --- |
| **Power cao** | Ban Giám hiệu — **Giữ hài lòng**; Bộ phận pháp chế/lưu trữ — **Giữ hài lòng** (cần chủ động kéo vào, không để mặc định rơi vào nhóm Theo dõi vì rủi ro pháp lý là trọng yếu) | Thư viện, Phòng CNTT — **Quản lý sát sao** |
| **Power thấp** | Nhà cung cấp thuê ngoài — **Theo dõi** | Khoa/GVHD/Sinh viên, Phòng Đào tạo — **Giữ thông tin** |

### Chiến lược tương tác (Engagement Strategy)

| Nhóm | Tần suất/kênh |
| --- | --- |
| Quản lý sát sao (Thư viện, CNTT) | Họp tuần + báo cáo tiến độ trực tiếp trong suốt vòng đời dự án |
| Giữ hài lòng (Ban Giám hiệu) | Báo cáo tổng kết theo mốc giai đoạn (end of Phase) + xin phê duyệt go/no-go |
| Giữ hài lòng (Pháp chế/lưu trữ) | Tư vấn trực tiếp ngay từ Giai đoạn 0, không chờ đến khi có vấn đề phát sinh — do rủi ro pháp lý được xếp mức cao |
| Giữ thông tin (Phòng Đào tạo, Khoa/GVHD/Sinh viên) | Thông báo định kỳ qua email/thông báo chính thức; khảo sát lấy ý kiến trước UAT |
| Theo dõi (nhà cung cấp thuê ngoài) | Cập nhật qua hợp đồng/hóa đơn theo tiến độ công việc |

## 3. Cơ sở Vật chất & Nguồn lực

| Hạng mục | Nội dung |
| --- | --- |
| Không gian số hóa | Khu vực/phòng dành riêng để scan, tháo gáy, sắp xếp tài liệu theo lô |
| Thiết bị | Máy scan tốc độ cao, phần mềm OCR hỗ trợ tiếng Việt (license nếu cần) |
| Môi trường kỹ thuật | Môi trường dev/staging/production riêng biệt; hạ tầng cloud/server; công cụ sao lưu |
| Công cụ quản trị dự án | Công cụ theo dõi tiến độ (Jira/Trello hoặc tương đương), kênh giao tiếp nhóm |
| Nhân sự | Đội ngũ nòng cốt gồm: 04 nhân sự chuyên môn từ Phòng CNTT (01 Quản trị dự án kiêm Kỹ sư hệ thống, 02 Lập trình viên, 01 Kỹ sư mạng) được phân bổ chính thức kiêm nhiệm 50% thời gian làm việc trong 3 tháng triển khai cốt lõi; cùng với 02 cán bộ chuyên môn từ Thư viện chịu trách nhiệm kiểm duyệt metadata và quy trình xuất bản. |

## 4. Ma trận Trách nhiệm (RACI)

R = Responsible, A = Accountable, C = Consulted, I = Informed. Mỗi gói công việc chỉ có đúng **1** đơn vị Accountable.

| Gói công việc | Thư viện | Phòng CNTT | Phòng Đào tạo | Pháp chế/Lưu trữ | Ban Giám hiệu | Khoa/GVHD/SV |
| --- | --- | --- | --- | --- | --- | --- |
| WP1 — Khảo sát & Khởi động | **A**, R | R | C | C | I | — |
| WP2 — Hạ tầng & Nền tảng | C | **A**, R | — | — | I | — |
| WP3 — Phát triển & Tùy biến | C | **A**, R | — | — | I | — |
| WP4 — Số hóa tài liệu | **A**, R | C | — | C | I | — |
| WP5 — Kiểm thử & Nghiệm thu | R | **A**, R | — | — | I | C |
| WP6 — Triển khai & Vận hành | **A**, R | R | C | — | I | I |

## 5. Lộ trình (Roadmap)

![Sơ đồ lộ trình triển khai (Project Roadmap)](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/docs/images/project_roadmap.svg)

| Giai đoạn | Trọng tâm | Kết quả chính |
| --- | --- | --- |
| 0 — Khảo sát | Kiểm kê, chọn nền tảng, chốt baseline, **giải quyết quy trình consent pháp lý** | Báo cáo hiện trạng + quyết định build/buy + ngân sách chi tiết + quy trình consent được ký duyệt |
| 1 — MVP | Repository + tìm kiếm toàn văn + phân quyền + số hóa thí điểm 1 khoa | Hệ thống chạy thật quy mô nhỏ, đo được lượt truy cập |
| 2 — Mở rộng | Số hóa toàn bộ kho, tích hợp xác thực toàn trường | Phủ toàn bộ khóa luận; quy trình nộp trực tuyến chính thức |
| 3 — Nâng cao | Tìm kiếm ngữ nghĩa AI/RAG, tích hợp công cụ chống đạo văn | Truy vấn theo ngữ nghĩa; báo cáo trùng lặp |

**Milestones chính:** (M1) Chốt baseline + quy trình consent — cuối Giai đoạn 0; (M2) MVP go-live thí điểm 1 khoa — cuối Giai đoạn 1; (M3) Phủ toàn trường — cuối Giai đoạn 2.

**Critical Path:** khối lượng **số hóa (WP4)** là đường găng quyết định tổng thời gian dự án, không phải phần phát triển kỹ thuật — số hóa có thể chạy song song với WP2–WP3 nhưng vẫn là yếu tố giới hạn tiến độ tổng thể (chi tiết thời lượng từng gói tại `04-feasibility-study.md` và bảng dưới).

![Biểu đồ tiến độ Gantt (Project Timeline Gantt Chart)](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/docs/images/project_timeline.svg)

| Gói | Thời lượng | Cách chạy |
| --- | --- | --- |
| WP1 | 3–4 tuần | Tuần tự |
| WP2 | 3–4 tuần | Sau WP1 |
| WP3 | 8–10 tuần | Sau WP2 |
| WP4 (số hóa ~10.000+ cuốn) | 16–24 tuần | Song song WP2–3 |
| WP5 | 3–4 tuần | Sau WP3 |
| WP6 | 2–3 tuần | Sau WP5 |

**Tổng thời gian tới release:** ước tính 7–10 tháng nếu số hóa toàn trường trước khi release; rút xuống còn 3–4 tháng nếu chấp nhận release MVP cho 1–2 khoa thí điểm trước (khuyến nghị).


## 6. Tiêu chí Thành công & KPI

1. Tỷ lệ khóa luận được số hóa và đưa lên hệ thống (mục tiêu: ≥ 90% trong 18 tháng).
2. Số lượt truy cập/tải tài liệu mỗi tháng (thiết lập đường nền sau 3 tháng vận hành).
3. Thời gian trung bình để tìm và truy cập một khóa luận (giảm so với quy trình thủ công).
4. Tỷ lệ khóa luận mới nộp qua quy trình trực tuyến (mục tiêu: 100% sau Giai đoạn 2).
5. Mức độ hài lòng của sinh viên/giảng viên (khảo sát định kỳ).
6. Diện tích kho thu hồi được (chỉ tính sau khi có quy định lưu trữ cho phép).

**Giả định tiên quyết:** quy chế lưu trữ và quy trình consent bản quyền đã được xác nhận trước khi các KPI liên quan đến số hóa/công khai được đo lường.

## 7. Phương pháp luận & Quy tắc Làm việc

**Phương pháp luận:** áp dụng mô hình **lai (hybrid)** — gating theo giai đoạn kiểu **RUP** ở cấp roadmap (mỗi giai đoạn 0→3 có điều kiện tiên quyết và quyết định go/no-go rõ ràng trước khi cấp ngân sách giai đoạn kế tiếp — phù hợp vì đây là dự án nội bộ cần phê duyệt ngân sách theo từng đợt), kết hợp **Scrum** (sprint 2 tuần) trong nội bộ WP3 (Phát triển & Tùy biến) để lặp nhanh, điều chỉnh theo phản hồi UAT — phù hợp vì quy mô đội nhỏ (3–4 người) và cần linh hoạt tùy biến nền tảng có sẵn thay vì đặc tả cứng từ đầu.

**Quy tắc làm việc:** sprint review cuối mỗi 2 tuần trong WP3; báo cáo tiến độ hàng tuần giữa Thư viện và Phòng CNTT; báo cáo tổng kết cuối mỗi giai đoạn gửi Ban Giám hiệu để xin phê duyệt giai đoạn tiếp theo.

## 8. Chữ ký (Signatures)

| Vai trò | Họ tên | Chữ ký | Ngày |
| --- | --- | --- | --- |
| Đại diện Ban Giám hiệu (Sponsor) | | | |
| Đại diện Thư viện (Client) | | | |
| Đại diện Phòng CNTT (Client) | | | |
| Đại diện Bộ phận pháp chế/lưu trữ | | | |
