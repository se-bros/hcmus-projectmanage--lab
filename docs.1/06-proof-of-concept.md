# KẾ HOẠCH VÀ BIÊN BẢN CHỨNG MINH Ý TƯỞNG

## Hệ thống Quản lý và Số hóa Tài liệu Thư viện HCMUS (HCMUS-LDMS)

### Thông tin tài liệu

| Trường      | Nội dung                                                               |
| ----------- | ---------------------------------------------------------------------- |
| Mã tài liệu | `HCMUS-LDMS-POC`                                                       |
| Chủ sở hữu  | Solution Architect — Ân Tiến Nguyên An                                 |
| Phiên bản   | 1.0 — 22/08/2026                                                       |
| Trạng thái  | Kế hoạch đã soạn; các thử nghiệm đang `Chưa chạy`                      |
| Mục tiêu    | Kiểm chứng hai bất định kỹ thuật lớn trước khi khẳng định tính khả thi |

## Mục lục

- [1. Mục đích](#1-mục-đích)
- [2. Lựa chọn thử nghiệm](#2-lựa-chọn-thử-nghiệm)
- [3. PoC-01 Nhận dạng ký tự và phục hồi tác vụ](#3-poc-01-nhận-dạng-ký-tự-và-phục-hồi-tác-vụ)
- [4. PoC-02 Xuất bản, phân quyền và đọc EPUB](#4-poc-02-xuất-bản-phân-quyền-và-đọc-epub)
- [5. Mẫu ghi kết quả](#5-mẫu-ghi-kết-quả)
- [6. Cách đánh giá và sử dụng kết quả](#6-cách-đánh-giá-và-sử-dụng-kết-quả)
- [7. Truy vết](#7-truy-vết)

## 1. Mục đích

Chứng minh ý tưởng là thử nghiệm nhỏ để giảm bất định, không phải sản phẩm hoàn chỉnh. HCMUS-LDMS chọn hai luồng có rủi ro cao: xử lý OCR nền có phục hồi và chuỗi EPUB–phân quyền–đọc trực tuyến. Tài liệu này quy định đầu vào, đầu ra, tiêu chí đạt và cách ghi evidence; không thay thế kết quả chạy thật.

## 2. Lựa chọn thử nghiệm

| Mã     | Giả định cần kiểm chứng                                                                   | Lý do ưu tiên                                       | Quyết định chịu ảnh hưởng                    |
| ------ | ----------------------------------------------------------------------------------------- | --------------------------------------------------- | -------------------------------------------- |
| PoC-01 | Backend có thể nhận tệp, chạy OCR nền, giữ trạng thái và phục hồi lỗi mà không mất source | Rủi ro R-02, R-03, R-07 cao/rất cao                 | Cách tổ chức job, timeout, retry và dữ liệu  |
| PoC-02 | Nội dung đã hiệu chỉnh có thể tạo EPUB, xuất bản có kiểm soát và chỉ người đủ quyền đọc   | Cắt ngang nhiều mô-đun và rủi ro truy cập trái phép | Công cụ EPUB, RBAC, object private và reader |

Không chọn giao diện đẹp, ghi chú hay trích dẫn làm PoC vì chúng không phải bất định quyết định khả năng hoàn thành MVP.

## 3. PoC-01 Nhận dạng ký tự và phục hồi tác vụ

### 3.1. Đầu vào và môi trường

- `DS-01`: một PDF/ảnh hợp lệ có quyền sử dụng, chữ Việt/Anh rõ.
- `DS-02`: một PDF nhiều trang có phần ground truth đủ để đối chiếu.
- Local: FastAPI, PostgreSQL, MinIO và Tesseract; ghi commit, hệ điều hành, phiên bản và cấu hình timeout.
- Tài khoản thử có quyền biên tập.

### 3.2. Các bước

1. Tải DS-01; ghi document ID, object key/hash và trạng thái ban đầu.
2. Khởi chạy OCR; quan sát `pending → processing → completed`.
3. Mở văn bản theo trang, sửa một đoạn, lưu và mở lại.
4. Chạy với DS-02; ghi thời gian và so sánh phần ground truth theo công thức được chốt.
5. Tạo tình huống timeout hoặc dừng tiến trình khi job đang chạy.
6. Khởi động lại, kiểm tra job được chuyển sang trạng thái có thể xử lý; retry.
7. Đối chiếu source hash, nội dung đã lưu và lịch sử attempt trước/sau retry.

### 3.3. Tiêu chí đạt

| Tiêu chí                             | Cách quan sát                                                       | Kết quả hiện tại |
| ------------------------------------ | ------------------------------------------------------------------- | ---------------- |
| UI/API không bị giữ đến khi OCR xong | Request tiếp nhận trả document/job ID và có thể theo dõi trạng thái | Chưa chạy        |
| Trạng thái và lỗi rõ                 | Log/API/UI cho thấy chuyển trạng thái hợp lệ                        | Chưa chạy        |
| Source không mất/ghi đè              | Hash/version trước và sau failure/retry không đổi                   | Chưa chạy        |
| Nội dung hiệu chỉnh được giữ         | Mở lại sau restart vẫn có save gần nhất                             | Chưa chạy        |
| Retry truy vết được                  | Attempt mới tồn tại, attempt cũ không bị xóa                        | Chưa chạy        |
| Chất lượng OCR được đo đúng          | Có dataset, ground truth, công thức và raw result                   | Chưa chạy        |

## 4. PoC-02 Xuất bản, phân quyền và đọc EPUB

### 4.1. Đầu vào

- Nội dung đã hiệu chỉnh từ tài liệu mẫu, metadata hợp lệ và một trường hợp thiếu metadata.
- Tài khoản Reader, Editor và Admin theo ma trận quyền.
- Công cụ tạo EPUB dự kiến và trình đọc Epub.js.

### 4.2. Các bước

1. Yêu cầu xuất bản khi thiếu dữ liệu bắt buộc; xác nhận bị chặn và nêu lý do.
2. Bổ sung metadata, tạo EPUB và kiểm tra bằng validator/reader mục tiêu.
3. Xuất bản với tài khoản có quyền; tìm kiếm và mở EPUB bằng Reader đủ quyền.
4. Dùng tài khoản không đủ quyền gọi trực tiếp API/object URL.
5. Kiểm tra draft không xuất hiện trong tìm kiếm và URL tạm thời hết hạn bị từ chối.
6. Gây lỗi tạo EPUB; xác nhận source/nội dung đã hiệu chỉnh không mất và có thể retry.

### 4.3. Tiêu chí đạt

| Tiêu chí                                                    | Kết quả hiện tại |
| ----------------------------------------------------------- | ---------------- |
| EPUB hợp lệ và mở được trên reader mục tiêu                 | Chưa chạy        |
| Publish gate chặn dữ liệu thiếu hoặc người sai quyền        | Chưa chạy        |
| Draft/private không lộ qua search/API/object URL            | Chưa chạy        |
| Reader đủ quyền mở được nội dung, không có nút tải EPUB gốc | Chưa chạy        |
| Lỗi tạo EPUB có trạng thái/retry và không mất dữ liệu       | Chưa chạy        |

## 5. Mẫu ghi kết quả

| Trường                   | Nội dung cần ghi                          |
| ------------------------ | ----------------------------------------- |
| Mã lần chạy              | `POC-01-RUN-NN` hoặc `POC-02-RUN-NN`      |
| Ngày/người chạy          | Người và thời điểm thực tế                |
| Commit/build/môi trường  | ID có thể truy vết                        |
| Dataset                  | ID, nguồn, quyền, hash và kích thước      |
| Các bước                 | Thao tác đã thực hiện                     |
| Kết quả mong đợi/thực tế | Quan sát và raw evidence                  |
| Kết luận                 | Đạt / Không đạt / Bị chặn                 |
| Ảnh hưởng                | ADR, Estimate, Risk, Backlog cần cập nhật |

Tại thời điểm phát hành tài liệu, chưa có giao diện đầu vào/đầu ra hoặc kết quả chạy được xác minh để chèn. Khi chạy, nhóm bổ sung ảnh chụp có build ID và che bí mật; không dùng hình thiết kế thay bằng chứng thực thi.

## 6. Cách đánh giá và sử dụng kết quả

- `Đạt`: tiêu chí bắt buộc có evidence; có thể giữ quyết định kiến trúc trong phạm vi đã thử.
- `Không đạt`: ghi nguyên nhân, thay đổi công nghệ/thiết kế/phạm vi và chạy lại nếu hợp lý.
- `Bị chặn`: ghi dependency/owner/ngày; không diễn giải là đạt.
- Kết quả cập nhật [Kiến trúc](05-software-architecture.md), [Ước lượng](10-project-estimate.md), [Risk Plan](18-risk-management-plan.md) và [ADR](A1-decision-log-and-adr.md).

## 7. Truy vết

PoC-01 truy vết `LDMS-002`, `003`, `004`, `005`, `022`, YC-ND và YC-PN-03/08. PoC-02 truy vết `LDMS-007`, `008`, `010`, `013`, `014`, `015`, YC-PH/TC và YC-PN-01/02. Kiểm thử chính thức được quản lý trong [Kế hoạch kiểm thử](20-test-plan.md).
