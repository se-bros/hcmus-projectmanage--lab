"""add OCR pages and publish jobs

Revision ID: 20260716_0002
Revises: 20260716_0001
Create Date: 2026-07-16
"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

revision: str = "20260716_0002"
down_revision: str | None = "20260716_0001"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def _timestamps() -> list[sa.Column]:
    return [
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
    ]


def upgrade() -> None:
    op.add_column("documents", sa.Column("content_type", sa.String(length=128), nullable=True))
    op.execute("UPDATE documents SET content_type = 'application/octet-stream'")
    op.alter_column("documents", "content_type", nullable=False)
    op.add_column("documents", sa.Column("title", sa.String(length=512), nullable=True))
    op.add_column("documents", sa.Column("author", sa.String(length=512), nullable=True))
    op.add_column("documents", sa.Column("epub_object_key", sa.String(length=512), nullable=True))

    op.create_table(
        "ocr_jobs",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("document_id", sa.Uuid(), nullable=False),
        sa.Column("attempt", sa.Integer(), nullable=False),
        sa.Column("status", sa.String(length=32), server_default="pending", nullable=False),
        sa.Column("error_message", sa.Text(), nullable=True),
        *_timestamps(),
        sa.ForeignKeyConstraint(["document_id"], ["documents.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_ocr_jobs_document_id"), "ocr_jobs", ["document_id"])

    op.create_table(
        "pages",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("document_id", sa.Uuid(), nullable=False),
        sa.Column("page_number", sa.Integer(), nullable=False),
        sa.Column("text_content", sa.Text(), nullable=False),
        sa.Column("image_object_key", sa.String(length=512), nullable=True),
        *_timestamps(),
        sa.ForeignKeyConstraint(["document_id"], ["documents.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("document_id", "page_number"),
    )
    op.create_index(op.f("ix_pages_document_id"), "pages", ["document_id"])

    op.create_table(
        "publish_jobs",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("document_id", sa.Uuid(), nullable=False),
        sa.Column("attempt", sa.Integer(), nullable=False),
        sa.Column("status", sa.String(length=32), server_default="pending", nullable=False),
        sa.Column("error_message", sa.Text(), nullable=True),
        *_timestamps(),
        sa.ForeignKeyConstraint(["document_id"], ["documents.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_publish_jobs_document_id"), "publish_jobs", ["document_id"])


def downgrade() -> None:
    op.drop_index(op.f("ix_publish_jobs_document_id"), table_name="publish_jobs")
    op.drop_table("publish_jobs")
    op.drop_index(op.f("ix_pages_document_id"), table_name="pages")
    op.drop_table("pages")
    op.drop_index(op.f("ix_ocr_jobs_document_id"), table_name="ocr_jobs")
    op.drop_table("ocr_jobs")
    op.drop_column("documents", "epub_object_key")
    op.drop_column("documents", "author")
    op.drop_column("documents", "title")
    op.drop_column("documents", "content_type")
