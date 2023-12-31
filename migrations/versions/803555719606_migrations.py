"""migrations

Revision ID: 803555719606
Revises: b78b241e92ff
Create Date: 2023-08-06 03:07:47.275876

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '803555719606'
down_revision = 'b78b241e92ff'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_post_files_id', table_name='post_files')
    op.drop_table('post_files')
    op.add_column('post_comments', sa.Column('approved', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post_comments', 'approved')
    op.create_table('post_files',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('post_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('image', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['post_comments.id'], name='post_files_post_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='post_files_pkey')
    )
    op.create_index('ix_post_files_id', 'post_files', ['id'], unique=False)
    # ### end Alembic commands ###
