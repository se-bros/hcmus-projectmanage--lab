"""merge document_tags and highlights migration branches

Revision ID: 20260814_0011
Revises: 20260722_0009, 20260812_0010
Create Date: 2026-08-14
"""

from collections.abc import Sequence

revision: str = "20260814_0011"
down_revision: str | Sequence[str] | None = ("20260722_0009", "20260812_0010")
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
