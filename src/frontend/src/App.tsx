import { NavLink, Navigate, Route, Routes, useNavigate } from 'react-router'
import './App.css'
import { DashboardPage } from './pages/DashboardPage'
import { CategoriesPage } from './pages/CategoriesPage'
import { DocumentsPage } from './pages/DocumentsPage'
import { DocumentViewerPage } from './pages/DocumentViewerPage'
import { UploadPage } from './pages/UploadPage'
import { LoginPage } from './pages/LoginPage'
import { AuthCallbackPage } from './pages/AuthCallbackPage'
import { AuthProvider, useAuth } from './context/AuthContext'

function AuthNavItem() {
  const { token, clearToken } = useAuth()
  const navigate = useNavigate()

  if (!token) {
    return <NavLink to="/login">Đăng nhập</NavLink>
  }

  return (
    <button
      type="button"
      className="nav-logout"
      onClick={() => {
        clearToken()
        navigate('/login')
      }}
    >
      Đăng xuất
    </button>
  )
}

function App() {
  return (
    <AuthProvider>
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
          <NavLink to="/categories">Category</NavLink>
          <AuthNavItem />
        </nav>
      </header>

      <Routes>
        <Route path="/" element={<UploadPage />} />
        <Route path="/dashboard" element={<DashboardPage />} />
        <Route path="/documents" element={<DocumentsPage />} />
        <Route path="/documents/:documentId" element={<DocumentViewerPage />} />
        <Route path="/categories" element={<CategoriesPage />} />
        <Route path="/login" element={<LoginPage />} />
        <Route path="/auth/callback" element={<AuthCallbackPage />} />
        <Route path="*" element={<Navigate to="/" replace />} />
      </Routes>
    </AuthProvider>
  )
}

export default App
