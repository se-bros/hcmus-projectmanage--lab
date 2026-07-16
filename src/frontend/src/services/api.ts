const API_BASE = '/api'

export type DocumentDetail = {
  id: string
  original_filename: string
  status: string
  title: string | null
  author: string | null
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

type ApiErrorBody = {
  detail?: string | { message?: string }
}

async function request<T>(path: string, init?: RequestInit): Promise<T> {
  const response = await fetch(`${API_BASE}${path}`, init)
  if (!response.ok) {
    let message = `Yêu cầu thất bại (${response.status}).`
    try {
      const body = (await response.json()) as ApiErrorBody
      if (typeof body.detail === 'string') message = body.detail
      else if (body.detail?.message) message = body.detail.message
    } catch {
      // Keep the status-based fallback when the response is not JSON.
    }
    throw new Error(message)
  }
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

export function getOcrStatus(documentId: string): Promise<OcrJob> {
  return request(`/documents/${documentId}/ocr`)
}

export function getOcrJobs(): Promise<OcrDashboardItem[]> {
  return request('/ocr/jobs')
}

export function retryOcr(documentId: string): Promise<OcrJob> {
  return request(`/documents/${documentId}/ocr`, { method: 'POST' })
}
