# Εδώ ορίζουμε πώς μοιάζει ένα βιβλίο μέσα στην βάση δεδομένων
from sqlalchemy import Column, Integer, String, Enum
from .database import Base
import enum

# Οι δύο καταστάσεις που μπορεί να έχει ένα βιβλίο
class BookStatus(str, enum.Enum):
    available = "available"
    checked_out = "checked_out"

# Ο πίνακας "books" στην βάση δεδομένων
class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)  # μοναδικό ID
    title = Column(String, nullable=False)               # τίτλος
    author = Column(String, nullable=False)              # συγγραφέας
    isbn = Column(String, unique=True, nullable=False)   # μοναδικός κωδικός βιβλίου
    year = Column(Integer, nullable=False)               # χρονιά έκδοσης
    status = Column(Enum(BookStatus), default=BookStatus.available)  # διαθεσιμότητα