import { useEffect, useRef, useState } from 'react'
import { Link, useParams } from 'react-router'
import ePub, { type Location, type Rendition } from 'epubjs'
import { getBookmark, getReaderContent, saveBookmark, type ReaderContent } from '../services/api'
import { AUTH_TOKEN_STORAGE_KEY } from '../context/AuthContext'

const FONT_KEY = 'ldms_reader_font_size'
const THEME_KEY = 'ldms_reader_theme'
const LIGHT_THEME = { body: { color: '#1a1a1a', background: '#ffffff' } }
const DARK_THEME = { body: { color: '#e6e6e6', background: '#141414' } }

type ReaderTheme = 'light' | 'dark'

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
      <div ref={viewerRef} className="reader-epub" style={{ height: '70vh' }} />
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
