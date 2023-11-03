"""Rename shortlink to hashcode

Revision ID: 2712f5ebae4e
Revises: b0dd2a838232
Create Date: 2023-11-03 14:54:20.687639

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2712f5ebae4e'
down_revision: Union[str, None] = 'b0dd2a838232'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column('urls', 'shortlink', new_column_name='hashcode', existing_type=sa.String())



def downgrade() -> None:
    op.alter_column('urls', 'hashcode', new_column_name='shortlink', existing_type=sa.String())
