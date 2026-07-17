import '@testing-library/jest-dom/vitest'

// jsdom's window.localStorage is undefined under some Node versions that ship
// their own experimental global `localStorage` (shadows jsdom's Storage impl).
// Fall back to an in-memory Storage so localStorage-backed code is testable.
if (typeof window.localStorage?.getItem !== 'function') {
  class MemoryStorage implements Storage {
    private store = new Map<string, string>()

    get length(): number {
      return this.store.size
    }

    clear(): void {
      this.store.clear()
    }

    getItem(key: string): string | null {
      return this.store.has(key) ? (this.store.get(key) ?? null) : null
    }

    key(index: number): string | null {
      return Array.from(this.store.keys())[index] ?? null
    }

    removeItem(key: string): void {
      this.store.delete(key)
    }

    setItem(key: string, value: string): void {
      this.store.set(key, value)
    }
  }

  Object.defineProperty(window, 'localStorage', { value: new MemoryStorage() })
}
