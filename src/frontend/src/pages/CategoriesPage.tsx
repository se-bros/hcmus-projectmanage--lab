import { useEffect, useState } from 'react'
import {
  createCategory,
  deleteCategory,
  getCategories,
  renameCategory,
} from '../services/api'
import type { Category, CategoryTree } from '../services/api'

export function CategoriesPage() {
  const [categories, setCategories] = useState<CategoryTree[]>([])
  const [name, setName] = useState('')
  const [parentId, setParentId] = useState('')
  const [isLoading, setIsLoading] = useState(true)
  const [isSaving, setIsSaving] = useState(false)
  const [error, setError] = useState('')

  async function refresh() {
    try {
      setCategories(await getCategories())
      setError('')
    } catch (loadError) {
      setError(loadError instanceof Error ? loadError.message : 'Không thể tải category.')
    } finally {
      setIsLoading(false)
    }
  }

  useEffect(() => {
    void refresh()
  }, [])

  async function submit(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault()
    setIsSaving(true)
    setError('')
    try {
      await createCategory(name, parentId || null)
      setName('')
      setParentId('')
      await refresh()
    } catch (saveError) {
      setError(saveError instanceof Error ? saveError.message : 'Không thể tạo category.')
    } finally {
      setIsSaving(false)
    }
  }

  async function rename(category: Category) {
    const nextName = window.prompt('Tên category mới', category.name)
    if (nextName === null || nextName === category.name) return
    try {
      await renameCategory(category.id, nextName)
      await refresh()
    } catch (renameError) {
      setError(renameError instanceof Error ? renameError.message : 'Không thể đổi tên.')
    }
  }

  async function remove(category: Category) {
    if (!window.confirm(`Xóa category “${category.name}”?`)) return
    try {
      await deleteCategory(category.id)
      await refresh()
    } catch (deleteError) {
      setError(deleteError instanceof Error ? deleteError.message : 'Không thể xóa category.')
    }
  }

  function row(category: Category, isChild = false) {
    return (
      <li className={isChild ? 'category-row category-child' : 'category-row'} key={category.id}>
        <span>
          {isChild && <i aria-hidden="true">↳</i>}
          <strong>{category.name}</strong>
          <small>{isChild ? 'Cấp 2' : 'Cấp 1'}</small>
        </span>
        <span className="category-actions">
          <button className="secondary-button" type="button" onClick={() => void rename(category)}>
            Đổi tên {category.name}
          </button>
          <button className="danger-button" type="button" onClick={() => void remove(category)}>
            Xóa {category.name}
          </button>
        </span>
      </li>
    )
  }

  return (
    <main className="page-shell categories-page">
      <header className="categories-heading">
        <div>
          <p className="eyebrow">LDMS-012</p>
          <h1>Category</h1>
          <p className="intro">Quản lý cây danh mục tối đa hai cấp cho tài liệu thư viện.</p>
        </div>
      </header>

      <section className="category-create-card" aria-labelledby="category-create-heading">
        <h2 id="category-create-heading">Tạo category</h2>
        <form onSubmit={submit}>
          <label>
            Tên category
            <input value={name} onChange={(event) => setName(event.target.value)} />
          </label>
          <label>
            Category cha
            <select value={parentId} onChange={(event) => setParentId(event.target.value)}>
              <option value="">Không có — tạo cấp 1</option>
              {categories.map((category) => (
                <option value={category.id} key={category.id}>
                  {category.name}
                </option>
              ))}
            </select>
          </label>
          <button type="submit" disabled={isSaving}>
            {isSaving ? 'Đang tạo…' : 'Tạo category'}
          </button>
        </form>
      </section>

      {error && (
        <p className="message error" role="alert">
          {error}
        </p>
      )}

      <section className="category-tree-card" aria-labelledby="category-tree-heading">
        <h2 id="category-tree-heading">Cây category</h2>
        {isLoading ? (
          <p>Đang tải category…</p>
        ) : categories.length === 0 ? (
          <p>Chưa có category.</p>
        ) : (
          <ul className="category-tree">
            {categories.flatMap((category) => [
              row(category),
              ...category.children.map((child) => row(child, true)),
            ])}
          </ul>
        )}
      </section>
    </main>
  )
}
