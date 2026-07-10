import type { Book } from '../store/mockData'
import { BookOpen, Lock, Globe, Building2, Tag } from 'lucide-react'

interface BookCardProps {
  book: Book
  onRead: (book: Book) => void
}

const accessIcon = {
  Public: <Globe size={12} />,
  Internal: <Building2 size={12} />,
  Restricted: <Lock size={12} />,
}

const accessColor = {
  Public: 'badge-green',
  Internal: 'badge-blue',
  Restricted: 'badge-red',
}

export default function BookCard({ book, onRead }: BookCardProps) {
  return (
    <div className="book-card">
      <div className="book-card-cover">
        <span className="book-cover-emoji">{book.cover}</span>
        <span className={`access-badge ${accessColor[book.access]}`}>
          {accessIcon[book.access]}
          {book.access}
        </span>
      </div>
      <div className="book-card-body">
        <h3 className="book-title">{book.title}</h3>
        <p className="book-author">{book.author} • {book.year}</p>
        <p className="book-desc">{book.description}</p>
        <div className="book-tags">
          {book.tags.slice(0, 3).map(tag => (
            <span key={tag} className="tag-chip">
              <Tag size={10} />
              {tag}
            </span>
          ))}
        </div>
        <div className="book-meta">
          <span>{book.pages} trang</span>
          <span>OCR: {book.ocrAccuracy}%</span>
        </div>
        <button className="btn-read" onClick={() => onRead(book)}>
          <BookOpen size={16} />
          Đọc ngay
        </button>
      </div>
    </div>
  )
}
