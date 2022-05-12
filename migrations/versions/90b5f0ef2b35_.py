"""empty message

Revision ID: 90b5f0ef2b35
Revises: a4dcb05c815d
Create Date: 2022-04-21 00:31:57.073537

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '90b5f0ef2b35'
down_revision = 'a4dcb05c815d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('selected_category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('task_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['task_id'], ['category.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('category', sa.Column('creative', sa.String(length=120), nullable=True))
    op.add_column('category', sa.Column('health', sa.String(length=120), nullable=True))
    op.add_column('category', sa.Column('professional', sa.String(length=120), nullable=True))
    op.add_column('category', sa.Column('school', sa.String(length=120), nullable=True))
    op.create_unique_constraint(None, 'category', ['health'])
    op.create_unique_constraint(None, 'category', ['professional'])
    op.create_unique_constraint(None, 'category', ['creative'])
    op.create_unique_constraint(None, 'category', ['school'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'category', type_='unique')
    op.drop_constraint(None, 'category', type_='unique')
    op.drop_constraint(None, 'category', type_='unique')
    op.drop_constraint(None, 'category', type_='unique')
    op.drop_column('category', 'school')
    op.drop_column('category', 'professional')
    op.drop_column('category', 'health')
    op.drop_column('category', 'creative')
    op.drop_table('selected_category')
    # ### end Alembic commands ###
