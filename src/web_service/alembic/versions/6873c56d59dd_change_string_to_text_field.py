"""Change string to text field

Revision ID: 6873c56d59dd
Revises: ef5b109d7527
Create Date: 2023-10-14 00:23:01.586057

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6873c56d59dd'
down_revision: Union[str, None] = 'ef5b109d7527'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Category', 'title',
               existing_type=sa.VARCHAR(length=200),
               type_=sa.Text(),
               existing_nullable=False)
    op.alter_column('Question', 'question',
               existing_type=sa.VARCHAR(length=200),
               type_=sa.Text(),
               existing_nullable=False)
    op.alter_column('Question', 'answer',
               existing_type=sa.VARCHAR(length=200),
               type_=sa.Text(),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Question', 'answer',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=200),
               existing_nullable=False)
    op.alter_column('Question', 'question',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=200),
               existing_nullable=False)
    op.alter_column('Category', 'title',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=200),
               existing_nullable=False)
    # ### end Alembic commands ###
