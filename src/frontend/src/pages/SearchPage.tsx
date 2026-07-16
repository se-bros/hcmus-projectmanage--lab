import { useState, type FormEvent, type ReactNode } from 'react'
import { Link } from 'react-router-dom'
import { searchDocuments, type SearchResult } from '../services/documents'

function highlightSnippet(snippet: string, keyword: string): ReactNode {
  const index = snippet.toLowerCase().indexOf(keyword.toLowerCase())
  if (!keyword || index === -1) {
    return snippet
  }
  return (
    <>
      {snippet.slice(0, index)}
      <mark>{snippet.slice(index, index + keyword.length)}</mark>
      {snippet.slice(index + keyword.length)}
    </>
  )
}

function SearchPage() {
  const [query, setQuery] = useState('')
  const [submitted, setSubmitted] = useState('')
  const [results, setResults] = useState<SearchResult[]>([])
  const [error, setError] = useState<string | null>(null)
  const [searching, setSearching] = useState(false)

  const handleSubmit = (event: FormEvent) => {
    event.preventDefault()
    const keyword = query.trim()
    if (!keyword) {
      setResults([])
      setSubmitted('')
      setError(null)
      return
    }
    setError(null)
    setSearching(true)
    searchDocuments(keyword)
      .then((data) => {
        setResults(data)
        setSubmitted(keyword)
      })
      .catch((err: Error) => setError(err.message))
      .finally(() => setSearching(false))
  }

  return (
    <>
      <div className="page-head">
        <h1 className="page-title">Tìm kiếm</h1>
        <p className="page-sub">Tìm trong nội dung đã số hóa của thư viện.</p>
      </div>

      <form className="search-form" onSubmit={handleSubmit}>
        <input
          type="search"
          className="search-input"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Nhập từ khóa, ví dụ: giới hạn"
          aria-label="Từ khóa tìm kiếm"
        />
        <button type="submit" className="btn-primary" disabled={searching}>
          {searching ? 'Đang tìm…' : 'Tìm'}
        </button>
      </form>

      {error && (
        <div className="state" role="alert">
          <p className="state-title state-title-danger">Tìm kiếm không thành công</p>
          <p className="state-detail">{error}</p>
        </div>
      )}

      {!error && submitted && results.length === 0 && (
        <div className="state">
          <p className="state-title">Không có kết quả cho "{submitted}"</p>
          <p className="state-detail">Thử từ khóa khác hoặc kiểm tra chính tả.</p>
        </div>
      )}

      {!error && results.length > 0 && (
        <>
          <p className="result-count">
            {results.length} kết quả cho "{submitted}"
          </p>
          <ul className="result-list">
            {results.map((result) => (
              <li key={result.document_id} className="result-item">
                <Link className="result-title" to={`/reader/${result.document_id}`}>
                  {result.title}
                </Link>
                <p className="result-snippet">{highlightSnippet(result.snippet, submitted)}</p>
              </li>
            ))}
          </ul>
        </>
      )}
    </>
  )
}

export default SearchPage
