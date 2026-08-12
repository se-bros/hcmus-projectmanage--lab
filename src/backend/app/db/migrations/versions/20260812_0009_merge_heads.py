"""merge bookmarks and users migration branches

Revision ID: 20260812_0009
Revises: 20260717_0007, 20260721_0008
Create Date: 2026-08-12

Nhánh 20260717_0006/0007 (search + bookmarks) và nhánh 20260721_0006/0007/0008
(users + owner + profile) cùng tách ra từ 20260716_0005, để lại hai head khiến
`alembic upgrade head` không chạy được. Revision này chỉ gộp hai nhánh, không
thay đổi schema.
"""

from collections.abc import Sequence

revision: str = "20260812_0009"
down_revision: str | Sequence[str] | None = ("20260717_0007", "20260721_0008")
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
