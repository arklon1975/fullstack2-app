"""create todos table

Revision ID: f99d9468aa3f
Revises: 
Create Date: 2024-10-03 14:36:58.609399

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f99d9468aa3f'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None



def upgrade():
    op.execute("""
    create table todos(
        id bigserial primary key,
        name text,
        completed boolean not null default false
    )
    """)

def downgrade():
    op.execute("drop table todos;")