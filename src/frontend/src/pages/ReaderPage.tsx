import { useCallback, useEffect, useRef, useState } from 'react'
import { Link, useParams } from 'react-router'
import ePub, { type Location, type Rendition } from 'epubjs'
import {
  createHighlight,
  deleteHighlight,
  getBookmark,
  getHighlights,
  getReaderContent,
  saveBookmark,
  updateHighlightNote,
  type Highlight,
  type ReaderContent,
} from '../services/api'
import { AUTH_TOKEN_STORAGE_KEY } from '../context/AuthContext'
import HighlightPopover from '../components/HighlightPopover'
import HighlightSidebar from '../components/HighlightSidebar'

const FONT_KEY = 'ldms_reader_font_size'
const THEME_KEY = 'ldms_reader_theme'
const LIGHT_THEME = { body: { color: '#1a1a1a', background: '#ffffff' } }
const DARK_THEME = { body: { color: '#e6e6e6', background: '#141414' } }
const HIGHLIGHT_STYLES = { fill: '#f5c518', 'fill-opacity': '0.4' }

type ReaderTheme = 'light' | 'dark'

type PendingSelection = {
  cfiRange: string
  text: string
  position: { top: number; left: number }
}

/** Tô một highlight lên trang sách. Trả về false khi CFI không còn dựng lại
 * được trên bản EPUB hiện tại — bản ghi khi đó thuộc nhóm "không định vị được"
 * (FR-011). Không tự dò tìm lại vị trí (FR-011c). */
function renderAnnotation(rendition: Rendition, highlight: Highlight): boolean {
  try {
    rendition.annotations.add(
      'highlight',
      highlight.cfi_range,
      { id: highlight.id },
      undefined,
      'ldms-highlight',
      HIGHLIGHT_STYLES,
    )
    return true
  } catch {
    return false
  }
}

function readStoredFontSize(): number {
  const stored = Number(window.localStorage.getItem(FONT_KEY))
  return Number.isFinite(stored) && stored >= 80 && stored <= 200 ? stored : 100
}

function readStoredTheme(): ReaderTheme {
  return window.localStorage.getItem(THEME_KEY) === 'dark' ? 'dark' : 'light'
}

function ReaderPage() {
  const { documentId } = useParams<{ documentId: string }>()
  const viewerRef = useRef<HTMLDivElement | null>(null)
  const renditionRef = useRef<Rendition | null>(null)
  const lastCfiRef = useRef<string | null>(null)
  const [content, setContent] = useState<ReaderContent | null>(null)
  const [error, setError] = useState<string | null>(null)
  const [loading, setLoading] = useState(true)
  const [fontSize, setFontSize] = useState<number>(readStoredFontSize)
  const [theme, setTheme] = useState<ReaderTheme>(readStoredTheme)
  const prefsRef = useRef({ fontSize, theme })
  const [anchored, setAnchored] = useState<Highlight[]>([])
  const [orphaned, setOrphaned] = useState<Highlight[]>([])
  const [pending, setPending] = useState<PendingSelection | null>(null)
  const [highlightError, setHighlightError] = useState<string | null>(null)
  const [selectedId, setSelectedId] = useState<string | null>(null)
  const [noteError, setNoteError] = useState<string | null>(null)

  useEffect(() => {
    if (!documentId) {
      return
    }
    const id = documentId
    let cancelled = false
    setLoading(true)
    setError(null)
    setContent(null)
    lastCfiRef.current = null

    getReaderContent(id)
      .then((reader) => {
        if (cancelled || !viewerRef.current) {
          return
        }
        setContent(reader)
        const book = ePub(reader.epub_url)
        const rendition = book.renderTo(viewerRef.current, {
          width: '100%',
          height: '100%',
          flow: 'scrolled-doc',
        })
        renditionRef.current = rendition
        rendition.themes.register('light', LIGHT_THEME)
        rendition.themes.register('dark', DARK_THEME)
        rendition.themes.select(prefsRef.current.theme)
        rendition.themes.fontSize(`${prefsRef.current.fontSize}%`)
        rendition.on('relocated', (location: Location) => {
          lastCfiRef.current = location?.start?.cfi ?? null
        })
        rendition.on('selected', (cfiRange: string, contents: { window: Window }) => {
          const selection = contents.window.getSelection()
          const text = selection?.toString().trim() ?? ''
          if (!text) return
          const rect = selection?.getRangeAt(0).getBoundingClientRect()
          setHighlightError(null)
          setPending({
            cfiRange,
            text,
            position: { top: (rect?.bottom ?? 0) + window.scrollY, left: rect?.left ?? 0 },
          })
        })

        void getHighlights(id)
          .then((highlights) => {
            if (cancelled) return
            const rendered: Highlight[] = []
            const broken: Highlight[] = []
            highlights.forEach((highlight) => {
              if (renderAnnotation(rendition, highlight)) rendered.push(highlight)
              else broken.push(highlight)
            })
            setAnchored(rendered)
            setOrphaned(broken)
          })
          .catch(() => {
            // Chưa đăng nhập hoặc lỗi mạng: vẫn đọc được sách, chỉ không có đánh dấu.
          })

        return getBookmark(id)
          .then((bookmark) => rendition.display(bookmark.location))
          .catch(() => rendition.display())
      })
      .catch((err: Error) => {
        if (!cancelled) setError(err.message)
      })
      .finally(() => {
        if (!cancelled) setLoading(false)
      })

    return () => {
      cancelled = true
      setAnchored([])
      setOrphaned([])
      setPending(null)
      const cfi = lastCfiRef.current
      const token = window.localStorage.getItem(AUTH_TOKEN_STORAGE_KEY)
      if (cfi && token) {
        void saveBookmark(id, cfi).catch(() => {})
      }
      renditionRef.current?.destroy()
      renditionRef.current = null
      lastCfiRef.current = null
    }
  }, [documentId])

  useEffect(() => {
    prefsRef.current = { fontSize, theme }
    window.localStorage.setItem(FONT_KEY, String(fontSize))
    window.localStorage.setItem(THEME_KEY, theme)
    const rendition = renditionRef.current
    if (rendition) {
      rendition.themes.select(theme)
      rendition.themes.fontSize(`${fontSize}%`)
    }
  }, [fontSize, theme])

  const handleCreateHighlight = useCallback(
    (note: string | null) => {
      const rendition = renditionRef.current
      if (!documentId || !pending || !rendition) return
      createHighlight(documentId, pending.cfiRange, pending.text, note)
        .then((highlight) => {
          if (renderAnnotation(rendition, highlight))
            setAnchored((current) => [...current, highlight])
          else setOrphaned((current) => [...current, highlight])
          setPending(null)
        })
        .catch((err: Error) => setHighlightError(err.message))
    },
    [documentId, pending],
  )

  const handleSaveNote = useCallback(
    (highlight: Highlight, note: string | null) => {
      if (!documentId) return
      setNoteError(null)
      updateHighlightNote(documentId, highlight.id, note)
        .then((updated) => {
          const replace = (items: Highlight[]) =>
            items.map((item) => (item.id === updated.id ? updated : item))
          setAnchored(replace)
          setOrphaned(replace)
        })
        .catch((err: Error) => setNoteError(err.message))
    },
    [documentId],
  )

  const handleDeleteHighlight = useCallback(
    (highlight: Highlight) => {
      if (!documentId) return
      setNoteError(null)
      deleteHighlight(documentId, highlight.id)
        .then(() => {
          // Bản ghi trong nhóm "không định vị được" không có annotation để gỡ.
          renditionRef.current?.annotations.remove(highlight.cfi_range, 'highlight')
          const drop = (items: Highlight[]) => items.filter((item) => item.id !== highlight.id)
          setAnchored(drop)
          setOrphaned(drop)
          setSelectedId(null)
        })
        .catch((err: Error) => setNoteError(err.message))
    },
    [documentId],
  )

  if (error) {
    return (
      <div className="state" role="alert">
        <p className="state-title state-title-danger">Không mở được tài liệu</p>
        <p className="state-detail">{error}</p>
        <Link className="btn-secondary" to="/documents">
          Về danh sách
        </Link>
      </div>
    )
  }

  return (
    <article className="reader">
      <div className="reader-toolbar">
        <Link to="/documents" className="back-link">
          ← Về danh sách
        </Link>
        {content && <span className="reader-title">{content.title}</span>}
        <div className="reader-controls">
          <button
            type="button"
            className="btn-secondary"
            aria-label="Giảm cỡ chữ"
            onClick={() => setFontSize((size) => Math.max(80, size - 10))}
          >
            A−
          </button>
          <button
            type="button"
            className="btn-secondary"
            aria-label="Tăng cỡ chữ"
            onClick={() => setFontSize((size) => Math.min(200, size + 10))}
          >
            A+
          </button>
          <button
            type="button"
            className="btn-secondary"
            onClick={() => setTheme((current) => (current === 'light' ? 'dark' : 'light'))}
          >
            {theme === 'light' ? '🌙 Nền tối' : '☀️ Nền sáng'}
          </button>
        </div>
      </div>
      {loading && <p className="page-sub">Đang tải nội dung…</p>}
      {highlightError && (
        <p className="state-detail" role="alert">
          {highlightError}
        </p>
      )}
      <div className="reader-body">
        <div ref={viewerRef} className="reader-epub" style={{ height: '70vh' }} />
        <HighlightSidebar
          anchored={anchored}
          orphaned={orphaned}
          selectedId={selectedId}
          noteError={noteError}
          onSelect={(highlight) => {
            setNoteError(null)
            setSelectedId((current) => (current === highlight.id ? null : highlight.id))
          }}
          onSaveNote={handleSaveNote}
          onDelete={handleDeleteHighlight}
        />
      </div>
      {pending && (
        <HighlightPopover
          selectedText={pending.text}
          position={pending.position}
          error={highlightError}
          onCreate={handleCreateHighlight}
          onDismiss={() => setPending(null)}
        />
      )}
      <div className="reader-nav">
        <button
          type="button"
          className="btn-secondary"
          onClick={() => void renditionRef.current?.prev()}
        >
          ← Trang trước
        </button>
        <button
          type="button"
          className="btn-secondary"
          onClick={() => void renditionRef.current?.next()}
        >
          Trang sau →
        </button>
      </div>
    </article>
  )
}

export default ReaderPage
