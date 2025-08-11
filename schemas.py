from pydantic import BaseModel #Import BaseModel from Pydantic, which is a data validation and parsing library.
                               #FastAPI uses Pydantic models to validate request data and serialize response data.
class BookBase(BaseModel):  #Define a base schema BookBase for the book data structure.
    title: str
    author: str

class BookCreate(BookBase):  #This is used for creating a new book.
    pass

class Book(BookBase):  #This model is used for reading book data (i.e., responses) where an ID is present.
    id: int

    class Config:
        from_attributes = True  # This allows returning ORM objects directly from your endpoints and Pydantic will convert them to JSON properly.


class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    class Config:
        from_attributes = True

# Token Schemas
class Token(BaseModel):
    access_token: str
    token_type: str