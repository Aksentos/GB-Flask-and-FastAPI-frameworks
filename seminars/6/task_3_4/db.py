import databases
from sqlalchemy import Table, Column, Integer, String, MetaData, create_engine, Boolean
from settings import settings


DATABASE_URL = settings.DATABASE_URL
db = databases.Database(DATABASE_URL)
metadata = MetaData()


tasks = Table(
    "tasks",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(50)),
    Column("description", String(120)),
    Column("status", Boolean()),
 
)

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
metadata.create_all(engine)

