import { useEffect, useState } from 'react'
import type { FormEvent } from 'react'
import {
  changePassword,
  createRoleRequest,
  getMyRoleRequest,
  getProfile,
  updateProfile,
} from '../services/api'
import type { RoleRequestDetail, UserProfile } from '../services/api'

type Tab = 'profile' | 'request'

export function SettingsModal({ onClose }: { onClose: () => void }) {
  const [tab, setTab] = useState<Tab>('profile')
  const [profile, setProfile] = useState<UserProfile | null>(null)
  const [roleRequest, setRoleRequest] = useState<RoleRequestDetail | null>(null)
  const [isLoading, setIsLoading] = useState(true)
  const [loadError, setLoadError] = useState('')

  useEffect(() => {
    let cancelled = false
    Promise.all([getProfile(), getMyRoleRequest()])
      .then(([profileResult, requestResult]) => {
        if (cancelled) return
        setProfile(profileResult)
        setRoleRequest(requestResult)
      })
      .catch((error: unknown) => {
        if (!cancelled) {
          setLoadError(
            error instanceof Error ? error.message : 'Không thể tải thông tin tài khoản.',
          )
        }
      })
      .finally(() => {
        if (!cancelled) setIsLoading(false)
      })
    return () => {
      cancelled = true
    }
  }, [])

  useEffect(() => {
    function handleKeyDown(event: KeyboardEvent) {
      if (event.key === 'Escape') onClose()
    }
    document.addEventListener('keydown', handleKeyDown)
    return () => document.removeEventListener('keydown', handleKeyDown)
  }, [onClose])

  return (
    <div className="modal-backdrop" onClick={onClose}>
      <div
        className="modal-panel settings-modal"
        role="dialog"
        aria-modal="true"
        aria-labelledby="settings-title"
        onClick={(event) => event.stopPropagation()}
      >
        <header className="settings-modal-header">
          <h2 id="settings-title">Cài đặt</h2>
          <button type="button" className="modal-close" onClick={onClose} aria-label="Đóng">
            ✕
          </button>
        </header>

        <div className="settings-modal-body">
          <nav className="settings-tabs" aria-label="Tab cài đặt">
            <button
              type="button"
              className={tab === 'profile' ? 'active' : ''}
              onClick={() => setTab('profile')}
            >
              Hồ sơ
            </button>
            <button
              type="button"
              className={tab === 'request' ? 'active' : ''}
              onClick={() => setTab('request')}
            >
              Yêu cầu
            </button>
          </nav>

          <div className="settings-tab-content">
            {isLoading && <p className="muted-message">Đang tải…</p>}
            {loadError && (
              <p className="message error" role="alert">
                {loadError}
              </p>
            )}
            {!isLoading && !loadError && profile && tab === 'profile' && (
              <ProfileTab profile={profile} onProfileUpdate={setProfile} />
            )}
            {!isLoading && !loadError && profile && tab === 'request' && (
              <RequestTab
                profile={profile}
                roleRequest={roleRequest}
                onRequestChange={setRoleRequest}
              />
            )}
          </div>
        </div>
      </div>
    </div>
  )
}

function ProfileTab({
  profile,
  onProfileUpdate,
}: {
  profile: UserProfile
  onProfileUpdate: (profile: UserProfile) => void
}) {
  const [username, setUsername] = useState(profile.username ?? '')
  const [usernameState, setUsernameState] = useState<'idle' | 'saving' | 'saved' | 'error'>('idle')
  const [usernameError, setUsernameError] = useState('')

  const [currentPassword, setCurrentPassword] = useState('')
  const [newPassword, setNewPassword] = useState('')
  const [confirmPassword, setConfirmPassword] = useState('')
  const [passwordState, setPasswordState] = useState<'idle' | 'saving' | 'saved' | 'error'>('idle')
  const [passwordError, setPasswordError] = useState('')

  async function saveUsername(event: FormEvent<HTMLFormElement>) {
    event.preventDefault()
    setUsernameState('saving')
    setUsernameError('')
    try {
      const updated = await updateProfile(username)
      onProfileUpdate(updated)
      setUsernameState('saved')
    } catch (error) {
      setUsernameState('error')
      setUsernameError(error instanceof Error ? error.message : 'Không thể lưu username.')
    }
  }

  async function savePassword(event: FormEvent<HTMLFormElement>) {
    event.preventDefault()
    if (newPassword !== confirmPassword) {
      setPasswordState('error')
      setPasswordError('Mật khẩu xác nhận không khớp.')
      return
    }
    setPasswordState('saving')
    setPasswordError('')
    try {
      const updated = await changePassword(
        profile.has_password ? currentPassword : null,
        newPassword,
      )
      onProfileUpdate(updated)
      setCurrentPassword('')
      setNewPassword('')
      setConfirmPassword('')
      setPasswordState('saved')
    } catch (error) {
      setPasswordState('error')
      setPasswordError(error instanceof Error ? error.message : 'Không thể đổi mật khẩu.')
    }
  }

  return (
    <div className="settings-profile-tab">
      <section>
        <h3>Thông tin cá nhân</h3>
        <p className="muted-message">{profile.email ?? 'Tài khoản dev (mock)'}</p>
        <form onSubmit={saveUsername} className="local-auth-form">
          <label>
            Username
            <input value={username} onChange={(event) => setUsername(event.target.value)} />
          </label>
          <button type="submit" disabled={usernameState === 'saving'}>
            {usernameState === 'saving' ? 'Đang lưu…' : 'Lưu'}
          </button>
        </form>
        {usernameState === 'saved' && <p className="save-state">Đã lưu.</p>}
        {usernameState === 'error' && (
          <p className="message error" role="alert">
            {usernameError}
          </p>
        )}
      </section>

      <section>
        <h3>Đổi mật khẩu</h3>
        <form onSubmit={savePassword} className="local-auth-form">
          {profile.has_password && (
            <label>
              Mật khẩu hiện tại
              <input
                type="password"
                required
                value={currentPassword}
                onChange={(event) => setCurrentPassword(event.target.value)}
              />
            </label>
          )}
          <label>
            Mật khẩu mới
            <input
              type="password"
              required
              minLength={8}
              value={newPassword}
              onChange={(event) => setNewPassword(event.target.value)}
            />
          </label>
          <label>
            Xác nhận mật khẩu mới
            <input
              type="password"
              required
              minLength={8}
              value={confirmPassword}
              onChange={(event) => setConfirmPassword(event.target.value)}
            />
          </label>
          <button type="submit" disabled={passwordState === 'saving'}>
            {passwordState === 'saving' ? 'Đang lưu…' : 'Đổi mật khẩu'}
          </button>
        </form>
        {passwordState === 'saved' && <p className="save-state">Đã đổi mật khẩu.</p>}
        {passwordState === 'error' && (
          <p className="message error" role="alert">
            {passwordError}
          </p>
        )}
      </section>
    </div>
  )
}

function RequestTab({
  profile,
  roleRequest,
  onRequestChange,
}: {
  profile: UserProfile
  roleRequest: RoleRequestDetail | null
  onRequestChange: (request: RoleRequestDetail) => void
}) {
  const [isSubmitting, setIsSubmitting] = useState(false)
  const [error, setError] = useState('')

  async function submitRequest() {
    setIsSubmitting(true)
    setError('')
    try {
      const created = await createRoleRequest()
      onRequestChange(created)
    } catch (submitError) {
      setError(submitError instanceof Error ? submitError.message : 'Không thể gửi yêu cầu.')
    } finally {
      setIsSubmitting(false)
    }
  }

  if (profile.role !== 'reader') {
    return (
      <div className="settings-request-tab">
        <p>
          Bạn hiện có quyền <strong>{profile.role}</strong> — không cần gửi yêu cầu nâng quyền.
        </p>
      </div>
    )
  }

  return (
    <div className="settings-request-tab">
      <p>Gửi yêu cầu để quản trị viên xét duyệt nâng quyền từ reader lên editor.</p>
      {roleRequest?.status === 'pending' ? (
        <p className="status-badge status-pending">Yêu cầu đang chờ duyệt.</p>
      ) : (
        <>
          <button type="button" onClick={() => void submitRequest()} disabled={isSubmitting}>
            {isSubmitting ? 'Đang gửi…' : 'Yêu cầu trở thành Editor'}
          </button>
          {roleRequest?.status === 'rejected' && (
            <p className="muted-message">Yêu cầu trước đã bị từ chối. Bạn có thể gửi lại.</p>
          )}
        </>
      )}
      {error && (
        <p className="message error" role="alert">
          {error}
        </p>
      )}
    </div>
  )
}
