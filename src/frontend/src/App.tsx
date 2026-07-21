import { NavLink, Navigate, Route, Routes, useNavigate } from 'react-router'
import './App.css'
import { DashboardPage } from './pages/DashboardPage'
import { CategoriesPage } from './pages/CategoriesPage'
import { DocumentsPage } from './pages/DocumentsPage'
import { DocumentViewerPage } from './pages/DocumentViewerPage'
import { UploadPage } from './pages/UploadPage'
import { LoginPage } from './pages/LoginPage'
import { RegisterPage } from './pages/RegisterPage'
import { AuthCallbackPage } from './pages/AuthCallbackPage'
import ReaderPage from './pages/ReaderPage'
import SearchPage from './pages/SearchPage'
import { AuthProvider, useAuth } from './context/AuthContext'
import { RequireRole } from './components/RequireRole'
import { logoutUser } from './services/api'

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
        void logoutUser().finally(() => {
          clearToken()
          navigate('/login')
        })
      }}
    >
      Đăng xuất
    </button>
  )
}

function RoleNavLinks() {
  const { role } = useAuth()

  return (
    <>
      {(role === 'editor' || role === 'admin') && <NavLink to="/dashboard">Dashboard OCR</NavLink>}
      <NavLink to="/documents">Tài liệu</NavLink>
      {role === 'admin' && <NavLink to="/categories">Category</NavLink>}
    </>
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
          <RoleNavLinks />
          <AuthNavItem />
        </nav>
      </header>

      <Routes>
        <Route path="/" element={<UploadPage />} />
        <Route
          path="/dashboard"
          element={
            <RequireRole roles={['editor', 'admin']}>
              <DashboardPage />
            </RequireRole>
          }
        />
        <Route path="/documents" element={<DocumentsPage />} />
        <Route path="/documents/:documentId" element={<DocumentViewerPage />} />
        <Route
          path="/categories"
          element={
            <RequireRole roles={['admin']}>
              <CategoriesPage />
            </RequireRole>
          }
        />
        <Route path="/login" element={<LoginPage />} />
        <Route path="/register" element={<RegisterPage />} />
        <Route path="/auth/callback" element={<AuthCallbackPage />} />
        <Route path="*" element={<Navigate to="/" replace />} />
      </Routes>
    </AuthProvider>
  )
}

export default App
