
# ADR-003: Choose FastAPI as the Backend Framework

- Status: Accepted
- Date: 2026-11-21

## 1. Context

HONEST DIMENSIONS requires a Python backend to expose APIs
for authentication, organizations, document management,
RAG, conversations, AI agents, and security operations.

The backend will communicate with databases, external LLM
providers, embedding models, and background processing systems.

We need a framework that supports API development, request
validation, asynchronous I/O, and maintainable application
architecture.

## 2. Decision

We propose FastAPI as the primary backend framework.

The application will use:
- FastAPI for HTTP API development.
- Pydantic for request and response validation.
- SQLAlchemy for database access.
- Alembic for database migrations.
- PostgreSQL as the primary database.

## 3. Alternatives Considered

### Option A: Django REST Framework

Advantages:
- Mature ecosystem.
- Built-in Django ORM and administration.
- Powerful serializers, authentication, and permissions.

Disadvantages:
- More framework functionality than we initially require.
- Its conventional request-handling model is not
  primarily async-first.

### Option B: FastAPI

Advantages:
- API-focused design.
- Python type-hint-based validation.
- Automatic OpenAPI documentation.
- Native support for asynchronous endpoints.
- Flexible integration with AI libraries.

Disadvantages:
- Requires explicit integration of database,
  authentication, and administration components.
- Requires architectural discipline.

### Option C: Flask

Advantages:
- Lightweight.
- Flexible.
- Simple to get started.

Disadvantages:
- Requires additional libraries and conventions.
- Less suitable as our preferred async-first API foundation.

## 4. Consequences

Positive:
- Clear API development structure.
- Automatic interactive API documentation.
- Strong request and response validation.
- Suitable integration with Python AI libraries.

Negative:
- More responsibility for assembling the backend ecosystem.
- We must implement consistent authentication,
  authorization, and database patterns ourselves.

## 5. Future Considerations

Evaluate framework limitations using real workload
measurements as the platform grows.

CPU-intensive document processing and model inference
should be handled through suitable background workers
rather than relying on asynchronous API handlers alone.

## 6. References

- docs/architecture/system-architecture.md
- docs/architecture/database-design.md
- https://fastapi.tiangolo.com/
- https://www.django-rest-framework.org/
- https://flask.palletsprojects.com/