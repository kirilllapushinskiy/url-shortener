"""Added long_url unique constraint.

Revision ID: e4a95afff7d5
Revises: 7f43b7287a1e
Create Date: 2022-07-29 03:15:04.192760

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e4a95afff7d5'
down_revision = '7f43b7287a1e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(op.f('uqurlslong_url'), 'urls', ['long_url'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f('uqurlslong_url'), 'urls', type_='unique')
    # ### end Alembic commands ###
