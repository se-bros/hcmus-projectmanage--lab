import { fireEvent, render, screen } from '@testing-library/react'
import { describe, expect, it, vi } from 'vitest'
import HighlightSidebar from './HighlightSidebar'
import type { Highlight } from '../services/api'

function highlight(id: string, text: string, note: string | null = null): Highlight {
  return {
    id,
    document_id: 'doc-1',
    cfi_range: `epubcfi(/6/14!/4/2,/1:0,/1:${text.length})`,
    selected_text: text,
    note,
    created_at: '2026-08-12T09:00:00Z',
    updated_at: '2026-08-12T09:00:00Z',
  }
}

type Overrides = Partial<React.ComponentProps<typeof HighlightSidebar>>

function renderSidebar(overrides: Overrides = {}) {
  const props = {
    anchored: [],
    orphaned: [],
    selectedId: null,
    noteError: null,
    onSelect: vi.fn(),
    onSaveNote: vi.fn(),
    onDelete: vi.fn(),
    ...overrides,
  }
  render(<HighlightSidebar {...props} />)
  return props
}

describe('HighlightSidebar', () => {
  it('shows an empty state when there is nothing marked', () => {
    renderSidebar()
    expect(screen.getByText('Chưa có đánh dấu nào.')).toBeInTheDocument()
  })

  it('lists anchored highlights and reports the count', () => {
    renderSidebar({ anchored: [highlight('a', 'đoạn một'), highlight('b', 'đoạn hai')] })

    expect(screen.getByText('Đánh dấu (2)')).toBeInTheDocument()
    expect(screen.getByText('đoạn một')).toBeInTheDocument()
    expect(screen.queryByText(/không còn định vị được/)).not.toBeInTheDocument()
  })

  it('separates highlights whose position no longer resolves (FR-011)', () => {
    renderSidebar({
      anchored: [highlight('a', 'còn định vị được')],
      orphaned: [highlight('b', 'đoạn cũ', 'ghi chú vẫn còn')],
    })

    expect(screen.getByText('Đánh dấu (1)')).toBeInTheDocument()
    expect(screen.getByText('Đánh dấu không còn định vị được (1)')).toBeInTheDocument()
    // Bản ghi hỏng vẫn hiển thị nhờ selected_text đã lưu (FR-003)...
    expect(screen.getByText('đoạn cũ')).toBeInTheDocument()
    // ...và ghi chú không mất theo (FR-011a).
    expect(screen.getByText('ghi chú vẫn còn')).toBeInTheDocument()
  })

  it('reports the picked highlight to the caller', () => {
    const picked = highlight('a', 'đoạn một')
    const { onSelect } = renderSidebar({ anchored: [picked] })

    fireEvent.click(screen.getByText('đoạn một'))
    expect(onSelect).toHaveBeenCalledWith(picked)
  })

  it('edits the note of the selected highlight (FR-007)', () => {
    const picked = highlight('a', 'đoạn một', 'bản nháp')
    const { onSaveNote } = renderSidebar({ anchored: [picked], selectedId: 'a' })

    const textarea = screen.getByRole('textbox')
    expect(textarea).toHaveValue('bản nháp')

    fireEvent.change(textarea, { target: { value: 'bản đã sửa' } })
    fireEvent.click(screen.getByRole('button', { name: 'Lưu ghi chú' }))
    expect(onSaveNote).toHaveBeenCalledWith(picked, 'bản đã sửa')
  })

  it('clears the note without removing the highlight (FR-007)', () => {
    const picked = highlight('a', 'đoạn một', 'sẽ gỡ')
    const { onSaveNote, onDelete } = renderSidebar({ anchored: [picked], selectedId: 'a' })

    fireEvent.change(screen.getByRole('textbox'), { target: { value: '   ' } })
    fireEvent.click(screen.getByRole('button', { name: 'Lưu ghi chú' }))
    expect(onSaveNote).toHaveBeenCalledWith(picked, null)
    expect(onDelete).not.toHaveBeenCalled()
  })

  it('blocks saving a note past the limit and keeps the typed text (FR-009)', () => {
    renderSidebar({ anchored: [highlight('a', 'đoạn một')], selectedId: 'a' })

    const textarea = screen.getByRole('textbox')
    fireEvent.change(textarea, { target: { value: 'a'.repeat(2001) } })

    expect(screen.getByText('2001/2000 ký tự')).toBeInTheDocument()
    expect(screen.getByRole('button', { name: 'Lưu ghi chú' })).toBeDisabled()
    // Nội dung đang gõ không bị mất trắng để độc giả tự cắt ngắn.
    expect(textarea).toHaveValue('a'.repeat(2001))
  })

  it('deletes the selected highlight (AC 3)', () => {
    const picked = highlight('a', 'đoạn một')
    const { onDelete } = renderSidebar({ anchored: [picked], selectedId: 'a' })

    fireEvent.click(screen.getByRole('button', { name: 'Xóa đánh dấu' }))
    expect(onDelete).toHaveBeenCalledWith(picked)
  })

  it('deletes a highlight from the unresolvable group too (FR-011b)', () => {
    const broken = highlight('b', 'đoạn cũ', 'ghi chú')
    const { onDelete } = renderSidebar({ orphaned: [broken], selectedId: 'b' })

    fireEvent.click(screen.getByRole('button', { name: 'Xóa đánh dấu' }))
    expect(onDelete).toHaveBeenCalledWith(broken)
  })
})
