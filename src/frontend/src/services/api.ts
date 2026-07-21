import { AUTH_TOKEN_STORAGE_KEY } from '../context/AuthContext'

const API_BASE = '/api'

export type DocumentDetail = {
  id: string
  original_filename: string
  content_type: string
  status: string
  title: string | null
  author: string | null
  shelf_location: string | null
  category_id: string | null
  epub_object_key: string | null
  created_at: string
}

export type OcrStatus = 'pending' | 'processing' | 'completed' | 'failed'

export type OcrJob = {
  job_id: string
  attempt: number
  status: OcrStatus
  error_message: string | null
  created_at?: string
  updated_at?: string
}

export type OcrDashboardItem = {
  document_id: string
  original_filename: string
  document_status: string
  job_id: string | null
  attempt: number | null
  ocr_status: OcrStatus | null
  error_message: string | null
  created_at: string
  updated_at: string | null
}

export type DocumentPage = {
  page_number: number
  text_content: string
  has_image: boolean
}

type ApiErrorBody = {
  detail?: string | { message?: string } | Array<{ loc?: Array<string | number>; msg?: string }>
}

export type AuthResponse = {
  access_token: string
  token_type: string
  role: 'reader' | 'editor' | 'admin'
}

async function request<T>(path: string, init?: RequestInit): Promise<T> {
  const token = window.localStorage.getItem(AUTH_TOKEN_STORAGE_KEY)
  const headers = new Headers(init?.headers)
  if (token) headers.set('Authorization', `Bearer ${token}`)

  const response = await fetch(`${API_BASE}${path}`, { ...init, headers })
  if (!response.ok) {
    let message = `Yêu cầu thất bại (${response.status}).`
    try {
      const body = (await response.json()) as ApiErrorBody
      if (typeof body.detail === 'string') message = body.detail
      else if (Array.isArray(body.detail)) {
        message = body.detail
          .map((error) => {
            const field = error.loc?.at(-1)
            return field ? `${field}: ${error.msg || 'không hợp lệ'}` : error.msg
          })
          .filter(Boolean)
          .join('; ')
      } else if (body.detail?.message) message = body.detail.message
    } catch {
      // Keep the status-based fallback when the response is not JSON.
    }
    throw new Error(message)
  }
  if (response.status === 204) return undefined as T
  return (await response.json()) as T
}

export async function uploadDocument(file: File): Promise<{ document_id: string }> {
  const formData = new FormData()
  formData.append('file', file)
  return request('/documents', { method: 'POST', body: formData })
}

export function getDocument(documentId: string): Promise<DocumentDetail> {
  return request(`/documents/${documentId}`)
}

export type DocumentMetadataInput = {
  title: string
  author: string
  shelf_location: string | null
  category_id: string | null
}

export function updateDocumentMetadata(
  documentId: string,
  metadata: DocumentMetadataInput,
): Promise<DocumentDetail> {
  return request(`/documents/${documentId}/metadata`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(metadata),
  })
}

export type Category = {
  id: string
  name: string
  parent_id: string | null
  created_at: string
  updated_at: string
}

export type CategoryTree = Category & { children: Category[] }

export function getCategories(): Promise<CategoryTree[]> {
  return request('/categories')
}

export function createCategory(name: string, parentId: string | null): Promise<Category> {
  return request('/categories', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ name, parent_id: parentId }),
  })
}

export function renameCategory(categoryId: string, name: string): Promise<Category> {
  return request(`/categories/${categoryId}`, {
    method: 'PATCH',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ name }),
  })
}

export function deleteCategory(categoryId: string): Promise<void> {
  return request(`/categories/${categoryId}`, { method: 'DELETE' })
}

export function getOcrStatus(documentId: string): Promise<OcrJob> {
  return request(`/documents/${documentId}/ocr`)
}

export function getOcrJobs(): Promise<OcrDashboardItem[]> {
  return request('/ocr/jobs')
}

export function getDocumentPages(documentId: string): Promise<DocumentPage[]> {
  return request(`/documents/${documentId}/pages`)
}

export function getDocumentPage(documentId: string, pageNumber: number): Promise<DocumentPage> {
  return request(`/documents/${documentId}/pages/${pageNumber}`)
}

export function updatePageText(
  documentId: string,
  pageNumber: number,
  textContent: string,
): Promise<DocumentPage> {
  return request(`/documents/${documentId}/pages/${pageNumber}`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ text_content: textContent }),
  })
}

export type ReaderContent = {
  document_id: string
  title: string
  author: string | null
  epub_url: string
  expires_in: number
}

export function getReaderContent(documentId: string): Promise<ReaderContent> {
  return request(`/documents/${documentId}/reader`)
}

export type SearchResult = {
  document_id: string
  title: string
  snippet: string
}

export function searchDocuments(query: string): Promise<SearchResult[]> {
  return request(`/search?q=${encodeURIComponent(query)}`)
}

export type Bookmark = {
  document_id: string
  location: string
  updated_at: string
}

export function getBookmark(documentId: string): Promise<Bookmark> {
  return request(`/documents/${documentId}/bookmark`)
}

export function saveBookmark(documentId: string, location: string): Promise<Bookmark> {
  return request(`/documents/${documentId}/bookmark`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ location }),
  })
}

export function getDocumentSourceUrl(documentId: string): string {
  return `${API_BASE}/documents/${documentId}/source`
}

export function getPageImageUrl(documentId: string, pageNumber: number): string {
  return `${API_BASE}/documents/${documentId}/pages/${pageNumber}/image`
}

export function retryOcr(documentId: string): Promise<OcrJob> {
  return request(`/documents/${documentId}/ocr`, { method: 'POST' })
}

export function registerUser(email: string, password: string): Promise<AuthResponse> {
  return request('/auth/register', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email, password }),
  })
}

export function loginUser(email: string, password: string): Promise<AuthResponse> {
  return request('/auth/login', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email, password }),
  })
}

export function logoutUser(): Promise<void> {
  return request('/auth/logout', { method: 'POST' })
}
