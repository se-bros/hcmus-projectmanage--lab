import { useEffect, useRef, useState } from 'react'
import { getOcrStatus, retryOcr } from '../services/api'
import type { OcrJob } from '../services/api'

type OcrStatusPanelProps = {
  documentId: string
  pollIntervalMs?: number
}

const STATUS_LABELS: Record<OcrJob['status'], string> = {
  pending: 'Đang chờ',
  processing: 'Đang nhận dạng',
  completed: 'Hoàn tất',
  failed: 'Thất bại',
}

export function OcrStatusPanel({ documentId, pollIntervalMs = 2000 }: OcrStatusPanelProps) {
  const [job, setJob] = useState<OcrJob | null>(null)
  const [error, setError] = useState('')
  const [isRetrying, setIsRetrying] = useState(false)
  const [pollGeneration, setPollGeneration] = useState(0)
  const timeoutRef = useRef<ReturnType<typeof setTimeout> | null>(null)

  useEffect(() => {
    let cancelled = false

    async function poll() {
      try {
        const nextJob = await getOcrStatus(documentId)
        if (cancelled) return
        setJob(nextJob)
        setError('')
        if (nextJob.status === 'pending' || nextJob.status === 'processing') {
          timeoutRef.current = setTimeout(poll, pollIntervalMs)
        }
      } catch (pollError) {
        if (cancelled) return
        setError(pollError instanceof Error ? pollError.message : 'Không thể đọc trạng thái OCR.')
      }
    }

    void poll()
    return () => {
      cancelled = true
      if (timeoutRef.current !== null) clearTimeout(timeoutRef.current)
    }
  }, [documentId, pollGeneration, pollIntervalMs])

  async function handleRetry() {
    setIsRetrying(true)
    setError('')
    try {
      const nextJob = await retryOcr(documentId)
      setJob({ ...nextJob, error_message: null })
      setPollGeneration((generation) => generation + 1)
    } catch (retryError) {
      setError(retryError instanceof Error ? retryError.message : 'Không thể chạy lại OCR.')
    } finally {
      setIsRetrying(false)
    }
  }

  return (
    <section className="ocr-panel" aria-labelledby="ocr-status-title" aria-live="polite">
      <div className="ocr-panel-heading">
        <div>
          <p className="section-kicker">OCR tự động</p>
          <h3 id="ocr-status-title">Trạng thái nhận dạng</h3>
        </div>
        {job && (
          <span className={`status-badge status-${job.status}`}>{STATUS_LABELS[job.status]}</span>
        )}
      </div>

      {!job && !error && <p className="muted-message">Đang đọc trạng thái OCR…</p>}
      {job && <p className="job-attempt">Lần xử lý #{job.attempt}</p>}
      {job?.status === 'pending' && <p>Tài liệu đang chờ worker OCR.</p>}
      {job?.status === 'processing' && <p>Hệ thống đang nhận dạng từng trang.</p>}
      {job?.status === 'completed' && <p>Văn bản và ảnh preview đã sẵn sàng.</p>}
      {job?.status === 'failed' && (
        <div className="ocr-failure">
          <p role="alert">{job.error_message || 'OCR thất bại nhưng không có thông báo lỗi.'}</p>
          <button type="button" onClick={handleRetry} disabled={isRetrying}>
            {isRetrying ? 'Đang chạy lại…' : 'Thử lại OCR'}
          </button>
        </div>
      )}
      {error && (
        <p className="inline-error" role="alert">
          {error}
        </p>
      )}
    </section>
  )
}
