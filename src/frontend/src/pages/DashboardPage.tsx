import { useEffect, useState } from 'react'
import { getOcrJobs, retryOcr } from '../services/api'
import type { OcrDashboardItem, OcrStatus } from '../services/api'

const STATUS_LABELS: Record<OcrStatus, string> = {
  pending: 'Đang chờ',
  processing: 'Đang nhận dạng',
  completed: 'Hoàn tất',
  failed: 'Thất bại',
}

const SUMMARY_STATUSES: OcrStatus[] = ['pending', 'processing', 'completed', 'failed']

export function DashboardPage() {
  const [items, setItems] = useState<OcrDashboardItem[]>([])
  const [error, setError] = useState('')
  const [isLoading, setIsLoading] = useState(true)
  const [lastUpdated, setLastUpdated] = useState<Date | null>(null)
  const [pollGeneration, setPollGeneration] = useState(0)
  const [retryingDocumentId, setRetryingDocumentId] = useState<string | null>(null)

  useEffect(() => {
    let cancelled = false
    let timeout: ReturnType<typeof setTimeout> | undefined

    async function refresh() {
      try {
        const nextItems = await getOcrJobs()
        if (cancelled) return
        setItems(nextItems)
        setError('')
        setLastUpdated(new Date())
      } catch (refreshError) {
        if (cancelled) return
        setError(
          refreshError instanceof Error ? refreshError.message : 'Không thể tải dashboard OCR.',
        )
      } finally {
        if (!cancelled) {
          setIsLoading(false)
          timeout = setTimeout(refresh, 2000)
        }
      }
    }

    void refresh()
    return () => {
      cancelled = true
      if (timeout) clearTimeout(timeout)
    }
  }, [pollGeneration])

  async function handleRetry(documentId: string) {
    setRetryingDocumentId(documentId)
    setError('')
    try {
      const job = await retryOcr(documentId)
      setItems((currentItems) =>
        currentItems.map((item) =>
          item.document_id === documentId
            ? {
                ...item,
                job_id: job.job_id,
                attempt: job.attempt,
                ocr_status: job.status,
                error_message: null,
              }
            : item,
        ),
      )
      setPollGeneration((generation) => generation + 1)
    } catch (retryError) {
      setError(retryError instanceof Error ? retryError.message : 'Không thể chạy lại OCR.')
    } finally {
      setRetryingDocumentId(null)
    }
  }

  const totals = Object.fromEntries(
    SUMMARY_STATUSES.map((status) => [
      status,
      items.filter((item) => item.ocr_status === status).length,
    ]),
  ) as Record<OcrStatus, number>

  return (
    <main className="page-shell dashboard-page">
      <header className="dashboard-heading">
        <div>
          <p className="eyebrow">Operations overview</p>
          <h1>Dashboard OCR</h1>
          <p className="intro">Theo dõi job mới nhất của từng tài liệu, tự cập nhật mỗi 2 giây.</p>
        </div>
        <div className="live-indicator">
          <span aria-hidden="true" />
          Live
        </div>
      </header>

      <section className="summary-grid" aria-label="Tổng quan trạng thái OCR">
        {SUMMARY_STATUSES.map((status) => (
          <article className={`summary-card summary-${status}`} key={status}>
            <span>{STATUS_LABELS[status]}</span>
            <strong>{totals[status]}</strong>
          </article>
        ))}
      </section>

      <section className="jobs-card" aria-labelledby="jobs-title">
        <div className="jobs-card-heading">
          <div>
            <h2 id="jobs-title">Tiến trình tài liệu</h2>
            <p>
              {lastUpdated
                ? `Cập nhật lúc ${lastUpdated.toLocaleTimeString('vi-VN')}`
                : 'Đang kết nối…'}
            </p>
          </div>
          <button
            className="secondary-button"
            type="button"
            onClick={() => setPollGeneration((generation) => generation + 1)}
          >
            Làm mới
          </button>
        </div>

        {error && (
          <p className="message error" role="alert">
            {error}
          </p>
        )}
        {isLoading && <p className="dashboard-state">Đang tải danh sách OCR…</p>}
        {!isLoading && items.length === 0 && (
          <p className="dashboard-state">Chưa có tài liệu nào được tải lên.</p>
        )}

        {items.length > 0 && (
          <div className="jobs-table-scroll">
            <table className="jobs-table">
              <thead>
                <tr>
                  <th>Tài liệu</th>
                  <th>Trạng thái</th>
                  <th>Lần chạy</th>
                  <th>Cập nhật</th>
                  <th>Lỗi / thao tác</th>
                </tr>
              </thead>
              <tbody>
                {items.map((item) => (
                  <tr key={item.document_id}>
                    <td>
                      <strong>{item.original_filename}</strong>
                      <small>{item.document_id}</small>
                    </td>
                    <td>
                      {item.ocr_status ? (
                        <span className={`status-badge status-${item.ocr_status}`}>
                          {item.ocr_status === 'processing' && (
                            <span className="status-pulse" aria-hidden="true" />
                          )}
                          {STATUS_LABELS[item.ocr_status]}
                        </span>
                      ) : (
                        <span className="muted-message">Chưa có job</span>
                      )}
                    </td>
                    <td>{item.attempt ? `#${item.attempt}` : '—'}</td>
                    <td>
                      {item.updated_at
                        ? new Date(item.updated_at).toLocaleString('vi-VN')
                        : new Date(item.created_at).toLocaleString('vi-VN')}
                    </td>
                    <td className="job-action-cell">
                      {item.ocr_status === 'failed' ? (
                        <>
                          <span className="job-error" title={item.error_message || undefined}>
                            {item.error_message || 'Không có thông báo lỗi'}
                          </span>
                          <button
                            type="button"
                            onClick={() => handleRetry(item.document_id)}
                            disabled={retryingDocumentId === item.document_id}
                          >
                            {retryingDocumentId === item.document_id ? 'Đang thử lại…' : 'Thử lại'}
                          </button>
                        </>
                      ) : (
                        <span className="muted-message">—</span>
                      )}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </section>
    </main>
  )
}
