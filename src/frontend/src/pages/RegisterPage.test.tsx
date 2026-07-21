import { cleanup, fireEvent, render, screen, waitFor } from '@testing-library/react'
import { MemoryRouter } from 'react-router'
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest'
import { RegisterPage } from './RegisterPage'
import { AuthProvider, useAuth } from '../context/AuthContext'

const fetchMock = vi.fn<typeof fetch>()

function response(body: object, status = 200): Response {
  return new Response(JSON.stringify(body), {
    status,
    headers: { 'Content-Type': 'application/json' },
  })
}

function TokenProbe() {
  const { token } = useAuth()
  return <span data-testid="token">{token ?? 'none'}</span>
}

describe('RegisterPage', () => {
  beforeEach(() => {
    vi.stubGlobal('fetch', fetchMock)
    fetchMock.mockReset()
  })

  afterEach(() => {
    cleanup()
    vi.restoreAllMocks()
    vi.unstubAllGlobals()
    window.localStorage.clear()
  })

  it('registers with matching passwords and stores the token', async () => {
    fetchMock.mockResolvedValueOnce(
      response({ access_token: 'new-token', token_type: 'bearer', role: 'reader' }, 201),
    )

    render(
      <AuthProvider>
        <MemoryRouter>
          <RegisterPage />
          <TokenProbe />
        </MemoryRouter>
      </AuthProvider>,
    )

    fireEvent.change(screen.getByLabelText('Email'), {
      target: { value: 'student@hcmus.edu.vn' },
    })
    fireEvent.change(screen.getByLabelText('Mật khẩu'), {
      target: { value: 'supersecret' },
    })
    fireEvent.change(screen.getByLabelText('Xác nhận mật khẩu'), {
      target: { value: 'supersecret' },
    })
    fireEvent.click(screen.getByRole('button', { name: 'Đăng ký' }))

    await waitFor(() => expect(screen.getByTestId('token').textContent).toBe('new-token'))
    expect(fetchMock).toHaveBeenCalledWith(
      '/api/auth/register',
      expect.objectContaining({
        method: 'POST',
        body: JSON.stringify({ email: 'student@hcmus.edu.vn', password: 'supersecret' }),
      }),
    )
  })

  it('shows an error and does not call the API when passwords do not match', () => {
    render(
      <AuthProvider>
        <MemoryRouter>
          <RegisterPage />
        </MemoryRouter>
      </AuthProvider>,
    )

    fireEvent.change(screen.getByLabelText('Email'), {
      target: { value: 'student@hcmus.edu.vn' },
    })
    fireEvent.change(screen.getByLabelText('Mật khẩu'), {
      target: { value: 'supersecret' },
    })
    fireEvent.change(screen.getByLabelText('Xác nhận mật khẩu'), {
      target: { value: 'different' },
    })
    fireEvent.click(screen.getByRole('button', { name: 'Đăng ký' }))

    expect(screen.getByRole('alert')).toHaveTextContent('Mật khẩu xác nhận không khớp.')
    expect(fetchMock).not.toHaveBeenCalled()
  })

  it('shows the server error when registration fails', async () => {
    fetchMock.mockResolvedValueOnce(
      response({ detail: 'An account with this email already exists.' }, 409),
    )

    render(
      <AuthProvider>
        <MemoryRouter>
          <RegisterPage />
        </MemoryRouter>
      </AuthProvider>,
    )

    fireEvent.change(screen.getByLabelText('Email'), {
      target: { value: 'student@hcmus.edu.vn' },
    })
    fireEvent.change(screen.getByLabelText('Mật khẩu'), {
      target: { value: 'supersecret' },
    })
    fireEvent.change(screen.getByLabelText('Xác nhận mật khẩu'), {
      target: { value: 'supersecret' },
    })
    fireEvent.click(screen.getByRole('button', { name: 'Đăng ký' }))

    expect(await screen.findByRole('alert')).toHaveTextContent(
      'An account with this email already exists.',
    )
  })

  it('links back to the login page', () => {
    render(
      <AuthProvider>
        <MemoryRouter>
          <RegisterPage />
        </MemoryRouter>
      </AuthProvider>,
    )
    expect(screen.getByRole('link', { name: 'Đăng nhập' })).toHaveAttribute('href', '/login')
  })
})
