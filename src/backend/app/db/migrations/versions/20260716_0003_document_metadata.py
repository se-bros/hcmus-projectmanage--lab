"""add document metadata fields

Revision ID: 20260716_0003
Revises: 20260716_0002
Create Date: 2026-07-16
"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

revision: str = "20260716_0003"
down_revision: str | None = "20260716_0002"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.add_column("documents", sa.Column("shelf_location", sa.String(length=255), nullable=True))
    op.add_column("documents", sa.Column("category_id", sa.Uuid(), nullable=True))
    op.create_index(op.f("ix_documents_category_id"), "documents", ["category_id"])


def downgrade() -> None:
    op.drop_index(op.f("ix_documents_category_id"), table_name="documents")
    op.drop_column("documents", "category_id")
    op.drop_column("documents", "shelf_location")
