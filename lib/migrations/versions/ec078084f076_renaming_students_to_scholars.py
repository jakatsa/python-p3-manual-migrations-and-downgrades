"""Renaming students to scholars

Revision ID: ec078084f076
Revises: 791279dd0760
Create Date: 2024-03-24 06:34:30.518928

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ec078084f076'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')

def downgrade() -> None:
    op.rename_table('scholars', 'students')