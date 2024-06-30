"""Add fields to referral

Revision ID: 0e3f5b4ac311
Revises: 823daaece31a
Create Date: 2024-06-20 21:48:33.480486

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel.sql.sqltypes


# revision identifiers, used by Alembic.
revision = '0e3f5b4ac311'
down_revision = '823daaece31a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('referral', sa.Column('daystohire', sa.Integer(), nullable=True))
    op.add_column('referral', sa.Column('creditrepair', sqlmodel.sql.sqltypes.AutoString(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('referral', 'creditrepair')
    op.drop_column('referral', 'daystohire')
    # ### end Alembic commands ###