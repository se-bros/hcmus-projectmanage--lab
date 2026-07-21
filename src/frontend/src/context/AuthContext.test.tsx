import { cleanup, render, screen } from '@testing-library/react'
import { afterEach, describe, expect, it } from 'vitest'
import { AuthProvider, useAuth } from './AuthContext'

function fakeToken(payload: Record<string, unknown>): string {
  const base64url = (value: string) =>
    btoa(value).replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '')
  const header = base64url(JSON.stringify({ alg: 'HS256', typ: 'JWT' }))
  const body = base64url(JSON.stringify(payload))
  return `${header}.${body}.signature`
}

function Probe() {
  const { role, userId } = useAuth()
  return (
    <>
      <span data-testid="role">{role ?? 'none'}</span>
      <span data-testid="userId">{userId ?? 'none'}</span>
    </>
  )
}

describe('AuthContext', () => {
  afterEach(() => {
    cleanup()
    window.localStorage.clear()
  })

  it('exposes role and userId as null when there is no token', () => {
    render(
      <AuthProvider>
        <Probe />
      </AuthProvider>,
    )
    expect(screen.getByTestId('role').textContent).toBe('none')
    expect(screen.getByTestId('userId').textContent).toBe('none')
  })

  it('decodes role and userId from a stored token', () => {
    window.localStorage.setItem(
      'ldms_token',
      fakeToken({ sub: 'user-123', role: 'editor', email: 'a@hcmus.edu.vn' }),
    )
    render(
      <AuthProvider>
        <Probe />
      </AuthProvider>,
    )
    expect(screen.getByTestId('role').textContent).toBe('editor')
    expect(screen.getByTestId('userId').textContent).toBe('user-123')
  })

  it('treats a malformed token as unauthenticated for role/userId', () => {
    window.localStorage.setItem('ldms_token', 'not-a-valid-jwt')
    render(
      <AuthProvider>
        <Probe />
      </AuthProvider>,
    )
    expect(screen.getByTestId('role').textContent).toBe('none')
    expect(screen.getByTestId('userId').textContent).toBe('none')
  })
})
