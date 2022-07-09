"""fix test mistake

Revision ID: 5a18c0afb134
Revises: e63187ef549b
Create Date: 2022-07-09 00:07:11.182199

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5a18c0afb134'
down_revision = 'e63187ef549b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'password_l')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('password_l', sa.VARCHAR(), nullable=False))
    # ### end Alembic commands ###
