import { useState } from 'react'
import { NavLink, Navigate, Route, Routes } from 'react-router'
import './App.css'
import { DashboardPage } from './pages/DashboardPage'
import { CategoriesPage } from './pages/CategoriesPage'
import { DocumentsPage } from './pages/DocumentsPage'
import { DocumentViewerPage } from './pages/DocumentViewerPage'
import ReaderPage from './pages/ReaderPage'
import { RequestsPage } from './pages/RequestsPage'
import { UploadPage } from './pages/UploadPage'
import { LoginPage } from './pages/LoginPage'
import { RegisterPage } from './pages/RegisterPage'
import { AuthCallbackPage } from './pages/AuthCallbackPage'
import { AuthProvider, useAuth } from './context/AuthContext'
import { RequireRole } from './components/RequireRole'
import { ProfileMenu } from './components/ProfileMenu'
import { SettingsModal } from './components/SettingsModal'

function AuthNavArea() {
  const { token } = useAuth()
  const [isSettingsOpen, setIsSettingsOpen] = useState(false)

  if (!token) {
    return <NavLink to="/login">Đăng nhập</NavLink>
  }

  return (
    <>
      <ProfileMenu onOpenSettings={() => setIsSettingsOpen(true)} />
      {isSettingsOpen && <SettingsModal onClose={() => setIsSettingsOpen(false)} />}
    </>
  )
}

function RoleNavLinks() {
  const { role } = useAuth()

  return (
    <>
      {(role === 'editor' || role === 'admin') && <NavLink to="/dashboard">Dashboard OCR</NavLink>}
      <NavLink to="/documents">Tài liệu</NavLink>
      {role === 'admin' && <NavLink to="/categories">Category</NavLink>}
      {role === 'admin' && <NavLink to="/requests">Yêu cầu</NavLink>}
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
          <AuthNavArea />
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
        <Route path="/reader/:documentId" element={<ReaderPage />} />
        <Route
          path="/categories"
          element={
            <RequireRole roles={['admin']}>
              <CategoriesPage />
            </RequireRole>
          }
        />
        <Route
          path="/requests"
          element={
            <RequireRole roles={['admin']}>
              <RequestsPage />
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
