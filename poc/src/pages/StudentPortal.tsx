import { useState, useEffect, useCallback } from 'react'
import { Search, Filter, BookOpen, X, Loader2, Wifi, WifiOff } from 'lucide-react'
import BookCard from '../components/BookCard'
import type { Book } from '../store/mockData'
import { CATEGORIES } from '../store/mockData'
import { fetchBooks } from '../store/api'

interface StudentPortalProps {
  onReadBook: (book: Book) => void
}

export default function StudentPortal({ onReadBook }: StudentPortalProps) {
  const [query, setQuery] = useState('')
  const [selectedCategory, setSelectedCategory] = useState('')
  const [results, setResults] = useState<Book[]>([])
  const [loading, setLoading] = useState(true)
  const [online, setOnline] = useState<boolean | null>(null)  // null = checking

  const load = useCallback(async (q: string, cat: string) => {
    setLoading(true)
    try {
      // Quick ping to check backend
      const ping = await fetch('http://localhost:8000/', { signal: AbortSignal.timeout(2000) })
      setOnline(ping.ok)
    } catch {
      setOnline(false)
    }
    const books = await fetchBooks(q || undefined, cat || undefined)
    setResults(books)
    setLoading(false)
  }, [])

  // Debounce search
  useEffect(() => {
    const timer = setTimeout(() => load(query, selectedCategory), 300)
    return () => clearTimeout(timer)
  }, [query, selectedCategory, load])

  return (
    <div className="page-container">
      {/* Hero search */}
      <div className="hero-section">
        <h1 className="hero-title">
          <BookOpen size={32} /> Thư viện Số HCMUS
        </h1>
        <p className="hero-sub">
          Tìm kiếm toàn văn — tra cứu từ khóa bên trong nội dung sách
        </p>

        <div className="search-bar">
          <Search size={20} className="search-icon" />
          <input
            className="search-input"
            type="text"
            placeholder="Nhập từ khóa, tên sách, tác giả, nội dung..."
            value={query}
            onChange={e => setQuery(e.target.value)}
            autoFocus
          />
          {query && (
            <button className="search-clear" onClick={() => setQuery('')}>
              <X size={16} />
            </button>
          )}
        </div>

        {/* Category filters */}
        <div className="filter-row">
          <Filter size={14} />
          <button
            className={`filter-chip ${!selectedCategory ? 'active' : ''}`}
            onClick={() => setSelectedCategory('')}
          >
            Tất cả
          </button>
          {CATEGORIES.map(cat => (
            <button
              key={cat}
              className={`filter-chip ${selectedCategory === cat ? 'active' : ''}`}
              onClick={() => setSelectedCategory(cat === selectedCategory ? '' : cat)}
            >
              {cat}
            </button>
          ))}
        </div>
      </div>

      {/* Backend status badge */}
      <div className="results-section">
        <div className="results-header">
          <span className="results-count">
            {loading
              ? 'Đang tải...'
              : query || selectedCategory
                ? `Tìm thấy ${results.length} kết quả`
                : `${results.length} tài liệu số hóa`}
          </span>
          {query && !loading && (
            <span className="search-highlight">
              Tìm kiếm toàn văn: "<strong>{query}</strong>"
            </span>
          )}
          <span className={`backend-badge ${online ? 'online' : online === false ? 'offline' : 'checking'}`}>
            {online === null && <Loader2 size={12} className="spin" />}
            {online === true && <Wifi size={12} />}
            {online === false && <WifiOff size={12} />}
            {online === null ? 'Đang kết nối...' : online ? 'Backend: PostgreSQL' : 'Backend offline — mock data'}
          </span>
        </div>

        {loading ? (
          <div className="empty-state">
            <Loader2 size={36} className="spin" />
            <p>Đang tải dữ liệu...</p>
          </div>
        ) : results.length === 0 ? (
          <div className="empty-state">
            <BookOpen size={48} />
            <p>Không tìm thấy tài liệu phù hợp</p>
            <button className="btn-secondary" onClick={() => { setQuery(''); setSelectedCategory('') }}>
              Xem tất cả tài liệu
            </button>
          </div>
        ) : (
          <div className="books-grid">
            {results.map(book => (
              <BookCard key={book.id} book={book} onRead={onReadBook} />
            ))}
          </div>
        )}
      </div>
    </div>
  )
}
