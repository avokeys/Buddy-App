"""empty message

Revision ID: 438957aa172e
Revises: 3404c432e41a
Create Date: 2022-06-05 21:12:58.215108

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '438957aa172e'
down_revision = '3404c432e41a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('goal', sa.Column('is_done', sa.Boolean(), nullable=True))
    op.add_column('goal', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'goal', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'goal', type_='foreignkey')
    op.drop_column('goal', 'user_id')
    op.drop_column('goal', 'is_done')
    # ### end Alembic commands ###