"""Added long_url index.

Revision ID: 03ddd8934c96
Revises: e4a95afff7d5
Create Date: 2022-07-29 03:27:46.301730

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '03ddd8934c96'
down_revision = 'e4a95afff7d5'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('idx_long_url', 'urls', ['long_url'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('idx_long_url', table_name='urls')
    # ### end Alembic commands ###
