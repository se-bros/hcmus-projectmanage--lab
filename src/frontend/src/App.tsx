import { useState } from 'react'
import type { FormEvent } from 'react'
import './App.css'

type DocumentDetail = {
  id: string
  original_filename: string
  status: string
  created_at: string
}

function App() {
  const [file, setFile] = useState<File | null>(null)
  const [document, setDocument] = useState<DocumentDetail | null>(null)
  const [isUploading, setIsUploading] = useState(false)
  const [error, setError] = useState('')

  async function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault()
    if (!file) return

    setIsUploading(true)
    setError('')
    setDocument(null)

    try {
      const formData = new FormData()
      formData.append('file', file)

      const uploadResponse = await fetch('/api/documents', {
        method: 'POST',
        body: formData,
      })
      if (!uploadResponse.ok) throw new Error('Không thể tải tài liệu lên.')

      const { document_id: documentId } = (await uploadResponse.json()) as {
        document_id: string
      }
      const detailResponse = await fetch(`/api/documents/${documentId}`)
      if (!detailResponse.ok) throw new Error('Đã tải lên nhưng không thể đọc metadata.')

      setDocument((await detailResponse.json()) as DocumentDetail)
    } catch (uploadError) {
      setError(
        uploadError instanceof Error ? uploadError.message : 'Không thể kết nối đến máy chủ.',
      )
    } finally {
      setIsUploading(false)
    }
  }

  return (
    <main className="page-shell">
      <section className="upload-card" aria-labelledby="upload-title">
        <header>
          <p className="eyebrow">HCMUS Library</p>
          <h1 id="upload-title">Tải tài liệu scan</h1>
          <p className="intro">Chọn bản scan PDF hoặc hình ảnh để lưu vào kho tài liệu số.</p>
        </header>

        <form onSubmit={handleSubmit}>
          <label className="file-field">
            <span>File tài liệu</span>
            <input
              type="file"
              accept=".pdf,.jpg,.jpeg,.png"
              onChange={(event) => {
                setFile(event.target.files?.[0] ?? null)
                setError('')
              }}
            />
            <small>Định dạng gợi ý: PDF, JPG, JPEG hoặc PNG</small>
          </label>

          {file && (
            <p className="selected-file">
              Đã chọn <strong>{file.name}</strong>
            </p>
          )}

          <button type="submit" disabled={!file || isUploading}>
            {isUploading ? 'Đang tải lên…' : 'Tải tài liệu lên'}
          </button>
        </form>

        {error && (
          <p className="message error" role="alert">
            {error}
          </p>
        )}

        {document && (
          <section className="document-detail" aria-live="polite">
            <div className="success-heading">
              <span aria-hidden="true">✓</span>
              <div>
                <h2>Tải lên thành công</h2>
                <p>Metadata đã được lưu và sẵn sàng cho bước xử lý tiếp theo.</p>
              </div>
            </div>
            <dl>
              <div>
                <dt>ID</dt>
                <dd>{document.id}</dd>
              </div>
              <div>
                <dt>Tên file</dt>
                <dd>{document.original_filename}</dd>
              </div>
              <div>
                <dt>Trạng thái</dt>
                <dd>
                  <span className="status-badge">{document.status}</span>
                </dd>
              </div>
              <div>
                <dt>Thời điểm tạo</dt>
                <dd>{new Date(document.created_at).toLocaleString('vi-VN')}</dd>
              </div>
            </dl>
          </section>
        )}
      </section>
    </main>
  )
}

export default App
