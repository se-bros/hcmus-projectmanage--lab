import { NavLink, Route, Routes } from 'react-router-dom'
import DocumentListPage from './pages/DocumentListPage'
import ReaderPage from './pages/ReaderPage'
import SearchPage from './pages/SearchPage'

function App() {
  return (
    <>
      <header className="app-header">
        <div className="app-header-inner">
          <NavLink to="/" className="brand">
            HCMUS-LDMS<span>Thư viện số</span>
          </NavLink>
          <nav className="app-nav">
            <NavLink to="/" end>
              Danh sách
            </NavLink>
            <NavLink to="/search">Tìm kiếm</NavLink>
          </nav>
        </div>
      </header>
      <main className="page">
        <Routes>
          <Route path="/" element={<DocumentListPage />} />
          <Route path="/reader/:documentId" element={<ReaderPage />} />
          <Route path="/search" element={<SearchPage />} />
        </Routes>
      </main>
    </>
  )
}

export default App
