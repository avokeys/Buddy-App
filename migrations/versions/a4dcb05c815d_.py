"""empty message

Revision ID: a4dcb05c815d
Revises: d21ea237d6e4
Create Date: 2022-04-18 22:43:49.872696

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a4dcb05c815d'
down_revision = 'd21ea237d6e4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('category', 'img')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('category', sa.Column('img', sa.VARCHAR(length=120), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
