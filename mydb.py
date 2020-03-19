import sqlalchemy
import sqlalchemy.dialects
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, DateTime
from sqlalchemy.orm import scoped_session, sessionmaker

# engine = create_engine(os.getenv("DATABASE_URL"))
DATABASE_URL = 'postgres://oqnyzoveayjpnb:35377aea43fe446da6620fc909e6cb5176fc2ff0d48e9eed0cc1e248caf979a0@ec2-52-203-160-194.compute-1.amazonaws.com:5432/d1hkt2ecuhb45o'
engine = create_engine(DATABASE_URL)
db = scoped_session(sessionmaker(bind=engine))

def create():
    meta = MetaData()
    students = Table(
       'users', meta, 
       Column('id', Integer, primary_key = True), 
       Column('name', String), 
       Column('lastname', String),
       Column('password', String),
       Column('registration_date', DateTime(timezone=False))
    )
    meta.create_all(engine)

if __name__ == '__main__':
    create()
