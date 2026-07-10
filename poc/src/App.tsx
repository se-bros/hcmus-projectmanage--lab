import { useState } from 'react'
import Navbar from './components/Navbar'
import LibrarianDashboard from './pages/LibrarianDashboard'
import StudentPortal from './pages/StudentPortal'
import EpubReader from './pages/EpubReader'
import type { Book } from './store/mockData'

export type View = 'librarian' | 'student' | 'reader'

function App() {
  const [view, setView] = useState<View>('student')
  const [selectedBook, setSelectedBook] = useState<Book | null>(null)

  const openReader = (book: Book) => {
    setSelectedBook(book)
    setView('reader')
  }

  const closeReader = () => {
    setView('student')
    setSelectedBook(null)
  }

  return (
    <div className="app">
      {view !== 'reader' && (
        <Navbar currentView={view} onChangeView={setView} />
      )}
      {view === 'librarian' && <LibrarianDashboard />}
      {view === 'student' && <StudentPortal onReadBook={openReader} />}
      {view === 'reader' && selectedBook && (
        <EpubReader book={selectedBook} onClose={closeReader} />
      )}
    </div>
  )
}

export default App
