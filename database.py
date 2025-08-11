from sqlalchemy import create_engine #This function creates a connection to the database and manages the database engine.
from sqlalchemy.ext.declarative import declarative_base #You will subclass this base to define your database tables as Python classes.
from sqlalchemy.orm import sessionmaker  #You use it to add, update, delete, and query objects in your database.

DATABASE_URL = "sqlite:///./books.db"  #Defines the connection URL to your database.

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})   #Creates a new database engine using the URL above.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)  #Creates a session factory called SessionLocal.

Base = declarative_base()  #Creates a base class named Base that your ORM models will inherit from.
