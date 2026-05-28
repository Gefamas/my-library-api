# Library API

REST API για διαχείριση βιβλίων βιβλιοθήκης.

## Τεχνολογίες
- Python 3.11, FastAPI, SQLAlchemy
- PostgreSQL
- Docker

## Πώς τρέχει

1. Αντέγραψε το .env.example σε .env και συμπλήρωσε τις τιμές
2. Τρέξε:

```bash
docker compose up --build
```

3. Το API είναι διαθέσιμο στο http://localhost:8000
4. 4. Documentation στο http://localhost:8000/docs

## Πώς τρέχουν τα tests

```bash
pip install -r requirements.txt
pytest tests/
```

## Authentication
Όλα τα endpoints χρειάζονται header: `X-API-Key: <your_api_key>`