# PROJECT VISION & SCOPE (WHAT)

## Kho Lưu trữ Số Khóa luận Tốt nghiệp HCMUS

**Trường Đại học Khoa học Tự nhiên, ĐHQG-HCM (HCMUS) — Thư viện & Phòng Công nghệ Thông tin**

Phiên bản 1.0 • Tháng 7/2026

## Mục lục

* [1. Glossary & Business Rules](#1-glossary--business-rules)
* [2. Feature Model & MVP](#2-feature-model--mvp)
* [3. Vision — Black-box Solution](#3-vision--black-box-solution)
* [4. Project Scope Statement](#4-project-scope-statement)
* [5. Mockup, Prototype & PoC](#5-mockup-prototype--poc)

---

## 1. Glossary & Business Rules

### Glossary

| Thuật ngữ | Định nghĩa |
| --- | --- |
| **Repository** | Nền tảng lưu trữ và quản lý vòng đời số của khóa luận (nộp → duyệt → lưu trữ → tra cứu). |
| **Metadata** | Dữ liệu mô tả khóa luận (tác giả, GVHD, năm, khoa, tóm tắt...), chuẩn hóa theo **Dublin Core**. |
| **Handle/DOI nội bộ** | Mã định danh bền vững, không đổi theo thời gian, dùng để trích dẫn/tham chiếu ổn định đến một khóa luận. |
| **Embargo** | Khoảng thời gian hạn chế công khai một tài liệu theo yêu cầu của tác giả, sau đó tự động chuyển sang mức truy cập đã định trước. |
| **OCR (Optical Character Recognition)** | Công nghệ nhận dạng ký tự từ ảnh scan để chuyển thành văn bản có thể tìm kiếm được. |
| **RAG (Retrieval-Augmented Generation)** | Kỹ thuật tìm kiếm ngữ nghĩa kết hợp mô hình sinh ngôn ngữ, dự kiến ở giai đoạn sau MVP. |

### Business Rules

| Quy tắc nghiệp vụ (Rule) | Nguồn tham chiếu (Source) | Mức độ biến động |
| --- | --- | --- |
| Metadata khóa luận phải tuân theo chuẩn Dublin Core | Thông lệ nghiệp vụ thư viện số quốc tế | Thấp — chuẩn quốc tế ổn định |
| Mỗi khóa luận có đúng 1 trong 3 mức truy cập: công khai / nội bộ mạng trường / hạn chế (embargo) | Quyết định số 142/QĐ-KHTN ngày 12/03/2024 của Hiệu trưởng HCMUS về Quy chế hoạt động Thư viện | Trung bình — có thể điều chỉnh theo chính sách xuất bản học thuật |
| Khóa luận chỉ được công khai sau khi có xác nhận đồng ý (consent) của tác giả | Luật Sở hữu trí tuệ số 50/2005/QH11 và Luật sửa đổi, bổ sung một số điều của Luật Sở hữu trí tuệ số 07/2022/QH15 | **Cao — phụ thuộc vào quy định pháp luật về bản quyền** |
| Thời hạn embargo tối đa là 36 tháng | Quy định quản lý sở hữu trí tuệ của ĐHQG-HCM ban hành kèm Quyết định số 82/QĐ-ĐHQG ngày 15/01/2023 | Trung bình |
| Việc di dời, bảo quản hoặc tiêu hủy bản cứng sau khi số hóa phải tuân thủ quy trình lưu trữ | Quy chế Công tác văn thư, lưu trữ của Trường ĐHKHTN ban hành kèm Quyết định số 915/QĐ-KHTN ngày 15/10/2022 | Trung bình |

## 2. Feature Model & MVP

Vì tính năng **phân quyền truy cập** chứa quan hệ **Alternative** (chọn đúng 1 mức), nhóm tính năng dưới đây được trình bày dưới dạng **Feature Model** đầy đủ (And / Alternative / Or / Mandatory-Optional), không phải Feature Tree đơn giản.

![Sơ đồ mô hình tính năng (Feature Model)](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/docs/images/feature_model.svg)


Mỗi feature quan trọng, viết theo mẫu *User → Business goal → Metric → Action*:

- **User** Sinh viên/Giảng viên → **Business goal** cần tra cứu khóa luận từ xa → **Metric** lượt truy cập/tháng, thời gian tra cứu → **Action** Tìm kiếm toàn văn theo nội dung/tác giả/GVHD/năm/khoa.
- **User** Cán bộ thư viện → **Business goal** kiểm soát chất lượng metadata và bản quyền trước khi xuất bản → **Metric** tỷ lệ khóa luận duyệt đúng hạn → **Action** Luồng duyệt metadata + phân quyền/embargo.
- **User** Tác giả khóa luận (cựu sinh viên) → **Business goal** kiểm soát mức độ công khai công trình của mình → **Metric** tỷ lệ khóa luận có xác nhận consent hợp lệ → **Action** Cơ chế embargo/hạn chế truy cập theo yêu cầu tác giả.

**MVP (Minimum Viable Product):** Nộp & Duyệt + Lưu trữ chuẩn hóa + Phân quyền 3 mức + Tìm kiếm toàn văn, triển khai thí điểm tại 1 khoa. Tìm kiếm ngữ nghĩa AI/RAG **không** thuộc MVP.

## 3. Vision — Black-box Solution

### Bối cảnh/Tổng quan

Hệ thống được mô tả như một "black-box" đối với người dùng: CÁI GÌ hệ thống làm cho họ, không mô tả CÁCH xây (xem `06-architecture.md` cho phần HOW).

![Sơ đồ ngữ cảnh hệ thống (System Context Diagram)](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/docs/images/context_diagram.svg)


### Current Situation (Trạng thái hiện tại)

#### Quy trình Hiện trạng (As-is Workflow)
Quy trình tiếp nhận, lưu trữ và khai thác khóa luận tốt nghiệp tại HCMUS hiện nay hoàn toàn thủ công và dựa trên bản giấy vật lý:
- **Bước 1 (Hoàn thành & In ấn):** Sau khi bảo vệ thành công, sinh viên phải tự in khóa luận và đóng tập bìa cứng mạ vàng thành nhiều bản.
- **Bước 2 (Nộp bài trực tiếp):** Sinh viên di chuyển từ các cơ sở (ví dụ: cơ sở Linh Trung ở Thủ Đức) đến Thư viện chính tại cơ sở Nguyễn Văn Cừ (Quận 5) để nộp trực tiếp bản cứng.
- **Bước 3 (Kiểm kê & Nhập liệu thủ công):** Thủ thư tiếp nhận sách giấy, đối chiếu thông tin sinh viên tốt nghiệp thủ công bằng danh sách giấy từ Phòng Đào tạo. Sau đó, nhập các thông tin mô tả cơ bản của khóa luận vào sổ đăng ký cá biệt và phần mềm quản lý thư viện truyền thống cũ.
- **Bước 4 (Phân loại & Xếp kho):** Thủ thư dán mã đăng ký cá biệt lên sách, phân phối và xếp cuốn khóa luận giấy lên kệ kho lưu trữ vật lý theo phân loại Khoa và Năm học.
- **Bước 5 (Tra cứu & Yêu cầu mượn):** Độc giả (sinh viên khóa dưới, giảng viên) có nhu cầu tham khảo phải đến trực tiếp Thư viện Q5 trong giờ hành chính, tra cứu mã sách qua tủ thẻ mục lục giấy hoặc máy tính nội bộ của thư viện, rồi viết thông tin vào phiếu mượn giấy nộp cho thủ thư.
- **Bước 6 (Tìm kiếm vật lý):** Thủ thư tiếp nhận phiếu mượn giấy, đi sâu vào các kệ kho lưu trữ tối để lục tìm cuốn khóa luận giấy duy nhất đó và bàn giao cho độc giả.
- **Bước 7 (Khai thác tại chỗ):** Độc giả chỉ được phép đọc và chép tay hoặc tự gõ lại các thông tin nghiên cứu quan trọng (thuật toán, công thức) trực tiếp tại phòng đọc thư viện. Thư viện nghiêm cấm photocopy hoặc chụp hình để bảo vệ bản quyền tác giả.
- **Bước 8 (Trả tài liệu):** Độc giả trả lại sách, thủ thư kiểm tra tình trạng vật lý (có rách hỏng, ẩm mốc, mất trang không) trước khi mang xếp lại vào kệ kho.

#### Vấn đề của quy trình hiện tại (Core Pain Points)
- **Hạn chế về mặt địa lý:** Độc giả buộc phải đến tận cơ sở Nguyễn Văn Cừ (Quận 5) để khai thác khóa luận. Sinh viên học tại Linh Trung (Thủ Đức) phải di chuyển hơn 15km rất tốn thời gian và công sức.
- **Tìm kiếm thông tin kém hiệu quả:** Chỉ có thể tra cứu theo các thông tin cơ bản (Tên khóa luận, Tác giả, Năm), hoàn toàn không thể tìm kiếm toàn văn (full-text) bên trong nội dung hoặc phương pháp nghiên cứu.
- **Hao mòn & Rủi ro hư hỏng tài liệu:** Do chỉ lưu trữ duy nhất một bản cứng vật lý, tần suất mượn đọc cao làm sách nhanh hư hỏng, rách nát. Môi trường kho lưu trữ không chuẩn dễ gây ẩm mốc, mối mọt làm mất mát nguồn tri thức quý giá.
- **Quy trình nghiệp vụ quá tải:** Mỗi mùa tốt nghiệp, thủ thư phải đối chiếu danh sách và nhập liệu thủ công hàng ngàn bản ghi mô tả khóa luận, mất hàng trăm giờ làm việc hành chính và dễ xảy ra sai sót dữ liệu.
- **Tắc nghẽn không gian kho bãi:** Số lượng khóa luận tăng tuyến tính mỗi năm gây áp lực nặng nề lên diện tích lưu kho vốn dĩ đã quá tải của thư viện.
- **Rủi ro pháp lý về bản quyền:** Thư viện thiếu một quy trình và công cụ để thu thập cam kết bản quyền (Consent Form) từ sinh viên một cách hệ thống và pháp lý, dẫn đến rủi ro pháp lý khi xuất bản hoặc chia sẻ tài liệu số hóa cho cộng đồng.

- **Domain model hiện tại (đơn giản):** *Khóa luận (bản giấy)* — *Sổ mượn/trả* — *Thẻ mục lục* — *Kệ/kho theo khoa-năm*. Không có thực thể "metadata số" hay "quyền truy cập" tách biệt khỏi bản vật lý.

### Future Situation (Trạng thái tương lai)

#### Quy trình Tương lai (To-be Workflow)
Hệ thống Repository số hóa sẽ tự động hóa toàn bộ vòng đời của khóa luận tốt nghiệp từ khâu nộp bài đến kiểm duyệt, lưu trữ và khai thác. Dưới đây là mô tả chi tiết cách người dùng tương tác với hệ thống:

##### 1. Đối với Tác giả (Sinh viên tốt nghiệp) - Quy trình Nộp bài trực tuyến:
- **Bước 1.1 (Đăng nhập hệ thống):** Sinh viên truy cập Cổng Repository số của HCMUS qua trình duyệt. Nhấp chọn "Đăng nhập", hệ thống sẽ chuyển hướng sang trang xác thực tập trung SSO của trường (CAS/LDAP). Sinh viên nhập tài khoản định danh trường (MSSV và mật khẩu) để hoàn tất đăng nhập.
- **Bước 1.2 (Khởi tạo hồ sơ nộp):** Tại giao diện Dashboard cá nhân, sinh viên chọn chức năng "Nộp khóa luận mới" để mở form khai báo hồ sơ.
- **Bước 1.3 (Nhập liệu Metadata chuẩn hóa):** Sinh viên nhập đầy đủ thông tin vào các trường metadata bắt buộc theo chuẩn Dublin Core:
  - *Thông tin tác giả:* Tên sinh viên, MSSV, Khoa, Khóa học, Email cá nhân.
  - *Thông tin khóa luận:* Tên đề tài (Tiếng Việt & Tiếng Anh), giảng viên hướng dẫn (chọn từ danh sách gợi ý hoặc nhập mới), hội đồng bảo vệ, điểm số.
  - *Tóm tắt & Từ khóa:* Nhập bản tóm tắt đề tài (abstract) và các từ khóa liên quan (keywords) phục vụ lập chỉ mục tìm kiếm.
- **Bước 1.4 (Tải lên file khóa luận):** Sinh viên tải lên file PDF khóa luận toàn văn. Hệ thống tự động kiểm tra định dạng tại chỗ (client-side validation): dung lượng file (tối đa 100MB), đuôi mở rộng bắt buộc là `.pdf`, và kiểm tra xem file có bị đặt mật khẩu khóa hay không.
- **Bước 1.5 (Ký cam kết bản quyền & Chọn phân quyền):** Sinh viên đọc văn bản thỏa thuận quyền sở hữu trí tuệ (Digital Consent Form) hiển thị trên màn hình, sau đó:
  - Tích chọn cam kết chịu trách nhiệm về tính trung thực và bản quyền của nội dung.
  - Lựa chọn 1 trong 3 mức truy cập:
    - *Public (Công khai):* Cho phép mọi người dùng Internet được truy cập và đọc toàn văn khóa luận.
    - *Internal (Nội bộ):* Chỉ cho phép người dùng đăng nhập bằng tài khoản SSO trường HCMUS truy cập đọc toàn văn.
    - *Embargo (Hạn chế có thời hạn):* Ẩn file toàn văn và chỉ hiển thị metadata trong thời hạn lựa chọn (12, 24 hoặc tối đa 36 tháng). Sau thời hạn này, hệ thống sẽ tự động chuyển sang mức truy cập đã cấu hình trước (Public hoặc Internal).
  - Nhấp nút "Gửi phê duyệt". Hệ thống lưu trạng thái hồ sơ là "Chờ duyệt" và tự động gửi email xác nhận đã tiếp nhận thành công cho sinh viên.
- **Bước 1.6 (Cập nhật sửa đổi):** Nếu bài nộp bị thủ thư từ chối, sinh viên nhận email tự động ghi rõ lý do. Sinh viên đăng nhập lại hệ thống, vào mục "Hồ sơ cần chỉnh sửa", thực hiện sửa metadata hoặc tải lại file PDF mới theo yêu cầu và gửi lại để duyệt.

##### 2. Đối với Thủ thư (Cán bộ kiểm duyệt) - Quy trình Duyệt bài trực tuyến:
- **Bước 2.1 (Tiếp nhận hồ sơ mới):** Khi sinh viên gửi bài nộp, yêu cầu duyệt sẽ được đẩy vào danh sách chờ (Approval Queue) trên dashboard quản trị của thủ thư theo thứ tự thời gian.
- **Bước 2.2 (Xem chi tiết & Thẩm định):** Thủ thư chọn một hồ sơ chờ duyệt để thực hiện:
  - *Thẩm định Metadata:* Hệ thống tự động đối chiếu thông tin sinh viên nhập với danh sách tốt nghiệp chính thức từ Phòng Đào tạo (cảnh báo đỏ nếu có sai lệch về MSSV, họ tên hoặc khoa).
  - *Thẩm định File PDF:* Thủ thư xem trực tiếp file PDF qua trình xem PDF nội bộ của admin để kiểm tra định dạng, sự đầy đủ của các trang chính, hình vẽ, và chữ ký xác nhận của GVHD/Hội đồng bảo vệ trên trang bìa.
- **Bước 2.3 (Thực hiện phê duyệt hoặc từ chối):**
  - **Trường hợp Phê duyệt (Approve):** Thủ thư xác nhận thông tin đã chuẩn hóa, nhấp "Phê duyệt & Xuất bản". Hệ thống sẽ tự động gán mã định danh bền vững Handle ID, lưu tệp PDF vào Object Storage, và lập chỉ mục toàn văn (Full-text Indexing) trên Elasticsearch. Một email thông báo tự động chứa Handle Link trích dẫn sẽ được gửi đến sinh viên.
  - **Trường hợp Từ chối (Reject):** Thủ thư chọn lý do từ chối từ danh mục mẫu (ví dụ: "File PDF thiếu trang bìa có chữ ký", "Metadata sai thông tin GVHD") hoặc tự nhập nội dung lý do chi tiết, rồi nhấp "Từ chối". Hệ thống chuyển trạng thái hồ sơ về "Cần chỉnh sửa" và gửi email phản hồi kèm lý do cho sinh viên.

##### 3. Đối với Độc giả (Sinh viên tra cứu, Giảng viên, Khách vãng lai) - Quy trình Tra cứu & Đọc tài liệu:
- **Bước 3.1 (Truy cập & Tìm kiếm):** Độc giả truy cập trang chủ Cổng Repository số của HCMUS (không bắt buộc đăng nhập để xem thông tin công khai):
  - *Tìm kiếm đơn giản:* Nhập từ khóa tự do vào thanh công cụ tìm kiếm toàn văn.
  - *Tìm kiếm nâng cao:* Kết hợp các bộ lọc thông minh ở thanh bên (lọc theo Khoa, Năm tốt nghiệp, Giảng viên hướng dẫn, v.v.).
- **Bước 3.2 (Xem Metadata):** Hệ thống trả về danh sách kết quả phù hợp nhất. Độc giả nhấp chọn tài liệu quan tâm để xem trang chi tiết chứa toàn bộ Metadata chuẩn Dublin Core và bản tóm tắt (abstract).
- **Bước 3.3 (Đọc toàn văn theo phân quyền):** Khi độc giả nhấp nút "Đọc toàn văn", hệ thống tự động kiểm tra mức độ phân quyền của tài liệu:
  - *Tài liệu Public:* Mở trình xem PDF trực tuyến trên giao diện web để đọc ngay lập tức.
  - *Tài liệu Internal:* Hiển thị hộp thoại yêu cầu đăng nhập. Độc giả phải đăng nhập tài khoản SSO trường để xem nội dung.
  - *Tài liệu Embargo:* Ẩn file toàn văn, hiển thị biểu tượng ổ khóa kèm ghi chú thời gian hết hạn embargo (ví dụ: "Bị hạn chế đến 12/08/2027"). Đối với độc giả trong trường cần truy cập sớm phục vụ nghiên cứu, hệ thống cung cấp nút "Gửi yêu cầu xin phép tác giả" để nhập lý do mượn; hệ thống sẽ chuyển tiếp yêu cầu đến email tác giả để tác giả phê duyệt cấp quyền đọc thủ công.
- **Bước 3.4 (Đọc trực tuyến bảo mật):** Đối với các tài liệu được quyền xem, trình xem PDF Viewer bảo mật của hệ thống hoạt động như sau:
  - Sinh đường dẫn Signed URL bảo mật tạm thời có hiệu lực tối đa 15 phút. Nếu độc giả vẫn tiếp tục đọc, hệ thống tự động làm mới liên kết ở chế độ nền mà không làm gián đoạn việc đọc, ngăn chặn việc sao chép link hoặc chia sẻ link ra ngoài.
  - Vô hiệu hóa chuột phải (ngăn chặn sao chép văn bản), ẩn phím tắt in ấn mặc định của trình duyệt và ẩn nút download tệp trực tiếp đối với các tài liệu nội bộ/embargo để phòng chống cào quét dữ liệu (data scraping).
- **Bước 3.5 (Trích dẫn tài liệu):** Tại trang chi tiết khóa luận, độc giả nhấp chọn chức năng "Trích dẫn". Hệ thống hiển thị các định dạng trích dẫn học thuật chuẩn hóa (APA, IEEE, Harvard...) chứa đầy đủ thông tin tác giả, năm, tên đề tài và đính kèm liên kết Handle Link bền vững để độc giả dễ dàng sao chép phục vụ nghiên cứu khoa học.


#### Sơ đồ Quy trình Hiện trạng (As-is) và Tương lai (To-be)
Quy trình chuyển đổi từ thủ công sang số hóa được trực quan hóa chi tiết trong sơ đồ dưới đây:

![Sơ đồ Quy trình Hiện trạng vs Tương lai](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/docs/images/as_is_to_be_workflow.svg)

#### Bảng Đối chiếu Vấn đề và Giải pháp Tính năng
Dưới đây là bảng ánh xạ cách các tính năng của hệ thống số hóa giải quyết triệt để từng vấn đề của quy trình thủ công hiện tại:

| Vấn đề Hiện tại (Pain Point) | Giải pháp Số hóa (To-be Solution) | Tính năng Hệ thống (System Feature) | Giá trị mang lại (Value Delivered) |
| :--- | :--- | :--- | :--- |
| **Hạn chế địa lý:** Phải đến tận thư viện Q5 để đọc bản cứng. | Cho phép truy cập từ xa mọi lúc mọi nơi thông qua mạng Internet. | • Cổng thông tin Web Responsive<br>• Tích hợp xác thực Single Sign-On (SSO) | Độc giả (đặc biệt ở Linh Trung) tra cứu tài liệu từ xa 24/7 không cần di chuyển vật lý. |
| **Tìm kiếm hạn chế:** Chỉ tra được theo tên đề tài, tác giả trên thẻ mục lục. | Hỗ trợ tìm kiếm từ khóa trong toàn bộ nội dung khóa luận. | • Tìm kiếm toàn văn (Full-text Search) bằng Elasticsearch<br>• Bộ lọc thông minh theo Khoa, Năm, GVHD | Tiết kiệm 95% thời gian tra cứu, tìm đúng nội dung chuyên môn sâu và đối chiếu đề tài trùng lặp. |
| **Hao mòn tài liệu:** Bản cứng duy nhất dễ rách hỏng, ẩm mốc. | Chuyển đổi thành bản số lưu trữ dự phòng đám mây/máy chủ. | • Lưu trữ số hóa (Object Storage)<br>• Quy trình sao lưu tự động (Backup & Disaster Recovery) | Bảo tồn nguyên vẹn tri thức học thuật vĩnh viễn, loại bỏ hao mòn vật lý. |
| **Rủi ro pháp lý bản quyền:** Không có sự đồng ý chính thức từ tác giả để chia sẻ. | Thu thập cam kết bản quyền của tác giả bằng quy trình số hóa bắt buộc. | • Quản lý cam kết bản quyền (Digital Consent Form)<br>• Phân quyền 3 mức (Public, Internal, Embargo) | Đảm bảo tính hợp pháp tối đa cho nhà trường khi chia sẻ dữ liệu số, bảo vệ quyền lợi sinh viên. |
| **Quá tải không gian kho:** Kệ sách vật lý chật kín, tốn chi phí quản lý diện tích. | Thay thế lưu trữ giấy bằng lưu trữ số dung lượng lớn, giải phóng kho bãi. | • Cloud/Server Storage dung lượng lớn<br>• Quản lý lưu trữ tệp số tập trung | Giải phóng hàng trăm mét vuông không gian thư viện làm khu tự học, giảm chi phí vận hành kho bãi. |
| **Quy trình thủ công quá tải:** Thủ thư mất thời gian đối chiếu danh sách và nhập liệu giấy. | Tự động hóa quy trình nộp bài, tự động gán mã và định danh. | • Luồng duyệt tự động (Review Workflow Dashboard)<br>• Tự động gán mã định danh bền vững Handle ID | Rút ngắn thời gian xử lý hồ sơ tốt nghiệp của thủ thư từ vài tuần xuống còn vài phút mỗi bài nộp. |
| **Rò rỉ & Tải tài liệu lậu:** Rủi ro độc giả tải hàng loạt PDF về phát tán trái phép. | Kiểm soát chặt chẽ việc tải tệp và đọc trực tuyến an toàn. | • Signed URL bảo mật (hạn dùng 15 phút)<br>• PDF Viewer bảo mật (chặn chuột phải, download trực tiếp) | Ngăn chặn các công cụ cào dữ liệu (bot/crawlers) tải hàng loạt tài liệu, bảo vệ tài sản trí tuệ. |

- **Domain model tương lai:** *Thesis (khóa luận số)* — *Metadata (Dublin Core)* — *Author/Consent* — *Access Level (Public/Internal/Embargo)* — *Identifier (Handle/DOI nội bộ)* — *Search Index*.
- **Thành phần/tính năng SẼ phát triển:** nộp & duyệt trực tuyến, lưu trữ chuẩn hóa, phân quyền 3 mức, tìm kiếm toàn văn (MVP); tìm kiếm ngữ nghĩa AI/RAG (sau MVP, khi ngân sách/nhu cầu được xác nhận).
- **Thành phần/tính năng SẼ loại trừ (out of scope):** công cụ kiểm tra đạo văn chuyên dụng (Turnitin/DoIT); số hóa các loại tài liệu khác ngoài khóa luận tốt nghiệp (giáo trình, luận văn cao học); việc tiêu hủy bản cứng.
- **Giả định:** quy chế lưu trữ cho phép công bố bản số song song với việc giữ/di dời bản cứng theo lộ trình riêng; tác giả có thể được liên hệ lại để xin consent hồi tố cho khóa luận cũ.
- **Rủi ro:** một số khóa luận cũ không thể liên hệ lại tác giả để xin consent → cần quy tắc mặc định (vd: mặc định giới hạn nội bộ nếu chưa có consent) — xem thêm `04-feasibility-study.md`.
- **Kết luận:** chuyển đổi từ mô hình "tài sản vật lý tĩnh, truy cập tại chỗ" sang "tài nguyên số có cấu trúc, truy cập theo phân quyền" là thay đổi cốt lõi mà dự án mang lại.


## 4. Project Scope Statement

**Mô tả phạm vi sản phẩm:** một nền tảng repository số cho khóa luận tốt nghiệp đại học của HCMUS, bao gồm nộp, duyệt, lưu trữ metadata chuẩn hóa, phân quyền truy cập, và tìm kiếm toàn văn.

**Deliverables:**
- Nền tảng repository vận hành (dựa trên nền tảng mã nguồn mở tùy biến).
- Kho khóa luận đã số hóa (thí điểm 1 khoa ở MVP, mở rộng toàn trường ở pha sau).
- Tài liệu hướng dẫn sử dụng/quản trị cho cán bộ thư viện.
- Quy trình nộp khóa luận trực tuyến tích hợp vào quy chế tốt nghiệp.

**Project Exclusions:**
- Công cụ chống đạo văn chuyên dụng (Turnitin/DoIT) — hạng mục tích hợp riêng, license riêng.
- Số hóa giáo trình, luận văn cao học hoặc tài liệu khác ngoài khóa luận đại học.
- Quyết định/thực hiện tiêu hủy bản cứng — thuộc thẩm quyền quy chế lưu trữ, không phải phạm vi dự án CNTT.
- Tìm kiếm ngữ nghĩa AI/RAG trong phạm vi MVP (đưa vào giai đoạn sau).

**Constraints:**
- Nội lực triển khai chủ yếu dựa vào đội CNTT hiện có của trường (chưa xác nhận năng lực/thời gian rảnh thực tế).
- Ngân sách số hóa tỷ lệ thuận với khối lượng tài liệu — số hóa toàn trường ngay từ đầu kéo dài thời gian và chi phí đáng kể (xem `04-feasibility-study.md`).
- Ràng buộc pháp lý về bản quyền/consent của sinh viên phải được giải quyết trước khi số hóa hàng loạt.

**Yêu cầu phi chức năng & Chỉ số chất lượng (Non-Functional Requirements):**
- **Hiệu năng (Performance):** Thời gian phản hồi cho truy vấn tìm kiếm toàn văn dưới 3 giây đối với 95% số truy vấn, dưới 5 giây đối với 99% số truy vấn dưới tải trọng 500 người dùng đồng thời.
- **Độ tin cậy (Reliability):** Uptime SLA đạt tối thiểu 99.5% hàng năm (trừ thời gian bảo trì hệ thống định kỳ được thông báo trước). Chỉ số điểm phục hồi mục tiêu RPO < 24 giờ và thời gian phục hồi hệ thống RTO < 4 giờ.
- **Bảo mật & Quyền riêng tư (Security & Privacy):** 
  - Toàn bộ dữ liệu truyền tải bắt buộc sử dụng giao thức mã hóa HTTPS (TLS 1.3).
  - Tuân thủ Nghị định 13/2023/NĐ-CP về bảo vệ dữ liệu cá nhân (ẩn các thông tin cá nhân nhạy cảm như số điện thoại, email cá nhân, địa chỉ nhà của sinh viên trên bản hiển thị công khai).
  - Áp dụng cơ chế Signed URL có thời hạn tối đa 15 phút để ngăn chặn việc tải tệp hàng loạt bất hợp pháp (scraping/crawling).
- **Chất lượng số hóa (OCR Quality):** Tỷ lệ nhận dạng ký tự tiếng Việt chính xác (Character Accuracy Rate - CAR) đạt tối thiểu 90% đối với tài liệu scan sạch (từ năm 2015 trở đi) và tối thiểu 75% đối với tài liệu scan cũ, mờ.

**Acceptance Criteria:**
- MVP vận hành ổn định với ít nhất 1 khoa thí điểm, đo được lượt truy cập thực tế.
- Cán bộ thư viện có thể duyệt và xuất bản khóa luận qua quy trình trực tuyến mà không cần thao tác thủ công song song.
- Người dùng tìm kiếm được khóa luận theo nội dung, tác giả, GVHD, năm, khoa với tỷ lệ khớp chính xác (Precision) đạt tối thiểu 90% và tỷ lệ bao phủ (Recall) đạt tối thiểu 85% dựa trên tập dữ liệu thử nghiệm.

**Assumptions:**
- Quy chế lưu trữ và bản quyền sẽ được làm rõ trong giai đoạn khảo sát trước khi số hóa quy mô lớn.
- Nền tảng mã nguồn mở (DSpace/Invenio) đáp ứng được yêu cầu nghiệp vụ mà không cần phát triển từ đầu.

## 5. Mockup, Prototype & PoC

**Thiết kế Prototype (luồng UI/UX cần trực quan hóa trước khi code):**
- Luồng **nộp — duyệt — xuất bản**: đây là luồng rủi ro cao nhất vì liên quan trực tiếp đến quyết định phân quyền/embargo của tác giả; cần mockup và cho cán bộ thư viện + một nhóm sinh viên thao tác thử trước khi lập trình chính thức.
- Luồng **tìm kiếm & lọc kết quả** (theo nội dung/tác giả/GVHD/năm/khoa): cần mockup để xác nhận bộ lọc đáp ứng đúng thói quen tra cứu của người dùng.

**Mục tiêu PoC (giới hạn công nghệ cần thử nghiệm trước khi cam kết kiến trúc):**
- **OCR tiếng Việt:** thử nghiệm trên một mẫu tài liệu scan thực tế (chất lượng không đồng đều) để đo độ chính xác nhận dạng trước khi cam kết quy trình số hóa hàng loạt ~10.000+ cuốn.
- **Tìm kiếm ngữ nghĩa AI/RAG (nếu triển khai ở pha sau):** thử nghiệm mô hình embedding hỗ trợ tiếng Việt trên một tập nhỏ khóa luận để xác nhận chất lượng truy vấn ngữ nghĩa trước khi đầu tư hạ tầng vector đầy đủ.
