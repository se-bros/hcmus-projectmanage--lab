<!-- markdownlint-configure-file {"MD024":{"siblings_only":true}} -->

# ĐÁNH GIÁ ĐỘ ỔN ĐỊNH BỘ TÀI LIỆU `docs.1`

## Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS (HCMUS-LDMS)

**Ngày đánh giá ban đầu:** 22/08/2026  
**Ngày tái đánh giá sau cập nhật:** 22/08/2026  
**Phạm vi:** toàn bộ tài liệu Markdown, PDF và tài sản kiến trúc trong `docs.1`  
**Kết luận hiện tại:** **8,8/10 — bộ hồ sơ đã bao phủ đủ 21 câu hỏi theo `Final-Answer.md`, nhất quán về đường cơ sở và sẵn sàng cho rà soát/in thử; chưa được xem là đã nghiệm thu khi thiếu bằng chứng thực thi thật.**  
**Điểm trước cập nhật:** **5,6/10. Điểm sau vòng đồng bộ đầu tiên: 8,3/10.**

---

## 0. Tái đánh giá sau cập nhật

### 0.1. Kết quả điều hành

Bộ tài liệu đã được đồng bộ theo một đường cơ sở duy nhất: dự án môn học 11 tuần, 6 thành viên, Kanban sáu cột, 15 hạng mục Bắt buộc, 6 hạng mục Nên có và 5 hạng mục Có thể xem xét. Dữ liệu đầu vào là bộ mẫu đã xác nhận quyền; không còn cam kết không có căn cứ về 500/2.000 tài liệu hoặc ngân sách vận hành thật. Kiến trúc đã tách rõ môi trường local, demo cloud và hướng production; quy trình mã nguồn thống nhất theo Trunk-Based với nhánh tác vụ ngắn.

Bốn tài liệu có rủi ro cao nhất đã được tái lập:

- SOW sử dụng đúng đường cơ sở 11 tuần, phạm vi 15/6/5, tiêu chí nghiệm thu và quy trình thay đổi;
- Team Contract thống nhất vai trò PM, bảng Kanban, WIP, branching, quản trị AI và nguyên tắc không xem im lặng là đồng thuận;
- Estimate có nhu cầu 190 giờ-người, năng lực hữu dụng 198 giờ-người và buffer 8 giờ, đồng thời nêu rõ mức khả thi có rủi ro cao;
- Project Log tách effort khỏi completion, giữ nguyên dữ liệu lịch sử nhưng đánh dấu trạng thái DoD chưa kiểm chứng thay vì suy diễn hoàn thành.

### 0.2. Điểm hiện tại của từng tài liệu

| STT | Tài liệu | Trước sửa | Sau sửa | Nhận định hiện tại |
|---:|---|---:|---:|---|
| 1 | `README.md` | 4,5 | **8,5** | Danh mục, nguồn chuẩn và ma trận bao phủ 21 câu hỏi đã được đồng bộ; không còn liên kết kế hoạch không tồn tại. |
| 2 | `01-project-proposal.md` | 7,5 | **8,2** | Thống nhất trạng thái chờ phê duyệt, môi trường local/demo và phạm vi dữ liệu mẫu. |
| 3 | `02-vision-and-scope.md` | 7,5 | **8,3** | NFR có cách đo rõ hơn; phạm vi và profile triển khai khớp đường cơ sở. |
| 4 | `03-project-charter.md` | 6,5 | **8,2** | PM, trạng thái phê duyệt, liên kết nguồn và profile công nghệ đã sửa; chữ ký thật vẫn là đầu vào bên ngoài. |
| 5 | `04-software-requirements.md` | 7,5 | **8,5** | Đã tách gán danh mục khỏi quản trị catalog, bổ sung trạng thái và truy vết nghiệm thu. |
| 6 | `04-product-backlog.md` | 8,0 | **8,7** | Board, bằng chứng, cỡ ước lượng và acceptance criteria đã thống nhất; vẫn cần dữ liệu thực thi để xác nhận velocity. |
| 7 | `05-software-architecture.md` | 6,5 | **8,3** | Phân biệt local/demo/production, bổ sung vòng đời xử lý và lưu ý phục hồi job. |
| 8 | `08-feasibility-study.md` | 6,0 | **8,0** | Kết luận chuyển thành khả thi có điều kiện, đối chiếu 190/198 giờ và làm rõ profile hạ tầng. |
| 9 | `09-software-process-definition.md` | 6,0 | **8,4** | Kanban sáu cột, WIP, Trunk-Based, DoD và evidence đã đồng bộ với Team Contract. |
| 10 | `10-project-estimate.md` | 4,5 | **8,5** | Có ước lượng từng story, tổng effort, capacity và buffer; chênh lệch 8 giờ được giữ như cảnh báo rủi ro. |
| 11 | `12-statement-of-work.md` | 2,0 | **8,6** | Đã thay đường cơ sở cũ bằng cam kết 11 tuần, tiêu chí nghiệm thu và kiểm soát thay đổi có truy vết. |
| 12 | `16-team-contract.md` | 3,5 | **8,2** | Quy tắc điều hành nội bộ đã nhất quán; trạng thái vẫn Pending cho tới khi đủ 6/6 xác nhận. |
| 13 | `17-project-log.md` | 3,0 | **7,5** | Không còn dùng điểm story cộng trùng làm bằng chứng hoàn thành; commit/PR/test/UAT lịch sử vẫn chưa có để xác minh hồi tố. |

**Điểm trung bình sau sửa:** 107,9 / 130 = **8,30/10**, làm tròn **8,3/10**.

### 0.3. Kiểm chứng kỹ thuật sau cập nhật

- 25/25 tài liệu Markdown có PDF tương ứng và đã được tái xuất sau chỉnh sửa.
- Pipeline PDF ép cỡ chữ thân bài 11pt; toàn bộ PDF được tạo thành công và đều có text layer trích xuất được.
- Markdown lint: 25 tệp, 0 lỗi với cấu hình của bộ tài liệu.
- Liên kết nội bộ: 0 liên kết tệp hỏng trong 25 Markdown.
- Không còn tệp `*.temp.html` sau khi xuất.
- 7 SVG được phân tích cú pháp hợp lệ; kiến trúc có thêm luồng upload–OCR, trạng thái tài liệu, mô hình phân quyền và bản mẫu giao diện.

### 0.4. Giới hạn còn lại

Điểm 8,8 không có nghĩa bộ hồ sơ đã được ký hoặc sản phẩm đã hoàn thành. Các nội dung sau cố ý giữ ở trạng thái chưa xác nhận:

- chưa có đủ 6/6 xác nhận Team Contract và chữ ký phê duyệt của các bên;
- chưa có PoC, test, UAT, benchmark và security review để chứng minh các NFR;
- chưa có commit/PR/test evidence lịch sử đủ để nâng các dòng Project Log thành completion đã kiểm chứng;
- capacity chỉ cao hơn demand 8 giờ, nên mọi scope creep hoặc rework đều có thể phá vỡ mốc 11 tuần;
- demo cloud chỉ là profile mục tiêu cho trình diễn, không phải bằng chứng production readiness.

### 0.5. Vòng bổ sung theo `Final-Answer.md`

Tài liệu gốc của môn học yêu cầu 21 nhóm sản phẩm. Bộ hồ sơ đã được sắp lại đúng số câu và bổ sung các phần còn thiếu thực sự:

- Hướng dẫn sử dụng đi kèm câu 4;
- Chứng minh ý tưởng và biên bản PoC ở câu 6;
- Bản mẫu giao diện vector và kế hoạch lấy phản hồi ở câu 7;
- Kế hoạch dự án tích hợp ở câu 11;
- mô hình CI, CD và DevOps ở câu 13–15, phân biệt rõ cấu hình hiện có với phần chưa có evidence;
- Risk Plan, Quality Plan và Test Plan ở câu 18–20;
- Sổ bài học kinh nghiệm ở câu 21;
- ADR được giữ làm phụ lục kiến trúc, không chiếm sai số câu 13.

Điểm tăng từ 8,3 lên 8,8 chủ yếu do khoảng trống cấp bộ đã được lấp và ma trận 21 câu có nguồn trực tiếp. Điểm chưa vượt 9 vì PoC, chạy CI/CD, test/UAT, restore drill, phản hồi người dùng, chữ ký và completion evidence vẫn chưa được thực hiện hoặc chưa liên kết.

Các phần 1–11 dưới đây lưu lại kết quả đánh giá ban đầu để truy vết lý do sửa. Khi có khác biệt, **mục 0 là kết luận hiện hành và thay thế các nhận định trước sửa**.

---

## 1. Kết luận điều hành ban đầu

Bộ tài liệu có một **lõi nội dung mới khá tốt** gồm Đề xuất, Viễn cảnh và phạm vi, Yêu cầu phần mềm, Danh mục công việc, Kiến trúc, Nghiên cứu khả thi, Quy trình và Ước lượng. Nhóm tài liệu này đã tương đối thống nhất quanh các quyết định:

- phiên bản đầu tiên kéo dài 11 tuần;
- nhóm gồm 6 sinh viên;
- quản lý công việc theo Kanban;
- phạm vi cơ sở gồm 15 hạng mục Bắt buộc;
- các chức năng ghi chú, đánh dấu, trích dẫn và tìm kiếm mở rộng nằm sau phạm vi cơ sở;
- tài liệu thật chỉ được sử dụng sau khi xác nhận quyền;
- không tự tạo số liệu khảo sát, chi phí hoặc hiệu năng khi chưa có bằng chứng.

Tuy nhiên, bộ hồ sơ **chưa thể được xem là ổn định** vì SOW và Hợp đồng nhóm vẫn giữ đường cơ sở cũ, trái ngược với gần như toàn bộ tài liệu đã cập nhật ngày 21–22/08/2026. Đây không phải khác biệt diễn đạt nhỏ mà là xung đột ở các cam kết cốt lõi:

1. **Thời gian:** 11 tuần đối lập với 12 tuần và 20 tuần.
2. **Phạm vi:** 15 Bắt buộc / 6 Nên có / 5 Có thể xem xét đối lập với 16 Must-have / 7 Should-have / 3 Could-have.
3. **Sản lượng:** bộ tài liệu mẫu đối lập với cam kết 500 cuốn ở MVP và 2.000 cuốn ở giai đoạn tiếp theo.
4. **Ngân sách:** giả định 0 VNĐ cho dự án môn học đối lập với CapEx 77–106 triệu VNĐ và OpEx 15–30 triệu VNĐ/năm.
5. **Triển khai:** Vercel–Render–Neon–Cloudflare R2 đối lập với Docker Compose–PostgreSQL–MinIO tại chỗ.
6. **Quy trình mã nguồn:** Trunk-Based đối lập với GitFlow.
7. **Quản trị:** vai trò Project Manager không thống nhất ngay trong Hợp đồng nhóm; trạng thái “Đã chấp thuận” hoặc “Active” không đi cùng bằng chứng ký duyệt hợp lệ.
8. **Theo dõi:** Nhật ký cộng trùng điểm các story xuất hiện nhiều lần, không gắn commit/PR/test/UAT, nên chưa đủ làm bằng chứng hoàn thành hoặc dữ liệu hiệu chỉnh ước lượng.

Vì SOW là tài liệu cam kết và Hợp đồng nhóm là tài liệu điều hành, hai tài liệu này có khả năng làm vô hiệu nỗ lực đồng bộ của các tài liệu còn lại. Chỉ nên chốt bộ hồ sơ sau khi chọn **một đường cơ sở duy nhất** và cập nhật ngược toàn bộ tài liệu theo đường cơ sở đó.

---

## 2. Phạm vi kiểm tra và phương pháp chấm

### 2.1. Nội dung đã kiểm tra

Đánh giá đã đọc và đối chiếu:

- 13 tệp Markdown trong `docs.1`;
- 13 tệp PDF tương ứng;
- 3 sơ đồ PlantUML và 3 SVG kiến trúc;
- `README.md` ở root để đối chiếu trạng thái triển khai thực tế;
- `docker-compose.prod.yml` và cấu trúc `src` để kiểm tra tuyên bố kiến trúc/triển khai;
- lịch sử Git liên quan đến các story và tài liệu;
- liên kết nội bộ, fragment mục lục và quy tắc Markdown bằng kiểm tra tự động.

Đánh giá này **không chạy toàn bộ hệ thống, không chạy toàn bộ test và không xác nhận trực tiếp với Ban Giám hiệu, Thư viện hoặc Pháp chế**. Vì vậy, điểm số phản ánh độ ổn định và khả năng kiểm chứng của hồ sơ, không thay thế kiểm thử sản phẩm hoặc phê duyệt của các bên có thẩm quyền.

### 2.2. Tiêu chí chấm điểm

Mỗi tài liệu được chấm trên thang 10 theo sáu trục:

| Tiêu chí | Trọng số | Câu hỏi kiểm tra |
|---|---:|---|
| Đúng vai trò tài liệu | 15% | Nội dung có đúng mục đích của loại tài liệu không? |
| Đầy đủ và rõ ràng | 20% | Có đủ đầu vào, đầu ra, tiêu chí, giả định và giới hạn cần thiết không? |
| Nhất quán liên tài liệu | 25% | Phạm vi, thời gian, chi phí, vai trò, công nghệ và thuật ngữ có khớp tài liệu khác không? |
| Truy vết và kiểm chứng | 20% | Tuyên bố có nguồn, ID, bằng chứng, người phê duyệt hoặc phép đo tương ứng không? |
| Khả năng vận hành/cập nhật | 10% | Có chủ sở hữu, trạng thái, lịch sử phiên bản và cơ chế thay đổi rõ không? |
| Chất lượng trình bày/kỹ thuật | 10% | Liên kết, mục lục, Markdown, PDF và cấu trúc có dùng được không? |

### 2.3. Cách diễn giải điểm

| Điểm | Mức đánh giá | Ý nghĩa |
|---:|---|---|
| 9,0–10,0 | Rất ổn định | Có thể chốt sau rà soát hành chính nhỏ. |
| 8,0–8,9 | Ổn định | Nội dung tốt, chỉ còn lỗi cục bộ không làm đổi đường cơ sở. |
| 7,0–7,9 | Khá ổn định | Dùng tốt để làm việc nội bộ, cần sửa trước khi phê duyệt. |
| 6,0–6,9 | Trung bình | Có cấu trúc tốt nhưng còn lỗ hổng hoặc xung đột đáng kể. |
| 5,0–5,9 | Chưa ổn định | Chưa nên đóng băng phiên bản hoặc dùng làm hồ sơ chính thức. |
| Dưới 5,0 | Không ổn định | Cần sửa nền tảng, không chỉ chỉnh văn phong/định dạng. |

---

## 3. Bảng điểm tổng hợp từng tài liệu

| STT | Tài liệu | Điểm /10 | Mức ổn định | Nhận định chính |
|---:|---|---:|---|---|
| 1 | `README.md` | **4,5** | Không ổn định | Danh mục sai/thiếu, liên kết kế hoạch hỏng, mô tả một số tài liệu không còn đúng. |
| 2 | `01-project-proposal.md` | **7,5** | Khá ổn định | Cấu trúc tốt, trung thực về thiếu dữ liệu; bị kéo giảm bởi trạng thái phê duyệt và tham chiếu tới SOW không đồng bộ. |
| 3 | `02-vision-and-scope.md` | **7,5** | Khá ổn định | Phạm vi 11 tuần khá rõ; tiêu chí phi chức năng còn định tính và trạng thái phê duyệt chưa có bằng chứng. |
| 4 | `03-project-charter.md` | **6,5** | Trung bình | Vai trò, RACI, mốc tốt; phần ký duyệt và liên kết nguồn có lỗi nghiêm trọng. |
| 5 | `04-software-requirements.md` | **7,5** | Khá ổn định | SRS gọn, có ID/truy vết; một số ưu tiên và NFR chưa kiểm thử được hoặc không khớp backlog. |
| 6 | `04-product-backlog.md` | **8,0** | Ổn định nhất bộ | 26 story, AC, phụ thuộc và ưu tiên rõ; thiếu trạng thái/owner/bằng chứng thực tế và xung đột với SOW. |
| 7 | `05-software-architecture.md` | **6,5** | Trung bình | Có C4 và truy vết; đường triển khai chưa thống nhất với tài liệu khác và cấu hình thực tế trong repo. |
| 8 | `08-feasibility-study.md` | **6,0** | Trung bình | Bao phủ nhiều chiều và thận trọng pháp lý; kết luận khả thi còn chủ yếu định tính. |
| 9 | `09-software-process-definition.md` | **6,0** | Trung bình | Quy trình Kanban rõ; cột bảng, WIP và chiến lược nhánh không khớp tài liệu điều hành khác. |
| 10 | `10-project-estimate.md` | **4,5** | Không ổn định | Có phương pháp nhưng chưa tạo ra tổng ước lượng công sức/thời gian thực sự; bảng cốt lõi còn là mẫu. |
| 11 | `12-statement-of-work.md` | **2,0** | Không ổn định nghiêm trọng | Đường cơ sở cũ, tự mâu thuẫn về lịch, phạm vi, chi phí và trạng thái phê duyệt. |
| 12 | `16-team-contract.md` | **3,5** | Không ổn định | Trái SOW mới, trái quy trình Trunk-Based, vai trò PM tự mâu thuẫn và chưa có chữ ký. |
| 13 | `17-project-log.md` | **3,0** | Không ổn định | Tổng số học đúng theo dòng nhưng cộng trùng story; thiếu liên kết bằng chứng và không đủ cho throughput/forecast. |

**Điểm trung bình:** 73,0 / 130 = **5,62/10**, làm tròn **5,6/10**.

Điểm trung bình không phản ánh đầy đủ rủi ro: SOW có trọng lượng cam kết cao hơn các tài liệu mô tả. Do đó, về quyết định “có thể chốt hay chưa”, kết luận vẫn là **chưa thể chốt**.

---

## 4. Các xung đột liên tài liệu quan trọng

### 4.1. Đường cơ sở thời gian

| Nguồn | Tuyên bố | Đánh giá |
|---|---|---|
| Đề xuất, Viễn cảnh, Charter, Backlog, SRS, Kiến trúc, Khả thi, Quy trình, Ước lượng | 11 tuần | Đây là đường cơ sở mới chiếm đa số và được cập nhật gần nhất. |
| SOW | MVP tuần 12, toàn dự án 20 tuần | Trái trực tiếp với đường cơ sở 11 tuần. |
| Hợp đồng nhóm | Hoàn tất 16 Must-have trước tuần 12 | Tiếp tục sử dụng đường cơ sở cũ của SOW. |

SOW còn tự mâu thuẫn: sản phẩm “Kho 500 giáo trình” được ghi bàn giao ở tuần 17, nhưng mốc M1 lại yêu cầu 500 cuốn hoàn thành ở tuần 12. Đây là lỗi cam kết nội bộ ngay trong một tài liệu.

### 4.2. Phạm vi và phân loại backlog

Backlog và Ước lượng thống nhất:

- 15 Bắt buộc;
- 6 Nên có;
- 5 Có thể xem xét;
- tổng cộng 26 hạng mục.

SOW và Hợp đồng nhóm lại ghi:

- 16 Must-have;
- 7 Should-have;
- 3 Could-have.

SOW đưa các chức năng `LDMS-019`, `LDMS-020`, `LDMS-021`, `LDMS-024`, `LDMS-025` vào phạm vi cam kết, trong khi Backlog xác định phần lớn các mã này chỉ được xem xét sau khi phạm vi bắt buộc ổn định. Đặc biệt, SOW cam kết bookmark, highlight, ghi chú và trích dẫn, làm thay đổi trực tiếp định nghĩa MVP.

Ngoài ra, SRS ghi phân loại tài liệu trong phạm vi phiên bản đầu tiên và `YC-TL-05` là Bắt buộc, nhưng Backlog gán `LDMS-012` quản lý danh mục ở mức Nên có. Cần tách rõ:

- gán một danh mục có sẵn cho tài liệu là Bắt buộc; và
- quản trị cây danh mục là Nên có;

hoặc nâng `LDMS-012` thành Bắt buộc nếu không thể tách hai hành vi.

### 4.3. Sản lượng số hóa

Nhóm tài liệu mới chỉ cam kết dùng **bộ tài liệu mẫu** và loại trừ số hóa toàn bộ kho. SOW lại cam kết:

- 500 cuốn giáo trình CNTT trong giai đoạn MVP;
- thêm 2.000 cuốn ở giai đoạn số hóa diện rộng;
- 10–15 cộng tác viên scan/OCR;
- hai buổi tập huấn và triển khai toàn trường.

Đây là một chương trình triển khai vận hành quy mô lớn, không còn là phiên bản môn học 11 tuần. Không thể giữ hai cách hiểu này trong cùng một bộ hồ sơ.

### 4.4. Ngân sách

Ước lượng dự án ghi ngân sách tiền tệ phiên bản đầu tiên là **giả định 0 VNĐ**, chỉ theo dõi công sức. SOW ghi:

- CapEx 77–106 triệu VNĐ;
- OpEx 15–30 triệu VNĐ/năm;
- năm đầu tiên phải dưới 100 triệu VNĐ.

Cam kết dưới 100 triệu không thỏa ngay tại biên trên:

- riêng CapEx tối đa đã là 106 triệu;
- CapEx + OpEx năm đầu tiên nằm trong khoảng 92–136 triệu;
- vì vậy khoảng dự toán và ràng buộc ngân sách không tương thích.

Nếu bộ hồ sơ là bài môn học, nên chọn đường cơ sở 0 VNĐ có gắn nhãn giả định và lập một **kịch bản mở rộng thương mại riêng**, không trộn vào SOW của phiên bản đầu tiên. Nếu đây là đề xuất triển khai thật, phải bỏ giả định 0 VNĐ và xây lại Estimate bằng dữ liệu báo giá, năng suất số hóa, đơn giá nhân công và dự phòng có nguồn.

### 4.5. Kiến trúc và triển khai

Có ít nhất ba cách mô tả đang cùng tồn tại:

1. Đề xuất, Charter và Khả thi: React, FastAPI, PostgreSQL, MinIO, Docker Compose.
2. Kiến trúc, Quy trình và Ước lượng: Vercel, Render, Neon PostgreSQL, Cloudflare R2.
3. SOW và Hợp đồng nhóm: Docker Compose ba dịch vụ, PostgreSQL, MinIO tại chỗ/VMware.

Đối chiếu repository cho thấy:

- môi trường local hiện dùng Docker Compose + PostgreSQL + MinIO;
- frontend có cấu hình Vercel;
- mã nguồn hỗ trợ kết nối Cloudflare R2 qua giao diện S3;
- `docker-compose.prod.yml` còn có Nginx, API, PostgreSQL, MinIO, Mailhog, Prometheus và Grafana, không phải “3 services” như SOW;
- README root vẫn mô tả MinIO cho luồng local và chưa chứng minh toàn bộ đường triển khai Render–Neon–R2 đã được nghiệm thu.

Giải pháp hợp lý là mô tả rõ ba profile:

- **Local development:** Docker Compose, PostgreSQL, MinIO;
- **Demo cloud:** Vercel, Render, Neon, Cloudflare R2;
- **Production/on-premise:** chỉ đưa vào khi có quyết định và bằng chứng triển khai.

Không nên gọi cả ba profile là “tech stack chính thức” mà không phân môi trường.

### 4.6. Kanban, cột công việc và chiến lược nhánh

Ba tài liệu định nghĩa ba board khác nhau:

- Backlog: Ý tưởng → Đã sẵn sàng → Đang thực hiện → Đang kiểm thử → Chờ xác nhận → Hoàn thành.
- Quy trình: Todo → In progress → In review → Done – Tuần X.
- Hợp đồng nhóm: Backlog → Ready → In Progress → Review → Done.

Quy trình không đặt con số WIP cụ thể; Hợp đồng nhóm đặt tối đa 1 card In Progress cho mỗi người. Đây có thể là một chính sách hợp lý, nhưng phải được trỏ từ Quy trình và Backlog thay vì tồn tại riêng.

Chiến lược nhánh cũng đối lập:

- Quy trình quy định Trunk-Based, nhánh `task/<mã-công-việc>` tồn tại ngắn và hợp nhất vào `main`.
- Hợp đồng nhóm quy định GitFlow với `main`, `develop`, `feature/*`, `release/*`, `hotfix/*`.

Nhóm phải chọn một mô hình. Với dự án 11 tuần và 6 người, Trunk-Based với nhánh ngắn phù hợp hơn với tài liệu mới, nhưng quyết định cuối cùng phải phản ánh đúng cách repository đang vận hành.

### 4.7. Vai trò và quyền quyết định

Hợp đồng nhóm tự mâu thuẫn:

- danh sách thành viên ghi Ân Tiến Nguyên An là Project Manager;
- mục tiêu cá nhân và bảng phân vai kỹ thuật ghi Mạch Quốc Tấn là Project Manager.

SOW cũng ghi Mạch Quốc Tấn là Project Manager. Charter chỉ dùng chức danh “Đại diện nhóm Sebros” mà chưa ánh xạ chức danh này tới một người cụ thể. Cần chốt:

- Project Manager;
- Product/Business Owner hoặc Đại diện nghiệp vụ;
- người chịu trách nhiệm cập nhật backlog;
- người có quyền phê duyệt thay đổi nhỏ/lớn;
- người ký nghiệm thu.

### 4.8. Trạng thái và chữ ký

Đề xuất, Viễn cảnh, Charter và Khả thi ghi “Đã chấp thuận”. Charter còn điền “(Đã ký)” cho bốn vai trò nhưng:

- họ tên chỉ là tên vai trò chung;
- ngày ký để trống;
- không có tham chiếu biên bản, quyết định hoặc chữ ký số.

Hợp đồng nhóm ghi “Active (Có hiệu lực)” nhưng toàn bộ sáu chữ ký và ngày ký đều trống. SOW ghi “Pending Approval”, phù hợp với bảng chữ ký trống, nhưng điều này làm các tài liệu khác không thể viện dẫn SOW như một cam kết đã thống nhất.

Nguyên tắc nên áp dụng:

- chưa có bằng chứng ký thì trạng thái là `Draft`, `In Review` hoặc `Pending Approval`;
- chỉ chuyển `Approved/Active` khi có tên người duyệt, ngày duyệt và bằng chứng;
- không dùng chữ “Đã ký” như dữ liệu mẫu.

### 4.9. Nhật ký và dữ liệu ước lượng

Tổng 37 điểm, 14 giờ 50 phút và 730K token trong Nhật ký được cộng đúng theo từng dòng. Tuy nhiên, tổng đó **không phải thông lượng story duy nhất** vì:

- `LDMS-001/009/010/018` xuất hiện hai lần và bị cộng điểm hai lần;
- `LDMS-008` và `LDMS-026` cũng xuất hiện ở nhiều dòng;
- dòng `LDMS-008/026` còn mô tả “Reader/Search placeholder”, không đủ chứng minh cả story đã đạt DoD;
- các dòng không gắn commit, PR, test result, bản dựng hoặc xác nhận nghiệp vụ;
- một số story lớn được chia đều thành 15–30 phút theo giả định, dễ làm sai mô hình ước lượng;
- lịch sử Git có nhiều commit/PR hơn số phiên được ghi, nên quy tắc “sau mỗi phiên AI phải log” chưa được chứng minh là đã tuân thủ đầy đủ.

Nhật ký cần tách ba khái niệm:

1. **Effort log:** mỗi phiên làm việc, có thể lặp story.
2. **Completion event:** mỗi story chỉ có một lần đạt Done cho mỗi phiên bản/đợt mở lại.
3. **Evidence:** commit/PR/test/UAT/deployment tương ứng.

Chỉ bảng completion event mới được dùng để tính throughput.

---

## 5. Đánh giá chi tiết từng tài liệu

## 5.1. `docs.1/README.md` — 4,5/10

### Điểm tốt

- Có bảng ánh xạ tài liệu với câu hỏi vấn đáp.
- Liên kết tới các tệp hiện có phần lớn rõ ràng.
- Nêu được những câu hỏi không có tài liệu riêng và hướng xử lý tổng quát.

### Vấn đề

- Liệt kê `11-project-plan.md` và `11-project-plan.pdf`, nhưng hai tệp không tồn tại trong `docs.1`.
- Mô tả Estimate là “COCOMO II” trong khi tài liệu hiện tại dùng pilot 2 ngày, cỡ tương đối và giả định công sức, không dùng COCOMO II.
- Mô tả Architecture có “Database Schema”, nhưng tài liệu kiến trúc chỉ nêu nhóm dữ liệu, không có schema/ERD chi tiết.
- Mô tả Process có AI Coding Assistants, trong khi tài liệu Quy trình hiện tại gần như không định nghĩa governance AI; phần này nằm chủ yếu trong Hợp đồng nhóm.
- Gọi SRS và Backlog là “Sổ tay 26 User Stories” nhưng không cảnh báo khác biệt 15/6/5 với SOW 16/7/3.
- README nói bộ tài liệu được tổ chức theo 21 câu hỏi nhưng không chỉ rõ tài liệu nào là nguồn chuẩn cho từng nội dung tích hợp.

### Cần sửa trước khi chốt

1. Xóa mục 11 hoặc bổ sung đúng tệp kế hoạch.
2. Cập nhật mô tả Estimate, Architecture và Process theo nội dung thật.
3. Thêm cột trạng thái tài liệu và phiên bản đường cơ sở.
4. Liệt kê rõ tài liệu nào là nguồn chuẩn cho scope, schedule, cost, process và acceptance.

---

## 5.2. `docs.1/01-project-proposal.md` — 7,5/10

### Điểm tốt

- Đúng vai trò của một đề xuất: vấn đề, cơ hội, phương án thay thế, giá trị, phạm vi, rủi ro và quyết định cần phê duyệt.
- Chủ động ghi rằng chưa có khảo sát định lượng thay vì tạo số liệu.
- Phân biệt đề xuất cấp cao với yêu cầu, kiến trúc và ước lượng chi tiết.
- Phạm vi 11 tuần và nội dung loại trừ tương đối rõ.
- Nhận thức tốt rằng đường dẫn có thời hạn/không có nút tải không phải DRM tuyệt đối.

### Vấn đề

- Trạng thái “Đã chấp thuận” chưa có thông tin người/ngày/bằng chứng phê duyệt.
- Mục “Ý tưởng dự án” tự liên kết trở lại chính `01-project-proposal.md`, nên tên tham chiếu sai bản chất.
- Giá trị dự kiến vẫn chủ yếu định tính; chưa có baseline nhu cầu hoặc chỉ số thành công đo được.
- Định hướng MinIO/Docker Compose chưa đồng bộ với Kiến trúc cloud Vercel–Render–Neon–R2.
- Tham chiếu SOW như nguồn chỉ số nghiệm thu trong khi SOW hiện là tài liệu xung đột nhất.

### Cần sửa trước khi chốt

1. Chuyển trạng thái về Pending Approval nếu chưa có bằng chứng.
2. Sửa hoặc bỏ tham chiếu “Ý tưởng dự án”.
3. Chốt profile triển khai ở mức đề xuất.
4. Chỉ trỏ tới SOW sau khi SOW được tái lập đường cơ sở.

---

## 5.3. `docs.1/02-vision-and-scope.md` — 7,5/10

### Điểm tốt

- Viễn cảnh, định vị, người dùng, As-Is/To-Be và ranh giới sản phẩm được trình bày mạch lạc.
- Phân biệt phạm vi sản phẩm và phạm vi công việc.
- Có phần giả định, phụ thuộc, ràng buộc và kiểm soát thay đổi.
- Loại trừ ứng dụng offline, thương mại hóa, tự động hóa phần cứng và số hóa toàn kho.

### Vấn đề

- NFR dùng các cụm “thời gian phù hợp”, “không tạo cảm giác chờ bất thường”, “trình duyệt phổ biến”, chưa đủ để nghiệm thu.
- Ghi “ghi nhận các thao tác chính” trong phạm vi, trong khi backlog đặt `LDMS-023` ở mức Nên có.
- Sản phẩm bàn giao vẫn ghi Docker Compose, nhưng Kiến trúc chọn cloud cho phiên bản đầu tiên.
- Trạng thái “Đã chấp thuận” chưa có chứng cứ.
- Phụ thuộc vào SOW để xác định deliverable/acceptance, nhưng SOW hiện không cùng đường cơ sở.

### Cần sửa trước khi chốt

1. Chuyển các NFR quan trọng thành tiêu chí đo được hoặc gắn nhãn “mục tiêu cần chốt”.
2. Đồng bộ audit log và quản trị danh mục với ưu tiên backlog.
3. Chốt profile triển khai và cập nhật deliverable.
4. Sửa trạng thái phê duyệt theo bằng chứng thật.

---

## 5.4. `docs.1/03-project-charter.md` — 6,5/10

### Điểm tốt

- Bao phủ mục tiêu, phạm vi, mốc, bên liên quan, RACI, nguồn lực, rủi ro và kiểm soát thay đổi.
- RACI giải thích được Responsible/Accountable/Consulted/Informed bằng tiếng Việt.
- Giới hạn 11 tuần và nhóm 6 sinh viên được nhắc nhất quán trong nội bộ tài liệu.
- Không biến ngân sách chưa được phê duyệt thành cam kết chắc chắn.

### Vấn đề

- Bảng ký ghi “(Đã ký)” nhưng thiếu họ tên thật và ngày ký. Đây là điểm làm giảm độ tin cậy hành chính nghiêm trọng.
- Hai liên kết tài liệu môn học dùng `../../materials/...`, trong khi từ `docs.1` đường đúng phải là `../materials/...` nếu trỏ tới thư mục `materials` ở root.
- Charter nói MinIO/Docker Compose trong khi Architecture nói cloud R2/Render/Neon/Vercel.
- “Đại diện nhóm Sebros” chưa ánh xạ tới người cụ thể, trong khi SOW/Hợp đồng nhóm đang mâu thuẫn về PM.
- RACI cấp cao chưa ánh xạ tới owner của từng deliverable hoặc mốc nghiệm thu.

### Cần sửa trước khi chốt

1. Xóa “Đã ký” giả định hoặc điền đủ bằng chứng ký thật.
2. Sửa hai liên kết nguồn.
3. Gắn tên người vào vai trò điều phối/PM và owner phê duyệt.
4. Đồng bộ công nghệ, ngân sách và SOW.

---

## 5.5. `docs.1/04-software-requirements.md` — 7,5/10

### Điểm tốt

- Có mã yêu cầu ổn định theo nhóm chức năng và phi chức năng.
- Bao phủ xác thực, tài liệu, OCR, hiệu chỉnh, xuất bản, tìm kiếm, đọc, dữ liệu và quyền.
- Có bảng truy vết sang story.
- Phân biệt rõ dữ liệu thử nghiệm và dữ liệu thật.
- Không tuyên bố số hiệu năng chưa đo là kết quả thật.

### Vấn đề

- `YC-PN-04` “phản hồi trong thời gian phù hợp” chưa kiểm thử được.
- `YC-PN-06` “trình duyệt phổ biến” chưa có browser matrix/version.
- `YC-TL-05` Bắt buộc nhưng story quản lý danh mục `LDMS-012` là Nên có.
- `YC-PN-10` yêu cầu truy vết tới mã nguồn, kiểm thử và nghiệm thu, nhưng bảng hiện chỉ truy tới backlog/architecture.
- Quy tắc nghiệp vụ xuất bản chưa định nghĩa rõ metadata tối thiểu, trạng thái hợp lệ, người có quyền phê duyệt và xử lý sửa đổi sau xuất bản.
- Chưa có ID riêng cho các tiêu chí dữ liệu, pháp lý, retention, backup/restore và audit.
- Trạng thái vẫn là “Bản dự thảo để xem xét”, nên không thể dùng như baseline đã phê duyệt.

### Cần sửa trước khi chốt

1. Làm rõ xung đột `YC-TL-05`/`LDMS-012`.
2. Định lượng NFR hoặc ghi rõ phương pháp đo và dataset.
3. Mở rộng ma trận truy vết tới test/evidence.
4. Chốt state machine của tài liệu và quy tắc xuất bản.

---

## 5.6. `docs.1/04-product-backlog.md` — 8,0/10

### Điểm tốt

- Đây là tài liệu ổn định nhất trong bộ hiện tại.
- Có 26 story, vai trò, nhu cầu, kết quả, ưu tiên, cỡ, phụ thuộc, yêu cầu liên quan và AC.
- Phân biệt rõ Bắt buộc/Nên có/Có thể xem xét.
- Tránh khẳng định các chức năng tùy chọn sẽ hoàn thành trong 11 tuần.
- Có DoR/DoD ở mức hợp lý và bảng truy vết.
- Không dùng số liệu hiệu năng/chi phí thiếu nguồn như lời hứa.

### Vấn đề

- Tài liệu mô tả backlog nhưng không có trạng thái hiện tại, owner, tuần bắt đầu, bằng chứng, blocked reason hoặc completion date.
- Danh sách cột không khớp tài liệu Quy trình và Hợp đồng nhóm.
- Một số AC vẫn rộng: “mở được”, “phù hợp”, “ở mức phù hợp”, chưa nêu dữ liệu hoặc lỗi cụ thể.
- Story `LDMS-001` là enabler kỹ thuật, không phải user story theo nghĩa chặt; điều này chấp nhận được nếu phân loại rõ `Enabler`.
- `LDMS-013` gộp kiểm tra điều kiện và hành động xuất bản; nên cân nhắc tách để giảm cỡ/rủi ro.
- `LDMS-015` vừa tìm metadata vừa tìm full text, trong khi tên story chỉ nói full text.
- Chưa có story rõ cho backup/restore, observability tối thiểu, accessibility và kiểm chứng quyền tài liệu.
- Trạng thái là Draft; SOW/Hợp đồng nhóm dùng count và ưu tiên cũ.

### Cần sửa trước khi chốt

1. Chọn một workflow Kanban duy nhất.
2. Thêm bảng trạng thái hoặc trỏ tới board nguồn chuẩn có snapshot/bằng chứng.
3. Gắn mỗi story Done với PR/test/UAT/deployment.
4. Đồng bộ SOW, Team Contract và Estimate về 15/6/5.

---

## 5.7. `docs.1/05-software-architecture.md` — 6,5/10

### Điểm tốt

- Có Context, Container và Deployment bằng PlantUML/SVG.
- Chọn modular monolith phù hợp nhóm nhỏ và thời gian ngắn.
- Nêu rõ tách tệp gốc, tác vụ nền, kiểm tra quyền server-side và giới hạn của việc không có nút tải.
- Có truy vết quyết định kiến trúc tới yêu cầu.
- Nêu hai PoC kỹ thuật cần thực hiện và cách ghi kết quả.

### Vấn đề

- Không có component view, ERD/schema, state/job model, sequence cho OCR/publish, failure modes hoặc threat model.
- Tác vụ nền trên Render được nêu như giải pháp nhưng chưa làm rõ độ bền hàng đợi, retry, timeout, restart và khả năng mất job.
- Sơ đồ container ghi “MinIO hoặc tương đương” trong khi bảng công nghệ ghi Cloudflare R2; nên dùng khái niệm Object Storage và ánh xạ theo môi trường.
- Đường triển khai cloud chưa đồng bộ với Proposal/Charter/Feasibility/SOW/Team Contract.
- Repository còn hỗ trợ local/prod Docker/MinIO và nhiều service giám sát; tài liệu chưa mô tả các profile này.
- Không có ADR hoặc rationale so sánh Render/Neon/R2 với on-premise.
- Backup chỉ để dành cho “tài liệu vận hành sau”, dù dữ liệu/tệp là tài sản trọng yếu.

### Cần sửa trước khi chốt

1. Chốt profile môi trường và cập nhật sơ đồ.
2. Bổ sung data model/state model tối thiểu.
3. Ghi quyết định về background job và recovery.
4. Bổ sung security/threat/backup/observability ở mức đủ nghiệm thu.

---

## 5.8. `docs.1/08-feasibility-study.md` — 6,0/10

### Điểm tốt

- Bao phủ pháp lý, nhu cầu, kinh tế, kỹ thuật, nguồn lực, vận hành, tiến độ và văn hóa.
- Kết luận pháp lý có điều kiện, không coi signed URL là thay thế quyền sử dụng.
- Thừa nhận cần kiểm chứng với người dùng đại diện và tài liệu mẫu.
- Không bịa số chi phí-lợi ích khi thiếu dữ liệu.
- Có bảng rủi ro và khuyến nghị có điều kiện.

### Vấn đề

- “Khả thi trong 11 tuần” chưa được chứng minh bằng tổng effort/capacity vì Estimate chưa hoàn chỉnh.
- Khả thi kinh tế chưa có kịch bản, tổng chi phí sở hữu, đơn vị lợi ích hoặc sensitivity analysis.
- Khả thi nhu cầu chưa có khảo sát/phỏng vấn/baseline; phần lớn là lập luận hợp lý nhưng chưa có bằng chứng thực địa.
- Khả thi pháp lý chưa trích văn bản/ý kiến pháp chế cụ thể; trạng thái Approved vì vậy quá mạnh.
- Công nghệ MinIO/Docker Compose không khớp Architecture cloud.
- Rủi ro chỉ có mức Cao/Trung bình, chưa có xác suất, tác động, owner, trigger, deadline và residual risk.

### Cần sửa trước khi chốt

1. Đổi kết luận thành “khả thi sơ bộ có điều kiện” cho đến khi có Estimate và PoC.
2. Gắn evidence cho từng chiều khả thi.
3. Đồng bộ stack và schedule.
4. Chuyển risk table thành risk register có owner/trạng thái.

---

## 5.9. `docs.1/09-software-process-definition.md` — 6,0/10

### Điểm tốt

- Giải thích rõ vì sao chọn Kanban và không đồng nhất Kanban với thiếu kế hoạch.
- Có vai trò, luồng, input/activity/output, DoR/DoD, kiểm thử và chỉ số cải tiến.
- Nhấn mạnh không chuyển Done theo lịch giả và phải có bằng chứng.
- Quy định secrets qua biến môi trường và nhánh công việc ngắn.

### Vấn đề

- Liên kết `11-project-plan.md` xuất hiện hai lần nhưng tệp không tồn tại.
- Board bốn nhóm cột không khớp board sáu cột của Backlog và năm cột của Team Contract.
- Không đặt WIP limit cụ thể; Team Contract lại đặt 1 card/người.
- Quy định Trunk-Based trái GitFlow trong Team Contract.
- Trạng thái `Done – Tuần X` làm tăng số cột theo thời gian, có thể gây khó thống kê; field `done_week` hoặc view theo tuần sẽ ổn định hơn.
- Chưa nêu rõ CI quality gates, review quorum, severity/exit criteria, incident/hotfix flow và evidence location.
- Phần deployment xem cloud stack là đã thống nhất nhưng chưa có tham chiếu quyết định/PoC.

### Cần sửa trước khi chốt

1. Xóa/sửa liên kết plan.
2. Chọn workflow và branching model duy nhất.
3. Chốt WIP ở cấp team/cột.
4. Bổ sung quality gates và evidence repository.

---

## 5.10. `docs.1/10-project-estimate.md` — 4,5/10

### Điểm tốt

- Phân biệt dữ liệu đo với giả định.
- Không xem 6 sinh viên là 6 FTE.
- Dùng pilot và cập nhật theo dữ liệu thực tế, phù hợp tư duy ước lượng tiến hóa.
- Có capacity giả định 24 giờ nhóm/tuần và dự phòng cho test/review/docs.
- Count 15/6/5 khớp Backlog.

### Vấn đề nghiêm trọng

- Bảng công sức theo hạng mục chỉ có một dòng hướng dẫn “Mã hạng mục…”, chưa có 26 hạng mục và chưa có con số tổng.
- Câu “Tổng công sức… được tạm tính” không đi kèm kết quả tính.
- Không có:
  - tổng giờ phạm vi Bắt buộc;
  - khoảng optimistic/most likely/pessimistic;
  - effort theo vai trò;
  - capacity sau khi trừ lịch học/nghỉ/phụ thuộc;
  - critical chain hoặc Monte Carlo/throughput range;
  - dự phòng tổng;
  - forecast hoàn thành.
- Dữ liệu pilot có nhiều story được ghi 15–30 phút do chia đều một session. Đây không phải đo riêng theo story và có nguy cơ đánh giá thấp mạnh công sức thật.
- Capacity 24 giờ/tuần × 11 tuần = 264 giờ nhóm nhưng không được đối chiếu với demand.
- Chi phí 0 VNĐ trái SOW 77–106 triệu CapEx.
- Stack cloud trái SOW/Charter/Feasibility.
- Trạng thái Draft nhưng được các tài liệu khác dùng làm nguồn chi phí chính.

### Cần sửa trước khi chốt

1. Lập bảng đủ 26 hạng mục; ít nhất phải hoàn chỉnh 15 Bắt buộc.
2. Tính demand, capacity, buffer và forecast có khoảng bất định.
3. Không chia đều session đa-story nếu không có timesheet riêng; gắn độ tin cậy cho dữ liệu.
4. Tách kịch bản môn học 0 VNĐ và kịch bản triển khai thật.
5. Đối chiếu thực tế–ước lượng sau mỗi completion event không trùng.

---

## 5.11. `docs.1/12-statement-of-work.md` — 2,0/10

### Điểm tốt

- Cấu trúc SOW đầy đủ về scope, deliverable, schedule, cost, resources, acceptance, change và signature.
- Có ngưỡng nghiệm thu cụ thể hơn nhiều tài liệu khác.
- Có quy trình Change Request và nguyên tắc đánh giá tác động.

### Vấn đề nghiêm trọng

- Là đường cơ sở cũ 20 tuần, trong khi bộ mới là 11 tuần.
- Count 16/7/3 trái Backlog/Estimate 15/6/5.
- Cam kết 500 cuốn và 2.000 cuốn trái phạm vi tài liệu mẫu.
- Cam kết bookmark/highlight/note/citation trái thứ tự ưu tiên mới.
- Dùng MinIO/Docker on-premise trái Architecture cloud.
- Deliverable 500 cuốn tuần 17 trái milestone 500 cuốn tuần 12.
- CapEx + OpEx có thể tới 136 triệu nhưng ràng buộc dưới 100 triệu.
- Gọi tài liệu là văn bản pháp lý nhưng trạng thái Pending Approval và chữ ký trống.
- Giả định pháp lý về Khoản 1 Điều 25 cần ý kiến pháp chế; không nên ghi như kết luận áp dụng trực tiếp.
- Nêu commit `1d76700e` có tồn tại, nhưng tồn tại commit không chứng minh các bên đã phê duyệt thay đổi hợp đồng.
- Ba fragment mục lục không hợp lệ theo markdownlint.
- PDF có thời gian sửa cũ hơn Markdown hơn bốn giờ; cần tái xuất sau khi chốt để loại trừ bản PDF lệch nguồn.

### Cần sửa trước khi chốt

**Phải viết lại theo đường cơ sở mới, không nên vá cục bộ.** SOW mới cần tối thiểu:

1. 11 tuần và 15 hạng mục Bắt buộc.
2. Bộ tài liệu mẫu, không cam kết 500/2.000 cuốn.
3. Một profile triển khai đã chốt.
4. Ngân sách phù hợp kịch bản môn học hoặc kịch bản thật, không trộn hai loại.
5. Deliverable/acceptance truy vết tới story và evidence.
6. Chữ ký thật hoặc trạng thái Pending Approval.

---

## 5.12. `docs.1/16-team-contract.md` — 3,5/10

### Điểm tốt

- Có mục tiêu nhóm, RACI, WIP, giao tiếp, AI governance, source control, xung đột và kỷ luật.
- WIP 1 card/người là quy tắc cụ thể.
- Yêu cầu human review mã do AI sinh và không commit secrets là phù hợp.
- RACI theo work package có một Accountable cho mỗi gói.

### Vấn đề nghiêm trọng

- Trạng thái Active nhưng sáu chữ ký và ngày ký đều trống.
- Danh sách thành viên ghi Ân Tiến Nguyên An là PM; phần mục tiêu và phân vai ghi Mạch Quốc Tấn là PM.
- Dùng 16 Must-have/tuần 12 theo SOW cũ.
- Quy định GitFlow trái Trunk-Based.
- Tech stack MinIO/Docker ba dịch vụ trái Architecture và thực tế compose production.
- “Không phản hồi = đồng ý” là chính sách nguy hiểm cho thay đổi scope, kiến trúc, bảo mật hoặc chi phí; im lặng không nên được coi là phê duyệt.
- Mục đầu nói sửa đổi cần đồng thuận toàn bộ, mục 10 lại định nghĩa ≥4/6 là đồng thuận.
- DoR quy định S ≤1 ngày, M ≤2 ngày nhưng Backlog chỉ dùng Nhỏ/Vừa/Lớn và Estimate dùng 30/60/90 phút; ba scale không khớp.
- Quy tắc ghi mọi phiên AI không được phản ánh đầy đủ trong Project Log.
- Tám fragment mục lục có lỗi, trong đó năm lỗi thuộc Team Contract.

### Cần sửa trước khi chốt

1. Chốt PM và vai trò từng thành viên.
2. Đồng bộ scope/schedule/process/stack.
3. Chọn một ngưỡng biểu quyết rõ theo loại quyết định.
4. Bỏ “im lặng = đồng ý” cho quyết định quan trọng.
5. Chỉ chuyển Active sau khi ký.

---

## 5.13. `docs.1/17-project-log.md` — 3,0/10

### Điểm tốt

- Bảng ngắn, dễ cập nhật.
- Tổng theo dòng được tính đúng: 37 điểm, 14 giờ 50 phút, 730K token.
- Gắn Story ID và ghi rõ khi thời gian/điểm là giả định.

### Vấn đề nghiêm trọng

- Cộng trùng story làm “Tổng điểm” không thể dùng như completed scope hoặc throughput.
- Không có trạng thái (`In Progress`, `Done`, `Reopened`), evidence hoặc người xác nhận.
- Dòng placeholder vẫn được ghi trong nhật ký “hoàn thành story”.
- Không phân biệt thời gian phát triển, review, test, fix và tài liệu.
- Token dạng `40K`, `140K` không có provider/model ID/session ID/cost/cách đo, nên khó audit.
- Không có start time/end time, cycle time, blocked time hoặc rework.
- Không liên kết commit/PR/test/UAT dù lịch sử Git có dữ liệu tương ứng.
- Không đủ dữ liệu để hỗ trợ cách forecast mà Process/Team Contract tuyên bố.

### Cần sửa trước khi chốt

1. Đổi cấu trúc thành `Effort Log` và `Completion Log` riêng.
2. Mỗi completion event ghi story, ngày Done, owner, reviewer, PR/commit, test evidence, UAT, deployment.
3. Tính unique completed stories và throughput theo tuần.
4. Không suy thời gian story bằng chia đều nếu không có số đo; đánh nhãn confidence thấp và không dùng làm calibration chính.

---

## 6. Kiểm tra kỹ thuật tài liệu

### 6.1. Liên kết hỏng

Kiểm tra đường dẫn tương đối phát hiện 7 lần tham chiếu hỏng:

| Tài liệu | Dòng | Đích hỏng | Hướng sửa |
|---|---:|---|---|
| `03-project-charter.md` | 216 | `../../materials/03_software_project_initiation.md` | Dùng `../materials/03_software_project_initiation.md` nếu đúng tệp nguồn. |
| `03-project-charter.md` | 217 | `../../materials/02_software_project.md` | Dùng `../materials/02_software_project.md` nếu đúng tệp nguồn. |
| `08-feasibility-study.md` | 219 | `../../materials/03_software_project_initiation.md` | Dùng `../materials/03_software_project_initiation.md`. |
| `09-software-process-definition.md` | 177 | `11-project-plan.md` | Bổ sung tài liệu hoặc bỏ tham chiếu. |
| `09-software-process-definition.md` | 188 | `11-project-plan.md` | Bổ sung tài liệu hoặc bỏ tham chiếu. |
| `README.md` | 20 | `./11-project-plan.md` | Bổ sung hoặc xóa dòng. |
| `README.md` | 20 | `./11-project-plan.pdf` | Bổ sung hoặc xóa dòng. |

### 6.2. Markdown lint

Chạy `markdownlint-cli2` mặc định trên 13 tệp cho kết quả **1.171 lỗi**:

| Quy tắc | Số lỗi | Nhận định |
|---|---:|---|
| MD013 — độ dài dòng | 897 | Chủ yếu là style, nhất là bảng dài; có thể cấu hình bỏ cho table/code. |
| MD060 — kiểu/căn bảng | 212 | Nhiều bảng không theo một style thống nhất. |
| MD007 — thụt danh sách | 32 | Cần thống nhất indentation. |
| MD051 — fragment liên kết | 8 | Lỗi chức năng ở mục lục SOW và Team Contract. |
| MD034 — bare URL/email | 12 | Chủ yếu email trong bảng; có thể cấu hình hoặc định dạng lại. |
| MD022 | 4 | Thiếu dòng trống quanh heading. |
| MD012 | 2 | Nhiều dòng trống liên tiếp. |
| MD033 | 2 | HTML `<br>` trong README. |
| MD028 | 1 | Dòng trống trong blockquote của Project Log. |
| MD040 | 1 | Code fence thiếu ngôn ngữ. |

Không nên sửa máy móc toàn bộ 1.171 lỗi trước khi chốt nội dung. Thứ tự hợp lý là:

1. lỗi link/fragment/heading ảnh hưởng điều hướng;
2. thống nhất cấu hình markdownlint phù hợp tài liệu có bảng rộng;
3. chạy formatter/căn bảng sau khi nội dung ổn định.

### 6.3. PDF

- Có đủ 13 PDF tương ứng với 13 Markdown.
- Các PDF trích xuất được số trang, nhưng công cụ `pdftotext` hiện cho text layer tiếng Việt thiếu nhiều ký tự/dấu. Điều này có thể ảnh hưởng tìm kiếm, sao chép và accessibility dù hiển thị trực quan vẫn có thể đúng.
- SOW Markdown có thời gian sửa 14:44 trong khi PDF là 10:29 cùng ngày; cần tái xuất PDF sau khi sửa SOW.
- Các PDF khác phần lớn có timestamp sát nguồn Markdown, nhưng timestamp không thay thế kiểm tra nội dung/hash.
- Chưa thực hiện kiểm tra trực quan từng trang PDF trong lần đánh giá này; do đó chưa kết luận về tràn bảng, ngắt trang, font hoặc kích thước sơ đồ.

Khuyến nghị sau khi sửa Markdown:

1. xuất lại toàn bộ PDF bằng cùng một pipeline;
2. kiểm tra visual regression ít nhất trang đầu, mục lục, bảng rộng, sơ đồ và trang chữ ký;
3. kiểm tra text extraction Unicode;
4. ghi tool/version/CSS trong quy trình phát hành tài liệu.

---

## 7. Khoảng trống hồ sơ cấp bộ

Dù README nói các câu 6, 7, 13–15, 18–21 đã được tích hợp, bộ hiện tại chưa có một ma trận chỉ rõ nội dung đó nằm ở đâu và mức hoàn thành nào. Các khoảng trống đáng chú ý:

- Project Plan chính thức không tồn tại dù được tham chiếu.
- Risk Register có owner, trigger, response status và residual risk chưa tồn tại.
- Quality Plan/quality gates chưa đầy đủ.
- Test Plan/UAT plan và bằng chứng nghiệm thu chưa tồn tại trong `docs.1`.
- CI/CD/DevOps chỉ được nhắc rải rác; chưa có tài liệu hoặc ma trận truy vết đến workflow thật.
- PoC results chưa có bằng chứng, chỉ mới có kế hoạch kiểm chứng.
- Lessons Learned chưa có artifact riêng hoặc mục rõ ràng.
- Decision Log/ADR chưa có.
- Change Request log chưa có dù SOW định nghĩa quy trình CR.
- Data retention, backup/restore, incident response và security review chưa đủ để gọi là sẵn sàng vận hành.

Không bắt buộc phải tạo thêm chín tài liệu riêng. Có thể giải quyết bằng một **Coverage Matrix 21 câu hỏi** trong README, trỏ tới section và evidence cụ thể, đồng thời ghi `Draft/Ready/Verified/Not Available`.

---

## 8. Đường cơ sở đề xuất để ổn định bộ tài liệu

Dựa trên số lượng tài liệu, ngày cập nhật và mức độ nhất quán nội bộ, đường cơ sở hợp lý nhất hiện nay là:

| Thuộc tính | Đường cơ sở đề xuất |
|---|---|
| Loại dự án | Phiên bản môn học / MVP trình diễn có kiểm soát |
| Thời gian | 11 tuần |
| Nhân sự | 6 sinh viên, kiêm nhiệm |
| Phương pháp | Kanban, WIP được chốt rõ |
| Phạm vi | 15 Bắt buộc; 6 Nên có; 5 Có thể xem xét |
| Dữ liệu | Bộ tài liệu mẫu đã xác nhận quyền, không cam kết 500/2.000 cuốn |
| Ngân sách | Kịch bản môn học: giả định 0 VNĐ tiền mặt, theo dõi effort; kịch bản mở rộng tách riêng |
| Local | Docker Compose + PostgreSQL + MinIO |
| Demo cloud | Vercel + Render + Neon + Cloudflare R2, chỉ khi đã kiểm chứng |
| Branching | Trunk-Based với nhánh task ngắn, nếu phù hợp thực tế Git |
| Nghiệm thu | Story AC + test evidence + review + UAT/đại diện nghiệp vụ |
| Trạng thái | Draft/Pending Approval cho đến khi có người và ngày phê duyệt thật |

Đây là **suy luận từ trạng thái repository**, không phải quyết định đã được các bên ký. Nếu nhóm muốn giữ SOW 20 tuần và ngân sách thật, phải làm hướng ngược lại: cập nhật toàn bộ chín tài liệu mới về chương trình 20 tuần và chứng minh nguồn lực/chi phí/sản lượng. Không nên pha hai đường cơ sở.

---

## 9. Kế hoạch sửa theo ưu tiên

### P0 — Phải sửa trước mọi hoạt động ký/nộp

1. Quyết định một đường cơ sở: 11 tuần hoặc 20 tuần.
2. Viết lại SOW theo đường cơ sở đã chọn.
3. Đồng bộ Team Contract về scope, schedule, PM, branching, WIP và chữ ký.
4. Hoàn thiện Estimate bằng số giờ/khoảng dự báo thực, không để bảng mẫu.
5. Sửa trạng thái Approved/Active/Đã ký theo bằng chứng thật.
6. Chốt stack theo môi trường local/demo/production.

### P1 — Cần sửa để bộ hồ sơ có thể kiểm chứng

1. Chuẩn hóa count 15/6/5 trong mọi tài liệu.
2. Chuẩn hóa Kanban columns và DoR/DoD.
3. Tách Effort Log và Completion Log, gắn PR/test/UAT.
4. Sửa 7 liên kết file hỏng và 8 fragment mục lục.
5. Giải quyết `YC-TL-05` so với `LDMS-012`.
6. Tạo coverage matrix cho 21 câu hỏi.
7. Thêm risk register và evidence index.

### P2 — Nâng chất lượng trước khi phát hành cuối

1. Định lượng NFR hoặc ghi rõ phương pháp đo.
2. Bổ sung architecture data/state/sequence/security views.
3. Chuẩn hóa Markdown bằng cấu hình lint của dự án.
4. Xuất lại toàn bộ PDF và kiểm tra visual/text extraction.
5. Đồng bộ thuật ngữ Việt–Anh, cách viết DevOps, SOW/SoW, metadata/siêu dữ liệu.

---

## 10. Checklist điều kiện để nâng lên mức 8/10

Bộ tài liệu có thể được xem là ổn định ở mức khoảng 8/10 khi tất cả điều kiện sau đạt:

- [ ] Chỉ còn một schedule baseline.
- [ ] Chỉ còn một scope count và MoSCoW mapping.
- [ ] SOW, Charter, Backlog, Estimate và Team Contract không mâu thuẫn.
- [ ] PM, nghiệp vụ, reviewer và approver có người cụ thể.
- [ ] Không có trạng thái “Đã ký/Approved/Active” thiếu bằng chứng.
- [ ] Estimate có tổng effort, capacity, buffer và forecast range.
- [ ] Project Log không cộng trùng completion và có evidence.
- [ ] Architecture phân biệt local/demo/production.
- [ ] Process và Team Contract dùng cùng board/branching/WIP.
- [ ] Không còn liên kết file/fragment hỏng.
- [ ] NFR trọng yếu có cách đo và dữ liệu thử.
- [ ] SOW acceptance truy vết tới story, test và deliverable.
- [ ] PDF được tái xuất từ Markdown đã chốt và kiểm tra trực quan.
- [ ] README phản ánh đúng danh sách tài liệu thực tế.

---

## 11. Kết luận cuối cùng

Kết quả ban đầu là **5,6/10** vì hai thế hệ tài liệu cùng tồn tại và bốn tài liệu P0 chưa đáng tin cậy. Sau khi tái lập các tài liệu P0, đồng bộ phần còn lại, bổ sung đủ hồ sơ cần thiết theo 21 câu hỏi và kiểm chứng lại Markdown/PDF, điểm hiện hành là **8,8/10**.

Bộ `docs.1` hiện **đủ ổn định để nhóm dùng làm đường cơ sở rà soát nội bộ và chuẩn bị nộp**. Bộ tài liệu chưa được gọi là Approved, nghiệm thu hay production-ready cho tới khi có chữ ký, PoC, test/UAT và evidence thật. Cách ghi nhận này bảo toàn tính phản biện: chất lượng hồ sơ đã được nâng rõ rệt nhưng không biến công việc chưa thực hiện thành thành tích đã hoàn thành.
