from pydantic import BaseModel
from enum import Enum
from typing import Optional

class BookStatus(str, Enum):
    available = "available"
    checked_out = "checked_out"

class BookBase(BaseModel):
    title: str
    author: str
    isbn: str
    year: int
    status: BookStatus = BookStatus.available

class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    isbn: Optional[str] = None
    year: Optional[int] = None
    status: Optional[BookStatus] = None

class BookOut(BookBase):
    id: int

    class Config:
        from_attributes = True