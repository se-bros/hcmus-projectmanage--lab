import { NavLink, Navigate, Route, Routes } from 'react-router'
import './App.css'
import { DashboardPage } from './pages/DashboardPage'
import { DocumentsPage } from './pages/DocumentsPage'
import { DocumentViewerPage } from './pages/DocumentViewerPage'
import { UploadPage } from './pages/UploadPage'

function App() {
  return (
    <>
      <header className="site-header">
        <NavLink className="brand-link" to="/">
          <span className="brand-mark" aria-hidden="true">
            L
          </span>
          <span>
            <strong>HCMUS Library</strong>
            <small>Digitization workspace</small>
          </span>
        </NavLink>
        <nav aria-label="Điều hướng chính">
          <NavLink to="/" end>
            Tải lên
          </NavLink>
          <NavLink to="/dashboard">Dashboard OCR</NavLink>
          <NavLink to="/documents">Tài liệu</NavLink>
        </nav>
      </header>

      <Routes>
        <Route path="/" element={<UploadPage />} />
        <Route path="/dashboard" element={<DashboardPage />} />
        <Route path="/documents" element={<DocumentsPage />} />
        <Route path="/documents/:documentId" element={<DocumentViewerPage />} />
        <Route path="*" element={<Navigate to="/" replace />} />
      </Routes>
    </>
  )
}

export default App
