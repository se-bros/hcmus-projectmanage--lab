# BÁO CÁO PHẢN BIỆN & ĐÁNH GIÁ

## Ý tưởng Dự án Số hóa & Quản lý Khóa luận Tốt nghiệp

### Digital Repository for Undergraduate Theses — Evaluation Report

**Trường Đại học Khoa học Tự nhiên, ĐHQG-HCM (HCMUS)**
**Thư viện & Phòng Công nghệ Thông tin**

Phiên bản 2.0 • Tháng 7/2026 • Đánh giá dựa trên **Bộ 6 tài liệu Project Initiation v1.0** (`project-initiation/01-project-idea.md` → `06-architecture.md`)

_Tài liệu nội bộ — dùng để hỗ trợ ra quyết định phê duyệt_

---

## 0. Giới thiệu & Phạm vi báo cáo

Báo cáo này tổng hợp kết quả phản biện và chấm điểm độc lập đối với ý tưởng dự án "Số hóa & Quản lý Khóa luận Tốt nghiệp" của HCMUS. Khác với phiên bản trước (đánh giá một Business Case đơn file), báo cáo này đánh giá **bộ 6 tài liệu Khởi tạo Dự án** được viết theo khung `project-initiation-writer` (Project Idea → Project Proposal → Vision & Scope → Feasibility Study → Project Charter → Architecture). Mục tiêu là cung cấp cơ sở khách quan, có phương pháp, để hỗ trợ Ban Giám hiệu và các bên liên quan ra quyết định phê duyệt.

Báo cáo áp dụng 8 nhóm khung tiêu chí được tổng hợp từ các chuẩn quốc tế và nghiên cứu học thuật về đánh giá dự án phần mềm: tam giác sắt mở rộng (Chow & Cao), chất lượng sản phẩm (ISO/IEC 25010), yếu tố quyết định thành công (Pinto & Slevin; Standish Group CHAOS), khả thi (TELOS), giá trị dài hạn (Atkinson; PMI Benefits Realization), tiêu chí lựa chọn đầu tư (Weighted Scoring Model), chỉ số kỹ thuật/vận hành (DORA), và tiêu chí hậu triển khai (Post-Implementation Review).

### Điểm khác biệt so với đánh giá trước (Business Case đơn file)

Việc tách nội dung thành 6 tài liệu tự-đủ-nghĩa theo đúng khung lý thuyết Software Project Initiation làm rõ ràng hơn một số điểm mà bản Business Case gộp chung trước đây chỉ nêu sơ lược: phân loại Sponsor/Client/Customer/User tách bạch (`02-project-proposal.md`), Feature Model chính thức thay vì danh sách tính năng phẳng (`03-vision-and-scope.md`), Stakeholder Register + Power/Interest Grid + RACI Matrix đầy đủ (`05-project-charter.md`), và tách bạch rõ Cost vs Budget (`04-feasibility-study.md`). Đây là lý do một số tiêu chí về **cấu trúc/tính rõ ràng của kế hoạch** được chấm cao hơn so với bản trước. Tuy nhiên, các tiêu chí phụ thuộc **hành động thực tế ngoài tài liệu** (khảo sát người dùng thật, ký duyệt quy trình pháp lý, báo giá thật, cam kết nhân sự) về bản chất **chưa thay đổi** — cấu trúc tài liệu tốt hơn không tự động lấp được các khoảng trống này.

### Phương pháp chấm điểm

Vì dự án đang ở giai đoạn Khởi tạo (chưa triển khai), báo cáo **KHÔNG** chấm điểm kết quả thực tế cho các tiêu chí đo lường sản phẩm/vận hành đã hoàn thành — những tiêu chí này được đánh dấu N/A. Với các tiêu chí còn lại, điểm số phản ánh mức độ bộ tài liệu hiện tại đáp ứng được tiêu chí đó, theo thang sau:

| Khoảng điểm | Ý nghĩa |
| --- | --- |
| 9 – 10 | Đáp ứng đầy đủ, có bằng chứng cụ thể |
| 7 – 8 | Đáp ứng khá tốt, còn thiếu chi tiết nhỏ |
| 5 – 6 | Đáp ứng một phần — có đề cập/kế hoạch nhưng thiếu số liệu hoặc xác nhận |
| 3 – 4 | Yếu — rủi ro hiện hữu, chưa có giải pháp rõ ràng |
| 1 – 2 | Không đáp ứng / thông tin trống |
| N/A | Chưa thể đánh giá vì dự án chưa triển khai |

---

## I. Tam giác sắt mở rộng (Quản lý dự án)

_Nguồn tham chiếu: Chow & Cao; Stankovic và cộng sự — mở rộng tam giác Thời gian–Chi phí–Phạm vi bằng Chất lượng, Sự hài lòng khách hàng và Mục tiêu kinh doanh._

| Tiêu chí | Điểm | Phản biện |
| --- | --- | --- |
| Thời gian | 8/10 | `05-project-charter.md` mục Roadmap nay có milestone rõ (M1–M3), đường găng xác định (WP4 số hóa) và bảng thời lượng từng gói. Trừ điểm: vẫn chưa có buffer rủi ro nhân sự kiêm nhiệm cho WP1–3. |
| Chi phí | 6/10 | `04-feasibility-study.md` tách rõ Cost (bottom-up theo WBS) và Budget (Cost + dự phòng 15%) — rõ ràng hơn bản trước. Nhưng toàn bộ vẫn là ước lượng minh họa, biên độ dao động gần gấp đôi, chưa có báo giá thực tế. |
| Phạm vi | 9/10 | `03-vision-and-scope.md` có Project Scope Statement đầy đủ (Deliverables/Exclusions/Constraints/Acceptance Criteria/Assumptions), rõ ràng hơn mục "Out of scope" đơn giản trước đây. Trừ nhẹ: tiêu chí chọn khoa thí điểm vẫn chưa nêu. |
| Chất lượng | 6/10 | Feature Model làm rõ ranh giới MVP, nhưng vẫn chưa có ngưỡng chất lượng cụ thể (vd % độ chính xác OCR chấp nhận được) dù đã xác định đây là hạng mục cần PoC. |
| Sự hài lòng khách hàng | 5/10 | KPI khảo sát hài lòng vẫn còn đó, nhưng điểm cộng thực sự là tài liệu mới **không còn giả vờ có "tiếng nói người dùng"** qua persona minh họa — Mục Customer Discovery ở `02-project-proposal.md` thẳng thắn ghi nhận "chưa có khảo sát/phỏng vấn người dùng thật nào". Trung thực hơn nhưng chưa giải quyết được gốc rễ. |
| Mục tiêu kinh doanh | 7/10 | Phù hợp rõ với định hướng chuyển đổi số của ĐHQG-HCM. `04-feasibility-study.md` mục ROI nay giải thích rõ vì sao không quy đổi ROI tài chính thuần túy và đề xuất mô hình cost-avoidance — lập luận chặt hơn nhưng số liệu vẫn thiếu. |

## II. Chất lượng sản phẩm phần mềm (ISO/IEC 25010)

_Chấm theo định hướng kiến trúc mô tả tại `06-architecture.md` (chưa có sản phẩm thực để đo lường trực tiếp)._

| Tiêu chí | Điểm | Phản biện |
| --- | --- | --- |
| Functional suitability | 7/10 | Feature Model chính thức (And/Alternative/Or/Mandatory-Optional) tại `03-vision-and-scope.md` truy vết được từng feature về đúng 1 user/business goal — rõ ràng hơn danh sách tính năng phẳng trước đây. |
| Performance efficiency | 4/10 | Vẫn không có yêu cầu phi chức năng cụ thể (SLA, thời gian phản hồi tìm kiếm, số người dùng đồng thời) ở bất kỳ tài liệu nào trong bộ 6 file. |
| Compatibility | 7/10 | Context Diagram (`02-project-proposal.md`) và Tech Stack (`06-architecture.md`) nay nêu rõ các điểm tích hợp (SSO/LDAP, hệ thống quản lý đào tạo) nhưng vẫn đánh dấu `[Cần xác nhận]` — chưa xác nhận tương thích thực tế. |
| Usability | 6/10 | `03-vision-and-scope.md` mục Mockup/Prototype nay chỉ đích danh luồng rủi ro cao nhất cần mockup trước khi code (nộp–duyệt–xuất bản) thay vì chỉ nói chung chung "UAT". |
| Reliability | 5/10 | Vẫn không có SLA uptime hay kế hoạch khôi phục thảm họa (DR) cụ thể, dù `06-architecture.md` đã nêu backup định kỳ ở tầng lưu trữ. |
| Security | 6/10 | Rủi ro dữ liệu cá nhân vẫn được xử lý chung chung ("rà soát/ẩn thông tin nhạy cảm") tại `04-feasibility-study.md` — không có thay đổi thực chất so với bản trước. |
| Maintainability | 8/10 | `06-architecture.md` biện luận rõ ràng hơn: chọn modular monolith trên nền tảng mã nguồn mở thay vì microservices, có lập luận tường minh theo từng tiêu chí (scale/bảo trì/tích hợp) — chặt chẽ hơn bản trước. |
| Portability | 7/10 | Không vendor lock-in nặng, giữ nguyên đánh giá. |

## III. Yếu tố Quyết định Thành công (Critical Success Factors)

_Nguồn tham chiếu: mô hình 10 yếu tố của Pinto & Slevin; các yếu tố thành công theo báo cáo CHAOS của Standish Group._

| Tiêu chí | Điểm | Phản biện |
| --- | --- | --- |
| Sứ mệnh dự án | 8/10 | Rõ ràng ngay từ `01-project-idea.md` và nhất quán xuyên suốt 6 tài liệu. |
| Hỗ trợ quản lý cấp cao | 4/10 | Ban Giám hiệu được phân tích rõ hơn trong Power/Interest Grid (`05-project-charter.md`, nhóm "Giữ hài lòng") nhưng mục Chữ ký (Signatures) vẫn để trống — chưa có phê duyệt/cam kết thực tế. |
| Lịch trình / kế hoạch | 8/10 | Roadmap + Milestones + Critical Path được hình thức hóa rõ ràng trong Project Charter, khá hơn bản WBS/Timeline rời rạc trước đây. |
| **Tham vấn người dùng** | **3/10** | Vẫn là điểm yếu nhất của toàn bộ hồ sơ. `02-project-proposal.md` mục Customer Discovery nay minh bạch ghi nhận việc chưa khảo sát người dùng thật (khuyến nghị 15–20 phỏng vấn) — cải thiện về tính trung thực, nhưng theo CHAOS Report đây vẫn là yếu tố quan trọng nhất cho thành công dự án CNTT và **chưa được lấp**. |
| Nhân sự | 5/10 | Giả định dùng nội lực CNTT (3–4 người × 3 tháng) vẫn chưa có xác nhận năng lực/thời gian rảnh thực tế, dù `05-project-charter.md` đã liệt kê rõ trong mục Cơ sở Vật chất & Nguồn lực. |
| Giám sát & phản hồi | 7/10 | Mục Quy tắc Làm việc (`05-project-charter.md`) nay quy định rõ nhịp báo cáo (sprint review 2 tuần, báo cáo tuần, báo cáo cuối giai đoạn) — cụ thể hơn bản trước. |
| Giao tiếp | 7/10 | Engagement Strategy đầy đủ theo từng nhóm Power/Interest (`05-project-charter.md`) — khắc phục rõ điểm yếu "thiếu kế hoạch truyền thông chi tiết" của bản trước. |
| Xử lý sự cố | 5/10 | Bảng rủi ro nay tách rõ kỹ thuật vs vận hành/dự án (`04-feasibility-study.md`), nhưng vẫn chưa gán chủ sở hữu rủi ro (risk owner) cụ thể cho từng mục. |

## IV. Khả thi trước triển khai (TELOS)

| Tiêu chí | Điểm | Phản biện |
| --- | --- | --- |
| Kỹ thuật | 8/10 | `06-architecture.md` biện luận kỹ hơn cho lựa chọn nền tảng mã nguồn mở + modular monolith — rủi ro kỹ thuật thấp và có cơ sở lập luận rõ ràng. |
| Kinh tế | 4/10 | Chưa có báo giá thực tế; biên độ chi phí quá rộng để dùng phê duyệt ngân sách chính thức — không đổi so với bản trước dù cách trình bày Cost/Budget mạch lạc hơn. |
| **Pháp lý** | **4/10** | Vẫn là rủi ro nghiêm trọng của toàn bộ đánh giá, nhưng nay đã được nâng cấp từ "rủi ro chưa xử lý" thành **điều kiện gate tường minh của Giai đoạn 0** trong Roadmap (`05-project-charter.md`, milestone M1: "quy trình consent được ký duyệt"). Có kế hoạch giải quyết cụ thể hơn, nhưng quy trình đồng ý công khai (consent) của sinh viên **vẫn chưa được thiết kế/ký duyệt tại thời điểm đánh giá** — đây vẫn là loại rủi ro có thể chặn đứng việc đăng tải khóa luận. |
| Vận hành | 6/10 | Có kế hoạch đào tạo, truyền thông nhưng chưa có cam kết nhân sự vận hành lâu dài sau go-live — không đổi. |
| Tiến độ | 8/10 | Phương án linh hoạt (toàn trường vs. thí điểm) nay được gắn trực tiếp vào Roadmap chính thức thay vì chỉ là một ghi chú giả định — hợp lý và thực tế hơn. |

> **Rủi ro trọng yếu:** Hai tiêu chí điểm thấp nhất — Tham vấn người dùng (Nhóm III, 3/10) và Pháp lý (Nhóm IV, 4/10) — vẫn là loại rủi ro có thể làm sụp đổ cả dự án bất kể chất lượng tài liệu hay chiến lược tốt đến đâu. Việc tái cấu trúc thành 6 tài liệu giúp **định vị rõ hơn** hai điểm nghẽn này (đưa vào milestone/gate tường minh), nhưng bản thân chúng chưa được giải quyết.

## V. Giá trị dài hạn

_Nguồn tham chiếu: mô hình "Square Route" của Atkinson; Benefits Realization Management (PMI)._

| Tiêu chí | Điểm | Phản biện |
| --- | --- | --- |
| Benefits realization | 5/10 | Lợi ích vẫn chủ yếu định tính, chưa có cơ chế đo lường sau go-live ngoài bộ KPI đã có. |
| Khả năng được người dùng chấp nhận | 5/10 | Rủi ro "adoption thấp" vẫn được nhận diện nhưng biện pháp giảm thiểu còn chung chung ("truyền thông, đào tạo"). |
| Phù hợp chiến lược tổ chức | 8/10 | Rất phù hợp định hướng chuyển đổi số của ĐHQG-HCM/HCMUS — không đổi. |
| Mức độ cấp thiết | 6/10 | Vấn đề có thật nhưng không có deadline bắt buộc mang tính cấp bách — không đổi. |

## VI. Tiêu chí lựa chọn đầu tư

_Nguồn tham chiếu: Weighted Scoring Model cho lựa chọn/ưu tiên hóa dự án._

| Tiêu chí | Điểm | Phản biện |
| --- | --- | --- |
| ROI kỳ vọng | 5/10 | `04-feasibility-study.md` nay trình bày rõ lý do không quy đổi ROI tài chính thuần túy và đề xuất mô hình cost-avoidance làm hướng thay thế — lập luận chặt hơn dù vẫn thiếu số liệu để tính cụ thể. |
| Nguồn lực sẵn có | 5/10 | Giả định dùng nội lực CNTT trường, chưa có xác nhận chính thức — không đổi. |
| Rủi ro & độ phức tạp | 7/10 | Bảng rủi ro nay tách rõ 2 nhóm (kỹ thuật vs vận hành/dự án) theo đúng khung Feasibility Study — mạch lạc hơn bảng rủi ro gộp chung trước đây. |

## VII. Chỉ số kỹ thuật/DevOps (DORA) & VIII. Hậu triển khai (PIR)

N/A toàn bộ — dự án chưa có một dòng code nào để đo tần suất triển khai, mật độ lỗi (theo khung DORA), hay đối chiếu kết quả thực tế theo quy trình Post-Implementation Review. Đây là điều bình thường ở giai đoạn khởi tạo dự án, không phải điểm trừ.

- Điểm cộng duy nhất đáng ghi nhận: mục Tiêu chí Thành công & KPI trong `05-project-charter.md` đã có sẵn bộ tiêu chí thành công kèm giả định tiên quyết để làm cơ sở đối chiếu khi PIR diễn ra sau này — mức độ sẵn sàng của kế hoạch đánh giá: **7/10**.

---

## IX. Tổng hợp điểm số

Điểm trung bình mỗi nhóm (chỉ tính 6 nhóm có thể đánh giá ở giai đoạn hiện tại; Nhóm VII và VIII là N/A):

| Nhóm | Điểm trung bình /10 |
| --- | --- |
| I. Tam giác sắt mở rộng | 6.8 |
| II. Chất lượng SP (ISO 25010) | 6.3 |
| III. Yếu tố thành công | 5.9 |
| IV. Khả thi (TELOS) | 6.0 |
| V. Giá trị dài hạn | 6.0 |
| VI. Lựa chọn đầu tư | 5.7 |

**Điểm trung bình chung: 6,1 / 10** — mức "trung bình khá, nhích lên từ 5,8/10 của bản Business Case trước" — cải thiện đến từ tính rõ ràng/rigor của cấu trúc tài liệu, chưa đủ để phê duyệt toàn bộ dự án.

Mẫu hình tương tự bản đánh giá trước vẫn còn nguyên: các nhóm phản ánh kế hoạch quản lý (I) và kiến trúc/chất lượng tài liệu (II) đạt điểm khá tốt nhờ được hình thức hóa đúng khung lý thuyết. Ngược lại, các nhóm phản ánh thực chất rủi ro triển khai (III, IV) vẫn quanh 5,9–6,0, kéo xuống bởi đúng hai điểm nghẽn cũ: tham vấn người dùng thật (3/10) và rủi ro pháp lý/bản quyền chưa xử lý (4/10, dù đã được gate hóa rõ ràng hơn).

---

## X. Kết luận & Khuyến nghị

> **KHÔNG** đồng ý phê duyệt toàn bộ dự án (ngân sách Giai đoạn 1–3) ở thời điểm hiện tại.

> **ĐỒNG Ý** phê duyệt Giai đoạn 0 (khảo sát) — kèm 4 điều kiện tiên quyết trước khi trình duyệt Giai đoạn 1. Điểm khác so với lần đánh giá trước: 2 trong 4 điều kiện này **đã được cài cắm sẵn** như một phần cấu trúc chính thức của Giai đoạn 0 trong `05-project-charter.md` (milestone M1), nên việc thực thi có cơ sở theo dõi rõ ràng hơn — nhưng vẫn CHƯA hoàn thành.

### Bốn điều kiện tiên quyết

1. **Giải quyết pháp lý trước, không song song** — thiết kế và ký duyệt quy trình đồng ý công khai (consent) cho sinh viên trước khi số hóa bất kỳ khóa luận nào. Đã được đưa vào milestone M1 của Roadmap; cần theo dõi để đảm bảo thực sự hoàn thành trước khi bước sang Giai đoạn 1.
2. **Thay persona giả định bằng khảo sát thật** — tối thiểu 15–20 phỏng vấn/khảo sát sinh viên, giảng viên, cán bộ thư viện trong WP1. Mục Customer Discovery (`02-project-proposal.md`) đã ghi nhận rõ khoảng trống này; cần thực thi thay vì chỉ ghi nhận.
3. **Thay ước lượng bằng báo giá thật** — ít nhất cho hạng mục số hóa (khoản chi phối ngân sách, `04-feasibility-study.md` mục 3) trước khi trình duyệt số tiền cụ thể.
4. **Xác nhận cam kết nhân sự nội bộ** — văn bản xác nhận từ Phòng CNTT về việc bố trí 3–4 người trong 3 tháng, thay vì giả định như hiện tại trong `05-project-charter.md` mục Cơ sở Vật chất & Nguồn lực.

### Nhận định chung

Việc tái cấu trúc thành bộ 6 tài liệu Khởi tạo Dự án theo khung `project-initiation-writer` đã nâng chất lượng hồ sơ lên rõ rệt về mặt **rigor và tính tự-đủ-nghĩa**: Sponsor/Client/Customer/User được tách bạch, Feature Model chính thức hóa MVP, Stakeholder Analysis có Power/Interest Grid và Engagement Strategy, RACI Matrix gán trách nhiệm rõ ràng, và Cost/Budget/ROI được trình bày minh bạch hơn. Đây là tiến bộ thực chất, không chỉ là hình thức.

Tuy nhiên, khoảng cách lớn nhất **vẫn chưa thay đổi**: hai lỗ hổng có thể kiểm chứng ngay — tiếng nói người dùng thật và quy trình pháp lý về bản quyền — chỉ mới được **định vị rõ hơn** trong tài liệu (qua milestone gate và ghi nhận minh bạch), chứ chưa được **giải quyết trong thực tế**. Một vòng khảo sát và một quy trình consent được ký duyệt trong Giai đoạn 0 sẽ lấp đúng những khoảng trống này trước khi quay lại xin phê duyệt đầy đủ.

---

## Phụ lục — Khung tham chiếu đã sử dụng

| Khung tham chiếu | Áp dụng cho nhóm |
| --- | --- |
| Chow & Cao; Stankovic và cộng sự — mở rộng tam giác sắt | I |
| ISO/IEC 25010 (SQuaRE) — chất lượng sản phẩm phần mềm | II |
| Pinto & Slevin (10 yếu tố); Standish Group CHAOS Report | III |
| TELOS (Technical, Economic, Legal, Operational, Scheduling) | IV |
| Atkinson "Square Route"; PMI Benefits Realization Management | V |
| Weighted Scoring Model cho lựa chọn/ưu tiên hóa dự án | VI |
| DORA metrics (DevOps Research and Assessment) | VII |
| Post-Implementation Review (PIR) checklist | VIII |

---

_— Hết —_

_Tài liệu nội bộ_
