import { cleanup, fireEvent, render, screen, waitFor } from '@testing-library/react'
import { MemoryRouter } from 'react-router'
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest'
import { ProfileMenu } from './ProfileMenu'
import { AuthProvider } from '../context/AuthContext'

const fetchMock = vi.fn<typeof fetch>()

function profileResponse(username: string | null = null): Response {
  return new Response(
    JSON.stringify({
      id: 'u1',
      email: 'user@hcmus.edu.vn',
      username,
      role: 'reader',
      auth_provider: 'local',
      has_password: true,
    }),
    { status: 200, headers: { 'Content-Type': 'application/json' } },
  )
}

describe('ProfileMenu', () => {
  beforeEach(() => {
    vi.stubGlobal('fetch', fetchMock)
    fetchMock.mockReset()
    fetchMock.mockResolvedValue(profileResponse())
  })

  afterEach(() => {
    cleanup()
    vi.restoreAllMocks()
    vi.unstubAllGlobals()
    window.localStorage.clear()
  })

  function renderMenu(onOpenSettings = vi.fn()) {
    return render(
      <AuthProvider>
        <MemoryRouter>
          <ProfileMenu onOpenSettings={onOpenSettings} />
        </MemoryRouter>
      </AuthProvider>,
    )
  }

  it('defaults the trigger label to "user" when no username is set', async () => {
    renderMenu()
    expect(await screen.findByRole('button', { name: /user/ })).toBeInTheDocument()
  })

  it('shows the fetched username as the trigger label', async () => {
    fetchMock.mockReset()
    fetchMock.mockResolvedValue(profileResponse('Nguyen Van A'))
    renderMenu()
    expect(await screen.findByRole('button', { name: /Nguyen Van A/ })).toBeInTheDocument()
  })

  it('opens the dropdown on click and shows Cài đặt / Đăng xuất', async () => {
    renderMenu()
    expect(screen.queryByRole('menuitem', { name: 'Cài đặt' })).not.toBeInTheDocument()

    fireEvent.click(await screen.findByRole('button', { name: /user/ }))

    expect(screen.getByRole('menuitem', { name: 'Cài đặt' })).toBeInTheDocument()
    expect(screen.getByRole('menuitem', { name: 'Đăng xuất' })).toBeInTheDocument()
  })

  it('calls onOpenSettings and closes the dropdown when Cài đặt is clicked', async () => {
    const onOpenSettings = vi.fn()
    renderMenu(onOpenSettings)

    fireEvent.click(await screen.findByRole('button', { name: /user/ }))
    fireEvent.click(screen.getByRole('menuitem', { name: 'Cài đặt' }))

    expect(onOpenSettings).toHaveBeenCalledOnce()
    expect(screen.queryByRole('menuitem', { name: 'Cài đặt' })).not.toBeInTheDocument()
  })

  it('closes the dropdown when clicking outside', async () => {
    render(
      <AuthProvider>
        <MemoryRouter>
          <div>
            <ProfileMenu onOpenSettings={vi.fn()} />
            <span data-testid="outside">outside</span>
          </div>
        </MemoryRouter>
      </AuthProvider>,
    )

    fireEvent.click(await screen.findByRole('button', { name: /user/ }))
    expect(screen.getByRole('menuitem', { name: 'Cài đặt' })).toBeInTheDocument()

    fireEvent.mouseDown(screen.getByTestId('outside'))
    await waitFor(() =>
      expect(screen.queryByRole('menuitem', { name: 'Cài đặt' })).not.toBeInTheDocument(),
    )
  })
})
