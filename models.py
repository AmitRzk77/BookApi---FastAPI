from sqlalchemy import Column, Integer, String
from database import Base

class Book(Base): #It inherits from Base, so SQLAlchemy knows this is a mapped table.
    __tablename__ = "books" #Specify the table name in the database as "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String, index=True)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)