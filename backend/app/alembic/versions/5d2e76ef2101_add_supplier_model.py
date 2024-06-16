"""Add supplier model

Revision ID: 5d2e76ef2101
Revises: 6b34dedcaa44
Create Date: 2024-06-11 13:17:41.362822

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel.sql.sqltypes


# revision identifiers, used by Alembic.
revision = '5d2e76ef2101'
down_revision = '6b34dedcaa44'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('supplier', sa.Column('address_1', sqlmodel.sql.sqltypes.AutoString(), nullable=False))
    op.add_column('supplier', sa.Column('address_town', sqlmodel.sql.sqltypes.AutoString(), nullable=False))
    op.add_column('supplier', sa.Column('address_postcode', sqlmodel.sql.sqltypes.AutoString(), nullable=False))
    op.add_column('supplier', sa.Column('created_on', sqlmodel.sql.sqltypes.AutoString(), nullable=True))
    op.add_column('supplier', sa.Column('modified_on', sqlmodel.sql.sqltypes.AutoString(), nullable=True))
    op.add_column('supplier', sa.Column('Email', sqlmodel.sql.sqltypes.AutoString(), nullable=False))
    op.add_column('supplier', sa.Column('Tel', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('supplier', 'Tel')
    op.drop_column('supplier', 'Email')
    op.drop_column('supplier', 'modified_on')
    op.drop_column('supplier', 'created_on')
    op.drop_column('supplier', 'address_postcode')
    op.drop_column('supplier', 'address_town')
    op.drop_column('supplier', 'address_1')
    # ### end Alembic commands ###