import { useEffect, useState } from 'react'
import { Link, useParams } from 'react-router'
import { getDocumentContent, type DocumentContent } from '../services/documents'

function ReaderPage() {
  const { documentId } = useParams<{ documentId: string }>()
  const [content, setContent] = useState<DocumentContent | null>(null)
  const [error, setError] = useState<string | null>(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    if (!documentId) {
      return
    }
    setLoading(true)
    setError(null)
    getDocumentContent(documentId)
      .then(setContent)
      .catch((err: Error) => setError(err.message))
      .finally(() => setLoading(false))
  }, [documentId])

  if (loading) {
    return <p className="page-sub">Đang tải nội dung…</p>
  }

  if (error) {
    return (
      <div className="state" role="alert">
        <p className="state-title state-title-danger">Không tìm thấy tài liệu</p>
        <p className="state-detail">{error}</p>
        <Link className="btn-secondary" to="/">
          Về danh sách
        </Link>
      </div>
    )
  }

  return (
    <article className="reader">
      <Link to="/" className="back-link">
        ← Về danh sách
      </Link>
      <div className="reader-text">{content?.text}</div>
    </article>
  )
}

export default ReaderPage
