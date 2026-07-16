import { act, fireEvent, render, screen, within } from '@testing-library/react'
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest'
import { DashboardPage } from './DashboardPage'

const fetchMock = vi.fn<typeof fetch>()

function response(body: object, status = 200): Response {
  return new Response(JSON.stringify(body), {
    status,
    headers: { 'Content-Type': 'application/json' },
  })
}

const failedItem = {
  document_id: 'doc-failed',
  original_filename: 'failed-book.pdf',
  document_status: 'ocr_failed',
  job_id: 'job-1',
  attempt: 1,
  ocr_status: 'failed',
  error_message: 'Tesseract timed out',
  created_at: '2026-07-16T08:00:00Z',
  updated_at: '2026-07-16T08:01:00Z',
}

describe('DashboardPage', () => {
  beforeEach(() => {
    vi.useFakeTimers()
    vi.setSystemTime(new Date('2026-07-16T08:02:00Z'))
    vi.stubGlobal('fetch', fetchMock)
    fetchMock.mockReset()
  })

  afterEach(() => {
    vi.useRealTimers()
    vi.unstubAllGlobals()
  })

  it('summarizes jobs, polls, and retries a failed document', async () => {
    fetchMock
      .mockResolvedValueOnce(response([failedItem]))
      .mockResolvedValueOnce(
        response({ job_id: 'job-2', attempt: 2, status: 'pending', error_message: null }, 202),
      )
      .mockResolvedValueOnce(
        response([{ ...failedItem, job_id: 'job-2', attempt: 2, ocr_status: 'processing' }]),
      )
      .mockResolvedValueOnce(
        response([{ ...failedItem, job_id: 'job-2', attempt: 2, ocr_status: 'completed' }]),
      )

    render(<DashboardPage />)
    await act(async () => Promise.resolve())

    expect(screen.getByText('failed-book.pdf')).toBeInTheDocument()
    expect(screen.getByText('Tesseract timed out')).toBeInTheDocument()
    expect(within(document.querySelector('.summary-failed')!).getByText('1')).toBeInTheDocument()

    await act(async () => {
      fireEvent.click(screen.getByRole('button', { name: 'Thử lại' }))
      await Promise.resolve()
    })
    expect(fetchMock).toHaveBeenNthCalledWith(2, '/api/documents/doc-failed/ocr', {
      method: 'POST',
    })
    expect(screen.getByText('#2')).toBeInTheDocument()
    const jobRow = screen.getByText('failed-book.pdf').closest('tr')!
    expect(within(jobRow).getByText('Đang nhận dạng')).toBeInTheDocument()

    await act(async () => {
      vi.advanceTimersByTime(2000)
      await Promise.resolve()
    })
    expect(within(jobRow).getByText('Hoàn tất')).toBeInTheDocument()
    expect(fetchMock).toHaveBeenCalledTimes(4)
  })
})
