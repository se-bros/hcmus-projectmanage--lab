# Các mô hình phát triển phần mềm (Software Development Models)

**Giảng viên / Lecturer:** Ngô Huy Biên (Ngo Huy Bien) — nhbien@fit.hcmus.edu.vn
**Đơn vị / Department:** Bộ môn Kỹ thuật phần mềm, Khoa Công nghệ thông tin, Trường Đại học Khoa học Tự nhiên, ĐHQG-HCM
**Môn học / Course:** Quản lý Dự án Phần mềm (Software Project Management)

---

## 1. Mục tiêu bài học (Learning Objectives)

Sau bài học, người học có thể:

- Trình bày mô hình Thác nước và các biến thể của nó.
  _(Present the Waterfall model and its modified versions.)_
- Trình bày mô hình Phát triển lặp và tăng dần (IID).
  _(Present the Iterative and Incremental Development (IID) model.)_
- Trình bày mô hình Xoắn ốc.
  _(Present the Spiral model.)_
- Trình bày mô hình Vee.
  _(Present the Vee model.)_

## 2. Nội dung (Contents Overview)

| #   | Chủ đề (VI)                        | Topic (EN)                            |
| --- | ---------------------------------- | ------------------------------------- |
| I   | Tại sao cần mô hình phát triển?    | Why Software Development Models?      |
| II  | Phân tích và Mã hóa (Code and Fix) | Analysis, Coding and Code & Fix       |
| III | Mô hình Thác nước                  | Waterfall Model                       |
| IV  | Các biến thể của Thác nước         | Waterfall Variants                    |
| V   | Mô hình IID (Lặp và Tăng dần)      | Iterative and Incremental Development |
| VI  | Mô hình Xoắn ốc                    | Spiral Model                          |
| VII | Mô hình Vee                        | Vee Model                             |

---

## I. Tại sao cần mô hình phát triển phần mềm? (Why Software Development Models?)

Mô hình phát triển phần mềm giúp trả lời các câu hỏi cơ bản trong quản lý dự án:

- Bước tiếp theo chúng ta nên làm gì? _(Which step should we do next?)_
- Sẽ mất bao lâu? _(How long will it take?)_
- Thực hiện bước đó như thế nào? Nó sử dụng và tạo ra những hiện vật nào? _(How to perform the step? Which artifacts will it use and produce?)_
- Ai chịu trách nhiệm thực hiện bước này? _(Who is responsible for doing the step?)_

---

## II. Phân tích và Mã hóa — Code and Fix \[1, 2\]

### 2.1 Hai bước cơ bản

> Có hai bước cơ bản chung cho tất cả các quá trình phát triển chương trình máy tính, bất kể quy mô hay độ phức tạp: bước phân tích và bước mã hóa.
> _(There are two essential steps common to all computer program developments, regardless of size or complexity: an analysis step, followed by a coding step.)_ \[1\]

Đây là những nỗ lực mà hầu hết khách hàng sẵn lòng trả tiền vì cả hai bước đều liên quan đến công việc sáng tạo thực sự.

### 2.2 Phương pháp Code and Fix

Phương pháp Code and Fix là phương pháp phát triển trong đó lập trình viên viết code rồi sửa các lỗi trong code đó.

**Đặc điểm:**

- Không có chi phí quản lý (không có kế hoạch, tài liệu, QA, tiêu chuẩn — chỉ là lập trình).
- Không yêu cầu chuyên môn cao; ai cũng có thể làm.

**Nhược điểm nghiêm trọng:**

- Không có cách nào để nhận diện rủi ro.
- Không phù hợp với nhu cầu của người dùng.
- Cấu trúc kém, không có cách tiếp cận chất lượng.
- Chi phí sửa chữa tốn kém.
- Không có cách nào đánh giá tiến độ.

### 2.3 Phương pháp hoành tráng hơn (A More Grandiose Approach)

> Theo kinh nghiệm thực tế, mô hình đơn giản hơn (Code and Fix) chưa bao giờ hoạt động trên quy mô phát triển phần mềm lớn.
> _(In my experience, the simpler model has never worked on large software development efforts.)_ \[2\]

Lý do: Các giai đoạn thiết kế liên kết chặt chẽ nhau — nếu có sự cố ở một giai đoạn, việc lặp lại thiết kế không bao giờ chỉ giới hạn ở các bước kế tiếp mà thường lan rộng ra nhiều giai đoạn.

---

## III. Mô hình Thác nước (Waterfall Model) \[2\]

### 3.1 Đặc điểm của mô hình Thác nước (của Winston Royce)

- Bao gồm các giai đoạn xác định được thực hiện tuần tự.
  _(Consists of definite phases that are executed in sequence.)_
- Có các sản phẩm hữu hình được tạo ra vào cuối từng giai đoạn.
  _(There are tangible deliverables produced at the end of each phase.)_
- Các giai đoạn có thể được xem xét lại nhưng chu trình tổng thể được thực hiện không quá 2 lần (lần đầu có thể là mô phỏng).
  _(The phases be revisited but the overall cycle is completely executed no more than 2 times. If executed more than once, the first cycle is for a simulation.)_
- Khi thiết kế bắt đầu, một quy trình kiểm soát thay đổi chính thức được áp dụng.
  _(Once design begins, a formal change-control process is used.)_
- Quá trình được điều khiển bằng tài liệu.
  _(The process is document-driven.)_

### 3.2 Ưu và nhược điểm (Pros & Cons)

**Ưu điểm:**

- Nhấn mạnh tài liệu đầy đủ như tiêu chí hoàn thành các giai đoạn sớm.
- Hạn chế rủi ro ở mức có thể chấp nhận được.
- Tránh khả năng mất kiểm soát dự án.
- Giảm thiểu nỗ lực chi tiêu vào các hướng không mong muốn.

**Nhược điểm:**

- Tiêu chuẩn dựa trên tài liệu đã đẩy nhiều dự án viết thông số kỹ thuật phức tạp cho giao diện người dùng chưa được hiểu rõ, dẫn đến mã nguồn không thể sử dụng.
- Trong thực tế, cần bắt đầu thiết kế và mã hóa phần mềm, và lập mô hình phần cứng, sớm hơn trong chu trình dự án.

### 3.3 Khuyến nghị của Royce để giảm thiểu rủi ro Thác nước \[3\]

1. Phát triển nguyên mẫu giao diện người dùng _(Develop a user-interface prototype)_
2. Sử dụng storyboarding hệ thống _(Use system storyboarding)_
3. Tiến hành phỏng vấn người dùng _(Conduct user interviews)_
4. Quay video người dùng tương tác với hệ thống cũ _(Videotape users interacting with an older system)_

### 3.4 Năm khuyến nghị bổ sung của Royce

1. Tài liệu thiết kế đầy đủ — lý do: giao tiếp, kiểm soát chất lượng, hỗ trợ tất cả các giai đoạn, hỗ trợ thiết kế lại.
2. Thực hiện hai lần ("Làm điều đó hai lần") — lần đầu cung cấp mô phỏng sớm của sản phẩm cuối cùng, với thang thời gian tương đối nhỏ.
3. Lập kế hoạch, kiểm soát và giám sát kiểm tra.
4. Thu hút khách hàng — sự tham gia phải chính thức, sâu sắc và liên tục.
5. Thiết kế chương trình sơ bộ trước khi phân tích chi tiết bắt đầu.

### 3.5 Khi nào nên sử dụng mô hình Thác nước?

- Chi phí và thời gian rõ ràng và cố định.
- Mục tiêu rõ ràng, đáng tin cậy và cố định.
- Yêu cầu có thể được xác định đầy đủ và không mơ hồ.
- Công nghệ được hiểu rõ.
- Nguồn lực (có chuyên môn) có sẵn.
- Các dự án tương tự đã tồn tại trước đây.
- Hệ thống (bảo trì) hiện có có sẵn ngay từ đầu.

---

## IV. Các biến thể của Thác nước (Waterfall Variants)

### 4.1 Mô hình Sashimi

- Hầu hết điểm yếu của Thác nước thuần túy phát sinh từ việc xử lý các hoạt động theo từng giai đoạn rời rạc, tuần tự.
  _(Most weaknesses in the pure waterfall arise from the treatment of activities as disjoint, sequential phases.)_
- Mô hình Sashimi đề xuất mức độ chồng chéo mạnh hơn giữa các giai đoạn.
  _(Sashimi model suggests a stronger degree of overlap between phases.)_
- **Nhược điểm:** Các cột mốc mơ hồ hơn; thực hiện song song có thể dẫn đến hiểu lầm và giả định sai.

### 4.2 Thác nước với các tiểu dự án (Waterfall with Subprojects)

- Nếu kiến trúc đã phân tách hệ thống thành các hệ thống con độc lập về mặt logic, có thể quản lý các dự án riêng biệt, mỗi dự án theo tốc độ riêng của nó.
  _(If the architecture has broken the system into logically independent subsystems, you can spin off separate projects, each proceeding at its own pace.)_
- Rủi ro chính: sự phụ thuộc lẫn nhau không lường trước được giữa các dự án con.

### 4.3 Giao hàng theo giai đoạn (Staged Delivery)

- Mô hình giao hàng theo giai đoạn là mô hình trong đó phần mềm được trình bày cho khách hàng qua các giai đoạn được cải tiến liên tục.
  _(Staged delivery is a model in which you show software to the customer in successively refined stages.)_
- **Ưu điểm:** Tránh tình trạng không có phần nào hoàn thành cho đến khi tất cả đều xong; cung cấp dấu hiệu tiến độ sớm hơn.
- **Lưu ý:** Phải tính đến tất cả các phụ thuộc kỹ thuật giữa các thành phần; có chi phí tích hợp.

### 4.4 Mô hình Thác nước trong thế giới thực

**Cho hệ thống mới:**

| Giai đoạn                             | Mô tả                                |
| ------------------------------------- | ------------------------------------ |
| Yêu cầu cấp cao + Thiết kế cấp cao    | Với nguyên mẫu và PoC                |
| Kế hoạch đầu tiên và ước tính         | Hợp đồng đầu tiên                    |
| Yêu cầu chi tiết và test case         | —                                    |
| Kiến trúc đầy đủ và thiết kế chi tiết | —                                    |
| Kế hoạch và lịch trình                | Hợp đồng đầy đủ                      |
| Thực hiện/Kiểm tra đơn vị             | Phân phối theo giai đoạn nếu khả thi |
| Kiểm tra hệ thống                     | Phân phối theo giai đoạn nếu khả thi |
| Sản xuất                              | —                                    |

**Cho hệ thống bảo trì:** Tương tự, nhưng giai đoạn đầu là "hiểu hệ thống hiện tại" (với nguyên mẫu và PoC), và kiến trúc được sửa đổi (revised architecture).

---

## V. Mô hình IID — Phát triển Lặp và Tăng dần (Iterative and Incremental Development) \[4\]

### 5.1 Khái niệm cơ bản

> Phát triển lặp và tăng dần là một cách tiếp cận xây dựng phần mềm trong đó vòng đời tổng thể bao gồm nhiều lần lặp theo trình tự, và chức năng hệ thống được cắt thành từng phần (increment).
> _(IID is an approach in which the overall lifecycle is composed of several iterations in sequence, and system functionality are sliced into increments.)_ \[4\]

- Mục tiêu khi kết thúc mỗi lần lặp: một bản phát hành lặp ổn định, tích hợp và được kiểm tra của hệ thống hoàn thiện một phần.
  _(The goal for the end of an iteration is an iteration release — a stable, integrated and tested partially complete system.)_
- Mỗi lần lặp là một tiểu dự án khép kín bao gồm phân tích yêu cầu, thiết kế, lập trình và kiểm thử.
  _(Each iteration is a self-contained mini-project composed of activities such as requirements analysis, design, programming, and test.)_

### 5.2 Phân phối tăng dần (Incremental Delivery)

Phân phối tăng dần là thực hành phân phối lặp đi lặp lại một hệ thống vào môi trường sản xuất (hoặc thị trường) theo một loạt các khả năng mở rộng.
_(Incremental delivery is the practice of repeatedly delivering a system into production in a series of expanding capabilities.)_

### 5.3 Phân phối tiến hóa (Evolutionary Delivery)

Phân phối tiến hóa là cải tiến của phân phối tăng dần, trong đó có nỗ lực mạnh mẽ để nắm bắt phản hồi về sản phẩm đã cài đặt và sử dụng phản hồi này để hướng dẫn lần giao hàng tiếp theo.
_(Evolutionary delivery is a refinement of incremental delivery in which there is a vigorous attempt to capture feedback regarding the installed product, and use this to guide the next delivery.)_

### 5.4 Nguyên mẫu tiến hóa (Evolutionary Prototyping Model)

- Bắt đầu bằng cách phát triển các khía cạnh dễ thấy nhất của hệ thống.
  _(Begin by developing the most visible aspects of the system.)_
- Trình diễn cho khách hàng, sau đó tiếp tục phát triển nguyên mẫu dựa trên phản hồi nhận được.
  _(Demonstrate that part of the system to the customer, then continue to develop the prototype based on feedback.)_
- Tại một thời điểm, khách hàng đồng ý rằng nguyên mẫu là "đủ tốt".
  _(At some point, you and the customer agree that the prototype is "good enough.")_
- Hoàn thành các công việc còn lại và phát hành nguyên mẫu như sản phẩm cuối cùng.
  _(Complete any remaining work on the system and release the prototype as the final product.)_

### 5.5 Phát triển lặp theo khung thời gian (Time-boxed Iterative Development)

Iteration time-boxing là thực hành cố định ngày kết thúc của lần lặp và không cho phép thay đổi nó.
_(Iteration time-boxing is the practice of fixing the iteration end date and not allowing it to change.)_

### 5.6 IID tiến hóa (Evolutionary IID)

Phát triển lặp mang tính tiến hóa hàm ý rằng các yêu cầu, kế hoạch, ước tính và giải pháp tiến hóa hoặc được cải tiến qua các lần lặp — thay vì được xác định đầy đủ và "đóng băng" trong một bước đặc tả lớn trước khi bắt đầu lặp.
_(Evolutionary iterative development implies that requirements, plans, estimates, and solutions evolve or are refined over iterations, rather than being fully defined and "frozen" in a major up-front specification effort before development iterations begin.)_

**Về kỹ thuật yêu cầu trong IID:** Trong dự án 20 lần lặp, hầu hết các yêu cầu sẽ được phát hiện và tinh chỉnh trong 4 lần lặp đầu tiên.

**Nón bất định (Cone of Uncertainty):** Độ không chắc chắn trong ước tính giảm dần theo thời gian khi dự án tiến triển.

### 5.7 Ưu và nhược điểm của IID

| Ưu điểm                                                     | Nhược điểm                                                                            |
| ----------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| Có dấu hiệu tiến triển ổn định, rõ ràng                     | Không thể biết ngay từ đầu sẽ mất bao lâu để tạo ra sản phẩm chấp nhận được           |
| Thích hợp khi yêu cầu thay đổi nhanh                        | Khó để tích hợp các ứng dụng được phát triển độc lập                                  |
| Thích hợp khi khách hàng không muốn cam kết yêu cầu cố định | Dễ phát triển nhiều mã khó thay đổi trước khi giải quyết các vấn đề kiến trúc dài hạn |
| Phù hợp khi cả bạn và khách hàng chưa hiểu rõ lĩnh vực      | —                                                                                     |
| Phù hợp khi nhà phát triển chưa chắc về kiến trúc tối ưu    | —                                                                                     |

### 5.8 Khi nào nên sử dụng mô hình IID?

- Chi phí và thời gian linh hoạt.
- Mục tiêu rõ ràng nhưng không cố định.
- Yêu cầu không thể xác định (không có triển khai hệ thống) hoặc mơ hồ.
- Công nghệ là mới.
- Nguồn lực (có chuyên môn) không có sẵn.
- Các dự án tương tự không tồn tại.
- Hệ thống (bảo trì) hiện có có thể không có sẵn ngay từ đầu.

---

## VI. Mô hình Xoắn ốc (Spiral Model) \[5, 6, 7\]

### 6.1 Cấu trúc của mô hình Xoắn ốc

- **Kích thước xuyên tâm:** đại diện cho chi phí tích lũy phát sinh để hoàn thành các bước đến thời điểm hiện tại.
  _(The radial dimension represents the cumulative cost incurred in accomplishing steps to date.)_
- **Kích thước góc:** đại diện cho tiến bộ đạt được khi hoàn thành mỗi chu kỳ xoắn ốc.
  _(The angular dimension represents the progress made in completing each cycle of the spiral.)_
- **Rủi ro** được phân loại thành: rủi ro hiệu suất/giao diện người dùng và rủi ro phát triển.

Mỗi chu kỳ xoắn ốc bắt đầu với việc xác định:

1. Mục tiêu của phần sản phẩm đang được xây dựng (hiệu suất, chức năng, khả năng thích nghi với thay đổi...).
2. Các phương tiện thay thế để thực hiện phần sản phẩm đó (thiết kế A, thiết kế B, tái sử dụng, mua...).
3. Những ràng buộc áp đặt lên các lựa chọn thay thế (chi phí, lịch trình, giao diện...).

### 6.2 Phân tích rủi ro trong Xoắn ốc

1. Xác định các khu vực không chắc chắn — nguồn đáng kể của rủi ro dự án.
   _(Identify areas of uncertainty that are significant sources of project risk.)_
2. Xây dựng chiến lược tiết kiệm chi phí để giải quyết nguồn rủi ro — có thể bao gồm tạo mẫu, mô phỏng, đối chiếu, phỏng vấn người dùng, mô hình phân tích.
   _(Formulate a cost-effective strategy for resolving sources of risk — may involve prototyping, simulation, benchmarking, user questionnaires, analytic modelling.)_

### 6.3 Định nghĩa mô hình Xoắn ốc \[7\]

> Mô hình phát triển xoắn ốc là một trình tạo mô hình quy trình định hướng rủi ro (risk-driven process model generator).
> _(The spiral development model is a risk-driven process model generator.)_

**Hai đặc điểm phân biệt chính:**

- Cách tiếp cận chu kỳ để phát triển dần dần mức độ xác định và triển khai của hệ thống trong khi giảm mức độ rủi ro.
  _(A cyclic approach for incrementally growing a system's degree of definition and implementation while decreasing its degree of risk.)_
- Tập hợp các cột mốc điểm neo (anchor point milestones) để đảm bảo cam kết của các bên liên quan về tính khả thi và giải pháp hệ thống thỏa mãn lẫn nhau.
  _(A set of anchor point milestones for ensuring stakeholder commitment to feasible and mutually satisfactory system solutions.)_

Mô hình Xoắn ốc trả lời câu hỏi: "Nên làm gì tiếp theo?" và "Nên tiếp tục bao lâu?" — câu trả lời được thúc đẩy bởi rủi ro và thay đổi theo từng dự án.

### 6.4 Các cột mốc điểm neo (Anchor Point Milestones)

| Cột mốc                                                                | Mô tả                                                                                                                       |
| ---------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| **LCO — Mục tiêu vòng đời** _(Life Cycle Objectives)_                  | Cam kết các bên liên quan để hỗ trợ kiến trúc; xác định khái niệm hoạt động, yêu cầu hệ thống, kiến trúc, kế hoạch vòng đời |
| **LCA — Kiến trúc vòng đời** _(Life Cycle Architecture)_               | Cam kết các bên liên quan để hỗ trợ toàn bộ vòng đời; xác định kiến trúc hệ thống & phần mềm, tính khả thi                  |
| **IOC — Khả năng vận hành ban đầu** _(Initial Operational Capability)_ | Cam kết hỗ trợ vận hành; bao gồm chuẩn bị phần mềm, địa điểm, người dùng/vận hành/bảo trì                                   |

### 6.5 Ưu và nhược điểm của mô hình Xoắn ốc

| Ưu điểm                                                           | Nhược điểm                                                                                            |
| ----------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| Rất linh hoạt                                                     | Phức tạp và tốn thời gian                                                                             |
| Đối phó tốt hơn với những thay đổi (gần như không thể tránh khỏi) | Chỉ dành cho dự án nội bộ (trong công ty)                                                             |
| Chủ động trước rủi ro với phân tích rủi ro rõ ràng                | Đòi hỏi nhân sự có kiến thức về quản lý rủi ro                                                        |
| —                                                                 | Chỉ phù hợp với phần mềm quy mô lớn; không có ý nghĩa nếu chi phí phân tích rủi ro chiếm tỷ trọng lớn |

---

## VII. Mô hình Vee (Vee Model) \[8\]

### 7.1 Giới thiệu

- Mô hình Xoắn ốc cố gắng giải quyết thiếu sót của Thác nước bằng cách đề xuất tạo mẫu sớm để xác định rủi ro, nhưng vai trò của kỹ thuật hệ thống vẫn chưa rõ ràng.
  _(Spiral model addresses the need for early feasibility modeling, but the system engineering role is still obscured.)_
- Mô hình Vee làm rõ vai trò đó và hình dung khía cạnh kỹ thuật của chu trình dự án theo hình chữ "V".

### 7.2 Tổng quan về mô hình Vee

> Mô hình Vee là mô hình phát triển phần mềm trong đó khía cạnh kỹ thuật của chu trình dự án được hình dung như chữ "V", bắt đầu từ Nhu cầu người dùng ở trên bên trái và kết thúc bằng hệ thống được người dùng xác thực ở trên bên phải.
> _(V-model is a software development model in which the technical aspect of the project cycle is envisioned as a "Vee," starting with User needs on the upper left and ending with a User-validated system on the upper right.)_

**Cấu trúc:**

- **Cạnh trái:** Phân tách và Định nghĩa (đi xuống) — theo mô hình Thác nước.
- **Cạnh phải:** Tích hợp và Xác minh (đi lên) — xác minh ở các cấp độ lắp ráp, đơn vị, thành phần và hệ thống con, đỉnh cao là ở cấp độ hệ thống.

### 7.3 Chín giai đoạn của mô hình Vee

1. Hiểu yêu cầu người dùng, phát triển khái niệm hệ thống và kế hoạch xác nhận.
   _(Understand user requirements, develop system concept and validation plan.)_
2. Phát triển đặc tả hiệu suất hệ thống và kế hoạch xác minh hệ thống.
   _(Develop system performance specification and system verification plan.)_
3. Mở rộng đặc tả hiệu năng hệ thống thành đặc tả "Design-to" của Configuration Items (CI) và kế hoạch xác minh CI.
   _(Expand system performance specification into CI "Design-to" specifications and CI verification plan.)_
4. Phát triển các đặc tả "Design-to" thành tài liệu "Build-to" và kế hoạch kiểm tra.
   _(Evolve "Design-to" specifications into "Build-to" documentation and inspection plan.)_
5. Chế tạo, lắp ráp và mã hóa theo tài liệu "Build-to".
   _(Fabricate, assemble and code to "Build-to" documentation.)_
6. Kiểm tra theo tài liệu "Build-to".
   _(Inspect to "Build-to" documentation.)_
7. Lắp ráp các CI và thực hiện xác minh CI theo đặc tả "Design-to".
   _(Assemble CIs and perform CI verification to CI "Design-to" specifications.)_
8. Tích hợp hệ thống và thực hiện xác minh hệ thống theo đặc tả hiệu suất.
   _(Integrate system and perform system verification to performance specification.)_
9. Trình diễn và xác nhận hệ thống theo kế hoạch xác nhận người dùng.
   _(Demonstrate and validate system to user validation plan.)_

### 7.4 Sáu đường cơ sở (Six Baselines)

| Đường cơ sở                                                    | Thời điểm thiết lập                          |
| -------------------------------------------------------------- | -------------------------------------------- |
| Đường cơ sở yêu cầu người dùng _(User Requirements Baseline)_  | Trước Đánh giá Yêu cầu Hệ thống (SRR)        |
| Đường cơ sở khái niệm _(Concept Baseline)_                     | Tại SRR                                      |
| Đường cơ sở hiệu suất hệ thống _(System Performance Baseline)_ | Tại Đánh giá Thiết kế Hệ thống (SDR)         |
| Đường cơ sở "Design-To" _(Allocated Baseline)_                 | Tại chuỗi PDR (Preliminary Design Reviews)   |
| Đường cơ sở "Build-To" _(Preliminary Product Baseline)_        | Tại chuỗi CDR (Critical Design Reviews)      |
| Đường cơ sở "As-Built" _(Production Baseline)_                 | Tại chuỗi FQR (Formal Qualification Reviews) |

### 7.5 Nguyên tắc lặp trong mô hình Vee

- **Lặp đi xuống (Downward Iteration):** Nên có đủ lặp đi xuống để thiết lập tính khả thi và xác định, lượng hóa rủi ro.
- **Lặp đi lên (Upward Iteration):** Được phép nhưng nên giữ ở mức tối thiểu. Lặp với Yêu cầu Người dùng nên dừng tại PDR.
- **Sau PDR:** Nếu cần thay đổi đáng kể Yêu cầu Người dùng, dự án nên dừng và khởi động lại chu trình Vee mới.

### 7.6 Phát triển gia tăng trong Vee (Incremental Development)

Nếu Yêu cầu Người dùng quá mơ hồ để xác định cuối cùng tại PDR, một cách tiếp cận là phát triển dự án theo các bản phát hành gia tăng được xác định trước. Bản phát hành đầu tiên tập trung vào đáp ứng nhóm tối thiểu Yêu cầu Người dùng; các bản tiếp theo cung cấp thêm chức năng và hiệu suất.

### 7.7 Vai trò của Kỹ thuật hệ thống (Role of System Engineering)

- **Trên đường phân chia:** Kỹ thuật Hệ thống chịu trách nhiệm; Kỹ thuật Thiết kế hỗ trợ kỹ thuật.
- **Dưới đường phân chia:** Kỹ thuật Thiết kế chịu trách nhiệm; Kỹ thuật Hệ thống thực hiện kiểm toán kỹ thuật.
- Kỹ thuật Hệ thống có ảnh hưởng xuyên suốt toàn bộ vòng đời dự án — từ phát triển Yêu cầu Người dùng đến ngừng hoạt động hệ thống.
  _(System Engineering is influential throughout the entire project life cycle, from User Requirements development to system decommissioning.)_

---

## Tài liệu tham khảo (References)

1. Herbert D. Bennington (1956). _Production of Large Computer Programs_.
2. Winston Royce (1970). _Managing The Development of Large Software Systems_.
3. Steve McConnell (1996). _Rapid Development: Taming Wild Software Schedules_. Microsoft Press.
4. Craig Larman (2003). _Agile and Iterative Development: A Manager's Guide_.
5. Barry Boehm (1988). _A Spiral Model of Software Development and Enhancement_.
6. Nayan B. Ruparelia (2010). _Software Development Lifecycle_.
7. Barry Boehm (2000). _Spiral Development: Experience, Principles, and Refinements_.
8. Kevin Forsberg và Harold Mooz (1991). _The Relationship of System Engineering to the Project Cycle_.
