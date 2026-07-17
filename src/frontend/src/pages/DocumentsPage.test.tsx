import { act, fireEvent, render, screen } from '@testing-library/react'
import { MemoryRouter } from 'react-router'
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest'
import { DocumentsPage } from './DocumentsPage'

const fetchMock = vi.fn<typeof fetch>()

function response(body: object, status = 200): Response {
  return new Response(JSON.stringify(body), {
    status,
    headers: { 'Content-Type': 'application/json' },
  })
}

describe('DocumentsPage', () => {
  beforeEach(() => {
    vi.stubGlobal('fetch', fetchMock)
    fetchMock.mockReset()
  })

  afterEach(() => vi.unstubAllGlobals())

  it('lists scanned items and filters by OCR status and filename', async () => {
    fetchMock.mockResolvedValueOnce(
      response([
        {
          document_id: 'doc-completed',
          original_filename: 'processed-book.pdf',
          document_status: 'ocr_completed',
          job_id: 'job-1',
          attempt: 1,
          ocr_status: 'completed',
          error_message: null,
          created_at: '2026-07-16T08:00:00Z',
          updated_at: '2026-07-16T08:01:00Z',
        },
        {
          document_id: 'doc-failed',
          original_filename: 'broken-scan.png',
          document_status: 'ocr_failed',
          job_id: 'job-2',
          attempt: 2,
          ocr_status: 'failed',
          error_message: 'OCR failed',
          created_at: '2026-07-16T07:00:00Z',
          updated_at: '2026-07-16T07:01:00Z',
        },
      ]),
    )

    render(
      <MemoryRouter>
        <DocumentsPage />
      </MemoryRouter>,
    )
    await act(async () => Promise.resolve())

    expect(screen.getByText('processed-book.pdf')).toBeInTheDocument()
    expect(screen.getByText('broken-scan.png')).toBeInTheDocument()
    expect(screen.getByRole('link', { name: /processed-book.pdf/ })).toHaveAttribute(
      'href',
      '/documents/doc-completed',
    )

    fireEvent.click(screen.getByRole('button', { name: 'Lỗi' }))
    expect(screen.queryByText('processed-book.pdf')).not.toBeInTheDocument()
    expect(screen.getByText('broken-scan.png')).toBeInTheDocument()

    fireEvent.click(screen.getByRole('button', { name: 'Tất cả' }))
    fireEvent.change(screen.getByPlaceholderText('Tìm theo tên file hoặc ID…'), {
      target: { value: 'processed' },
    })
    expect(screen.getByText('processed-book.pdf')).toBeInTheDocument()
    expect(screen.queryByText('broken-scan.png')).not.toBeInTheDocument()
  })
})
