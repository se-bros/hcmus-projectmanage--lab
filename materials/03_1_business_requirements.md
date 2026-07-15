# Yêu cầu kinh doanh (Business Requirements)

**Giảng viên / Lecturer:** Ngô Huy Biên (Ngo Huy Bien) — nhbien@fit.hcmus.edu.vn
**Đơn vị / Department:** Bộ môn Kỹ thuật phần mềm, Khoa Công nghệ thông tin, Trường Đại học Khoa học Tự nhiên, ĐHQG-HCM
**Môn học / Course:** Quản lý Dự án Phần mềm (Software Project Management)

---

## 1. Mục tiêu bài học (Learning Objectives)

Sau bài học, người học có thể:

- Khám phá và thu thập các yêu cầu kinh doanh.
  *(Discover business requirements.)*
- Tạo lập tài liệu tóm tắt điều hành (executive summary document).
  *(Create an executive summary document.)*

## 2. Nội dung (Contents Overview)

| # | Chủ đề (VI) | Topic (EN) |
|---|---|---|
| I | Yêu cầu kinh doanh | Business Requirements |
| II | Các bên liên quan | Stakeholders |
| III | Thuật ngữ | Terminologies |
| IV | Vấn đề | Problems |
| V | Mục tiêu kinh doanh | Business Goals |
| VI | Tính năng cấp cao | High-Level Features |
| VII | Sơ đồ bối cảnh | Context Diagram |
| VIII | Bài trình bày đánh giá | Evaluator Pitch |
| IX | Tóm tắt điều hành | Executive Summary |

---

## I. Yêu cầu kinh doanh (Business Requirements) \[1\]

> "Yêu cầu kinh doanh" đề cập đến một tập hợp thông tin mà khi tổng hợp lại, mô tả một nhu cầu dẫn đến một hoặc nhiều dự án nhằm đưa ra giải pháp và kết quả kinh doanh cuối cùng mong muốn.
> *("Business requirements" refers to a set of information that, in the aggregate, describes a need that leads to one or more projects to deliver a solution and the desired ultimate business outcomes.)*

- Các yêu cầu nghiệp vụ đặt ra bối cảnh và cho phép đo lường những lợi ích mà doanh nghiệp mong muốn đạt được từ việc thực hiện một dự án.
  *(The business requirements set the context for, and enable the measurement of, the benefits the business hopes to achieve from undertaking a project.)*

### 1.1 Thu thập hiện vật ban đầu (Capture Initial Artifacts)

Bước đầu tiên là thu thập các tài liệu, hiện vật liên quan đến dự án:

- Email *(Emails)*
- Slide thuyết trình *(Presentation slides)*
- Văn bản đề xuất *(Proposal document)*
- Hệ thống hiện có *(Existing systems)*
- Hệ thống tương tự *(Similar systems)*
- Hướng dẫn quản trị, hướng dẫn sử dụng *(Administrative guide, user guide)*
- Danh sách tính năng *(Feature list)*
- Đặc tả yêu cầu ban đầu *(Initial requirement specification)*

---

## II. Các bên liên quan (Stakeholders)

### 2.1 Xác định các bên liên quan \[3\] (Identify Stakeholders)

- Một **khách hàng** (client) là người trả tiền cho việc phát triển sản phẩm.
  *(A client pays for the development of the product.)*
- **Khách hàng mua sản phẩm** (customers) là người mua sản phẩm sau khi hoàn thành.
  *(Customers buy the product.)*
- **Người dùng** (users) là những người sẽ cuối cùng vận hành sản phẩm.
  *(Users are the people who will ultimately operate your product.)*

### 2.2 Đặc điểm của các bên liên quan \[4\]

- Các bên liên quan thường, nhưng không phải lúc nào cũng vậy, có một lợi ích kinh doanh liên quan đến phần mềm.
  *(Stakeholders usually, but not always, have a business interest in the software.)*
- Họ có thể trả tiền cho phần mềm hoặc trực tiếp hưởng lợi từ nó.
  *(They might pay for the software or directly profit from it.)*

### 2.3 Tạo bản đồ các bên liên quan (Create Stakeholder Map)

Bản đồ các bên liên quan (stakeholder map) là một sơ đồ mạng thể hiện tất cả mọi người có liên quan đến hoặc bị ảnh hưởng bởi hệ thống phần mềm đề xuất.
*(A stakeholder map is a network diagram showing all the people involved with or affected by the proposed software system.)*

- Bản đồ này lý tưởng để hình dung các mối quan hệ và tương tác giữa mọi người.
  *(They are ideal for visualizing relationships and interactions among people.)*
- Bản đồ còn cung cấp cái nhìn tổng quan về điều gì thúc đẩy các bên liên quan khác nhau.
  *(They also give you a snapshot of what motivates different stakeholders.)*

---

## III. Thuật ngữ (Terminologies)

### 3.1 Xác định tên miền quan tâm (Domains of Interest) \[3\]

Ví dụ minh họa về cách xác định tên miền từ mô tả bài toán:

> "Đường đóng băng vào mùa đông và điều kiện băng giá gây ra tai nạn đường bộ làm chết người. Chúng ta cần có khả năng dự đoán khi nào băng sẽ hình thành trên đường để có thể điều xe phá băng xử lý kịp thời. Chúng tôi kỳ vọng một hệ thống mới sẽ cung cấp những dự đoán chính xác hơn về điều kiện băng giá, dẫn đến việc xử lý làm tan băng kịp thời hơn và giảm tai nạn giao thông. Chúng tôi cũng muốn loại bỏ việc đối xử bừa bãi trên đường gây lãng phí hợp chất làm tan băng và ô nhiễm môi trường."
> *("Roads freeze in winter, and icy conditions cause road accidents that kill people. We need to be able to predict when ice will form on a road so we can schedule a de-icing truck to treat the road in time. We expect a new system to provide more accurate predictions of icy conditions. This will lead to more timely de-icing treatment than at present, which will reduce road accidents. We also want to eliminate indiscriminate treatment of roads, which wastes de-icing compounds and causes environmental damage.")*

Bốn tên miền được xác định từ đoạn văn trên: **Đường bộ (Roads)**, **Thời tiết (Weather)**, **Lập kế hoạch (Scheduling)**, **Vận tải đường bộ (Trucking)**.

### 3.2 Xác định thuật ngữ (Define Terminologies)

- Xây dựng nền tảng và bối cảnh xung quanh các thuật ngữ.
  *(Build a background and context around the terminologies.)*
- Mở rộng thuật ngữ thành các khái niệm cụ thể — càng đầy đủ càng tốt (as much as possible):
  - Vai trò kinh doanh *(Business roles)*
  - Quy trình làm việc kinh doanh *(Business workflows)*
  - Thành phần kinh doanh *(Business components)*
  - Đơn vị/Bộ phận *(Units/Departments)*
  - Các thực thể kinh doanh (đối tượng) *(Business entities (objects))*
  - Hiện vật kinh doanh *(Business artifacts)*

### 3.3 Phân tích thuật ngữ (Analyze Terminologies)

**Xác định nhà tài trợ (Identify Sponsor):**
- Tổ chức *(Organization)*
- Nhóm người hoặc cá nhân *(Group of people or individual)*

**Xác định ngân sách (Identify Budget):**
- Ngân sách hàng năm dành cho phát triển phần mềm hỗ trợ hoạt động kinh doanh *(Yearly budget for software development to support business operations)*
- Ngân sách hàng năm cho nghiên cứu liên quan đến phát triển phần mềm *(Yearly budget for research related to software development)*
- Tiết kiệm *(Savings)*

---

## IV. Vấn đề (Problems)

### 4.1 Định nghĩa vấn đề \[2\] (Problem Definition)

> Về mặt hình thức, một vấn đề có thể được định nghĩa là sự khác biệt giữa trạng thái mục tiêu và trạng thái hiện tại của một hệ thống.
> *(Formally, a problem can be defined as the differences between a goal state and the current state of a system.)*

> Giải quyết vấn đề có thể được định nghĩa là một quá trình tìm kiếm sử dụng các hành động để giảm bớt hoặc loại bỏ sự khác biệt đó.
> *(Problem solving can be defined as a search process using actions to reduce or eliminate the differences.)*

Các dấu hiệu nhận diện vấn đề thường gặp:
- Chúng tôi không thể… *(We cannot…)*
- Rất khó… *(It's difficult…)*
- Đó tốn chi phí quá nhiều… *(It costs too much…)*
- Gây đau đớn, lo sợ *(Pain, fear)*
- Gây chán nản *(Boredom)*
- Tốn tiền, tốn thời gian *(Money, time cost)*

### 4.2 Vấn đề vận hành (Operational Problems)

**Xử lý RFP có vấn đề cụ thể (Handle RFP with Concrete Problems):**

1. Lập tài liệu về các vấn đề vận hành *(Document Operational Problems)*:
   - Sửa lỗi, cải tiến bảo mật, tự động hóa tác vụ, số hóa, nâng cấp công nghệ, yêu cầu tuân thủ.
     *(Bug fixes, security enhancements, task automation, digitalization, technology upgrade, compliance requirements.)*
   - Chuẩn bị RFP với các vấn đề cụ thể; được thực hiện bởi nhân viên tổ chức (người quản lý tiếp thị, bán hàng, hỗ trợ).
     *(Prepare RFP with concrete problems; done by organization employees — marketing managers, sales, support.)*

2. Xử lý RFP với vấn đề cụ thể *(Handle RFP with Concrete Problems)* — sử dụng các đầu vào:
   - Yêu cầu đề xuất *(Request for proposal)*
   - Biên bản họp *(Meeting minutes)*
   - Hệ thống hiện có *(Existing systems)*
   - Mã nguồn và dữ liệu hiện có *(Existing source code and data)*
   - Hệ thống tương tự *(Similar systems)*

3. Chuẩn bị phản hồi cho RFP với vấn đề cụ thể *(Prepare Response to RFP with Concrete Problems)* — bao gồm:
   - Giải pháp *(Solution)*
   - Bản đồ hành trình khách hàng *(Customer journey map)*
   - Trải nghiệm người dùng trong việc tìm kiếm và tiếp cận dịch vụ *(Customer user experiences in seeking and accessing services)*
   - Chi phí *(Cost)*

**Xử lý RFP không có vấn đề cụ thể (Handle RFP without Concrete Problems):**

1. Xác định các vấn đề vận hành *(Identify Operational Problems)*:
   - Sửa lỗi, cải tiến bảo mật, tự động hóa tác vụ, số hóa, nâng cấp công nghệ.
     *(Bug fixes, security enhancements, task automation, digitalization, technology upgrade.)*
   - Được thực hiện bởi các đơn vị bên ngoài *(Done by external entities)*.

2. Khám phá vấn đề dẫn đến **phát triển hệ thống mới** *(Discover Problems Leading to New System Development)*:
   - Xây dựng hệ thống thông tin doanh nghiệp mới cho khách hàng.
     *(Building a new corporate information system (enterprise application) for a client.)*
   - Xuất phát từ: quy trình thủ công, giải pháp tầm thường hiện có, công nghệ lạc hậu, yêu cầu tuân thủ, hệ thống của đối thủ cạnh tranh.
     *(Start with: a manual process, a trivial existing solution, outdated technologies, compliance requirements, and competitors' systems.)*

3. Khám phá vấn đề dẫn đến **cải tiến hệ thống hiện có** *(Discover Problems Leading to Existing System Enhancements)*:
   - Tăng cường hệ thống thông tin doanh nghiệp hiện có cho khách hàng.
     *(Enhancing an existing corporate information system (enterprise application) for a client.)*
   - Xuất phát từ: lỗi, vấn đề bảo mật, vấn đề hiệu suất, yêu cầu tuân thủ, yêu cầu hội nhập, hệ thống của đối thủ.
     *(Start with: bugs, security issues, performance issues, compliance requirements, integration requirements, and competitors' systems.)*

4. Chuẩn bị phản hồi cho RFP không có vấn đề cụ thể: bao gồm vấn đề được phát hiện, giải pháp, bản đồ hành trình khách hàng, chi phí.

**Xử lý RFP nghiên cứu (Handle Research RFP):**

1. Xác định công nghệ xu hướng *(Identify Trending Technologies)*:
   - Xu hướng công nghệ mà đối thủ cạnh tranh đang sử dụng hoặc sắp sử dụng.
     *(Trending technologies that competitors are using or are going to be using.)*

2. Khám phá những cải tiến tiềm năng *(Discover Potential Enhancements)*:
   - Tiến hành nghiên cứu cho khách hàng; bắt đầu từ hệ thống hiện có, hệ thống đối thủ và kết quả nghiên cứu xu hướng.
     *(Conducting research for a client; start with existing systems, competitors' systems, and trending research results.)*

3. Chuẩn bị phản hồi cho RFP nghiên cứu: bao gồm các cải tiến tiềm năng đã phát hiện, bản đồ hành trình khách hàng, chi phí.

**Xác định cơ hội (Identify Opportunities):**

1. Xác định cơ hội *(Identify Opportunities)*:
   - Tiết kiệm *(Savings)*
   - Vấn đề thực tế dựa trên kiến thức, kỹ năng và kinh nghiệm *(Practical problems based on knowledge, skills and experiences)*

2. Khám phá vấn đề từ các bên liên quan *(Discover Problems)*:
   - Vấn đề có thể đến từ giám đốc điều hành, quản lý tiếp thị nhà tài trợ, hoặc người có tầm nhìn về sản phẩm.
     *(Problems might come from corporate executives, marketing managers funding sponsors, or product visionaries.)*

3. Khám phá vấn đề từ kịch bản thực tế *(Discover Problems from Real World Scenarios)*:
   - Quy trình công việc kinh doanh, quy trình kinh doanh, mô hình miền, trường hợp sử dụng kinh doanh.
     *(Business workflows, business processes, domain models, business use cases.)*
   - Sản phẩm của đối thủ cạnh tranh *(Competitors' products)*
   - Các tài liệu nghiên cứu *(Research papers)*

4. Xem xét cơ hội *(Review Opportunities)* — xác định:
   - Nhà tài trợ: tên, số điện thoại, địa chỉ *(Sponsor: name, phone number, address)*
   - Khách hàng (client): tên, số điện thoại, địa chỉ
   - Khách hàng mua (customers): tên, số điện thoại, địa chỉ
   - Người dùng: tên, số điện thoại, địa chỉ
   - Mô hình kinh doanh tham khảo: Salesforce (SaaS), Dropbox (SaaS), App Store, Google Play, AdSense, Spotify, Amazon (B2C), Uber (C2C)
   - Đối thủ cạnh tranh *(Competitors)*

### 4.3 Liên quan của vấn đề (Problem Relevance) \[2\]

Sự liên quan của bất kỳ nỗ lực nghiên cứu khoa học thiết kế nào phải gắn với một cộng đồng cấu thành.
*(The relevance of any design-science research effort is with respect to a constituent community.)*

Đối với các nhà nghiên cứu IS, cộng đồng đó bao gồm những người thực hiện kế hoạch, quản lý, thiết kế, vận hành, đánh giá hệ thống thông tin — và những người phát triển các công nghệ hỗ trợ họ.

Để phù hợp với cộng đồng này, nghiên cứu phải giải quyết:
- Những vấn đề phải đối mặt *(the problems faced)*
- Những cơ hội được tạo ra bởi sự tương tác của con người, tổ chức và công nghệ thông tin *(the opportunities afforded by the interaction of people, organizations, and information technology)*

---

## V. Mục tiêu kinh doanh (Business Goals)

### 5.1 Định nghĩa mục tiêu

- Mục tiêu là điều bạn muốn đạt được *(Goals: what you want to achieve)*.
- \[Từ điển Oxford\] Điều mà bạn mong muốn đạt được *(Something that you hope to achieve)*.
- Mục tiêu của dự án là yêu cầu cấp cao nhất — tất cả các yêu cầu chi tiết phải đóng góp tích cực vào việc đạt mục tiêu đó.
  *(The project goal is the highest-level requirement. All detailed requirements must make a positive contribution toward reaching that goal.)*

### 5.2 Thiết lập mục tiêu (Goal Settings)

Ví dụ mục tiêu tốt:
- **Mục đích:** Dự báo chính xác thời gian đóng băng trên đường và lên lịch xử lý làm tan băng kịp thời.
  *(Purpose: To accurately forecast road freezing times and schedule de-icing treatment.)*
- **Ưu điểm:** Giảm tai nạn giao thông bằng cách loại bỏ tình trạng đường băng.
  *(Advantage: To reduce road accidents by eliminating icy road conditions.)*
- **(Tùy chọn) Đo lường:** Tai nạn do băng không vượt quá 15% tổng số tai nạn trong mùa đông.
  *((Optional) Measurement: Accidents attributed to ice shall be no more than 15 percent of the total number of accidents during winter.)*

Ví dụ mục tiêu mơ hồ (cần tránh):
- Mục đích mơ hồ: "Cải thiện cách thức chúng tôi làm kinh doanh." *(Vague purpose: "To improve the way we do business.")*

### 5.3 Mục tiêu SMART

Mục tiêu SMART là mục tiêu được xác định rõ ràng mang đến sự rõ ràng, định hướng, động lực và tập trung.
*(A SMART goal is a well-defined target that gives you clarity, direction, motivation, and focus.)*

| Tiêu chí | Câu hỏi gợi ý |
|---|---|
| **S** — Specific (Cụ thể) | Cái gì? Tại sao? Ai? Ở đâu? Cái nào? |
| **M** — Measurable (Đo lường được) | Bao nhiêu? Tôi biết khi nào nó hoàn thành? |
| **A** — Achievable (Có thể đạt được) | Những bước nào? Mục tiêu có thể hoàn thành không? |
| **R** — Relevant (Liên quan) | Điều này có vẻ đáng giá không? |
| **T** — Time-bound (Có thời hạn) | Khi nào? Tôi có thể làm gì trong 6 tháng / 6 tuần / hôm nay? |

### 5.4 Xác định mục tiêu kinh doanh (Identify Business Goals)

Đối với hệ thống thông tin doanh nghiệp của khách hàng, mô tả:
- Vấn đề kinh doanh đang được giải quyết, hoặc quy trình đang được cải thiện.
  *(The business problem that is being solved or the process being improved.)*
- Môi trường mà hệ thống sẽ được sử dụng.
  *(The environment in which the system will be used.)*

Đối với sản phẩm thương mại, mô tả:
- Cơ hội kinh doanh hiện có và thị trường mà sản phẩm sẽ cạnh tranh.
  *(The business opportunity that exists and the market in which the product will be competing.)*
- Có thể bao gồm đánh giá so sánh các sản phẩm hiện có, chỉ ra lý do sản phẩm đề xuất hấp dẫn.
  *(Include a comparative evaluation of existing products, indicating why the proposed product is attractive.)*
- Mô tả các vấn đề hiện không thể giải quyết mà không có giải pháp đã hình dung.
  *(Describe the problems that cannot currently be solved without the envisioned solution.)*

### 5.5 Mục tiêu kinh doanh phổ biến (Common Business Goals) \[3\]

- Giảm chi phí và thời gian *(Reduce costs and time)*
- Cải thiện dịch vụ khách hàng *(Improve customer service)*
- Cải thiện giao tiếp *(Improve communication)*
- Cải thiện việc ra quyết định *(Improve decision making)*
- Tạo hoặc tăng cường mối quan hệ với nhà cung cấp, khách hàng hoặc đối tác *(Create or strengthen relationships with suppliers, customers, or partners)*
- Cải thiện các quy trình *(Improve processes)*
- Cải thiện khả năng báo cáo *(Improve reporting capabilities)*
- Hỗ trợ các yêu cầu pháp lý mới *(Support new legal requirements)*
- Mang lại nhiều niềm vui hơn *(Bring more pleasure)*
- Tạo một sản phẩm hoặc dịch vụ mới — có giá trị không? *(Create a new product or service. Is this product valuable?)*

### 5.6 Khám phá khách hàng về sản phẩm (Customer Discovery for a Product)

| Khía cạnh | Nội dung |
|---|---|
| **Ai? (Who?)** | Bạn bè, đồng nghiệp cũ, nhà đầu tư, nhân viên, sinh viên, khách hàng hiện tại |
| **Ở đâu? (Where?)** | Trường đại học, bệnh viện, đường phố, phương tiện truyền thông, hội nghị, triển lãm thương mại |
| **Cái gì? (What?)** | Thông tin cá nhân, nỗi đau/nhu cầu/hạnh phúc, lý do, nhận xét |
| **Làm sao? (How?)** | Khảo sát, demo, bản dùng thử |

---

## VI. Tính năng cấp cao (High-Level Features)

### 6.1 Mục tiêu kinh doanh của các bên liên quan

| Đối tượng (VI) | Stakeholder (EN) | Mục tiêu muốn đạt |
|---|---|---|
| Cá nhân | Individuals | Gia tăng sự giàu có, quyền lực, danh tiếng, niềm vui cá nhân, hoặc kiến thức |
| Tổ chức | Organizations | Tăng doanh thu, tối đa hóa lợi nhuận, phát triển kinh doanh, trở thành người dẫn đầu thị trường, cải thiện sự ổn định, tham gia thị trường mới, đánh bại đối thủ |
| Người lao động | Employees | Công việc thú vị và ý nghĩa, nâng cao kiến thức, giúp đỡ người dùng, được công nhận là chuyên gia |
| Nhóm phát triển | Development Team | Cải thiện thuộc tính chất lượng, giảm chi phí, thêm tính năng mới, thực hiện tiêu chuẩn, cải thiện thời gian đưa sản phẩm ra thị trường |
| Chính phủ | Governments | An ninh, phúc lợi công dân, trách nhiệm xã hội, tuân thủ pháp lý |

### 6.2 Xác định các tính năng cấp cao (Identify High-Level Features)

Tính năng cấp cao là cầu nối giữa mục tiêu kinh doanh của các bên liên quan và các yêu cầu chi tiết.

---

## VII. Sơ đồ bối cảnh (Context Diagram)

### 7.1 Đặt phạm vi \[3\] (Set the Scope)

- Phạm vi bạn quan tâm là phạm vi của công việc mà sản phẩm sẽ được sử dụng — tức là hoạt động kinh doanh mà người dùng cần sản phẩm.
  *(The scope you are interested in is the scope of the work for which the product is to be used. Work here means the business activity for which the user needs the product.)*
- Đặt phạm vi công việc nghĩa là xác định phần công việc bạn sẽ nghiên cứu, các phần công việc liền kề và luồng thông tin kết nối chúng.
  *(Setting the scope of the work means you determine what work you are about to study, what other pieces of work surround it, and what flows of information make up the connections.)*
- Khi đặt phạm vi, bạn quyết định bao nhiêu phần công việc sẽ được nghiên cứu và phần nào không. Công cụ: sơ đồ bối cảnh và bản đồ hệ sinh thái.
  *(When you set the scope, you are deciding how much of the work you will study and what you will not study. Tools: context diagram & ecosystem map.)*

### 7.2 Sơ đồ bối cảnh công việc (Work Context Diagram)

- Sơ đồ bối cảnh công việc xác định phạm vi của công việc mà chúng ta dự định nghiên cứu.
  *(The work context diagram identifies the scope of the work that we intend to study.)*
- Nó thể hiện công việc như một quy trình duy nhất chưa được điều tra, được bao quanh bởi các hệ thống liền kề.
  *(It shows the work as a single, as-yet uninvestigated process, surrounded by the adjacent systems.)*
- Sơ đồ bối cảnh cho thấy ranh giới trách nhiệm giữa công việc và các hệ thống lân cận.
  *(The work context shows where the responsibilities of the work and the responsibilities of the adjacent systems start and end.)*
- **Nguyên tắc:** Hãy hiểu công việc trước, sau đó mới quyết định sản phẩm nào hỗ trợ tốt nhất cho công việc đó.
  *(First understand the work, then decide which product best supports that work.)*

### 7.3 Bản đồ hệ sinh thái (Ecosystem Map) \[1\]

Bản đồ hệ sinh thái bổ sung cho sơ đồ bối cảnh, cho thấy toàn bộ hệ sinh thái mà hệ thống phần mềm tồn tại trong đó.

---

## VIII. Bài trình bày đánh giá (Evaluator Pitch)

Tạo một bài trình bày đánh giá (evaluator pitch) để trình bày dự án với các bên liên quan đánh giá.

**Ví dụ minh họa:**
- Bạn có biết rằng có bảo hiểm y tế khi đủ khả năng là yêu cầu pháp lý không?
  *(Did you know that having health insurance when you can afford is the law?)*
- Nếu bạn đủ khả năng mua bảo hiểm y tế nhưng chọn không mua vào năm 2016, bạn có thể phải trả một khoản phí — đôi khi được gọi là "hình phạt", "tiền phạt" hoặc "ủy thác cá nhân" — khi nộp thuế thu nhập liên bang năm 2016.
  *(If you can afford health insurance but choose not to get it for 2016, you may be required to pay a fee — sometimes called the "penalty," "fine," or "individual mandate" — when you file your 2016 federal income taxes.)*
- Chào mừng bạn đến với XYZ, nơi duy nhất để đăng ký hỗ trợ tài chính giúp giảm chi phí của bạn.
  *(Welcome to XYZ, the only place to apply for financial assistance to help reduce your costs.)*

---

## IX. Tóm tắt điều hành (Executive Summary)

Tóm tắt điều hành bao gồm các thành phần sau:

- **Thị trường/đối tượng mục tiêu:** nhà tài trợ, khách hàng, người dùng, các bên liên quan.
  *(The market/target audience: the sponsors, the customers, the users, the stakeholders.)*
- **Ngân sách và thời gian** *(The budget, the timing)*
- **Những điểm khó khăn/vấn đề/nhu cầu** *(The pain points/problems/needs)*
- **Giải pháp** — trường hợp sử dụng kinh doanh cốt lõi *(The solution — The core business use case)*
- **Đối thủ cạnh tranh/điểm yếu/sự khác biệt** *(The competitors/weakness/differentiators)*
- **Rủi ro/điểm mạnh/cơ hội/tầm nhìn lớn** *(The risks/strengths/opportunities/grand vision)*
- **Mục tiêu kinh doanh và lý do giải quyết vấn đề** — lợi ích dự kiến, doanh thu và thu nhập *(The business goals, the reasons to solve the problems — the predicted benefits, revenue and incomes)*
- **Đối với sản phẩm thương mại:** báo cáo khám phá khách hàng *(For a commercial product: The customer discovery report)*
- **Tính năng cấp cao, các hiện vật mong đợi, sơ đồ bối cảnh, bài trình bày sân thang máy** *(The high-level features, the expected artifacts, the context diagram, the elevator pitch)*

### Sản phẩm bàn giao (Deliverables)

| Hạng mục | Ví dụ |
|---|---|
| Đặc tả yêu cầu | Requirement specification |
| Đặc tả thử nghiệm, dữ liệu thử nghiệm và kết quả | Test specification, test data and test results |
| Đặc điểm thiết kế | Design specification |
| Hướng dẫn quản trị, hướng dẫn sử dụng | Administrative guide, user guide |
| Môi trường nghiệm thu, sản xuất; tiện ích di chuyển dữ liệu | Acceptance testing, production environment, data migration utility |
| Mã nguồn | Source code |
| Kế hoạch phát triển (lịch trình/kế hoạch phát hành sơ bộ) | Development plan (schedule/preliminary release plan) |

### Tiến hành cuộc họp khởi động dự án \[3\] (Conduct Project Blastoff Meeting)

- Blastoff còn được gọi là "bắt đầu dự án", "khởi động", "điều lệ", "khởi động dự án" và nhiều tên khác.
  *(Blastoff is also known as "project initiation," "kickoff," "charter," "project launch," and many other things.)*
- Cuộc họp khởi công chuẩn bị dự án và đảm bảo tính khả thi trước khi đưa ra nỗ lực yêu cầu chi tiết.
  *(The blastoff meeting prepares the project and ensures its feasibility before launching the detailed requirements effort.)*

---

## Tài liệu tham khảo (References)

1. Karl Wiegers và Joy Beatty (2013). *Software Requirements*. Microsoft Press.
2. Alan R. Hevner và cộng sự. (2004). *Design Science in Information Systems Research*.
3. Suzanne Robertson và James Robertson (2012). *Mastering the Requirements Process*. Addison Wesley Professional.
4. Michael Keeling (2017). *Design It: From Programmer to Software Architect*. Pragmatic Bookshelf.
5. Joy Beatty và Anthony Chen (2012). *Visual Models for Software Requirements*. Microsoft Press.
