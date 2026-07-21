import { cleanup, render, screen } from '@testing-library/react'
import { MemoryRouter } from 'react-router'
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest'
import App from './App'

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

describe('App nav', () => {
  beforeEach(() => {
    vi.stubGlobal('fetch', fetchMock)
    fetchMock.mockReset()
    fetchMock.mockResolvedValue(response([]))
  })

  afterEach(() => {
    cleanup()
    vi.restoreAllMocks()
    vi.unstubAllGlobals()
    window.localStorage.clear()
  })

  it('hides Dashboard OCR and Category for a reader', () => {
    window.localStorage.setItem('ldms_token', fakeToken({ sub: 'u1', role: 'reader' }))
    render(
      <MemoryRouter initialEntries={['/']}>
        <App />
      </MemoryRouter>,
    )
    expect(screen.queryByRole('link', { name: 'Dashboard OCR' })).not.toBeInTheDocument()
    expect(screen.queryByRole('link', { name: 'Category' })).not.toBeInTheDocument()
    expect(screen.getByRole('link', { name: 'Tài liệu' })).toBeInTheDocument()
  })

  it('shows Dashboard OCR but hides Category for an editor', () => {
    window.localStorage.setItem('ldms_token', fakeToken({ sub: 'u1', role: 'editor' }))
    render(
      <MemoryRouter initialEntries={['/']}>
        <App />
      </MemoryRouter>,
    )
    expect(screen.getByRole('link', { name: 'Dashboard OCR' })).toBeInTheDocument()
    expect(screen.queryByRole('link', { name: 'Category' })).not.toBeInTheDocument()
  })

  it('shows Dashboard OCR and Category for an admin', () => {
    window.localStorage.setItem('ldms_token', fakeToken({ sub: 'u1', role: 'admin' }))
    render(
      <MemoryRouter initialEntries={['/']}>
        <App />
      </MemoryRouter>,
    )
    expect(screen.getByRole('link', { name: 'Dashboard OCR' })).toBeInTheDocument()
    expect(screen.getByRole('link', { name: 'Category' })).toBeInTheDocument()
  })

  it('hides Dashboard OCR and Category for a logged-out guest', () => {
    render(
      <MemoryRouter initialEntries={['/']}>
        <App />
      </MemoryRouter>,
    )
    expect(screen.queryByRole('link', { name: 'Dashboard OCR' })).not.toBeInTheDocument()
    expect(screen.queryByRole('link', { name: 'Category' })).not.toBeInTheDocument()
  })

  it('redirects away from /dashboard for a reader navigating directly', () => {
    window.localStorage.setItem('ldms_token', fakeToken({ sub: 'u1', role: 'reader' }))
    render(
      <MemoryRouter initialEntries={['/dashboard']}>
        <App />
      </MemoryRouter>,
    )
    expect(screen.getByRole('heading', { name: 'Tải tài liệu scan' })).toBeInTheDocument()
  })

  it('redirects away from /categories for an editor navigating directly', () => {
    window.localStorage.setItem('ldms_token', fakeToken({ sub: 'u1', role: 'editor' }))
    render(
      <MemoryRouter initialEntries={['/categories']}>
        <App />
      </MemoryRouter>,
    )
    expect(screen.getByRole('heading', { name: 'Tải tài liệu scan' })).toBeInTheDocument()
  })
})
