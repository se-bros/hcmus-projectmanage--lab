import { cleanup, fireEvent, render, screen, waitFor } from '@testing-library/react'
import { MemoryRouter } from 'react-router'
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest'
import { LoginPage } from './LoginPage'
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

describe('LoginPage', () => {
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

  it('links to the backend Google login redirect', () => {
    render(
      <AuthProvider>
        <MemoryRouter>
          <LoginPage />
        </MemoryRouter>
      </AuthProvider>,
    )
    const link = screen.getByRole('link', { name: 'Đăng nhập với Google' })
    expect(link).toHaveAttribute('href', '/api/auth/login/google')
  })

  it('logs in with email and password and stores the token', async () => {
    fetchMock.mockResolvedValueOnce(
      response({ access_token: 'local-token', token_type: 'bearer', role: 'reader' }),
    )

    render(
      <AuthProvider>
        <MemoryRouter>
          <LoginPage />
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
    fireEvent.click(screen.getByRole('button', { name: 'Đăng nhập' }))

    await waitFor(() => expect(screen.getByTestId('token').textContent).toBe('local-token'))
    expect(fetchMock).toHaveBeenCalledWith(
      '/api/auth/login',
      expect.objectContaining({
        method: 'POST',
        body: JSON.stringify({ email: 'student@hcmus.edu.vn', password: 'supersecret' }),
      }),
    )
  })

  it('shows an error message when login fails', async () => {
    fetchMock.mockResolvedValueOnce(response({ detail: 'Invalid email or password.' }, 401))

    render(
      <AuthProvider>
        <MemoryRouter>
          <LoginPage />
        </MemoryRouter>
      </AuthProvider>,
    )

    fireEvent.change(screen.getByLabelText('Email'), {
      target: { value: 'student@hcmus.edu.vn' },
    })
    fireEvent.change(screen.getByLabelText('Mật khẩu'), {
      target: { value: 'wrong' },
    })
    fireEvent.click(screen.getByRole('button', { name: 'Đăng nhập' }))

    expect(await screen.findByRole('alert')).toHaveTextContent('Invalid email or password.')
  })

  it('links to the register page', () => {
    render(
      <AuthProvider>
        <MemoryRouter>
          <LoginPage />
        </MemoryRouter>
      </AuthProvider>,
    )
    expect(screen.getByRole('link', { name: 'Đăng ký' })).toHaveAttribute('href', '/register')
  })
})
