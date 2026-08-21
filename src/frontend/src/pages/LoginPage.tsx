import { useState } from 'react'
import type { FormEvent } from 'react'
import { Link, useNavigate } from 'react-router'
import { API_BASE, loginUser } from '../services/api'
import { useAuth } from '../context/AuthContext'

function GoogleIcon() {
  return (
    <svg width="18" height="18" viewBox="0 0 18 18" aria-hidden="true">
      <path
        fill="#4285F4"
        d="M17.64 9.2c0-.637-.057-1.251-.164-1.84H9v3.481h4.844a4.14 4.14 0 0 1-1.796 2.716v2.259h2.908c1.702-1.567 2.684-3.874 2.684-6.615z"
      />
      <path
        fill="#34A853"
        d="M9 18c2.43 0 4.467-.806 5.956-2.184l-2.908-2.259c-.806.54-1.837.86-3.048.86-2.344 0-4.328-1.584-5.036-3.711H.957v2.332A8.997 8.997 0 0 0 9 18z"
      />
      <path
        fill="#FBBC05"
        d="M3.964 10.706A5.41 5.41 0 0 1 3.682 9c0-.593.102-1.17.282-1.706V4.962H.957A8.996 8.996 0 0 0 0 9c0 1.452.348 2.827.957 4.038l3.007-2.332z"
      />
      <path
        fill="#EA4335"
        d="M9 3.58c1.321 0 2.508.454 3.44 1.345l2.582-2.58C13.463.891 11.426 0 9 0A8.997 8.997 0 0 0 .957 4.962L3.964 7.294C4.672 5.167 6.656 3.58 9 3.58z"
      />
    </svg>
  )
}

const HIGHLIGHTS = [
  'Tra cứu toàn văn tức thì trên toàn bộ kho tài liệu',
  'Đọc sách bảo mật trên mọi thiết bị, không giới hạn',
  'Biên tập song song ảnh scan và văn bản OCR',
]

export function LoginPage() {
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [isSubmitting, setIsSubmitting] = useState(false)
  const [error, setError] = useState('')
  const { setToken } = useAuth()
  const navigate = useNavigate()

  async function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault()
    setIsSubmitting(true)
    setError('')

    try {
      const { access_token: accessToken } = await loginUser(email, password)
      setToken(accessToken)
      navigate('/', { replace: true })
    } catch (loginError) {
      setError(loginError instanceof Error ? loginError.message : 'Không thể kết nối đến máy chủ.')
    } finally {
      setIsSubmitting(false)
    }
  }

  return (
    <main className="auth-shell">
      <section className="auth-hero">
        <div className="auth-hero-glow" aria-hidden="true" />
        <div className="auth-hero-content">
          <p className="eyebrow auth-hero-eyebrow">HCMUS Library</p>
          <h1 className="auth-hero-title">
            Số hóa tri thức,
            <br />
            lưu giữ trăm năm.
          </h1>
          <p className="auth-hero-copy">
            Nền tảng quản lý và số hóa tài liệu thư viện HCMUS — tra cứu, biên tập và đọc sách trực
            tuyến trong một không gian duy nhất.
          </p>
          <ul className="auth-hero-list">
            {HIGHLIGHTS.map((item) => (
              <li key={item}>
                <span aria-hidden="true">✓</span>
                {item}
              </li>
            ))}
          </ul>
        </div>
      </section>

      <section className="auth-panel">
        <div className="login-card" aria-labelledby="login-title">
          <header>
            <p className="eyebrow">Đăng nhập</p>
            <h2 id="login-title">Chào mừng trở lại</h2>
            <p className="intro">Đăng nhập bằng email hoặc tài khoản Google trường.</p>
          </header>

          <form className="local-auth-form" onSubmit={handleSubmit}>
            <label>
              Email
              <input
                type="email"
                required
                value={email}
                onChange={(event) => setEmail(event.target.value)}
              />
            </label>
            <label>
              Mật khẩu
              <input
                type="password"
                required
                value={password}
                onChange={(event) => setPassword(event.target.value)}
              />
            </label>
            <button type="submit" disabled={isSubmitting}>
              {isSubmitting ? 'Đang đăng nhập…' : 'Đăng nhập'}
            </button>
          </form>

          {error && (
            <p className="message error" role="alert">
              {error}
            </p>
          )}

          <p className="login-hint">
            Chưa có tài khoản? <Link to="/register">Đăng ký</Link>
          </p>

          <div className="auth-divider" role="separator">
            <span>hoặc</span>
          </div>

          <a className="google-button" href={`${API_BASE}/auth/login/google`}>
            <GoogleIcon />
            <span>Đăng nhập với Google</span>
          </a>

          <p className="login-hint">
            Chỉ chấp nhận email trường (vd. <code>@hcmus.edu.vn</code>,{' '}
            <code>@clc.fitus.edu.vn</code>). Tài khoản thuộc domain khác sẽ bị từ chối sau bước xác
            thực.
          </p>
        </div>
      </section>
    </main>
  )
}
