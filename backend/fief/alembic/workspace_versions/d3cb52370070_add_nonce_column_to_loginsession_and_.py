"""Add nonce column to LoginSession and AuthorizationCode

Revision ID: d3cb52370070
Revises: cfaa3c85d3d3
Create Date: 2022-03-25 15:53:14.719330

"""
import sqlalchemy as sa
from alembic import op

import fief

# revision identifiers, used by Alembic.
revision = "d3cb52370070"
down_revision = "cfaa3c85d3d3"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "fief_authorization_codes",
        sa.Column("nonce", sa.String(length=255), nullable=True),
    )
    op.add_column(
        "fief_login_sessions", sa.Column("nonce", sa.String(length=255), nullable=True)
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("fief_login_sessions", "nonce")
    op.drop_column("fief_authorization_codes", "nonce")
    # ### end Alembic commands ###
