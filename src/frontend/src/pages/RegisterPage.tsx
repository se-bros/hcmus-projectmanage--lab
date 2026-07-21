import { useState } from 'react'
import type { FormEvent } from 'react'
import { Link, useNavigate } from 'react-router'
import { registerUser } from '../services/api'
import { useAuth } from '../context/AuthContext'

export function RegisterPage() {
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [confirmPassword, setConfirmPassword] = useState('')
  const [isSubmitting, setIsSubmitting] = useState(false)
  const [error, setError] = useState('')
  const { setToken } = useAuth()
  const navigate = useNavigate()

  async function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault()
    if (password !== confirmPassword) {
      setError('Mật khẩu xác nhận không khớp.')
      return
    }

    setIsSubmitting(true)
    setError('')

    try {
      const { access_token: accessToken } = await registerUser(email, password)
      setToken(accessToken)
      navigate('/', { replace: true })
    } catch (registerError) {
      setError(
        registerError instanceof Error ? registerError.message : 'Không thể kết nối đến máy chủ.',
      )
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
            Tạo tài khoản,
            <br />
            bắt đầu số hóa.
          </h1>
          <p className="auth-hero-copy">
            Đăng ký bằng email trường để tải lên, biên tập và đọc tài liệu số hóa của thư viện
            HCMUS.
          </p>
        </div>
      </section>

      <section className="auth-panel">
        <div className="login-card" aria-labelledby="register-title">
          <header>
            <p className="eyebrow">Đăng ký</p>
            <h2 id="register-title">Tạo tài khoản mới</h2>
            <p className="intro">Chỉ chấp nhận email trường (vd. @hcmus.edu.vn).</p>
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
                minLength={8}
                value={password}
                onChange={(event) => setPassword(event.target.value)}
              />
            </label>
            <label>
              Xác nhận mật khẩu
              <input
                type="password"
                required
                minLength={8}
                value={confirmPassword}
                onChange={(event) => setConfirmPassword(event.target.value)}
              />
            </label>
            <button type="submit" disabled={isSubmitting}>
              {isSubmitting ? 'Đang đăng ký…' : 'Đăng ký'}
            </button>
          </form>

          {error && (
            <p className="message error" role="alert">
              {error}
            </p>
          )}

          <p className="login-hint">
            Đã có tài khoản? <Link to="/login">Đăng nhập</Link>
          </p>
        </div>
      </section>
    </main>
  )
}
