import { cleanup, fireEvent, render, screen } from '@testing-library/react'
import { MemoryRouter } from 'react-router'
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest'
import { ProfileMenu } from './ProfileMenu'
import { AuthProvider } from '../context/AuthContext'

const fetchMock = vi.fn<typeof fetch>()

describe('ProfileMenu', () => {
  beforeEach(() => {
    vi.stubGlobal('fetch', fetchMock)
    fetchMock.mockReset()
    fetchMock.mockResolvedValue(new Response(null, { status: 204 }))
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

  it('opens the dropdown on click and shows Cài đặt / Đăng xuất', () => {
    renderMenu()
    expect(screen.queryByRole('menuitem', { name: 'Cài đặt' })).not.toBeInTheDocument()

    fireEvent.click(screen.getByRole('button', { name: /Tài khoản/ }))

    expect(screen.getByRole('menuitem', { name: 'Cài đặt' })).toBeInTheDocument()
    expect(screen.getByRole('menuitem', { name: 'Đăng xuất' })).toBeInTheDocument()
  })

  it('calls onOpenSettings and closes the dropdown when Cài đặt is clicked', () => {
    const onOpenSettings = vi.fn()
    renderMenu(onOpenSettings)

    fireEvent.click(screen.getByRole('button', { name: /Tài khoản/ }))
    fireEvent.click(screen.getByRole('menuitem', { name: 'Cài đặt' }))

    expect(onOpenSettings).toHaveBeenCalledOnce()
    expect(screen.queryByRole('menuitem', { name: 'Cài đặt' })).not.toBeInTheDocument()
  })

  it('closes the dropdown when clicking outside', () => {
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

    fireEvent.click(screen.getByRole('button', { name: /Tài khoản/ }))
    expect(screen.getByRole('menuitem', { name: 'Cài đặt' })).toBeInTheDocument()

    fireEvent.mouseDown(screen.getByTestId('outside'))
    expect(screen.queryByRole('menuitem', { name: 'Cài đặt' })).not.toBeInTheDocument()
  })
})
