# BÁO CÁO PHẢN BIỆN & ĐÁNH GIÁ (EVALUATION REPORT)

## Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS (HCMUS-LDMS)

**Trường Đại học Khoa học Tự nhiên, ĐHQG-HCM (HCMUS)**
**Thư viện & Phòng Công nghệ Thông tin**

Phiên bản 3.0 • Tháng 7/2026 • Đánh giá dựa trên **Bộ 8 tài liệu Project Initiation & Planning v2.0** (`docs/01-project-idea.md` → `08-cost-time-resource.md`)

_Tài liệu nội bộ — dùng để hỗ trợ ra quyết định phê duyệt_

---

> 🧠 **Tư duy của Agent:**
> - **Phạm vi đánh giá:** Bộ 8 tài liệu Khởi tạo và Hoạch định Dự án v2.0 của đề tài mới "Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS (HCMUS-LDMS)".
> - **Giai đoạn dự án:** Khởi tạo (chưa triển khai). Các nhóm DORA (VII) và PIR (VIII) được đánh dấu N/A và thay bằng đánh giá mức độ sẵn sàng của kế hoạch đo lường.
> - **Mục tiêu:** Đánh giá khách quan, phản biện độc lập xem bộ tài liệu mới có đáp ứng các tiêu chuẩn nghiệp vụ và kỹ thuật theo khung lý thuyết không, đồng thời chỉ ra các khoảng trống cần hoàn thiện.

---

## 0. Giới thiệu & Phương pháp báo cáo

Báo cáo này tổng hợp kết quả phản biện và chấm điểm độc lập đối với hồ sơ dự án **Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS (HCMUS-LDMS)**. Tài liệu đánh giá bao gồm bộ 8 tệp tin Markdown đặc tả khởi tạo và hoạch định dự án:
1.  [01-project-idea.md](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/hcmus-projectmanage--lab/docs/01-project-idea.md)
2.  [02-project-proposal.md](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/hcmus-projectmanage--lab/docs/02-project-proposal.md)
3.  [03-vision-and-scope.md](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/hcmus-projectmanage--lab/docs/03-vision-and-scope.md)
4.  [04-feasibility-study.md](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/hcmus-projectmanage--lab/docs/04-feasibility-study.md)
5.  [05-project-charter.md](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/hcmus-projectmanage--lab/docs/05-project-charter.md)
6.  [06-architecture.md](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/hcmus-projectmanage--lab/docs/06-architecture.md)
7.  [07-product-backlog.md](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/hcmus-projectmanage--lab/docs/07-product-backlog.md)
8.  [08-cost-time-resource.md](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/hcmus-projectmanage--lab/docs/08-cost-time-resource.md)

### Thang điểm đánh giá chuẩn
*   **9 – 10:** Đáp ứng đầy đủ, có bằng chứng trích dẫn cụ thể.
*   **7 – 8:** Đáp ứng khá tốt, chỉ còn thiếu chi tiết nhỏ hoặc cần kiểm chứng thực tế.
*   **5 – 6:** Đáp ứng một phần — có đề cập nhưng thiếu số liệu hoặc xác nhận chính thức.
*   **3 – 4:** Yếu — rủi ro hiện hữu cao, giải pháp chưa rõ ràng.
*   **1 – 2:** Không đáp ứng / thông tin trống.
*   **N/A:** Tiêu chí chưa áp dụng ở giai đoạn này.

---

> 🧠 **Tư duy của Agent:**
> - **Nhóm I & II:** Đánh giá các khía cạnh quản lý dự án truyền thống và chất lượng sản phẩm phần mềm theo ISO/IEC 25010.
> - **Tiêu chí trọng tâm:** Xác định xem bộ tài liệu mới có cung cấp các NFRs (yêu cầu phi chức năng) cụ thể và thiết kế bảo mật chặt chẽ để giải quyết rủi ro bản quyền hay không.

## I. Tam giác sắt mở rộng (Quản lý dự án)

| Tiêu chí | Điểm | Phản biện & Bằng chứng trích dẫn |
| --- | --- | --- |
| **Thời gian** | 8/10 | [05-project-charter.md](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/hcmus-projectmanage--lab/docs/05-project-charter.md) mục 5 có Roadmap và Gantt timeline chi tiết 20 tuần, phân rõ Critical Path (WP4 số hóa). Tuy nhiên, nhân sự tham gia là kiêm nhiệm 50% nên rủi ro trễ tiến độ do quá tải công việc khác vẫn ở mức trung bình. |
| **Chi phí** | 8/10 | [04-feasibility-study.md](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/hcmus-projectmanage--lab/docs/04-feasibility-study.md) mục 3 tách bạch rõ Cost (bottom-up theo WBS) và Budget (CapEx: $45.000–$85.000 bao gồm dự phòng 15%). Chi phí đã cụ thể hóa máy scan và server ảo hóa. Vẫn cần báo giá thực tế của nhà cung cấp máy quét chữ V. |
| **Phạm vi** | 9/10 | [03-vision-and-scope.md](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/hcmus-projectmanage--lab/docs/03-vision-and-scope.md) mục 4 ghi rõ Deliverables, Constraints và Project Exclusions (loại trừ Turnitin và AI/RAG trong MVP). Feature Model ở mục 2 phân tách rõ ràng MVP và phi MVP. |
| **Chất lượng** | 8/10 | Đã bổ sung các chỉ số đo lường chất lượng cụ thể: tỷ lệ OCR tiếng Việt chính xác (CAR) ≥ 85%, thời gian phản hồi Elasticsearch < 3s, Uptime SLA ≥ 99.5% ([03-vision-and-scope.md#L162-L170](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/hcmus-projectmanage--lab/docs/03-vision-and-scope.md#L162-L170)). |
| **Sự hài lòng** | 6/10 | Đã đưa ra chỉ số KPI hài lòng độc giả ≥ 85%, nhưng mục Customer Discovery ([02-project-proposal.md#L69-L70](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/hcmus-projectmanage--lab/docs/02-project-proposal.md#L69-L70)) vẫn ghi nhận là dự kiến phỏng vấn 15-20 sinh viên ở WP1 chứ chưa có dữ liệu khảo sát thực tế. |
| **Mục tiêu KD** | 8/10 | Đã xây dựng mô hình hòa vốn Cost Avoidance dựa trên diện tích kho bãi Quận 5 thu hồi và tiết kiệm 85% công sức thủ thư ([04-feasibility-study.md#L81-L94](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/hcmus-projectmanage--lab/docs/04-feasibility-study.md#L81-L94)). Lập luận hiệu quả kinh tế chặt chẽ. |

*   **Điểm trung bình Nhóm I: 7.8 / 10**

---

## II. Chất lượng sản phẩm phần mềm (ISO/IEC 25010)

| Tiêu chí | Điểm | Phản biện & Bằng chứng trích dẫn |
| --- | --- | --- |
| **Functional suitability** | 8/10 | Feature Model tại [03-vision-and-scope.md](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/hcmus-projectmanage--lab/docs/03-vision-and-scope.md) mô tả đầy đủ luồng nghiệp vụ Scan-to-EPUB. Trình soạn thảo WYSIWYG/Markdown giúp sửa lỗi OCR trực quan. |
| **Performance efficiency** | 8/10 | Yêu cầu thời gian phản hồi tìm kiếm toàn văn dưới 3 giây đối với 500 người dùng đồng thời được đặc tả rõ ràng ([03-vision-and-scope.md#L162-L170](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/hcmus-projectmanage--lab/docs/03-vision-and-scope.md#L162-L170)). |
| **Compatibility** | 8/10 | Tích hợp xác thực Keycloak SSO và kết nối trực tiếp LDAP/AD của trường ([06-architecture.md#L42](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/hcmus-projectmanage--lab/docs/06-architecture.md#L42)), tương thích tốt với hạ tầng CNTT HCMUS. |
| **Usability** | 8/10 | Định hình rõ mockup màn hình hiệu chỉnh lỗi chính tả OCR (Split-screen) và trình đọc Web EPUB Reader responsive trên di động ([03-vision-and-scope.md#L173-L181](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/hcmus-projectmanage--lab/docs/03-vision-and-scope.md#L173-L181)). |
| **Reliability** | 8/10 | Thiết lập SLA Uptime ≥ 99.5%, RPO < 24h và RTO < 4h ([06-architecture.md#L57-L61](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/hcmus-projectmanage--lab/docs/06-architecture.md#L57-L61)). Chiến lược backup tự động sử dụng PgBackRest và Restic được nêu chi tiết. |
| **Security** | 8/10 | Bảo mật đa lớp: HTTPS TLS 1.3, mã hóa tĩnh tệp tin, sinh Signed URL giới hạn 15 phút, và vô hiệu hóa tính năng download/print/chuột phải trên Epub.js ([06-architecture.md#L62-L68](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/hcmus-projectmanage--lab/docs/06-architecture.md#L62-L68)). |
| **Maintainability** | 9/10 | Kiến trúc Modular Monolith trên FastAPI & React là lựa chọn tối ưu, dễ bảo trì đối với đội ngũ kỹ thuật nhỏ của trường ([06-architecture.md#L26-L31](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/hcmus-projectmanage--lab/docs/06-architecture.md#L26-L31)). |
| **Portability** | 8/10 | Đóng gói Docker & Docker Compose giúp triển khai linh hoạt trên các máy chủ ảo hóa vật lý của trường ([06-architecture.md#L45](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/hcmus-projectmanage--lab/docs/06-architecture.md#L45)). |

*   **Điểm trung bình Nhóm II: 8.1 / 10**

---

> 🧠 **Tư duy của Agent:**
> - **Nhóm III & IV:** Đánh giá các Yếu tố Thành công (Pinto & Slevin) và tính khả thi TELOS.
> - **Tiêu chí pháp lý:** Kiểm tra giải pháp bản quyền số hóa sách theo luật pháp Việt Nam. Các rủi ro vận hành phải có chủ sở hữu rõ ràng.

## III. Yếu tố Quyết định Thành công (Critical Success Factors)

| Tiêu chí | Điểm | Phản biện & Bằng chứng trích dẫn |
| --- | --- | --- |
| **Sứ mệnh dự án** | 8/10 | Sứ mệnh số hóa sách giáo trình, bảo tồn tri thức số và tối ưu hóa không gian đọc sách được định nghĩa nhất quán xuyên suốt 6 tài liệu. |
| **Hỗ trợ quản lý** | 7/10 | Ban Giám hiệu được định vị rõ vai trò Sponsor chịu trách nhiệm cấp ngân sách trong Power/Interest Grid ([05-project-charter.md#L41-L50](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/hcmus-projectmanage--lab/docs/05-project-charter.md#L41-L50)). Mục Signatures vẫn trống đang chờ phê duyệt. |
| **Lịch trình / kế hoạch** | 8/10 | Kế hoạch WBS 6 gói công việc chi tiết. Xác định rõ Critical Path là WP4 số hóa sách ([05-project-charter.md#L97-L121](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/hcmus-projectmanage--lab/docs/05-project-charter.md#L97-L121)). |
| **Tham vấn user** | 5/10 | Khảo sát người dùng thật vẫn ở dạng kế hoạch phỏng vấn trong WP1 chứ chưa thực thi ([02-project-proposal.md#L69-L70](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/hcmus-projectmanage--lab/docs/02-project-proposal.md#L69-L70)). |
| **Nhân sự** | 7/10 | Định nghĩa rõ vai trò kiêm nhiệm của 4 kỹ sư Phòng CNTT và 2 cán bộ Thư viện ([05-project-charter.md#L70-L79](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/hcmus-projectmanage--lab/docs/05-project-charter.md#L70-L79)). Bổ sung thêm lực lượng sinh viên CTV biên tập. |
| **Giám sát & phản hồi** | 8/10 | Quy định nhịp độ báo cáo (sprint review 2 tuần, họp giao ban tuần, kết thúc giai đoạn báo cáo BGH) rõ ràng ([05-project-charter.md#L133-L138](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/hcmus-projectmanage--lab/docs/05-project-charter.md#L133-L138)). |
| **Giao tiếp** | 8/10 | Đã xây dựng Bảng chiến lược tương tác chi tiết theo từng nhóm Stakeholder ([05-project-charter.md#L53-L68](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/hcmus-projectmanage--lab/docs/05-project-charter.md#L53-L68)). |
| **Xử lý sự cố** | 8/10 | Bảng ma trận rủi ro đã gán cụ thể Risk Owner cho từng đầu việc (ví dụ: Ban Giám đốc Thư viện chịu trách nhiệm rủi ro Bản quyền; Trưởng phòng CNTT chịu trách nhiệm rủi ro kỹ thuật rò rỉ file) ([04-feasibility-study.md#L95-L107](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/hcmus-projectmanage--lab/docs/04-feasibility-study.md#L95-L107)). |

*   **Điểm trung bình Nhóm III: 7.4 / 10**

---

## IV. Khả thi trước triển khai (TELOS)

| Tiêu chí | Điểm | Phản biện & Bằng chứng trích dẫn |
| --- | --- | --- |
| **Technical** | 8/10 | Giải pháp tự phát triển React + FastAPI + Tesseract + Pandoc khả thi cao, làm chủ mã nguồn. Có PoC cụ thể để test OCR và Pandoc ([03-vision-and-scope.md#L178-L181](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/hcmus-projectmanage--lab/docs/03-vision-and-scope.md#L178-L181)). |
| **Economic** | 7/10 | Dự toán CapEx và OpEx chi tiết. Mô hình hòa vốn Cost Avoidance mạch lạc. Tuy nhiên, vẫn cần báo giá máy quét chuyên dụng chính xác từ đối tác ([04-feasibility-study.md#L48-L80](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/hcmus-projectmanage--lab/docs/04-feasibility-study.md#L48-L80)). |
| **Legal** | 8/10 | Giải quyết tốt bằng cách trích dẫn Khoản 1 Điều 25 Luật SHTT Việt Nam (giới hạn quyền tác giả cho việc sao chép nội bộ giảng dạy không thương mại), bảo vệ bằng cơ chế Signed URL và chỉ số hóa giáo trình nội bộ trường ([04-feasibility-study.md#L98-L99](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/hcmus-projectmanage--lab/docs/04-feasibility-study.md#L98-L99)). |
| **Operational** | 7/10 | Quy trình đào tạo thủ thư và vận hành đã sẵn sàng. Sử dụng sinh viên làm CTV sửa lỗi giúp giảm tải vận hành cho cán bộ thư viện ([04-feasibility-study.md#L101-L102](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/hcmus-projectmanage--lab/docs/04-feasibility-study.md#L101-L102)). |
| **Scheduling** | 8/10 | Phương án triển khai MVP thí điểm cuốn chiếu (Phương án B) giảm thiểu áp lực tiến độ đường găng số hóa, tính khả thi cao ([05-project-charter.md#L106-L121](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/hcmus-projectmanage--lab/docs/05-project-charter.md#L106-L121)). |

*   **Điểm trung bình Nhóm IV: 7.6 / 10**

---

> 🧠 **Tư duy của Agent:**
> - **Nhóm V & VI:** Giá trị lâu dài và lựa chọn đầu tư.
> - **Nhóm VII & VIII:** Vì dự án chưa code nên DORA và PIR là N/A, nhưng tài liệu đã chuẩn bị tốt kế hoạch đo lường.

## V. Giá trị dài hạn (Atkinson & PMI Benefits)

*   **Benefits realization:** 7/10. Hệ thống có các KPI cụ thể về lượt đọc sách, độ chính xác OCR và Uptime để đo lường lợi ích thực chất sau khi chạy.
*   **Khả năng chấp nhận (Adoption):** 7/10. Kế hoạch chạy MVP cuốn chiếu giúp sinh viên làm quen định dạng EPUB sớm; có đào tạo và truyền thông đi kèm để tăng mức độ tiếp nhận.
*   **Phù hợp chiến lược:** 9/10. Hoàn toàn phù hợp với kế hoạch chuyển đổi số giai đoạn 2026-2030 của HCMUS.
*   **Mức độ cấp thiết:** 7/10. Cần có sản phẩm chạy trước kỳ khai giảng năm học 2026 để kịp cung cấp giáo trình số cho sinh viên khóa mới.

*   **Điểm trung bình Nhóm V: 7.5 / 10**

---

## VI. Tiêu chí lựa chọn đầu tư (Weighted Scoring Model)

*   **ROI kỳ vọng:** 7/10. Đo lường hiệu quả bằng giá trị Cost Avoidance và diện tích kệ sách giải phóng làm phòng tự học.
*   **Nguồn lực sẵn có:** 7/10. Đã liệt kê chi tiết tên vai trò và tỷ lệ phân bổ thời gian (50% kiêm nhiệm của nhóm kỹ thuật CNTT).
*   **Rủi ro & độ phức tạp:** 8/10. Bảng rủi ro chi tiết, phân nhóm rõ ràng và có phương án giảm thiểu cụ thể cho từng loại.

*   **Điểm trung bình Nhóm VI: 7.3 / 10**

---

## VII. Chỉ số kỹ thuật/DevOps (DORA) & VIII. Hậu triển khai (PIR)

*   **VII. DORA (Deployment Frequency, Lead Time, MTTR, CFR):** **N/A** (Hồ sơ dự án ở giai đoạn khởi tạo, chưa triển khai code thực tế).
*   **VIII. PIR (Post-Implementation Review):** **N/A** (Chưa go-live sản phẩm).
*   **Mức độ sẵn sàng của kế hoạch đo lường:** **8/10**. Dự án đã định nghĩa sẵn các chỉ số đo lường thành công (KPIs) và giả định tiên quyết tại mục 6 của Project Charter làm cơ sở cho việc kiểm toán PIR sau này.

---

## IX. Tổng hợp điểm số

Bảng điểm trung bình theo từng nhóm tiêu chí:

| Nhóm tiêu chí | Điểm trung bình | Nhận xét |
| --- | :---: | --- |
| **I. Tam giác sắt mở rộng** | **7.8 / 10** | Kế hoạch tiến độ và phạm vi rõ ràng; NFRs bổ sung đầy đủ; cần chốt giá thiết bị thực tế. |
| **II. Chất lượng sản phẩm (ISO 25010)** | **8.1 / 10** | Kiến trúc Modular Monolith hợp lý; các biện pháp bảo mật chống rò rỉ sách (Signed URL) thiết kế chặt chẽ. |
| **III. Yếu tố quyết định thành công** | **7.4 / 10** | Có phân bổ nguồn lực và quy tắc làm việc rõ ràng; đã gán Risk Owners cụ thể; cần thực hiện khảo sát người dùng. |
| **IV. Khả thi trước triển khai (TELOS)** | **7.6 / 10** | Khả thi kỹ thuật và pháp lý (Luật SHTT) tốt; lịch trình cuốn chiếu MVP thực tế. |
| **V. Giá trị dài hạn** | **7.5 / 10** | Phù hợp chiến lược chuyển đổi số; KPI đo lường lợi ích rõ ràng. |
| **VI. Tiêu chí lựa chọn đầu tư** | **7.3 / 10** | Lập luận cost avoidance tốt; rủi ro được hoạch định kỹ càng. |
| **VII. Chỉ số DevOps (DORA)** | **N/A** | Chưa có code thực tế. |
| **VIII. Hậu triển khai (PIR)** | **N/A** | Chưa go-live sản phẩm. |
| **ĐIỂM TRUNG BÌNH CHUNG** | **7.6 / 10** | **Đạt yêu cầu phê duyệt có điều kiện.** |

**Nhận định mẫu hình hồ sơ:** Điểm số trung bình chung tăng từ **6.1/10 (v1.0)** lên **7.6/10 (v2.0)** nhờ việc chuyển đổi toàn diện sang đề tài mới. Kiến trúc kỹ thuật custom (FastAPI/React/MinIO) giải quyết triệt để bài toán nghiệp vụ số hóa EPUB; phân tích pháp lý dựa trên Luật SHTT rõ ràng hơn; ma trận rủi ro đã có Risk Owner gán cụ thể giúp hồ sơ dự án đạt độ tin cậy cao.

---

## X. Kết luận & Khuyến nghị

> **QUYẾT ĐỊNH:** **ĐỒNG Ý phê duyệt có điều kiện** triển khai **Giai đoạn 0 (Khảo sát)** và **Giai đoạn 1 (Xây dựng MVP thí điểm)** của dự án HCMUS-LDMS. 

### Bốn điều kiện tiên quyết trước khi bước sang Giai đoạn 2 (Số hóa diện rộng toàn trường)

1.  **Hoàn thành chốt quy chế bản quyền:** Ban Giám đốc Thư viện phối hợp bộ phận Pháp chế hoàn thiện biểu mẫu consent và quy chế số hóa nội bộ trong Giai đoạn 0 (Milestone M1), bảo đảm có chữ ký số xác nhận của tác giả/giảng viên đối với tài liệu tự soạn.
2.  **Thực hiện khảo sát người dùng thật:** Nhóm dự án phải tiến hành tối thiểu 15-20 cuộc phỏng vấn sâu độc giả (sinh viên, giảng viên) trong Giai đoạn 1 để thu thập phản hồi về trải nghiệm đọc sách EPUB trên di động, khắc phục khoảng trống dữ liệu Customer Discovery.
3.  **Cung cấp báo giá thiết bị scan thực tế:** Phòng CNTT phối hợp Thư viện khảo sát và lấy báo giá chính thức của 02 máy quét sách chuyên dụng chữ V để chốt chính xác ngân sách CapEx đầu tư thiết bị.
4.  **Ký quyết định phân bổ nhân sự chính thức:** Trưởng phòng CNTT ký văn bản phê duyệt phân bổ chính thức thời gian làm việc (50% kiêm nhiệm) cho 4 kỹ sư tham gia dự án để đảm bảo tiến độ không bị ảnh hưởng bởi các công việc phát sinh khác.

---

## Phụ lục — Các khung tiêu chí đã sử dụng

1.  **Tam giác sắt mở rộng:** Chow & Cao (2008), Stankovic et al. (2013).
2.  **ISO/IEC 25010 (SQuaRE):** Hệ thống đánh giá chất lượng phần mềm quốc tế.
3.  **CHAOS Report (Standish Group):** Đánh giá rủi ro và tỷ lệ thành công dự án IT.
4.  **Pinto & Slevin (1987):** 10 yếu tố quyết định thành công của quản trị dự án.
5.  **TELOS Framework:** Khung đánh giá tính khả thi (Technical, Economic, Legal, Operational, Scheduling).
6.  **Atkinson "Square Route" (1999):** Đánh giá lợi ích dự án ngoài tam giác sắt truyền thống.
7.  **PMI Benefits Realization Management:** Đo lường giá trị thực tế sau triển khai.
8.  **Weighted Scoring Model:** Lựa chọn danh mục đầu tư dự án CNTT.
