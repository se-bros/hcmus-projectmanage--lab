import type { Book } from './mockData'
import { mockBooks } from './mockData'

const API_BASE = 'http://localhost:8000'

export async function fetchBooks(q?: string, category?: string): Promise<Book[]> {
  try {
    const params = new URLSearchParams()
    if (q) params.set('q', q)
    if (category) params.set('category', category)
    const res = await fetch(`${API_BASE}/api/books?${params}`, { signal: AbortSignal.timeout(3000) })
    if (!res.ok) throw new Error('API error')
    const data = await res.json()
    return data as Book[]
  } catch {
    // Fallback: filter mock data locally
    console.warn('[LDMS] Backend offline — using mock data')
    const q2 = q?.toLowerCase() ?? ''
    return mockBooks.filter(b => {
      const matchCat = !category || b.category === category
      if (!q2) return matchCat
      return matchCat && (
        b.title.toLowerCase().includes(q2) ||
        b.author.toLowerCase().includes(q2) ||
        b.description.toLowerCase().includes(q2) ||
        b.content.toLowerCase().includes(q2)
      )
    })
  }
}

export async function fetchBook(id: string): Promise<Book | null> {
  try {
    const res = await fetch(`${API_BASE}/api/books/${id}`, { signal: AbortSignal.timeout(3000) })
    if (!res.ok) throw new Error('Not found')
    return await res.json() as Book
  } catch {
    return mockBooks.find(b => b.id === id) ?? null
  }
}

export async function publishBook(book: Book): Promise<boolean> {
  try {
    const res = await fetch(`${API_BASE}/api/books`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(book),
      signal: AbortSignal.timeout(5000),
    })
    return res.ok
  } catch {
    console.warn('[LDMS] Publish failed — backend offline')
    return false
  }
}
