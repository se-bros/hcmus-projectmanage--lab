# Giới thiệu về Ước tính Phần mềm (Introduction to Software Estimation)

**Giảng viên / Lecturer:** Ngô Huy Biên (Ngo Huy Bien) — nhbien@fit.hcmus.edu.vn
**Đơn vị / Department:** Bộ môn Kỹ thuật phần mềm, Khoa Công nghệ thông tin, Trường Đại học Khoa học Tự nhiên, ĐHQG-HCM
**Môn học / Course:** Quản lý Dự án Phần mềm (Software Project Management)

---

## 1. Mục tiêu bài học (Learning Objectives)

Sau bài học, người học có thể:

- Giao tiếp trong lĩnh vực ước tính phần mềm.
  *(Communicate in software estimation field.)*
- Ước tính kích thước và nỗ lực bằng phương pháp đếm, tính toán và đánh giá.
  *(Estimate size and effort using counting, computing, and judging method.)*
- Ước tính kích thước và nỗ lực bằng phương pháp tương tự.
  *(Estimate size and effort using analogy method.)*
- Ước tính kích thước và nỗ lực bằng phương pháp đánh giá chuyên gia có cấu trúc.
  *(Estimate size and effort using structured expert judgment method.)*

## 2. Nội dung (Contents Overview)

| # | Chủ đề (VI) | Topic (EN) |
|---|---|---|
| I | Ước tính phần mềm là gì? | What is Software Estimation? |
| II | Đo kích thước phần mềm | Measuring Software Size |
| III | Ước tính so với Cam kết | Estimate vs. Commitment |
| IV | Hình nón bất định | Cone of Uncertainty |
| V | Phương pháp Đếm, Tính, Đánh giá | Count, Compute, Judge Method |
| VI | Ước tính bằng Tương tự | Estimation by Analogy |
| VII | Đánh giá chuyên gia có cấu trúc | Structured Expert Judgment |
| VIII | Ước tính theo dãy giá trị & PERT | Range Estimation & PERT |
| IX | Thực tiễn tốt nhất | Best Practices |

---

## I. Ước tính phần mềm là gì? (What is Software Estimation?) \[1\]

> Ước tính phần mềm là hành động dự đoán kích thước, thời gian và chi phí của một dự án.
> *(Software estimation is the act of predicting size, duration and cost of a project.)*

**Ai cần ước tính phần mềm?**
Người quản lý dự án, Khách hàng, Kiến trúc sư, Nhà phát triển, Người kiểm tra, Nhà nghiên cứu.

**Bài toán thực tế:**
- Khi có yêu cầu tương đối tốt (25 use case hoặc 80 user story), sẽ mất bao lâu để phát triển hệ thống?
- Chi phí là bao nhiêu?
- Cần bao nhiêu người?
- Năng suất của nhóm là bao nhiêu?

---

## II. Đo kích thước phần mềm (Measuring Software Size)

> Bạn không thể lập kế hoạch nếu không thể đo lường, và nếu bạn không lập kế hoạch, bạn đã lên kế hoạch để thất bại.
> *(You cannot plan if you cannot measure, and if you fail to plan, you have planned to fail.)*

### 2.1 Dòng mã nguồn — SLOC (Source Lines of Code)

SLOC là số liệu phần mềm dùng để đo lượng mã trong một chương trình.
*(Source lines of code — SLOC is a software metric used to measure the amount of code in a program.)*

| Biến thể SLOC | Mô tả |
|---|---|
| **LOC / SLOC vật lý** *(Physical SLOC)* | Tổng số dòng mã vật lý |
| **SLOC logic** | Không có dòng trống, không bình luận; KLOC = 1000×LOC |
| **ELOC / DSI** | Chỉ dòng tạo ra lệnh thực thi, loại trừ khai báo dữ liệu |
| **ESLOC** | SLOC đã điều chỉnh theo lượng làm lại cần thiết |

**Ưu điểm:** Dễ hiểu, dễ đếm; tương quan tốt với chức năng và nỗ lực; có thể dẫn xuất các số liệu khác (năng suất = SLOC/nhân viên×tháng; chất lượng = lỗi/SLOC).

**Nhược điểm:** Không có SLOC tồn tại ở giai đoạn khởi động dự án; ở cấp vi mô có thể gây hiểu nhầm.

### 2.2 Các số liệu kích thước khác

- **Story point** *(Điểm câu chuyện)*
- **Function Points (FP)** — đo lường chức năng được cung cấp từ góc độ người dùng *(measure the delivered functionality from user perspective)*
- **Use case points, Object points**

### 2.3 Mục đích đo kích thước phần mềm

- Chuẩn bị đề xuất *(Request for proposals)*
- Đàm phán hợp đồng *(Contract negotiations)*
- Lập kế hoạch và tiến độ *(Planning and scheduling)*
- Giám sát và kiểm soát: Năng suất = Kích thước / Thời gian; Chất lượng = Lỗi / Kích thước
  *(Monitoring and control: productivity = size/time; quality = defects/size)*

---

## III. Ước tính so với Cam kết (Estimate vs. Commitment)

| Khái niệm | Định nghĩa |
|---|---|
| **Ước tính (Estimate)** | Dự đoán về thời gian dự án sẽ thực hiện hoặc chi phí bao nhiêu. *(A prediction of how long a project will take or how much it will cost.)* |
| **Mục tiêu (Target)** | Tuyên bố về một mục tiêu kinh doanh mong muốn. *(A statement of a desirable business objective.)* |
| **Cam kết (Commitment)** | Lời hứa cung cấp chức năng được xác định ở chất lượng cụ thể vào ngày nhất định. *(A promise to deliver defined functionality at a specific level of quality by a certain date.)* |

> **Đừng giả định cam kết phải giống với ước tính.**
> *(Do not assume that the commitment has to be the same as the estimate.)*

**Tại sao cần ước tính phần mềm?**
- Xác định liệu các mục tiêu dự án có đủ thực tế để cho phép kiểm soát dự án đạt được chúng hay không.
  *(To determine whether a project's targets are realistic enough to allow the project to be controlled to meet them.)*
- Được sử dụng để thực hiện cam kết.

---

## IV. Hình nón bất định (Cone of Uncertainty)

Hình nón bất định mô tả khoảng biến thiên của ước tính qua các giai đoạn dự án.

**Nguyên tắc:**
- Hình nón không tự thu hẹp. Nếu dự án không được kiểm soát tốt hoặc người ước tính thiếu kỹ năng, ước tính có thể không cải thiện.
  *(The Cone doesn't narrow itself. If the project is not well controlled or estimators aren't skilled, estimates can fail to improve.)*
- Hình nón chỉ thu hẹp khi bạn đưa ra những quyết định loại bỏ sự biến thiên.
  *(The Cone narrows only as you make decisions that eliminate variability.)*
- Những cam kết có ý nghĩa không thể thực hiện được ngay từ đầu, khi hình nón vẫn còn rộng.
  *(Meaningful commitments are not possible in the early, wide part of the Cone.)*

**Trong phát triển lặp (IID) \[2\]:**
- Bạn sẽ trải qua một hình nón thu nhỏ trong mỗi lần lặp.
  *(You'll go through a miniature Cone on each iteration.)*
- Việc để yêu cầu không xác định đến đầu mỗi lần lặp mất đi khả năng dự báo dài hạn.
- Lựa chọn thay thế: Ít lặp hơn (Phân phối theo giai đoạn) hoặc Lặp khác nhau (RUP).

---

## V. Phương pháp Đếm, Tính, Đánh giá (Count, Compute, Judge) \[1\]

> Đếm nếu có thể. Tính toán khi bạn không thể đếm. Chỉ sử dụng sự phán xét như là phương sách cuối cùng.
> *(Count if at all possible. Compute when you can't count. Use judgment alone only as a last resort.)*

### 5.1 Bước 1: Quyết định cần đếm gì

Tìm thứ có sẵn sớm hơn và có thể đếm với nỗ lực tối thiểu:

| Đối tượng đếm | Dữ liệu lịch sử tương ứng |
|---|---|
| Yêu cầu tiếp thị *(Marketing requirements)* | Số giờ nỗ lực trung bình cho mỗi yêu cầu |
| Tính năng *(Features)* | Số giờ nỗ lực trung bình cho mỗi tính năng |
| Trường hợp sử dụng *(Use cases)* | Tổng giờ nỗ lực trung bình cho mỗi use case |
| Câu chuyện người dùng *(User stories)* | Tổng giờ nỗ lực trung bình cho mỗi câu chuyện |
| Trang web *(Web pages)* | Nỗ lực trung bình mỗi trang web cho công việc UI |
| Bảng cơ sở dữ liệu *(Database tables)* | Nỗ lực trung bình mỗi bảng |

### 5.2 Bước 2: Chuyển số lượng thành ước tính

Nếu có dữ liệu lịch sử liên quan đến số lượng, chuyển đổi chúng thành ước tính nỗ lực.
Nếu chưa có dữ liệu lịch sử, bắt đầu thu thập càng sớm càng tốt.

**Ví dụ thực tế:** Chuyển đổi website .NET sang JEE
- Đếm: 45 file .aspx với 6.996 dòng mã; 50 file .cs với 12.232 dòng mã
- Đánh giá: Chuyển đổi UI: 20 ngày; Chuyển đổi mã: 30 ngày; Điều tra JEE: 10 ngày

**Công cụ đếm SLOC:**
- VS Code Counter: https://marketplace.visualstudio.com/items?itemName=uctakeoff.vscode-counter
- Count LOC online: https://codetabs.com/count-loc/count-loc-online.html
- Tokei: https://github.com/XAMPPRocky/tokei

---

## VI. Ước tính bằng Tương tự (Estimation by Analogy)

Ước tính bằng cách so sánh với dự án cũ tương tự — đơn giản, chính xác, rẻ và dựa trên đặc tính đã được chứng minh.

**5 bước thực hiện:**

**Bước 1:** Thu thập kích thước chi tiết, nỗ lực và chi phí của dự án cũ.

**Bước 2:** So sánh kích thước hệ thống con của dự án mới với dự án cũ.

| Hệ thống con | Dự án cũ | Dự án mới | Hệ số nhân |
|---|---|---|---|
| Cơ sở dữ liệu | 10 bảng, 5.000 LOC | 14 bảng | 1.4 |
| Giao diện người dùng | 14 trang web, 14.000 LOC | 19 trang web | 1.4 |
| Đồ thị và báo cáo | 10 đồ thị + 8 báo cáo, 9.000 LOC | 14 đồ thị + 16 báo cáo | 1.7 |
| Lớp cơ bản | 15 lớp, 4.500 LOC | 15 lớp | 1.0 |
| Quy tắc kinh doanh | ??? LOC, 11.000 LOC | ??? | 1.5 |
| **Tổng** | **43.500 LOC** | **62.900 LOC** | — |

**Bước 3:** Tính kích thước ước tính cho dự án mới (43.500 × hệ số từng hệ thống con = 62.900 LOC).

**Bước 4:** Tạo ước tính nỗ lực:
- Tỷ lệ kích thước = 62.900 / 43.500 = 1.45
- Nỗ lực ước tính = 1.45 × 30 tháng nhân công = **44 tháng nhân công**

**Bước 5:** Kiểm tra giả định nhất quán giữa dự án cũ và mới (công nghệ, thành viên nhóm, loại phần mềm...).

**Ưu và nhược điểm:**
- ✅ Đơn giản, chính xác, rẻ; dựa trên đặc tính đã được chứng minh.
- ❌ Không thể thực hiện nếu không có dự án tương tự; cần xác định biến quan trọng nhất.

---

## VII. Đánh giá chuyên gia có cấu trúc (Structured Expert Judgment)

- "Đánh giá trực quan của chuyên gia" có xu hướng không chính xác.
  *("Intuitive expert judgment" tends to be inaccurate.)*
- "Đánh giá chuyên môn có cấu trúc" có thể tạo ra ước tính chính xác như ước tính dựa trên mô hình.
  *("Structured expert judgment" can produce estimates that are about as accurate as model-based estimates.)*

**Ai tạo ra ước tính?** Để tạo ước tính cấp nhiệm vụ, hãy để những người thực sự sẽ thực hiện công việc tạo ra ước tính.
*(To create the task-level estimates, have the people who will actually do the work create the estimates.)*

### 7.1 Ước tính bằng phân tách (Estimation by Decomposition)

Phân tách theo WBS dựa trên hoạt động, bao gồm các loại công việc: Tạo/Thực hiện, Kế hoạch, Quản lý, Đánh giá, Làm lại, Báo cáo, Lỗi.

**Mức độ chi tiết của nhiệm vụ (Task Granularity):**
- Một trong những cách tốt nhất để cải thiện độ chính xác là tách nhiệm vụ lớn thành nhiệm vụ nhỏ hơn.
  *(One of the best ways to improve the accuracy is to separate large tasks into smaller tasks.)*
- Phân tách ước tính thành nhiệm vụ không quá **2 ngày nỗ lực**; ước tính ở mức 1/4 ngày, 1/2 ngày hoặc cả ngày là phù hợp.
  *(Decompose estimates into tasks requiring no more than about 2 days of effort.)*
- Cần từ 5 đến 10 mục riêng lẻ để hưởng lợi từ Luật Số Lớn.
  *(You need 5 to 10 individual items before getting much benefit from the Law of Large Numbers.)*

### 7.2 Vấn đề ước tính trường hợp tốt nhất

Khi nhà phát triển được yêu cầu cung cấp ước tính điểm đơn, họ thường vô thức đưa ra ước tính Trường hợp Tốt nhất.

Nếu mỗi tính năng có P(hoàn thành đúng hạn) = 0.25 (không tệ), thì:
P(tất cả 10 tính năng hoàn thành đúng hạn) = 0.25^10 = 0.000095% (cực kỳ nhỏ)

**Giải pháp:** Điều chỉnh ước tính để phản ánh xác suất 50% hoặc sử dụng dãy giá trị.

---

## VIII. Ước tính theo dãy giá trị & PERT (Range Estimation & PERT)

### 8.1 Ước tính theo dãy giá trị (Use of Ranges)

Thay vì ước tính điểm đơn, sử dụng dãy giá trị: Trường hợp tốt nhất (Best Case) và Trường hợp xấu nhất (Worst Case).

### 8.2 Công thức PERT (Program Evaluation and Review Technique)

Trong nhiều trường hợp, Trường hợp xấu nhất tệ hơn nhiều so với Trường hợp dự kiến. Lấy trung điểm của dãy có thể dẫn đến ước tính quá cao.

**Công thức Trường hợp dự kiến (Expected Case):**

```
Expected Case = (Optimistic + 4 × Most Likely + Pessimistic) / 6
```

*(Trường hợp dự kiến = (Lạc quan + 4 × Khả năng xảy ra cao nhất + Bi quan) / 6)*

**Ước tính trường hợp Dự kiến có thể được ở mức % tin cậy (Percentage Confident):**

| Mức tin cậy | Công thức |
|---|---|
| 10% | Expected − 1.28 × SD |
| 50% | Expected Case |
| 75% | Expected + 0.67 × SD |
| 80% | Expected + 0.84 × SD |
| 90% | Expected + 1.28 × SD |

*(SD = Standard Deviation = Độ lệch chuẩn)*

### 8.3 Danh sách kiểm tra ước tính cá nhân

- Những gì được ước tính có được xác định rõ ràng không? *(Is what's being estimated clearly defined?)*
- Ước tính có bao gồm tất cả các loại công việc cần thiết? *(Does the estimate include all the kinds of work needed?)*
- Ước tính có bao gồm tất cả các vùng chức năng cần thiết? *(Does the estimate include all the functionality areas needed?)*
- Ước tính có được chia thành đủ chi tiết để lộ công việc ẩn? *(Is the estimate broken down enough to expose hidden work?)*
- Bạn có xem xét dữ liệu ghi chép từ công việc trước, thay vì ước tính thuần túy từ trí nhớ? *(Did you look at documented facts from past work rather than estimating purely from memory?)*
- Ước tính có được phê duyệt bởi người thực sự sẽ làm việc? *(Is the estimate approved by the person who will actually do the work?)*

### 8.4 So sánh ước tính với thực tế (MRE)

- Giữ danh sách ước tính và điền kết quả thực tế khi hoàn thành.
- Tính toán Độ lớn của Sai số Tương đối *(Magnitude of Relative Error — MRE)*.
- Hiểu điều gì đúng, điều gì sai, điều gì bỏ qua để cải thiện ước tính trong tương lai.

---

## IX. Thực tiễn tốt nhất (Best Practices)

- Sử dụng nhiều hơn một kỹ thuật ước tính.
  *(Using more than one estimation technique.)*
- Bao gồm tác động rủi ro trong ước tính.
  *(Including risk impact.)*
- Từ trên xuống vs. Từ dưới lên \[1\]:
  - **Từ dưới lên (Bottom-Up):** Bắt đầu ở cấp thành phần, ước tính nỗ lực từng thành phần, cộng lại. Có thể sử dụng khi kiến trúc và thành phần đã biết; có thể đánh giá thấp chi phí cấp hệ thống như tích hợp và tài liệu.
  - **Từ trên xuống (Top-Down):** Bắt đầu ở cấp hệ thống, đánh giá chức năng tổng thể và phân phối qua các hệ thống con. Có thể sử dụng mà không cần biết kiến trúc; có thể đánh giá thấp chi phí vấn đề kỹ thuật cấp thấp.

**Lưu ý: Kỹ thuật "Price to Win":**
> "Kỹ thuật giá để thắng đã giành được một số lượng lớn hợp đồng phần mềm cho nhiều công ty. Hầu như tất cả đều ngừng hoạt động ngày hôm nay." — Boehm 81, trang 337.
> *("The price-to-win technique has won a large number of software contracts for a large number of software companies. Almost all of them are out of business today.")*

Phần mềm có thể được định giá (ước tính) để giành hợp đồng và chức năng điều chỉnh theo giá — đây là rủi ro lớn cần tránh.

---

## Tài liệu tham khảo (References)

1. Steve McConnell (2006). *Software Estimation: Demystifying the Black Art*. Microsoft Press.
2. Jonathan Rasmusson (2010). *The Agile Samurai: How Agile Masters Deliver Great Software*. Pragmatic Bookshelf.
