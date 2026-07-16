import { useEffect, useState } from 'react'
import { Link, useParams } from 'react-router'
import {
  getDocument,
  getDocumentPages,
  getDocumentSourceUrl,
  getOcrStatus,
  getPageImageUrl,
} from '../services/api'
import type { DocumentDetail, DocumentPage, OcrJob } from '../services/api'

export function DocumentViewerPage() {
  const { documentId } = useParams<{ documentId: string }>()
  const [document, setDocument] = useState<DocumentDetail | null>(null)
  const [pages, setPages] = useState<DocumentPage[]>([])
  const [job, setJob] = useState<OcrJob | null>(null)
  const [selectedPageNumber, setSelectedPageNumber] = useState<number | null>(null)
  const [isLoading, setIsLoading] = useState(true)
  const [error, setError] = useState('')

  useEffect(() => {
    let cancelled = false
    if (!documentId) {
      setError('Document ID không hợp lệ.')
      setIsLoading(false)
      return
    }

    async function loadDocument() {
      try {
        const detail = await getDocument(documentId!)
        const [documentPages, ocrJob] = await Promise.all([
          getDocumentPages(documentId!),
          getOcrStatus(documentId!),
        ])
        if (cancelled) return
        setDocument(detail)
        setPages(documentPages)
        setJob(ocrJob)
        setSelectedPageNumber(documentPages[0]?.page_number ?? null)
        setError('')
      } catch (loadError) {
        if (!cancelled) {
          setError(
            loadError instanceof Error ? loadError.message : 'Không thể mở tài liệu đã scan.',
          )
        }
      } finally {
        if (!cancelled) setIsLoading(false)
      }
    }

    void loadDocument()
    return () => {
      cancelled = true
    }
  }, [documentId])

  const selectedPage = pages.find((page) => page.page_number === selectedPageNumber) ?? null

  if (isLoading) {
    return <main className="page-shell viewer-page viewer-state">Đang mở tài liệu…</main>
  }

  if (error || !document || !documentId) {
    return (
      <main className="page-shell viewer-page viewer-state">
        <p className="message error" role="alert">
          {error || 'Không tìm thấy tài liệu.'}
        </p>
        <Link className="secondary-link" to="/documents">
          ← Về danh sách
        </Link>
      </main>
    )
  }

  return (
    <main className="page-shell viewer-page">
      <header className="viewer-heading">
        <div>
          <Link className="back-link" to="/documents">
            ← Tài liệu đã scan
          </Link>
          <p className="eyebrow">Document viewer</p>
          <h1>{document.title || document.original_filename}</h1>
          <p className="viewer-subtitle">
            {document.author || 'Chưa có tác giả'} · {document.original_filename}
          </p>
        </div>
        <div className="viewer-actions">
          <span className={`status-badge status-${job?.status || 'pending'}`}>
            OCR {job?.status || document.status}
          </span>
          <a
            className="secondary-link"
            href={getDocumentSourceUrl(documentId)}
            target="_blank"
            rel="noreferrer"
          >
            Mở file gốc ↗
          </a>
        </div>
      </header>

      <section className="viewer-metadata" aria-label="Thông tin tài liệu">
        <div>
          <span>Document ID</span>
          <strong>{document.id}</strong>
        </div>
        <div>
          <span>Định dạng</span>
          <strong>{document.content_type}</strong>
        </div>
        <div>
          <span>Số trang xử lý</span>
          <strong>{pages.length}</strong>
        </div>
        <div>
          <span>Ngày tạo</span>
          <strong>{new Date(document.created_at).toLocaleDateString('vi-VN')}</strong>
        </div>
      </section>

      {pages.length === 0 ? (
        <section className="viewer-empty">
          <span aria-hidden="true">⌛</span>
          <h2>Chưa có trang đã xử lý</h2>
          <p>
            {job?.status === 'failed'
              ? job.error_message || 'OCR đã thất bại.'
              : 'OCR đang chạy; quay lại dashboard để theo dõi tiến trình.'}
          </p>
          <Link className="primary-link" to="/dashboard">
            Mở Dashboard OCR
          </Link>
        </section>
      ) : (
        <>
          <nav className="page-selector" aria-label="Chọn trang tài liệu">
            <span>Trang</span>
            <div>
              {pages.map((page) => (
                <button
                  type="button"
                  key={page.page_number}
                  className={selectedPageNumber === page.page_number ? 'active' : ''}
                  aria-current={selectedPageNumber === page.page_number ? 'page' : undefined}
                  onClick={() => setSelectedPageNumber(page.page_number)}
                >
                  {page.page_number}
                </button>
              ))}
            </div>
          </nav>

          {selectedPage && (
            <section
              className="scan-split-view"
              aria-label={`Nội dung trang ${selectedPage.page_number}`}
            >
              <article className="scan-pane">
                <header>
                  <span>Ảnh scan</span>
                  <strong>Trang {selectedPage.page_number}</strong>
                </header>
                <div className="scan-image-frame">
                  {selectedPage.has_image ? (
                    <img
                      src={getPageImageUrl(documentId, selectedPage.page_number)}
                      alt={`Ảnh scan trang ${selectedPage.page_number}`}
                    />
                  ) : (
                    <p>Trang này chưa có ảnh preview.</p>
                  )}
                </div>
              </article>
              <article className="processed-pane">
                <header>
                  <span>Văn bản OCR</span>
                  <strong>{selectedPage.text_content.length} ký tự</strong>
                </header>
                <pre>{selectedPage.text_content || 'Trang này chưa có nội dung OCR.'}</pre>
              </article>
            </section>
          )}
        </>
      )}
    </main>
  )
}
