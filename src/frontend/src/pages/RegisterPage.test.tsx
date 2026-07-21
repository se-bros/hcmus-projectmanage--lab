import { cleanup, fireEvent, render, screen, waitFor } from '@testing-library/react'
import { MemoryRouter, Route, Routes } from 'react-router'
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest'
import { RegisterPage } from './RegisterPage'
import { AuthProvider } from '../context/AuthContext'

const fetchMock = vi.fn<typeof fetch>()

function response(body: object, status = 200): Response {
  return new Response(JSON.stringify(body), {
    status,
    headers: { 'Content-Type': 'application/json' },
  })
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

  it('registers with matching passwords and redirects to login without storing a token', async () => {
    fetchMock.mockResolvedValueOnce(
      response({ access_token: 'new-token', token_type: 'bearer', role: 'reader' }, 201),
    )

    render(
      <AuthProvider>
        <MemoryRouter initialEntries={['/register']}>
          <Routes>
            <Route path="/register" element={<RegisterPage />} />
            <Route path="/login" element={<div data-testid="login-page" />} />
          </Routes>
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

    await waitFor(() => expect(screen.getByTestId('login-page')).toBeInTheDocument())
    expect(fetchMock).toHaveBeenCalledWith(
      '/api/auth/register',
      expect.objectContaining({
        method: 'POST',
        body: JSON.stringify({ email: 'student@hcmus.edu.vn', password: 'supersecret' }),
      }),
    )
    expect(window.localStorage.getItem('ldms_token')).toBeNull()
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
