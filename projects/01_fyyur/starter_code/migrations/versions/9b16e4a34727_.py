"""empty message

Revision ID: 9b16e4a34727
Revises: 4f9355c20b61
Create Date: 2020-12-24 18:43:56.929523

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9b16e4a34727'
down_revision = '4f9355c20b61'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('past_shows', sa.PickleType(), nullable=True))
    op.add_column('Artist', sa.Column('past_shows_count', sa.Integer(), nullable=True))
    op.add_column('Artist', sa.Column('upcoming_shows', sa.PickleType(), nullable=True))
    op.add_column('Artist', sa.Column('upcoming_shows_count', sa.Integer(), nullable=True))
    op.add_column('Venue', sa.Column('past_shows', sa.PickleType(), nullable=True))
    op.add_column('Venue', sa.Column('past_shows_count', sa.Integer(), nullable=True))
    op.add_column('Venue', sa.Column('upcoming_shows', sa.PickleType(), nullable=True))
    op.add_column('Venue', sa.Column('upcoming_shows_count', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Venue', 'upcoming_shows_count')
    op.drop_column('Venue', 'upcoming_shows')
    op.drop_column('Venue', 'past_shows_count')
    op.drop_column('Venue', 'past_shows')
    op.drop_column('Artist', 'upcoming_shows_count')
    op.drop_column('Artist', 'upcoming_shows')
    op.drop_column('Artist', 'past_shows_count')
    op.drop_column('Artist', 'past_shows')
    # ### end Alembic commands ###
