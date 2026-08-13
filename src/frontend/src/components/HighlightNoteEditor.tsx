import { useState } from 'react'
import { MAX_NOTE_LENGTH } from '../services/api'

const COUNTER_VISIBLE_FROM = MAX_NOTE_LENGTH - 200

type HighlightNoteEditorProps = {
  initialNote: string | null
  error?: string | null
  onSave: (note: string | null) => void
  saveLabel?: string
}

function HighlightNoteEditor({
  initialNote,
  error,
  onSave,
  saveLabel = 'Lưu ghi chú',
}: HighlightNoteEditorProps) {
  // Không reset về `initialNote` khi server trả lỗi: FR-009 yêu cầu giữ nguyên
  // nội dung đang gõ để độc giả tự cắt ngắn.
  const [draft, setDraft] = useState(initialNote ?? '')
  const tooLong = draft.length > MAX_NOTE_LENGTH

  return (
    <div className="highlight-note-editor">
      <label className="highlight-note-label">
        Ghi chú
        <textarea
          className="highlight-note-input"
          value={draft}
          rows={3}
          onChange={(event) => setDraft(event.target.value)}
          placeholder={initialNote ? '' : 'Chưa có ghi chú'}
        />
      </label>
      {(draft.length >= COUNTER_VISIBLE_FROM || tooLong) && (
        <p className={tooLong ? 'highlight-note-count-over' : 'highlight-note-count'}>
          {draft.length}/{MAX_NOTE_LENGTH} ký tự
        </p>
      )}
      {error && (
        <p className="highlight-note-count-over" role="alert">
          {error}
        </p>
      )}
      <button
        type="button"
        className="btn-primary"
        disabled={tooLong}
        onClick={() => onSave(draft.trim() ? draft : null)}
      >
        {saveLabel}
      </button>
    </div>
  )
}

export default HighlightNoteEditor
