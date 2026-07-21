import { useEffect, useRef, useState } from 'react'
import { useNavigate } from 'react-router'
import { useAuth } from '../context/AuthContext'
import { logoutUser } from '../services/api'

export function ProfileMenu({ onOpenSettings }: { onOpenSettings: () => void }) {
  const { clearToken } = useAuth()
  const navigate = useNavigate()
  const [isOpen, setIsOpen] = useState(false)
  const containerRef = useRef<HTMLDivElement>(null)

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
        Tài khoản
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
