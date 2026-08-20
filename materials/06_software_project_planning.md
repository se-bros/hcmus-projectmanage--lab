# Lập kế hoạch dự án phần mềm (Software Project Planning)

**Giảng viên / Lecturer:** Ngô Huy Biên (Ngo Huy Bien) — nhbien@fit.hcmus.edu.vn
**Đơn vị / Department:** Bộ môn Kỹ thuật phần mềm, Khoa Công nghệ thông tin, Trường Đại học Khoa học Tự nhiên, ĐHQG-HCM
**Môn học / Course:** Quản lý Dự án Phần mềm (Software Project Management)

---

## 1. Mục tiêu bài học (Learning Objectives)

Sau bài học, người học có thể:

- Tạo một lịch trình dự án.
  _(Create a project schedule.)_
- Tính toán ngân sách dự án.
  _(Calculate a project budget.)_
- Tạo một tuyên bố về công việc (Statement of Work — SOW).
  _(Create a statement of work.)_
- Tạo một hợp đồng phần mềm.
  _(Create a software contract.)_
- Tạo một kế hoạch dự án.
  _(Create a project plan.)_

## 2. Nội dung (Contents Overview)

| #   | Chủ đề (VI)              | Topic (EN)              |
| --- | ------------------------ | ----------------------- |
| I   | Tiến độ dự án            | Project Schedule        |
| II  | Ngân sách dự án          | Project Budget          |
| III | Tuyên bố công việc (SOW) | Statement of Work (SOW) |
| IV  | Hợp đồng phần mềm        | Software Contract       |
| V   | Kế hoạch dự án           | Project Plan            |

---

## I. Tiến độ dự án (Project Schedule)

### 1.1 Khái niệm cơ bản: Nỗ lực so với Thời lượng \[1\]

**Bài toán thực tế:**

- Khi có yêu cầu tương đối tốt (ví dụ: 25 use case), sẽ mất bao lâu để phát triển hệ thống?
- Chi phí là bao nhiêu?
- Cần bao nhiêu người?

| Thuật ngữ                                | Định nghĩa                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ---------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Nỗ lực (Effort)**                      | Số lượng đơn vị lao động cần thiết để hoàn thành một hoạt động tiến độ hoặc một thành phần WBS, thường được biểu thị bằng giờ công (người-giờ), ngày công hoặc tuần công.<br>_(The number of labor units required to complete a schedule activity or WBS component, often expressed in man-hours (person-hours), man-days, or man-weeks.)_                                                                                  |
| **Thời lượng (Duration - DU/DUR)**       | Tổng số thời gian làm việc (không tính ngày nghỉ hoặc thời gian không làm việc khác) cần thiết để hoàn thành một hoạt động tiến độ hoặc một thành phần WBS, thường được biểu thị bằng ngày làm việc hoặc tuần làm việc.<br>_(The total number of work periods (not including holidays or other nonworking periods) required to complete a schedule activity or WBS component. Usually expressed as workdays or workweeks.)_ |
| **Thời gian đã trôi qua (Elapsed Time)** | Tổng thời gian thực tế trôi qua từ lúc bắt đầu đến lúc kết thúc (bao gồm cả ngày nghỉ, ngày lễ và thời gian không làm việc).<br>_(The total calendar time elapsed from start to finish, including weekends and holidays.)_                                                                                                                                                                                                  |

### 1.2 Biểu đồ Gantt (Gantt Charts)

> Biểu đồ Gantt thể hiện thông tin lịch trình, trong đó các hoạt động được liệt kê trên trục dọc, ngày tháng được hiển thị trên trục ngang, và thời lượng hoạt động được thể hiện dưới dạng các thanh ngang được đặt theo ngày bắt đầu và kết thúc.
> _(Gantt charts represent schedule information where activities are listed on the vertical axis, dates are shown on the horizontal axis, and activity durations are shown as horizontal bars placed according to start and finish dates.)_

### 1.3 Các bước tạo biểu đồ Gantt

#### Bước 1: Xác định hoạt động (Define Activities)

Là quá trình xác định và ghi lại các hành động cụ thể cần thực hiện để tạo ra các sản phẩm bàn giao của dự án.
_(Identifying and documenting the specific actions to be performed to produce the project deliverables.)_

- **Đầu vào (Inputs):** WBS dự án, sản phẩm bàn giao, ràng buộc và giả định.
- **Kỹ thuật (Techniques):** Phân rã (Decomposition), Phán quyết của chuyên gia (Expert Judgment), Lập kế hoạch làn sóng cuốn (Rolling Wave Planning).
- **Đầu ra (Outputs):** Danh sách hoạt động (Activity List), Thuộc tính hoạt động (Activity Attributes), Danh sách cột mốc (Milestone List).

_Danh sách hoạt động (Activity List)_ là một danh sách toàn diện bao gồm tất cả các hoạt động theo tiến độ cần thiết trong dự án cùng mã định danh và mô tả phạm vi công việc đủ chi tiết để các thành viên hiểu rõ.

#### Bước 2: Xác định sự phụ thuộc (Determine Dependencies)

- **Sự phụ thuộc nội bộ (Internal dependencies):** Mối quan hệ ưu tiên giữa các hoạt động trong dự án.
- **Sự phụ thuộc bên ngoài (External dependencies):** Mối quan hệ giữa hoạt động dự án và các hoạt động phi dự án.
- **Sự phụ thuộc bắt buộc (Mandatory dependencies):** Các ràng buộc bắt buộc theo luật pháp, hợp đồng hoặc do bản chất tự nhiên của công việc.
- **Sự phụ thuộc tùy ý (Discretionary dependencies):** Còn gọi là logic ưu tiên (preferred/preferential logic) hoặc logic mềm (soft logic), được thiết lập dựa trên kiến thức về các thực tiễn tốt nhất (best practices).

#### Bước 3: Xác định mối quan hệ logic (Identify Logical Relationships)

- **Hoạt động tiền nhiệm (Predecessor activity):** Hoạt động diễn ra trước một cách logic trong lịch trình.
- **Hoạt động kế nhiệm (Successor activity):** Hoạt động phụ thuộc diễn ra sau một hoạt động khác một cách logic.
- **Mối quan hệ Kết thúc - Bắt đầu (Finish-to-Start):** Loại quan hệ ưu tiên được sử dụng phổ biến nhất. Quan hệ Bắt đầu - Kết thúc (Start-to-Finish) rất hiếm khi được sử dụng.

#### Bước 4: Danh sách cột mốc (Milestone List)

- Cột mốc là một điểm hoặc sự kiện quan trọng trong dự án, có **thời lượng bằng 0** vì nó đại diện cho một thời điểm cụ thể.
  _(A milestone is a significant point or event in a project, having zero duration because it represents a moment in time.)_

#### Bước 5: Hoạt động tuần tự (Sequence Activities)

Quy trình xác định và ghi lại các mối quan hệ giữa các hoạt động dự án nhằm đạt hiệu quả cao nhất dưới các ràng buộc.
_(The process of identifying and documenting relationships among the project activities to obtain the greatest efficiency.)_

- **Kỹ thuật:** Phương pháp lập sơ đồ ưu tiên — PDM (Precedence Diagramming Method) vẽ dưới dạng Hoạt động trên nút — AON (Activity-On-Node) hoặc Hoạt động trên mũi tên (Activity-On-Arrow), cùng các kỹ thuật dẫn đầu và độ trễ (Leads and Lags).
- **Đầu ra:** Sơ đồ mạng lưới tiến độ dự án (Project Schedule Network Diagram).

#### Bước 6: Ước tính tài nguyên hoạt động (Estimate Activity Resources)

Ước tính loại và số lượng vật liệu, nhân lực, thiết bị cần thiết cho mỗi hoạt động.
_(Estimating the type and quantities of material, human resources, equipment, or supplies required to perform each activity.)_

- **Đầu ra:** Yêu cầu nguồn lực hoạt động (Activity Resource Requirements), Cấu trúc phân chia tài nguyên — RBS (Resource Breakdown Structure — thể hiện có thứ bậc của tài nguyên theo danh mục và loại).

#### Bước 7: Ước tính thời lượng hoạt động (Estimate Activity Durations)

Ước tính số đơn vị thời gian cần thiết để hoàn thành hoạt động với các tài nguyên đã ước tính.
_(Estimating the number of work periods needed to complete individual activities with estimated resources.)_

**Các kỹ thuật ước tính:**

1. **Phán quyết của chuyên gia (Expert Judgment):** Dựa trên dữ liệu lịch sử và kinh nghiệm.
2. **Ước tính tương tự / Từ trên xuống (Analogous / Top-down Estimating):** Dùng nỗ lực thực tế từ dự án cũ tương tự.
3. **Ước tính tham số (Parametric Estimating):** Phương pháp định lượng bằng cách nhân khối lượng công việc với định mức năng suất.
4. **Ước tính ba điểm (Three-Point Estimates):**
   - Phân phối tam giác (Triangular Distribution): $t_E = \frac{t_O + t_M + t_P}{3}$
   - Phân phối Beta / PERT truyền thống (Beta Distribution): $t_E = \frac{t_O + 4t_M + t_P}{6}$
5. **Phân tích dự trữ (Reserve Analysis):** Thêm nỗ lực dự phòng (buffer) để đối phó rủi ro.

#### Bước 8: Chọn công cụ lập tiến độ (Scheduling Tool)

Sử dụng các phần mềm chuyên dụng như MS Project, GanttProject, GanttPRO, Smartsheet để mô hình hóa tiến độ.

- **Mô hình tiến độ (Schedule Model):** Đại diện động cho kế hoạch thực hiện dự án (gồm việc gì, ai làm, và khi nào).
- **Phiên bản mô hình tiến độ (Schedule Model Instance):** Bản sao của mô hình tiến độ được cập nhật thực tế và lưu trữ để tham chiếu.

#### Bước 9: Phát triển tiến độ (Develop Schedule)

Quá trình phân tích trình tự hoạt động, thời lượng, yêu cầu tài nguyên để tạo ra mô hình tiến độ dự án hoàn chỉnh.

**Phương pháp Đường dẫn quan trọng (Critical Path Method — CPM):**

- **Đường dẫn quan trọng (Critical Path):** Chuỗi các hoạt động đại diện cho con đường dài nhất xuyên qua dự án, quyết định thời gian ngắn nhất có thể để hoàn thành dự án.
- Bất kỳ sự chậm trễ nào trên các hoạt động thuộc đường dẫn quan trọng sẽ làm chậm trễ toàn bộ dự án.
- **Tổng thời gian dự phòng (Total Float / Slack):** Khoảng thời gian một hoạt động có thể bị chậm trễ mà không làm chậm ngày kết thúc dự án:
  $$\text{Total Float} = LF - EF \text{ (hoặc } LS - ES\text{)}$$
  _(Tất cả hoạt động trên đường găng đều có Total Float bằng 0)._
- **Thời gian dự phòng tự do (Free Float):** Khoảng thời gian một hoạt động có thể bị chậm trễ mà không làm ảnh hưởng đến ngày bắt đầu sớm của hoạt động kế tiếp:
  $$\text{Free Float} = \text{ES của hoạt động kế tiếp} - EF - 1$$

- **Phương pháp Chuỗi quan trọng (Critical Chain Method — CCM):** Đặt các vùng đệm thời gian (buffers) phi công việc trên các đường dẫn tiến độ để quản lý các hạn chế về tài nguyên và sự không chắc chắn của dự án.

#### Bước 10: Quản lý tài nguyên và nén lịch trình

- **San lấp tài nguyên (Resource Leveling):** Điều chỉnh ngày bắt đầu/kết thúc dựa trên các hạn chế về nguồn lực để cân bằng nhu cầu và nguồn cung (thường làm tăng thời gian dự án và thay đổi đường găng).
- **Làm mịn tài nguyên (Resource Smoothing):** Điều chỉnh hoạt động sao cho yêu cầu tài nguyên không vượt quá giới hạn định trước mà không làm thay đổi đường găng và ngày hoàn thành dự án (chỉ trì hoãn hoạt động trong phạm vi slack).
- **Dẫn đầu và Độ trễ (Leads and Lags):**
  - Dẫn đầu (Lead): Đẩy hoạt động kế tiếp bắt đầu sớm hơn.
  - Độ trễ (Lag): Trì hoãn hoạt động kế tiếp bắt đầu muộn hơn.
- **Nén tiến độ (Schedule Compression):** Rút ngắn thời gian dự án mà không giảm phạm vi:
  - **Crashing:** Thêm tài nguyên để rút ngắn thời gian với chi phí tăng thêm thấp nhất (ví dụ: làm thêm giờ, bổ sung người).
  - **Fast tracking:** Thực hiện song song các hoạt động thông thường phải làm tuần tự (làm tăng rủi ro làm lại).

---

## II. Ngân sách dự án (Project Budget)

### 2.1 Ước tính chi phí (Estimate Costs)

Quá trình phát triển một ước lượng các nguồn lực tiền tệ cần thiết để hoàn thành các hoạt động của dự án.
_(The process of developing an approximation of the monetary resources needed to complete project activities.)_

**Các yếu tố chi phí hoạt động:**

- **Chi phí nỗ lực (Effort costs):** Yếu tố chi phối lớn nhất, gồm lương kỹ sư, chi phí phúc lợi xã hội và bảo hiểm. Phải tính thêm chi phí chung (overheads).
- Chi phí phần cứng và phần mềm.
- Chi phí vận hành văn phòng, sưởi ấm, chiếu sáng, mạng lưới và truyền thông.
- Chi phí cơ sở vật chất dùng chung (thư viện, nhà ăn, v.v.).
- Chi phí đi lại và đào tạo.
- Chi phí hỗ trợ kỹ thuật và bảo trì.

### 2.2 Xác định ngân sách (Determine Budget)

Quá trình tổng hợp ước tính chi phí của các hoạt động riêng lẻ hoặc các gói công việc để thiết lập một đường cơ sở chi phí được phê duyệt (authorized cost baseline).
_(Aggregating the estimated costs of individual activities or work packages to establish an authorized cost baseline.)_

> **Lưu ý:** Không có mối quan hệ tuyến tính đơn giản giữa giá bán của hệ thống và chi phí phát triển thực tế của nó.
> _(There is no simple relationship between the price charged for a system and its development costs.)_

**Mẫu Dự toán dự án (Project Estimate Template):**

- Tên dự án, ngày bắt đầu, ngày kết thúc.
- Tổng nỗ lực (ngày công), thời lượng (ngày), chi phí (USD).
- Danh sách các mốc quan trọng (Milestones) kèm thời gian và mô tả sản phẩm bàn giao.

---

## III. Tuyên bố công việc (Statement of Work — SOW)

> Tuyên bố công việc (SOW) là bản mô tả chính thức bằng văn bản về các yêu cầu tối thiểu mà nhà thầu phải thực hiện. SOW nói về **CÁI GÌ (WHAT)** cần làm, không nói về **CÁCH NÀO (HOW)** thực hiện.
> _(SOW is a formal written description of your minimum requirements to be performed by a contractor. It specifies WHAT to do, not HOW.)_

**Các thành phần chính của một SOW:**

1. Mục đích và mục tiêu bài học (Purpose and learning objectives)
2. Phạm vi công việc (Scope of work)
3. Vị trí thực hiện công việc (Location of work)
4. Thời hạn thực hiện (Period of performance)
5. Thiết kế đề xuất, giao diện và quy trình (Proposed designs, UIs, workflows)
6. Các giả định (Assumptions)
7. Danh mục sản phẩm bàn giao và tiến độ (Deliverables schedule)
8. Tiêu chuẩn áp dụng (Applicable standards)
9. Tiêu chí nghiệm thu (Acceptance criteria)
10. Quy trình quản lý thay đổi (Change management process)
11. Thỏa thuận dịch vụ chuyên nghiệp (Professional services agreement)
12. Các yêu cầu chuyên biệt (Specialized requirements)

**Lợi ích của SOW:** Cung cấp sự hiểu biết rõ ràng về các yêu cầu; thiết lập cơ sở để đánh giá hồ sơ đề xuất; giảm thiểu thời gian đàm phán; hạn chế các yêu cầu thay đổi trong tương lai.

---

## IV. Hợp đồng phần mềm (Software Contract)

Hợp đồng phần mềm là thỏa thuận phát triển phần mềm tùy chỉnh quy định các quyền và trách nhiệm của lập trình viên (nhà cung cấp) và khách hàng.
_(A custom-software development agreement that stipulates the rights and responsibilities of the vendor and the customer.)_

**Các điều khoản thông thường:** Xác định các bên, hình thức thanh toán, chi phí phát sinh, phí trễ hạn, thay đổi phạm vi, xử lý chậm trễ, đào tạo, hỗ trợ và bảo trì, bảo hành, trách nhiệm pháp lý.

### 4.1 Hợp đồng giá cố định (Fixed-Price Contract)

Phù hợp khi các yêu cầu được xác định chi tiết và rõ ràng. Nếu yêu cầu quá mơ hồ, nên chia làm hai giai đoạn hợp đồng (giai đoạn phân tích/thiết kế ban đầu và giai đoạn triển khai sau đó).

### 4.2 Hợp đồng thời gian và vật liệu (Time and Materials Contract)

Khách hàng trả tiền theo chi phí lao động thực tế dựa trên đơn giá giờ đã thỏa thuận và chi phí vật tư/thiết bị thực tế cộng với lợi nhuận cố định của nhà thầu. Đòi hỏi sự tin tưởng lẫn nhau cao giữa khách hàng và nhà phát triển.

### 4.3 Khi nào nên ký hợp đồng giá cố định? \[4\]

Chỉ ký kết khi nhóm của bạn:

- Có thể xác định đầy đủ, ước tính và lập kế hoạch chi tiết cho dự án.
- Hiểu rõ về nghiệp vụ (domain) và công nghệ sử dụng.
- Có khả năng phân rã tốt nếu dự án lớn (> 1 năm).
- Kiểm soát tốt chi phí giao tiếp (nhóm > 50 người).
- Các thành viên có kinh nghiệm làm việc cùng nhau trước đó.

### 4.4 Các mẹo bán hàng và triển khai thực tế

**Mẹo 1: Đừng chỉ phản hồi RFP (Request for Proposal)**

- RFP thường không đầy đủ và có thể được viết với sự hỗ trợ của đối thủ cạnh tranh của bạn (nhằm định hướng giải pháp của họ). Hãy tiếp cận và tìm hiểu sâu hơn thay vì chỉ trả lời rập khuôn.

**Mẹo 2: Mối quan hệ làm việc quan trọng hơn hợp đồng**

- Hợp đồng giá cố định là thỏa thuận mang lại lợi ích cho cả hai bên. Giao tiếp tốt, sự tin tưởng lẫn nhau và cam kết giải quyết vấn đề phát sinh mới là chìa khóa thành công.

**Mẹo 3: Đừng bỏ thầu quá thấp (Underbid)**

- Tránh việc cố tình giảm giá sâu để giành dự án rồi tìm cách bù lỗ bằng các yêu cầu thay đổi (change requests) phát sinh sau đó.

**Mẹo 4: Bổ sung khoảng đệm thời gian (Slack) để quản lý rủi ro**

- Luôn thêm từ 10% (dự án ngắn, dễ đoán, khách hàng chuyên nghiệp) đến 30% (dự án nhiều biến động) vào ước tính ban đầu để phòng ngừa các yếu tố bất khả kháng (nhân sự ốm đau, sự cố kỹ thuật, khách hàng chậm trễ cam kết).

**Mẹo 5: Đồng thiết lập yêu cầu kinh doanh thực tế**

- Viết tài liệu đặc tả cùng với khách hàng. Đảm bảo mỗi tính năng/user story: được cả hai bên hiểu rõ (không dùng thuật ngữ kỹ thuật quá phức tạp), mang lại giá trị kinh doanh thực tế, và khách hàng có thể tự kiểm chứng nghiệm thu được.

---

## V. Kế hoạch dự án (Project Plan) \[5\]

> Kế hoạch dự án giống như một bản đồ giúp định hướng cho nhóm trong suốt hành trình phức tạp của dự án phần mềm.
> _(The software project plan is a map that defines the software engineering work to guide the team as it makes the journey.)_

**Các thành phần của kế hoạch dự án:** Sản phẩm công việc cần tạo (SOW), nhiệm vụ kỹ thuật cần thực hiện (POC, kiến trúc), tài nguyên yêu cầu (ngân sách, nhân sự), tiến độ làm việc, và các rủi ro có thể xảy ra.

### 5.1 Nguyên lý W5HH (The W5HH Principle)

Bất kỳ kế hoạch dự án nào cũng phải trả lời được các câu hỏi cốt lõi sau:

| Câu hỏi       | Ý nghĩa                                                                                                                                                             |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Why?**      | Tại sao hệ thống được phát triển? (Lý do và lợi ích kinh doanh)<br>_(Why is the system being developed?)_                                                           |
| **What?**     | Điều gì sẽ được thực hiện? (Mục tiêu sản phẩm)<br>_(What will be done?)_                                                                                            |
| **When?**     | Khi nào nó sẽ được thực hiện? (Các cột mốc và tiến độ thời gian)<br>_(When will it be done?)_                                                                       |
| **Who?**      | Ai chịu trách nhiệm cho các chức năng? (Phân công vai trò)<br>_(Who is responsible for a function?)_                                                                |
| **Where?**    | Họ nằm ở đâu về mặt tổ chức?<br>_(Where are they located organizationally?)_                                                                                        |
| **How?**      | Công việc sẽ được thực hiện như thế nào về mặt kỹ thuật và quản lý? (Chiến lược kỹ thuật và quản trị)<br>_(How will the job be done technically and managerially?)_ |
| **How much?** | Mỗi nguồn lực cần bao nhiêu? (Ước tính nỗ lực, ngân sách, vật tư)<br>_(How much of each resource is needed?)_                                                       |

### 5.2 Tại sao cần lập kế hoạch dự án? \[6\]

- Trả lời các câu hỏi: Nhóm có làm được không? Chi phí bao nhiêu? Khi nào hoàn thành?
- Giảm thiểu sự không chắc chắn (uncertainty).
- Thiết lập niềm tin giữa các bên (trust).
- Giảm thiểu rủi ro (risks).
- Hỗ trợ ra quyết định tốt hơn và truyền tải thông tin hiệu quả trong dự án.

---

## Tài liệu tham khảo (References)

1. Project Management Institute (2017). _A Guide to the Project Management Body of Knowledge_. 6th Edition.
2. Andrew Stellman & Jennifer Greene (2014). _Head First PMP_. 3rd Edition. O'Reilly Media.
3. Project Management Institute (2011). _Practice Standard for Scheduling_. 2nd Edition.
4. Pascal Van Cauwenberghe (2003). _Agile Fixed Price Projects Part 1: The Price is Right_.
5. Roger S. Pressman (2010). _Software Engineering: A Practitioner's Approach_.
6. Mike Cohn (2005). _Agile Estimating and Planning_. Pearson Education.
