export interface DocumentSummary {
  id: string
  title: string
  status: 'draft' | 'published'
  created_at: string
}

export interface DocumentContent {
  document_id: string
  text: string
}

export interface SearchResult {
  document_id: string
  title: string
  snippet: string
}

const API_BASE = '/api'

async function request<T>(path: string): Promise<T> {
  const response = await fetch(`${API_BASE}${path}`)
  if (!response.ok) {
    let detail = `Yêu cầu thất bại (${response.status})`
    try {
      const body = (await response.json()) as { detail?: string }
      if (body?.detail) {
        detail = body.detail
      }
    } catch {
      // Body không phải JSON — giữ nguyên message mặc định.
    }
    throw new Error(detail)
  }
  return (await response.json()) as T
}

export function getDocuments(): Promise<DocumentSummary[]> {
  return request<DocumentSummary[]>('/documents')
}

export function getDocumentContent(documentId: string): Promise<DocumentContent> {
  return request<DocumentContent>(`/reader/${encodeURIComponent(documentId)}`)
}

export function searchDocuments(query: string): Promise<SearchResult[]> {
  return request<SearchResult[]>(`/search?q=${encodeURIComponent(query)}`)
}
