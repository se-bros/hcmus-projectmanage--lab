import { useEffect } from 'react'
import { useNavigate, useSearchParams } from 'react-router'
import { useAuth } from '../context/AuthContext'

export function AuthCallbackPage() {
  const [searchParams] = useSearchParams()
  const { setToken } = useAuth()
  const navigate = useNavigate()

  useEffect(() => {
    const token = searchParams.get('token')
    if (token) {
      setToken(token)
      navigate('/', { replace: true })
    }
  }, [searchParams, setToken, navigate])

  return (
    <main className="page-shell login-page">
      <section className="upload-card login-card auth-callback-card" aria-live="polite">
        <div className="live-indicator">
          <span aria-hidden="true" />
          Đang xác thực
        </div>
        <p className="intro">Đang hoàn tất đăng nhập, vui lòng đợi trong giây lát…</p>
      </section>
    </main>
  )
}
