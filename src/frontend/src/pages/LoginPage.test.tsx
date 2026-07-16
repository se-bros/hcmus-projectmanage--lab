import { render, screen } from '@testing-library/react'
import { describe, expect, it } from 'vitest'
import { LoginPage } from './LoginPage'

describe('LoginPage', () => {
  it('links to the backend Google login redirect', () => {
    render(<LoginPage />)
    const link = screen.getByRole('link', { name: 'Đăng nhập với Google' })
    expect(link).toHaveAttribute('href', '/api/auth/login/google')
  })
})
