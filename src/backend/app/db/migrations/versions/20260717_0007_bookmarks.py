"""add bookmarks table (LDMS-020)

Revision ID: 20260717_0007
Revises: 20260717_0006
Create Date: 2026-07-17
"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

revision: str = "20260717_0007"
down_revision: str | None = "20260717_0006"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table(
        "bookmarks",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("document_id", sa.Uuid(), nullable=False),
        sa.Column("user_sub", sa.String(length=255), nullable=False),
        sa.Column("location", sa.Text(), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(["document_id"], ["documents.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("document_id", "user_sub"),
    )
    op.create_index(op.f("ix_bookmarks_document_id"), "bookmarks", ["document_id"])
    op.create_index(op.f("ix_bookmarks_user_sub"), "bookmarks", ["user_sub"])


def downgrade() -> None:
    op.drop_index(op.f("ix_bookmarks_user_sub"), table_name="bookmarks")
    op.drop_index(op.f("ix_bookmarks_document_id"), table_name="bookmarks")
    op.drop_table("bookmarks")
