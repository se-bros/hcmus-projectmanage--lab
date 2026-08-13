import type { Highlight } from '../services/api'
import HighlightNoteEditor from './HighlightNoteEditor'

type HighlightSidebarProps = {
  anchored: Highlight[]
  orphaned: Highlight[]
  selectedId: string | null
  noteError: string | null
  onSelect: (highlight: Highlight) => void
  onSaveNote: (highlight: Highlight, note: string | null) => void
  onDelete: (highlight: Highlight) => void
}

type HighlightGroupProps = HighlightSidebarProps & {
  items: Highlight[]
  orphanedGroup?: boolean
}

function HighlightGroup({
  items,
  orphanedGroup,
  selectedId,
  noteError,
  onSelect,
  onSaveNote,
  onDelete,
}: HighlightGroupProps) {
  return (
    <ul className="highlight-list">
      {items.map((highlight) => (
        <li key={highlight.id}>
          <button
            type="button"
            className={orphanedGroup ? 'highlight-item highlight-item-orphaned' : 'highlight-item'}
            onClick={() => onSelect(highlight)}
          >
            <span className="highlight-item-text">{highlight.selected_text}</span>
            {highlight.note && selectedId !== highlight.id && (
              <span className="highlight-item-note">{highlight.note}</span>
            )}
          </button>
          {selectedId === highlight.id && (
            <div className="highlight-item-detail">
              <HighlightNoteEditor
                key={highlight.id}
                initialNote={highlight.note}
                error={noteError}
                onSave={(note) => onSaveNote(highlight, note)}
              />
              <button type="button" className="btn-secondary" onClick={() => onDelete(highlight)}>
                Xóa đánh dấu
              </button>
            </div>
          )}
        </li>
      ))}
    </ul>
  )
}

function HighlightSidebar(props: HighlightSidebarProps) {
  const { anchored, orphaned } = props

  if (anchored.length === 0 && orphaned.length === 0) {
    return (
      <aside className="highlight-sidebar" aria-label="Đánh dấu">
        <p className="page-sub">Chưa có đánh dấu nào.</p>
      </aside>
    )
  }

  return (
    <aside className="highlight-sidebar" aria-label="Đánh dấu">
      <h2 className="highlight-sidebar-title">Đánh dấu ({anchored.length})</h2>
      <HighlightGroup {...props} items={anchored} />

      {orphaned.length > 0 && (
        <>
          <h2 className="highlight-sidebar-title highlight-sidebar-title-muted">
            Đánh dấu không còn định vị được ({orphaned.length})
          </h2>
          <p className="page-sub">
            Tài liệu đã được xuất bản lại nên các đoạn dưới đây không tô lại được trên sách. Ghi chú
            của bạn vẫn còn nguyên.
          </p>
          <HighlightGroup {...props} items={orphaned} orphanedGroup />
        </>
      )}
    </aside>
  )
}

export default HighlightSidebar
