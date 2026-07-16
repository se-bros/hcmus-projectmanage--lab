import { createContext, useContext, useMemo, useState, type ReactNode } from 'react'

export const AUTH_TOKEN_STORAGE_KEY = 'ldms_token'

type AuthContextValue = {
  token: string | null
  setToken: (token: string) => void
  clearToken: () => void
}

const AuthContext = createContext<AuthContextValue | undefined>(undefined)

export function AuthProvider({ children }: { children: ReactNode }) {
  const [token, setTokenState] = useState<string | null>(() =>
    window.localStorage.getItem(AUTH_TOKEN_STORAGE_KEY),
  )

  const value = useMemo<AuthContextValue>(
    () => ({
      token,
      setToken: (next: string) => {
        window.localStorage.setItem(AUTH_TOKEN_STORAGE_KEY, next)
        setTokenState(next)
      },
      clearToken: () => {
        window.localStorage.removeItem(AUTH_TOKEN_STORAGE_KEY)
        setTokenState(null)
      },
    }),
    [token],
  )

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>
}

export function useAuth(): AuthContextValue {
  const context = useContext(AuthContext)
  if (!context) throw new Error('useAuth must be used within AuthProvider')
  return context
}
