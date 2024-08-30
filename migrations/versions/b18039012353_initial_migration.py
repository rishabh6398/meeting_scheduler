"""Initial migration.

Revision ID: b18039012353
Revises: 
Create Date: 2024-08-30 21:32:09.151984

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b18039012353'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('attendee', schema=None) as batch_op:
        batch_op.add_column(sa.Column('email', sa.String(length=100), nullable=False))
        batch_op.create_unique_constraint(None, ['email'])

    with op.batch_alter_table('meeting', schema=None) as batch_op:
        batch_op.alter_column('description',
               existing_type=sa.TEXT(),
               type_=sa.String(length=200),
               nullable=False)
        batch_op.alter_column('room_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.create_foreign_key(None, 'room', ['room_id'], ['id'])
        batch_op.drop_column('participants')
        batch_op.drop_column('room')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('meeting', schema=None) as batch_op:
        batch_op.add_column(sa.Column('room', sa.TEXT(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('participants', sa.TEXT(), autoincrement=False, nullable=True))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.alter_column('room_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('description',
               existing_type=sa.String(length=200),
               type_=sa.TEXT(),
               nullable=True)

    with op.batch_alter_table('attendee', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('email')

    # ### end Alembic commands ###
