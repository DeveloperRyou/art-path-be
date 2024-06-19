"""initialize db

Revision ID: a65d06192325
Revises: 
Create Date: 2024-06-19 22:40:00.129852

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a65d06192325'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('routes',
    sa.Column('id', sa.Uuid(), autoincrement=False, nullable=False),
    sa.Column('name', sa.String(length=10), nullable=False),
    sa.Column('coordinates', sa.JSON(), nullable=False),
    sa.Column('distance', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.String(length=30), autoincrement=False, nullable=False),
    sa.Column('username', sa.String(length=30), nullable=False),
    sa.Column('profile_image', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('records',
    sa.Column('id', sa.Uuid(), autoincrement=False, nullable=False),
    sa.Column('name', sa.String(length=10), nullable=False),
    sa.Column('profile_image', sa.String(length=255), nullable=False),
    sa.Column('owner_id', sa.String(length=30), nullable=False),
    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('records')
    op.drop_table('users')
    op.drop_table('routes')
    # ### end Alembic commands ###