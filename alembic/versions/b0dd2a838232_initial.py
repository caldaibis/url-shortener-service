"""Initial

Revision ID: b0dd2a838232
Revises: 
Create Date: 2023-11-03 12:14:34.990485

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'b0dd2a838232'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('urls',
        sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column('original', sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column('shortlink', sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column('hits', sa.INTEGER(), server_default=sa.text('0'), autoincrement=False, nullable=False),
        sa.Column('created_on', postgresql.TIMESTAMP(), server_default=sa.func.now(), autoincrement=False, nullable=False),
        sa.PrimaryKeyConstraint('id', name='urls_pkey')
    )

def downgrade() -> None:
    op.drop_table('urls')
