"""empty message

Revision ID: 068530fd11f3
Revises: c607195a9c96
Create Date: 2022-05-12 17:44:12.901745

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '068530fd11f3'
down_revision = 'c607195a9c96'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('fun_fact', sa.String(length=250), nullable=False))
    op.add_column('user', sa.Column('inspiration', sa.String(length=250), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'inspiration')
    op.drop_column('user', 'fun_fact')
    # ### end Alembic commands ###