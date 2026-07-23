# TỔNG HỢP VÀ TRÍCH DẪN ĐÁNH GIÁ CÁC YÊU CẦU DỰ ÁN HCMUS-LDMS

Tài liệu này đối chiếu và trả lời trực tiếp từng câu hỏi kiểm tra tính đầy đủ của bộ 8 tài liệu quản lý dự án (`01-project-idea.md` đến `08-cost-time-resource.md`). 
- Các nội dung **đã có** được trích dẫn chính xác tệp tin, mục và đoạn văn bản tương ứng.
- Các nội dung **chưa có chi tiết hoặc là thao tác Demo thực tế** được ghi chú `[CHƯA CÓ TRONG 8 TÀI LIỆU GỐC - ĐỂ TRỐNG ĐỂ BỔ SUNG]`.

---

## 1. PROJECT PROPOSAL (ĐỀ XUẤT DỰ ÁN)

### 1.1. Tại sao nên thực hiện dự án này?
- **Trạng thái:** ĐÃ CÓ TRONG TÀI LIỆU.
- **Trích dẫn chi tiết:**
  - [01-project-idea.md](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/hcmus-projectmanage--lab/docs/01-project-idea.md#L60-L68) — **Mục 3.1. Thực trạng và Vấn đề**:
    > "- Xuống cấp học liệu vật lý: Hơn 40% giáo trình cũ và tài liệu chuyên ngành độc bản xuất bản trước năm 2010 tại thư viện đang bị mục nát, rách hỏng do thời tiết nóng ẩm và tần suất lật giở mượn đọc cao.  
    > - Khoảng cách địa lý tiếp cận tri thức: Sinh viên học tập tại cơ sở 2 (Linh Trung - Thủ Đức) phải di chuyển hơn 15km để mượn hoặc đọc trực tiếp các tài liệu giấy độc bản chỉ có ở cơ sở 1 (Quận 5).  
    > - Trải nghiệm đọc số hóa kém: Các tài liệu số hóa hiện tại chủ yếu là PDF scan ảnh tĩnh. Việc không hỗ trợ tự động co giãn dòng (reflowable) khiến sinh viên phải zoom liên tục khi đọc trên màn hình điện thoại di động."
  - [02-project-proposal.md](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/hcmus-projectmanage--lab/docs/02-project-proposal.md#L79-L95) — **Mục 2.1. Hành trình từ "Nỗi đau" vật lý...**:
    > "- Persona Độc giả (SV Nguyễn Văn Linh): Mất 3 tiếng di chuyển 15km từ Thủ Đức về Q.5 chỉ để đọc cuốn sách độc bản; tài liệu ố vàng; PDF scan không responsive làm giảm 80% hiệu suất học tập.  
    > - Persona Vận hành (Cô thủ thư Mai): Kho sách giấy chiếm trọn 100% diện tích thiết kế; ngốn 85% thời gian làm việc để tra tìm sách thủ công trong kho tối."
  - [04-feasibility-study.md](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/hcmus-projectmanage--lab/docs/04-feasibility-study.md#L50-L55) — **Mục 2. Lý do thực hiện**:
    > "1. Sự xuống cấp vật lý của tri thức: Hơn 40% giáo trình in cũ và tài liệu học thuật quý bản cứng đang bị rách hỏng.  
    > 2. Sự quá tải hạ tầng lưu trữ vật lý: Diện tích kho kệ sách giấy tại cơ sở 1 Quận 5 đã đạt ngưỡng tối đa 100%.  
    > 3. Trải nghiệm đọc số hóa nghèo nàn: File PDF scan ảnh tĩnh không responsive gây mỏi mắt."

---

### 1.2. So sánh đề xuất với các đối thủ cạnh tranh
- **Trạng thái:** ĐÃ CÓ TRONG TÀI LIỆU.
- **Trích dẫn chi tiết:**
  - [02-project-proposal.md](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/hcmus-projectmanage--lab/docs/02-project-proposal.md#L109-L111) — **Mục 2.3. Phân tích đối chuẩn: Đối thủ cạnh tranh**:
    > "Các giải pháp thư viện điện tử thương mại (như Lạc Việt Vebrary, DSpace thương mại) yêu cầu chi phí bản quyền và triển khai rất cao (thường từ 300 triệu đến hơn 1 tỷ VNĐ), vượt quá xa mức ngân sách giới hạn dưới 100 triệu VNĐ của dự án này. Hơn nữa, các hệ thống đóng này cực kỳ khó tùy biến để tích hợp quy trình sửa lỗi OCR Split-screen chuyên biệt cho tiếng Việt chuyên ngành, đồng thời không hỗ trợ cơ chế bảo mật DRM động thông qua Signed URL liên kết trực tiếp với LDAP của trường."
  - [03-vision-and-scope.md](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/hcmus-projectmanage--lab/docs/03-vision-and-scope.md#L295-L306) — **Mục 3.6. So sánh đối chuẩn quy trình nghiệp vụ (Workflow Benchmarking)**:
    > Bảng đối chiếu chỉ rõ giải pháp thương mại thương đối thủ: (1) Quét thủ công $\rightarrow$ Nhập metadata cồng kềnh; (2) Không tích hợp sẵn engine OCR tiếng Việt chuyên sâu; (3) Lưu trữ PDF tĩnh/EPUB tĩnh không tối ưu hiển thị; (4) Chi phí triển khai đắt đỏ 300M - 1 tỷ VNĐ.
  - [06-architecture.md](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/hcmus-projectmanage--lab/docs/06-architecture.md#L213-L217) — **Mục 4.1. Vì sao không sử dụng DSpace?**:
    > "DSpace là một kho lưu trữ số tĩnh, tối ưu cho việc lưu trữ file PDF và siêu dữ liệu (metadata)... DSpace hoàn toàn không hỗ trợ các luồng nghiệp vụ tương tác động phức tạp như: chạy OCR tự động, biên tập sửa lỗi chính tả trực quan so sánh song song với ảnh quét gốc trên giao diện web, và tự động biên dịch sang định dạng EPUB responsive thông qua Pandoc."

---

### 1.3. So sánh đề xuất với việc kết hợp các công cụ có sẵn để giải quyết vấn đề đặt ra
- **Trạng thái:** ĐÃ CÓ TRONG TÀI LIỆU.
- **Trích dẫn chi tiết:**
  - [02-project-proposal.md](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/hcmus-projectmanage--lab/docs/02-project-proposal.md#L112-L120) — **Mục 2.3. Phương án kết hợp công cụ có sẵn**:
    > "Phương án thay thế thủ công là sử dụng máy quét văn phòng $\rightarrow$ chạy phần mềm Abbyy FineReader offline $\rightarrow$ đóng gói EPUB bằng Calibre $\rightarrow$ chia sẻ qua Google Drive/OneDrive. Phương án này gặp 3 nút thắt lớn:  
    > 1. Quy trình rời rạc: Tốn từ 2-3 giờ lao động thủ công của thủ thư cho mỗi đầu sách.  
    > 2. Rủi ro bản quyền nghiêm trọng: Google Drive/OneDrive không có cơ chế chặn tải xuống tệp gốc, không chặn được chuột phải copy, và không có Signed URL tự động hết hạn sau 15 phút.  
    > 3. Tra cứu hạn chế: Không hỗ trợ cơ chế lập chỉ mục tìm kiếm toàn văn sâu đến từng trang sách như PostgreSQL Full-Text Search."
  - [03-vision-and-scope.md](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/hcmus-projectmanage--lab/docs/03-vision-and-scope.md#L295-L306) — **Mục 3.6. Workflow Benchmarking**:
    > Bảng so sánh chỉ rõ phương án kết hợp Abbyy + Drive có nỗ lực vận hành "Rất cao (2-3 giờ/cuốn)", dễ lỗi font khi convert Calibre và hoàn toàn không bảo mật DRM.

---

### 1.4. Phân tích các bên liên quan để làm rõ tính khả thi
- **Trạng thái:** ĐÃ CÓ TRONG TÀI LIỆU.
- **Trích dẫn chi tiết:**
  - [02-project-proposal.md](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/hcmus-projectmanage--lab/docs/02-project-proposal.md#L201-L228) — **Mục 5. Phân tích các bên liên quan và Phân vai (Stakeholders & RACI)**:
    > - Sponsor (Ban Giám hiệu): Phê duyệt chủ trương, cấp ngân sách CapEx/OpEx.  
    > - Client Nghiệp vụ (Ban Giám đốc Thư viện): Quản lý quy trình duyệt xuất bản, kiểm soát chất lượng dữ liệu, tổ chức sinh viên CTV.  
    > - Client Kỹ thuật (Phòng CNTT): Thiết lập hạ tầng VMware, cài đặt React/FastAPI/Postgres/MinIO, tích hợp Google OAuth 2.0.  
    > - Cố vấn Pháp lý (Pháp chế & Lưu trữ): Thẩm định quy chế bản quyền số hóa nội bộ.  
    > - Độc giả (Sinh viên/Giảng viên): Sử dụng tra cứu và đọc trực tuyến.
  - [04-feasibility-study.md](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/hcmus-projectmanage--lab/docs/04-feasibility-study.md#L74-L99) — **Mục 5.1. Đánh giá 8 khía cạnh khả thi**:
    > Phân tích tính khả thi cụ thể trên các khía cạnh: Pháp lý (tuân thủ Khoản 1 Điều 25 Luật SHTT), Kinh tế (Cost Avoidance tiết kiệm 35M/năm), Nguồn lực (4 kỹ sư CNTT kiêm nhiệm + 2 cán bộ Thư viện + SV CTV), Vận hành và Lịch trình.

---

### 1.5. Demo việc đánh giá tài liệu với sự trợ giúp của AI và xem xét bởi con người
- **Trạng thái:** [CHƯA CÓ TRONG 8 TÀI LIỆU GỐC - ĐỂ TRỐNG ĐỂ BỔ SUNG]
- **Nội dung bổ sung / Kịch bản Demo:**
  - 

---

## 2. PROJECT VISION AND SCOPE, PROJECT CHARTER, VÀ PRODUCT BACKLOG

### 2.1. So sánh quy trình nghiệp vụ với quy trình thủ công (As-Is vs To-Be)
- **Trạng thái:** ĐÃ CÓ TRONG TÀI LIỆU.
- **Trích dẫn chi tiết:**
  - [03-vision-and-scope.md](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/hcmus-projectmanage--lab/docs/03-vision-and-scope.md#L109-L195) — **Mục 2.3. Phân tích Quy trình Hiện tại (As-Is) và Quy trình Tương lai (To-Be)**:
    > - As-Is Workflow: Thủ thư quét photocopy thành PDF ảnh tĩnh $\rightarrow$ Upload lên Google Drive/File Server chia sẻ link công khai $\rightarrow$ Độc giả di chuyển 15km đến kho Q5 tra mã sách giấy hoặc đọc file PDF tĩnh phóng to co giãn thủ công trên di động.  
    > - To-Be Workflow: Scan máy chữ V $\rightarrow$ FastAPI BackgroundTasks (Tesseract OCR tiếng Việt ngầm) $\rightarrow$ Biên tập viên hiệu chỉnh chữ trên giao diện Split-screen đối chiếu ảnh-văn bản $\rightarrow$ Thủ thư duyệt 1-click xuất bản EPUB 3.0 (Pandoc) $\rightarrow$ Lập chỉ mục PostgreSQL FTS $\rightarrow$ Sinh viên tra cứu toàn văn < 3s & đọc qua MinIO Signed URL (15 phút).
  - [05-project-charter.md](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/hcmus-projectmanage--lab/docs/05-project-charter.md#L75-L83) — **Mục 5.1. Ma trận Tác nhân và Tác động As-is vs To-be**:
    > Bảng so sánh tác động trước và sau khi có hệ thống cho Ban Giám hiệu, Ban Giám đốc Thư viện, Thủ thư/Editor và Độc giả.

---

### 2.2. So sánh quy trình nghiệp vụ với quy trình của các đối thủ
- **Trạng thái:** ĐÃ CÓ TRONG TÀI LIỆU.
- **Trích dẫn chi tiết:**
  - [03-vision-and-scope.md](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/hcmus-projectmanage--lab/docs/03-vision-and-scope.md#L295-L306) — **Mục 3.6. So sánh đối chuẩn quy trình nghiệp vụ (Workflow Benchmarking)**:
    > Bảng đối chiếu 6 tiêu chí nghiệp vụ với Giải pháp thương mại đối thủ (Lạc Việt / DSpace):  
    > 1. Quét & Metadata: Đối thủ dùng module cồng kềnh $\leftrightarrow$ LDMS dùng máy scan chữ V + Dublin Core tự động.  
    > 2. OCR & Soát lỗi: Đối thủ không tích hợp sẵn engine OCR tiếng Việt $\leftrightarrow$ LDMS tích hợp OCR ngầm + Split-screen Workspace.  
    > 3. Đóng gói: Đối thủ lưu PDF gốc hoặc EPUB tĩnh $\leftrightarrow$ LDMS dùng Pandoc biên dịch EPUB 3.0 reflowable 1-click.  
    > 4. Tìm kiếm: Đối thủ tìm kiếm cơ bản hoặc Elasticsearch đắt đỏ $\leftrightarrow$ LDMS dùng PostgreSQL FTS siêu tốc < 3s.  
    > 5. Bảo mật DRM: Đối thủ phân phối PDF gốc dễ cào API $\leftrightarrow$ LDMS dùng Signed URL MinIO (hết hạn 15 phút).

---

### 2.3. So sánh quy trình nghiệp vụ với việc kết hợp các công cụ có sẵn một cách thủ công
- **Trạng thái:** ĐÃ CÓ TRONG TÀI LIỆU.
- **Trích dẫn chi tiết:**
  - [03-vision-and-scope.md](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/hcmus-projectmanage--lab/docs/03-vision-and-scope.md#L295-L306) — **Mục 3.6. Workflow Benchmarking (Cột "Kết hợp công cụ rời rạc")**:
    > - Quét & Metadata: Scan máy VP $\rightarrow$ Upload thủ công, không hỗ trợ Dublin Core.  
    > - OCR & Soát lỗi: Chạy OCR offline bằng Abbyy $\rightarrow$ Xuất text $\rightarrow$ Soát lỗi Word thủ công.  
    > - Đóng gói: Thủ thư dùng Calibre convert EPUB thủ công (dễ vỡ ảnh, lỗi font).  
    > - Tìm kiếm: Tìm tên file trên Google Drive, không tìm được nội dung bên trong.  
    > - Bảo mật: Google Drive chia sẻ link trực tiếp, dễ bị copy và phát tán trái phép.  
    > - Nỗ lực: Rất cao (Tốn 2-3 giờ/cuốn).

---

### 2.4. Phân tích các bên liên quan, trách nhiệm (R), trách nhiệm giải trình (A), khả năng tiếp cận (Accessibility), và mức độ ảnh hưởng (Influence)
- **Trạng thái:** ĐÃ CÓ TRONG TÀI LIỆU.
- **Trích dẫn chi tiết:**
  - **Trách nhiệm thực hiện (R) vs Trách nhiệm giải trình (A):**
    - [02-project-proposal.md](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/hcmus-projectmanage--lab/docs/02-project-proposal.md#L213-L228) & [05-project-charter.md](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/hcmus-projectmanage--lab/docs/05-project-charter.md#L90-L101) — **Mục Ma trận RACI**:
      > Đặc tả rõ từng gói WBS chỉ có duy nhất 1 đơn vị chịu trách nhiệm giải trình cuối cùng (**Accountable - A**):  
      > `WP1 (Khảo sát & Bản quyền):` **A** = Thư viện  
      > `WP2 (Backend & DB) & WP3 (UI & Reader):` **A** = Phòng CNTT  
      > `WP4 (Số hóa 2.500 sách):` **A** = Thư viện  
      > `WP5 (Kiểm thử UAT):` **A** = Phòng CNTT  
      > `WP6 (Triển khai & Vận hành):` **A** = Thư viện.
  - **Mức độ ảnh hưởng (Influence / Power-Interest):**
    - [05-project-charter.md](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/hcmus-projectmanage--lab/docs/05-project-charter.md#L84-L88) — **Mục 5.2. Bản đồ Stakeholder (Power/Interest Grid)**:
      > - Power cao, Interest cao (Quản trị sát sao): Ban GĐ Thư viện, Trưởng phòng CNTT (PM).  
      > - Power cao, Interest vừa (Giữ hài lòng): Ban Giám hiệu (Sponsor), Bộ phận Pháp chế.  
      > - Power thấp, Interest cao (Thông báo đầy đủ): Giảng viên, Sinh viên trường.
  - **Khả năng tiếp cận (Accessibility / Phân quyền RBAC):**
    - [03-vision-and-scope.md](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/hcmus-projectmanage--lab/docs/03-vision-and-scope.md#L232-L247) (Mục 2.3.4), [06-architecture.md](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/hcmus-projectmanage--lab/docs/06-architecture.md#L111-L150) (Mục 3 Use Case) & [06-architecture.md](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/hcmus-projectmanage--lab/docs/06-architecture.md#L397-L404) (Mục 5.1 Security Layers):
      > Phân quyền RBAC quy định rõ: Guest chỉ xem danh mục public; Reader (SV/GV) đọc sách bảo mật qua MinIO Signed URL (15m), không được download tệp EPUB gốc; Editor (CTV) chỉ được sửa text OCR trang được phân công; Librarian có quyền upload và phê duyệt xuất bản; Admin quản lý hệ thống.

---

### 2.5. Phân tích các tiêu chí chấp nhận cho từng yêu cầu (Acceptance Criteria)
- **Trạng thái:** ĐÃ CÓ TRONG TÀI LIỆU.
- **Trích dẫn chi tiết:**
  - [07-product-backlog.md](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/hcmus-projectmanage--lab/docs/07-product-backlog.md#L108-L446) — **Mục 2. Chi tiết Product Backlog — User Story & Acceptance Criteria**:
    > Đặc tả toàn bộ 26 User Stories với tiêu chí AC đo lường được (Given-When-Then / Checklist):  
    > - `LDMS-001:` Docker compose khởi động API + DB + MinIO healthy trong $\le$ 5 phút, `GET /health` trả 200 `{"status":"ok"}`.  
    > - `LDMS-014:` Trình đọc không có nút Download file gốc, EPUB serve qua Signed URL có `expires_in` 15 phút, sau 15 phút request bị từ chối 403.  
    > - `LDMS-015:` PostgreSQL FTS trả về kết quả chứa từ khóa cả trong tiêu đề lẫn nội dung `text_content` trang sách dưới 3 giây.

---

### 2.6. Demo việc đánh giá các tài liệu với sự trợ giúp của AI và xem xét bởi con người
- **Trạng thái:** [CHƯA CÓ TRONG 8 TÀI LIỆU GỐC - ĐỂ TRỐNG ĐỂ BỔ SUNG]
- **Nội dung bổ sung / Kịch bản Demo:**
  - 

---

## 3. ARCHITECTURE VÀ PROOF OF CONCEPT (PoC)

### 3.1. Demo và chứng minh technology stack lựa chọn hoạt động đúng kiến trúc đề ra
- **Trạng thái:** ĐÃ CÓ TRONG TÀI LIỆU.
- **Trích dẫn chi tiết:**
  - [06-architecture.md](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/hcmus-projectmanage--lab/docs/06-architecture.md#L160-L207) — **Mục 4. Góc nhìn logic (Logical View - C4 Model)**:
    > Sơ đồ phân lớp Kiến trúc Modular Monolith: Client Presentation (React SPA + Epub.js) $\rightarrow$ Security Layer (Nginx + Google OAuth) $\rightarrow$ Application Service (FastAPI + BackgroundTasks) $\rightarrow$ Domain Logic $\rightarrow$ Infrastructure (PostgreSQL FTS + MinIO S3).
  - [06-architecture.md](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/hcmus-projectmanage--lab/docs/06-architecture.md#L226-L240) — **Mục 4.2. Ngăn xếp công nghệ chi tiết (Technology Stack)**:
    > Bảng liệt kê phiên bản và lý do kỹ thuật chọn React 18, FastAPI (Python 3.11), PostgreSQL 16 (FTS), MinIO S3, Google OAuth 2.0, Docker Compose.
  - [06-architecture.md](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/hcmus-projectmanage--lab/docs/06-architecture.md#L550) — **Mục 9.3. PoC 2: Kiểm chứng tích hợp liên thông Tech Stack E2E**:
    > Kiểm chứng luồng gọi liên thông từ React SPA $\rightarrow$ FastAPI API $\rightarrow$ PostgreSQL DB $\rightarrow$ MinIO Signed URL $\rightarrow$ Epub.js Reader.

---

### 3.2. Demo và chứng minh bài toán khó nhất có thể được giải quyết
- **Trạng thái:** ĐÃ CÓ TRONG TÀI LIỆU.
- **Trích dẫn chi tiết:**
  - [06-architecture.md](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/hcmus-projectmanage--lab/docs/06-architecture.md#L550) — **Mục 9.2. PoC 1: Kiến trúc luồng xử lý OCR tiếng Việt bất đồng bộ (Hardest Core Feature)**:
    > - Bài toán khó nhất: Tác vụ OCR tài liệu lớn ngốn CPU (CPU-bound), nếu xử lý đồng bộ sẽ gây nghẽn toàn bộ Web Server (block Event Loop).  
    > - Giải pháp PoC 1: Khi nhận request OCR, FastAPI tạo tác vụ ngầm `FastAPI BackgroundTasks` và trả về HTTP 202 Accepted với `job_id` lập tức. Event Loop tiếp tục phục vụ request khác. Tiến trình ngầm gọi Tesseract OCR bóc tách tiếng Việt, lưu PostgreSQL và cập nhật trạng thái `completed`. Frontend Polling % tiến độ realtime.

---

## 4. DEVELOPMENT METHOD (PHƯƠNG PHÁP PHÁT TRIỂN)

### 4.1. Demo việc tạo mã nguồn tính năng, hoặc module, hoặc toàn hệ thống với sự trợ giúp của AI Coding Assistants
- **Trạng thái:** [CHƯA CÓ TRONG 8 TÀI LIỆU GỐC - ĐỂ TRỐNG ĐỂ BỔ SUNG]
- *(Ghi chú: Trong tài liệu `08-cost-time-resource.md` mục 5.2 có ghi nhận việc thu thập token AI qua `project_log.md`, nhưng kịch bản thao tác Demo trực tiếp việc sinh code bằng AI chưa viết chi tiết trong 8 file gốc).*
- **Nội dung bổ sung / Kịch bản Demo:**
  - 

---

### 4.2. Demo việc tích hợp mã nguồn hệ thống giữa các thành viên trong nhóm
- **Trạng thái:** ĐÃ CÓ QUY TRÌNH / [THAO TÁC DEMO TRỰC TIẾP ĐỂ TRỐNG ĐỂ BỔ SUNG].
- **Trích dẫn quy trình Git:**
  - [06-architecture.md](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/hcmus-projectmanage--lab/docs/06-architecture.md#L537-L547) — **Mục 8.2. Chiến lược nhánh Git (Git Branching Strategy)**:
    > "Dự án áp dụng mô hình GitFlow... Nhánh `main` (Production), `develop` (Tích hợp chính), `feature/*` (Tính năng riêng lẻ)... Developer tạo nhánh từ `develop`, hoàn tất code và unit test, sau đó tạo Pull Request (PR) gửi Tech Lead review trước khi Merge."
- **Nội dung bổ sung / Thao tác Demo tích hợp trực tiếp:**
  - 

---

## 5. SOFTWARE ESTIMATION, PLANNING VÀ MONITORING

### 5.1. Giải thích các ước lượng về thời gian, tài nguyên và chi phí của dự án với sự trợ giúp của AI Assistants
- **Trạng thái:** ĐÃ CÓ TRONG TÀI LIỆU.
- **Trích dẫn chi tiết:**
  - [08-cost-time-resource.md](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/hcmus-projectmanage--lab/docs/08-cost-time-resource.md#L70-L178) — **Mục 2. Phương pháp luận ước lượng nỗ lực phần mềm (UCP & COCOMO II)**:
    > - Mô hình UCP: UAW = 12, UUCW = 130 $\rightarrow$ UUCP = 142. TCF = 1.13, ECF = 0.785 $\rightarrow$ AUCP = 126 points. Nỗ lực quy đổi = 2.520 người-giờ ($\approx 15.75 \text{ PM}$). Tái sử dụng mã nguồn mở giúp nỗ lực thực tế viết mới giảm xuống **10.0 PM** ($\approx$ 5 tháng làm việc của 4 kỹ sư kiêm nhiệm 50%).  
    > - Mô hình COCOMO II: Viết mới 3.5 KLOC $\rightarrow \text{Effort\_New} \approx \mathbf{10.4\text{ PM}}$ (Khớp hoàn toàn với UCP).
  - [08-cost-time-resource.md](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/hcmus-projectmanage--lab/docs/08-cost-time-resource.md#L183-L202) — **Mục 3. Dự toán chi phí và Phân bổ ngân sách dự án (Cost & Budget Plan)**:
    > CapEx đầu tư ban đầu: 75.000.000 VNĐ – 95.000.000 VNĐ. OpEx duy trì định kỳ: 15.000.000 VNĐ – 30.000.000 VNĐ / năm.
  - [08-cost-time-resource.md](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/hcmus-projectmanage--lab/docs/08-cost-time-resource.md#L273-L314) — **Mục 5.3. Snapshot tiến độ thực tế & Chi phí AI Token**:
    > Ghi nhận dữ liệu thực tế Tuần 1: Dùng 440.000 tokens AI $\approx$ 300.000 VNĐ (chiếm 6% hạn mức CapEx AI Tools). Dự báo tốc độ Throughput $T = 12 \text{ stories/tuần} \rightarrow$ Hoàn thành các stories còn lại trong 2–4 tuần tiếp theo.

---

### 5.2. Giải thích bản kế hoạch của dự án
- **Trạng thái:** ĐÃ CÓ TRONG TÀI LIỆU.
- **Trích dẫn chi tiết:**
  - [05-project-charter.md](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/hcmus-projectmanage--lab/docs/05-project-charter.md#L103-L113) — **Mục 7. Cấu trúc phân rã công việc (WBS) và Tiến độ**:
    > Phân rã 6 gói công việc WBS (WP1 đến WP6) triển khai cuốn chiếu trong 20 tuần, go-live phiên bản MVP ở tuần 12.
  - [08-cost-time-resource.md](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/hcmus-projectmanage--lab/docs/08-cost-time-resource.md#L50-L67) — **Mục 1. Kế hoạch thời gian và Tiến độ thực hiện (Time & Schedule Plan)**:
    > - Lộ trình 4 Giai đoạn: GĐ 0 (Khảo sát Tuần 1-2), GĐ 1 (MVP Tuần 3-12), GĐ 2 (Số hóa diện rộng Tuần 13-18), GĐ 3 (Nghiệm thu Tuần 19-20).  
    > - Đường găng (Critical Path): **Gói công việc WP4 (Số hóa tài liệu)** là đường găng dự án do khâu scan và rà soát lỗi OCR phụ thuộc lớn vào năng suất con người.

---

### 5.3. Giải thích ý nghĩa của tài liệu phát biểu công việc (Statement of Work - SOW)
- **Trạng thái:** [CHƯA CÓ TRONG 8 TÀI LIỆU GỐC - ĐỂ TRỐNG ĐỂ BỔ SUNG]
- *(Ghi chú: Tài liệu 03 có Scope Statement và tài liệu 05/08 có WBS, nhưng chưa có mục riêng định nghĩa và giải thích ý nghĩa của SOW trong 8 file gốc).*
- **Nội dung bổ sung / Giải thích SOW:**
  - 

---

### 5.4. Demo việc thu thập dữ liệu dùng để báo cáo tình trạng dự án
- **Trạng thái:** ĐÃ CÓ MÔ HÌNH DỮ LIỆU / [THAO TÁC DEMO TRỰC TIẾP ĐỂ TRỐNG ĐỂ BỔ SUNG].
- **Trích dẫn mô hình dữ liệu:**
  - [08-cost-time-resource.md](file:///g:/HCMUS/NAM3-HK3/Management/Lab/W5/hcmus-projectmanage--lab/docs/08-cost-time-resource.md#L225-L271) — **Mục 5.1 & 5.2. Bộ chỉ số Giám sát & Cơ chế Session Logging**:
    > Sau mỗi phiên làm việc với AI, developer ghi 1 dòng log vào `project_log.md`: `[Ngày | Dev | Story ID | Tên Story | Thời gian | Token AI | Ghi chú]`. PM thu thập dữ liệu này để tính toán Throughput $T$ (số story Done/tuần), Cycle time và Velocity-based Forecast thời gian còn lại $N / T$.
- **Nội dung bổ sung / Thao tác Demo thu thập dữ liệu trực tiếp:**
  - 

---
