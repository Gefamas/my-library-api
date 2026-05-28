# Write-up — Τι θα έκανα με 4 ακόμα ώρες

Με επιπλέον χρόνο θα βελτίωνα τα εξής:

**1. Περισσότερα tests**
Θα πρόσθετα tests για pagination, αναζήτηση βάσει τίτλου/συγγραφέα
και για duplicate ISBN.

**2. Logging**
Θα πρόσθετα logging ώστε να καταγράφονται τα errors και τα requests
για ευκολότερο debugging.

**3. Alembic migrations**
Αντί να δημιουργούμε τους πίνακες αυτόματα με το SQLAlchemy,
θα χρησιμοποιούσα Alembic για σωστό version control της βάσης.

**4. Rate limiting**
Θα πρόσθετα όριο στα requests ανά API key για προστασία από κατάχρηση.

**5. Health check endpoint**
Ένα GET /health που ελέγχει αν το API και η βάση δουλεύουν σωστά.