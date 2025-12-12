# Design Notes

## Modular and Clean Design

This project follows a modular, layered architecture. Files are organized so each file has one responsibility:
- `routes/` contains HTTP endpoints.
- `crud.py` contains database operations.
- `schemas.py` contains Pydantic models for validation/serialization.
- `database.py` isolates DB connection logic (Motor).
- `utils.py` contains reusable helpers (hashing, JWT).
- `tests/` holds unit and integration tests.

### Principles
- Single Responsibility
- Separation of concerns (API vs DB)
- Async-first design (FastAPI + Motor)
- Security best practices (hashed passwords, JWT)
- Testability and maintainability

### Benefits
- Easier maintenance and testing
- Reusable components
- Ready for scaling and deployment
