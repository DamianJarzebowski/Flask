"""empty message

Revision ID: 12c10700be78
Revises: f5cd39874a1a
Create Date: 2024-02-02 15:05:12.583677

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '12c10700be78'
down_revision = 'f5cd39874a1a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.add_column(sa.Column('description', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.drop_column('description')

    # ### end Alembic commands ###
