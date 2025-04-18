""" adding foreign-key to post table

Revision ID: 7f1ba8989cfd
Revises: 0dd109e50b11
Create Date: 2025-04-18 08:32:30.102436

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7f1ba8989cfd'
down_revision: Union[str, None] = '0dd109e50b11'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts',sa.Column('owner_id',sa.Integer(),nullable=False))
    op.create_foreign_key('post_user_fk',source_table="posts",referent_table="users",
                          local_cols=['owner_id'],remote_cols=['id'],ondelete="CASCADE")


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint('post_user_fk',table_name="posts")
    op.drop_column('posts','owner_id')
