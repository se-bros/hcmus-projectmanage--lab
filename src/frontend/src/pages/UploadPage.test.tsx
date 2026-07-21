import { cleanup, render, screen } from '@testing-library/react'
import { afterEach, describe, expect, it } from 'vitest'
import { UploadPage } from './UploadPage'
import { AuthProvider } from '../context/AuthContext'

function fakeToken(payload: Record<string, unknown>): string {
  const base64url = (value: string) =>
    btoa(value).replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '')
  const header = base64url(JSON.stringify({ alg: 'HS256', typ: 'JWT' }))
  const body = base64url(JSON.stringify(payload))
  return `${header}.${body}.signature`
}

describe('UploadPage', () => {
  afterEach(() => {
    cleanup()
    window.localStorage.clear()
  })

  it('hides the upload form and shows a permission message for a reader', () => {
    window.localStorage.setItem('ldms_token', fakeToken({ sub: 'u1', role: 'reader' }))
    render(
      <AuthProvider>
        <UploadPage />
      </AuthProvider>,
    )
    expect(screen.queryByLabelText('File tài liệu')).not.toBeInTheDocument()
    expect(
      screen.getByText(
        'Bạn không có quyền tải lên tài liệu. Liên hệ quản trị viên nếu cần quyền editor.',
      ),
    ).toBeInTheDocument()
  })

  it('hides the upload form for a guest with no token', () => {
    render(
      <AuthProvider>
        <UploadPage />
      </AuthProvider>,
    )
    expect(screen.queryByLabelText('File tài liệu')).not.toBeInTheDocument()
  })

  it('shows the upload form for an editor', () => {
    window.localStorage.setItem('ldms_token', fakeToken({ sub: 'u1', role: 'editor' }))
    render(
      <AuthProvider>
        <UploadPage />
      </AuthProvider>,
    )
    expect(screen.getByText('File tài liệu')).toBeInTheDocument()
  })

  it('shows the upload form for an admin', () => {
    window.localStorage.setItem('ldms_token', fakeToken({ sub: 'u1', role: 'admin' }))
    render(
      <AuthProvider>
        <UploadPage />
      </AuthProvider>,
    )
    expect(screen.getByText('File tài liệu')).toBeInTheDocument()
  })
})
