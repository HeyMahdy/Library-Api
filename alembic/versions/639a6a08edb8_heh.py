"""heh 

Revision ID: 639a6a08edb8
Revises: cf615a7a33c9
Create Date: 2024-12-27 01:59:43.359265

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '639a6a08edb8'
down_revision: Union[str, None] = 'cf615a7a33c9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() :

    op.drop_column('posts', 'mahdy')
    op.drop_column('posts', 'post_by')
    pass


def downgrade() -> None:
    pass
