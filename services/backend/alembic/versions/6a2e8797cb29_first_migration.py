"""First migration

Revision ID: 6a2e8797cb29
Revises: 
Create Date: 2022-02-12 03:43:25.170880

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "6a2e8797cb29"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "template",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("created_at", sa.String(), nullable=True),
        sa.Column("name", sa.String(), nullable=True),
        sa.Column("content", sa.Text(), nullable=True),
        sa.Column("premium", sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_template_id"), "template", ["id"], unique=False)
    op.create_index(op.f("ix_template_name"), "template", ["name"], unique=False)
    op.create_index(op.f("ix_template_premium"), "template", ["premium"], unique=False)
    op.create_table(
        "user",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("created_at", sa.String(), nullable=True),
        sa.Column("username", sa.String(), nullable=True),
        sa.Column("password", sa.String(), nullable=True),
        sa.Column("is_admin", sa.Boolean(), nullable=True),
        sa.Column("is_premium", sa.Boolean(), nullable=True),
        sa.Column("template_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.ForeignKeyConstraint(
            ["template_id"],
            ["template.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_user_id"), "user", ["id"], unique=False)
    op.create_index(op.f("ix_user_password"), "user", ["password"], unique=False)
    op.create_index(op.f("ix_user_username"), "user", ["username"], unique=False)
    op.create_table(
        "userprofile",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("created_at", sa.String(), nullable=True),
        sa.Column("first_name", sa.String(), nullable=True),
        sa.Column("last_name", sa.String(), nullable=True),
        sa.Column("public_name", sa.String(), nullable=True),
        sa.Column("theme", sa.String(), nullable=True),
        sa.Column("summary", sa.String(), nullable=True),
        sa.Column("email", sa.String(), nullable=True),
        sa.Column("phone", sa.String(), nullable=True),
        sa.Column("designation", sa.String(), nullable=True),
        sa.Column("user_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_userprofile_id"), "userprofile", ["id"], unique=False)
    op.create_table(
        "certification",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("current", sa.Boolean(), nullable=True),
        sa.Column("deleted", sa.Boolean(), nullable=True),
        sa.Column("name", sa.String(), nullable=True),
        sa.Column("issuing_organization", sa.String(), nullable=True),
        sa.Column("issue_date", sa.String(), nullable=True),
        sa.Column("expiration_date", sa.String(), nullable=True),
        sa.Column("credential_id", sa.String(), nullable=True),
        sa.Column("credential_url", sa.String(), nullable=True),
        sa.Column("profile_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.ForeignKeyConstraint(
            ["profile_id"],
            ["userprofile.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_certification_id"), "certification", ["id"], unique=False)
    op.create_index(
        op.f("ix_certification_name"), "certification", ["name"], unique=False
    )
    op.create_table(
        "education",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("current", sa.Boolean(), nullable=True),
        sa.Column("deleted", sa.Boolean(), nullable=True),
        sa.Column("college", sa.String(), nullable=True),
        sa.Column("designation", sa.String(), nullable=True),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("startdate", sa.String(), nullable=True),
        sa.Column("enddate", sa.String(), nullable=True),
        sa.Column("profile_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.ForeignKeyConstraint(
            ["profile_id"],
            ["userprofile.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_education_college"), "education", ["college"], unique=False
    )
    op.create_index(op.f("ix_education_id"), "education", ["id"], unique=False)
    op.create_table(
        "job",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("current", sa.Boolean(), nullable=True),
        sa.Column("deleted", sa.Boolean(), nullable=True),
        sa.Column("company", sa.String(), nullable=True),
        sa.Column("designation", sa.String(), nullable=True),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("startdate", sa.String(), nullable=True),
        sa.Column("enddate", sa.String(), nullable=True),
        sa.Column("profile_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.ForeignKeyConstraint(
            ["profile_id"],
            ["userprofile.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_job_company"), "job", ["company"], unique=False)
    op.create_index(op.f("ix_job_designation"), "job", ["designation"], unique=False)
    op.create_index(op.f("ix_job_id"), "job", ["id"], unique=False)
    op.create_table(
        "skill",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("deleted", sa.Boolean(), nullable=True),
        sa.Column("name", sa.String(), nullable=True),
        sa.Column("learning", sa.Boolean(), nullable=True),
        sa.Column("profile_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.ForeignKeyConstraint(
            ["profile_id"],
            ["userprofile.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_skill_id"), "skill", ["id"], unique=False)
    op.create_index(op.f("ix_skill_name"), "skill", ["name"], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_skill_name"), table_name="skill")
    op.drop_index(op.f("ix_skill_id"), table_name="skill")
    op.drop_table("skill")
    op.drop_index(op.f("ix_job_id"), table_name="job")
    op.drop_index(op.f("ix_job_designation"), table_name="job")
    op.drop_index(op.f("ix_job_company"), table_name="job")
    op.drop_table("job")
    op.drop_index(op.f("ix_education_id"), table_name="education")
    op.drop_index(op.f("ix_education_college"), table_name="education")
    op.drop_table("education")
    op.drop_index(op.f("ix_certification_name"), table_name="certification")
    op.drop_index(op.f("ix_certification_id"), table_name="certification")
    op.drop_table("certification")
    op.drop_index(op.f("ix_userprofile_id"), table_name="userprofile")
    op.drop_table("userprofile")
    op.drop_index(op.f("ix_user_username"), table_name="user")
    op.drop_index(op.f("ix_user_password"), table_name="user")
    op.drop_index(op.f("ix_user_id"), table_name="user")
    op.drop_table("user")
    op.drop_index(op.f("ix_template_premium"), table_name="template")
    op.drop_index(op.f("ix_template_name"), table_name="template")
    op.drop_index(op.f("ix_template_id"), table_name="template")
    op.drop_table("template")
    # ### end Alembic commands ###
