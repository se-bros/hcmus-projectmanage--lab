import { useCallback, useEffect, useState } from 'react'
import { Link } from 'react-router'
import { getDocuments, type DocumentSummary } from '../services/documents'

const STATUS_LABELS: Record<DocumentSummary['status'], string> = {
  published: 'Đã xuất bản',
  draft: 'Bản nháp',
}

function formatDate(iso: string): string {
  return new Date(iso).toLocaleDateString('vi-VN', {
    day: '2-digit',
    month: '2-digit',
    year: 'numeric',
  })
}

function DocumentListPage() {
  const [documents, setDocuments] = useState<DocumentSummary[]>([])
  const [error, setError] = useState<string | null>(null)
  const [loading, setLoading] = useState(true)

  const load = useCallback(() => {
    setLoading(true)
    setError(null)
    getDocuments()
      .then(setDocuments)
      .catch((err: Error) => setError(err.message))
      .finally(() => setLoading(false))
  }, [])

  useEffect(() => {
    load()
  }, [load])

  return (
    <>
      <div className="page-head">
        <h1 className="page-title">Kho tài liệu</h1>
        <p className="page-sub">
          {loading
            ? 'Đang tải danh sách…'
            : error
              ? 'Thư viện số HCMUS'
              : `${documents.length} tài liệu trong thư viện`}
        </p>
      </div>

      {loading && (
        <div className="table-wrap" aria-hidden="true">
          <div className="skeleton-table">
            <div className="skeleton-row" />
            <div className="skeleton-row" />
            <div className="skeleton-row" />
            <div className="skeleton-row" />
          </div>
        </div>
      )}

      {!loading && error && (
        <div className="state" role="alert">
          <p className="state-title state-title-danger">Không tải được danh sách tài liệu</p>
          <p className="state-detail">{error}</p>
          <button type="button" className="btn-primary" onClick={load}>
            Thử lại
          </button>
        </div>
      )}

      {!loading && !error && documents.length === 0 && (
        <div className="state">
          <p className="state-title">Chưa có tài liệu nào</p>
          <p className="state-detail">Tài liệu được tải lên và số hóa sẽ xuất hiện ở đây.</p>
        </div>
      )}

      {!loading && !error && documents.length > 0 && (
        <div className="table-wrap">
          <table className="doc-table">
            <thead>
              <tr>
                <th>Tài liệu</th>
                <th>Trạng thái</th>
                <th>Ngày tạo</th>
              </tr>
            </thead>
            <tbody>
              {documents.map((doc) => (
                <tr key={doc.id}>
                  <td>
                    <Link className="doc-title-link" to={`/reader/${doc.id}`}>
                      {doc.title}
                    </Link>
                  </td>
                  <td>
                    <span className={`badge badge-${doc.status}`}>{STATUS_LABELS[doc.status]}</span>
                  </td>
                  <td className="doc-date">{formatDate(doc.created_at)}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </>
  )
}

export default DocumentListPage
