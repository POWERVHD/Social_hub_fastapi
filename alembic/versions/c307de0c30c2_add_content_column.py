"""add content column

Revision ID: c307de0c30c2
Revises: 6968fdc39981
Create Date: 2025-04-18 08:17:51.223206

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c307de0c30c2'
down_revision: Union[str, None] = '6968fdc39981'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() :
    """Upgrade schema."""
    op.add_column('posts',sa.Column('content',sa.String(),nullable=False))


def downgrade() :
    """Downgrade schema."""
    op.drop_column('posts','content')
