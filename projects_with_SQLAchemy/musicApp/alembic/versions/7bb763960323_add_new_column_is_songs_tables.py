"""Add new column is songs tables

Revision ID: 7bb763960323
Revises: 2cae985140a6
Create Date: 2024-08-18 17:30:17.771973

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7bb763960323'
down_revision: Union[str, None] = '2cae985140a6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('songs', sa.Column('music_file_data', sa.LargeBinary(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('songs', 'music_file_data')
    # ### end Alembic commands ###
