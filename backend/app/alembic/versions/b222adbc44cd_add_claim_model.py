"""Add claim model

Revision ID: b222adbc44cd
Revises: 92f735e5195d
Create Date: 2024-06-11 20:10:26.975212

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel.sql.sqltypes


# revision identifiers, used by Alembic.
revision = 'b222adbc44cd'
down_revision = '92f735e5195d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('claim',
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('owner_id', sa.Integer(), nullable=False),
    sa.Column('client_firstname', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('client_lastname', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('client_address_1', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('client_address_town', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('client_address_postcode', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('client_vehicle_reg', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('client_insurer', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('client_insurer_policyno', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('client_phone', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('client_mobile', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('client_email', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('created_datetime', sa.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('updated_datetime', sa.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('plate_type', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('accident_date', sa.Date(), nullable=False),
    sa.Column('accident_time', sa.Time(), nullable=False),
    sa.Column('accident_location', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('accident_circs', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('tp_firstname', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('tp_lastname', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('tp_address_1', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('tp_address_town', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('tp_address_postcode', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('tp_vehicle_reg', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('tp_insurer', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('tp_insurer_polcyno', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('tp_phone', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('tp_mobile', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.ForeignKeyConstraint(['owner_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('claim')
    # ### end Alembic commands ###
