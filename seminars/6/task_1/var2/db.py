import databases
import sqlalchemy as sql
from settings import settings


DATABASE_URL = settings.DATABASE_URL
db = databases.Database(DATABASE_URL)
metadata = sql.MetaData()


users = sql.Table(
    "users",
    metadata,
    sql.Column("id", sql.Integer, primary_key=True),
    sql.Column("username", sql.String(20)),
    sql.Column("email", sql.String(128)),
    sql.Column("password", sql.String(10)),
)

engine = sql.create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
metadata.create_all(engine)
