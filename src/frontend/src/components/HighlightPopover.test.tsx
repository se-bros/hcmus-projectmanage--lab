import { cleanup, fireEvent, render, screen } from '@testing-library/react'
import { afterEach, describe, expect, it, vi } from 'vitest'
import HighlightPopover from './HighlightPopover'

describe('HighlightPopover', () => {
  afterEach(() => {
    cleanup()
  })

  it('shows the selected excerpt and creates a highlight on confirm', () => {
    const onCreate = vi.fn()
    const onDismiss = vi.fn()
    render(
      <HighlightPopover
        selectedText="thư viện số là hạ tầng tri thức"
        position={{ top: 10, left: 20 }}
        onCreate={onCreate}
        onDismiss={onDismiss}
      />,
    )

    expect(screen.getByText('thư viện số là hạ tầng tri thức')).toBeInTheDocument()

    fireEvent.click(screen.getByRole('button', { name: 'Đánh dấu' }))
    expect(onCreate).toHaveBeenCalledWith(null)
    expect(onDismiss).not.toHaveBeenCalled()
  })

  it('can attach a note at creation time', () => {
    const onCreate = vi.fn()
    render(
      <HighlightPopover
        selectedText="một đoạn"
        position={{ top: 0, left: 0 }}
        onCreate={onCreate}
        onDismiss={vi.fn()}
      />,
    )

    fireEvent.change(screen.getByRole('textbox'), { target: { value: 'ghi chú ngay từ đầu' } })
    fireEvent.click(screen.getByRole('button', { name: 'Đánh dấu' }))
    expect(onCreate).toHaveBeenCalledWith('ghi chú ngay từ đầu')
  })

  it('dismisses without creating anything', () => {
    const onCreate = vi.fn()
    const onDismiss = vi.fn()
    render(
      <HighlightPopover
        selectedText="một đoạn"
        position={{ top: 0, left: 0 }}
        onCreate={onCreate}
        onDismiss={onDismiss}
      />,
    )

    fireEvent.click(screen.getByRole('button', { name: 'Bỏ qua' }))
    expect(onDismiss).toHaveBeenCalledTimes(1)
    expect(onCreate).not.toHaveBeenCalled()
  })
})
