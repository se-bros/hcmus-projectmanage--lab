# Feature Specification: Highlight và ghi chú khi đọc sách (LDMS-021)

**Feature Branch**: `003-highlight-and-notes`
**Created**: 2026-08-12
**Status**: Draft
**Input**: User description: "Là độc giả, tôi muốn highlight đoạn văn và gắn ghi chú. Module M6 | Size M | Độ ưu tiên: Could | depends_on: LDMS-020. AC 1: Chọn đoạn text trên reader → tạo highlight → đoạn được đánh dấu và persist theo user+document. AC 2: Có thể gắn ghi chú text; GET lại còn ghi chú. AC 3: Xóa highlight → không còn trên UI sau reload."

**Bối cảnh**: Story LDMS-021 (`docs/07-product-backlog.md` §LDMS-021, hàng 24 của bảng roadmap) thuộc Module M6 — Reader, độ ưu tiên **Could**, phụ thuộc LDMS-020 (Bookmark). LDMS-020 đã thiết lập sẵn khuôn mẫu "trạng thái đọc riêng theo từng user trên từng document": bản ghi gắn theo cặp `(document_id, user)`, chỉ user sở hữu mới đọc được, và vị trí trong sách được lưu dưới dạng một chuỗi định vị do trình đọc EPUB sinh ra. Feature này mở rộng đúng khuôn mẫu đó từ **một** vị trí đọc dở sang **nhiều** vùng văn bản được đánh dấu, mỗi vùng kèm một ghi chú tùy chọn.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Tạo highlight cho đoạn văn đang đọc (Priority: P1)

Là độc giả đã đăng nhập và đang đọc một tài liệu đã xuất bản, tôi muốn bôi đen một đoạn văn bất kỳ trong sách và đánh dấu (highlight) đoạn đó, để khi quay lại đọc tiếp tôi nhận ra ngay những đoạn mình thấy quan trọng.

**Why this priority**: Đây là hạt nhân của cả story — hai AC còn lại (ghi chú, xóa) đều thao tác **trên** một highlight đã tồn tại, nên không có gì để ghi chú hay để xóa nếu chưa tạo được highlight. Chỉ riêng story này đã tự nó có giá trị sử dụng: độc giả đánh dấu được đoạn quan trọng và thấy lại sau khi mở lại sách, kể cả khi chưa bao giờ gõ một ghi chú nào.

**Independent Test**: Đăng nhập, mở một document đã `published` trên trang Reader, bôi đen một đoạn text và tạo highlight → đoạn đó đổi nền/được đánh dấu ngay trên màn hình → đóng trình duyệt, mở lại đúng document đó bằng cùng tài khoản → highlight vẫn còn, đúng đoạn văn cũ. Test được hoàn toàn độc lập với User Story 2 và 3.

**Acceptance Scenarios**:

1. **Given** độc giả đã đăng nhập và đang mở một document đã `published`, **When** bôi đen một đoạn text rồi chọn thao tác tạo highlight, **Then** đoạn text đó được đánh dấu trực quan ngay lập tức trên trình đọc.
2. **Given** vừa tạo highlight ở bước trên, **When** reload trang Reader (hoặc đóng và mở lại) với cùng tài khoản và cùng document, **Then** highlight hiển thị lại đúng đoạn văn đã đánh dấu, không lệch vị trí.
3. **Given** user A đã tạo highlight trên document X, **When** user B mở cùng document X, **Then** user B không nhìn thấy highlight của user A.
4. **Given** cùng một user đã tạo highlight trên document X, **When** user đó mở một document Y khác, **Then** highlight của document X không xuất hiện trên document Y.
5. **Given** độc giả **chưa** đăng nhập đang xem trang Reader, **When** bôi đen một đoạn text, **Then** hệ thống không cho tạo highlight và thông báo cần đăng nhập, không tạo bản ghi mồ côi cũng không lỗi hệ thống.
6. **Given** độc giả đã tạo nhiều highlight trong cùng một document, **When** mở lại document đó, **Then** tất cả highlight đã tạo đều hiển thị lại, không mất bản ghi nào.
7. **Given** đã có một highlight trên một đoạn văn, **When** độc giả bôi đen một vùng chồng lấn lên đoạn đó và tạo highlight mới, **Then** cả hai highlight cùng tồn tại độc lập, phần giao nhau hiển thị đậm hơn.
8. **Given** độc giả bôi đen một vùng bắt đầu ở chương này và kéo sang chương kế tiếp, **When** chọn thao tác tạo highlight, **Then** hệ thống từ chối kèm thông báo "chỉ đánh dấu được trong cùng một chương" và không tạo bản ghi nào.
9. **Given** độc giả bôi đen một vùng trải qua nhiều trang nhưng vẫn trong cùng một chương, **When** tạo highlight rồi đổi cỡ chữ làm nội dung dàn lại trang, **Then** highlight vẫn bám đúng đoạn văn ban đầu.

---

### User Story 2 - Gắn ghi chú vào highlight (Priority: P2)

Là độc giả, tôi muốn viết một ghi chú dạng text gắn vào đoạn đã highlight, để lưu lại suy nghĩ/diễn giải của mình về đoạn đó và đọc lại được về sau.

**Why this priority**: Đây là giá trị tăng thêm rõ rệt so với chỉ tô màu — biến đoạn đánh dấu thành ghi chép học tập. Nhưng nó phụ thuộc User Story 1 (phải có highlight để gắn vào), và nếu chưa làm thì highlight vẫn dùng được bình thường, nên xếp sau P1.

**Independent Test**: Trên một highlight đã tồn tại, mở ô nhập ghi chú, gõ nội dung và lưu → reload trang → mở lại chính highlight đó → nội dung ghi chú hiện đúng như đã gõ. Test độc lập với User Story 3 (không cần chức năng xóa).

**Acceptance Scenarios**:

1. **Given** một highlight đã tồn tại của chính user đang đăng nhập, **When** user nhập nội dung ghi chú và lưu, **Then** ghi chú được lưu gắn với đúng highlight đó.
2. **Given** ghi chú vừa được lưu, **When** reload trang Reader và mở lại highlight đó, **Then** nội dung ghi chú hiển thị lại đúng nguyên văn.
3. **Given** một highlight chưa có ghi chú, **When** user mở highlight đó, **Then** hiển thị trạng thái "chưa có ghi chú" và cho phép thêm, không hiển thị lỗi.
4. **Given** một highlight đã có ghi chú, **When** user sửa nội dung ghi chú và lưu lại, **Then** nội dung mới thay thế nội dung cũ sau khi reload.
5. **Given** một highlight đã có ghi chú, **When** user xóa sạch nội dung ghi chú và lưu, **Then** highlight vẫn còn nguyên trên sách, chỉ ghi chú bị gỡ bỏ.
6. **Given** user A đã gắn ghi chú vào highlight của mình, **When** user B mở cùng document, **Then** user B không đọc được ghi chú của user A.
7. **Given** độc giả đang soạn ghi chú, **When** nội dung vượt quá 2.000 ký tự và người dùng bấm lưu, **Then** hệ thống từ chối lưu, báo rõ số ký tự hiện tại, và giữ nguyên nội dung đang gõ để người dùng tự cắt ngắn.
8. **Given** hai highlight chồng lấn nhau, mỗi cái có ghi chú riêng, **When** độc giả mở từng highlight, **Then** mỗi highlight hiển thị đúng ghi chú của chính nó, không lẫn sang nhau.

---

### User Story 3 - Xóa highlight không cần nữa (Priority: P3)

Là độc giả, tôi muốn xóa một highlight đã đánh dấu nhầm hoặc không còn cần, để trang sách không bị rối bởi những đoạn đánh dấu thừa.

**Why this priority**: Là thao tác dọn dẹp, cần cho trải nghiệm dùng lâu dài nhưng không chặn giá trị chính. Nếu chưa có, độc giả vẫn tạo và ghi chú được bình thường — chỉ là không sửa được lỗi đánh dấu nhầm.

**Independent Test**: Tạo một highlight, chọn xóa → highlight biến mất khỏi màn hình ngay → reload trang Reader → highlight vẫn không xuất hiện trở lại. Test độc lập, chỉ cần chức năng tạo highlight của User Story 1.

**Acceptance Scenarios**:

1. **Given** một highlight của chính user đang hiển thị trên trang Reader, **When** user chọn thao tác xóa highlight đó, **Then** dấu highlight biến mất khỏi đoạn văn ngay lập tức.
2. **Given** highlight vừa bị xóa, **When** reload trang Reader với cùng user và cùng document, **Then** highlight đó không xuất hiện trở lại.
3. **Given** một highlight có kèm ghi chú, **When** user xóa highlight đó, **Then** ghi chú gắn theo nó cũng bị gỡ bỏ, không còn truy cập được và không để lại bản ghi mồ côi.
4. **Given** document có nhiều highlight, **When** user xóa đúng một highlight, **Then** các highlight còn lại vẫn nguyên vẹn sau reload.
5. **Given** user B biết định danh highlight của user A, **When** user B yêu cầu xóa highlight đó, **Then** hệ thống từ chối và highlight của user A vẫn còn nguyên.
6. **Given** một highlight nằm trong danh sách "không còn định vị được" sau khi tài liệu xuất bản lại, **When** độc giả chọn xóa nó, **Then** bản ghi bị gỡ khỏi danh sách và không quay lại sau reload.
7. **Given** hai highlight chồng lấn nhau, **When** độc giả xóa highlight nằm ngoài, **Then** highlight nằm trong vẫn còn nguyên kèm ghi chú của nó sau reload.

---

### Edge Cases

- **Chọn vùng rỗng hoặc chỉ toàn khoảng trắng**: bôi đen nhưng không dính ký tự có nghĩa nào (hoặc chỉ dính dấu cách/xuống dòng) → hệ thống phải từ chối tạo highlight, không tạo bản ghi rác.
- **Vùng chọn vắt qua nhiều trang trong cùng chương**: được chấp nhận và đánh dấu trọn vùng (FR-005a). Cần kiểm: đổi cỡ chữ làm số trang thay đổi thì highlight vẫn bám đúng đoạn văn cũ.
- **Vùng chọn vắt qua ranh giới chương**: bị từ chối kèm thông báo rõ ràng (FR-005b), không tạo bản ghi nào — kể cả bản ghi một phần cho riêng chương đầu.
- **Hai highlight chồng lấn nhau**: độc giả đánh dấu một câu nằm bên trong đoạn đã highlight trước đó → hai bản ghi cùng tồn tại, phần giao hiển thị đậm hơn (FR-004). Cần kiểm thêm: xóa highlight ngoài thì highlight trong vẫn còn nguyên kèm ghi chú của nó.
- **Đánh dấu trùng khít cùng một đoạn nhiều lần**: bôi đen đúng vùng đã highlight rồi tạo tiếp → theo FR-004 vẫn sinh bản ghi mới; giao diện phải cho độc giả chọn được đúng highlight mình muốn ghi chú/xóa khi nhiều vùng nằm chồng nhau.
- **Ghi chú quá dài**: độc giả dán vào ô ghi chú một khối text vượt 2.000 ký tự → hệ thống từ chối lưu và báo rõ số ký tự đang có (FR-009), không cắt cụt âm thầm cũng không lỗi hệ thống. Nội dung vừa gõ không bị mất trắng để độc giả tự cắt ngắn lại được.
- **Tài liệu được xuất bản lại (re-publish/re-OCR) sau khi đã có highlight**: bản EPUB mới làm chuỗi định vị cũ không còn trỏ đúng đoạn văn → highlight rơi xuống danh sách "không còn định vị được", kèm nguyên ghi chú (FR-011, FR-011a). Cần kiểm: một document có cả highlight dựng lại được lẫn highlight hỏng thì hiển thị đồng thời được cả hai nhóm.
- **Document bị xóa**: toàn bộ highlight và ghi chú gắn với document đó phải bị dọn theo, không để lại bản ghi trỏ tới tài liệu không còn tồn tại.
- **Highlight đã bị xóa ở tab khác**: user mở hai tab cùng một document, xóa highlight ở tab 1 rồi thao tác lên chính highlight đó ở tab 2 → hệ thống báo lỗi rõ ràng ("highlight không còn tồn tại"), không lỗi hệ thống.
- **Thay đổi cỡ chữ/theme khi đọc (LDMS-019)**: độc giả tăng giảm cỡ chữ làm chữ dàn lại trang → highlight phải vẫn bám đúng đoạn văn gốc, không nhảy sang đoạn khác.
- **Document chưa xuất bản hoặc không có bản đọc**: không có nội dung để chọn → chức năng highlight không khả dụng, nhất quán với hành vi Reader hiện có.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: Hệ thống MUST cho phép độc giả **đã đăng nhập** tạo highlight từ một vùng văn bản do chính họ chọn trên trang Reader của một tài liệu đã xuất bản.
- **FR-002**: Hệ thống MUST lưu mỗi highlight gắn với đúng bộ ba: người dùng tạo ra nó, tài liệu chứa nó, và vị trí vùng văn bản trong tài liệu — đủ để dựng lại đúng vùng đã đánh dấu ở lần mở sau.
- **FR-003**: Hệ thống MUST lưu kèm mỗi highlight phần văn bản đã được chọn tại thời điểm tạo, để độc giả vẫn nhận ra mình đã đánh dấu nội dung gì kể cả khi vùng đó không dựng lại được trên bản sách hiện tại.
- **FR-004**: Hệ thống MUST cho phép các highlight chồng lấn nhau tồn tại song song như những bản ghi độc lập. Vùng chọn mới chồng lên highlight đã có sẽ tạo ra một highlight riêng, không gộp và không thay đổi highlight cũ; phần giao nhau được thể hiện trực quan đậm hơn để độc giả nhận ra có nhiều lớp đánh dấu. Mỗi highlight giữ ghi chú riêng của nó, và xóa một highlight không ảnh hưởng tới highlight nào chồng lấn với nó.
- **FR-005**: Hệ thống MUST từ chối tạo highlight khi vùng chọn rỗng hoặc chỉ chứa khoảng trắng, kèm thông báo rõ ràng cho người dùng.
- **FR-005a**: Hệ thống MUST cho phép một highlight trải qua nhiều trang hiển thị, vì trang chỉ là đơn vị dàn chữ và thay đổi theo cỡ chữ độc giả chọn (LDMS-019) nên không phải ranh giới ổn định.
- **FR-005b**: Hệ thống MUST giới hạn mỗi highlight nằm gọn trong **một chương**. Khi vùng chọn vượt qua ranh giới chương, hệ thống từ chối tạo và báo rõ "chỉ đánh dấu được trong cùng một chương", không tự cắt vùng chọn thành nhiều bản ghi.
- **FR-006**: Hệ thống MUST hiển thị lại toàn bộ highlight của người dùng hiện tại trên đúng vùng văn bản tương ứng mỗi khi họ mở lại tài liệu đó.
- **FR-007**: Người dùng MUST be able to gắn một ghi chú dạng văn bản vào một highlight của chính mình, sửa nội dung ghi chú đó, và gỡ bỏ ghi chú mà không làm mất highlight.
- **FR-008**: Hệ thống MUST trả lại nguyên văn nội dung ghi chú đã lưu khi người dùng mở lại highlight tương ứng.
- **FR-009**: Hệ thống MUST giới hạn nội dung ghi chú ở tối đa **2.000 ký tự**. Khi độc giả nhập vượt quá, hệ thống báo lỗi rõ ràng kèm số ký tự hiện tại và từ chối lưu — không cắt bớt nội dung mà không báo. Giao diện nhập ghi chú SHOULD hiển thị số ký tự còn lại khi người dùng tiến gần giới hạn.
- **FR-010**: Người dùng MUST be able to xóa một highlight của chính mình; sau khi xóa, highlight đó không còn hiển thị và không quay lại sau khi tải lại trang.
- **FR-011**: Hệ thống MUST giữ lại highlight có vị trí không dựng lại được trên bản sách hiện tại, thay vì xóa. Những highlight này không được tô lên trang sách nữa, mà hiển thị trong một danh sách riêng ("Đánh dấu không còn định vị được") ngay trong trang Reader, sử dụng phần văn bản đã lưu ở FR-003 để độc giả nhận ra mình từng đánh dấu nội dung gì.
- **FR-011a**: Ghi chú gắn với các highlight nói trên MUST vẫn đọc được đầy đủ trong danh sách riêng đó — độc giả không mất ghi chú vì tài liệu được xuất bản lại.
- **FR-011b**: Người dùng MUST be able to xóa một highlight không còn định vị được, giống như xóa highlight bình thường, để tự dọn danh sách này.
- **FR-011c**: Hệ thống MUST không tự động dò tìm lại vị trí mới cho highlight hỏng bằng cách so khớp nội dung văn bản. Việc tự bám lại nằm ngoài phạm vi story này (xem Assumptions).
- **FR-012**: Hệ thống MUST giới hạn mọi thao tác đọc, sửa và xóa highlight/ghi chú trong phạm vi người dùng sở hữu chúng; người dùng khác không được đọc, sửa hay xóa, kể cả khi biết định danh của bản ghi.
- **FR-013**: Hệ thống MUST xóa toàn bộ highlight và ghi chú gắn với một tài liệu khi tài liệu đó bị xóa khỏi hệ thống.
- **FR-014**: Hệ thống MUST giữ highlight bám đúng vùng văn bản gốc khi độc giả thay đổi cỡ chữ hoặc chế độ sáng/tối làm nội dung dàn lại trang.
- **FR-015**: Hệ thống MUST từ chối mọi thao tác tạo/sửa/xóa highlight từ người dùng chưa đăng nhập, kèm thông báo yêu cầu đăng nhập.

### Key Entities

- **Highlight**: Một vùng văn bản do độc giả đánh dấu trong một tài liệu. Thuộc về đúng một người dùng và đúng một tài liệu; mang thông tin vị trí vùng văn bản trong sách, bản sao phần văn bản đã chọn, và thời điểm tạo/cập nhật. Một tài liệu có thể chứa nhiều highlight của cùng một người dùng. Bị xóa theo khi tài liệu bị xóa.
- **Ghi chú (Note)**: Nội dung văn bản do độc giả viết, gắn vào đúng một Highlight. Là tùy chọn — một Highlight có thể không có ghi chú nào. Bị gỡ bỏ khi Highlight tương ứng bị xóa. Có giới hạn độ dài (xem FR-009).
- **Người dùng (Reader)**: Chủ sở hữu của Highlight và Ghi chú, xác định qua danh tính đăng nhập. Là ranh giới phân tách dữ liệu — dùng chung khuôn mẫu định danh mà LDMS-020 (Bookmark) đã thiết lập.
- **Tài liệu (Document)**: Sách đã xuất bản mà độc giả đang đọc; là ngữ cảnh chứa Highlight. Đã tồn tại sẵn từ các story trước, feature này không thay đổi nó.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: 100% highlight đã tạo hiển thị lại đúng vùng văn bản ban đầu sau khi độc giả tải lại trang Reader, trong điều kiện bản sách không thay đổi.
- **SC-002**: 100% ghi chú đã lưu trả về đúng nguyên văn nội dung khi đọc lại, không sai lệch ký tự.
- **SC-003**: 100% highlight đã xóa không xuất hiện trở lại sau khi tải lại trang.
- **SC-004**: 0 trường hợp một người dùng nhìn thấy, sửa được hoặc xóa được highlight/ghi chú của người dùng khác, kiểm bằng kịch bản hai tài khoản trên cùng một tài liệu.
- **SC-005**: Độc giả hoàn tất thao tác từ lúc bôi đen đoạn văn tới lúc thấy đoạn được đánh dấu trong vòng 3 giây, không phải rời khỏi trang đang đọc.
- **SC-006**: Trang Reader mở kèm đầy đủ highlight đã lưu mà không làm chậm thời điểm đọc được nội dung sách quá 1 giây so với khi không có highlight nào, với tài liệu có tới 50 highlight.
- **SC-007**: 0 lỗi hệ thống (5xx/màn trắng) trên toàn bộ các tình huống biên đã liệt kê ở mục Edge Cases.
- **SC-008**: 0 highlight và 0 ghi chú bị mất sau khi tài liệu được xuất bản lại — mọi bản ghi không dựng lại được vị trí đều còn truy cập được kèm nguyên văn ghi chú, kiểm bằng kịch bản đếm số bản ghi trước và sau khi re-publish.

## Assumptions

- **Highlight là dữ liệu riêng tư của từng độc giả**, không chia sẻ và không hiển thị cho người dùng khác. Suy ra từ AC 1 ("persist theo user+document") và từ tiền lệ LDMS-020 AC 3 (bookmark của user này không lộ sang user khác). Chia sẻ highlight giữa các độc giả nằm ngoài phạm vi story này.
- **Chỉ hỗ trợ một kiểu đánh dấu duy nhất** (một màu mặc định). Backlog không nhắc tới việc chọn màu hay phân loại nhãn, nên nhiều màu/nhãn được coi là ngoài phạm vi.
- **Mỗi highlight có nhiều nhất một ghi chú.** AC 2 nói "gắn ghi chú" ở dạng số ít; nhiều ghi chú cho một highlight (dạng thảo luận) không thuộc phạm vi.
- **Ghi chú chỉ là văn bản thuần**, không định dạng đậm/nghiêng, không đính kèm ảnh hay tệp.
- **Chỉ áp dụng trên tài liệu đã xuất bản (`published`) mở qua trang Reader**, đúng phạm vi Module M6. Màn hình biên tập (Module M3, LDMS-006/017) không thuộc phạm vi story này.
- **Tái sử dụng cơ chế đăng nhập và cách định danh người dùng đã có** từ LDMS-009/LDMS-020, không thêm cách xác thực mới.
- **Tái sử dụng cách định vị vị trí trong sách mà LDMS-020 đã dùng cho bookmark** để mô tả vùng văn bản của highlight, thay vì đặt ra một hệ định vị mới.
- **Không tự động bám lại vị trí (re-anchor) khi sách đổi bản.** Việc so khớp nội dung văn bản để tìm lại đúng đoạn trên bản EPUB mới bị loại khỏi phạm vi (FR-011c): OCR chạy lại thường đổi chính tả nên dễ bám nhầm đoạn, và chi phí vượt quá một story Size M / ưu tiên Could. Nếu về sau thấy cần, đây là ứng viên cho một story riêng trong roadmap.
- **Chương là ranh giới ổn định của một highlight**, còn trang thì không — trang phụ thuộc cỡ chữ độc giả chọn (LDMS-019). Đây là cơ sở của FR-005a/FR-005b.
- **Chưa cần màn hình "danh sách tất cả highlight/ghi chú" tách riêng** hay xuất ghi chú ra file. AC chỉ yêu cầu highlight và ghi chú sống trên chính trang Reader; các tính năng tổng hợp thuộc về roadmap sau (LDMS-024 Citation và nhóm story Could khác).
- **Không có yêu cầu làm việc offline**; độc giả được giả định đang có kết nối khi tạo/sửa/xóa highlight.
- **LDMS-020 (Bookmark) đã hoàn thành** và trang Reader đã hoạt động với EPUB thật — đây là điều kiện `depends_on` ghi trong backlog.
