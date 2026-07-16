import { act, fireEvent, render, screen } from '@testing-library/react'
import { MemoryRouter, Route, Routes } from 'react-router'
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest'
import { DocumentViewerPage } from './DocumentViewerPage'

const fetchMock = vi.fn<typeof fetch>()

function response(body: object, status = 200): Response {
  return new Response(JSON.stringify(body), {
    status,
    headers: { 'Content-Type': 'application/json' },
  })
}

describe('DocumentViewerPage', () => {
  beforeEach(() => {
    vi.stubGlobal('fetch', fetchMock)
    fetchMock.mockReset()
  })

  afterEach(() => vi.unstubAllGlobals())

  it('loads a dynamic document route and switches scan/text pages together', async () => {
    fetchMock
      .mockResolvedValueOnce(
        response({
          id: 'doc-1',
          original_filename: 'two-page.pdf',
          content_type: 'application/pdf',
          status: 'ocr_completed',
          title: 'OCR Sample',
          author: 'HCMUS LDMS',
          epub_object_key: null,
          created_at: '2026-07-16T08:00:00Z',
        }),
      )
      .mockResolvedValueOnce(
        response([
          { page_number: 1, text_content: 'First processed page', has_image: true },
          { page_number: 2, text_content: 'Second processed page', has_image: true },
        ]),
      )
      .mockResolvedValueOnce(
        response({
          job_id: 'job-1',
          attempt: 1,
          status: 'completed',
          error_message: null,
        }),
      )

    render(
      <MemoryRouter initialEntries={['/documents/doc-1']}>
        <Routes>
          <Route path="/documents/:documentId" element={<DocumentViewerPage />} />
        </Routes>
      </MemoryRouter>,
    )
    await act(async () => Promise.resolve())

    expect(screen.getByRole('heading', { name: 'OCR Sample' })).toBeInTheDocument()
    expect(screen.getByText('First processed page')).toBeInTheDocument()
    expect(screen.getByAltText('Ảnh scan trang 1')).toHaveAttribute(
      'src',
      '/api/documents/doc-1/pages/1/image',
    )
    expect(screen.getByRole('link', { name: 'Mở file gốc ↗' })).toHaveAttribute(
      'href',
      '/api/documents/doc-1/source',
    )

    fireEvent.click(screen.getByRole('button', { name: '2' }))
    expect(screen.getByText('Second processed page')).toBeInTheDocument()
    expect(screen.getByAltText('Ảnh scan trang 2')).toHaveAttribute(
      'src',
      '/api/documents/doc-1/pages/2/image',
    )
  })
})
