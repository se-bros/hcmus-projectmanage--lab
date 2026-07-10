import { useState, useCallback } from 'react'
import {
  Upload, FileText, Eye, CheckCircle, Cpu, Tag as TagIcon,
  ChevronRight, Loader2, Sparkles
} from 'lucide-react'
import { CATEGORIES } from '../store/mockData'

type Step = 'upload' | 'ocr' | 'edit' | 'publish' | 'done'

const MOCK_OCR_TEXT = `CHƯƠNG 2: CÁC THUẬT TOÁN SẮP XẾP

Trong chương này, chúng ta sẽ nghiên cứu các thuật toán sắp xếp
phổ biến và phân tích độ phức tạp của chúng.

2.1. Sắp xếp Nổi bọt (Bubble Sort)

Sắp xếp nổi bọt là thuật toán đơn giản nhất, hoạt động bằng cách
lặp đi lặp lại việc so sánh các cặp phần tử liền kề và đổi chỗ
chúng nếu chúng ở sai thứ tự.

Độ phức tạp: O(n²) trong trường hợp xấu nhất.

2.2. Sắp xếp Chèn (Insertion Sort)

Sắp xếp chèn xây dựng mảng đã sắp xếp từng phần tử một. Tại mỗi
bước, nó lấy phần tử tiếp theo và chèn vào đúng vị trí trong phần
đã sắp xếp.

Lưu ý: OCR có thể nhận dạng sai một số ký tự đặc biệt như: O(n²),
các ký hiệu toán học cần kiểm tra kỹ.`

export default function LibrarianDashboard() {
  const [step, setStep] = useState<Step>('upload')
  const [fileName, setFileName] = useState('')
  const [ocrProgress, setOcrProgress] = useState(0)
  const [ocrText, setOcrText] = useState(MOCK_OCR_TEXT)
  const [title, setTitle] = useState('Thuật toán Sắp xếp và Tìm kiếm')
  const [author, setAuthor] = useState('Nguyễn Văn Hùng')
  const [year, setYear] = useState('2024')
  const [category, setCategory] = useState('Khoa học Máy tính')
  const [tags, setTags] = useState('#GiaoTrinh, #Algorithm, #SortSearch')
  const [access, setAccess] = useState('Internal')
  const [isDragging, setIsDragging] = useState(false)

  const handleFileDrop = useCallback((e: React.DragEvent) => {
    e.preventDefault()
    setIsDragging(false)
    const file = e.dataTransfer.files[0]
    if (file) processFile(file.name)
  }, [])

  const handleFileSelect = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0]
    if (file) processFile(file.name)
  }

  const processFile = (name: string) => {
    setFileName(name)
    setStep('ocr')
    setOcrProgress(0)
    // Simulate OCR progress
    let progress = 0
    const interval = setInterval(() => {
      progress += Math.random() * 12 + 3
      if (progress >= 100) {
        progress = 100
        clearInterval(interval)
        setTimeout(() => setStep('edit'), 500)
      }
      setOcrProgress(Math.min(progress, 100))
    }, 180)
  }

  const handlePublish = () => {
    setStep('done')
  }

  const handleReset = () => {
    setStep('upload')
    setFileName('')
    setOcrProgress(0)
    setOcrText(MOCK_OCR_TEXT)
  }

  return (
    <div className="page-container">
      {/* Step indicator */}
      <div className="step-indicator">
        {(['upload', 'ocr', 'edit', 'publish'] as Step[]).map((s, i) => {
          const labels: Record<string, string> = {
            upload: '1. Tải lên',
            ocr: '2. OCR',
            edit: '3. Biên tập',
            publish: '4. Xuất bản',
          }
          const current = ['upload', 'ocr', 'edit', 'publish', 'done'].indexOf(step)
          const idx = ['upload', 'ocr', 'edit', 'publish'].indexOf(s)
          const isDone = current > idx || step === 'done'
          const isCurrent = current === idx && step !== 'done'
          return (
            <div key={s} className={`step-item ${isCurrent ? 'active' : ''} ${isDone ? 'done' : ''}`}>
              <div className="step-circle">
                {isDone ? <CheckCircle size={16} /> : <span>{i + 1}</span>}
              </div>
              <span className="step-label">{labels[s]}</span>
              {i < 3 && <ChevronRight size={16} className="step-arrow" />}
            </div>
          )
        })}
      </div>

      {/* Step 1: Upload */}
      {step === 'upload' && (
        <div className="section-card fade-in">
          <h2 className="section-title">
            <Upload size={22} /> Tải lên Tài liệu Scan
          </h2>
          <div
            className={`drop-zone ${isDragging ? 'dragging' : ''}`}
            onDragOver={(e) => { e.preventDefault(); setIsDragging(true) }}
            onDragLeave={() => setIsDragging(false)}
            onDrop={handleFileDrop}
          >
            <Upload size={48} className="drop-icon" />
            <p className="drop-title">Kéo thả tệp PDF vào đây</p>
            <p className="drop-sub">hoặc</p>
            <label className="btn-primary" style={{ cursor: 'pointer' }}>
              Chọn tệp từ máy tính
              <input type="file" accept=".pdf,.jpg,.png" onChange={handleFileSelect} hidden />
            </label>
            <p className="drop-hint">Hỗ trợ: PDF, JPG, PNG — Tối đa 100MB</p>
          </div>
          <div className="quick-demo">
            <p>Demo nhanh:</p>
            <button className="btn-secondary" onClick={() => processFile('giao_trinh_thuat_toan.pdf')}>
              <FileText size={16} /> Dùng tệp mẫu: giao_trinh_thuat_toan.pdf
            </button>
          </div>
        </div>
      )}

      {/* Step 2: OCR Progress */}
      {step === 'ocr' && (
        <div className="section-card fade-in">
          <h2 className="section-title">
            <Cpu size={22} /> Đang chạy OCR Tesseract...
          </h2>
          <div className="ocr-panel">
            <div className="ocr-file-info">
              <FileText size={20} />
              <span>{fileName}</span>
            </div>
            <div className="ocr-progress-bar">
              <div
                className="ocr-progress-fill"
                style={{ width: `${ocrProgress}%` }}
              />
            </div>
            <div className="ocr-progress-labels">
              <span>Nhận dạng ký tự tiếng Việt (vie)...</span>
              <span>{Math.round(ocrProgress)}%</span>
            </div>
            <div className="ocr-steps">
              {[
                ['Tiền xử lý ảnh (lọc nhiễu, tăng tương phản)', 20],
                ['Phân tích bố cục trang', 40],
                ['Nhận dạng ký tự OCR Tesseract', 70],
                ['Ghép văn bản theo cấu trúc', 90],
                ['Hoàn tất & Lưu kết quả', 100],
              ].map(([label, threshold]) => (
                <div
                  key={label as string}
                  className={`ocr-step ${ocrProgress >= (threshold as number) ? 'done' : ocrProgress >= (threshold as number) - 25 ? 'running' : ''}`}
                >
                  {ocrProgress >= (threshold as number) ? (
                    <CheckCircle size={14} />
                  ) : ocrProgress >= (threshold as number) - 25 ? (
                    <Loader2 size={14} className="spin" />
                  ) : (
                    <div className="dot" />
                  )}
                  <span>{label as string}</span>
                </div>
              ))}
            </div>
          </div>
        </div>
      )}

      {/* Step 3: Split-screen editor */}
      {step === 'edit' && (
        <div className="section-card fade-in" style={{ maxWidth: '100%' }}>
          <div className="edit-header">
            <h2 className="section-title">
              <Eye size={22} /> Biên tập & Hiệu chỉnh OCR
            </h2>
            <div className="edit-header-actions">
              <span className="accuracy-badge">
                <Sparkles size={14} /> Độ chính xác OCR: 91.2%
              </span>
              <button className="btn-primary" onClick={() => setStep('publish')}>
                Tiếp theo: Phân loại & Xuất bản
              </button>
            </div>
          </div>
          <p className="edit-hint">Giao diện Split-screen: đối chiếu ảnh gốc bên trái và biên tập văn bản bên phải</p>
          <div className="split-screen">
            {/* Left: PDF preview */}
            <div className="split-left">
              <div className="split-panel-header">
                <FileText size={14} /> Ảnh scan gốc (trang 1)
              </div>
              <div className="pdf-preview">
                <div className="pdf-page">
                  <p className="pdf-page-title">CHƯƠNG 2: CÁC THUẬT TOÁN SẮP XẾP</p>
                  <div className="pdf-line" style={{ width: '95%' }} />
                  <div className="pdf-line" style={{ width: '88%' }} />
                  <div className="pdf-line" style={{ width: '92%' }} />
                  <div className="pdf-line" style={{ width: '70%' }} />
                  <br />
                  <p className="pdf-subtitle">2.1. Sắp xếp Nổi bọt (Bubble Sort)</p>
                  <div className="pdf-line" style={{ width: '100%' }} />
                  <div className="pdf-line" style={{ width: '85%' }} />
                  <div className="pdf-line" style={{ width: '90%' }} />
                  <div className="pdf-code-block" />
                  <br />
                  <p className="pdf-subtitle">2.2. Sắp xếp Chèn (Insertion Sort)</p>
                  <div className="pdf-line" style={{ width: '100%' }} />
                  <div className="pdf-line" style={{ width: '78%' }} />
                  <div className="pdf-line" style={{ width: '60%' }} />
                </div>
              </div>
            </div>
            {/* Right: Text editor */}
            <div className="split-right">
              <div className="split-panel-header">
                <Eye size={14} /> Văn bản OCR — Biên tập & Định dạng
              </div>
              <textarea
                className="ocr-editor"
                value={ocrText}
                onChange={e => setOcrText(e.target.value)}
                spellCheck={false}
              />
              <div className="editor-toolbar">
                <span className="toolbar-hint">Tip: Sửa lỗi chính tả, thêm # Heading để định dạng cấu trúc</span>
              </div>
            </div>
          </div>
        </div>
      )}

      {/* Step 4: Publish form */}
      {step === 'publish' && (
        <div className="section-card fade-in">
          <h2 className="section-title">
            <TagIcon size={22} /> Siêu dữ liệu & Phân loại Xuất bản
          </h2>
          <div className="publish-form">
            <div className="form-row">
              <label>Tên tài liệu *</label>
              <input
                className="form-input"
                value={title}
                onChange={e => setTitle(e.target.value)}
                placeholder="Nhập tên sách / giáo trình..."
              />
            </div>
            <div className="form-row">
              <label>Tác giả *</label>
              <input
                className="form-input"
                value={author}
                onChange={e => setAuthor(e.target.value)}
              />
            </div>
            <div className="form-row-2">
              <div>
                <label>Nhà xuất bản</label>
                <input className="form-input" defaultValue="NXB ĐHQG-HCM" />
              </div>
              <div>
                <label>Năm xuất bản</label>
                <input
                  className="form-input"
                  value={year}
                  onChange={e => setYear(e.target.value)}
                  type="number"
                />
              </div>
            </div>
            <div className="form-row">
              <label>Danh mục (Category) *</label>
              <select
                className="form-input"
                value={category}
                onChange={e => setCategory(e.target.value)}
              >
                {CATEGORIES.map(c => (
                  <option key={c} value={c}>{c}</option>
                ))}
              </select>
            </div>
            <div className="form-row">
              <label>Thẻ Tag (phân cách bằng dấu phẩy)</label>
              <input
                className="form-input"
                value={tags}
                onChange={e => setTags(e.target.value)}
                placeholder="#GiaoTrinh, #Algorithm..."
              />
            </div>
            <div className="form-row">
              <label>Quyền truy cập</label>
              <div className="access-options">
                {['Public', 'Internal', 'Restricted'].map(a => (
                  <label key={a} className={`access-option ${access === a ? 'selected' : ''}`}>
                    <input
                      type="radio"
                      name="access"
                      value={a}
                      checked={access === a}
                      onChange={() => setAccess(a)}
                      hidden
                    />
                    {a === 'Public' && '🌐 Public'}
                    {a === 'Internal' && '🏛️ Internal'}
                    {a === 'Restricted' && '🔒 Restricted'}
                  </label>
                ))}
              </div>
            </div>
            <div className="form-actions">
              <button className="btn-secondary" onClick={() => setStep('edit')}>
                ← Quay lại Biên tập
              </button>
              <button className="btn-publish" onClick={handlePublish}>
                <Sparkles size={18} />
                Đóng gói EPUB & Xuất bản
              </button>
            </div>
          </div>
        </div>
      )}

      {/* Step 5: Done */}
      {step === 'done' && (
        <div className="section-card fade-in done-card">
          <div className="done-icon">✅</div>
          <h2 className="done-title">Xuất bản thành công!</h2>
          <div className="done-info">
            <div className="done-row"><span>Tài liệu</span><strong>{title}</strong></div>
            <div className="done-row"><span>Tác giả</span><strong>{author}</strong></div>
            <div className="done-row"><span>Danh mục</span><strong>{category}</strong></div>
            <div className="done-row"><span>Quyền truy cập</span><strong>{access}</strong></div>
            <div className="done-row"><span>Trạng thái</span><strong className="status-published">✓ Published</strong></div>
            <div className="done-row"><span>Lưu trữ</span><strong>MinIO → bucket-library/epub/</strong></div>
            <div className="done-row"><span>Elasticsearch</span><strong>Đã lập chỉ mục toàn văn</strong></div>
          </div>
          <button className="btn-primary" onClick={handleReset}>
            ← Số hóa tài liệu tiếp theo
          </button>
        </div>
      )}
    </div>
  )
}
