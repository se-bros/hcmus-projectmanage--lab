import { useEffect, useState } from 'react'
import { Link, useParams } from 'react-router'
import {
  getDocument,
  getCategories,
  getDocumentPages,
  getDocumentSourceUrl,
  getOcrStatus,
  getPageImageUrl,
  updatePageText,
  updateDocumentMetadata,
  getDocumentTags,
  addDocumentTag,
  deleteDocumentTag,
} from '../services/api'
import type { CategoryTree, DocumentDetail, DocumentPage, OcrJob } from '../services/api'
import { useAuth } from '../context/AuthContext'

export function DocumentViewerPage() {
  const { documentId } = useParams<{ documentId: string }>()
  const { role, userId } = useAuth()
  const [document, setDocument] = useState<DocumentDetail | null>(null)
  const [pages, setPages] = useState<DocumentPage[]>([])
  const [job, setJob] = useState<OcrJob | null>(null)
  const [selectedPageNumber, setSelectedPageNumber] = useState<number | null>(null)
  const [isLoading, setIsLoading] = useState(true)
  const [error, setError] = useState('')
  const [title, setTitle] = useState('')
  const [author, setAuthor] = useState('')
  const [shelfLocation, setShelfLocation] = useState('')
  const [metadataSaveState, setMetadataSaveState] = useState<'idle' | 'saving' | 'saved' | 'error'>(
    'idle',
  )
  const [metadataError, setMetadataError] = useState('')
  const [categories, setCategories] = useState<CategoryTree[]>([])
  const [categoryId, setCategoryId] = useState('')
  const [draftText, setDraftText] = useState('')
  const [pageSaveState, setPageSaveState] = useState<'idle' | 'saving' | 'saved' | 'error'>('idle')
  const [pageSaveError, setPageSaveError] = useState('')

  const [tags, setTags] = useState<string[]>([])
  const [newTag, setNewTag] = useState('')
  const [tagError, setTagError] = useState('')
  const [isAddingTag, setIsAddingTag] = useState(false)

  useEffect(() => {
    let cancelled = false
    if (!documentId) {
      setError('Document ID không hợp lệ.')
      setIsLoading(false)
      return
    }

    async function loadDocument() {
      try {
        const detail = await getDocument(documentId!)
        const [documentPages, ocrJob, categoryTree, docTags] = await Promise.all([
          getDocumentPages(documentId!),
          getOcrStatus(documentId!),
          getCategories().catch(() => []),
          getDocumentTags(documentId!).catch(() => []),
        ])
        if (cancelled) return
        setDocument(detail)
        setTitle(detail.title ?? '')
        setAuthor(detail.author ?? '')
        setShelfLocation(detail.shelf_location ?? '')
        setCategoryId(detail.category_id ?? '')
        setPages(documentPages)
        setJob(ocrJob)
        setCategories(categoryTree)
        setTags(docTags)
        setSelectedPageNumber(documentPages[0]?.page_number ?? null)
        setDraftText(documentPages[0]?.text_content ?? '')
        setError('')
      } catch (loadError) {
        if (!cancelled) {
          setError(
            loadError instanceof Error ? loadError.message : 'Không thể mở tài liệu đã scan.',
          )
        }
      } finally {
        if (!cancelled) setIsLoading(false)
      }
    }

    void loadDocument()
    return () => {
      cancelled = true
    }
  }, [documentId])

  const canEdit =
    role === 'admin' || (role === 'editor' && document !== null && document.owner_id === userId)

  const selectedPage = pages.find((page) => page.page_number === selectedPageNumber) ?? null
  const hasUnsavedPageText = selectedPage !== null && draftText !== selectedPage.text_content

  useEffect(() => {
    if (!hasUnsavedPageText) return
    function warnBeforeUnload(event: BeforeUnloadEvent) {
      event.preventDefault()
      event.returnValue = ''
    }
    window.addEventListener('beforeunload', warnBeforeUnload)
    return () => window.removeEventListener('beforeunload', warnBeforeUnload)
  }, [hasUnsavedPageText])

  function selectPage(pageNumber: number) {
    if (
      hasUnsavedPageText &&
      !window.confirm('Trang hiện tại có nội dung chưa lưu. Bỏ thay đổi và chuyển trang?')
    ) {
      return
    }
    const nextPage = pages.find((page) => page.page_number === pageNumber)
    setSelectedPageNumber(pageNumber)
    setDraftText(nextPage?.text_content ?? '')
    setPageSaveState('idle')
    setPageSaveError('')
  }

  async function savePageText() {
    if (!documentId || !selectedPage) return
    setPageSaveState('saving')
    setPageSaveError('')
    try {
      const updated = await updatePageText(documentId, selectedPage.page_number, draftText)
      setPages((current) =>
        current.map((page) => (page.page_number === updated.page_number ? updated : page)),
      )
      setDraftText(updated.text_content)
      setPageSaveState('saved')
    } catch (saveError) {
      setPageSaveState('error')
      setPageSaveError(
        saveError instanceof Error ? saveError.message : 'Không thể lưu nội dung trang.',
      )
    }
  }

  async function saveMetadata(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault()
    if (!documentId) return
    setMetadataSaveState('saving')
    setMetadataError('')
    try {
      const updated = await updateDocumentMetadata(documentId, {
        title,
        author,
        shelf_location: shelfLocation || null,
        category_id: categoryId || null,
      })
      setDocument(updated)
      setTitle(updated.title ?? '')
      setAuthor(updated.author ?? '')
      setShelfLocation(updated.shelf_location ?? '')
      setCategoryId(updated.category_id ?? '')
      setMetadataSaveState('saved')
    } catch (saveError) {
      setMetadataSaveState('error')
      setMetadataError(saveError instanceof Error ? saveError.message : 'Không thể lưu metadata.')
    }
  }

  async function handleAddTag(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault()
    if (!documentId || !newTag.trim()) return
    setIsAddingTag(true)
    setTagError('')
    try {
      const updatedTags = await addDocumentTag(documentId, newTag)
      setTags(updatedTags)
      setNewTag('')
    } catch (tagAddError) {
      setTagError(tagAddError instanceof Error ? tagAddError.message : 'Không thể thêm tag.')
    } finally {
      setIsAddingTag(false)
    }
  }

  async function handleRemoveTag(tagName: string) {
    if (!documentId) return
    setTagError('')
    try {
      const updatedTags = await deleteDocumentTag(documentId, tagName)
      setTags(updatedTags)
    } catch (tagRemoveError) {
      setTagError(tagRemoveError instanceof Error ? tagRemoveError.message : 'Không thể xóa tag.')
    }
  }

  if (isLoading) {
    return <main className="page-shell viewer-page viewer-state">Đang mở tài liệu…</main>
  }

  if (error || !document || !documentId) {
    return (
      <main className="page-shell viewer-page viewer-state">
        <p className="message error" role="alert">
          {error || 'Không tìm thấy tài liệu.'}
        </p>
        <Link className="secondary-link" to="/documents">
          ← Về danh sách
        </Link>
      </main>
    )
  }

  return (
    <main className="page-shell viewer-page">
      <header className="viewer-heading">
        <div>
          <Link className="back-link" to="/documents">
            ← Tài liệu đã scan
          </Link>
          <p className="eyebrow">Document viewer</p>
          <h1>{document.title || document.original_filename}</h1>
          <p className="viewer-subtitle">
            {document.author || 'Chưa có tác giả'} · {document.original_filename}
          </p>
        </div>
        <div className="viewer-actions">
          <span className={`status-badge status-${job?.status || 'pending'}`}>
            OCR {job?.status || document.status}
          </span>
          <a
            className="secondary-link"
            href={getDocumentSourceUrl(documentId)}
            target="_blank"
            rel="noreferrer"
          >
            Mở file gốc ↗
          </a>
        </div>
      </header>

      <section className="viewer-metadata" aria-label="Thông tin tài liệu">
        <div>
          <span>Document ID</span>
          <strong>{document.id}</strong>
        </div>
        <div>
          <span>Định dạng</span>
          <strong>{document.content_type}</strong>
        </div>
        <div>
          <span>Số trang xử lý</span>
          <strong>{pages.length}</strong>
        </div>
        <div>
          <span>Ngày tạo</span>
          <strong>{new Date(document.created_at).toLocaleDateString('vi-VN')}</strong>
        </div>
      </section>

      {canEdit && (
        <section className="metadata-editor" aria-labelledby="metadata-heading">
          <div>
            <p className="section-kicker">LDMS-011</p>
            <h2 id="metadata-heading">Metadata tài liệu</h2>
            <p>Title và author là bắt buộc trước khi xuất bản.</p>
          </div>
          <form onSubmit={saveMetadata}>
            <label>
              Title
              <input value={title} onChange={(event) => setTitle(event.target.value)} />
            </label>
            <label>
              Author
              <input value={author} onChange={(event) => setAuthor(event.target.value)} />
            </label>
            <label>
              Vị trí kệ (không bắt buộc)
              <input
                value={shelfLocation}
                onChange={(event) => setShelfLocation(event.target.value)}
              />
            </label>
            <label>
              Category (không bắt buộc)
              <select value={categoryId} onChange={(event) => setCategoryId(event.target.value)}>
                <option value="">Chưa gán category</option>
                {categories.map((category) => (
                  <optgroup label={category.name} key={category.id}>
                    <option value={category.id}>{category.name} — cấp 1</option>
                    {category.children.map((child) => (
                      <option value={child.id} key={child.id}>
                        {child.name} — cấp 2
                      </option>
                    ))}
                  </optgroup>
                ))}
              </select>
            </label>
            <div className="metadata-save-row">
              <button type="submit" disabled={metadataSaveState === 'saving'}>
                {metadataSaveState === 'saving' ? 'Đang lưu…' : 'Lưu metadata'}
              </button>
              <span
                className={metadataSaveState === 'error' ? 'save-state error-text' : 'save-state'}
                role="status"
              >
                {metadataSaveState === 'saved' && 'Đã lưu metadata.'}
                {metadataSaveState === 'error' && (metadataError || 'Lưu metadata thất bại.')}
              </span>
            </div>
          </form>
        </section>
      )}

      <section className="tags-section" aria-labelledby="tags-heading">
        <div>
          <p className="section-kicker">LDMS-023</p>
          <h2 id="tags-heading">Tags tài liệu</h2>
          <p>Gắn tag linh hoạt để hỗ trợ phân loại và tìm kiếm nhanh.</p>
        </div>
        <div className="tags-container">
          <div className="tags-list">
            {tags.length === 0 ? (
              <p className="no-tags">Chưa có tag nào.</p>
            ) : (
              tags.map((tag) => (
                <span key={tag} className="tag-badge">
                  <span className="tag-hash">#</span>
                  {tag}
                  {canEdit && (
                    <button
                      type="button"
                      aria-label={`Xóa tag ${tag}`}
                      className="remove-tag-btn"
                      onClick={() => handleRemoveTag(tag)}
                    >
                      ×
                    </button>
                  )}
                </span>
              ))
            )}
          </div>
          {canEdit && (
            <form onSubmit={handleAddTag} className="add-tag-form">
              <input
                type="text"
                placeholder="Nhập tag mới (ví dụ: lịch sử)..."
                value={newTag}
                onChange={(e) => setNewTag(e.target.value)}
                aria-label="Tên tag mới"
              />
              <button type="submit" disabled={isAddingTag || !newTag.trim()}>
                {isAddingTag ? 'Đang thêm…' : 'Thêm tag'}
              </button>
            </form>
          )}
          {tagError && (
            <p className="message error" role="alert">
              {tagError}
            </p>
          )}
        </div>
      </section>

      {pages.length === 0 ? (
        <section className="viewer-empty">
          <span aria-hidden="true">⌛</span>
          <h2>Chưa có trang đã xử lý</h2>
          <p>
            {job?.status === 'failed'
              ? job.error_message || 'OCR đã thất bại.'
              : 'OCR đang chạy; quay lại dashboard để theo dõi tiến trình.'}
          </p>
          <Link className="primary-link" to="/dashboard">
            Mở Dashboard OCR
          </Link>
        </section>
      ) : (
        <>
          <nav className="page-selector" aria-label="Chọn trang tài liệu">
            <span>Trang</span>
            <div>
              {pages.map((page) => (
                <button
                  type="button"
                  key={page.page_number}
                  className={selectedPageNumber === page.page_number ? 'active' : ''}
                  aria-current={selectedPageNumber === page.page_number ? 'page' : undefined}
                  onClick={() => selectPage(page.page_number)}
                >
                  {page.page_number}
                </button>
              ))}
            </div>
          </nav>

          {selectedPage && (
            <section
              className="scan-split-view"
              aria-label={`Nội dung trang ${selectedPage.page_number}`}
            >
              <article className="scan-pane">
                <header>
                  <span>Ảnh scan</span>
                  <strong>Trang {selectedPage.page_number}</strong>
                </header>
                <div className="scan-image-frame">
                  {selectedPage.has_image ? (
                    <img
                      src={getPageImageUrl(documentId, selectedPage.page_number)}
                      alt={`Ảnh scan trang ${selectedPage.page_number}`}
                    />
                  ) : (
                    <p>Trang này chưa có ảnh preview.</p>
                  )}
                </div>
              </article>
              <article className="processed-pane">
                <header>
                  <span>Văn bản OCR</span>
                  <strong>{draftText.length} ký tự</strong>
                </header>
                {canEdit ? (
                  <div className="page-text-editor">
                    <label className="sr-only" htmlFor="page-text-content">
                      Nội dung OCR trang {selectedPage.page_number}
                    </label>
                    <textarea
                      id="page-text-content"
                      value={draftText}
                      placeholder="Trang này chưa có nội dung OCR."
                      onChange={(event) => {
                        setDraftText(event.target.value)
                        setPageSaveState('idle')
                        setPageSaveError('')
                      }}
                    />
                    <footer className="page-save-row">
                      <button
                        type="button"
                        disabled={pageSaveState === 'saving'}
                        onClick={() => void savePageText()}
                      >
                        {pageSaveState === 'saving' ? 'Đang lưu…' : 'Lưu trang'}
                      </button>
                      <span
                        className={
                          pageSaveState === 'error' ? 'save-state error-text' : 'save-state'
                        }
                        role="status"
                      >
                        {pageSaveState === 'saved' && 'Đã lưu trang.'}
                        {pageSaveState === 'error' &&
                          (pageSaveError || 'Lưu nội dung trang thất bại.')}
                        {pageSaveState === 'idle' && hasUnsavedPageText && 'Có thay đổi chưa lưu.'}
                      </span>
                    </footer>
                  </div>
                ) : (
                  <div className="page-text-editor page-text-readonly">
                    <p>{draftText || 'Trang này chưa có nội dung OCR.'}</p>
                  </div>
                )}
              </article>
            </section>
          )}
        </>
      )}
    </main>
  )
}
