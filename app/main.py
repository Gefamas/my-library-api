from fastapi import FastAPI
from .database import engine, Base
from .routers import books

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Library API")

app.include_router(books.router)

@app.get("/")
def root():
    return {"message": "Library API is running!"}