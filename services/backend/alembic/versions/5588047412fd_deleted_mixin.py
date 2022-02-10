"""Deleted mixin

Revision ID: 5588047412fd
Revises: 098a88825606
Create Date: 2022-02-10 04:00:46.747241

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5588047412fd'
down_revision = '098a88825606'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('certification', sa.Column('deleted', sa.Boolean(), nullable=True))
    op.add_column('education', sa.Column('deleted', sa.Boolean(), nullable=True))
    op.add_column('job', sa.Column('deleted', sa.Boolean(), nullable=True))
    op.add_column('skill', sa.Column('deleted', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('skill', 'deleted')
    op.drop_column('job', 'deleted')
    op.drop_column('education', 'deleted')
    op.drop_column('certification', 'deleted')
    # ### end Alembic commands ###
