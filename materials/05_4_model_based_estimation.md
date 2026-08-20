# Ước tính dựa trên mô hình (Model-Based Estimation)

**Giảng viên / Lecturer:** Ngô Huy Biên (Ngo Huy Bien) — nhbien@fit.hcmus.edu.vn
**Đơn vị / Department:** Bộ môn Kỹ thuật phần mềm, Khoa Công nghệ thông tin, Trường Đại học Khoa học Tự nhiên, ĐHQG-HCM
**Môn học / Course:** Quản lý Dự án Phần mềm (Software Project Management)

---

## 1. Mục tiêu bài học (Learning Objectives)

Sau bài học, người học có thể:

- Ước tính kích thước bằng Điểm chức năng (Function Points).
  _(Estimate size in function points.)_
- Ước tính kích thước bằng Điểm trường hợp sử dụng (Use Case Points).
  _(Estimate size in use case points.)_
- Ước tính kích thước bằng Điểm đối tượng (Object Points).
  _(Estimate size in object points.)_
- Ước tính quy mô, chi phí và tiến độ bằng các mô hình thuật toán.
  _(Estimate size, cost and schedule using algorithmic models.)_

## 2. Nội dung (Contents Overview)

| #   | Chủ đề (VI)                    | Topic (EN)                    |
| --- | ------------------------------ | ----------------------------- |
| I   | Phân tích Điểm chức năng (FPA) | Function Point Analysis (FPA) |
| II  | Điểm trường hợp sử dụng (UCP)  | Use Case Points (UCP)         |
| III | Điểm đối tượng (OP)            | Object Points (OP)            |
| IV  | Phân tích hồi quy              | Regression Analysis           |
| V   | Mô hình COCOMO                 | COCOMO Model                  |
| VI  | Khoa học phần mềm Halstead     | Halstead's Software Science   |
| VII | Đo lường vs. Đánh giá          | Measurement vs. Rating        |

---

## I. Phân tích Điểm chức năng (Function Point Analysis — FPA) \[1, 2, 3\]

> Điểm chức năng (FP) là thước đo phần mềm dùng để đo lường chức năng được cung cấp trong một chương trình từ góc độ người dùng.
> _(Function points — FP is a software metric used to measure the delivered functionality in a program from user perspective.)_

FPA là phương pháp tiêu chuẩn để đo lường phát triển phần mềm từ quan điểm người dùng.

### 1.1 Các bước thực hiện FPA

**Bước 1: Xác định loại tính điểm**

- Điểm chức năng của dự án phát triển mới
- Điểm chức năng của dự án nâng cao
- Số điểm chức năng ứng dụng

**Bước 2: Xác định ranh giới ứng dụng**

**Bước 3: Xác định chức năng dữ liệu**

| Loại                              | Định nghĩa                                                                                                     |
| --------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| **ILF** (Internal Logical File)   | Nhóm dữ liệu có liên quan logic, được nhận dạng bởi người dùng và được duy trì bởi ứng dụng (bảng, tệp phẳng). |
| **EIF** (External Interface File) | Nhóm dữ liệu có liên quan logic, được nhận dạng bởi người dùng và được duy trì bởi ứng dụng khác.              |

**Bước 4: Xác định chức năng giao dịch**

| Loại                        | Định nghĩa                                                                                     |
| --------------------------- | ---------------------------------------------------------------------------------------------- |
| **EI** (External Inputs)    | Hàm hoặc giao dịch chuyển dữ liệu vào ứng dụng (người dùng nhập, ứng dụng bên ngoài cung cấp). |
| **EO** (External Outputs)   | Hàm hoặc giao dịch thao tác và trình bày dữ liệu cho người dùng (báo cáo, hình ảnh).           |
| **EQ** (External Inquiries) | Yêu cầu duy nhất dẫn đến truy xuất dữ liệu (báo cáo, tìm kiếm).                                |

**Bước 5: Xác định độ phức tạp ILF/EIF**

| ILF/EIF | 1-19 DET   | 20-50 DET  | 51+ DET    |
| ------- | ---------- | ---------- | ---------- |
| 1 RET   | Thấp       | Thấp       | Trung bình |
| 2-5 RET | Thấp       | Trung bình | Cao        |
| 6+ RET  | Trung bình | Cao        | Cao        |

_(DET = Data Element Types; RET = Record Element Types)_

**Bước 6: Xác định độ phức tạp EI/EO/EQ**

| EI      | 1-4 DET    | 5-15 DET   | 16+ DET    |
| ------- | ---------- | ---------- | ---------- |
| 0-1 FTR | Thấp       | Thấp       | Trung bình |
| 2 FTR   | Thấp       | Trung bình | Trung bình |
| 3+ FTR  | Trung bình | Cao        | Cao        |

_(FTR = File Types Referenced)_

**Bước 7: Tính điểm chức năng chưa điều chỉnh (UFP)**

| Đặc điểm                       | Thấp | Trung bình | Cao |
| ------------------------------ | ---- | ---------- | --- |
| External Inputs (EI)           | ×3   | ×4         | ×6  |
| External Outputs (EO)          | ×4   | ×5         | ×7  |
| External Queries (EQ)          | ×3   | ×4         | ×6  |
| Internal Logical Files (ILF)   | ×4   | ×10        | ×15 |
| External Interface Files (EIF) | ×5   | ×7         | ×10 |

UFP = Σ(EI FP + EO FP + EQ FP + ILF FP + EIF FP)

**Bước 8: Đánh giá đặc tính chung hệ thống (F1–F14)**

14 đặc tính chung, mỗi đặc tính có giá trị từ 0-5:

| Mã  | Đặc tính                         |
| --- | -------------------------------- |
| F1  | Sao lưu và phục hồi đáng tin cậy |
| F2  | Truyền thông dữ liệu             |
| F3  | Hàm phân tán                     |
| F4  | Hiệu suất                        |
| F5  | Cấu hình được sử dụng nhiều      |
| F6  | Nhập dữ liệu trực tuyến          |
| F7  | Dễ vận hành                      |
| F8  | Cập nhật trực tuyến              |
| F9  | Giao diện phức tạp               |
| F10 | Xử lý phức tạp                   |
| F11 | Khả năng tái sử dụng             |
| F12 | Dễ cài đặt                       |
| F13 | Nhiều trang web                  |
| F14 | Tạo điều kiện thay đổi           |

```text
VAF (Value Adjustment Factor) = 0.65 + 0.01 × Sum(F1, F14)
AFP (Adjusted Function Points) = UFP × VAF
```

**Chuyển đổi FP sang SLOC:**
Số câu lệnh lập trình trên mỗi FP thay đổi theo ngôn ngữ (Java: ~53 SLOC/FP; C: ~128 SLOC/FP; v.v.)

**Ưu và nhược điểm (Pros & Cons):**

- ✅ Độc lập với ngôn ngữ và nền tảng phát triển; tiêu chuẩn ISO; có thể thực thi ở cuối mỗi giai đoạn.
- ❌ Tốn nhiều công sức; yêu cầu đào tạo và kinh nghiệm đáng kể; trọng số được xác định qua tranh luận.

---

## II. Điểm trường hợp sử dụng (Use Case Points — UCP)

### 2.1 Trọng lượng Use Case chưa điều chỉnh (UUCW)

| Loại Use Case  | Tiêu chí                                            | Trọng số |
| -------------- | --------------------------------------------------- | -------- |
| **Đơn giản**   | Giao diện đơn giản, ≤1 bảng DB, ≤3 bước, <5 lớp     | 5        |
| **Trung bình** | Nhiều giao diện hơn, 2+ bảng DB, 4-7 bước, 5-10 lớp | 10       |
| **Phức tạp**   | Giao diện phức tạp, 3+ bảng DB, >7 bước, >10 lớp    | 15       |

### 2.2 Trọng lượng Actor chưa điều chỉnh (UAW)

| Loại Actor     | Mô tả                                | Trọng số |
| -------------- | ------------------------------------ | -------- |
| **Đơn giản**   | Hệ thống khác qua API được xác định  | 1        |
| **Trung bình** | Hệ thống khác qua giao thức (TCP/IP) | 2        |
| **Phức tạp**   | Người dùng tương tác qua giao diện   | 3        |

### 2.3 Hệ số phức tạp kỹ thuật (TCF) và môi trường (ECF)

**Hệ số TCF (13 yếu tố kỹ thuật T1-T13):**

```text
TCF = 0.6 + (0.01 × Tổng hệ số)
```

**Hệ số ECF (8 yếu tố môi trường E1-E8):**

```text
ECF = 1.4 + (-0.03 × Tổng hệ số)
```

### 2.4 Tính Use Case Points điều chỉnh

```text
UUCP = UUCW + UAW
AUCP = UUCP × TCF × ECF
Nỗ lực (người-giờ) = AUCP × PF
```

_(PF = Productivity Factor; giá trị khuyến nghị từ 15-30, điển hình là 20 nếu không có dữ liệu lịch sử)_

**Ưu và nhược điểm:**

- ✅ Có thể thực hiện sớm; đơn giản, nhanh chóng và minh bạch.
- ❌ Thiếu trọng số được chấp nhận rõ ràng.

---

## III. Điểm đối tượng (Object Points — OP)

Hệ thống được phân rã thành:

- Các màn hình được hiển thị _(Screens that are displayed)_
- Các báo cáo do hệ thống tạo ra _(Reports that are produced)_
- Mô-đun 3GL _(3GL modules)_

> **Lưu ý:** Điểm đối tượng KHÔNG giống với các lớp đối tượng.
> _(Object points are NOT the same as object classes.)_

**Bảng trọng số:**

| Loại đối tượng    | Đơn giản | Trung bình | Khó |
| ----------------- | -------- | ---------- | --- |
| Màn hình (Screen) | 1        | 2          | 3   |
| Báo cáo (Report)  | 2        | 5          | 8   |
| Mô-đun 3GL        | 10       | 10         | 10  |

```text
OP = Σ(tất cả phiên bản đối tượng có trọng số)
NOP (New Object Points) = OP × (100 - %Reuse) / 100
```

**Ước tính nỗ lực (COCOMO II — Application composition model):**

```text
Nỗ lực (người-tháng) = NOP / PROD
```

_(PROD phụ thuộc vào kinh nghiệm và năng lực nhà phát triển: Very Low → Very High)_

---

## IV. Phân tích hồi quy (Regression Analysis) \[4, 5\]

Hồi quy tuyến tính: **y = a + bx**

Trong hồi quy bội, biến phụ thuộc phụ thuộc vào nhiều biến độc lập hơn.
_(In multiple regression, the dependent variable depends on more than a single independent variable.)_

**Ví dụ:** Mô hình chi phí công ty (1965 Corporation Cost Model) \[6\]:

```text
MM = -33.63
  + 9.15 × (Lack of Requirements) (0-2)
  + 10.73 × (Stability of Design) (0-3)
  + 0.51 × (% Math Instructions)
  + 0.46 × (% Storage/Retrieval Instructions)
  + ... (13 tham số tổng cộng)
```

---

## V. Mô hình COCOMO (COCOMO Model)

### 5.1 COCOMO cơ bản

COCOMO là phân cấp ba mô hình ngày càng chi tiết. Mức cơ bản chỉ dùng chế độ và kích thước để xác định nỗ lực và tiến độ — hữu ích cho ước tính nhanh, sơ bộ dự án nhỏ đến trung bình.

**Ba chế độ phát triển:**

| Chế độ                          | Quy mô điển hình | Đặc điểm                                                 |
| ------------------------------- | ---------------- | -------------------------------------------------------- |
| **Hữu cơ (Organic)**            | 2–50 KLOC        | Dự án nhỏ, nhóm nhỏ, quen thuộc với ứng dụng             |
| **Bán tách rời (Semidetached)** | 50–300 KLOC      | Dự án vừa, nhóm vừa, năng lực trung bình                 |
| **Nhúng (Embedded)**            | > 300 KLOC       | Dự án lớn, yêu cầu thời gian thực, ràng buộc nghiêm ngặt |

### 5.2 COCOMO trung cấp

Cấp trung cấp sử dụng kích thước, chế độ và 15 biến bổ sung (cost drivers) để xác định nỗ lực:

```text
E = a × (Kích thước)^b × EAF
```

_(EAF = Effort Adjustment Factor = C1 × C2 × ... × Cn)_

### 5.3 COCOMO chi tiết

Xây dựng dựa trên COCOMO trung cấp, giới thiệu:

- Hệ số nhân nỗ lực theo pha _(phase-sensitive effort multipliers)_
- Phân cấp sản phẩm 3 cấp: hệ thống → hệ thống con → mô-đun

4 pha chính: Yêu cầu (RQ), Thiết kế sản phẩm (PD), Thiết kế chi tiết (DD), Mã hóa và kiểm tra đơn vị (CUT).

### 5.4 Hạn chế của COCOMO

COCOMO gặp khó khăn với:

- Phần mềm hướng đối tượng
- Phần mềm được tạo theo mô hình xoắn ốc hoặc tiến hóa
- Ứng dụng phát triển từ phần mềm thương mại sẵn có (COTS)
- Khi thiếu thông tin về quy mô dự án hoặc nhân sự

### 5.5 COCOMO II

COCOMO II là phiên bản sửa đổi, mở rộng của COCOMO gốc:

- **Giai đoạn khái niệm sớm:** Sử dụng Object Points để tính nỗ lực.
- **Thiết kế ban đầu:** Sử dụng UFP làm đầu vào.
  - `Nỗ lực = 2.45 × KLOC × EAF`
- **Sau khi chọn kiến trúc:** Sử dụng SLOC.
  - `Nỗ lực = 2.55 × KLOC^B × EAF`

### 5.6 Mô hình SLIM Putnam \[6, 7\]

Putnam phát hiện rằng mối quan hệ giữa kích thước, tiến độ và nỗ lực phù hợp với **Hàm Norden/Rayleigh**:

```text
S = C × K^(1/3) × td^(4/3)
```

_(S = kích thước LOC; C = hệ số môi trường; K = tổng nỗ lực; td = thời gian phát triển tính bằng năm)_

### 5.7 Ước tính phân bổ nỗ lực theo hoạt động

| Hoạt động                     | Tỷ lệ  |
| ----------------------------- | ------ |
| Yêu cầu (Requirement)         | 11.30% |
| Phân tích & Thiết kế (A&D)    | 8.25%  |
| Triển khai (Implementation)   | 48.55% |
| Kiểm tra (Test)               | 16.05% |
| Triển khai (Deployment)       | 2.55%  |
| Quản lý (Management)          | 6.15%  |
| Môi trường (Environment)      | 2.03%  |
| SCM                           | 1.86%  |
| SQA                           | 1.80%  |
| Đào tạo (Training)            | 0.63%  |
| Phòng ngừa lỗi (Defect Prev.) | 0.85%  |

### 5.8 Ước tính lịch trình (Schedule Estimation)

```text
Lịch trình = 3 × Nỗ lực^(1/3)
```

Jones's First-Order: `Lịch trình = FPs^x` (x từ 0.33 đến 0.44 tùy loại phần mềm)

---

## VI. Khoa học phần mềm Halstead (Halstead's Software Science)

**Các thuộc tính đo được:**

- n1 = số toán tử duy nhất
- n2 = số toán hạng duy nhất
- N1 = tổng sử dụng tất cả toán tử
- N2 = tổng sử dụng tất cả toán hạng

**Các công thức:**

| Đại lượng | Công thức                 |
| --------- | ------------------------- |
| Từ vựng   | n = n1 + n2               |
| Độ dài    | N = N1 + N2               |
| Thể tích  | V = n1·log₂n1 + n2·log₂n2 |
| Độ khó    | D = (n1/2) × (N2/n2)      |
| Nỗ lực    | E = D × V                 |

**Ưu và nhược điểm:**

- ✅ Đơn giản tính toán; có thể dùng cho bất kỳ ngôn ngữ nào.
- ❌ Phụ thuộc vào mã đã hoàn thành; không có giá trị dự đoán trước.

---

## VII. Đo lường vs. Đánh giá (Measurement vs. Rating)

> - **Đo lường (Measurement)** mang tính khách quan và có thể thao túng toán học.
>   _(A measurement is objective and can be manipulated mathematically.)_
> - **Đánh giá (Rating)** mang tính chủ quan và không thể thao túng toán học.
>   _(A rating is subjective and cannot be manipulated mathematically.)_

FP, UCP, OP là **đánh giá (rating)**, không phải đo lường (measurement).

Câu hỏi mở: 1 ứng dụng 2000 FP = 2 × ứng dụng 1000 FP? Nếu nhóm hoàn thành 250 FP trong 10 tuần, họ có thể hoàn thành 500 FP trong 20 tuần?

---

## Đọc thêm (Further Reading)

- McCabe's Cyclomatic Number _(Số Cyclomatic của McCabe)_
- Fan-In Fan-Out Complexity — Henry's and Kafura's
- Defects Estimation _(Ước tính khuyết tật)_
- Reliability Estimation _(Đánh giá độ tin cậy)_

---

## Tài liệu tham khảo (References)

1. Linda M. Laird, M. Carol Brennan (2006). _Software Measurement and Estimation: A Practical Approach_.
2. AJ Albrecht (1979). _Measuring Application Development Productivity_.
3. CR Symons (1988). _Function Point Analysis: Difficulties and Improvements_.
4. Mohammed A. Shayib (2013). _Applied Statistics_.
5. N.H. Bingham và John M. Fry (2010). _Regression: Linear Models in Statistics_.
6. Robert T. Futrell et al. (2002). _Quality Software Project Management_.
7. Daniel D. Galorath (2006). _Software Sizing, Estimation, and Risk Management_.
8. Steve McConnell (2006). _Software Estimation: Demystifying the Black Art_. Microsoft Press.
