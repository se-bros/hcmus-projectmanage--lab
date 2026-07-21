import { createContext, useContext, useMemo, useState, type ReactNode } from 'react'

export const AUTH_TOKEN_STORAGE_KEY = 'ldms_token'

export type Role = 'reader' | 'editor' | 'admin'

type TokenPayload = {
  sub: string
  role: Role
}

function decodeTokenPayload(token: string): TokenPayload | null {
  try {
    const segment = token.split('.')[1]
    if (!segment) return null
    const normalized = segment.replace(/-/g, '+').replace(/_/g, '/')
    const padded = normalized.padEnd(normalized.length + ((4 - (normalized.length % 4)) % 4), '=')
    const payload: unknown = JSON.parse(atob(padded))
    if (
      typeof payload !== 'object' ||
      payload === null ||
      typeof (payload as { sub?: unknown }).sub !== 'string' ||
      typeof (payload as { role?: unknown }).role !== 'string'
    ) {
      return null
    }
    return { sub: (payload as { sub: string }).sub, role: (payload as { role: Role }).role }
  } catch {
    return null
  }
}

type AuthContextValue = {
  token: string | null
  role: Role | null
  userId: string | null
  setToken: (token: string) => void
  clearToken: () => void
}

const AuthContext = createContext<AuthContextValue | undefined>(undefined)

export function AuthProvider({ children }: { children: ReactNode }) {
  const [token, setTokenState] = useState<string | null>(() =>
    window.localStorage.getItem(AUTH_TOKEN_STORAGE_KEY),
  )

  const value = useMemo<AuthContextValue>(() => {
    const payload = token ? decodeTokenPayload(token) : null
    return {
      token,
      role: payload?.role ?? null,
      userId: payload?.sub ?? null,
      setToken: (next: string) => {
        window.localStorage.setItem(AUTH_TOKEN_STORAGE_KEY, next)
        setTokenState(next)
      },
      clearToken: () => {
        window.localStorage.removeItem(AUTH_TOKEN_STORAGE_KEY)
        setTokenState(null)
      },
    }
  }, [token])

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>
}

export function useAuth(): AuthContextValue {
  const context = useContext(AuthContext)
  if (!context) throw new Error('useAuth must be used within AuthProvider')
  return context
}
