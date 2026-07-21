import { useEffect, useState } from 'react'
import { approveRoleRequest, declineRoleRequest, listRoleRequests } from '../services/api'
import type { RoleRequestDetail } from '../services/api'

const STATUS_LABELS: Record<RoleRequestDetail['status'], string> = {
  pending: 'Đang chờ',
  approved: 'Đã duyệt',
  rejected: 'Đã từ chối',
}

export function RequestsPage() {
  const [requests, setRequests] = useState<RoleRequestDetail[]>([])
  const [isLoading, setIsLoading] = useState(true)
  const [error, setError] = useState('')
  const [decidingId, setDecidingId] = useState<string | null>(null)

  useEffect(() => {
    let cancelled = false
    listRoleRequests()
      .then((result) => {
        if (!cancelled) setRequests(result)
      })
      .catch((loadError: unknown) => {
        if (!cancelled) {
          setError(
            loadError instanceof Error ? loadError.message : 'Không thể tải danh sách yêu cầu.',
          )
        }
      })
      .finally(() => {
        if (!cancelled) setIsLoading(false)
      })
    return () => {
      cancelled = true
    }
  }, [])

  async function decide(requestId: string, approve: boolean) {
    setDecidingId(requestId)
    setError('')
    try {
      const updated = approve
        ? await approveRoleRequest(requestId)
        : await declineRoleRequest(requestId)
      setRequests((current) =>
        current.map((request) => (request.id === requestId ? updated : request)),
      )
    } catch (decideError) {
      setError(decideError instanceof Error ? decideError.message : 'Không thể xử lý yêu cầu.')
    } finally {
      setDecidingId(null)
    }
  }

  return (
    <main className="page-shell requests-page">
      <header>
        <p className="eyebrow">Quản trị</p>
        <h1>Yêu cầu nâng quyền</h1>
        <p className="intro">Duyệt yêu cầu chuyển từ reader lên editor.</p>
      </header>

      {error && (
        <p className="message error" role="alert">
          {error}
        </p>
      )}
      {isLoading && <p className="library-state">Đang tải…</p>}

      {!isLoading && requests.length === 0 && <p className="library-state">Chưa có yêu cầu nào.</p>}

      {requests.length > 0 && (
        <table className="requests-table">
          <thead>
            <tr>
              <th>Người dùng</th>
              <th>Quyền yêu cầu</th>
              <th>Trạng thái</th>
              <th>Ngày gửi</th>
              <th aria-label="Hành động" />
            </tr>
          </thead>
          <tbody>
            {requests.map((request) => (
              <tr key={request.id}>
                <td>
                  <strong>{request.user_username || request.user_email}</strong>
                  <span className="requests-table-email">{request.user_email}</span>
                </td>
                <td>{request.requested_role}</td>
                <td>
                  <span className={`status-badge status-${request.status}`}>
                    {STATUS_LABELS[request.status]}
                  </span>
                </td>
                <td>{new Date(request.created_at).toLocaleDateString('vi-VN')}</td>
                <td>
                  {request.status === 'pending' && (
                    <div className="requests-actions">
                      <button
                        type="button"
                        disabled={decidingId === request.id}
                        onClick={() => void decide(request.id, true)}
                      >
                        Duyệt
                      </button>
                      <button
                        type="button"
                        className="danger-button"
                        disabled={decidingId === request.id}
                        onClick={() => void decide(request.id, false)}
                      >
                        Từ chối
                      </button>
                    </div>
                  )}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </main>
  )
}
