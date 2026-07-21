import { cleanup, fireEvent, render, screen } from '@testing-library/react'
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest'
import { RequestsPage } from './RequestsPage'

const fetchMock = vi.fn<typeof fetch>()

function response(body: unknown, status = 200): Response {
  return new Response(JSON.stringify(body), {
    status,
    headers: { 'Content-Type': 'application/json' },
  })
}

const pendingRequest = {
  id: 'req-1',
  user_id: 'user-1',
  user_email: 'reader@hcmus.edu.vn',
  user_username: 'Reader Name',
  requested_role: 'editor',
  status: 'pending' as const,
  created_at: '2026-07-21T00:00:00Z',
  decided_at: null,
}

describe('RequestsPage', () => {
  beforeEach(() => {
    vi.stubGlobal('fetch', fetchMock)
    fetchMock.mockReset()
  })

  afterEach(() => {
    cleanup()
    vi.restoreAllMocks()
    vi.unstubAllGlobals()
  })

  it('lists requests with an Approve/Decline row for a pending one', async () => {
    fetchMock.mockResolvedValueOnce(response([pendingRequest]))

    render(<RequestsPage />)

    expect(await screen.findByText('Reader Name')).toBeInTheDocument()
    expect(screen.getByRole('button', { name: 'Duyệt' })).toBeInTheDocument()
    expect(screen.getByRole('button', { name: 'Từ chối' })).toBeInTheDocument()
  })

  it('shows an empty state when there are no requests', async () => {
    fetchMock.mockResolvedValueOnce(response([]))

    render(<RequestsPage />)

    expect(await screen.findByText('Chưa có yêu cầu nào.')).toBeInTheDocument()
  })

  it('approves a request and updates the row without an action button', async () => {
    fetchMock
      .mockResolvedValueOnce(response([pendingRequest]))
      .mockResolvedValueOnce(response({ ...pendingRequest, status: 'approved' }))

    render(<RequestsPage />)
    fireEvent.click(await screen.findByRole('button', { name: 'Duyệt' }))

    expect(await screen.findByText('Đã duyệt')).toBeInTheDocument()
    expect(screen.queryByRole('button', { name: 'Duyệt' })).not.toBeInTheDocument()
    expect(fetchMock).toHaveBeenLastCalledWith(
      '/api/role-requests/req-1/approve',
      expect.objectContaining({ method: 'POST' }),
    )
  })

  it('declines a request', async () => {
    fetchMock
      .mockResolvedValueOnce(response([pendingRequest]))
      .mockResolvedValueOnce(response({ ...pendingRequest, status: 'rejected' }))

    render(<RequestsPage />)
    fireEvent.click(await screen.findByRole('button', { name: 'Từ chối' }))

    expect(await screen.findByText('Đã từ chối')).toBeInTheDocument()
    expect(fetchMock).toHaveBeenLastCalledWith(
      '/api/role-requests/req-1/decline',
      expect.objectContaining({ method: 'POST' }),
    )
  })

  it('shows an error message when the list fails to load', async () => {
    fetchMock.mockResolvedValueOnce(response({ detail: 'Forbidden' }, 403))

    render(<RequestsPage />)

    expect(await screen.findByRole('alert')).toHaveTextContent('Forbidden')
  })
})
