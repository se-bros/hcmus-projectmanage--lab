"""add document_tags table

Revision ID: 20260722_0009
Revises: 20260721_0008
Create Date: 2026-07-22
"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

revision: str = "20260722_0009"
down_revision: str | None = "20260721_0008"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table(
        "document_tags",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("document_id", sa.Uuid(), nullable=False),
        sa.Column("name", sa.String(length=128), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(["document_id"], ["documents.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("document_id", "name", name="uq_document_tags_document_id_name"),
    )
    op.create_index(op.f("ix_document_tags_document_id"), "document_tags", ["document_id"])
    op.create_index(op.f("ix_document_tags_name"), "document_tags", ["name"])


def downgrade() -> None:
    op.drop_index(op.f("ix_document_tags_name"), table_name="document_tags")
    op.drop_index(op.f("ix_document_tags_document_id"), table_name="document_tags")
    op.drop_table("document_tags")
