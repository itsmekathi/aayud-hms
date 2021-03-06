"""add expenses and contact tables

Revision ID: 605e01be1d78
Revises: 127762c91e39
Create Date: 2020-02-25 10:50:09.635288

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '605e01be1d78'
down_revision = '127762c91e39'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('address_type_lu',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('description', sa.String(length=300), nullable=False),
    sa.Column('icon', sa.String(length=100), nullable=False),
    sa.Column('style_class', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('contact_type_lu',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('description', sa.String(length=300), nullable=False),
    sa.Column('icon', sa.String(length=100), nullable=False),
    sa.Column('style_class', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('expense_category_lu',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('description', sa.String(length=300), nullable=False),
    sa.Column('icon', sa.String(length=100), nullable=False),
    sa.Column('style_class', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('expense_type_lu',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('description', sa.String(length=300), nullable=False),
    sa.Column('icon', sa.String(length=100), nullable=False),
    sa.Column('style_class', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('unit_of_measurement_lu',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('description', sa.String(length=300), nullable=False),
    sa.Column('icon', sa.String(length=100), nullable=False),
    sa.Column('style_class', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('contacts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('contact_type_id', sa.Integer(), nullable=True),
    sa.Column('created_by_id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=100), nullable=False),
    sa.Column('middle_name', sa.String(length=100), nullable=True),
    sa.Column('last_name', sa.String(length=100), nullable=False),
    sa.Column('image_url', sa.String(length=200), nullable=True),
    sa.Column('email_id', sa.String(length=200), nullable=True),
    sa.Column('phone_number', sa.String(length=200), nullable=True),
    sa.Column('is_private', sa.Boolean(), nullable=True),
    sa.Column('created_on', sa.DateTime(), nullable=False),
    sa.Column('modified_on', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['contact_type_id'], ['contact_type_lu.id'], ),
    sa.ForeignKeyConstraint(['created_by_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('address',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('address_type_id', sa.Integer(), nullable=True),
    sa.Column('contact_id', sa.Integer(), nullable=False),
    sa.Column('created_by_id', sa.Integer(), nullable=False),
    sa.Column('address_line1', sa.String(length=200), nullable=False),
    sa.Column('address_line2', sa.String(length=200), nullable=False),
    sa.Column('address_line3', sa.String(length=200), nullable=False),
    sa.Column('city', sa.String(length=200), nullable=False),
    sa.Column('state', sa.String(length=200), nullable=False),
    sa.Column('country', sa.String(length=200), nullable=False),
    sa.Column('comments', sa.String(length=300), nullable=True),
    sa.Column('latitude', sa.String(length=100), nullable=True),
    sa.Column('longitude', sa.String(length=100), nullable=True),
    sa.Column('is_private', sa.Boolean(), nullable=True),
    sa.Column('created_on', sa.DateTime(), nullable=False),
    sa.Column('modified_on', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['address_type_id'], ['address_type_lu.id'], ),
    sa.ForeignKeyConstraint(['contact_id'], ['contacts.id'], ),
    sa.ForeignKeyConstraint(['created_by_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('expenses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('expense_type_id', sa.Integer(), nullable=True),
    sa.Column('expense_category_id', sa.Integer(), nullable=True),
    sa.Column('expenses_contact_id', sa.Integer(), nullable=True),
    sa.Column('created_by_id', sa.Integer(), nullable=False),
    sa.Column('expense_amount', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('expense_date_time', sa.DateTime(), nullable=False),
    sa.Column('description', sa.String(length=300), nullable=False),
    sa.Column('created_on', sa.DateTime(), nullable=False),
    sa.Column('modified_on', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['created_by_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['expense_category_id'], ['expense_category_lu.id'], ),
    sa.ForeignKeyConstraint(['expense_type_id'], ['expense_type_lu.id'], ),
    sa.ForeignKeyConstraint(['expenses_contact_id'], ['contacts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('expense_details',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('item_name', sa.String(length=200), nullable=False),
    sa.Column('expenses_id', sa.Integer(), nullable=False),
    sa.Column('uom_id', sa.Integer(), nullable=True),
    sa.Column('unit_price', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('quantity', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('gross_price', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('created_on', sa.DateTime(), nullable=False),
    sa.Column('modified_on', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['expenses_id'], ['expenses.id'], ),
    sa.ForeignKeyConstraint(['uom_id'], ['unit_of_measurement_lu.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('expense_details')
    op.drop_table('expenses')
    op.drop_table('address')
    op.drop_table('contacts')
    op.drop_table('unit_of_measurement_lu')
    op.drop_table('expense_type_lu')
    op.drop_table('expense_category_lu')
    op.drop_table('contact_type_lu')
    op.drop_table('address_type_lu')
    # ### end Alembic commands ###
