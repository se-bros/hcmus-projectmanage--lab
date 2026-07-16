import { act, fireEvent, render, screen } from '@testing-library/react'
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest'
import { OcrStatusPanel } from './OcrStatusPanel'

const fetchMock = vi.fn<typeof fetch>()

function response(body: object, status = 200): Response {
  return new Response(JSON.stringify(body), {
    status,
    headers: { 'Content-Type': 'application/json' },
  })
}

describe('OcrStatusPanel', () => {
  beforeEach(() => {
    vi.useFakeTimers()
    vi.stubGlobal('fetch', fetchMock)
    fetchMock.mockReset()
  })

  afterEach(() => {
    vi.useRealTimers()
    vi.unstubAllGlobals()
  })

  it('polls active jobs every two seconds and stops when completed', async () => {
    fetchMock
      .mockResolvedValueOnce(
        response({ job_id: 'job-1', attempt: 1, status: 'pending', error_message: null }),
      )
      .mockResolvedValueOnce(
        response({ job_id: 'job-1', attempt: 1, status: 'processing', error_message: null }),
      )
      .mockResolvedValueOnce(
        response({ job_id: 'job-1', attempt: 1, status: 'completed', error_message: null }),
      )

    render(<OcrStatusPanel documentId="doc-1" />)
    await act(async () => Promise.resolve())
    expect(screen.getByText('Đang chờ')).toBeInTheDocument()

    await act(async () => {
      vi.advanceTimersByTime(2000)
      await Promise.resolve()
    })
    expect(screen.getByText('Đang nhận dạng')).toBeInTheDocument()
    await act(async () => {
      vi.advanceTimersByTime(2000)
      await Promise.resolve()
    })
    expect(screen.getByText('Hoàn tất')).toBeInTheDocument()
    await act(async () => vi.advanceTimersByTime(4000))

    expect(fetchMock).toHaveBeenCalledTimes(3)
  })

  it('shows the worker error and retries with a new job', async () => {
    fetchMock
      .mockResolvedValueOnce(
        response({
          job_id: 'job-1',
          attempt: 1,
          status: 'failed',
          error_message: 'Tesseract timed out',
        }),
      )
      .mockResolvedValueOnce(
        response({ job_id: 'job-2', attempt: 2, status: 'pending', error_message: null }, 202),
      )
      .mockResolvedValueOnce(
        response({ job_id: 'job-2', attempt: 2, status: 'processing', error_message: null }),
      )

    render(<OcrStatusPanel documentId="doc-1" />)
    await act(async () => Promise.resolve())
    expect(screen.getByText('Tesseract timed out')).toBeInTheDocument()

    await act(async () => {
      fireEvent.click(screen.getByRole('button', { name: 'Thử lại OCR' }))
      await Promise.resolve()
    })
    expect(screen.getByText('Lần xử lý #2')).toBeInTheDocument()
    expect(fetchMock).toHaveBeenNthCalledWith(
      2,
      '/api/documents/doc-1/ocr',
      expect.objectContaining({ method: 'POST' }),
    )
    expect(screen.getByText('Đang nhận dạng')).toBeInTheDocument()
  })
})
