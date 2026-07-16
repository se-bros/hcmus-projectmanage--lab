import { cleanup, fireEvent, render, screen, waitFor } from '@testing-library/react'
import { MemoryRouter } from 'react-router'
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest'
import { CategoriesPage } from './CategoriesPage'

const fetchMock = vi.fn<typeof fetch>()

function response(body: object, status = 200): Response {
  return new Response(JSON.stringify(body), {
    status,
    headers: { 'Content-Type': 'application/json' },
  })
}

const parent = {
  id: 'parent-1',
  name: 'Science',
  parent_id: null,
  created_at: '2026-07-16T08:00:00Z',
  updated_at: '2026-07-16T08:00:00Z',
}

const child = {
  id: 'child-1',
  name: 'Physics',
  parent_id: 'parent-1',
  created_at: '2026-07-16T08:00:00Z',
  updated_at: '2026-07-16T08:00:00Z',
}

describe('CategoriesPage', () => {
  beforeEach(() => {
    vi.stubGlobal('fetch', fetchMock)
    fetchMock.mockReset()
  })

  afterEach(() => {
    cleanup()
    vi.restoreAllMocks()
    vi.unstubAllGlobals()
  })

  it('renders a two-level category tree', async () => {
    fetchMock.mockResolvedValueOnce(response([{ ...parent, children: [child] }]))
    render(
      <MemoryRouter>
        <CategoriesPage />
      </MemoryRouter>,
    )

    expect(await screen.findByRole('button', { name: 'Đổi tên Science' })).toBeInTheDocument()
    expect(screen.getByRole('button', { name: 'Đổi tên Physics' })).toBeInTheDocument()
    expect(screen.getByText('Cấp 1')).toBeInTheDocument()
    expect(screen.getByText('Cấp 2')).toBeInTheDocument()
  })

  it('creates a child, renames it and deletes it', async () => {
    fetchMock
      .mockResolvedValueOnce(response([{ ...parent, children: [] }]))
      .mockResolvedValueOnce(response(child, 201))
      .mockResolvedValueOnce(response([{ ...parent, children: [child] }]))
      .mockResolvedValueOnce(response({ ...child, name: 'Mechanics' }))
      .mockResolvedValueOnce(
        response([{ ...parent, children: [{ ...child, name: 'Mechanics' }] }]),
      )
      .mockResolvedValueOnce(new Response(null, { status: 204 }))
      .mockResolvedValueOnce(response([{ ...parent, children: [] }]))

    vi.spyOn(window, 'prompt').mockReturnValue('Mechanics')
    vi.spyOn(window, 'confirm').mockReturnValue(true)
    render(
      <MemoryRouter>
        <CategoriesPage />
      </MemoryRouter>,
    )
    await screen.findByRole('button', { name: 'Đổi tên Science' })

    fireEvent.change(screen.getByLabelText('Tên category'), { target: { value: 'Physics' } })
    fireEvent.change(screen.getByLabelText('Category cha'), { target: { value: 'parent-1' } })
    fireEvent.click(screen.getByRole('button', { name: 'Tạo category' }))
    expect(await screen.findByRole('button', { name: 'Đổi tên Physics' })).toBeInTheDocument()
    expect(fetchMock).toHaveBeenNthCalledWith(
      2,
      '/api/categories',
      expect.objectContaining({
        method: 'POST',
        body: JSON.stringify({ name: 'Physics', parent_id: 'parent-1' }),
      }),
    )

    fireEvent.click(screen.getByRole('button', { name: 'Đổi tên Physics' }))
    expect(await screen.findByRole('button', { name: 'Đổi tên Mechanics' })).toBeInTheDocument()

    fireEvent.click(screen.getByRole('button', { name: 'Xóa Mechanics' }))
    await waitFor(() =>
      expect(screen.queryByRole('button', { name: 'Đổi tên Mechanics' })).not.toBeInTheDocument(),
    )
    expect(fetchMock).toHaveBeenCalledWith('/api/categories/child-1', { method: 'DELETE' })
  })
})
