"""add document owner_id

Revision ID: 20260721_0007
Revises: 20260721_0006
Create Date: 2026-07-21
"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

revision: str = "20260721_0007"
down_revision: str | None = "20260721_0006"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.add_column("documents", sa.Column("owner_id", sa.Uuid(), nullable=True))


def downgrade() -> None:
    op.drop_column("documents", "owner_id")
