# Bug Hunt

## Bug 1 — Λανθασμένο φιλτράρισμα orders

**Κώδικας:** `orders = db.query(Order).all()`

**Πρόβλημα:** Φέρνει ΟΛΑ τα orders από τη βάση και μετά τα φιλτράρει με Python.
Αν υπάρχουν 1.000.000 orders, φορτώνει όλα στη μνήμη — πολύ αργό και επικίνδυνο.

**Διόρθωση:**
```python
orders = db.query(Order).filter(Order.user_id == user_id).all()
```

## Bug 2 — Διαρροή ευαίσθητων δεδομένων

**Κώδικας:** `"password": user.password`

**Πρόβλημα:** Επιστρέφει το password του χρήστη στο response!
Κανείς δεν πρέπει να βλέπει passwords — ούτε κρυπτογραφημένα.

**Διόρθωση:** Αφαίρεσε εντελώς το πεδίο password από το response.

## Bug 3 — Δεν ελέγχει αν υπάρχει ο χρήστης

**Κώδικας:** `user = db.query(User).filter(User.id == user_id).first()`

**Πρόβλημα:** Αν δεν βρεθεί χρήστης, το `user` είναι `None`.
Μετά το `user.password` κάνει crash με AttributeError.

**Διόρθωση:**
```python
if not user:
    raise HTTPException(status_code=404, detail="User not found")
```
