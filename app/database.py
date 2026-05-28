# Αυτό το αρχείο συνδέει το API με την βάση δεδομένων
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from pydantic_settings import BaseSettings, SettingsConfigDict

# Διαβάζουμε τις ρυθμίσεις από το .env αρχείο
class Settings(BaseSettings):
    DATABASE_URL: str
    API_KEY: str

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()

# Δημιουργούμε σύνδεση με την βάση
engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Αυτή η συνάρτηση δίνει σύνδεση σε κάθε request και την κλείνει μετά
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()