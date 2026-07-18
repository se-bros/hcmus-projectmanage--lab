"""add full-text search GIN indexes (LDMS-015)

Revision ID: 20260717_0006
Revises: 20260716_0005
Create Date: 2026-07-17
"""

from collections.abc import Sequence

from alembic import op

revision: str = "20260717_0006"
down_revision: str | None = "20260716_0005"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    bind = op.get_bind()
    if bind.dialect.name != "postgresql":
        return
    op.execute(
        "CREATE INDEX ix_documents_fts ON documents "
        "USING gin (to_tsvector('simple', coalesce(title, '') || ' ' || coalesce(author, '')))"
    )
    op.execute("CREATE INDEX ix_pages_fts ON pages USING gin (to_tsvector('simple', text_content))")


def downgrade() -> None:
    bind = op.get_bind()
    if bind.dialect.name != "postgresql":
        return
    op.execute("DROP INDEX IF EXISTS ix_pages_fts")
    op.execute("DROP INDEX IF EXISTS ix_documents_fts")
