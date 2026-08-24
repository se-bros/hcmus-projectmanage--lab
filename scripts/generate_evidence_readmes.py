import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EVIDENCE_DIR = os.path.join(BASE_DIR, "docs.1", "evidence")

QUESTIONS_DATA = [
    {
        "num": 1,
        "num_str": "01",
        "title": "Đề xuất dự án (Project Proposal)",
        "english_title": "Project Proposal",
        "question_prompt": "Trình bày quá trình hình thành và phương pháp đánh giá tài liệu Đề xuất dự án (Project Proposal) của nhóm. _(Sinh viên nộp kèm bản in tài liệu Đề xuất dự án của nhóm.)_",
        "submissions": [
            {
                "name": "Bản in tài liệu Đề xuất dự án (Project Proposal)",
                "type": "Tài liệu in A4",
                "local_file": "01-project-proposal.pdf",
                "source_md": "../../md/01-project-proposal.md",
                "source_pdf": "../../pdf/01-project-proposal.pdf",
                "desc": "Tài liệu đề xuất dự án mô tả vấn đề tại Thư viện HCMUS, các bên liên quan, giải pháp 4 use case cốt lõi, so sánh 3 đối thủ và quyết định đề xuất."
            }
        ],
        "key_evidence": [
            "Bối cảnh & Vấn đề: 50.000 đầu sách, tài liệu quý chưa được số hóa, quy trình mượn đọc thủ công hạn chế tiếp cận.",
            "3 Sản phẩm đối chuẩn: DSpace, Koha, Calibre-Web (so sánh chi phí, tính phức tạp và khả năng tích hợp OCR tiếng Việt).",
            "4 Use cases cốt lõi: Tiếp nhận tài liệu, Nhận dạng OCR tiếng Việt, Hiệu chỉnh 2 cột, Đọc sách EPUB trực tuyến.",
            "Quyết định đề xuất: Chấp thuận triển khai phiên bản thử nghiệm môn học 11 tuần."
        ],
        "blueprint": {
            "what": "Tài liệu khởi tạo nhằm chứng minh vấn đề của Thư viện HCMUS là đáng giải quyết và đề xuất giải pháp khả thi.",
            "how": "Khảo sát hiện trạng thư viện → Phân tích đối thủ cạnh tranh → Xác định phạm vi và 4 use case cốt lõi → Soạn thảo Proposal → Đánh giá nội bộ và thông qua quyết định đề xuất.",
            "why": "Tránh lãng phí nguồn lực vào các giải pháp không khả thi hoặc không đúng nhu cầu của thư viện.",
            "evidence": "Chỉ vào Bảng so sánh đối thủ cạnh tranh (Mục 2.3) và Bảng phạm vi đề xuất (Mục 3.3) trong bản in Proposal."
        },
        "related_links": [
            "[Tài liệu Markdown (docs.1/md/01-project-proposal.md)](../../md/01-project-proposal.md)",
            "[Tài liệu PDF (docs.1/pdf/01-project-proposal.pdf)](../../pdf/01-project-proposal.pdf)",
            "[Phiếu ôn tập Câu 1 (final-exam/preparation/1_Initiation_Charter_Feasibility/README.md)](../../../final-exam/preparation/1_Initiation_Charter_Feasibility/README.md)"
        ]
    },
    {
        "num": 2,
        "num_str": "02",
        "title": "Viễn cảnh và phạm vi dự án (Project Vision and Scope)",
        "english_title": "Project Vision and Scope",
        "question_prompt": "Trình bày quá trình hình thành và phương pháp đánh giá tài liệu Viễn cảnh và phạm vi dự án (Project Vision and Scope) của nhóm. _(Sinh viên nộp kèm bản in tài liệu Viễn cảnh và phạm vi dự án của nhóm.)_",
        "submissions": [
            {
                "name": "Bản in tài liệu Viễn cảnh và phạm vi (Vision & Scope Document)",
                "type": "Tài liệu in A4",
                "local_file": "02-vision-and-scope.pdf",
                "source_md": "../../md/02-vision-and-scope.md",
                "source_pdf": "../../pdf/02-vision-and-scope.pdf",
                "desc": "Tài liệu mô tả tuyên bố viễn cảnh, người dùng mục tiêu, phân tích As-Is vs To-Be, ranh giới In-Scope (15 Bắt buộc, 6 Nên có) và Out-of-Scope (5 Có thể xem xét)."
            }
        ],
        "key_evidence": [
            "Tuyên bố viễn cảnh (Vision Statement) cho độc giả và thủ thư ĐH Khoa học Tự nhiên.",
            "Phân tích hiện trạng As-Is vs tương lai To-Be (số hóa tự động, tìm kiếm toàn văn, bảo vệ bản quyền tệp EPUB).",
            "Ranh giới phạm vi rõ ràng: In-Scope (15 Must + 6 Should) và Out-of-Scope (5 Could: lưu bookmark đám mây, highlight nâng cao...).",
            "NFR định hướng: Thời gian phản hồi tìm kiếm < 2s, thời gian xử lý OCR < 30s/trang."
        ],
        "blueprint": {
            "what": "Tài liệu định hình ranh giới mong muốn của sản phẩm, kết nối mục tiêu kinh doanh với yêu cầu kỹ thuật.",
            "how": "Xác định chân dung người dùng (User Personas) → Khảo sát quy trình As-Is → Thiết kế quy trình To-Be → Phân định In-scope / Out-of-scope → Review cùng Stakeholder.",
            "why": "Chống Scope Creep (phình phạm vi) và bảo đảm nhóm tập trung vào các tính năng mang lại giá trị cốt lõi trong 11 tuần.",
            "evidence": "Chỉ vào Sơ đồ As-Is / To-Be và Bảng phân định In-Scope / Out-of-Scope trong bản in Vision & Scope."
        },
        "related_links": [
            "[Tài liệu Markdown (docs.1/md/02-vision-and-scope.md)](../../md/02-vision-and-scope.md)",
            "[Tài liệu PDF (docs.1/pdf/02-vision-and-scope.pdf)](../../pdf/02-vision-and-scope.pdf)",
            "[Phiếu ôn tập Câu 2 (final-exam/preparation/2_Requirements_Scope_SoW/README.md)](../../../final-exam/preparation/2_Requirements_Scope_SoW/README.md)"
        ]
    },
    {
        "num": 3,
        "num_str": "03",
        "title": "Ủy nhiệm dự án (Project Charter)",
        "english_title": "Project Charter",
        "question_prompt": "Trình bày quá trình hình thành và phương pháp đánh giá tài liệu Ủy nhiệm dự án (Project Charter) của nhóm. _(Sinh viên nộp kèm bản in tài liệu Ủy nhiệm dự án của nhóm.)_",
        "submissions": [
            {
                "name": "Bản in tài liệu Ủy nhiệm dự án (Project Charter)",
                "type": "Tài liệu in A4",
                "local_file": "03-project-charter.pdf",
                "source_md": "../../md/03-project-charter.md",
                "source_pdf": "../../pdf/03-project-charter.pdf",
                "desc": "Tài liệu phê duyệt chính thức khởi động dự án, xác lập mục tiêu SMART, quyền hạn PM, ma trận RACI 6 thành viên, 6 mốc tiến độ chính (Milestones)."
            }
        ],
        "key_evidence": [
            "Mục tiêu SMART: Triển khai hệ thống LDMS trong 11 tuần, hỗ trợ xử lý số hóa tài liệu mẫu, độ chính xác OCR > 85%.",
            "Quyền hạn PM: Điều phối công việc, phê duyệt Pull Request, quản lý thay đổi phạm vi.",
            "Ma trận RACI: Phân định rõ R (Responsible), A (Accountable), C (Consulted), I (Informed) cho 6 thành viên.",
            "6 Mốc Milestones: M1 Khởi tạo → M2 Yêu cầu & Kiến trúc → M3 OCR & Core Backend → M4 Giao diện & EPUB → M5 Tích hợp CI/CD & Test → M6 Nghiệm thu."
        ],
        "blueprint": {
            "what": "Văn bản chính thức cấp quyền cho Project Manager sử dụng nguồn lực tổ chức để thực hiện dự án.",
            "how": "Kế thừa Proposal & Vision → Xác định mục tiêu SMART → Thiết lập ma trận RACI và 6 Milestones → Ký phê duyệt điều lệ.",
            "why": "Tạo cam kết chính thức giữa các bên, phân quyền rõ ràng để tránh tranh chấp quyền hạn trong quá trình thực thi.",
            "evidence": "Chỉ vào Ma trận RACI (Mục 3) và Bảng 6 Milestones (Mục 4) trong bản in Project Charter."
        },
        "related_links": [
            "[Tài liệu Markdown (docs.1/md/03-project-charter.md)](../../md/03-project-charter.md)",
            "[Tài liệu PDF (docs.1/pdf/03-project-charter.pdf)](../../pdf/03-project-charter.pdf)",
            "[Phiếu ôn tập Câu 3 (final-exam/preparation/1_Initiation_Charter_Feasibility/README.md)](../../../final-exam/preparation/1_Initiation_Charter_Feasibility/README.md)"
        ]
    },
    {
        "num": 4,
        "num_str": "04",
        "title": "Yêu cầu phần mềm (Software Requirements / Product Backlog)",
        "english_title": "Software Requirements & Product Backlog",
        "question_prompt": "Trình bày quá trình hình thành và phương pháp đánh giá tài liệu Yêu cầu phần mềm (Software Requirements, hay Product Backlog) của nhóm. _(Sinh viên nộp kèm bản in tài liệu Yêu cầu phần mềm và bản in tài liệu Hướng dẫn sử dụng hệ thống của nhóm.)_",
        "submissions": [
            {
                "name": "Bản in tài liệu Yêu cầu phần mềm (SRS)",
                "type": "Tài liệu in A4",
                "local_file": "04-software-requirements.pdf",
                "source_md": "../../md/04-software-requirements.md",
                "source_pdf": "../../pdf/04-software-requirements.pdf",
                "desc": "Đặc tả 26 yêu cầu chức năng (YC-001..026), 10 yêu cầu phi chức năng (YCP-01..10) và ma trận truy vết 1:1."
            },
            {
                "name": "Bản in tài liệu Danh mục công việc (Product Backlog)",
                "type": "Tài liệu in A4",
                "local_file": "04-product-backlog.pdf",
                "source_md": "../../md/04-product-backlog.md",
                "source_pdf": "../../pdf/04-product-backlog.pdf",
                "desc": "Danh mục 26 User Stories (LDMS-001..026), ưu tiên 15 Must, 6 Should, 5 Could, Acceptance Criteria chi tiết, DoR và DoD."
            },
            {
                "name": "Bản in tài liệu Hướng dẫn sử dụng hệ thống (User Guide)",
                "type": "Tài liệu in A4",
                "local_file": "04-user-guide.pdf",
                "source_md": "../../md/04-user-guide.md",
                "source_pdf": "../../pdf/04-user-guide.pdf",
                "desc": "Hướng dẫn chi tiết quy trình sử dụng giao diện theo vai trò: Quản trị viên, Thủ thư, Biên tập viên và Độc giả."
            }
        ],
        "key_evidence": [
            "26 User Stories phân bổ: 15 Bắt buộc (Must), 6 Nên có (Should), 5 Có thể xem xét (Could).",
            "Cấu trúc Story chuẩn: `As a <role>, I want <goal>, so that <benefit>` + Acceptance Criteria kiểm thử được.",
            "Quy tắc DoR (Definition of Ready) và DoD (Definition of Done) cho từng card công việc.",
            "Hướng dẫn sử dụng đầy đủ các bước thao tác trên màn hình: Đăng nhập, Tải sách, OCR, Sửa văn bản 2 cột, Xuất bản, Tìm kiếm và Đọc EPUB."
        ],
        "blueprint": {
            "what": "SRS/Backlog là tập hợp các chức năng và ràng buộc của hệ thống; User Guide là tài liệu hướng dẫn người dùng cuối vận hành.",
            "how": "Phân tích nghiệp vụ thư viện → Viết 26 User Stories → Xác định Acceptance Criteria → Xây dựng User Guide theo vai trò → Review và nghiệm thu.",
            "why": "Đảm bảo đội phát triển hiểu đúng yêu cầu và người dùng có tài liệu tham khảo chuẩn mực khi sử dụng.",
            "evidence": "Chỉ vào Bảng 26 User Stories trong Backlog và các luồng thao tác cụ thể trong bản in Hướng dẫn sử dụng."
        },
        "related_links": [
            "[Tài liệu SRS (docs.1/md/04-software-requirements.md)](../../md/04-software-requirements.md)",
            "[Tài liệu Product Backlog (docs.1/md/04-product-backlog.md)](../../md/04-product-backlog.md)",
            "[Tài liệu User Guide (docs.1/md/04-user-guide.md)](../../md/04-user-guide.md)",
            "[Phiếu ôn tập Câu 4 (final-exam/preparation/2_Requirements_Scope_SoW/README.md)](../../../final-exam/preparation/2_Requirements_Scope_SoW/README.md)"
        ]
    },
    {
        "num": 5,
        "num_str": "05",
        "title": "Kiến trúc phần mềm (Software Architecture)",
        "english_title": "Software Architecture",
        "question_prompt": "Trình bày quá trình hình thành và phương pháp đánh giá tài liệu Kiến trúc phần mềm (Software Architecture) của nhóm. _(Sinh viên nộp kèm bản in tài liệu Kiến trúc phần mềm của nhóm.)_",
        "submissions": [
            {
                "name": "Bản in tài liệu Kiến trúc phần mềm (Software Architecture Document)",
                "type": "Tài liệu in A4",
                "local_file": "05-software-architecture.pdf",
                "source_md": "../../md/05-software-architecture.md",
                "source_pdf": "../../pdf/05-software-architecture.pdf",
                "desc": "Tài liệu kiến trúc mô hình C4, sơ đồ tuần tự xử lý, mô hình an toàn dữ liệu, phân rã module máy chủ và 10 quyết định ADR."
            },
            {
                "name": "Bản in tài liệu Nhật ký quyết định kiến trúc (ADR Log)",
                "type": "Tài liệu in A4",
                "local_file": "A1-decision-log-and-adr.pdf",
                "source_md": "../../md/A1-decision-log-and-adr.md",
                "source_pdf": "../../pdf/A1-decision-log-and-adr.pdf",
                "desc": "10 quyết định kiến trúc quan trọng (ADR-01 đến ADR-10) giải thích lý do lựa chọn công nghệ và đánh giá đánh đổi."
            }
        ],
        "key_evidence": [
            "Mô hình C4: C4 mức 1 Bối cảnh, C4 mức 2 Vùng chứa (Frontend React, API FastAPI, PostgreSQL, MinIO).",
            "Tech Stack: Backend Python FastAPI, Frontend React, Storage MinIO (S3-compatible), OCR Tesseract 5, CSDL PostgreSQL.",
            "Bảo mật: Xác thực JWT token, phân quyền RBAC ở máy chủ, bảo vệ tệp EPUB bằng Presigned URLs.",
            "10 Quyết định kiến trúc ADR (ADR-01 đến ADR-10) giải thích lý do lựa chọn công nghệ."
        ],
        "blueprint": {
            "what": "Bản thiết kế cấu trúc hệ thống, phân rã thành phần, giao tiếp giữa các module và cơ chế bảo mật.",
            "how": "Phân tích NFR từ SRS → Lựa chọn Tech Stack phù hợp → Vẽ mô hình C4 PlantUML → Thiết kế sơ đồ tuần tự và bảo mật → Ghi nhận ADR.",
            "why": "Đảm bảo tính mở rộng, hiệu năng, bảo mật và tính khả thi trong việc tích hợp nhiều thành phần phức tạp (OCR, EPUB, CSDL).",
            "evidence": "Chỉ vào Sơ đồ C4 Vùng chứa (Mục 4) và Sơ đồ tuần tự Upload-OCR trong bản in Kiến trúc phần mềm."
        },
        "related_links": [
            "[Tài liệu Kiến trúc (docs.1/md/05-software-architecture.md)](../../md/05-software-architecture.md)",
            "[Nhật ký ADR (docs.1/md/A1-decision-log-and-adr.md)](../../md/A1-decision-log-and-adr.md)",
            "[Phiếu ôn tập Câu 5 (final-exam/preparation/3_Architecture_PoC_Prototype/README.md)](../../../final-exam/preparation/3_Architecture_PoC_Prototype/README.md)"
        ]
    },
    {
        "num": 6,
        "num_str": "06",
        "title": "Chứng minh ý tưởng (Proof of Concept)",
        "english_title": "Proof of Concept (PoC)",
        "question_prompt": "Trình bày quá trình hình thành và phương pháp đánh giá sản phẩm Chứng minh ý tưởng (Proof of Concept) của nhóm. _(Sinh viên nộp kèm bản in giao diện thể hiện đầu vào và đầu ra khi chạy mã nguồn Chứng minh ý tưởng của nhóm.)_",
        "submissions": [
            {
                "name": "Bản in giao diện đầu vào/đầu ra PoC 1 (OCR tiếng Việt) và MinIO Storage",
                "type": "Ảnh chụp thực nghiệm",
                "local_file": "poc1_split-screen-view.png",
                "source_md": "N/A",
                "source_pdf": "N/A",
                "desc": "Tập hợp 8 ảnh chụp màn hình thực nghiệm PoC 1: input scan, xử lý OCR, kết quả trích xuất văn bản và lưu trữ MinIO."
            },
            {
                "name": "Bản in giao diện đầu vào/đầu ra PoC 2 (Trình đọc EPUB Reader & Stream)",
                "type": "Ảnh chụp thực nghiệm",
                "local_file": "poc2_epub-exported.png",
                "source_md": "N/A",
                "source_pdf": "N/A",
                "desc": "Tập hợp 5 ảnh chụp màn hình thực nghiệm PoC 2: đóng gói EPUB, stream dữ liệu qua presigned URL 900s và hiển thị reader."
            },
            {
                "name": "Ảnh chụp kết quả chạy kiểm thử tự động PoC (Pytest Pass)",
                "type": "Ảnh chụp console",
                "local_file": "test-passed.png",
                "source_md": "N/A",
                "source_pdf": "N/A",
                "desc": "Minh chứng toàn bộ unit tests kiểm chứng PoC chạy thành công 100%."
            }
        ],
        "key_evidence": [
            "PoC 1 (OCR Engine): Đánh giá Tesseract 5 với bộ ngôn ngữ `vie.traineddata`, xử lý tiền xử lý ảnh đạt độ chính xác > 85%.",
            "PoC 2 (EPUB Reader Web): Đánh giá thư viện ePub.js, stream dữ liệu từ MinIO qua Presigned URL 900s.",
            "Tiêu chí nghiệm thu PoC: Thời gian xử lý < 30s/trang, RAM < 512MB, không lộ direct download link."
        ],
        "blueprint": {
            "what": "Thực nghiệm kỹ thuật quy mô nhỏ nhằm kiểm chứng các rủi ro công nghệ lớn nhất trước khi xây dựng toàn hệ thống.",
            "how": "Nhận diện 2 rủi ro kỹ thuật cao nhất (OCR & EPUB Reader) → Xây dựng mã nguồn PoC độc lập → Chạy thử nghiệm với dữ liệu mẫu → Đo lường kết quả → Đánh giá Go/No-go.",
            "why": "Giảm thiểu rủi ro kiến trúc thất bại ở giai đoạn muộn của dự án.",
            "evidence": "Chỉ vào Ảnh chụp Input/Output của PoC OCR và PoC EPUB Reader trong thư mục evidence."
        },
        "related_links": [
            "[Mục 8 PoC trong Kiến trúc phần mềm (docs.1/md/05-software-architecture.md)](../../md/05-software-architecture.md)",
            "[Phiếu ôn tập Câu 6 (final-exam/preparation/3_Architecture_PoC_Prototype/README.md)](../../../final-exam/preparation/3_Architecture_PoC_Prototype/README.md)"
        ]
    },
    {
        "num": 7,
        "num_str": "07",
        "title": "Bản mẫu (Prototype)",
        "english_title": "Prototype",
        "question_prompt": "Trình bày quá trình hình thành và phương pháp đánh giá sản phẩm Bản mẫu (Prototype) của nhóm. _(Sinh viên nộp kèm bản in phác thảo giao diện ban đầu cho hệ thống của nhóm.)_",
        "submissions": [
            {
                "name": "Bản in phác thảo giao diện Màn hình Biên tập OCR 2 cột",
                "type": "Ảnh chụp giao diện",
                "local_file": "split-screen-editor.png",
                "source_md": "N/A",
                "source_pdf": "N/A",
                "desc": "Thiết kế biên tập 2 cột: cột trái xem trang scan gốc, cột phải trình soạn thảo văn bản nhận dạng."
            },
            {
                "name": "Bản in phác thảo giao diện Trình đọc sách trực tuyến cho Độc giả",
                "type": "Ảnh chụp giao diện",
                "local_file": "web-reader.png",
                "source_md": "N/A",
                "source_pdf": "N/A",
                "desc": "Giao diện đọc sách EPUB tối ưu trải nghiệm đọc, tìm kiếm toàn văn và mục lục."
            },
            {
                "name": "Bản in Dashboard OCR, Phân quyền RBAC và Lịch sử xử lý",
                "type": "Ảnh chụp giao diện",
                "local_file": "dashboard-ocr.png",
                "source_md": "N/A",
                "source_pdf": "N/A",
                "desc": "Màn hình quản lý tiến trình số hóa, phân quyền và lịch sử thao tác."
            }
        ],
        "key_evidence": [
            "Màn hình Đăng nhập: Thiết kế điều hướng theo vai trò (Role-based Navigation).",
            "Màn hình Biên tập viên: Thiết kế song song 2 cột (Side-by-side) — Cột trái xem ảnh scan gốc phóng to/thu nhỏ, Cột phải trình soạn thảo văn bản nhận dạng.",
            "Màn hình Độc giả: Thanh tìm kiếm toàn văn trực quan, bộ lọc danh mục và giao diện đọc sách EPUB tối ưu trên Desktop/Mobile.",
            "Phản hồi từ người dùng: Cải tiến thao tác phím tắt chuyển trang nhanh (Next/Prev Page) trong màn hình hiệu chỉnh."
        ],
        "blueprint": {
            "what": "Bản mô phỏng trực quan trải nghiệm người dùng (UI/UX) giúp các bên liên quan hình dung sản phẩm thực tế.",
            "how": "Phác thảo Wireframe giấy → Thiết kế Prototype số hóa → Trình bày cho đại diện Thư viện lấy ý kiến → Tinh chỉnh luồng giao diện → Đưa vào Backlog.",
            "why": "Phát hiện sớm các vấn đề về khả năng sử dụng (Usability) trước khi tốn công lập trình Frontend.",
            "evidence": "Chỉ vào Bản in phác thảo giao diện Màn hình Biên tập 2 cột và Giao diện Độc giả."
        },
        "related_links": [
            "[Tài liệu Hướng dẫn sử dụng (docs.1/md/04-user-guide.md)](../../md/04-user-guide.md)",
            "[Phiếu ôn tập Câu 7 (final-exam/preparation/3_Architecture_PoC_Prototype/README.md)](../../../final-exam/preparation/3_Architecture_PoC_Prototype/README.md)"
        ]
    },
    {
        "num": 8,
        "num_str": "08",
        "title": "Báo cáo tính khả thi (Feasibility Study Report)",
        "english_title": "Feasibility Study Report",
        "question_prompt": "Trình bày quá trình hình thành và phương pháp đánh giá tài liệu Báo cáo tính khả thi (Feasibility Study Report) của nhóm. _(Sinh viên nộp kèm bản in tài liệu Báo cáo tính khả thi của nhóm.)_",
        "submissions": [
            {
                "name": "Bản in tài liệu Báo cáo tính khả thi (Feasibility Study Report)",
                "type": "Tài liệu in A4",
                "local_file": "08-feasibility-study.pdf",
                "source_md": "../../md/08-feasibility-study.md",
                "source_pdf": "../../pdf/08-feasibility-study.pdf",
                "desc": "Đánh giá 8 loại khả thi theo khung TELOS, phân tích chi phí - lợi ích (CBA) và kết luận khả thi có điều kiện."
            }
        ],
        "key_evidence": [
            "Khung TELOS 5 chiều: Technical (Kỹ thuật), Economic (Kinh tế), Legal (Pháp lý), Operational (Vận hành), Schedule (Lịch trình).",
            "Kỹ thuật: PoC chứng minh Tesseract và ePub.js khả thi trong giới hạn tài nguyên.",
            "Kinh tế: Dự án tận dụng hạ tầng mã nguồn mở, không phát sinh chi phí bản quyền thương mại.",
            "Kết luận: Dự án đạt tính khả thi có điều kiện trong phạm vi môn học 11 tuần."
        ],
        "blueprint": {
            "what": "Tài liệu phân tích đa chiều nhằm xác định dự án có thể thực hiện thành công với các ràng buộc về kỹ thuật, tài chính, thời gian và pháp lý hay không.",
            "how": "Thu thập dữ liệu từ Proposal & PoC → Phân tích 8 khía cạnh khả thi theo TELOS → Tính toán CBA → Nhận diện rào cản và đề xuất điều kiện khả thi → Kết luận Go/No-go.",
            "why": "Đưa ra quyết định đầu tư có căn cứ khoa học, bảo vệ nhóm khỏi việc cam kết những mục tiêu bất khả thi.",
            "evidence": "Chỉ vào Bảng đánh giá TELOS (Mục 3) và Bảng kết luận khả thi có điều kiện trong bản in Báo cáo tính khả thi."
        },
        "related_links": [
            "[Tài liệu Markdown (docs.1/md/08-feasibility-study.md)](../../md/08-feasibility-study.md)",
            "[Tài liệu PDF (docs.1/pdf/08-feasibility-study.pdf)](../../pdf/08-feasibility-study.pdf)",
            "[Phiếu ôn tập Câu 8 (final-exam/preparation/1_Initiation_Charter_Feasibility/README.md)](../../../final-exam/preparation/1_Initiation_Charter_Feasibility/README.md)"
        ]
    },
    {
        "num": 9,
        "num_str": "09",
        "title": "Định nghĩa quy trình phát triển phần mềm (Software Process Definition)",
        "english_title": "Software Process Definition",
        "question_prompt": "Trình bày quá trình hình thành và phương pháp đánh giá tài liệu Định nghĩa quy trình phát triển phần mềm (Software Process Definition) của nhóm. _(Sinh viên nộp kèm bản in tài liệu Định nghĩa quy trình phát triển phần mềm của nhóm.)_",
        "submissions": [
            {
                "name": "Bản in tài liệu Định nghĩa quy trình phát triển phần mềm",
                "type": "Tài liệu in A4",
                "local_file": "09-software-process-definition.pdf",
                "source_md": "../../md/09-software-process-definition.md",
                "source_pdf": "../../pdf/09-software-process-definition.pdf",
                "desc": "Quy định quy trình Kanban 6 cột, chính sách giới hạn WIP (WIP Limits), quy tắc DoR / DoD và chiến lược nhánh Trunk-Based Development."
            }
        ],
        "key_evidence": [
            "Bảng Kanban 6 cột: Backlog → Ready → In Progress → In Review → Testing → Done.",
            "WIP Limits nghiêm ngặt: In Progress ≤ 3, In Review ≤ 2, Testing ≤ 2 nhằm tránh nghẽn luồng và tăng thông lượng.",
            "Quy tắc chuyển cột: Tiêu chí đầu vào DoR và tiêu chí hoàn thành DoD rõ ràng cho từng bước.",
            "Chiến lược phân nhánh Trunk-Based Development: Nhánh `main` luôn deploy được, nhánh tính năng tồn tại ngắn < 2 ngày."
        ],
        "blueprint": {
            "what": "Văn bản hóa toàn bộ quy chuẩn làm việc, luồng di chuyển công việc và quy tắc phối hợp kỹ thuật của đội ngũ phát triển.",
            "how": "Phân tích đặc thù dự án 11 tuần → Chọn mô hình Agile/Kanban kết hợp Trunk-Based → Thiết lập bảng 6 cột và WIP limits → Ban hành DoR/DoD → Tích hợp vào GitHub Project.",
            "why": "Chuẩn hóa cách làm việc, giảm thời gian lãng phí, phát hiện sớm điểm nghẽn và duy trì nhịp độ phát triển bền vững.",
            "evidence": "Chỉ vào Bảng Kanban 6 cột kèm WIP limits (Mục 3) và Quy tắc Trunk-Based (Mục 5) trong bản in Quy trình."
        },
        "related_links": [
            "[Tài liệu Markdown (docs.1/md/09-software-process-definition.md)](../../md/09-software-process-definition.md)",
            "[Tài liệu PDF (docs.1/pdf/09-software-process-definition.pdf)](../../pdf/09-software-process-definition.pdf)",
            "[Phiếu ôn tập Câu 9 (final-exam/preparation/4_Estimation_Planning_Process/README.md)](../../../final-exam/preparation/4_Estimation_Planning_Process/README.md)"
        ]
    },
    {
        "num": 10,
        "num_str": "10",
        "title": "Ước lượng dự án (Project Estimate)",
        "english_title": "Project Estimate",
        "question_prompt": "Trình bày quá trình hình thành và phương pháp đánh giá tài liệu Ước lượng dự án (Project Estimate) của nhóm. _(Sinh viên nộp kèm bản in tài liệu Ước lượng dự án của nhóm.)_",
        "submissions": [
            {
                "name": "Bản in tài liệu Ước lượng dự án (Project Estimate)",
                "type": "Tài liệu in A4",
                "local_file": "10-project-estimate.pdf",
                "source_md": "../../md/10-project-estimate.md",
                "source_pdf": "../../pdf/10-project-estimate.pdf",
                "desc": "Ước lượng Bottom-up từ kết quả làm thử, áp dụng hệ số dự phòng 2,5, tính toán Demand 190 giờ và đối chiếu Capacity 198 giờ."
            }
        ],
        "key_evidence": [
            "Phương pháp ước lượng Bottom-up dựa trên kết quả làm thử thực tế (spike test ngày 16-17/07/2026).",
            "Hệ số dự phòng rủi ro kỹ thuật và học tập: 2,5× trên thời gian làm thử.",
            "Tổng thời gian yêu cầu (Demand): 190 giờ cho 15 hạng mục Bắt buộc.",
            "Năng lực đáp ứng (Capacity): 198 giờ (6 thành viên × 3 giờ/tuần × 11 tuần) đảm bảo tính khả thi cao."
        ],
        "blueprint": {
            "what": "Tài liệu dự báo tổng khối lượng công việc, thời gian và công sức cần thiết để hoàn thành phạm vi cam kết.",
            "how": "Phân rã 15 Must stories thành task kỹ thuật → Thực hiện làm thử đo thời gian gốc → Nhân hệ số dự phòng 2,5 → Tính tổng Demand → Đối chiếu với Capacity của 6 thành viên.",
            "why": "Đảm bảo kế hoạch dự án dựa trên dữ liệu thực nghiệm, tránh ước lượng cảm tính dẫn đến trễ hạn.",
            "evidence": "Chỉ vào Bảng phân tích Demand vs Capacity và Bảng kết quả làm thử trong bản in Ước lượng dự án."
        },
        "related_links": [
            "[Tài liệu Markdown (docs.1/md/10-project-estimate.md)](../../md/10-project-estimate.md)",
            "[Tài liệu PDF (docs.1/pdf/10-project-estimate.pdf)](../../pdf/10-project-estimate.pdf)",
            "[Phiếu ôn tập Câu 10 (final-exam/preparation/4_Estimation_Planning_Process/README.md)](../../../final-exam/preparation/4_Estimation_Planning_Process/README.md)"
        ]
    },
    {
        "num": 11,
        "num_str": "11",
        "title": "Kế hoạch dự án (Project Plan)",
        "english_title": "Project Plan",
        "question_prompt": "Trình bày quá trình hình thành và phương pháp đánh giá tài liệu Kế hoạch dự án (Project Plan) của nhóm. _(Sinh viên nộp kèm bản in tài liệu Kế hoạch dự án của nhóm.)_",
        "submissions": [
            {
                "name": "Bản in tài liệu Kế hoạch dự án (Project Plan)",
                "type": "Tài liệu in A4",
                "local_file": "11-project-plan.pdf",
                "source_md": "../../md/11-project-plan.md",
                "source_pdf": "../../pdf/11-project-plan.pdf",
                "desc": "Kế hoạch tích hợp 11 tuần, cấu trúc phân rã công việc WBS 5 pha, phân bổ nguồn lực, quản lý phụ thuộc và ngân sách."
            }
        ],
        "key_evidence": [
            "WBS 5 Pha: 1. Khởi tạo & Yêu cầu → 2. Thiết kế Kiến trúc & PoC → 3. Xây dựng Core & Giao diện → 4. Tích hợp & Kiểm thử → 5. Chuyển giao & Nghiệm thu.",
            "Lịch trình 11 tuần đồng bộ với 6 Milestones trong Project Charter.",
            "Kế hoạch phân bổ nhân sự 6 thành viên theo chuyên môn (Backend, Frontend, DevOps, QA).",
            "Đường găng (Critical Path): Luồng xử lý OCR và Trình đọc EPUB Reader."
        ],
        "blueprint": {
            "what": "Bản kế hoạch tổng thể tích hợp phạm vi, thời gian, nhân lực, chi phí và chất lượng để định hướng thực thi dự án.",
            "how": "Xây dựng WBS từ Backlog → Sắp xếp thứ tự phụ thuộc và xác định đường găng → Phân bổ 11 tuần theo milestone → Gán trách nhiệm cho thành viên → Thiết lập cơ chế kiểm soát.",
            "why": "Đảm bảo mọi thành viên nắm rõ công việc, tiến độ, sự phụ thuộc lẫn nhau để phối hợp nhịp nhàng hướng tới mục tiêu chung.",
            "evidence": "Chỉ vào Cây WBS (Mục 3) và Lịch trình 11 tuần (Mục 4) trong bản in Kế hoạch dự án."
        },
        "related_links": [
            "[Tài liệu Markdown (docs.1/md/11-project-plan.md)](../../md/11-project-plan.md)",
            "[Tài liệu PDF (docs.1/pdf/11-project-plan.pdf)](../../pdf/11-project-plan.pdf)",
            "[Phiếu ôn tập Câu 11 (final-exam/preparation/4_Estimation_Planning_Process/README.md)](../../../final-exam/preparation/4_Estimation_Planning_Process/README.md)"
        ]
    },
    {
        "num": 12,
        "num_str": "12",
        "title": "Bản mô tả công việc (Statement of Work)",
        "english_title": "Statement of Work (SOW)",
        "question_prompt": "Trình bày quá trình hình thành và phương pháp đánh giá tài liệu Phát biểu công việc (Statement of Work) của nhóm. _(Sinh viên nộp kèm bản in tài liệu Phát biểu công việc của nhóm.)_",
        "submissions": [
            {
                "name": "Bản in tài liệu Bản mô tả công việc (Statement of Work - SOW)",
                "type": "Tài liệu in A4",
                "local_file": "12-statement-of-work.pdf",
                "source_md": "../../md/12-statement-of-work.md",
                "source_pdf": "../../pdf/12-statement-of-work.pdf",
                "desc": "Tài liệu cam kết phạm vi bàn giao, 5 nhóm sản phẩm bàn giao (Deliverables), tiêu chí nghiệm thu và quy trình quản lý thay đổi."
            }
        ],
        "key_evidence": [
            "5 Nhóm Deliverables bàn giao: (1) Bộ mã nguồn & Docker Compose, (2) Bộ tài liệu kỹ thuật & quản lý, (3) Bộ dữ liệu mẫu, (4) Báo cáo kiểm thử, (5) Hướng dẫn sử dụng.",
            "Tiêu chí nghiệm thu rõ ràng: 100% 15 Must stories đạt DoD, hệ thống chạy ổn định trên môi trường demo.",
            "Quy trình quản lý thay đổi (Change Control): Yêu cầu thay đổi phải được đánh giá tác động và phê duyệt trước khi áp dụng.",
            "Bảng ký xác nhận nội bộ của 6 thành viên nhóm Sebros."
        ],
        "blueprint": {
            "what": "Văn bản quy định chi tiết phạm vi công việc, sản phẩm bàn giao, tiêu chuẩn nghiệm thu và điều kiện hoàn thành dự án.",
            "how": "Tổng hợp yêu cầu từ Charter, SRS và Plan → Cụ thể hóa 5 nhóm Deliverables → Thiết lập tiêu chí nghiệm thu → Quy định quy trình Change Control → Ký duyệt xác nhận.",
            "why": "Ngăn ngừa tranh chấp về sản phẩm bàn giao, làm căn cứ pháp lý/học thuật để đánh giá kết quả nghiệm thu cuối kỳ.",
            "evidence": "Chỉ vào Bảng 5 nhóm Deliverables (Mục 3) và Bảng ký xác nhận nội bộ (Mục 7) trong bản in SOW."
        },
        "related_links": [
            "[Tài liệu Markdown (docs.1/md/12-statement-of-work.md)](../../md/12-statement-of-work.md)",
            "[Tài liệu PDF (docs.1/pdf/12-statement-of-work.pdf)](../../pdf/12-statement-of-work.pdf)",
            "[Phiếu ôn tập Câu 12 (final-exam/preparation/2_Requirements_Scope_SoW/README.md)](../../../final-exam/preparation/2_Requirements_Scope_SoW/README.md)"
        ]
    },
    {
        "num": 13,
        "num_str": "13",
        "title": "Mô hình tích hợp liên tục (Continuous Integration)",
        "english_title": "Continuous Integration (CI)",
        "question_prompt": "Vẽ và giải thích mô hình tích hợp liên tục (Continuous Integration) của nhóm. Ghi chú trên mô hình các công cụ nhóm đã dùng cho từng thành phần. Tại sao cần sử dụng hệ thống tích hợp liên tục cho dự án? _(Sinh viên nộp kèm bản in kịch bản build (build scripts), bản in giao diện email nhận thông báo về kết quả build tự động, và bản in tài liệu Hướng dẫn cài đặt công cụ và biên dịch mã nguồn hệ thống cho máy tính của nhà phát triển của nhóm.)_",
        "submissions": [
            {
                "name": "Bản in kịch bản CI Build Scripts (.github/workflows/ci.yml)",
                "type": "Kịch bản CI (Code printout)",
                "local_file": "ci.yml",
                "source_md": "../../.github/workflows/ci.yml",
                "source_pdf": "N/A",
                "desc": "Kịch bản tự động hóa GitHub Actions thực hiện format check, linting, unit test backend/frontend và validate Terraform."
            },
            {
                "name": "Bản in ảnh chụp GitHub Actions CI chạy thành công (CI-pass.png)",
                "type": "Ảnh chụp màn hình",
                "local_file": "CI-pass.png",
                "source_md": "N/A",
                "source_pdf": "N/A",
                "desc": "Ảnh chụp thực tế tất cả các jobs CI trên GitHub Actions đều pass 100%."
            },
            {
                "name": "Bản in giao diện email nhận thông báo kết quả build tự động (Mail.png)",
                "type": "Ảnh chụp giao diện email",
                "local_file": "Mail.png",
                "source_md": "N/A",
                "source_pdf": "N/A",
                "desc": "Ảnh chụp email Brevo gửi tự động thông báo kết quả build sau mỗi lần merge vào nhánh main."
            },
            {
                "name": "Bản in tài liệu Hướng dẫn cài đặt và biên dịch mã nguồn (Developer Guide)",
                "type": "Tài liệu in A4",
                "local_file": "06-developer-guide.md",
                "source_md": "06-developer-guide.md",
                "source_pdf": "N/A",
                "desc": "Tài liệu chuẩn hóa các bước cài đặt môi trường dev, chạy Docker, cài thư viện và biên dịch mã nguồn."
            }
        ],
        "key_evidence": [
            "Mô hình CI: Developer Commit → Push PR → GitHub Actions kích hoạt 4 jobs song song: (1) Backend Ruff/Pytest, (2) Frontend ESLint/Next Build, (3) Terraform Validate, (4) Notify Email qua Brevo API.",
            "Kịch bản `.github/workflows/ci.yml` có sẵn trong repo, thiết lập ma trận kiểm tra tự động.",
            "Lợi ích CI: Phát hiện lỗi tích hợp ngay trong vòng 3 phút, bảo đảm nhánh `main` luôn ở trạng thái biên dịch thành công.",
            "Developer Guide chuẩn: Các bước `docker compose up -d`, `npm ci`, `pytest` được chuẩn hóa."
        ],
        "blueprint": {
            "what": "Thực hành phát triển phần mềm trong đó các thành viên tích hợp mã nguồn thường xuyên vào nhánh chính, mỗi lần tích hợp được kiểm tra tự động bằng build và test.",
            "how": "Cấu hình GitHub Actions runner → Thiết lập jobs linting, testing, validation → Tích hợp dịch vụ gửi email Brevo qua Webhook/Action → Ban hành Developer Guide.",
            "why": "Loại bỏ 'Integration Hell' (địa ngục tích hợp vào cuối kỳ), tăng độ tin cậy và tốc độ phát triển của nhóm.",
            "evidence": "Chỉ vào Bản in file `ci.yml`, Ảnh chụp màn hình CI-pass và Email thông báo thực tế."
        },
        "related_links": [
            "[Kịch bản CI (.github/workflows/ci.yml)](../../../.github/workflows/ci.yml)",
            "[Developer Guide (docs/03-execution-monitoring/06-developer-guide.md)](../../../docs/03-execution-monitoring/06-developer-guide.md)",
            "[Phiếu ôn tập Câu 13 (final-exam/preparation/5_CICD_DevOps_Testing/README.md)](../../../final-exam/preparation/5_CICD_DevOps_Testing/README.md)"
        ]
    },
    {
        "num": 14,
        "num_str": "14",
        "title": "Mô hình chuyển giao liên tục (Continuous Delivery)",
        "english_title": "Continuous Delivery (CD)",
        "question_prompt": "Vẽ và giải thích mô hình chuyển giao liên tục (Continuous Delivery) của nhóm. Ghi chú trên mô hình các công cụ nhóm đã dùng cho từng thành phần. Tại sao cần sử dụng hệ thống chuyển giao liên tục cho dự án? _(Sinh viên nộp kèm bản in kịch bản triển khai (deployment scripts), kịch bản cấu hình cơ sở dữ liệu, cấu hình các dịch vụ bên thứ ba, bản in giao diện email nhận thông báo về kết quả triển khai tự động, và bản in tài liệu Hướng dẫn triển khai hệ thống cho kỹ sư vận hành của nhóm.)_",
        "submissions": [
            {
                "name": "Bản in kịch bản triển khai (Deployment Scripts) — cd.yml, docker-compose.prod.yml",
                "type": "Kịch bản CD (Code printout)",
                "local_file": "cd.yml",
                "source_md": "../../.github/workflows/cd.yml",
                "source_pdf": "N/A",
                "desc": "Kịch bản tự động hóa quy trình đóng gói container, chạy migration và deploy lên hạ tầng Staging/Production."
            },
            {
                "name": "Bản in cấu hình Docker Compose Production (docker-compose.prod.yml)",
                "type": "Kịch bản cấu hình",
                "local_file": "docker-compose.prod.yml",
                "source_md": "../../docker-compose.prod.yml",
                "source_pdf": "N/A",
                "desc": "Cấu hình Docker Compose Production, Nginx reverse proxy, PostgreSQL, MinIO S3 bucket, Prometheus và Grafana."
            },
            {
                "name": "Bản in giao diện email nhận thông báo kết quả triển khai tự động",
                "type": "Ảnh chụp giao diện email",
                "local_file": "cd-brevo-deploy-email-live-url-terraform.png",
                "source_md": "N/A",
                "source_pdf": "N/A",
                "desc": "Ảnh chụp email Brevo gửi tự động xác nhận deploy thành công kèm đường link Live URL của hệ thống."
            },
            {
                "name": "Bản in tài liệu Hướng dẫn triển khai hệ thống cho kỹ sư vận hành (Deployment Guide)",
                "type": "Tài liệu in A4",
                "local_file": "07-deployment-guide.md",
                "source_md": "07-deployment-guide.md",
                "source_pdf": "N/A",
                "desc": "Quy trình vận hành, thiết lập biến môi trường, chạy migration Alembic, smoke test và kịch bản Rollback khi có lỗi."
            },
            {
                "name": "Bản in ảnh chụp GitHub Actions CD deploy và Live URL thực tế",
                "type": "Ảnh chụp màn hình",
                "local_file": "cd-workflow-deploy.png",
                "source_md": "N/A",
                "source_pdf": "N/A",
                "desc": "Minh chứng thực tế pipeline CD chạy pass và live URL hệ thống."
            }
        ],
        "key_evidence": [
            "Mô hình CD: CI Pass → Build Docker Images → Provisioning → Apply Database Migrations (Alembic) → Deploy Containers → Smoke Test tự động → Gửi Email Live URL.",
            "Kịch bản triển khai: `cd.yml`, `scripts/run-prod.sh`, `docker-compose.prod.yml`.",
            "Chiến lược Rollback: Tự động giữ bản backup CSDL trước migration, hỗ trợ rollback phiên bản container trước đó trong < 2 phút.",
            "Bằng chứng Live URL và email thông báo thực tế từ Brevo."
        ],
        "blueprint": {
            "what": "Mở rộng của CI nhằm đảm bảo mã nguồn sau khi vượt qua kiểm tra có thể tự động triển khai an toàn lên môi trường vận hành.",
            "how": "Tự động hóa đóng gói container → Áp dụng IaC Terraform → Chạy migration cơ sở dữ liệu có kiểm soát → Kích hoạt smoke test → Gửi thông báo kết quả qua email.",
            "why": "Rút ngắn thời gian đưa tính năng mới tới người dùng (Time-to-Market), giảm thiểu rủi ro lỗi thao tác thủ công khi triển khai.",
            "evidence": "Chỉ vào File `cd.yml`, File `docker-compose.prod.yml`, Ảnh chụp Live URL và Email thông báo deploy."
        },
        "related_links": [
            "[Kịch bản CD (.github/workflows/cd.yml)](../../../.github/workflows/cd.yml)",
            "[Deployment Guide (docs/03-execution-monitoring/07-deployment-guide.md)](../../../docs/03-execution-monitoring/07-deployment-guide.md)",
            "[Phiếu ôn tập Câu 14 (final-exam/preparation/5_CICD_DevOps_Testing/README.md)](../../../final-exam/preparation/5_CICD_DevOps_Testing/README.md)"
        ]
    },
    {
        "num": 15,
        "num_str": "15",
        "title": "Mô hình DevOps",
        "english_title": "DevOps Model & Operations",
        "question_prompt": "Vẽ và giải thích mô hình DevOps của nhóm. Ghi chú trên mô hình các công cụ nhóm đã dùng cho từng thành phần. Tại sao cần sử dụng quy trình DevOps cho dự án? Giải thích quy trình phát triển, triển khai và vận hành liên tục đồng thời nhiều phiên bản trên của dự án bằng cách áp dụng DevOps. _(Sinh viên nộp kèm bản in kịch bản khởi tạo và cấu hình tài nguyên hạ tầng cho việc triển khai hệ thống của nhóm, bản in hệ thống thư mục và tệp tin hỗ trợ quản lý hạ tầng triển khai.)_",
        "submissions": [
            {
                "name": "Bản in kịch bản khởi tạo tài nguyên hạ tầng Terraform (terraform_main.tf)",
                "type": "Kịch bản IaC (Code printout)",
                "local_file": "terraform_main.tf",
                "source_md": "../../terraform/main.tf",
                "source_pdf": "N/A",
                "desc": "Kịch bản Terraform định nghĩa toàn bộ tài nguyên Docker network, volume, container PostgreSQL, MinIO, Prometheus và Grafana."
            },
            {
                "name": "Bản in biến và đầu ra Terraform (terraform_variables.tf, terraform_outputs.tf)",
                "type": "Kịch bản IaC",
                "local_file": "terraform_outputs.tf",
                "source_md": "../../terraform/outputs.tf",
                "source_pdf": "N/A",
                "desc": "Khai báo biến cấu hình hạ tầng và trích xuất tự động các Live URL endpoint sau khi apply."
            },
            {
                "name": "Bản in ảnh chụp kết quả chạy Terraform Init, Plan và CI Validation",
                "type": "Ảnh chụp màn hình",
                "local_file": "terraform-plan.png",
                "source_md": "N/A",
                "source_pdf": "N/A",
                "desc": "Ảnh chụp thực tế quá trình chạy terraform plan, terraform apply và kiểm tra tự động trong CI pipeline."
            }
        ],
        "key_evidence": [
            "Mô hình DevOps CALMS (Culture, Automation, Lean, Measurement, Sharing).",
            "Quản lý hạ tầng bằng mã (Infrastructure as Code - IaC) qua Terraform và Docker Compose.",
            "Quy trình đa môi trường: Local Dev (Docker) → Staging CI/CD → Production/Demo Cloud.",
            "Giám sát & Vận hành: Prometheus thu thập metrics, Grafana trực quan hóa dashboard, kịch bản sao lưu tự động `backup-postgres.sh` và `backup-minio.sh`."
        ],
        "blueprint": {
            "what": "Sự kết hợp giữa triết lý văn hóa, thực hành và công cụ nhằm tăng khả năng phân phối ứng dụng với vận tốc cao và độ tin cậy vượt trội.",
            "how": "Thiết lập pipeline CI/CD → Chuẩn hóa hạ tầng bằng Terraform/Docker → Tích hợp hệ thống giám sát Prometheus/Grafana → Tự động hóa quy trình sao lưu và phục hồi.",
            "why": "Phá bỏ bức tường ngăn cách giữa Development và Operations, đảm bảo hệ thống vận hành liên tục và ổn định.",
            "evidence": "Chỉ vào File `terraform_main.tf`, File `terraform_outputs.tf` và Ảnh chụp Terraform Plan."
        },
        "related_links": [
            "[Thư mục Terraform (terraform/)](../../../terraform)",
            "[Thư mục Monitoring (monitoring/)](../../../monitoring)",
            "[Phiếu ôn tập Câu 15 (final-exam/preparation/5_CICD_DevOps_Testing/README.md)](../../../final-exam/preparation/5_CICD_DevOps_Testing/README.md)"
        ]
    },
    {
        "num": 16,
        "num_str": "16",
        "title": "Quản lý con người và phát triển nhóm",
        "english_title": "Team Management & Human Resource",
        "question_prompt": "Trình bày quá trình hình thành và phát triển nhóm mà nhóm đã trải qua. Liệt kê các vấn đề liên quan đến quản lý con người nhóm đã thực sự vướng phải. Trình bày cách nhóm đã giải quyết các vấn đề này và kết quả thu được (có thể thành công, có thể không thành công). _(Sinh viên nộp kèm bản in ảnh chụp chung các thành viên trong nhóm, bản in tài liệu quy định, quy chế, lịch làm việc của nhóm, bản in một biên bản họp của nhóm, bản in giao diện hệ thống liên lạc với dữ liệu thực tế của nhóm.)_",
        "submissions": [
            {
                "name": "Bản in tài liệu Hợp đồng nhóm (Team Contract)",
                "type": "Tài liệu in A4",
                "local_file": "16-team-contract.pdf",
                "source_md": "../../md/16-team-contract.md",
                "source_pdf": "../../pdf/16-team-contract.pdf",
                "desc": "Quy định quy chế làm việc, lịch sinh hoạt, cam kết trách nhiệm, chính sách escalation và văn hóa ứng xử của 6 thành viên."
            },
            {
                "name": "Bản in Biên bản họp nhóm chính thức (Meeting Minutes - Sprint 1)",
                "type": "Biên bản in A4",
                "local_file": "01_meeting_minutes_sprint1.md",
                "source_md": "01_meeting_minutes_sprint1.md",
                "source_pdf": "N/A",
                "desc": "Biên bản họp Kick-off Sprint 1 (mã HCMUS-LDMS-MM01) thống nhất phân công 17 stories, cơ chế Kanban và biểu quyết đồng thuận 6/6."
            },
            {
                "name": "Bản in ảnh chụp chung các thành viên trong nhóm Sebros",
                "type": "Ảnh chụp thực tế",
                "local_file": "group3-photo.png",
                "source_md": "N/A",
                "source_pdf": "N/A",
                "desc": "Ảnh chụp đầy đủ 6 thành viên nhóm Sebros cùng tham gia sinh hoạt dự án."
            },
            {
                "name": "Bản in giao diện hệ thống liên lạc Discord thực tế của nhóm",
                "type": "Ảnh chụp màn hình liên lạc",
                "local_file": "discord_communication.png",
                "source_md": "N/A",
                "source_pdf": "N/A",
                "desc": "Ảnh chụp không gian trao đổi công việc, thông báo họp và chia sẻ tài liệu trên Discord của nhóm."
            }
        ],
        "key_evidence": [
            "Mô hình phát triển nhóm Tuckman: Forming (Hình thành) → Storming (Sóng gió) → Norming (Ổn định) → Performing (Hiệu quả cao) → Adjourning (Đóng dự án).",
            "Xung đột thực tế: Thành viên trễ deadline do bận đồ án khác → Giải quyết bằng quy tắc báo trước 12h và giới hạn WIP ≤ 3.",
            "Quy tắc Team Contract: Họp tuần định kỳ, Pull Request bắt buộc 1 Tech Lead approve, xử lý vắng mặt công bằng.",
            "Ảnh chụp nhóm 6 người, Biên bản họp Sprint 1 và bằng chứng kênh liên lạc Discord thực tế."
        ],
        "blueprint": {
            "what": "Hoạt động tổ chức, điều phối, tạo động lực và giải quyết xung đột nhằm xây dựng một đội ngũ gắn kết và đạt hiệu suất cao.",
            "how": "Ký kết Team Contract ngay Tuần 1 → Thiết lập kênh Discord và lịch họp cố định → Áp dụng mô hình Tuckman nhận diện sóng gió → Thảo luận giải quyết qua Retrospective.",
            "why": "Con người là yếu tố quyết định 80% sự thành bại của dự án phần mềm.",
            "evidence": "Chỉ vào Bản in Team Contract, Bản in Biên bản họp Sprint 1, Ảnh chụp 6 thành viên và Ảnh chụp kênh Discord thực tế."
        },
        "related_links": [
            "[Tài liệu Hợp đồng nhóm (docs.1/md/16-team-contract.md)](../../md/16-team-contract.md)",
            "[Phiếu ôn tập Câu 16 (final-exam/preparation/6_Team_Monitoring_Risk_Lessons/README.md)](../../../final-exam/preparation/6_Team_Monitoring_Risk_Lessons/README.md)"
        ]
    },
    {
        "num": 17,
        "num_str": "17",
        "title": "Phân công, theo dõi, đánh giá, kiểm soát và báo cáo tiến độ",
        "english_title": "Project Monitoring & Control",
        "question_prompt": "Trình bày các hoạt động phân công, theo dõi, đánh giá, kiểm soát công việc và báo cáo tình trạng dự án của nhóm. Trình bày cách nhóm đã giải quyết các vấn đề này và kết quả thu được. _(Sinh viên nộp kèm bản in giao diện hệ thống phân công, theo dõi công việc với dữ liệu thực tế của nhóm, bản in giao diện hệ thống quản lý thời gian đã dùng cho từng công việc của nhóm, bản in bản cập nhật tài liệu Kế hoạch dự án theo dữ liệu thực tiễn của nhóm, bản in biểu đồ Burndown / Cumulative Flow Diagram của toàn dự án, bản in báo cáo tình trạng toàn bộ dự án ở tuần trước thi giữa kỳ của nhóm.)_",
        "submissions": [
            {
                "name": "Bản in tài liệu Nhật ký dự án (Project Log / Time Tracking)",
                "type": "Tài liệu in A4",
                "local_file": "17-project-log.pdf",
                "source_md": "../../md/17-project-log.md",
                "source_pdf": "../../pdf/17-project-log.pdf",
                "desc": "Ghi nhận công việc thực tế, thời gian hoàn thành (Actual Effort), nhật ký cuộc họp và chỉ số luồng qua 11 tuần."
            },
            {
                "name": "Bản in tài liệu Kế hoạch dự án cập nhật theo thực tiễn (Project Plan Actuals)",
                "type": "Tài liệu in A4",
                "local_file": "11-project-plan.pdf",
                "source_md": "../../md/11-project-plan.md",
                "source_pdf": "../../pdf/11-project-plan.pdf",
                "desc": "Kế hoạch 11 tuần cập nhật tiến độ thực tế các mốc Milestones và phân rã công việc WBS."
            },
            {
                "name": "Bản in Báo cáo tình trạng dự án tuần trước thi giữa kỳ (Midterm Status Report)",
                "type": "Báo cáo in A4",
                "local_file": "01_midterm_status_report.md",
                "source_md": "01_midterm_status_report.md",
                "source_pdf": "N/A",
                "desc": "Báo cáo tình trạng tiến độ toàn bộ dự án tại mốc tuần trước thi giữa học kỳ."
            },
            {
                "name": "Bản in giao diện bảng Kanban theo dõi công việc thực tế",
                "type": "Ảnh chụp màn hình Kanban",
                "local_file": "trello_kanban_board.png",
                "source_md": "N/A",
                "source_pdf": "N/A",
                "desc": "Ảnh chụp bảng Kanban với đầy đủ các cards công việc, phân công người thực hiện và trạng thái di chuyển cột."
            },
            {
                "name": "Bản in biểu đồ Burndown Chart toàn bộ dự án",
                "type": "Biểu đồ tiến độ",
                "local_file": "burndown_chart.png",
                "source_md": "N/A",
                "source_pdf": "N/A",
                "desc": "Biểu đồ Burn-down trực quan thể hiện đường tiến độ lý tưởng (Ideal Line) so với đường tiến độ thực tế (Actual Line)."
            }
        ],
        "key_evidence": [
            "Công cụ theo dõi: GitHub Projects / Trello Kanban Board trực quan với 6 cột luồng công việc.",
            "Time Tracking: Ghi nhận giờ thực tế so với ước lượng ban đầu (190h estimate vs actuals).",
            "Kiểm soát tiến độ: Họp Standup tuần, phân tích biểu đồ Burndown phát hiện sớm độ lệch tiến độ.",
            "Báo cáo tiến độ: Báo cáo giữa kỳ Tuần 5 và Báo cáo nghiệm thu Tuần 11."
        ],
        "blueprint": {
            "what": "Hoạt động giám sát liên tục tiến độ, chi phí, công sức thực tế so với kế hoạch cơ sở nhằm đưa ra các hành động điều chỉnh kịp thời.",
            "how": "Cập nhật bảng Kanban hàng ngày → Ghi nhận giờ vào Project Log → Vẽ biểu đồ Burndown theo tuần → Họp đánh giá độ lệch (Variance Analysis) → Điều chỉnh phân công.",
            "why": "Đảm bảo tính minh bạch (Transparency), phát hiện sớm trễ hạn để kịp thời cứu vãn trước khi quá muộn.",
            "evidence": "Chỉ vào Bản in Project Log, Ảnh chụp Kanban Board và Biểu đồ Burndown Chart."
        },
        "related_links": [
            "[Tài liệu Nhật ký dự án (docs.1/md/17-project-log.md)](../../md/17-project-log.md)",
            "[Phiếu ôn tập Câu 17 (final-exam/preparation/6_Team_Monitoring_Risk_Lessons/README.md)](../../../final-exam/preparation/6_Team_Monitoring_Risk_Lessons/README.md)"
        ]
    },
    {
        "num": 18,
        "num_str": "18",
        "title": "Kế hoạch quản lý rủi ro (Software Risk Management Plan)",
        "english_title": "Software Risk Management Plan",
        "question_prompt": "Trình bày quá trình hình thành và phương pháp đánh giá tài liệu Kế hoạch quản lý rủi ro (Software Risk Management Plan) của nhóm. _(Sinh viên nộp kèm bản in tài liệu Kế hoạch quản lý rủi ro của nhóm.)_",
        "submissions": [
            {
                "name": "Bản in tài liệu Kế hoạch quản lý rủi ro (Software Risk Management Plan)",
                "type": "Tài liệu in A4",
                "local_file": "18-risk-management-plan.pdf",
                "source_md": "../../md/18-risk-management-plan.md",
                "source_pdf": "../../pdf/18-risk-management-plan.pdf",
                "desc": "Quy trình quản lý rủi ro, ma trận đánh giá 5x5, sổ đăng ký 18 rủi ro (RSK-01..18), phân công Risk Owner và kế hoạch ứng phó."
            }
        ],
        "key_evidence": [
            "Sổ đăng ký 18 rủi ro phân loại theo 4 nhóm: Kỹ thuật, Lịch trình & Con người, Nghiệp vụ & Dữ liệu, Vận hành & Môi trường.",
            "Ma trận định lượng rủi ro 5×5 (Xác suất P × Mức độ tác động I = Điểm rủi ro R).",
            "4 Chiến lược ứng phó chính: Né tránh (Avoid), Giảm thiểu (Mitigate), Chuyển giao (Transfer), Chấp nhận (Accept).",
            "Các rủi ro hàng đầu: RSK-01 (Độ chính xác OCR thấp), RSK-02 (Rò rỉ bản quyền EPUB), RSK-05 (Thành viên quá tải)."
        ],
        "blueprint": {
            "what": "Quy trình nhận diện, phân tích, lập kế hoạch ứng phó và theo dõi các biến cố không chắc chắn có thể ảnh hưởng tiêu cực đến dự án.",
            "how": "Họp Brainstorming nhận diện rủi ro → Lập Sổ Risk Register → Định lượng P×I trên ma trận 5×5 → Xây dựng kịch bản ứng phó cho rủi ro Cao/Nghiêm trọng → Rà soát định kỳ hàng tuần.",
            "why": "Chuyển từ thế bị động ứng phó sự cố (Firefighting) sang chủ động phòng ngừa, bảo vệ tiến độ và chất lượng dự án.",
            "evidence": "Chỉ vào Sổ đăng ký 18 rủi ro (Mục 3) và Ma trận rủi ro 5×5 trong bản in Kế hoạch quản lý rủi ro."
        },
        "related_links": [
            "[Tài liệu Kế hoạch quản lý rủi ro (docs.1/md/18-risk-management-plan.md)](../../md/18-risk-management-plan.md)",
            "[Phiếu ôn tập Câu 18 (final-exam/preparation/6_Team_Monitoring_Risk_Lessons/README.md)](../../../final-exam/preparation/6_Team_Monitoring_Risk_Lessons/README.md)"
        ]
    },
    {
        "num": 19,
        "num_str": "19",
        "title": "Kế hoạch quản lý chất lượng (Software Quality Management Plan)",
        "english_title": "Software Quality Management Plan",
        "question_prompt": "Trình bày quá trình hình thành và phương pháp đánh giá tài liệu Kế hoạch quản lý chất lượng (Software Quality Management Plan) của nhóm. _(Sinh viên nộp kèm bản in tài liệu Kế hoạch quản lý chất lượng của nhóm, bản in Định nghĩa hoàn thành của nhóm, bản in giao diện cấu hình đảm bảo Coding Standards cho mã nguồn của nhóm, bản in biên bản thanh tra mã nguồn của nhóm, bản in biên bản phản hồi từ khách hàng của nhóm.)_",
        "submissions": [
            {
                "name": "Bản in tài liệu Kế hoạch quản lý chất lượng (Quality Management Plan)",
                "type": "Tài liệu in A4",
                "local_file": "19-quality-management-plan.pdf",
                "source_md": "../../md/19-quality-management-plan.md",
                "source_pdf": "../../pdf/19-quality-management-plan.pdf",
                "desc": "Mô hình chất lượng, 6 cổng kiểm soát chất lượng (Quality Gates), tiêu chuẩn đánh giá và quy trình kiểm soát."
            },
            {
                "name": "Bản in Biên bản thanh tra mã nguồn của nhóm (Code Inspection Record PR #41)",
                "type": "Biên bản in A4",
                "local_file": "01_code_inspection_record_pr41.md",
                "source_md": "01_code_inspection_record_pr41.md",
                "source_pdf": "N/A",
                "desc": "Biên bản thanh tra chính thức cho Pull Request #41 (Tối ưu hóa pipeline OCR) theo chuẩn IEEE 1028 với danh sách defect đã fix."
            },
            {
                "name": "Bản in Biên bản phản hồi từ khách hàng / UAT (UAT Feedback Record)",
                "type": "Biên bản in A4",
                "local_file": "02_uat_feedback_record.md",
                "source_md": "02_uat_feedback_record.md",
                "source_pdf": "N/A",
                "desc": "Biên bản kiểm thử chấp nhận người dùng thực tế ngày 15/08/2026 với đại diện Thư viện nghiệm thu 6 kịch bản UAT."
            },
            {
                "name": "Bản in cấu hình tiêu chuẩn Coding Standards & Linter (ruff, eslint, markdownlint)",
                "type": "Tài liệu cấu hình linter",
                "local_file": "03_coding_standards_and_linter_config.md",
                "source_md": "03_coding_standards_and_linter_config.md",
                "source_pdf": "N/A",
                "desc": "Cấu hình linter chuẩn: Ruff cho Python, ESLint/Prettier cho Next.js, Markdownlint cho tài liệu."
            }
        ],
        "key_evidence": [
            "6 Quality Gates (G1 Commit → G2 Code Review → G3 CI Automation → G4 Staging Deploy → G5 UAT Acceptance → G6 Release).",
            "Coding Standards tự động hóa 100% trong CI: Không cho phép merge PR nếu vi phạm linting hoặc test failed.",
            "Bằng chứng thanh tra mã nguồn PR #41: Ghi nhận 3 defect (1 Major, 2 Minor) và bằng chứng fix.",
            "Bằng chứng UAT thực tế: Biên bản UAT có chữ ký đại diện Thư viện nghiệm thu 6/6 kịch bản."
        ],
        "blueprint": {
            "what": "Quy trình đảm bảo chất lượng (QA) nhằm ngăn ngừa lỗi và kiểm soát chất lượng (QC) nhằm phát hiện và loại bỏ lỗi trước khi bàn giao.",
            "how": "Thiết lập tiêu chuẩn Coding Standards & DoD → Cài đặt linter tự động trong CI → Tiến hành Code Inspection cho PR quan trọng → Thực hiện kiểm thử chấp nhận UAT với khách hàng.",
            "why": "Xây dựng chất lượng ngay từ trong quá trình phát triển (Quality at the Source) thay vì phụ thuộc vào việc tìm lỗi cuối kỳ.",
            "evidence": "Chỉ vào Bản in DoD, File cấu hình linter `03_coding_standards`, Biên bản Code Inspection PR #41 và Biên bản UAT."
        },
        "related_links": [
            "[Tài liệu Kế hoạch chất lượng (docs.1/md/19-quality-management-plan.md)](../../md/19-quality-management-plan.md)",
            "[Phiếu ôn tập Câu 19 (final-exam/preparation/6_Team_Monitoring_Risk_Lessons/README.md)](../../../final-exam/preparation/6_Team_Monitoring_Risk_Lessons/README.md)"
        ]
    },
    {
        "num": 20,
        "num_str": "20",
        "title": "Kế hoạch kiểm thử (Test Plan)",
        "english_title": "Software Test Plan",
        "question_prompt": "Trình bày quá trình hình thành và phương pháp đánh giá tài liệu Kế hoạch kiểm thử (Test Plan) của nhóm. _(Sinh viên nộp kèm bản in tài liệu Kế hoạch kiểm thử của nhóm, bản in giao diện cấu hình đảm bảo Coding Standards cho mã nguồn của nhóm, bản in giao diện hệ thống quản lý lỗi với dữ liệu thực tế của nhóm, bản in giao diện kết quả chạy mã nguồn kiểm thử đơn vị (Unit Tests) của nhóm, bản in biên bản thanh tra mã nguồn của nhóm, bản in báo cáo kết quả kiểm thử của nhóm, bản in biên bản phản hồi của khách hàng của nhóm.)_",
        "submissions": [
            {
                "name": "Bản in tài liệu Kế hoạch kiểm thử (Test Plan)",
                "type": "Tài liệu in A4",
                "local_file": "20-test-plan.pdf",
                "source_md": "../../md/20-test-plan.md",
                "source_pdf": "../../pdf/20-test-plan.pdf",
                "desc": "Chiến lược kiểm thử đa tầng (Unit, Integration, Security, Performance, UAT), ma trận truy vết RTM và báo cáo kết quả kiểm thử."
            },
            {
                "name": "Bản in giao diện kết quả chạy mã nguồn Unit Tests (run-test.png)",
                "type": "Ảnh chụp màn hình console",
                "local_file": "run-test.png",
                "source_md": "N/A",
                "source_pdf": "N/A",
                "desc": "Ảnh chụp console chạy Pytest backend với 100% tests pass và báo cáo code coverage."
            },
            {
                "name": "Bản in Biên bản thanh tra mã nguồn của nhóm (Code Inspection PR #41)",
                "type": "Biên bản in A4",
                "local_file": "01_code_inspection_record_pr41.md",
                "source_md": "01_code_inspection_record_pr41.md",
                "source_pdf": "N/A",
                "desc": "Biên bản thanh tra PR #41."
            },
            {
                "name": "Bản in Biên bản phản hồi của khách hàng (UAT Feedback Record)",
                "type": "Biên bản in A4",
                "local_file": "02_uat_feedback_record.md",
                "source_md": "02_uat_feedback_record.md",
                "source_pdf": "N/A",
                "desc": "Biên bản UAT nghiệm thu người dùng."
            }
        ],
        "key_evidence": [
            "Chiến lược kiểm thử Test Pyramid: Unit Test (Pytest/Vitest) chiếm 70% → Integration Test 20% → E2E/UAT 10%.",
            "Ma trận truy vết (RTM): 100% của 15 Must stories đều có ít nhất 2 Test Cases tương ứng.",
            "Bằng chứng chạy test: Pytest backend pass 100%, code coverage đạt > 80%.",
            "Hệ thống quản lý lỗi: Quy trình Issue Lifecycle trên GitHub (Triage → In Progress → In Review → Verified & Closed)."
        ],
        "blueprint": {
            "what": "Tài liệu chi tiết hóa phạm vi, phương pháp, nguồn lực và lịch trình của các hoạt động kiểm thử nhằm xác minh phần mềm đáp ứng đúng yêu cầu.",
            "how": "Phân tích yêu cầu từ SRS/Backlog → Thiết kế Test Cases & RTM → Viết mã nguồn Unit/Integration test tự động → Chạy test trong CI → Ghi nhận và theo dõi lỗi qua GitHub Issues → Thực hiện UAT.",
            "why": "Đảm bảo chất lượng phần mềm không có lỗi nghiêm trọng trước khi bàn giao cho người dùng cuối.",
            "evidence": "Chỉ vào Bản in Test Plan, Ảnh chụp màn hình Pytest Report `run-test.png` và Biên bản UAT."
        },
        "related_links": [
            "[Tài liệu Kế hoạch kiểm thử (docs.1/md/20-test-plan.md)](../../md/20-test-plan.md)",
            "[Phiếu ôn tập Câu 20 (final-exam/preparation/5_CICD_DevOps_Testing/README.md)](../../../final-exam/preparation/5_CICD_DevOps_Testing/README.md)"
        ]
    },
    {
        "num": 21,
        "num_str": "21",
        "title": "Báo cáo bài học kinh nghiệm (Lessons Learned Register)",
        "english_title": "Lessons Learned Register",
        "question_prompt": "Trình bày quá trình hình thành và phương pháp đánh giá tài liệu Báo cáo bài học kinh nghiệm (Lessons Learned Register) của nhóm. _(Sinh viên nộp kèm bản in tài liệu Báo cáo bài học kinh nghiệm của nhóm.)_",
        "submissions": [
            {
                "name": "Bản in tài liệu Báo cáo bài học kinh nghiệm (Lessons Learned Register)",
                "type": "Tài liệu in A4",
                "local_file": "21-lessons-learned.pdf",
                "source_md": "../../md/21-lessons-learned.md",
                "source_pdf": "../../pdf/21-lessons-learned.pdf",
                "desc": "Tài liệu tổng kết 7 bài học kinh nghiệm thực tiễn có căn cứ rút ra qua 11 tuần triển khai dự án kèm theo khuyến nghị cho các dự án tương lai."
            }
        ],
        "key_evidence": [
            "7 Bài học cốt lõi: (1) Quản lý phạm vi và ngăn ngừa Scope Creep, (2) Lựa chọn và kiểm chứng công nghệ qua PoC sớm, (3) Tự động hóa CI/CD ngay từ Tuần 1, (4) Kiểm soát luồng công việc bằng WIP limits, (5) Giao tiếp liên tục và demo sớm với khách hàng, (6) Quản lý tập trung Secrets và cấu hình bảo mật, (7) Văn hóa Retrospective cởi mở và cải tiến liên tục.",
            "Cấu trúc bài học chuẩn: Bối cảnh (Situation) → Vấn đề phát sinh (Problem) → Giải pháp áp dụng (Action) → Bài học rút ra (Lesson) → Khuyến nghị (Recommendation).",
            "Giá trị thực tiễn: Đóng góp vào kho tài sản quy trình tổ chức (Organizational Process Assets) cho các khóa sinh viên sau."
        ],
        "blueprint": {
            "what": "Tập hợp các tri thức, kinh nghiệm (cả thành công và thất bại) được nhóm đúc kết trong suốt vòng đời dự án.",
            "how": "Ghi nhận bài học liên tục trong Project Log → Tổ chức họp Sprint Retrospective định kỳ → Tổng hợp và phân loại bài học theo chủ đề → Đánh giá và lưu trữ vào Sổ bài học kinh nghiệm.",
            "why": "Giúp nhóm không lặp lại các sai lầm trong quá khứ và chuyển giao tri thức hữu ích cho các dự án phần mềm tiếp theo.",
            "evidence": "Chỉ vào 7 Bài học kinh nghiệm cụ thể trong bản in Lessons Learned Register."
        },
        "related_links": [
            "[Tài liệu Bài học kinh nghiệm (docs.1/md/21-lessons-learned.md)](../../md/21-lessons-learned.md)",
            "[Phiếu ôn tập Câu 21 (final-exam/preparation/6_Team_Monitoring_Risk_Lessons/README.md)](../../../final-exam/preparation/6_Team_Monitoring_Risk_Lessons/README.md)"
        ]
    }
]

def generate_evidence_files():
    os.makedirs(EVIDENCE_DIR, exist_ok=True)
    
    # 1. Generate individual question READMEs
    for q in QUESTIONS_DATA:
        md_lines = []
        md_lines.append(f"# BẰNG CHỨNG NỘP KÈM — CÂU {q['num']}: {q['title'].upper()}\n")
        md_lines.append(f"**Mã câu hỏi:** `CÂU-{q['num_str']}` | **Chủ đề:** {q['english_title']}\n")
        md_lines.append("## 1. Đề bài và Yêu cầu nộp kèm từ Đề thi vấn đáp\n")
        md_lines.append(f"> {q['question_prompt']}\n")
        
        md_lines.append("## 2. Danh mục tài liệu / bằng chứng cần nộp kèm khi thi\n")
        md_lines.append("| STT | Tên tài liệu / Bằng chứng nộp kèm | Loại tài liệu | Tệp đính kèm tại thư mục này | Nguồn tài liệu PDF | Mô tả chi tiết |")
        md_lines.append("|:---:|---|---|---|---|---|")
        
        for idx, sub in enumerate(q["submissions"], 1):
            local_link = f"[{sub['local_file']}](./{sub['local_file']})" if sub.get("local_file") else "N/A"
            pdf_link = f"[{os.path.basename(sub['source_pdf'])}]({sub['source_pdf']})" if sub.get("source_pdf") and sub["source_pdf"] != "N/A" else "N/A"
            md_lines.append(f"| {idx} | **{sub['name']}** | `{sub['type']}` | {local_link} | {pdf_link} | {sub['desc']} |")
        
        md_lines.append("\n## 3. Các bằng chứng & số liệu then chốt cần chỉ ra trên tài liệu\n")
        for item in q["key_evidence"]:
            parts = item.split(":")
            if len(parts) > 1:
                md_lines.append(f"- **{parts[0].strip()}:** {':'.join(parts[1:]).strip()}")
            else:
                md_lines.append(f"- {item}")
            
        md_lines.append("\n## 4. Khung hướng dẫn trả lời vấn đáp (WHAT — HOW — WHY — EVIDENCE)\n")
        bp = q["blueprint"]
        md_lines.append(f"- **WHAT (Khái niệm & Nội dung):** {bp['what']}")
        md_lines.append(f"- **HOW (Quy trình thực hiện):** {bp['how']}")
        md_lines.append(f"- **WHY (Lý do & Giá trị):** {bp['why']}")
        md_lines.append(f"- **EVIDENCE (Minh chứng chỉ tay):** {bp['evidence']}")
        
        md_lines.append("\n## 5. Liên kết tệp nguồn và tài liệu liên quan\n")
        for link in q["related_links"]:
            md_lines.append(f"- {link}")
        md_lines.append("")
        
        content = "\n".join(md_lines)
        
        folder_path = os.path.join(EVIDENCE_DIR, q["num_str"])
        os.makedirs(folder_path, exist_ok=True)
        readme_path = os.path.join(folder_path, "README.md")
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Generated: {readme_path}")

    # 2. Generate Master README in docs.1/evidence/README.md
    master_lines = []
    master_lines.append("# TỔNG HỢP DANH MỤC BẰNG CHỨNG NỘP KÈM VẤN ĐÁP (21 CÂU HỎI)\n")
    master_lines.append("Thư mục này chứa danh mục và hướng dẫn chuẩn bị chi tiết các **tài liệu, bản in, ảnh chụp giao diện và biên bản nộp kèm** cho từng câu hỏi trong đề thi vấn đáp môn Quản lý Dự án Phần mềm (`Final Exam Questions - Software Project Management.md`).\n")
    master_lines.append("## Danh mục 21 thư mục bằng chứng\n")
    master_lines.append("| Câu | Tên câu hỏi | Thư mục bằng chứng | Tài liệu / Bằng chứng nộp kèm chính | Tệp PDF chính nguồn |")
    master_lines.append("|:---:|---|:---:|---|---|")
    
    for q in QUESTIONS_DATA:
        folder_link = f"[{q['num_str']}](./{q['num_str']}/README.md)"
        sub_names = ", ".join([f"**{s['name']}**" for s in q["submissions"]])
        pdf_links = ", ".join([f"[{os.path.basename(s['source_pdf'])}](../pdf/{os.path.basename(s['source_pdf'])})" for s in q["submissions"] if "pdf" in s.get("source_pdf", "") and s["source_pdf"] != "N/A"])
        if not pdf_links:
            pdf_links = "N/A"
        master_lines.append(f"| **{q['num']}** | {q['title']} | {folder_link} | {sub_names} | {pdf_links} |")
        
    master_lines.append("\n## Quy tắc chuẩn bị bản in khi đi thi\n")
    master_lines.append("1. **Trình bày:** Tất cả câu trả lời trình bày trên giấy A4 bằng giấy bút, không sử dụng thiết bị điện tử trong phòng thi.")
    master_lines.append("2. **Bản in nộp kèm:** Mang đầy đủ các bản in A4 của tài liệu / ảnh chụp giao diện theo đúng danh mục từng câu để hỗ trợ giải thích và chỉ bằng chứng trực quan cho giám khảo.")
    master_lines.append("3. **Khung trả lời:** Trả lời dứt khoát theo khung **WHAT — HOW — WHY — EVIDENCE**.")
    master_lines.append("")
    
    master_readme_path = os.path.join(EVIDENCE_DIR, "README.md")
    with open(master_readme_path, "w", encoding="utf-8") as f:
        f.write("\n".join(master_lines))
    print(f"Generated Master README: {master_readme_path}")

if __name__ == "__main__":
    generate_evidence_files()
