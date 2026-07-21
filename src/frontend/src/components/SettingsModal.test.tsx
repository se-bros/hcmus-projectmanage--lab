import { cleanup, fireEvent, render, screen, waitFor } from '@testing-library/react'
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest'
import { SettingsModal } from './SettingsModal'

const fetchMock = vi.fn<typeof fetch>()

function response(body: unknown, status = 200): Response {
  return new Response(JSON.stringify(body), {
    status,
    headers: { 'Content-Type': 'application/json' },
  })
}

const localProfile = {
  id: 'user-1',
  email: 'reader@hcmus.edu.vn',
  username: 'Old Name',
  role: 'reader' as const,
  auth_provider: 'local',
  has_password: true,
}

describe('SettingsModal', () => {
  beforeEach(() => {
    vi.stubGlobal('fetch', fetchMock)
    fetchMock.mockReset()
  })

  afterEach(() => {
    cleanup()
    vi.restoreAllMocks()
    vi.unstubAllGlobals()
  })

  it('loads profile and shows the Hồ sơ tab by default', async () => {
    fetchMock.mockResolvedValueOnce(response(localProfile)).mockResolvedValueOnce(response(null))

    render(<SettingsModal onClose={vi.fn()} />)

    expect(await screen.findByDisplayValue('Old Name')).toBeInTheDocument()
    expect(screen.getByText('reader@hcmus.edu.vn')).toBeInTheDocument()
    expect(screen.getByLabelText('Mật khẩu hiện tại')).toBeInTheDocument()
  })

  it('saves a new username', async () => {
    fetchMock
      .mockResolvedValueOnce(response(localProfile))
      .mockResolvedValueOnce(response(null))
      .mockResolvedValueOnce(response({ ...localProfile, username: 'New Name' }))

    render(<SettingsModal onClose={vi.fn()} />)
    await screen.findByDisplayValue('Old Name')

    fireEvent.change(screen.getByLabelText('Username'), { target: { value: 'New Name' } })
    fireEvent.click(screen.getByRole('button', { name: 'Lưu' }))

    expect(await screen.findByText('Đã lưu.')).toBeInTheDocument()
    expect(fetchMock).toHaveBeenLastCalledWith(
      '/api/auth/me',
      expect.objectContaining({
        method: 'PATCH',
        body: JSON.stringify({ username: 'New Name' }),
      }),
    )
  })

  it('does not show a current-password field for a Google-only account', async () => {
    fetchMock
      .mockResolvedValueOnce(
        response({ ...localProfile, auth_provider: 'google', has_password: false }),
      )
      .mockResolvedValueOnce(response(null))

    render(<SettingsModal onClose={vi.fn()} />)
    await screen.findByDisplayValue('Old Name')

    expect(screen.queryByLabelText('Mật khẩu hiện tại')).not.toBeInTheDocument()
    expect(screen.getByLabelText('Mật khẩu mới')).toBeInTheDocument()
  })

  it('shows a mismatch error and does not call the API when new passwords differ', async () => {
    fetchMock.mockResolvedValueOnce(response(localProfile)).mockResolvedValueOnce(response(null))

    render(<SettingsModal onClose={vi.fn()} />)
    await screen.findByDisplayValue('Old Name')
    const callsBefore = fetchMock.mock.calls.length

    fireEvent.change(screen.getByLabelText('Mật khẩu hiện tại'), {
      target: { value: 'supersecret' },
    })
    fireEvent.change(screen.getByLabelText('Mật khẩu mới'), { target: { value: 'newpassword1' } })
    fireEvent.change(screen.getByLabelText('Xác nhận mật khẩu mới'), {
      target: { value: 'different1' },
    })
    fireEvent.click(screen.getByRole('button', { name: 'Đổi mật khẩu' }))

    expect(await screen.findByText('Mật khẩu xác nhận không khớp.')).toBeInTheDocument()
    expect(fetchMock.mock.calls.length).toBe(callsBefore)
  })

  it('shows the "request to become editor" button for a reader with no pending request', async () => {
    fetchMock.mockResolvedValueOnce(response(localProfile)).mockResolvedValueOnce(response(null))

    render(<SettingsModal onClose={vi.fn()} />)
    await screen.findByDisplayValue('Old Name')

    fireEvent.click(screen.getByRole('button', { name: 'Yêu cầu' }))
    expect(
      await screen.findByRole('button', { name: 'Yêu cầu trở thành Editor' }),
    ).toBeInTheDocument()
  })

  it('shows a pending status instead of the button when a request is already pending', async () => {
    fetchMock.mockResolvedValueOnce(response(localProfile)).mockResolvedValueOnce(
      response({
        id: 'req-1',
        user_id: 'user-1',
        user_email: 'reader@hcmus.edu.vn',
        user_username: 'Old Name',
        requested_role: 'editor',
        status: 'pending',
        created_at: '2026-07-21T00:00:00Z',
        decided_at: null,
      }),
    )

    render(<SettingsModal onClose={vi.fn()} />)
    await screen.findByDisplayValue('Old Name')

    fireEvent.click(screen.getByRole('button', { name: 'Yêu cầu' }))
    expect(await screen.findByText('Yêu cầu đang chờ duyệt.')).toBeInTheDocument()
    expect(
      screen.queryByRole('button', { name: 'Yêu cầu trở thành Editor' }),
    ).not.toBeInTheDocument()
  })

  it('submits a new request and shows the pending state', async () => {
    fetchMock
      .mockResolvedValueOnce(response(localProfile))
      .mockResolvedValueOnce(response(null))
      .mockResolvedValueOnce(
        response(
          {
            id: 'req-2',
            user_id: 'user-1',
            user_email: 'reader@hcmus.edu.vn',
            user_username: 'Old Name',
            requested_role: 'editor',
            status: 'pending',
            created_at: '2026-07-21T00:00:00Z',
            decided_at: null,
          },
          201,
        ),
      )

    render(<SettingsModal onClose={vi.fn()} />)
    await screen.findByDisplayValue('Old Name')
    fireEvent.click(screen.getByRole('button', { name: 'Yêu cầu' }))

    fireEvent.click(await screen.findByRole('button', { name: 'Yêu cầu trở thành Editor' }))

    expect(await screen.findByText('Yêu cầu đang chờ duyệt.')).toBeInTheDocument()
  })

  it('shows a static message for an editor instead of the request button', async () => {
    fetchMock
      .mockResolvedValueOnce(response({ ...localProfile, role: 'editor' }))
      .mockResolvedValueOnce(response(null))

    render(<SettingsModal onClose={vi.fn()} />)
    await screen.findByDisplayValue('Old Name')

    fireEvent.click(screen.getByRole('button', { name: 'Yêu cầu' }))
    expect(await screen.findByText(/Bạn hiện có quyền/)).toBeInTheDocument()
  })

  it('closes when the backdrop is clicked but not when the panel is clicked', async () => {
    fetchMock.mockResolvedValueOnce(response(localProfile)).mockResolvedValueOnce(response(null))
    const onClose = vi.fn()

    render(<SettingsModal onClose={onClose} />)
    await screen.findByDisplayValue('Old Name')

    fireEvent.click(screen.getByRole('dialog'))
    expect(onClose).not.toHaveBeenCalled()

    fireEvent.click(screen.getByLabelText('Đóng'))
    expect(onClose).toHaveBeenCalledOnce()
  })

  it('closes on Escape', async () => {
    fetchMock.mockResolvedValueOnce(response(localProfile)).mockResolvedValueOnce(response(null))
    const onClose = vi.fn()

    render(<SettingsModal onClose={onClose} />)
    await screen.findByDisplayValue('Old Name')

    fireEvent.keyDown(document, { key: 'Escape' })
    await waitFor(() => expect(onClose).toHaveBeenCalledOnce())
  })
})
