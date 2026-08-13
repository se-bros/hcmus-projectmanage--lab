"""add highlights table (LDMS-021)

Revision ID: 20260812_0010
Revises: 20260812_0009
Create Date: 2026-08-12
"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

revision: str = "20260812_0010"
down_revision: str | None = "20260812_0009"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table(
        "highlights",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("document_id", sa.Uuid(), nullable=False),
        sa.Column("user_sub", sa.String(length=255), nullable=False),
        sa.Column("cfi_range", sa.Text(), nullable=False),
        sa.Column("selected_text", sa.Text(), nullable=False),
        sa.Column("note", sa.Text(), nullable=True),
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
    )
    op.create_index(op.f("ix_highlights_document_id"), "highlights", ["document_id"])
    op.create_index(op.f("ix_highlights_user_sub"), "highlights", ["user_sub"])
    op.create_index("ix_highlights_document_user", "highlights", ["document_id", "user_sub"])


def downgrade() -> None:
    op.drop_index("ix_highlights_document_user", table_name="highlights")
    op.drop_index(op.f("ix_highlights_user_sub"), table_name="highlights")
    op.drop_index(op.f("ix_highlights_document_id"), table_name="highlights")
    op.drop_table("highlights")
