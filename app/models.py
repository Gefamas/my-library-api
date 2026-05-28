from sqlalchemy import Column, Integer, String, Enum
from .database import Base
import enum

class BookStatus(str, enum.Enum):
    available = "available"
    checked_out = "checked_out"

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    isbn = Column(String, unique=True, nullable=False)
    year = Column(Integer, nullable=False)
    status = Column(Enum(BookStatus), default=BookStatus.available)