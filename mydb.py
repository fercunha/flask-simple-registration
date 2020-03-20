import os
import sqlalchemy
import sqlalchemy.dialects
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, DateTime
from sqlalchemy.orm import scoped_session, sessionmaker
import logging
from dotenv import load_dotenv

load_dotenv()

# logging.basicConfig()
# logging.getLogger('sqlalchemy.engine').setLevel(logging.DEBUG)

engine = create_engine(os.getenv("DATABASE_URL"), echo=True)
db = scoped_session(sessionmaker(bind=engine))

def create():
    meta = MetaData()
    students = Table(
       'users', meta, 
       Column('id', Integer, primary_key = True), 
       Column('name', String), 
       Column('lastname', String),
       Column('username', String),
       Column('password', String),
       Column('registration_date', DateTime(timezone=True))
    )
    meta.create_all(engine)

if __name__ == '__main__':
    create()
