"""Template to UserProfile

Revision ID: a3192f683f9e
Revises: 6a2e8797cb29
Create Date: 2022-02-23 09:24:16.642958

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "a3192f683f9e"
down_revision = "6a2e8797cb29"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint("user_template_id_fkey", "user", type_="foreignkey")
    op.drop_column("user", "template_id")
    op.add_column(
        "userprofile",
        sa.Column("template_id", postgresql.UUID(as_uuid=True), nullable=True),
    )
    op.create_foreign_key(None, "userprofile", "template", ["template_id"], ["id"])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "userprofile", type_="foreignkey")
    op.drop_column("userprofile", "template_id")
    op.add_column(
        "user",
        sa.Column("template_id", postgresql.UUID(), autoincrement=False, nullable=True),
    )
    op.create_foreign_key(
        "user_template_id_fkey", "user", "template", ["template_id"], ["id"]
    )
    # ### end Alembic commands ###