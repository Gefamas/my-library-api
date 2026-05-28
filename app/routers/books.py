# Εδώ ορίζουμε όλα τα endpoints του API για τα βιβλία
from fastapi import APIRouter, Depends, HTTPException, Query, Header
from sqlalchemy.orm import Session
from typing import Optional
from .. import models, schemas
from ..database import get_db, settings

router = APIRouter(prefix="/books", tags=["books"])

# Ελέγχουμε αν το API key είναι σωστό
def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != settings.API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

# GET /books - Επιστρέφει λίστα βιβλίων με pagination και αναζήτηση
@router.get("/", response_model=dict)
def get_books(
    page: int = Query(1, ge=1),           # σελίδα (ξεκινά από 1)
    size: int = Query(10, ge=1, le=100),  # αποτελέσματα ανά σελίδα
    title: Optional[str] = None,           # αναζήτηση βάσει τίτλου
    author: Optional[str] = None,          # αναζήτηση βάσει συγγραφέα
    db: Session = Depends(get_db),
    _: None = Depends(verify_api_key)
):
    query = db.query(models.Book)

    # Φιλτράρουμε αν δόθηκε τίτλος ή συγγραφέας
    if title:
        query = query.filter(models.Book.title.ilike(f"%{title}%"))
    if author:
        query = query.filter(models.Book.author.ilike(f"%{author}%"))

    total = query.count()
    books = query.offset((page - 1) * size).limit(size).all()
    return {"total": total, "page": page, "size": size, "books": books}

# GET /books/{id} - Επιστρέφει ένα συγκεκριμένο βιβλίο
@router.get("/{book_id}", response_model=schemas.BookOut)
def get_book(book_id: int, db: Session = Depends(get_db), _: None = Depends(verify_api_key)):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

# POST /books - Δημιουργεί νέο βιβλίο
@router.post("/", response_model=schemas.BookOut, status_code=201)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db), _: None = Depends(verify_api_key)):
    # Ελέγχουμε αν υπάρχει ήδη βιβλίο με το ίδιο ISBN
    existing = db.query(models.Book).filter(models.Book.isbn == book.isbn).first()
    if existing:
        raise HTTPException(status_code=400, detail="ISBN already exists")
    db_book = models.Book(**book.model_dump())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

# PUT /books/{id} - Ενημερώνει υπάρχον βιβλίο
@router.put("/{book_id}", response_model=schemas.BookOut)
def update_book(book_id: int, book: schemas.BookUpdate, db: Session = Depends(get_db), _: None = Depends(verify_api_key)):
    db_book = db.query