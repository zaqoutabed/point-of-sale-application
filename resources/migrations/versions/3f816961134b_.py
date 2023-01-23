"""empty message

Revision ID: 3f816961134b
Revises: 71bad18d95cf
Create Date: 2023-01-23 14:33:56.299039

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3f816961134b'
down_revision = '71bad18d95cf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('sale_item', sa.Column('gross_profit_amount', sa.Numeric(precision=10, scale=4), nullable=True))
    op.add_column('sale_item', sa.Column('net_profit_amount', sa.Numeric(precision=10, scale=4), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('sale_item', 'net_profit_amount')
    op.drop_column('sale_item', 'gross_profit_amount')
    # ### end Alembic commands ###