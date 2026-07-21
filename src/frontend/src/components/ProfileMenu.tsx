import { useEffect, useRef, useState } from 'react'
import { useNavigate } from 'react-router'
import { useAuth } from '../context/AuthContext'
import { getProfile, logoutUser } from '../services/api'

export function ProfileMenu({ onOpenSettings }: { onOpenSettings: () => void }) {
  const { token, clearToken } = useAuth()
  const navigate = useNavigate()
  const [isOpen, setIsOpen] = useState(false)
  const [displayName, setDisplayName] = useState('user')
  const containerRef = useRef<HTMLDivElement>(null)

  useEffect(() => {
    let cancelled = false
    getProfile()
      .then((profile) => {
        if (!cancelled) setDisplayName(profile.username || 'user')
      })
      .catch(() => {
        if (!cancelled) setDisplayName('user')
      })
    return () => {
      cancelled = true
    }
  }, [token])

  useEffect(() => {
    if (!isOpen) return
    function handleClickOutside(event: MouseEvent) {
      if (containerRef.current && !containerRef.current.contains(event.target as Node)) {
        setIsOpen(false)
      }
    }
    document.addEventListener('mousedown', handleClickOutside)
    return () => document.removeEventListener('mousedown', handleClickOutside)
  }, [isOpen])

  function handleLogout() {
    setIsOpen(false)
    void logoutUser().finally(() => {
      clearToken()
      navigate('/login')
    })
  }

  return (
    <div className="profile-menu" ref={containerRef}>
      <button
        type="button"
        className="profile-menu-trigger"
        onClick={() => setIsOpen((open) => !open)}
        aria-haspopup="true"
        aria-expanded={isOpen}
      >
        {displayName}
        <span aria-hidden="true" className="profile-menu-caret">
          ▾
        </span>
      </button>
      {isOpen && (
        <div className="profile-menu-dropdown" role="menu">
          <button
            type="button"
            role="menuitem"
            onClick={() => {
              setIsOpen(false)
              onOpenSettings()
            }}
          >
            Cài đặt
          </button>
          <button type="button" role="menuitem" onClick={handleLogout}>
            Đăng xuất
          </button>
        </div>
      )}
    </div>
  )
}
