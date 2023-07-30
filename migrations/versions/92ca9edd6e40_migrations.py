"""migrations

Revision ID: 92ca9edd6e40
Revises: c7271c092c40
Create Date: 2023-07-30 16:42:27.429783

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '92ca9edd6e40'
down_revision = 'c7271c092c40'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('nombre', sa.String(), nullable=True))
    op.add_column('users', sa.Column('apellido', sa.String(), nullable=True))
    op.create_index(op.f('ix_users_apellido'), 'users', ['apellido'], unique=False)
    op.create_index(op.f('ix_users_nombre'), 'users', ['nombre'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_nombre'), table_name='users')
    op.drop_index(op.f('ix_users_apellido'), table_name='users')
    op.drop_column('users', 'apellido')
    op.drop_column('users', 'nombre')
    # ### end Alembic commands ###
