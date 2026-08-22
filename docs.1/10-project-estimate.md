# ƯỚC LƯỢNG DỰ ÁN

## Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS (HCMUS-LDMS)

### Thông tin tài liệu

| Trường thông tin | Nội dung |
|---|---|
| Mã tài liệu | `HCMUS-LDMS-EST` |
| Tên tài liệu | Ước lượng dự án |
| Người phụ trách | Mạch Quốc Tấn |
| Người xem xét | Đại diện nhóm Sebros và Đại diện nghiệp vụ Thư viện |
| Trạng thái | Bản dự thảo để hiệu chỉnh bằng dữ liệu thực tế |
| Phạm vi | MVP 11 tuần; 15 hạng mục Bắt buộc |

### Lịch sử phiên bản

| Phiên bản | Ngày | Mô tả thay đổi | Người thực hiện |
|---:|:---:|---|---|
| 1.0 | 21/08/2026 | Xây dựng phương pháp dựa trên pilot và cỡ tương đối. | Mạch Quốc Tấn |
| 2.0 | 22/08/2026 | Hoàn chỉnh demand/capacity/forecast, tách dữ liệu đo khỏi giả định, đồng bộ 15/6/5 và ngân sách MVP. | Mạch Quốc Tấn |

## Mục lục

- [1. Mục đích và nguyên tắc](#1-mục-đích-và-nguyên-tắc)
- [2. Đường cơ sở và giả định](#2-đường-cơ-sở-và-giả-định)
- [3. Chất lượng dữ liệu đầu vào](#3-chất-lượng-dữ-liệu-đầu-vào)
- [4. Phương pháp ước lượng](#4-phương-pháp-ước-lượng)
- [5. Ước lượng 15 hạng mục Bắt buộc](#5-ước-lượng-15-hạng-mục-bắt-buộc)
- [6. Demand, capacity và forecast](#6-demand-capacity-và-forecast)
- [7. Mốc điều phối](#7-mốc-điều-phối)
- [8. Nguồn lực và chi phí](#8-nguồn-lực-và-chi-phí)
- [9. Cách cập nhật và kiểm soát sai lệch](#9-cách-cập-nhật-và-kiểm-soát-sai-lệch)
- [10. Kết luận ước lượng](#10-kết-luận-ước-lượng)
- [11. Tài liệu tham chiếu](#11-tài-liệu-tham-chiếu)

---

## 1. Mục đích và nguyên tắc

Tài liệu ước lượng demand, capacity và mức độ khả thi của MVP HCMUS-LDMS trong 11 tuần. Kết quả là forecast có bất định, không phải cam kết chắc chắn cho từng story.

Nguyên tắc:

- tách số liệu thực tế khỏi giả định;
- effort của story bao gồm phát triển, test, review, sửa lỗi và tài liệu để đạt DoD;
- không chia đều thời gian của một session đa-story rồi coi là số đo riêng đáng tin cậy;
- không dùng token AI hoặc số commit để thay cho effort/hoàn thành;
- cập nhật forecast khi có ít nhất ba completion event đủ evidence;
- ưu tiên 15 hạng mục Bắt buộc; optional không được dùng hết buffer.

## 2. Đường cơ sở và giả định

### 2.1. Phạm vi

| Mức độ | Số hạng mục | Tổng điểm tương đối | Cam kết |
|---|---:|---:|---|
| Bắt buộc | 15 | 26 | Phạm vi cơ sở cần forecast. |
| Nên có | 6 | 9 | Chỉ kéo khi baseline ổn định và còn buffer. |
| Có thể xem xét | 5 | 8 | Ngoài cam kết cơ sở. |
| Tổng | 26 | 43 | Không phải toàn bộ đều phải hoàn thành trong 11 tuần. |

Quy ước điểm: Nhỏ = 1, Vừa = 2, Lớn = 3. Điểm dùng để so sánh tương đối, không quy đổi trực tiếp thành giờ.

### 2.2. Cỡ effort dùng cho forecast ban đầu

| Cỡ | Khoảng effort hoàn chỉnh | Giá trị kế hoạch |
|---|---:|---:|
| Nhỏ | 4–8 giờ-người | 6 giờ-người |
| Vừa | 8–16 giờ-người | 12 giờ-người |
| Lớn | 16–32 giờ-người | Phải phân rã hoặc PoC; không có trong baseline hiện tại |

Giá trị kế hoạch đã bao gồm công việc để đạt DoD. Khoảng dưới/trên được dùng cho sensitivity analysis.

### 2.3. Capacity

- 6 thành viên.
- 4 giờ/người/tuần là giả định năng lực dành riêng cho dự án.
- Gross capacity: 6 × 4 × 11 = **264 giờ-người**.
- Focus factor kế hoạch: 75% sau lịch học, phối hợp và gián đoạn.
- Usable capacity: 264 × 75% = **198 giờ-người**.
- Không cộng công sức đại diện nghiệp vụ vào capacity phát triển; thời gian chờ phản hồi được theo dõi là blocked time.

## 3. Chất lượng dữ liệu đầu vào

Nhật ký hiện có các session đa-story với tổng thời gian 14 giờ 50 phút và 730K token. Các dòng này được giữ như **effort log lịch sử**, nhưng chưa đủ để hiệu chỉnh cỡ story vì:

- một story xuất hiện ở nhiều session;
- nhiều session chia đều tổng thời gian cho nhiều mã;
- chưa có liên kết đầy đủ tới PR/test/UAT cho từng completion event;
- một số mô tả là placeholder hoặc phạm vi một phần;
- thời gian 15–30 phút/story không thể hiện đầy đủ test, review, tích hợp và tài liệu.

Do đó:

| Dữ liệu | Cách sử dụng |
|---|---|
| Tổng effort từng session | Dùng tham khảo hoạt động đã ghi. |
| Thời gian chia đều theo story | Confidence thấp; không dùng làm baseline chính. |
| Story có PR + test + review + Done date | Dùng hiệu chỉnh sau khi xác minh. |
| Token AI | Không dùng ước lượng năng suất. |

Forecast 2.0 sử dụng dải planning 4–8/8–16 giờ cho đến khi completion log có đủ bằng chứng.

## 4. Phương pháp ước lượng

### 4.1. Bottom-up theo story

1. Xác định cỡ, phụ thuộc và AC của từng story.
2. Chọn khoảng effort theo cỡ.
3. Điều chỉnh hệ số rủi ro theo phụ thuộc/không chắc chắn.
4. Cộng demand theo chuỗi phụ thuộc và module.
5. So sánh với usable capacity.
6. Theo dõi actual effort, cycle time, blocked time và rework.

### 4.2. Hệ số rủi ro

| Mức | Hệ số | Điều kiện |
|---|---:|---|
| Thấp | 1,00 | Phạm vi rõ, có mẫu tương tự, ít tích hợp. |
| Trung bình | 1,15 | Có tích hợp hoặc cần kiểm chứng đáng kể. |
| Cao | 1,30 | Chuỗi xử lý, bảo mật, job nền hoặc công nghệ chưa ổn định. |

Giá trị kế hoạch trong bảng Mục 5 đã áp dụng hệ số bằng cách làm tròn đến 0,5 giờ.

### 4.3. Forecast theo throughput

Khi có ít nhất ba tuần dữ liệu đáng tin cậy, nhóm dùng song song:

- số story Done/tuần;
- điểm Done/tuần;
- cycle-time percentile;
- remaining effort.

Forecast phải trình bày dạng khoảng và nêu dữ liệu đầu vào. Không dùng một tuần có nhiều story nhỏ để suy ra toàn bộ dự án.

## 5. Ước lượng 15 hạng mục Bắt buộc

| Story | Cỡ | Effort cơ sở | Rủi ro | Kế hoạch | Lý do chính |
|---|:---:|---:|:---:|---:|---|
| LDMS-001 | Vừa | 12,0 | Thấp | 12,0 | Môi trường, cấu trúc, hướng dẫn và smoke check. |
| LDMS-009 | Nhỏ | 6,0 | Trung bình | 7,0 | Phiên, lỗi đăng nhập và test auth. |
| LDMS-010 | Vừa | 12,0 | Cao | 15,5 | RBAC server-side, role matrix và negative tests. |
| LDMS-002 | Vừa | 12,0 | Cao | 15,5 | File validation, storage, quyền và bảo toàn source. |
| LDMS-003 | Vừa | 12,0 | Cao | 15,5 | Job OCR, trạng thái, failure/restart behavior. |
| LDMS-004 | Vừa | 12,0 | Trung bình | 14,0 | Page mapping, source preview và error states. |
| LDMS-005 | Vừa | 12,0 | Trung bình | 14,0 | Lưu/reload text, concurrency/error handling. |
| LDMS-026 | Nhỏ | 6,0 | Trung bình | 7,0 | List/filter/status và permission filtering. |
| LDMS-011 | Vừa | 12,0 | Trung bình | 14,0 | Metadata validation và integration. |
| LDMS-007 | Vừa | 12,0 | Cao | 15,5 | EPUB generation, validation và job failure. |
| LDMS-013 | Nhỏ | 6,0 | Trung bình | 7,0 | Publish gate, reason list và authorization. |
| LDMS-015 | Vừa | 12,0 | Cao | 15,5 | FTS/index, permission filtering và test dataset. |
| LDMS-016 | Nhỏ | 6,0 | Trung bình | 7,0 | Result content, link và empty/error state. |
| LDMS-008 | Vừa | 12,0 | Cao | 15,5 | Epub.js integration, navigation và responsive behavior. |
| LDMS-014 | Vừa | 12,0 | Cao | 15,5 | Read authorization, private object access và negative tests. |
| **Tổng** |  | **156,0** |  | **190,0** | Tổng kế hoạch đã gồm điều chỉnh rủi ro. |

Tổng lower/upper thô theo dải cỡ trước hệ số là **104–208 giờ-người**. Sau rủi ro, khoảng có thể rộng hơn; vì vậy con số 190 giờ là kế hoạch trung tâm, không phải giới hạn trên.

## 6. Demand, capacity và forecast

### 6.1. So sánh

| Chỉ số | Giá trị |
|---|---:|
| Gross capacity 11 tuần | 264 giờ-người |
| Usable capacity ở focus factor 75% | 198 giờ-người |
| Demand kế hoạch 15 Bắt buộc | 190 giờ-người |
| Buffer còn lại | 8 giờ-người |
| Mức sử dụng usable capacity | 96,0% |

### 6.2. Nhận định

Baseline **có thể hoàn thành nhưng rủi ro cao**, vì buffer chỉ khoảng 8 giờ-người. Một lỗi tích hợp hoặc chậm phản hồi nghiệp vụ có thể làm forecast vượt tuần 11.

Các điều kiện để giữ forecast:

- không kéo hạng mục Nên có/Có thể xem xét khi baseline chưa đạt ít nhất 80% và remaining forecast còn buffer;
- giảm blocked time bằng việc chốt dữ liệu, quyền và reviewer trước khi kéo story;
- tách story nếu remaining estimate vượt 16 giờ-người;
- theo dõi actual effort thay vì số giờ chia đều;
- nếu forecast P85 vượt tuần 11, lập CR giảm scope hoặc tăng capacity; không tự hạ DoD.

### 6.3. Kịch bản

| Kịch bản | Focus factor | Capacity sử dụng | Kết quả so với demand 190 giờ |
|---|---:|---:|---|
| Bất lợi | 60% | 158,4 | Thiếu 31,6 giờ; cần giảm scope/tăng capacity. |
| Kế hoạch | 75% | 198,0 | Dư 8,0 giờ; rủi ro cao. |
| Thuận lợi | 85% | 224,4 | Dư 34,4 giờ; có buffer sửa lỗi, chưa tự động cấp cho optional. |

## 7. Mốc điều phối

| Tuần | Nhóm story trọng tâm | Cumulative planned effort | Kết quả cần kiểm tra |
|---|---|---:|---|
| 1 | LDMS-001 | 12,0 | Local baseline và hướng dẫn. |
| 2–3 | LDMS-009, 010, 002, 026 | 57,0 | Auth/RBAC/upload/list đúng quyền. |
| 4–6 | LDMS-003, 004, 005 | 101,0 | OCR đến saved correction. |
| 7–8 | LDMS-011, 007, 013 | 137,5 | Metadata/EPUB/publish gate. |
| 9–10 | LDMS-015, 016, 008, 014 | 190,0 | Search/read/private access. |
| 11 | Hồi quy/bàn giao | Dùng buffer và phần effort đã phân bổ trong DoD | Evidence, lỗi còn lại và handover. |

Effort không phải lịch tuần cứng. Story chỉ chuyển trạng thái theo Kanban; bảng dùng để phát hiện lệch forecast.

## 8. Nguồn lực và chi phí

### 8.1. Nguồn lực

| Nguồn lực | Số lượng | Ghi chú |
|---|---:|---|
| Sinh viên | 6 | Kiêm nhiệm; capacity phải cập nhật theo lịch thật. |
| Đại diện nghiệp vụ | 1 đầu mối khi được chỉ định | Không tính vào giờ phát triển. |
| Local stack | Docker/PostgreSQL/MinIO | Dùng cho phát triển/test. |
| Demo cloud | Vercel/Render/Neon/R2 | Chỉ dùng khi cấu hình và kiểm chứng đạt. |

### 8.2. Chi phí

Baseline MVP môn học dùng giả định **0 VNĐ tiền mặt được phê duyệt**:

| Nhóm | Giá trị baseline | Cách theo dõi |
|---|---:|---|
| Nhân công sinh viên | 0 VNĐ tiền mặt | 190 giờ-người kế hoạch; actual theo effort log. |
| Local/demo service | 0 VNĐ nếu dùng gói sẵn có | Ghi phí thật nếu phát sinh. |
| AI tools | Chưa có hạn mức được phê duyệt | Chỉ ghi chi phí có số đo/chứng từ. |
| Thiết bị/số hóa/production | Ngoài phạm vi | SOW riêng nếu mở rộng. |

Không dùng 0 VNĐ để kết luận chi phí kinh tế của sản phẩm bằng 0. Một dự án triển khai thật phải định giá nhân công, hạ tầng, số hóa, pháp lý, bảo trì và dự phòng.

## 9. Cách cập nhật và kiểm soát sai lệch

Mỗi completion event cần:

- Story ID;
- start/done date;
- actual effort;
- blocked time và rework;
- commit/PR;
- test evidence;
- reviewer/người xác nhận;
- remaining estimate của chuỗi phụ thuộc.

### Ngưỡng hành động

| Trigger | Hành động |
|---|---|
| Actual > 150% kế hoạch story | Phân tích nguyên nhân và cập nhật story tương tự. |
| Blocked > 2 ngày lịch | PM ưu tiên gỡ phụ thuộc hoặc đổi thứ tự kéo việc. |
| Usable capacity dự báo < 190 giờ | Lập CR về scope/capacity trước khi hạ chất lượng. |
| Baseline chưa đạt 80% | Không kéo optional. |
| Forecast vượt tuần 11 | Báo trạng thái, phương án giảm scope/tăng capacity và quyết định có thẩm quyền. |

## 10. Kết luận ước lượng

- Demand kế hoạch: **190 giờ-người** cho 15 hạng mục Bắt buộc.
- Usable capacity kế hoạch: **198 giờ-người**.
- Buffer: **8 giờ-người**, mức rủi ro cao.
- Phạm vi 11 tuần chỉ khả thi có điều kiện; không đủ cơ sở cam kết optional.
- Dữ liệu session cũ chưa đủ chất lượng để giảm mạnh estimate.
- Forecast phải cập nhật bằng completion event có evidence.

## 11. Tài liệu tham chiếu

- [Đề xuất dự án](01-project-proposal.md)
- [Viễn cảnh và phạm vi](02-vision-and-scope.md)
- [Ủy nhiệm dự án](03-project-charter.md)
- [Yêu cầu phần mềm](04-software-requirements.md)
- [Danh mục công việc](04-product-backlog.md)
- [Kiến trúc phần mềm](05-software-architecture.md)
- [Định nghĩa quy trình](09-software-process-definition.md)
- [Bản mô tả công việc](12-statement-of-work.md)
- [Nhật ký dự án](17-project-log.md)
