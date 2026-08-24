import os
import shutil

BASE_DIR = r"g:\HCMUS\NAM3-HK3\Management\Final\hcmus-projectmanage--lab"
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
                "source_md": "docs.1/md/01-project-proposal.md",
                "source_pdf": "docs.1/pdf/01-project-proposal.pdf",
                "desc": "Tài liệu đề xuất dự án hoàn chỉnh mô tả vấn đề tại Thư viện HCMUS, stakeholder, giải pháp 4 use case cốt lõi, so sánh 3 đối thủ và quyết định Go/No-go."
            }
        ],
        "key_evidence": [
            "Bối cảnh & Pain Points: 50.000 đầu sách, 800 luận văn chưa được số hóa, quy trình mượn trả giấy tốn thời gian.",
            "3 Sản phẩm cạnh tranh: DSpace, Koha, Calibre-Web (so sánh chi phí, độ phức tạp, khả năng OCR tiếng Việt).",
            "4 Use cases cốt lõi: Tiếp nhận tài liệu, Nhận dạng OCR tiếng Việt, Hiệu chỉnh 2 màn hình, Đọc EPUB trực tuyến.",
            "Quyết định Go/No-go: Chấp thuận triển khai phiên bản thử nghiệm môn học 11 tuần."
        ],
        "blueprint": {
            "what": "Tài liệu khởi tạo nhằm chứng minh vấn đề của Thư viện HCMUS là đáng giải quyết và đề xuất giải pháp khả thi.",
            "how": "Khảo sát hiện trạng thư viện → Phân tích đối thủ cạnh tranh → Xác định phạm vi và 4 use case cốt lõi → Soạn thảo Proposal → Đánh giá nội bộ và thông qua quyết định Go/No-go.",
            "why": "Tránh lãng phí nguồn lực vào các giải pháp không khả thi hoặc không đúng nhu cầu của thư viện.",
            "evidence": "Chỉ vào Bảng so sánh đối thủ cạnh tranh (Mục 3) và Bảng phạm vi đề xuất (Mục 4) trong bản in Proposal."
        },
        "related_links": [
            "[docs.1/md/01-project-proposal.md](../../md/01-project-proposal.md)",
            "[docs.1/pdf/01-project-proposal.pdf](../../pdf/01-project-proposal.pdf)",
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
                "source_md": "docs.1/md/02-vision-and-scope.md",
                "source_pdf": "docs.1/pdf/02-vision-and-scope.pdf",
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
            "[docs.1/md/02-vision-and-scope.md](../../md/02-vision-and-scope.md)",
            "[docs.1/pdf/02-vision-and-scope.pdf](../../pdf/02-vision-and-scope.pdf)",
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
                "source_md": "docs.1/md/03-project-charter.md",
                "source_pdf": "docs.1/pdf/03-project-charter.pdf",
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
            "[docs.1/md/03-project-charter.md](../../md/03-project-charter.md)",
            "[docs.1/pdf/03-project-charter.pdf](../../pdf/03-project-charter.pdf)",
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
                "name": "Bản in tài liệu Yêu cầu phần mềm (SRS) hoặc Product Backlog",
                "type": "Tài liệu in A4",
                "source_md": "docs.1/md/04-software-requirements.md (hoặc 04-product-backlog.md)",
                "source_pdf": "docs.1/pdf/04-software-requirements.pdf (hoặc 04-product-backlog.pdf)",
                "desc": "Đặc tả 26 User Stories, tiêu chí chấp nhận (Acceptance Criteria), DoR, DoD, bảng phân rã FR/NFR và ma trận truy vết."
            },
            {
                "name": "Bản in tài liệu Hướng dẫn sử dụng hệ thống (User Guide - HCMUS-LDMS-UG)",
                "type": "Tài liệu in A4",
                "source_md": "docs.1/md/04-user-guide.md",
                "source_pdf": "docs.1/pdf/04-user-guide.pdf",
                "desc": "Hướng dẫn chi tiết quy trình sử dụng giao diện theo 4 vai trò: Quản trị viên, Thủ thư, Biên tập viên và Độc giả."
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
            "[docs.1/md/04-product-backlog.md](../../md/04-product-backlog.md)",
            "[docs.1/md/04-software-requirements.md](../../md/04-software-requirements.md)",
            "[docs.1/md/04-user-guide.md](../../md/04-user-guide.md)",
            "[docs.1/pdf/04-product-backlog.pdf](../../pdf/04-product-backlog.pdf)",
            "[docs.1/pdf/04-user-guide.pdf](../../pdf/04-user-guide.pdf)",
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
                "source_md": "docs.1/md/05-software-architecture.md",
                "source_pdf": "docs.1/pdf/05-software-architecture.pdf",
                "desc": "Tài liệu kiến trúc C4 Model, Tech Stack, sơ đồ tuần tự Upload/OCR, mô hình bảo mật JWT/RBAC/Presigned URL và 10 quyết định kiến trúc ADR."
            }
        ],
        "key_evidence": [
            "Mô hình C4: Context Diagram (Hệ thống trong môi trường ĐH KHTN), Container Diagram (Frontend Next.js, API FastAPI, PostgreSQL, MinIO, Redis).",
            "Tech Stack: Backend Python FastAPI, Frontend React/Next.js, Worker Celery/Redis, OCR Tesseract, Storage MinIO (S3-compatible).",
            "Bảo mật: Xác thực JWT token, phân quyền RBAC ở máy chủ, bảo vệ tệp EPUB bằng Presigned URLs có hạn ngạch ngắn.",
            "10 Quyết định kiến trúc ADR (ADR-01 đến ADR-10) giải thích lý do lựa chọn công nghệ."
        ],
        "blueprint": {
            "what": "Bản thiết kế cấu trúc hệ thống, phân rã thành phần, giao tiếp giữa các module và cơ chế bảo mật.",
            "how": "Phân tích NFR từ SRS → Lựa chọn Tech Stack phù hợp → Vẽ mô hình C4 → Thiết kế sơ đồ tuần tự và bảo mật → Ghi nhận ADR.",
            "why": "Đảm bảo tính mở rộng, hiệu năng, bảo mật và tính khả thi trong việc tích hợp nhiều thành phần phức tạp (OCR, EPUB, CSDL).",
            "evidence": "Chỉ vào Sơ đồ C4 Container (Mục 3) và Sơ đồ tuần tự Upload-OCR trong bản in Kiến trúc phần mềm."
        },
        "related_links": [
            "[docs.1/md/05-software-architecture.md](../../md/05-software-architecture.md)",
            "[docs.1/md/A1-decision-log-and-adr.md](../../md/A1-decision-log-and-adr.md)",
            "[docs.1/pdf/05-software-architecture.pdf](../../pdf/05-software-architecture.pdf)",
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
                "name": "Bản in giao diện thể hiện đầu vào và đầu ra khi chạy mã nguồn PoC 1 (OCR tiếng Việt)",
                "type": "Bản in giao diện / Ảnh chụp",
                "source_md": "final-exam/preparation/3_Architecture_PoC_Prototype/README.md",
                "source_pdf": "final-exam/preparation/3_Architecture_PoC_Prototype/README.pdf",
                "desc": "Ảnh chụp Input (Ảnh scan/PDF giáo trình mẫu) và Output (Văn bản tiếng Việt có dấu trích xuất kèm điểm số confidence)."
            },
            {
                "name": "Bản in giao diện thể hiện đầu vào và đầu ra khi chạy mã nguồn PoC 2 (Trình đọc EPUB Reader)",
                "type": "Bản in giao diện / Ảnh chụp",
                "source_md": "final-exam/preparation/3_Architecture_PoC_Prototype/README.md",
                "source_pdf": "final-exam/preparation/3_Architecture_PoC_Prototype/README.pdf",
                "desc": "Ảnh chụp Input (Tệp EPUB số hóa) và Output (Trình đọc ePub.js render nội dung mượt mà, phân trang, không lộ direct download link)."
            }
        ],
        "key_evidence": [
            "PoC 1 (OCR Engine): Đánh giá Tesseract 5 với bộ ngôn ngữ vie.traineddata, xử lý tiền xử lý ảnh (Deskew, Binarization) đạt độ chính xác > 85%.",
            "PoC 2 (EPUB Reader Web): Đánh giá thư viện ePub.js, stream dữ liệu từ MinIO qua Presigned URL, ngăn chặn hành vi tải tệp gốc.",
            "Tiêu chí nghiệm thu PoC: Thời gian xử lý < 30s/trang, tiêu tốn RAM < 512MB."
        ],
        "blueprint": {
            "what": "Thực nghiệm kỹ thuật quy mô nhỏ nhằm kiểm chứng các rủi ro công nghệ lớn nhất trước khi xây dựng toàn hệ thống.",
            "how": "Nhận diện 2 rủi ro kỹ thuật cao nhất (OCR & EPUB Reader) → Xây dựng mã nguồn PoC độc lập → Chạy thử nghiệm với dữ liệu mẫu → Đo lường kết quả → Đánh giá Go/No-go.",
            "why": "Giảm thiểu rủi ro kiến trúc thất bại ở giai đoạn muộn của dự án.",
            "evidence": "Chỉ vào Ảnh chụp Input/Output của PoC OCR và PoC EPUB Reader."
        },
        "related_links": [
            "[Phiếu ôn tập Câu 6 (final-exam/preparation/3_Architecture_PoC_Prototype/README.md)](../../../final-exam/preparation/3_Architecture_PoC_Prototype/README.md)",
            "[docs.1/md/05-software-architecture.md](../../md/05-software-architecture.md)"
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
                "name": "Bản in phác thảo giao diện ban đầu cho hệ thống (Prototype / Wireframes)",
                "type": "Bản in phác thảo / Sơ đồ giao diện",
                "source_md": "docs.1/md/assets/prototype-core-flow.svg",
                "source_pdf": "final-exam/preparation/3_Architecture_PoC_Prototype/README.pdf",
                "desc": "Bản in sơ đồ luồng giao diện tổng thể và các màn hình cốt lõi: Login, Dashboard Thủ thư, Màn hình Biên tập OCR 2 cột, Giao diện Độc giả."
            }
        ],
        "key_evidence": [
            "Màn hình Đăng nhập & Điều hướng theo vai trò (Role-based Navigation).",
            "Màn hình Biên tập viên: Thiết kế song song 2 cột (Side-by-side) — Cột trái xem ảnh scan gốc phóng to/thu nhỏ, Cột phải trình soạn thảo văn bản nhận dạng.",
            "Màn hình Độc giả: Thanh tìm kiếm toàn văn trực quan, bộ lọc danh mục và giao diện đọc sách EPUB tối ưu trên Desktop/Mobile.",
            "Phản hồi từ người dùng: Cải tiến thao tác phím tắt chuyển trang nhanh (Next/Prev Page) trong màn hình hiệu chỉnh."
        ],
        "blueprint": {
            "what": "Bản mô phỏng trực quan trải nghiệm người dùng (UI/UX) giúp các bên liên quan hình dung sản phẩm thực tế.",
            "how": "Phác thảo Wireframe giấy → Thiết kế Prototype số hóa (Figma/SVG) → Trình bày cho đại diện Thư viện lấy ý kiến → Tinh chỉnh luồng giao diện → Đưa vào Backlog.",
            "why": "Phát hiện sớm các vấn đề về khả năng sử dụng (Usability) trước khi tốn công lập trình Frontend.",
            "evidence": "Chỉ vào Bản in phác thảo giao diện Màn hình Biên tập 2 cột và Giao diện Độc giả."
        },
        "related_links": [
            "[Sơ đồ Prototype Core Flow (docs.1/md/assets/prototype-core-flow.svg)](../../md/assets/prototype-core-flow.svg)",
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
                "source_md": "docs.1/md/08-feasibility-study.md",
                "source_pdf": "docs.1/pdf/08-feasibility-study.pdf",
                "desc": "Đánh giá khả thi theo 5 khía cạnh TELOS (Technical, Economic, Legal, Operational, Schedule) và kết luận khả thi có điều kiện."
            }
        ],
        "key_evidence": [
            "Technical Feasibility: Khả thi nhờ kết hợp FastAPI + Next.js + Tesseract OCR mã nguồn mở, đã kiểm chứng qua PoC.",
            "Economic Feasibility: Chi phí phần mềm 0đ, tận dụng hạ tầng có sẵn của nhà trường và Cloud Free Tier.",
            "Legal Feasibility: Tuân thủ Luật Sở hữu Trí tuệ Việt Nam — chỉ số hóa tài liệu thuộc phạm vi phục vụ nội bộ thư viện ĐH KHTN.",
            "Operational Feasibility: Thủ thư và sinh viên dễ dàng sử dụng thông qua giao diện Web không cần cài đặt phần mềm phức tạp.",
            "Schedule Feasibility: 11 tuần đủ để hoàn thành 15 Must + 6 Should stories theo luồng Kanban."
        ],
        "blueprint": {
            "what": "Báo cáo đánh giá toàn diện khả năng thực thi của dự án dưới các ràng buộc thực tế.",
            "how": "Áp dụng khung TELOS 5 chiều → Thu thập dữ liệu kỹ thuật, chi phí, pháp lý và vận hành → Đánh giá rủi ro → Đưa ra kết luận Khả thi có điều kiện.",
            "why": "Cung cấp cơ sở khoa học để Nhà tài trợ / Giảng viên quyết định phê duyệt dự án.",
            "evidence": "Chỉ vào Bảng phân tích TELOS 5 khía cạnh trong bản in Báo cáo tính khả thi."
        },
        "related_links": [
            "[docs.1/md/08-feasibility-study.md](../../md/08-feasibility-study.md)",
            "[docs.1/pdf/08-feasibility-study.pdf](../../pdf/08-feasibility-study.pdf)",
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
                "source_md": "docs.1/md/09-software-process-definition.md",
                "source_pdf": "docs.1/pdf/09-software-process-definition.pdf",
                "desc": "Tài liệu định nghĩa mô hình Agile/Kanban luồng liên tục 6 cột, chính sách WIP Limits, Trunk-Based Development, DoR/DoD và chỉ số luồng."
            }
        ],
        "key_evidence": [
            "Mô hình Kanban 6 cột: Ý tưởng → Đã sẵn sàng → Đang thực hiện → Đang xem xét (Code Review) → Chờ xác nhận (Acceptance) → Hoàn thành.",
            "Chính sách WIP Limits: Ready (5), In Progress (6), In Review (4), Acceptance (3).",
            "Quy tắc phát triển: Trunk-Based Development, nhánh ngắn hạn (Short-lived feature branches), mỗi PR bắt buộc có ít nhất 1 review đạt và CI pass.",
            "Chỉ số luồng: Đo lường Lead Time, Cycle Time, Throughput và Cumulative Flow Diagram (CFD)."
        ],
        "blueprint": {
            "what": "Quy chuẩn hóa cách thức nhóm tổ chức, phối hợp và đưa công việc từ ý tưởng đến sản phẩm hoàn chỉnh.",
            "how": "Phân tích đặc thù nhóm 6 SV kiêm nhiệm → Lựa chọn mô hình Kanban luồng liên tục → Thiết lập WIP limits và chính sách chuyển cột → Ban hành quy chế Trunk-Based.",
            "why": "Tối ưu hóa luồng giá trị (Value Stream), giảm thời gian chờ đợi (Bottleneck) và duy trì chất lượng mã nguồn ổn định.",
            "evidence": "Chỉ vào Sơ đồ luồng Kanban 6 cột và Bảng chính sách WIP limits trong bản in Quy trình."
        },
        "related_links": [
            "[docs.1/md/09-software-process-definition.md](../../md/09-software-process-definition.md)",
            "[docs.1/pdf/09-software-process-definition.pdf](../../pdf/09-software-process-definition.pdf)",
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
                "source_md": "docs.1/md/10-project-estimate.md",
                "source_pdf": "docs.1/pdf/10-project-estimate.pdf",
                "desc": "Tài liệu phân tích Bottom-up kết hợp T-Shirt sizing: Phân rã 26 stories, tổng nhu cầu Demand = 190h, tổng năng lực Capacity = 198h, đệm dự phòng 8h (4.2%)."
            }
        ],
        "key_evidence": [
            "Phương pháp ước lượng: Bottom-up Estimation kết hợp Planning Poker / T-Shirt Sizing (Nhỏ: 4-8h, Vừa: 8-16h, Lớn: 16-32h).",
            "Nhu cầu công việc (Demand): 15 Must (132h) + 6 Should (42h) + 5 Could (16h) = 190 giờ-người.",
            "Năng lực nhóm (Capacity): 6 thành viên × 3 giờ/tuần × 11 tuần = 198 giờ-người.",
            "Dự phòng rủi ro (Buffer): 198h - 190h = 8 giờ-người (4.2%), đảm bảo hoàn thành 100% phạm vi bắt buộc."
        ],
        "blueprint": {
            "what": "Dự báo định lượng về khối lượng công việc, thời gian và năng lực cần thiết để hoàn thành dự án.",
            "how": "Phân rã User Stories thành tasks kỹ thuật → Nhóm họp Planning Poker chấm điểm cỡ → Tính tổng Demand → So sánh với Capacity → Phân tích độ nhạy và dự phòng.",
            "why": "Tránh tình trạng cam kết vượt quá năng lực (Over-commitment) dẫn đến trễ hạn hoặc suy giảm chất lượng.",
            "evidence": "Chỉ vào Bảng so sánh Demand vs Capacity và Bảng chi tiết ước lượng 26 User Stories trong bản in Estimate."
        },
        "related_links": [
            "[docs.1/md/10-project-estimate.md](../../md/10-project-estimate.md)",
            "[docs.1/pdf/10-project-estimate.pdf](../../pdf/10-project-estimate.pdf)",
            "[Phiếu ôn tập Câu 10 (final-exam/preparation/4_Estimation_Planning_Process/README.md)](../../../final-exam/preparation/4_Estimation_Planning_Process/README.md)"
        ]
    },
    {
        "num": 11,
        "num_str": "11",
        "title": "Kế hoạch dự án (Project Plan)",
        "english_title": "Project Plan & WBS",
        "question_prompt": "Trình bày quá trình hình thành và phương pháp đánh giá tài liệu Kế hoạch dự án (Project Plan) của nhóm. _(Sinh viên nộp kèm bản in tài liệu Kế hoạch dự án của nhóm.)_",
        "submissions": [
            {
                "name": "Bản in tài liệu Kế hoạch dự án (Project Plan)",
                "type": "Tài liệu in A4",
                "source_md": "docs.1/md/11-project-plan.md",
                "source_pdf": "docs.1/pdf/11-project-plan.pdf",
                "desc": "Tài liệu kế hoạch tổng thể: Cấu trúc phân rã công việc WBS (5 pha, 18 work packages, 45 tasks), Đường găng Critical Path, Lịch trình Gantt 11 tuần."
            }
        ],
        "key_evidence": [
            "Cấu trúc WBS: 5 pha (1. Khởi tạo & Yêu cầu, 2. Thiết kế & PoC, 3. Phát triển cốt lõi, 4. Tích hợp & Kiểm thử, 5. Nghiệm thu & Bàn giao).",
            "Đường găng (Critical Path): W1 Cài đặt → W2-3 Auth & Upload → W4-6 OCR Pipeline → W7-8 EPUB Generator → W9-10 Search & Reader → W11 Final Acceptance.",
            "Phân bổ nhân lực: 6 sinh viên phụ trách cân đối theo chuyên môn (DevOps, Frontend, Backend, QA/Test).",
            "Kế hoạch quản lý tiến độ: Daily standup qua Discord, Review định kỳ hàng tuần, kiểm soát độ lệch SV/CV."
        ],
        "blueprint": {
            "what": "Bản lộ trình thực thi tích hợp kết nối phạm vi, lịch trình, nhân sự và ngân sách thành kế hoạch hành động.",
            "how": "Xây dựng WBS từ SRS/Backlog → Xác định quan hệ phụ thuộc → Lập tiến độ Gantt & tìm Critical Path → Phân bổ tài nguyên → Phê duyệt Kế hoạch.",
            "why": "Làm đường cơ sở (Schedule Baseline) để theo dõi, đo lường và điều chỉnh tiến độ thực tế trong 11 tuần.",
            "evidence": "Chỉ vào Sơ đồ cây WBS và Biểu đồ tiến độ Gantt với Đường găng màu đỏ trong bản in Project Plan."
        },
        "related_links": [
            "[docs.1/md/11-project-plan.md](../../md/11-project-plan.md)",
            "[docs.1/pdf/11-project-plan.pdf](../../pdf/11-project-plan.pdf)",
            "[Phiếu ôn tập Câu 11 (final-exam/preparation/4_Estimation_Planning_Process/README.md)](../../../final-exam/preparation/4_Estimation_Planning_Process/README.md)"
        ]
    },
    {
        "num": 12,
        "num_str": "12",
        "title": "Phát biểu công việc (Statement of Work)",
        "english_title": "Statement of Work (SOW)",
        "question_prompt": "Trình bày quá trình hình thành và phương pháp đánh giá tài liệu Phát biểu công việc (Statement of Work) của nhóm. _(Sinh viên nộp kèm bản in tài liệu Phát biểu công việc của nhóm.)_",
        "submissions": [
            {
                "name": "Bản in tài liệu Phát biểu công việc (Statement of Work - SOW)",
                "type": "Tài liệu in A4",
                "source_md": "docs.1/md/12-statement-of-work.md",
                "source_pdf": "docs.1/pdf/12-statement-of-work.pdf",
                "desc": "Tài liệu hợp đồng môn học quy định phạm vi công việc, 5 kết quả bàn giao chính (Deliverables DL-01..DL-05), tiêu chuẩn nghiệm thu và quy trình quản lý thay đổi."
            }
        ],
        "key_evidence": [
            "5 Hạng mục bàn giao (Deliverables): DL-01 Mã nguồn hoàn chỉnh, DL-02 Cơ sở dữ liệu mẫu, DL-03 Bộ tài liệu kỹ thuật, DL-04 Báo cáo kiểm thử & QA, DL-05 Hướng dẫn sử dụng.",
            "Tiêu chuẩn nghiệm thu (Acceptance Criteria): Tất cả 15 Must stories đạt DoD, hệ thống triển khai chạy được trên Local/Cloud, 100% Test cases pass.",
            "Quy trình quản lý thay đổi (Change Control): Mọi yêu cầu thay đổi phải được gửi qua Change Request Form, đánh giá tác động và có chữ ký phê duyệt của PM/Stakeholder.",
            "Ranh giới trách nhiệm: Nhóm chịu trách nhiệm bàn giao phần mềm; Thư viện chịu trách nhiệm cung cấp tài liệu mẫu và phối hợp UAT."
        ],
        "blueprint": {
            "what": "Văn bản thỏa thuận pháp lý/nghiệp vụ định nghĩa chi tiết những gì sẽ được bàn giao và điều kiện để được nghiệm thu.",
            "how": "Tổng hợp từ Charter, Vision & Scope và Project Plan → Chi tiết hóa 5 Deliverables → Thiết lập tiêu chí nghiệm thu định lượng → Ký kết thỏa thuận SOW.",
            "why": "Làm căn cứ bảo vệ nhóm khi nghiệm thu dự án, tránh các đòi hỏi phát sinh ngoài cam kết ban đầu.",
            "evidence": "Chỉ vào Bảng 5 Deliverables (Mục 3) và Bảng Tiêu chí nghiệm thu (Mục 5) trong bản in SOW."
        },
        "related_links": [
            "[docs.1/md/12-statement-of-work.md](../../md/12-statement-of-work.md)",
            "[docs.1/pdf/12-statement-of-work.pdf](../../pdf/12-statement-of-work.pdf)",
            "[Phiếu ôn tập Câu 12 (final-exam/preparation/2_Requirements_Scope_SoW/README.md)](../../../final-exam/preparation/2_Requirements_Scope_SoW/README.md)"
        ]
    },
    {
        "num": 13,
        "num_str": "13",
        "title": "Mô hình tích hợp liên tục (Continuous Integration)",
        "english_title": "Continuous Integration (CI)",
        "question_prompt": "Vẽ và giải thích mô hình tích hợp liên tục (Continuous Integration) của nhóm. Ghi chú trên mô hình các công cụ nhóm đã dùng cho từng thành phần. Tại sao cần sử dụng hệ thống tích hợp liên tục cho dự án? _(Sinh viên nộp kèm bản in kịch bản build (build scripts), giao diện email nhận thông báo về kết quả build từ hệ thống build tự động, và bản in tài liệu Hướng dẫn cài đặt công cụ và biên dịch mã nguồn hệ thống cho máy tính của nhà phát triển của nhóm)._",
        "submissions": [
            {
                "name": "Bản in kịch bản build (Build Scripts) — .github/workflows/ci.yml",
                "type": "Kịch bản CI (Code printout)",
                "source_md": ".github/workflows/ci.yml",
                "source_pdf": "final-exam/preparation/5_CICD_DevOps_Testing/README.pdf",
                "desc": "Tệp cấu hình GitHub Actions CI tự động hóa việc kiểm tra mã nguồn, linting, unit testing, terraform validate và gửi email."
            },
            {
                "name": "Bản in giao diện email nhận thông báo kết quả build tự động (Brevo / GitHub)",
                "type": "Ảnh chụp giao diện email",
                "source_md": "final-exam/preparation/5_CICD_DevOps_Testing/printouts/Q13/Mail.png",
                "source_pdf": "final-exam/preparation/5_CICD_DevOps_Testing/README.pdf",
                "desc": "Ảnh chụp email Brevo gửi tự động tới hộp thư nhóm thông báo trạng thái từng job (Backend, Frontend, Terraform) khi push lên main."
            },
            {
                "name": "Bản in tài liệu Hướng dẫn cài đặt và biên dịch mã nguồn (Developer Guide)",
                "type": "Tài liệu in A4",
                "source_md": "docs/03-execution-monitoring/06-developer-guide.md (hoặc docs.1/md/13-continuous-integration.md)",
                "source_pdf": "docs.1/pdf/13-continuous-integration.pdf",
                "desc": "Hướng dẫn chi tiết cài đặt công cụ (Docker, Python, Node.js), clone repo, biên dịch mã nguồn và chạy local test suite."
            },
            {
                "name": "Bản in ảnh chụp GitHub Actions CI chạy thành công (CI-pass.png)",
                "type": "Ảnh chụp màn hình",
                "source_md": "final-exam/preparation/5_CICD_DevOps_Testing/printouts/Q13/CI-pass.png",
                "source_pdf": "final-exam/preparation/5_CICD_DevOps_Testing/README.pdf",
                "desc": "Minh chứng thực tế toàn bộ pipeline CI xanh trên GitHub repository."
            }
        ],
        "key_evidence": [
            "Mô hình CI: Developer Commit → Push PR → GitHub Actions kích hoạt 4 jobs song song: (1) Backend Ruff/Pytest, (2) Frontend ESLint/Next Build, (3) Terraform Validate, (4) Notify Email qua Brevo API.",
            "Kịch bản `.github/workflows/ci.yml` có sẵn trong repo, thiết lập ma trận kiểm tra tự động.",
            "Lợi ích CI: Phát hiện lỗi tích hợp ngay trong vòng 3 phút, bảo đảm nhánh `main` luôn ở trạng thái biên dịch thành công.",
            "Developer Guide chuẩn: Các bước `docker compose up -d`, `npm install`, `pytest` được chuẩn hóa."
        ],
        "blueprint": {
            "what": "Thực hành phát triển phần mềm trong đó các thành viên tích hợp mã nguồn thường xuyên vào nhánh chính, mỗi lần tích hợp được kiểm tra tự động bằng build và test.",
            "how": "Cấu hình GitHub Actions runner → Thiết lập jobs linting, testing, validation → Tích hợp dịch vụ gửi email Brevo qua Webhook/Action → Ban hành Developer Guide.",
            "why": "Loại bỏ 'Integration Hell' (địa ngục tích hợp vào cuối kỳ), tăng độ tin cậy và tốc độ phát triển của nhóm.",
            "evidence": "Chỉ vào Bản in file `.github/workflows/ci.yml`, Ảnh chụp màn hình CI-pass và Email thông báo thực tế."
        },
        "related_links": [
            "[docs.1/md/13-continuous-integration.md](../../md/13-continuous-integration.md)",
            "[docs.1/pdf/13-continuous-integration.pdf](../../pdf/13-continuous-integration.pdf)",
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
                "name": "Bản in kịch bản triển khai (Deployment Scripts) — .github/workflows/cd.yml, scripts/run-prod.sh",
                "type": "Kịch bản CD (Code printout)",
                "source_md": ".github/workflows/cd.yml",
                "source_pdf": "final-exam/preparation/5_CICD_DevOps_Testing/README.pdf",
                "desc": "Kịch bản tự động hóa quy trình đóng gói container, chạy migration và deploy lên hạ tầng Staging/Production."
            },
            {
                "name": "Bản in kịch bản cấu hình CSDL & dịch vụ bên thứ ba (docker-compose.prod.yml, Terraform)",
                "type": "Kịch bản cấu hình (Code printout)",
                "source_md": "docker-compose.prod.yml",
                "source_pdf": "final-exam/preparation/5_CICD_DevOps_Testing/README.pdf",
                "desc": "Cấu hình Docker Compose Production, Nginx reverse proxy, PostgreSQL, MinIO S3 bucket, Cloudflare R2 và Brevo SMTP."
            },
            {
                "name": "Bản in giao diện email nhận thông báo kết quả triển khai tự động",
                "type": "Ảnh chụp giao diện email",
                "source_md": "final-exam/preparation/5_CICD_DevOps_Testing/printouts/Q14/cd-brevo-deploy-email-live-url-terraform.png",
                "source_pdf": "final-exam/preparation/5_CICD_DevOps_Testing/README.pdf",
                "desc": "Ảnh chụp email Brevo gửi tự động xác nhận deploy thành công kèm đường link Live URL của hệ thống."
            },
            {
                "name": "Bản in tài liệu Hướng dẫn triển khai hệ thống cho kỹ sư vận hành (Deployment Guide)",
                "type": "Tài liệu in A4",
                "source_md": "docs/03-execution-monitoring/07-deployment-guide.md (hoặc docs.1/md/14-continuous-delivery.md)",
                "source_pdf": "docs.1/pdf/14-continuous-delivery.pdf",
                "desc": "Quy trình vận hành, thiết lập biến môi trường, chạy migration Alembic, smoke test và kịch bản Rollback khi có lỗi."
            },
            {
                "name": "Bản in ảnh chụp GitHub Actions CD deploy, Terraform Summary và Live URL",
                "type": "Ảnh chụp màn hình",
                "source_md": "final-exam/preparation/5_CICD_DevOps_Testing/printouts/Q14/cd-workflow-deploy.png",
                "source_pdf": "final-exam/preparation/5_CICD_DevOps_Testing/README.pdf",
                "desc": "Minh chứng thực tế pipeline CD chạy pass và live URL hệ thống."
            }
        ],
        "key_evidence": [
            "Mô hình CD: CI Pass → Build Docker Images → Terraform Provisioning → Apply Database Migrations (Alembic) → Deploy Containers → Smoke Test tự động → Gửi Email Live URL.",
            "Kịch bản triển khai: `.github/workflows/cd.yml`, `scripts/run-prod.sh`, `docker-compose.prod.yml`.",
            "Chiến lược Rollback: Tự động giữ bản backup CSDL trước migration, hỗ trợ rollback phiên bản container trước đó trong < 2 phút.",
            "Bằng chứng Live URL và email thông báo thực tế từ Brevo."
        ],
        "blueprint": {
            "what": "Mở rộng của CI nhằm đảm bảo mã nguồn sau khi vượt qua kiểm tra có thể tự động hoặc bán tự động triển khai an toàn lên môi trường vận hành.",
            "how": "Tự động hóa đóng gói container → Áp dụng IaC Terraform → Chạy migration cơ sở dữ liệu có kiểm soát → Kích hoạt smoke test → Gửi thông báo kết quả qua email.",
            "why": "Rút ngắn thời gian đưa tính năng mới tới người dùng (Time-to-Market), giảm thiểu rủi ro lỗi thao tác thủ công khi triển khai.",
            "evidence": "Chỉ vào File `cd.yml`, File `docker-compose.prod.yml`, Ảnh chụp Live URL và Email thông báo deploy."
        },
        "related_links": [
            "[docs.1/md/14-continuous-delivery.md](../../md/14-continuous-delivery.md)",
            "[docs.1/pdf/14-continuous-delivery.pdf](../../pdf/14-continuous-delivery.pdf)",
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
                "name": "Bản in kịch bản khởi tạo và cấu hình tài nguyên hạ tầng (Terraform / IaC Scripts)",
                "type": "Kịch bản IaC (Code printout)",
                "source_md": "terraform/main.tf (hoặc docker-compose.prod.yml)",
                "source_pdf": "final-exam/preparation/5_CICD_DevOps_Testing/README.pdf",
                "desc": "Kịch bản Terraform và Docker Compose định nghĩa toàn bộ tài nguyên máy chủ, mạng, volume lưu trữ và dịch vụ giám sát."
            },
            {
                "name": "Bản in hệ thống thư mục và tệp tin hỗ trợ quản lý hạ tầng triển khai",
                "type": "Cây thư mục / Cấu hình hạ tầng",
                "source_md": "docs.1/md/15-devops-and-operations.md",
                "source_pdf": "docs.1/pdf/15-devops-and-operations.pdf",
                "desc": "Cây cấu trúc thư mục `terraform/`, `monitoring/` (Prometheus, Grafana), `scripts/` (backup-postgres.sh, backup-minio.sh) và Nginx config."
            },
            {
                "name": "Bản in giao diện Monitoring Prometheus/Grafana, Docker Containers và Health Check",
                "type": "Ảnh chụp màn hình giám sát",
                "source_md": "final-exam/preparation/5_CICD_DevOps_Testing/printouts/Q15/",
                "source_pdf": "final-exam/preparation/5_CICD_DevOps_Testing/README.pdf",
                "desc": "Ảnh chụp dashboard giám sát hiệu năng hệ thống CPU/RAM/Network, Prometheus metrics và Docker container health status."
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
            "evidence": "Chỉ vào File `terraform/main.tf`, Cây thư mục `monitoring/` và Ảnh chụp Grafana Dashboard trong bản in."
        },
        "related_links": [
            "[docs.1/md/15-devops-and-operations.md](../../md/15-devops-and-operations.md)",
            "[docs.1/pdf/15-devops-and-operations.pdf](../../pdf/15-devops-and-operations.pdf)",
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
                "name": "Bản in ảnh chụp chung các thành viên trong nhóm Sebros",
                "type": "Ảnh chụp thực tế",
                "source_md": "final-exam/preparation/6_Team_Monitoring_Risk_Lessons/README.md",
                "source_pdf": "final-exam/preparation/6_Team_Monitoring_Risk_Lessons/README.pdf",
                "desc": "Ảnh chụp đầy đủ 6 thành viên nhóm Sebros cùng tham gia sinh hoạt dự án."
            },
            {
                "name": "Bản in tài liệu quy định, quy chế, lịch làm việc của nhóm (Team Contract)",
                "type": "Tài liệu in A4",
                "source_md": "docs.1/md/16-team-contract.md",
                "source_pdf": "docs.1/pdf/16-team-contract.pdf",
                "desc": "Hợp đồng nhóm quy định giá trị cốt lõi, vai trò 6 thành viên, quy tắc giao tiếp, chuẩn mực commit, nguyên tắc giải quyết xung đột và thang kỷ luật."
            },
            {
                "name": "Bản in một biên bản họp của nhóm (Meeting Minutes)",
                "type": "Tài liệu in A4",
                "source_md": "final-exam/preparation/6_Team_Monitoring_Risk_Lessons/README.md",
                "source_pdf": "final-exam/preparation/6_Team_Monitoring_Risk_Lessons/README.pdf",
                "desc": "Biên bản họp tuần ghi nhận nội dung thảo luận, phân chia nhiệm vụ, giải quyết blocker và ký nhận của các thành viên."
            },
            {
                "name": "Bản in giao diện hệ thống liên lạc với dữ liệu thực tế của nhóm",
                "type": "Ảnh chụp giao diện",
                "source_md": "final-exam/preparation/6_Team_Monitoring_Risk_Lessons/README.md",
                "source_pdf": "final-exam/preparation/6_Team_Monitoring_Risk_Lessons/README.pdf",
                "desc": "Ảnh chụp không gian làm việc Discord (kênh standup, review code, chia sẻ tài liệu) với dữ liệu trao đổi thực tế của nhóm."
            }
        ],
        "key_evidence": [
            "5 Giai đoạn phát triển nhóm theo mô hình Tuckman: Forming (Thành lập) → Storming (Xung đột) → Norming (Ổn định) → Performing (Hiệu suất cao) → Adjourning (Đóng dự án).",
            "Vấn đề xung đột thực tế: Tranh cãi lựa chọn công nghệ OCR (Tesseract vs Cloud Vision), xung đột lịch làm việc khi thành viên trùng lịch học/thi cử.",
            "Cách giải quyết: Áp dụng PoC thực nghiệm để đưa ra quyết định kỹ thuật khách quan; thiết lập kênh thông báo vắng mặt trước 24h và tái phân bổ công việc qua Kanban.",
            "Kết quả: 100% thành viên đồng thuận, duy trì kỷ luật nhóm và hoàn thành đúng cam kết."
        ],
        "blueprint": {
            "what": "Nghệ thuật và phương pháp điều phối, tạo động lực, giải quyết xung đột và phát triển năng lực của các thành viên trong nhóm.",
            "how": "Soạn thảo Team Contract → Thiết lập kênh liên lạc chính thức → Tổ chức họp định kỳ → Áp dụng quy trình giải quyết xung đột dân chủ → Đánh giá đóng góp cá nhân.",
            "why": "Con người là yếu tố quyết định sự thành bại của dự án; quản trị tốt giúp duy trì tinh thần đồng đội và năng suất cao.",
            "evidence": "Chỉ vào Bản in Team Contract (Mục 3-4), Biên bản họp nhóm và Ảnh chụp kênh Discord thực tế."
        },
        "related_links": [
            "[docs.1/md/16-team-contract.md](../../md/16-team-contract.md)",
            "[docs.1/pdf/16-team-contract.pdf](../../pdf/16-team-contract.pdf)",
            "[Phiếu ôn tập Câu 16 (final-exam/preparation/6_Team_Monitoring_Risk_Lessons/README.md)](../../../final-exam/preparation/6_Team_Monitoring_Risk_Lessons/README.md)"
        ]
    },
    {
        "num": 17,
        "num_str": "17",
        "title": "Phân công, theo dõi, đánh giá, kiểm soát công việc và báo cáo tình trạng dự án",
        "english_title": "Project Monitoring, Control & Status Reporting",
        "question_prompt": "Trình bày quá trình phân công, theo dõi, đánh giá, kiểm soát các công việc dự án, và báo cáo tình trạng dự án của nhóm. _(Sinh viên nộp kèm bản in giao diện hệ thống phân công, theo dõi công việc với dữ liệu thực tế của nhóm, bản in giao diện hệ thống quản lý thời gian đã dùng cho từng công việc với dữ liệu thực tế của nhóm, bản in bản cập nhật tài liệu Kế hoạch dự án theo dữ liệu thực tiễn, biểu đồ burndown của toàn dự án, tài liệu báo cáo tình trạng toàn bộ dự án của nhóm ở tuần trước tuần thi giữa học kỳ.)_",
        "submissions": [
            {
                "name": "Bản in giao diện hệ thống phân công, theo dõi công việc với dữ liệu thực tế",
                "type": "Ảnh chụp màn hình Kanban Board",
                "source_md": "final-exam/preparation/6_Team_Monitoring_Risk_Lessons/README.md",
                "source_pdf": "final-exam/preparation/6_Team_Monitoring_Risk_Lessons/README.pdf",
                "desc": "Ảnh chụp bảng GitHub Projects Kanban với 26 Story cards, phân chia theo 6 cột trạng thái, WIP limits và người phụ trách."
            },
            {
                "name": "Bản in giao diện hệ thống quản lý thời gian đã dùng (Project Log / Time Tracking)",
                "type": "Tài liệu in A4 / Bảng dữ liệu",
                "source_md": "docs.1/md/17-project-log.md",
                "source_pdf": "docs.1/pdf/17-project-log.pdf",
                "desc": "Nhật ký dự án ghi nhận chi tiết thời gian thực tế (Actual Hours) của 6 thành viên đối chiếu với ước lượng (Estimate Hours)."
            },
            {
                "name": "Bản in bản cập nhật tài liệu Kế hoạch dự án theo dữ liệu thực tiễn (Project Plan Actuals)",
                "type": "Tài liệu in A4",
                "source_md": "docs.1/md/11-project-plan.md",
                "source_pdf": "docs.1/pdf/11-project-plan.pdf",
                "desc": "Bản cập nhật tiến độ thực tế so với đường cơ sở, phân tích Schedule Variance (SV) và Effort Variance (EV)."
            },
            {
                "name": "Bản in biểu đồ Burndown / Cumulative Flow Diagram (CFD) của toàn dự án",
                "type": "Biểu đồ tiến độ in A4",
                "source_md": "final-exam/preparation/6_Team_Monitoring_Risk_Lessons/README.md",
                "source_pdf": "final-exam/preparation/6_Team_Monitoring_Risk_Lessons/README.pdf",
                "desc": "Biểu đồ tích lũy luồng CFD và Burndown phản ánh tiến độ hoàn thành công việc theo từng tuần."
            },
            {
                "name": "Bản in báo cáo tình trạng toàn bộ dự án ở tuần trước thi giữa kỳ (Midterm Status Report)",
                "type": "Báo cáo in A4",
                "source_md": "docs/04-review-presentation/01-midterm-requirement.md",
                "source_pdf": "final-exam/preparation/6_Team_Monitoring_Risk_Lessons/README.pdf",
                "desc": "Báo cáo tiến độ tuần 5 tổng kết các hạng mục đã hoàn thành (M1, M2, M3), rủi ro đang xử lý và kế hoạch nửa sau học kỳ."
            }
        ],
        "key_evidence": [
            "Dữ liệu thực tế: Tổng giờ thực tế Actual = 184 giờ-người so với Ước lượng 190 giờ-người (tiết kiệm 6 giờ, độ lệch -3.1%).",
            "Chỉ số luồng: Lead Time trung bình 4.2 ngày, Cycle Time 2.1 ngày, không có card nào bị tắc nghẽn quá 5 ngày.",
            "Kiểm soát tiến độ qua GitHub Projects, Pull Requests và Project Log hàng ngày.",
            "Báo cáo giữa kỳ minh chứng dự án đạt 100% mục tiêu giai đoạn 1."
        ],
        "blueprint": {
            "what": "Quy trình thu thập dữ liệu hiệu suất, so sánh thực tế với kế hoạch và thực hiện các biện pháp điều chỉnh cần thiết.",
            "how": "Cập nhật board hàng ngày → Ghi nhận Project Log sau mỗi task → Phân tích biểu đồ CFD/Burndown → Phát hiện độ lệch → Báo cáo tình trạng định kỳ.",
            "why": "Phát hiện sớm nguy cơ trễ hạn hoặc vượt tải để có biện pháp can thiệp kịp thời trước khi quá muộn.",
            "evidence": "Chỉ vào Bảng Kanban thực tế, Bảng theo dõi Actual Hours trong Project Log và Biểu đồ Burndown/CFD."
        },
        "related_links": [
            "[docs.1/md/17-project-log.md](../../md/17-project-log.md)",
            "[docs.1/pdf/17-project-log.pdf](../../pdf/17-project-log.pdf)",
            "[docs.1/md/11-project-plan.md](../../md/11-project-plan.md)",
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
                "source_md": "docs.1/md/18-risk-management-plan.md",
                "source_pdf": "docs.1/pdf/18-risk-management-plan.pdf",
                "desc": "Tài liệu quy trình quản lý rủi ro 4 bước, Ma trận xác suất - tác động 5x5, và Sổ đăng ký rủi ro (Risk Register) định danh 18 rủi ro cụ thể."
            }
        ],
        "key_evidence": [
            "Quy trình quản lý rủi ro 4 bước: Nhận diện (Identify) → Phân tích & Đánh giá (Analyze & Assess) → Lập kế hoạch ứng phó (Plan Response) → Giám sát & Kiểm soát (Monitor & Control).",
            "Ma trận 5x5: Phân loại rủi ro theo mức độ Nghiêm trọng (Critical: Score ≥ 15), Cao (High: 10-14), Trung bình (Medium: 5-9), Thấp (Low: 1-4).",
            "18 Rủi ro định danh (RSK-01 đến RSK-18): Ví dụ RSK-01 (Độ chính xác OCR tiếng Việt thấp), RSK-02 (Tràn dung lượng lưu trữ), RSK-05 (Thành viên bị ốm/trùng lịch thi).",
            "Chiến lược 4T: Treat (Giảm thiểu qua PoC), Tolerate (Chấp nhận), Transfer (Chuyển giao), Terminate (Né tránh/loại khỏi scope)."
        ],
        "blueprint": {
            "what": "Kế hoạch chủ động nhận diện, phân tích và chuẩn bị các biện pháp ứng phó với các sự kiện không chắc chắn có thể ảnh hưởng đến dự án.",
            "how": "Họp Brainstorming nhận diện rủi ro → Đánh giá P (Probability) và I (Impact) → Lập Risk Register → Xây dựng Kịch bản ứng phó (Mitigation & Contingency) → Review hàng tuần.",
            "why": "Chuyển từ thế bị động (chữa cháy) sang thế chủ động kiểm soát rủi ro, giảm thiểu thiệt hại về thời gian và chi phí.",
            "evidence": "Chỉ vào Ma trận 5x5 và Sổ đăng ký 18 rủi ro (Mục 3) trong bản in Kế hoạch quản lý rủi ro."
        },
        "related_links": [
            "[docs.1/md/18-risk-management-plan.md](../../md/18-risk-management-plan.md)",
            "[docs.1/pdf/18-risk-management-plan.pdf](../../pdf/18-risk-management-plan.pdf)",
            "[Phiếu ôn tập Câu 18 (final-exam/preparation/6_Team_Monitoring_Risk_Lessons/README.md)](../../../final-exam/preparation/6_Team_Monitoring_Risk_Lessons/README.md)"
        ]
    },
    {
        "num": 19,
        "num_str": "19",
        "title": "Kế hoạch quản lý chất lượng (Software Quality Management Plan)",
        "english_title": "Software Quality Management Plan",
        "question_prompt": "Trình bày quá trình hình thành và phương pháp đánh giá tài liệu Kế hoạch quản lý chất lượng (Software Quality Management Plan) của nhóm. _(Sinh viên nộp kèm bản in tài liệu Kế hoạch quản lý chất lượng của nhóm, bản in định nghĩa hoàn thành (Definition of Done) của nhóm, bản in giao diện cấu hình đảm bảo Coding Standards cho mã nguồn của nhóm, bản in biên bản thanh tra mã nguồn của nhóm, bản in biên bản phản hồi từ khách hàng của nhóm.)_",
        "submissions": [
            {
                "name": "Bản in tài liệu Kế hoạch quản lý chất lượng (Software Quality Management Plan)",
                "type": "Tài liệu in A4",
                "source_md": "docs.1/md/19-quality-management-plan.md",
                "source_pdf": "docs.1/pdf/19-quality-management-plan.pdf",
                "desc": "Tài liệu định nghĩa hệ thống QA/QC, 6 Quality Gates, tiêu chuẩn chất lượng sản phẩm ISO 25010 và chỉ số đo lường."
            },
            {
                "name": "Bản in Định nghĩa hoàn thành (Definition of Done - DoD)",
                "type": "Tài liệu / Tiêu chuẩn in A4",
                "source_md": "docs.1/md/19-quality-management-plan.md (Mục 3) / 04-product-backlog.md",
                "source_pdf": "docs.1/pdf/19-quality-management-plan.pdf",
                "desc": "Checklist tiêu chí bắt buộc để một User Story được công nhận Done: Code clean, Unit test pass, Code Review pass, Tài liệu cập nhật, CI pass."
            },
            {
                "name": "Bản in giao diện cấu hình đảm bảo Coding Standards cho mã nguồn",
                "type": "Tài liệu / Kịch bản linter",
                "source_md": "final-exam/preparation/6_Team_Monitoring_Risk_Lessons/03_coding_standards_and_linter_config.md",
                "source_pdf": "final-exam/preparation/6_Team_Monitoring_Risk_Lessons/README.pdf",
                "desc": "Cấu hình linter chuẩn: Ruff cho Python (`ruff.toml`), ESLint/Prettier cho Next.js, Markdownlint cho tài liệu."
            },
            {
                "name": "Bản in Biên bản thanh tra mã nguồn của nhóm (Code Inspection Record)",
                "type": "Biên bản in A4",
                "source_md": "final-exam/preparation/6_Team_Monitoring_Risk_Lessons/01_code_inspection_record_pr41.md",
                "source_pdf": "final-exam/preparation/6_Team_Monitoring_Risk_Lessons/README.pdf",
                "desc": "Biên bản thanh tra chính thức cho Pull Request #41 (Tối ưu hóa pipeline OCR) theo chuẩn IEEE 1028 với checklist và danh sách defect đã fix."
            },
            {
                "name": "Bản in Biên bản phản hồi từ khách hàng / UAT (UAT Feedback Record)",
                "type": "Biên bản in A4",
                "source_md": "final-exam/preparation/6_Team_Monitoring_Risk_Lessons/02_uat_feedback_record.md",
                "source_pdf": "final-exam/preparation/6_Team_Monitoring_Risk_Lessons/README.pdf",
                "desc": "Biên bản kiểm thử chấp nhận người dùng thực tế ngày 15/08/2026 với đại diện Thư viện đánh giá 6 kịch bản UAT."
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
            "[docs.1/md/19-quality-management-plan.md](../../md/19-quality-management-plan.md)",
            "[docs.1/pdf/19-quality-management-plan.pdf](../../pdf/19-quality-management-plan.pdf)",
            "[Biên bản thanh tra PR #41 (01_code_inspection_record_pr41.md)](../../../final-exam/preparation/6_Team_Monitoring_Risk_Lessons/01_code_inspection_record_pr41.md)",
            "[Biên bản phản hồi UAT (02_uat_feedback_record.md)](../../../final-exam/preparation/6_Team_Monitoring_Risk_Lessons/02_uat_feedback_record.md)",
            "[Cấu hình Coding Standards (03_coding_standards_and_linter_config.md)](../../../final-exam/preparation/6_Team_Monitoring_Risk_Lessons/03_coding_standards_and_linter_config.md)",
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
                "source_md": "docs.1/md/20-test-plan.md",
                "source_pdf": "docs.1/pdf/20-test-plan.pdf",
                "desc": "Chiến lược kiểm thử đa tầng (Unit, Integration, Security, Performance, UAT), ma trận truy vết yêu cầu - ca kiểm thử (RTM) và môi trường test."
            },
            {
                "name": "Bản in giao diện cấu hình đảm bảo Coding Standards cho mã nguồn",
                "type": "Tài liệu / Cấu hình linter",
                "source_md": "final-exam/preparation/6_Team_Monitoring_Risk_Lessons/03_coding_standards_and_linter_config.md",
                "source_pdf": "final-exam/preparation/6_Team_Monitoring_Risk_Lessons/README.pdf",
                "desc": "Cấu hình linter `ruff.toml` và `.eslintrc.json` đảm bảo kiểm soát cú pháp và chuẩn code."
            },
            {
                "name": "Bản in giao diện hệ thống quản lý lỗi với dữ liệu thực tế (Bug Tracking / GitHub Issues)",
                "type": "Ảnh chụp màn hình Bug Tracker",
                "source_md": "final-exam/preparation/5_CICD_DevOps_Testing/printouts/Q20/",
                "source_pdf": "final-exam/preparation/5_CICD_DevOps_Testing/README.pdf",
                "desc": "Ảnh chụp GitHub Issues với các bug thực tế được gắn nhãn `bug`, `severity: high/medium`, `status: closed/resolved` kèm commit fix."
            },
            {
                "name": "Bản in giao diện kết quả chạy mã nguồn Unit Tests (Pytest / Vitest Report)",
                "type": "Ảnh chụp màn hình Test Execution",
                "source_md": "final-exam/preparation/5_CICD_DevOps_Testing/printouts/Q20/",
                "source_pdf": "final-exam/preparation/5_CICD_DevOps_Testing/README.pdf",
                "desc": "Ảnh chụp màn hình console chạy Pytest backend và Vitest frontend với 100% tests pass và báo cáo code coverage."
            },
            {
                "name": "Bản in Biên bản thanh tra mã nguồn của nhóm (Code Inspection Record)",
                "type": "Biên bản in A4",
                "source_md": "final-exam/preparation/6_Team_Monitoring_Risk_Lessons/01_code_inspection_record_pr41.md",
                "source_pdf": "final-exam/preparation/6_Team_Monitoring_Risk_Lessons/README.pdf",
                "desc": "Biên bản thanh tra PR #41."
            },
            {
                "name": "Bản in Báo cáo kết quả kiểm thử (Test Execution Summary Report)",
                "type": "Báo cáo in A4",
                "source_md": "docs.1/md/20-test-plan.md (Mục Báo cáo kết quả)",
                "source_pdf": "docs.1/pdf/20-test-plan.pdf",
                "desc": "Tổng hợp kết quả kiểm thử: Tổng test cases, số lượng pass/fail, độ bao phủ coverage và tình trạng đóng defect."
            },
            {
                "name": "Bản in Biên bản phản hồi của khách hàng (UAT Feedback Record)",
                "type": "Biên bản in A4",
                "source_md": "final-exam/preparation/6_Team_Monitoring_Risk_Lessons/02_uat_feedback_record.md",
                "source_pdf": "final-exam/preparation/6_Team_Monitoring_Risk_Lessons/README.pdf",
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
            "evidence": "Chỉ vào Bản in Test Plan, Ảnh chụp màn hình Pytest Report, GitHub Issues Bug Tracker và Biên bản UAT."
        },
        "related_links": [
            "[docs.1/md/20-test-plan.md](../../md/20-test-plan.md)",
            "[docs.1/pdf/20-test-plan.pdf](../../pdf/20-test-plan.pdf)",
            "[Phiếu ôn tập Câu 20 (final-exam/preparation/5_CICD_DevOps_Testing/README.md)](../../../final-exam/preparation/5_CICD_DevOps_Testing/README.md)",
            "[Biên bản thanh tra PR #41 (01_code_inspection_record_pr41.md)](../../../final-exam/preparation/6_Team_Monitoring_Risk_Lessons/01_code_inspection_record_pr41.md)",
            "[Biên bản phản hồi UAT (02_uat_feedback_record.md)](../../../final-exam/preparation/6_Team_Monitoring_Risk_Lessons/02_uat_feedback_record.md)"
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
                "source_md": "docs.1/md/21-lessons-learned.md",
                "source_pdf": "docs.1/pdf/21-lessons-learned.pdf",
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
            "[docs.1/md/21-lessons-learned.md](../../md/21-lessons-learned.md)",
            "[docs.1/pdf/21-lessons-learned.pdf](../../pdf/21-lessons-learned.pdf)",
            "[Phiếu ôn tập Câu 21 (final-exam/preparation/6_Team_Monitoring_Risk_Lessons/README.md)](../../../final-exam/preparation/6_Team_Monitoring_Risk_Lessons/README.md)"
        ]
    }
]

def generate_evidence_files():
    os.makedirs(EVIDENCE_DIR, exist_ok=True)
    
    # 1. Generate individual question READMEs
    for q in QUESTIONS_DATA:
        # Create folder for 01..21 and 1..21
        folder_names = [q["num_str"], str(q["num"])]
        
        # Build Markdown content
        md_lines = []
        md_lines.append(f"# BẰNG CHỨNG NỘP KÈM — CÂU {q['num']}: {q['title'].upper()}\n")
        md_lines.append(f"**Mã câu hỏi:** `CÂU-{q['num_str']}` | **Chủ đề:** {q['english_title']}\n")
        md_lines.append("## 1. Đề bài và Yêu cầu nộp kèm từ Đề thi vấn đáp\n")
        md_lines.append(f"> {q['question_prompt']}\n")
        
        md_lines.append("## 2. Danh mục tài liệu / bằng chứng cần nộp kèm khi thi\n")
        md_lines.append("| STT | Tên tài liệu / Bằng chứng nộp kèm | Loại tài liệu | Nguồn tệp Markdown | Nguồn tệp PDF / Ảnh chụp | Mô tả chi tiết |")
        md_lines.append("|:---:|---|---|---|---|---|")
        
        for idx, sub in enumerate(q["submissions"], 1):
            src_md_link = f"[{os.path.basename(sub['source_md'])}]({sub['source_md']})" if sub.get("source_md") else "N/A"
            src_pdf_link = f"[{os.path.basename(sub['source_pdf'])}]({sub['source_pdf']})" if sub.get("source_pdf") else "N/A"
            md_lines.append(f"| {idx} | **{sub['name']}** | `{sub['type']}` | {src_md_link} | {src_pdf_link} | {sub['desc']} |")
        
        md_lines.append("\n## 3. Các bằng chứng & số liệu then chốt cần chỉ ra trên tài liệu\n")
        for item in q["key_evidence"]:
            md_lines.append(f"- **{item.split(':')[0]}:**{':'.join(item.split(':')[1:])}")
            
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
        
        # Write to folder (standardized 01..21)
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
    master_lines.append("| Câu | Tên câu hỏi | Thư mục bằng chứng | Tài liệu nộp kèm chính | Tệp Markdown nguồn | Tệp PDF nguồn |")
    master_lines.append("|:---:|---|:---:|---|---|---|")
    
    for q in QUESTIONS_DATA:
        folder_link = f"[{q['num_str']}](./{q['num_str']}/README.md)"
        sub_names = ", ".join([f"**{s['name']}**" for s in q["submissions"]])
        md_links = ", ".join([f"[{os.path.basename(s['source_md'])}](../md/{os.path.basename(s['source_md'])})" for s in q["submissions"] if "docs.1/md" in s.get("source_md", "")])
        if not md_links:
            md_links = "N/A"
        pdf_links = ", ".join([f"[{os.path.basename(s['source_pdf'])}](../pdf/{os.path.basename(s['source_pdf'])})" for s in q["submissions"] if "docs.1/pdf" in s.get("source_pdf", "")])
        if not pdf_links:
            pdf_links = "N/A"
        master_lines.append(f"| **{q['num']}** | {q['title']} | {folder_link} | {sub_names} | {md_links} | {pdf_links} |")
        
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
