import { useState, useRef, useEffect } from 'react'
import {
  X, ChevronLeft, ChevronRight, BookOpen, Bookmark,
  Highlighter, Quote, Sun, Moon, Coffee,
  Type, List, ArrowLeft
} from 'lucide-react'
import type { Book } from '../store/mockData'

interface EpubReaderProps {
  book: Book
  onClose: () => void
}

type Theme = 'light' | 'sepia' | 'dark'

interface Highlight {
  id: string
  text: string
  color: string
  note: string
}

export default function EpubReader({ book, onClose }: EpubReaderProps) {
  const [theme, setTheme] = useState<Theme>('light')
  const [fontSize, setFontSize] = useState(100)
  const [bookmarked, setBookmarked] = useState(false)
  const [highlights, setHighlights] = useState<Highlight[]>([])
  const [showSidebar, setShowSidebar] = useState(false)
  const [sidebarTab, setSidebarTab] = useState<'toc' | 'highlights'>('toc')
  const [showHighlightMenu, setShowHighlightMenu] = useState(false)
  const [highlightColor, setHighlightColor] = useState('#ffd700')
  const [noteText, setNoteText] = useState('')
  const [selectedText, setSelectedText] = useState('')
  const [copied, setCopied] = useState(false)
  const contentRef = useRef<HTMLDivElement>(null)

  const themeStyles: Record<Theme, React.CSSProperties> = {
    light: { background: '#ffffff', color: '#1a1a2e' },
    sepia: { background: '#f5ecd7', color: '#3d2b1f' },
    dark: { background: '#1a1a2e', color: '#d4d4d8' },
  }

  const handleTextSelection = () => {
    const sel = window.getSelection()
    const text = sel?.toString().trim()
    if (text && text.length > 3) {
      setSelectedText(text)
      setShowHighlightMenu(true)
    } else {
      setShowHighlightMenu(false)
    }
  }

  const addHighlight = () => {
    if (!selectedText) return
    const newHL: Highlight = {
      id: Date.now().toString(),
      text: selectedText,
      color: highlightColor,
      note: noteText,
    }
    setHighlights(prev => [...prev, newHL])
    setShowHighlightMenu(false)
    setSelectedText('')
    setNoteText('')
  }

  const handleCite = () => {
    const citation = `${book.author}. (${book.year}). ${book.title}. ${book.publisher}. Trích từ hệ thống HCMUS-LDMS. ID: ${book.id}`
    navigator.clipboard.writeText(citation).catch(() => {})
    setCopied(true)
    setTimeout(() => setCopied(false), 2500)
  }

  // Close highlight menu on outside click
  useEffect(() => {
    const handler = () => {
      const sel = window.getSelection()
      if (!sel?.toString().trim()) {
        setShowHighlightMenu(false)
      }
    }
    document.addEventListener('mousedown', handler)
    return () => document.removeEventListener('mousedown', handler)
  }, [])

  return (
    <div className="reader-root" style={themeStyles[theme]}>
      {/* Reader topbar */}
      <div className="reader-topbar" style={themeStyles[theme]}>
        <button className="reader-btn" onClick={onClose}>
          <ArrowLeft size={18} />
          <span>Trở về</span>
        </button>
        <div className="reader-book-info">
          <BookOpen size={16} />
          <span className="reader-book-title">{book.title}</span>
          <span className="reader-author">— {book.author}</span>
        </div>
        <div className="reader-controls">
          {/* Font size */}
          <div className="control-group">
            <button className="reader-btn" onClick={() => setFontSize(f => Math.max(70, f - 10))}>
              <Type size={13} />-
            </button>
            <span className="font-size-label">{fontSize}%</span>
            <button className="reader-btn" onClick={() => setFontSize(f => Math.min(200, f + 10))}>
              <Type size={16} />+
            </button>
          </div>
          {/* Theme */}
          <div className="control-group">
            <button className={`reader-btn ${theme === 'light' ? 'active-ctrl' : ''}`} onClick={() => setTheme('light')} title="Nền sáng">
              <Sun size={16} />
            </button>
            <button className={`reader-btn ${theme === 'sepia' ? 'active-ctrl' : ''}`} onClick={() => setTheme('sepia')} title="Nền Sepia">
              <Coffee size={16} />
            </button>
            <button className={`reader-btn ${theme === 'dark' ? 'active-ctrl' : ''}`} onClick={() => setTheme('dark')} title="Dark mode">
              <Moon size={16} />
            </button>
          </div>
          {/* Sidebar */}
          <button className={`reader-btn ${showSidebar ? 'active-ctrl' : ''}`} onClick={() => setShowSidebar(v => !v)}>
            <List size={16} />
          </button>
          {/* Bookmark */}
          <button
            className={`reader-btn ${bookmarked ? 'bookmarked' : ''}`}
            onClick={() => setBookmarked(v => !v)}
            title={bookmarked ? 'Đã đánh dấu trang' : 'Đánh dấu trang'}
          >
            <Bookmark size={16} fill={bookmarked ? 'currentColor' : 'none'} />
          </button>
          {/* Cite */}
          <button className="reader-btn cite-btn" onClick={handleCite}>
            <Quote size={16} />
            {copied ? 'Đã sao chép!' : 'Trích dẫn'}
          </button>
          <button className="reader-btn close-btn" onClick={onClose}>
            <X size={18} />
          </button>
        </div>
      </div>

      <div className="reader-body">
        {/* Sidebar */}
        {showSidebar && (
          <div className="reader-sidebar" style={themeStyles[theme]}>
            <div className="sidebar-tabs">
              <button
                className={`sidebar-tab ${sidebarTab === 'toc' ? 'active' : ''}`}
                onClick={() => setSidebarTab('toc')}
              >
                <List size={14} /> Mục lục
              </button>
              <button
                className={`sidebar-tab ${sidebarTab === 'highlights' ? 'active' : ''}`}
                onClick={() => setSidebarTab('highlights')}
              >
                <Highlighter size={14} /> Ghi chú ({highlights.length})
              </button>
            </div>
            {sidebarTab === 'toc' ? (
              <div className="toc-list">
                <div className="toc-item active">📖 Chương đang đọc</div>
                <div className="toc-item">2.1 Giải thuật cơ bản</div>
                <div className="toc-item">2.2 Phân tích độ phức tạp</div>
                <div className="toc-item">2.3 So sánh các thuật toán</div>
              </div>
            ) : (
              <div className="highlights-list">
                {highlights.length === 0 ? (
                  <p className="no-highlight">Chưa có ghi chú nào. Bôi đen văn bản để tô sáng.</p>
                ) : (
                  highlights.map(h => (
                    <div key={h.id} className="highlight-item">
                      <div className="highlight-bar" style={{ background: h.color }} />
                      <div>
                        <p className="highlight-text">"{h.text}"</p>
                        {h.note && <p className="highlight-note">📝 {h.note}</p>}
                      </div>
                    </div>
                  ))
                )}
              </div>
            )}
          </div>
        )}

        {/* Main content */}
        <div className="reader-content-wrap">
          <div
            ref={contentRef}
            className="reader-content"
            style={{ fontSize: `${fontSize}%`, ...themeStyles[theme] }}
            onMouseUp={handleTextSelection}
            dangerouslySetInnerHTML={{ __html: book.content }}
          />

          {/* Highlight toolbar */}
          {showHighlightMenu && (
            <div className="highlight-toolbar">
              <span className="selected-preview">"{selectedText.slice(0, 40)}{selectedText.length > 40 ? '…' : ''}"</span>
              <div className="color-picks">
                {['#ffd700', '#ff9f9f', '#9fffb8', '#9fcfff'].map(c => (
                  <button
                    key={c}
                    className={`color-dot ${highlightColor === c ? 'selected' : ''}`}
                    style={{ background: c }}
                    onClick={() => setHighlightColor(c)}
                  />
                ))}
              </div>
              <input
                className="note-input"
                placeholder="Thêm ghi chú (tùy chọn)..."
                value={noteText}
                onChange={e => setNoteText(e.target.value)}
              />
              <div className="highlight-actions">
                <button className="btn-highlight" onClick={addHighlight}>
                  <Highlighter size={14} /> Lưu
                </button>
                <button className="btn-cancel" onClick={() => { setShowHighlightMenu(false); setSelectedText('') }}>
                  <X size={14} />
                </button>
              </div>
            </div>
          )}

          {/* Navigation */}
          <div className="reader-nav">
            <button className="nav-btn">
              <ChevronLeft size={20} /> Chương trước
            </button>
            <span className="page-indicator">Trang 1 / {book.pages}</span>
            <button className="nav-btn">
              Chương sau <ChevronRight size={20} />
            </button>
          </div>

          {bookmarked && (
            <div className="bookmark-toast">
              <Bookmark size={14} fill="currentColor" /> Đã đánh dấu trang — sẽ quay lại tại đây lần sau
            </div>
          )}
        </div>
      </div>
    </div>
  )
}
