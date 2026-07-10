import type { View } from '../App'
import { BookOpen, LayoutDashboard, Library } from 'lucide-react'

interface NavbarProps {
  currentView: View
  onChangeView: (view: View) => void
}

export default function Navbar({ currentView, onChangeView }: NavbarProps) {
  return (
    <nav className="navbar">
      <div className="navbar-brand">
        <BookOpen size={24} strokeWidth={2} />
        <span className="navbar-title">HCMUS-LDMS</span>
        <span className="navbar-subtitle">Thư viện Số</span>
      </div>
      <div className="navbar-tabs">
        <button
          className={`nav-tab ${currentView === 'student' ? 'active' : ''}`}
          onClick={() => onChangeView('student')}
        >
          <Library size={16} />
          Tra cứu & Đọc sách
        </button>
        <button
          className={`nav-tab ${currentView === 'librarian' ? 'active' : ''}`}
          onClick={() => onChangeView('librarian')}
        >
          <LayoutDashboard size={16} />
          Dashboard Thủ thư
        </button>
      </div>
      <div className="navbar-badge">PoC Demo v1.0</div>
    </nav>
  )
}
