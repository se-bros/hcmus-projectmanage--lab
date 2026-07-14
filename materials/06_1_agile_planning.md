# Lập kế hoạch linh hoạt (Agile Planning)

**Giảng viên / Lecturer:** Ngô Huy Biên (Ngo Huy Bien) — nhbien@fit.hcmus.edu.vn
**Đơn vị / Department:** Bộ môn Kỹ thuật phần mềm, Khoa Công nghệ thông tin, Trường Đại học Khoa học Tự nhiên, ĐHQG-HCM
**Môn học / Course:** Quản lý Dự án Phần mềm (Software Project Management)

---

## 1. Mục tiêu bài học (Learning Objectives)

Sau bài học, người học có thể:

- Tạo lộ trình sản phẩm (product roadmap).
  *(Create a product roadmap.)*
- Tạo kế hoạch phát hành (release plan).
  *(Create a release plan.)*
- Tính toán chi phí dự án.
  *(Calculate project cost.)*
- Tạo các nhiệm vụ Sprint.
  *(Create sprint tasks.)*
- Tạo hợp đồng linh hoạt.
  *(Create an agile contract.)*

## 2. Nội dung (Contents Overview)

| # | Chủ đề (VI) | Topic (EN) |
|---|---|---|
| I | Ước tính cấp cao | High-Level Estimate |
| II | Lộ trình sản phẩm | Product Roadmap |
| III | Lập kế hoạch phát hành | Release Planning |
| IV | Kế hoạch phát hành có ngày cố định | Fixed-Date Release Plan |
| V | Kế hoạch phát hành phạm vi cố định | Fixed-Scope Release Plan |
| VI | Tính toán chi phí phát hành | Release Cost Calculation |
| VII | Kiến trúc hệ thống & Sprint Tasks | System Architecture & Sprint Tasks |
| VIII | Hợp đồng linh hoạt | Agile Contracts |

---

## I. Ước tính cấp cao (High-Level Estimate) \[1, 2\]

Lập kế hoạch linh hoạt:
*(Agile planning:)*
- Tập trung nhiều vào **quá trình lập kế hoạch** hơn là tạo ra một kế hoạch cố định.
  *(Focused more on the planning than on the creation of a plan.)*
- Khuyến khích thay đổi và tạo ra các kế hoạch có thể dễ dàng thay đổi.
  *(Encourages change and results in plans that are easily changed.)*
- Trải dài khắp dự án — không phải sự kiện một lần.
  *(Is spread throughout the project.)*

**Kỹ thuật ước tính cấp cao:**
- Dùng dãy Fibonacci: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
- Mấu chốt là **tính tương đối**: Chọn một thứ quen thuộc, cho nó 3 điểm. Sau đó so sánh mọi thứ khác với nó.
  *(The key is about relativity: Pick one familiar thing, give it 3, then compare everything else against it.)*
- Chúng ta **KHÔNG THỂ** đưa ra ước tính chính xác — và điều đó là bình thường.

---

## II. Lộ trình sản phẩm (Product Roadmap) \[3\]

> Lộ trình sản phẩm là một loạt các phiên bản nhằm đạt được một số hoặc tất cả tầm nhìn sản phẩm của chúng ta.
> *(Product roadmap: a series of releases for achieving some or all of our product vision.)*

- Nếu chỉ lên kế hoạch một bản phát hành nhỏ duy nhất, không cần lộ trình sản phẩm.
- Phát hành thường xuyên không có nghĩa là đặt deadline quá quyết liệt — điều đó thường dẫn đến bỏ lỡ ngày.
  *(Releasing frequently doesn't mean setting overly aggressive deadlines; such deadlines frequently result in missed dates.)*
- Mỗi bản phát hành tập trung vào một tập nhỏ **Tính năng phát hành tối thiểu (MRF)** mà các bên liên quan đạt đồng thuận mạnh mẽ.
  *(Each release focuses on a small set of Minimum Releasable Features (MRFs) around which stakeholders share strong group consensus.)*

Lộ trình nên kéo dài ít nhất đến thời điểm bạn yêu cầu người khác tài trợ.

---

## III. Lập kế hoạch phát hành (Release Planning) \[3\]

Lập kế hoạch phát hành là lập kế hoạch dài hạn để trả lời câu hỏi:
- "Khi nào chúng ta sẽ hoàn thành?" *(When will we be done?)*
- "Tôi có thể nhận được những tính năng nào vào cuối năm?" *(Which features can I get by end of year?)*
- "Cái này sẽ có giá bao nhiêu?" *(How much will this cost?)*

Lập kế hoạch phát hành **không phải** là sự kiện một lần — mà là hoạt động thường xuyên, mỗi Sprint.

**Quy trình lập kế hoạch phát hành:**

1. **Tạo ước tính cấp cao** — dùng story points.
2. **Tạo lộ trình sản phẩm** — xác định các bản phát hành theo MRF.
3. **Ưu tiên các hạng mục tồn đọng** — dùng bản đồ câu chuyện (story map) để xác định giá trị kinh doanh.
4. **Tạo bản đồ Sprint (Sprint Map)** — phân bổ PBI vào từng Sprint dựa trên vận tốc nhóm.
5. **Tạo kế hoạch phát hành sơ bộ** — xác định các bản phát hành và thời gian dự kiến.
6. **Xác định ràng buộc phát hành** — phạm vi cố định? ngày cố định? ngân sách cố định?
7. **Tạo kế hoạch phát hành chi tiết**.
8. **Tính toán chi phí phát hành**.
9. **Tạo dự toán dự án** — gồm kích thước, thời gian và chi phí.
10. **Chuẩn bị cho phát hành** — nhân sự, rủi ro, công cụ, ngân sách.
11. **Tạo kiến trúc hệ thống cho phát hành**.
12. **Thực hiện Iteration 0** — thiết lập hạ tầng.

---

## IV. Kế hoạch phát hành có ngày cố định (Fixed-Date Release Plan)

Khi ngày phát hành đã cố định, ta xác định **phạm vi có thể bàn giao**:

1. Xác định có bao nhiêu Sprint trong bản phát hành.
2. Chăm chút Product Backlog đến độ sâu đủ.
3. Đo hoặc ước tính vận tốc nhóm theo **dãy** (vận tốc trung bình nhanh hơn và chậm hơn).
4. Nhân vận tốc chậm hơn × số Sprint → vẽ đường "**will-have**" (chắc chắn có).
5. Nhân vận tốc nhanh hơn × số Sprint → vẽ đường "**might-have**" (có thể có).

Xác định vị trí các tính năng bắt buộc phải có (must-have) so với phạm vi có thể bàn giao.

---

## V. Kế hoạch phát hành phạm vi cố định (Fixed-Scope Release Plan)

Khi phạm vi đã cố định, ta xác định **khoảng thời gian cần thiết**:

1. Chăm chút Product Backlog để bao gồm ít nhất các PBI mong muốn.
2. Xác định tổng kích thước của PBI sẽ bàn giao.
3. Đo hoặc ước tính vận tốc nhóm theo dãy.
4. Tổng kích thước ÷ vận tốc nhanh hơn (làm tròn lên) = số Sprint **thấp nhất**.
5. Tổng kích thước ÷ vận tốc chậm hơn (làm tròn lên) = số Sprint **cao nhất**.

---

## VI. Tính toán chi phí phát hành (Release Cost Calculation)

1. Xác định thành phần nhóm.
2. Xác định độ dài Sprint.
3. Xác định chi phí nhân sự để vận hành một Sprint.
4. Với ngày cố định: `Chi phí = Số Sprint × Chi phí/Sprint`
5. Với phạm vi cố định: `Khoảng chi phí = \[Số Sprint thấp × Chi phí/Sprint, Số Sprint cao × Chi phí/Sprint\]`

**Ví dụ ước toán dự án:**
- Dự án: XYZ. Bắt đầu: 06/09/21. Kết thúc: 27/12/21.
- Kích thước: 720 điểm. Thời gian: 80 ngày. Chi phí: $61.580.

---

## VII. Kiến trúc hệ thống & Sprint Tasks (System Architecture & Sprint Tasks)

### 7.1 Tạo kiến trúc hệ thống cho phát hành

- Xem xét các hạng mục tồn đọng được giao.
- Xác định những thay đổi cần thiết.
- Phân tích miền và cập nhật mô hình miền.
- Tinh chỉnh kiến trúc để hỗ trợ bối cảnh mới.
- Tổ chức cuộc họp đánh giá thiết kế.

Trong môi trường linh hoạt, ít thiết kế được thực hiện trước — phần lớn được giao cho các nhóm thành phần.
*(In agile environments, less of the design is done upfront and more is delegated to component teams.)*

### 7.2 Tạo Sprint Backlog và Sprint Tasks

**Sprint Backlog:** Danh sách công việc nhóm phải giải quyết trong Sprint tiếp theo.

**Sprint Tasks (Nhiệm vụ Sprint):**
- Các tính năng được chia thành nhiệm vụ, mỗi nhiệm vụ **từ 4 đến 16 giờ** làm việc.
  *(Features are broken down into tasks between four and sixteen hours of work.)*
- Cá nhân không đăng ký nhiệm vụ cho đến khi lần lặp bắt đầu, và thường chỉ đăng ký một hoặc hai nhiệm vụ liên quan cùng lúc.
- Nhiệm vụ mới không bắt đầu cho đến khi nhiệm vụ trước được hoàn thành.

**Lập kế hoạch Sprint (Sprint Planning):**
- Xác định sản phẩm bàn giao Sprint *(Sprint deliverables)*
- Xác định cách đạt được sản phẩm bàn giao Sprint
- Thỏa thuận giữa Product Owner và Nhóm

---

## VIII. Hợp đồng linh hoạt (Agile Contracts) \[5\]

### 8.1 Hợp đồng giá cố định truyền thống (Traditional Fixed-Price Contract)

Hợp đồng dựa trên phạm vi hoàn chỉnh được xác định, bồi thường và ngày giao hàng. Dựa trên mô hình Thác nước.

| Quan điểm | Ưu | Nhược |
|---|---|---|
| **Khách hàng** | Giá biết trước; cảm giác kiểm soát an toàn | Thay đổi có chi phí cao; thông tin không đầy đủ và không thể đoán trước |
| **Nhà cung cấp** | Doanh thu thêm khi có thay đổi (yêu cầu thay đổi) | Rủi ro cao nếu thiếu chuyên môn |
| **Nhà tư vấn** | Tăng khả năng thành công dự án | Thành công không bao giờ được đảm bảo |

### 8.2 Hợp đồng thời gian và vật liệu (Time and Materials Contract)

Phù hợp khi nhiều dự án CNTT không thể mô tả đầy đủ và rõ ràng trước.
*(Many IT projects cannot be described fully and clearly in advance.)*

| Quan điểm | Đặc điểm |
|---|---|
| **Khách hàng** | Cần quản lý vi mô liên tục; trách nhiệm quản lý toàn phần thuộc về khách hàng |
| **Nhà cung cấp** | Tối đa hóa lợi nhuận; không có hậu quả nếu dự án mất kiểm soát tài chính |
| **Nhà tư vấn** | Thiếu vị thế thanh toán rõ ràng dựa trên hiệu suất |

### 8.3 Hợp đồng giá cố định linh hoạt (Agile Fixed-Price Contract) \[5\]

Kết hợp ưu điểm của cả hai loại hợp đồng trên. 4 điểm khác biệt chính so với hợp đồng T&M:

1. **Ước tính sơ bộ "giá cố định"** dựa trên Product Backlog thô ban đầu.
   *(A rough estimate — the "fixed" price — is made based on a rough initial product backlog.)*
2. **Chia sẻ rủi ro:** Nếu chi phí thực vượt ước tính, cả khách hàng và nhà cung cấp chia sẻ chi phí (nhà cung cấp chỉ tính 30-70% chi phí thêm).
3. **Yêu cầu có thể thay đổi** và được đánh giá trong phạm vi giá "cố định" — thường thay thế PBI cũ bằng mới.
4. **Phần mềm làm việc có chất lượng** được giao mỗi 2-3 tuần cho khách hàng.

**Điểm yếu:** Nhà cung cấp có thể rời hợp đồng khi toàn bộ ngân sách đã được chi tiêu.

---

## Tài liệu tham khảo (References)

1. Mike Cohn (2005). *Agile Estimating and Planning*. Pearson Education.
2. Ken Schwaber (1995). *SCRUM Development Process*.
3. Kenneth S. Rubin (2012). *Essential Scrum: A Practical Guide to the Most Popular Agile Process*. Addison-Wesley Professional.
4. Jonathan Rasmusson (2010). *The Agile Samurai: How Agile Masters Deliver Great Software*. Pragmatic Bookshelf.
5. Andreas Opelt et al. (2013). *Agile Contracts: Creating and Managing Successful Projects with Scrum*. John Wiley & Sons.
