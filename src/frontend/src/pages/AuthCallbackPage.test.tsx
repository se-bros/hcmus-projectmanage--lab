import { render, waitFor } from '@testing-library/react'
import { MemoryRouter, Route, Routes } from 'react-router'
import { afterEach, describe, expect, it } from 'vitest'
import { AuthCallbackPage } from './AuthCallbackPage'
import { AuthProvider, useAuth } from '../context/AuthContext'

function TokenProbe() {
  const { token } = useAuth()
  return <span data-testid="token">{token ?? 'none'}</span>
}

describe('AuthCallbackPage', () => {
  afterEach(() => {
    window.localStorage.clear()
  })

  it('stores the token from the query string and redirects home', async () => {
    const { getByTestId } = render(
      <AuthProvider>
        <MemoryRouter initialEntries={['/auth/callback?token=abc123']}>
          <Routes>
            <Route path="/auth/callback" element={<AuthCallbackPage />} />
            <Route path="/" element={<TokenProbe />} />
          </Routes>
        </MemoryRouter>
      </AuthProvider>,
    )

    await waitFor(() => expect(getByTestId('token').textContent).toBe('abc123'))
    expect(window.localStorage.getItem('ldms_token')).toBe('abc123')
  })
})
