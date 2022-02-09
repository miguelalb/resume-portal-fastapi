"""Add Skills

Revision ID: 7c814369bfce
Revises: e508405ebf4e
Create Date: 2022-02-07 10:52:00.878748

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '7c814369bfce'
down_revision = 'e508405ebf4e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('skill',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('learning', sa.Boolean(), nullable=True),
    sa.Column('profile_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.ForeignKeyConstraint(['profile_id'], ['userprofile.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_skill_id'), 'skill', ['id'], unique=False)
    op.create_index(op.f('ix_skill_name'), 'skill', ['name'], unique=False)
    op.add_column('userprofile', sa.Column('theme', sa.String(), nullable=True))
    op.add_column('userprofile', sa.Column('summary', sa.String(), nullable=True))
    op.add_column('userprofile', sa.Column('email', sa.String(), nullable=True))
    op.add_column('userprofile', sa.Column('phone', sa.String(), nullable=True))
    op.add_column('userprofile', sa.Column('designation', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('userprofile', 'designation')
    op.drop_column('userprofile', 'phone')
    op.drop_column('userprofile', 'email')
    op.drop_column('userprofile', 'summary')
    op.drop_column('userprofile', 'theme')
    op.drop_index(op.f('ix_skill_name'), table_name='skill')
    op.drop_index(op.f('ix_skill_id'), table_name='skill')
    op.drop_table('skill')
    # ### end Alembic commands ###