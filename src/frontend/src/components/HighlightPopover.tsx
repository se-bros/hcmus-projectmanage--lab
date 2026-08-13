import HighlightNoteEditor from './HighlightNoteEditor'

type HighlightPopoverProps = {
  selectedText: string
  position: { top: number; left: number }
  error?: string | null
  onCreate: (note: string | null) => void
  onDismiss: () => void
}

function HighlightPopover({
  selectedText,
  position,
  error,
  onCreate,
  onDismiss,
}: HighlightPopoverProps) {
  return (
    <div
      className="highlight-popover"
      style={{ top: position.top, left: position.left }}
      role="dialog"
      aria-label="Đánh dấu đoạn văn"
    >
      <p className="highlight-popover-excerpt">{selectedText}</p>
      <div className="highlight-popover-actions">
        <HighlightNoteEditor
          initialNote={null}
          error={error}
          onSave={onCreate}
          saveLabel="Đánh dấu"
        />
        <button type="button" className="btn-secondary" onClick={onDismiss}>
          Bỏ qua
        </button>
      </div>
    </div>
  )
}

export default HighlightPopover
