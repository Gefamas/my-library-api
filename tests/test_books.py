def test_create_book(client, api_key):
    # Happy path - δημιουργία βιβλίου επιτυχώς
    response = client.post("/books/", json={
        "title": "Test Book",
        "author": "Test Author",
        "isbn": "1234567890",
        "year": 2024,
        "status": "available"
    }, headers={"X-API-Key": api_key})
    assert response.status_code == 201
    assert response.json()["title"] == "Test Book"

def test_get_book_not_found(client, api_key):
    # Error case - βιβλίο που δεν υπάρχει
    response = client.get("/books/999", headers={"X-API-Key": api_key})
    assert response.status_code == 404
    assert response.json()["detail"] == "Book not found"

def test_invalid_api_key(client):
    # Auth - λάθος API key
    response = client.get("/books/", headers={"X-API-Key": "wrongkey"})
    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid API Key"