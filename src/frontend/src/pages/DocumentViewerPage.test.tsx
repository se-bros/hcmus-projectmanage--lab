import { act, cleanup, fireEvent, render, screen, waitFor } from '@testing-library/react'
import { MemoryRouter, Route, Routes } from 'react-router'
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest'
import { DocumentViewerPage } from './DocumentViewerPage'
import { AuthProvider } from '../context/AuthContext'

const fetchMock = vi.fn<typeof fetch>()

function response(body: object, status = 200): Response {
  return new Response(JSON.stringify(body), {
    status,
    headers: { 'Content-Type': 'application/json' },
  })
}

function fakeToken(payload: Record<string, unknown>): string {
  const base64url = (value: string) =>
    btoa(value).replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '')
  const header = base64url(JSON.stringify({ alg: 'HS256', typ: 'JWT' }))
  const body = base64url(JSON.stringify(payload))
  return `${header}.${body}.signature`
}

describe('DocumentViewerPage', () => {
  beforeEach(() => {
    vi.stubGlobal('fetch', fetchMock)
    fetchMock.mockReset()
    fetchMock.mockResolvedValue(response([]))
    window.localStorage.setItem(
      'ldms_token',
      fakeToken({ sub: 'admin-user', role: 'admin', email: 'admin@hcmus.edu.vn' }),
    )
  })

  afterEach(() => {
    cleanup()
    vi.restoreAllMocks()
    vi.unstubAllGlobals()
    window.localStorage.clear()
  })

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
      <AuthProvider>
        <MemoryRouter initialEntries={['/documents/doc-1']}>
          <Routes>
            <Route path="/documents/:documentId" element={<DocumentViewerPage />} />
          </Routes>
        </MemoryRouter>
      </AuthProvider>,
    )
    await act(async () => Promise.resolve())

    expect(screen.getByRole('heading', { name: 'OCR Sample' })).toBeInTheDocument()
    expect(screen.getByLabelText('Nội dung OCR trang 1')).toHaveValue('First processed page')
    expect(screen.getByAltText('Ảnh scan trang 1')).toHaveAttribute(
      'src',
      '/api/documents/doc-1/pages/1/image',
    )
    expect(screen.getByRole('link', { name: 'Mở file gốc ↗' })).toHaveAttribute(
      'href',
      '/api/documents/doc-1/source',
    )

    fireEvent.click(screen.getByRole('button', { name: '2' }))
    expect(screen.getByLabelText('Nội dung OCR trang 2')).toHaveValue('Second processed page')
    expect(screen.getByAltText('Ảnh scan trang 2')).toHaveAttribute(
      'src',
      '/api/documents/doc-1/pages/2/image',
    )
  })

  it('edits metadata and shows saving then saved state', async () => {
    fetchMock
      .mockResolvedValueOnce(
        response({
          id: 'doc-1',
          original_filename: 'scan.pdf',
          content_type: 'application/pdf',
          status: 'ocr_completed',
          title: 'Old title',
          author: 'Old author',
          shelf_location: null,
          category_id: null,
          epub_object_key: null,
          created_at: '2026-07-16T08:00:00Z',
        }),
      )
      .mockResolvedValueOnce(response([]))
      .mockResolvedValueOnce(
        response({ job_id: 'job-1', attempt: 1, status: 'completed', error_message: null }),
      )
      .mockResolvedValueOnce(
        response([
          {
            id: 'category-parent',
            name: 'Science',
            parent_id: null,
            created_at: '2026-07-16T08:00:00Z',
            updated_at: '2026-07-16T08:00:00Z',
            children: [
              {
                id: 'category-child',
                name: 'Physics',
                parent_id: 'category-parent',
                created_at: '2026-07-16T08:00:00Z',
                updated_at: '2026-07-16T08:00:00Z',
              },
            ],
          },
        ]),
      )

    let resolveSave!: (value: Response) => void
    fetchMock.mockImplementationOnce(
      () => new Promise<Response>((resolve) => (resolveSave = resolve)),
    )

    render(
      <AuthProvider>
        <MemoryRouter initialEntries={['/documents/doc-1']}>
          <Routes>
            <Route path="/documents/:documentId" element={<DocumentViewerPage />} />
          </Routes>
        </MemoryRouter>
      </AuthProvider>,
    )
    expect(await screen.findByDisplayValue('Old title')).toBeInTheDocument()

    fireEvent.change(screen.getByLabelText('Title'), { target: { value: ' New title ' } })
    fireEvent.change(screen.getByLabelText('Author'), { target: { value: 'New author' } })
    fireEvent.change(screen.getByLabelText('Vị trí kệ (không bắt buộc)'), {
      target: { value: 'A-12' },
    })
    fireEvent.change(screen.getByLabelText('Category (không bắt buộc)'), {
      target: { value: 'category-child' },
    })
    fireEvent.click(screen.getByRole('button', { name: 'Lưu metadata' }))
    expect(screen.getByRole('button', { name: 'Đang lưu…' })).toBeDisabled()

    resolveSave(
      response({
        id: 'doc-1',
        original_filename: 'scan.pdf',
        content_type: 'application/pdf',
        status: 'ocr_completed',
        title: 'New title',
        author: 'New author',
        shelf_location: 'A-12',
        category_id: 'category-child',
        epub_object_key: null,
        created_at: '2026-07-16T08:00:00Z',
      }),
    )
    expect(await screen.findByText('Đã lưu metadata.')).toBeInTheDocument()
    expect(screen.getByRole('heading', { name: 'New title' })).toBeInTheDocument()
    expect(fetchMock).toHaveBeenLastCalledWith(
      '/api/documents/doc-1/metadata',
      expect.objectContaining({
        method: 'PUT',
        body: JSON.stringify({
          title: ' New title ',
          author: 'New author',
          shelf_location: 'A-12',
          category_id: 'category-child',
        }),
      }),
    )
  })

  it('shows metadata API validation errors', async () => {
    fetchMock
      .mockResolvedValueOnce(
        response({
          id: 'doc-1',
          original_filename: 'scan.pdf',
          content_type: 'application/pdf',
          status: 'ocr_completed',
          title: null,
          author: null,
          shelf_location: null,
          category_id: null,
          epub_object_key: null,
          created_at: '2026-07-16T08:00:00Z',
        }),
      )
      .mockResolvedValueOnce(response([]))
      .mockResolvedValueOnce(
        response({ job_id: 'job-1', attempt: 1, status: 'completed', error_message: null }),
      )
      .mockResolvedValueOnce(response([]))
      .mockResolvedValueOnce(
        response(
          { detail: [{ loc: ['body', 'title'], msg: 'must not be empty or whitespace' }] },
          422,
        ),
      )

    render(
      <AuthProvider>
        <MemoryRouter initialEntries={['/documents/doc-1']}>
          <Routes>
            <Route path="/documents/:documentId" element={<DocumentViewerPage />} />
          </Routes>
        </MemoryRouter>
      </AuthProvider>,
    )
    await screen.findByRole('heading', { name: 'Metadata tài liệu' })
    fireEvent.click(screen.getByRole('button', { name: 'Lưu metadata' }))

    await waitFor(() =>
      expect(screen.getByRole('status')).toHaveTextContent(
        'title: must not be empty or whitespace',
      ),
    )
  })

  it('saves corrected page text, exposes saving/saved and reloads the persisted value', async () => {
    const detail = {
      id: 'doc-1',
      original_filename: 'scan.pdf',
      content_type: 'application/pdf',
      status: 'ocr_completed',
      title: 'Book',
      author: 'Author',
      shelf_location: null,
      category_id: null,
      epub_object_key: null,
      created_at: '2026-07-16T08:00:00Z',
    }
    const job = { job_id: 'job-1', attempt: 1, status: 'completed', error_message: null }
    fetchMock
      .mockResolvedValueOnce(response(detail))
      .mockResolvedValueOnce(
        response([{ page_number: 1, text_content: 'Original', has_image: true }]),
      )
      .mockResolvedValueOnce(response(job))
      .mockResolvedValueOnce(response([]))

    let resolveSave!: (value: Response) => void
    fetchMock.mockImplementationOnce(
      () => new Promise<Response>((resolve) => (resolveSave = resolve)),
    )
    const view = render(
      <AuthProvider>
        <MemoryRouter initialEntries={['/documents/doc-1']}>
          <Routes>
            <Route path="/documents/:documentId" element={<DocumentViewerPage />} />
          </Routes>
        </MemoryRouter>
      </AuthProvider>,
    )

    const editor = await screen.findByLabelText('Nội dung OCR trang 1')
    fireEvent.change(editor, { target: { value: 'Corrected text' } })
    expect(screen.getByText('Có thay đổi chưa lưu.')).toBeInTheDocument()
    fireEvent.click(screen.getByRole('button', { name: 'Lưu trang' }))
    expect(screen.getByRole('button', { name: 'Đang lưu…' })).toBeDisabled()
    resolveSave(response({ page_number: 1, text_content: 'Corrected text', has_image: true }))
    expect(await screen.findByText('Đã lưu trang.')).toBeInTheDocument()
    expect(fetchMock).toHaveBeenLastCalledWith(
      '/api/documents/doc-1/pages/1',
      expect.objectContaining({
        method: 'PUT',
        body: JSON.stringify({ text_content: 'Corrected text' }),
      }),
    )

    view.unmount()
    fetchMock.mockReset()
    fetchMock
      .mockResolvedValueOnce(response(detail))
      .mockResolvedValueOnce(
        response([{ page_number: 1, text_content: 'Corrected text', has_image: true }]),
      )
      .mockResolvedValueOnce(response(job))
      .mockResolvedValueOnce(response([]))
    render(
      <AuthProvider>
        <MemoryRouter initialEntries={['/documents/doc-1']}>
          <Routes>
            <Route path="/documents/:documentId" element={<DocumentViewerPage />} />
          </Routes>
        </MemoryRouter>
      </AuthProvider>,
    )
    await waitFor(() =>
      expect(screen.getByLabelText('Nội dung OCR trang 1')).toHaveValue('Corrected text'),
    )
  })

  it('keeps the current page when unsaved changes are rejected and shows image placeholder', async () => {
    fetchMock
      .mockResolvedValueOnce(
        response({
          id: 'doc-1',
          original_filename: 'scan.pdf',
          content_type: 'application/pdf',
          status: 'ocr_completed',
          title: 'Book',
          author: 'Author',
          shelf_location: null,
          category_id: null,
          epub_object_key: null,
          created_at: '2026-07-16T08:00:00Z',
        }),
      )
      .mockResolvedValueOnce(
        response([
          { page_number: 1, text_content: 'First', has_image: true },
          { page_number: 2, text_content: 'Second', has_image: false },
        ]),
      )
      .mockResolvedValueOnce(
        response({ job_id: 'job-1', attempt: 1, status: 'completed', error_message: null }),
      )
      .mockResolvedValueOnce(response([]))
    const confirm = vi.spyOn(window, 'confirm').mockReturnValueOnce(false).mockReturnValueOnce(true)

    render(
      <AuthProvider>
        <MemoryRouter initialEntries={['/documents/doc-1']}>
          <Routes>
            <Route path="/documents/:documentId" element={<DocumentViewerPage />} />
          </Routes>
        </MemoryRouter>
      </AuthProvider>,
    )
    fireEvent.change(await screen.findByLabelText('Nội dung OCR trang 1'), {
      target: { value: 'Unsaved' },
    })
    fireEvent.click(screen.getByRole('button', { name: '2' }))
    expect(screen.getByLabelText('Nội dung OCR trang 1')).toHaveValue('Unsaved')

    fireEvent.click(screen.getByRole('button', { name: '2' }))
    expect(screen.getByLabelText('Nội dung OCR trang 2')).toHaveValue('Second')
    expect(screen.getByText('Trang này chưa có ảnh preview.')).toBeInTheDocument()
    expect(confirm).toHaveBeenCalledTimes(2)
  })

  it('shows an observable page save error', async () => {
    fetchMock
      .mockResolvedValueOnce(
        response({
          id: 'doc-1',
          original_filename: 'scan.pdf',
          content_type: 'application/pdf',
          status: 'ocr_completed',
          title: 'Book',
          author: 'Author',
          shelf_location: null,
          category_id: null,
          epub_object_key: null,
          created_at: '2026-07-16T08:00:00Z',
        }),
      )
      .mockResolvedValueOnce(
        response([{ page_number: 1, text_content: 'Original', has_image: false }]),
      )
      .mockResolvedValueOnce(
        response({ job_id: 'job-1', attempt: 1, status: 'completed', error_message: null }),
      )
      .mockResolvedValueOnce(response([]))
      .mockResolvedValueOnce(response({ detail: 'Page update failed.' }, 500))

    render(
      <AuthProvider>
        <MemoryRouter initialEntries={['/documents/doc-1']}>
          <Routes>
            <Route path="/documents/:documentId" element={<DocumentViewerPage />} />
          </Routes>
        </MemoryRouter>
      </AuthProvider>,
    )
    fireEvent.change(await screen.findByLabelText('Nội dung OCR trang 1'), {
      target: { value: 'Changed' },
    })
    fireEvent.click(screen.getByRole('button', { name: 'Lưu trang' }))
    expect(await screen.findByText('Page update failed.')).toBeInTheDocument()
  })

  it('hides the metadata form and page-text editor for a reader, but still shows read-only content', async () => {
    window.localStorage.setItem(
      'ldms_token',
      fakeToken({ sub: 'reader-user', role: 'reader', email: 'reader@hcmus.edu.vn' }),
    )
    fetchMock
      .mockResolvedValueOnce(
        response({
          id: 'doc-1',
          original_filename: 'scan.pdf',
          content_type: 'application/pdf',
          status: 'ocr_completed',
          title: 'Book',
          author: 'Author',
          shelf_location: null,
          category_id: null,
          epub_object_key: null,
          owner_id: 'editor-owner',
          created_at: '2026-07-16T08:00:00Z',
        }),
      )
      .mockResolvedValueOnce(
        response([{ page_number: 1, text_content: 'Read-only OCR text', has_image: true }]),
      )
      .mockResolvedValueOnce(
        response({ job_id: 'job-1', attempt: 1, status: 'completed', error_message: null }),
      )
      .mockResolvedValueOnce(response([]))

    render(
      <AuthProvider>
        <MemoryRouter initialEntries={['/documents/doc-1']}>
          <Routes>
            <Route path="/documents/:documentId" element={<DocumentViewerPage />} />
          </Routes>
        </MemoryRouter>
      </AuthProvider>,
    )

    expect(await screen.findByText('Read-only OCR text')).toBeInTheDocument()
    expect(screen.queryByRole('heading', { name: 'Metadata tài liệu' })).not.toBeInTheDocument()
    expect(screen.queryByLabelText('Nội dung OCR trang 1')).not.toBeInTheDocument()
    expect(screen.queryByRole('button', { name: 'Lưu trang' })).not.toBeInTheDocument()
  })

  it('hides the metadata form and page-text editor for an editor who does not own the document', async () => {
    window.localStorage.setItem(
      'ldms_token',
      fakeToken({ sub: 'editor-user', role: 'editor', email: 'editor@hcmus.edu.vn' }),
    )
    fetchMock
      .mockResolvedValueOnce(
        response({
          id: 'doc-1',
          original_filename: 'scan.pdf',
          content_type: 'application/pdf',
          status: 'ocr_completed',
          title: 'Book',
          author: 'Author',
          shelf_location: null,
          category_id: null,
          epub_object_key: null,
          owner_id: 'someone-else',
          created_at: '2026-07-16T08:00:00Z',
        }),
      )
      .mockResolvedValueOnce(
        response([{ page_number: 1, text_content: 'Not my document', has_image: true }]),
      )
      .mockResolvedValueOnce(
        response({ job_id: 'job-1', attempt: 1, status: 'completed', error_message: null }),
      )
      .mockResolvedValueOnce(response([]))

    render(
      <AuthProvider>
        <MemoryRouter initialEntries={['/documents/doc-1']}>
          <Routes>
            <Route path="/documents/:documentId" element={<DocumentViewerPage />} />
          </Routes>
        </MemoryRouter>
      </AuthProvider>,
    )

    expect(await screen.findByText('Not my document')).toBeInTheDocument()
    expect(screen.queryByRole('heading', { name: 'Metadata tài liệu' })).not.toBeInTheDocument()
    expect(screen.queryByLabelText('Nội dung OCR trang 1')).not.toBeInTheDocument()
  })

  it('shows the metadata form and page-text editor for an editor who owns the document', async () => {
    window.localStorage.setItem(
      'ldms_token',
      fakeToken({ sub: 'editor-user', role: 'editor', email: 'editor@hcmus.edu.vn' }),
    )
    fetchMock
      .mockResolvedValueOnce(
        response({
          id: 'doc-1',
          original_filename: 'scan.pdf',
          content_type: 'application/pdf',
          status: 'ocr_completed',
          title: 'Book',
          author: 'Author',
          shelf_location: null,
          category_id: null,
          epub_object_key: null,
          owner_id: 'editor-user',
          created_at: '2026-07-16T08:00:00Z',
        }),
      )
      .mockResolvedValueOnce(
        response([{ page_number: 1, text_content: 'My document', has_image: true }]),
      )
      .mockResolvedValueOnce(
        response({ job_id: 'job-1', attempt: 1, status: 'completed', error_message: null }),
      )
      .mockResolvedValueOnce(response([]))

    render(
      <AuthProvider>
        <MemoryRouter initialEntries={['/documents/doc-1']}>
          <Routes>
            <Route path="/documents/:documentId" element={<DocumentViewerPage />} />
          </Routes>
        </MemoryRouter>
      </AuthProvider>,
    )

    expect(await screen.findByRole('heading', { name: 'Metadata tài liệu' })).toBeInTheDocument()
    expect(screen.getByLabelText('Nội dung OCR trang 1')).toHaveValue('My document')
  })
})
