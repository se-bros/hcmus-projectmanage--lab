import { render, screen, waitFor } from '@testing-library/react'
import { MemoryRouter, Route, Routes } from 'react-router'
import { beforeEach, describe, expect, it, vi } from 'vitest'
import ReaderPage from './ReaderPage'
import type { Highlight } from '../services/api'

const annotationsAdd = vi.fn()
const display = vi.fn().mockResolvedValue(undefined)

vi.mock('epubjs', () => ({
  default: () => ({
    renderTo: () => ({
      themes: { register: vi.fn(), select: vi.fn(), fontSize: vi.fn() },
      on: vi.fn(),
      annotations: { add: annotationsAdd, remove: vi.fn() },
      display,
      destroy: vi.fn(),
      prev: vi.fn(),
      next: vi.fn(),
    }),
  }),
}))

vi.mock('../services/api', async () => {
  const actual = await vi.importActual<typeof import('../services/api')>('../services/api')
  return {
    ...actual,
    getReaderContent: vi.fn().mockResolvedValue({
      document_id: 'doc-1',
      title: 'A Book',
      author: 'An Author',
      epub_url: 'https://minio.local/signed/book.epub',
      expires_in: 900,
    }),
    getBookmark: vi.fn().mockRejectedValue(new Error('no bookmark')),
    saveBookmark: vi.fn().mockResolvedValue(undefined),
    getHighlights: vi.fn(),
    createHighlight: vi.fn(),
  }
})

const api = await import('../services/api')

function highlight(id: string, text: string): Highlight {
  return {
    id,
    document_id: 'doc-1',
    cfi_range: `epubcfi(/6/14!/4/2,/1:0,/1:${text.length})`,
    selected_text: text,
    note: null,
    created_at: '2026-08-12T09:00:00Z',
    updated_at: '2026-08-12T09:00:00Z',
  }
}

function renderReader() {
  return render(
    <MemoryRouter initialEntries={['/reader/doc-1']}>
      <Routes>
        <Route path="/reader/:documentId" element={<ReaderPage />} />
      </Routes>
    </MemoryRouter>,
  )
}

describe('ReaderPage highlights', () => {
  beforeEach(() => {
    annotationsAdd.mockReset()
    vi.mocked(api.getHighlights).mockReset()
  })

  it('paints every stored highlight when the book opens', async () => {
    vi.mocked(api.getHighlights).mockResolvedValue([
      highlight('a', 'đoạn một'),
      highlight('b', 'đoạn hai'),
    ])

    renderReader()

    await waitFor(() => expect(annotationsAdd).toHaveBeenCalledTimes(2))
    expect(await screen.findByText('Đánh dấu (2)')).toBeInTheDocument()
  })

  it('moves highlights that no longer resolve into the separate group (FR-011)', async () => {
    vi.mocked(api.getHighlights).mockResolvedValue([
      highlight('a', 'còn dựng được'),
      highlight('b', 'vị trí đã hỏng'),
    ])
    // epub.js ném lỗi khi CFI không trỏ vào spine item nào của bản EPUB hiện tại.
    annotationsAdd
      .mockImplementationOnce(() => undefined)
      .mockImplementationOnce(() => {
        throw new Error('cannot resolve cfi')
      })

    renderReader()

    expect(await screen.findByText('Đánh dấu (1)')).toBeInTheDocument()
    expect(screen.getByText('Đánh dấu không còn định vị được (1)')).toBeInTheDocument()
    expect(screen.getByText('vị trí đã hỏng')).toBeInTheDocument()
  })

  it('still renders the book when highlights cannot be loaded', async () => {
    vi.mocked(api.getHighlights).mockRejectedValue(new Error('401'))

    renderReader()

    await waitFor(() => expect(display).toHaveBeenCalled())
    expect(screen.getByText('Chưa có đánh dấu nào.')).toBeInTheDocument()
  })
})
