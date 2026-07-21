import { cleanup, render, screen } from '@testing-library/react'
import { MemoryRouter, Route, Routes } from 'react-router'
import { afterEach, describe, expect, it } from 'vitest'
import { RequireRole } from './RequireRole'
import { AuthProvider } from '../context/AuthContext'

function fakeToken(payload: Record<string, unknown>): string {
  const base64url = (value: string) =>
    btoa(value).replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '')
  const header = base64url(JSON.stringify({ alg: 'HS256', typ: 'JWT' }))
  const body = base64url(JSON.stringify(payload))
  return `${header}.${body}.signature`
}

function renderAt(path: string) {
  return render(
    <AuthProvider>
      <MemoryRouter initialEntries={[path]}>
        <Routes>
          <Route
            path="/guarded"
            element={
              <RequireRole roles={['editor', 'admin']}>
                <span>Guarded content</span>
              </RequireRole>
            }
          />
          <Route path="/" element={<span>Home</span>} />
        </Routes>
      </MemoryRouter>
    </AuthProvider>,
  )
}

describe('RequireRole', () => {
  afterEach(() => {
    cleanup()
    window.localStorage.clear()
  })

  it('renders children when the role is allowed', () => {
    window.localStorage.setItem('ldms_token', fakeToken({ sub: 'u1', role: 'editor' }))
    renderAt('/guarded')
    expect(screen.getByText('Guarded content')).toBeInTheDocument()
  })

  it('redirects home when the role is not allowed', () => {
    window.localStorage.setItem('ldms_token', fakeToken({ sub: 'u1', role: 'reader' }))
    renderAt('/guarded')
    expect(screen.queryByText('Guarded content')).not.toBeInTheDocument()
    expect(screen.getByText('Home')).toBeInTheDocument()
  })

  it('redirects home when there is no token', () => {
    renderAt('/guarded')
    expect(screen.queryByText('Guarded content')).not.toBeInTheDocument()
    expect(screen.getByText('Home')).toBeInTheDocument()
  })
})
