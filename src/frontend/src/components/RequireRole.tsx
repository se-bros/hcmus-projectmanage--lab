import type { ReactNode } from 'react'
import { Navigate } from 'react-router'
import { useAuth } from '../context/AuthContext'
import type { Role } from '../context/AuthContext'

export function RequireRole({ roles, children }: { roles: Role[]; children: ReactNode }) {
  const { role } = useAuth()
  if (!role || !roles.includes(role)) {
    return <Navigate to="/" replace />
  }
  return <>{children}</>
}
