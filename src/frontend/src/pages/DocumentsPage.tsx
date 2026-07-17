import { useEffect, useMemo, useState } from 'react'
import { Link } from 'react-router'
import { getOcrJobs, getPageImageUrl } from '../services/api'
import type { OcrDashboardItem, OcrStatus } from '../services/api'

type Filter = 'all' | OcrStatus

const FILTERS: { value: Filter; label: string }[] = [
  { value: 'all', label: 'Tất cả' },
  { value: 'pending', label: 'Đang chờ' },
  { value: 'processing', label: 'Đang xử lý' },
  { value: 'completed', label: 'Đã xử lý' },
  { value: 'failed', label: 'Lỗi' },
]

const STATUS_LABELS: Record<OcrStatus, string> = {
  pending: 'Đang chờ',
  processing: 'Đang nhận dạng',
  completed: 'Đã xử lý',
  failed: 'Thất bại',
}

function DocumentThumbnail({ item }: { item: OcrDashboardItem }) {
  const [imageFailed, setImageFailed] = useState(false)
  const showPreview = item.ocr_status === 'completed' && !imageFailed

  return (
    <div className="library-thumbnail">
      {showPreview ? (
        <img
          src={getPageImageUrl(item.document_id, 1)}
          alt={`Trang scan đầu tiên của ${item.original_filename}`}
          onError={() => setImageFailed(true)}
        />
      ) : (
        <div className="document-placeholder" aria-hidden="true">
          <span>{item.original_filename.toLowerCase().endsWith('.pdf') ? 'PDF' : 'IMG'}</span>
          <i />
          <i />
          <i />
        </div>
      )}
      <span className="file-type-chip">
        {item.original_filename.split('.').pop()?.toUpperCase() || 'FILE'}
      </span>
    </div>
  )
}

export function DocumentsPage() {
  const [items, setItems] = useState<OcrDashboardItem[]>([])
  const [filter, setFilter] = useState<Filter>('all')
  const [query, setQuery] = useState('')
  const [isLoading, setIsLoading] = useState(true)
  const [error, setError] = useState('')
  const [refreshGeneration, setRefreshGeneration] = useState(0)

  useEffect(() => {
    let cancelled = false
    getOcrJobs()
      .then((nextItems) => {
        if (!cancelled) {
          setItems(nextItems)
          setError('')
        }
      })
      .catch((loadError: unknown) => {
        if (!cancelled) {
          setError(loadError instanceof Error ? loadError.message : 'Không thể tải kho tài liệu.')
        }
      })
      .finally(() => {
        if (!cancelled) setIsLoading(false)
      })
    return () => {
      cancelled = true
    }
  }, [refreshGeneration])

  const visibleItems = useMemo(() => {
    const normalizedQuery = query.trim().toLowerCase()
    return items.filter((item) => {
      const matchesFilter = filter === 'all' || item.ocr_status === filter
      const matchesQuery =
        !normalizedQuery ||
        item.original_filename.toLowerCase().includes(normalizedQuery) ||
        item.document_id.toLowerCase().includes(normalizedQuery)
      return matchesFilter && matchesQuery
    })
  }, [filter, items, query])

  return (
    <main className="page-shell library-page">
      <header className="library-heading">
        <div>
          <p className="eyebrow">Digitized collection</p>
          <h1>Tài liệu đã scan</h1>
          <p className="intro">Xem file nguồn, ảnh từng trang và văn bản OCR đã xử lý.</p>
        </div>
        <Link className="primary-link" to="/">
          + Tải tài liệu
        </Link>
      </header>

      <section className="library-toolbar" aria-label="Lọc tài liệu">
        <label className="library-search">
          <span className="sr-only">Tìm tài liệu</span>
          <input
            type="search"
            placeholder="Tìm theo tên file hoặc ID…"
            value={query}
            onChange={(event) => setQuery(event.target.value)}
          />
        </label>
        <div className="filter-tabs">
          {FILTERS.map((option) => (
            <button
              type="button"
              key={option.value}
              className={filter === option.value ? 'active' : ''}
              aria-pressed={filter === option.value}
              onClick={() => setFilter(option.value)}
            >
              {option.label}
            </button>
          ))}
        </div>
        <button
          className="secondary-button library-refresh"
          type="button"
          onClick={() => setRefreshGeneration((generation) => generation + 1)}
        >
          Làm mới
        </button>
      </section>

      {error && (
        <p className="message error" role="alert">
          {error}
        </p>
      )}
      {isLoading && <p className="library-state">Đang tải tài liệu…</p>}
      {!isLoading && items.length === 0 && (
        <section className="library-empty">
          <span aria-hidden="true">▤</span>
          <h2>Chưa có tài liệu</h2>
          <p>Tải bản scan đầu tiên để bắt đầu quy trình số hóa.</p>
          <Link className="primary-link" to="/">
            Tải tài liệu lên
          </Link>
        </section>
      )}
      {!isLoading && items.length > 0 && visibleItems.length === 0 && (
        <p className="library-state">Không có tài liệu phù hợp bộ lọc.</p>
      )}

      {visibleItems.length > 0 && (
        <section className="document-grid" aria-label="Danh sách tài liệu">
          {visibleItems.map((item) => (
            <Link
              className="document-card"
              to={`/documents/${item.document_id}`}
              key={item.document_id}
            >
              <DocumentThumbnail item={item} />
              <div className="document-card-body">
                <div className="document-card-title">
                  <h2>{item.original_filename}</h2>
                  {item.ocr_status && (
                    <span className={`status-badge status-${item.ocr_status}`}>
                      {STATUS_LABELS[item.ocr_status]}
                    </span>
                  )}
                </div>
                <p>{item.document_id}</p>
                <footer>
                  <span>{item.attempt ? `OCR lần #${item.attempt}` : 'Chưa có OCR job'}</span>
                  <time dateTime={item.updated_at || item.created_at}>
                    {new Date(item.updated_at || item.created_at).toLocaleDateString('vi-VN')}
                  </time>
                </footer>
              </div>
            </Link>
          ))}
        </section>
      )}
    </main>
  )
}
