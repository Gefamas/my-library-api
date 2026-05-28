# Εδώ ορίζουμε τι δεδομένα στέλνει και παίρνει το API
from pydantic import BaseModel
from enum import Enum
from typing import Optional

class BookStatus(str, Enum):
    available = "available"
    checked_out = "checked_out"

# Τα βασικά πεδία ενός βιβλίου
class BookBase(BaseModel):
    title: str
    author: str
    isbn: str
    year: int
    status: BookStatus = BookStatus.available

# Αυτό χρησιμοποιείται όταν δημιουργούμε νέο βιβλίο
class BookCreate(BookBase):
    pass

# Αυτό χρησιμοποιείται όταν ενημερώνουμε βιβλίο - όλα τα πεδία προαιρετικά
class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    isbn: Optional[str] = None
    year: Optional[int] = None
    status: Optional[BookStatus] = None

# Αυτό επιστρέφεται στον χρήστη - περιλαμβάνει και το ID
class BookOut(BookBase):
    id: int

    model_config = {"from_attributes": True}