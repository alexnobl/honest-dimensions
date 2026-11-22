
# Project Structure — HONEST DIMENSIONS

## 1. Architecture Style

HONEST DIMENSIONS follows a modular monolith architecture.

The repository separates frontend, backend, infrastructure,
documentation, and testing responsibilities.

## 2. Root Structure

```text
honest-dimensions/
├── apps/
│   ├── backend/
│   └── frontend/
├── docs/
│   ├── requirements/
│   ├── architecture/
│   ├── decisions/
│   ├── security/
│   └── api/
├── infrastructure/
├── scripts/
├── .github/
├── .env.example
├── .gitignore
├── docker-compose.yml
├── README.md
├── CHANGELOG.md
└── LICENSE
```

## 3. Backend Structure

The backend uses Python, FastAPI, Pydantic,
SQLAlchemy, and Alembic.

```text
backend/
├── app/
│   ├── main.py
│   ├── api/
│   │   └── v1/
│   ├── core/
│   ├── database/
│   ├── modules/
│   │   ├── auth/
│   │   ├── users/
│   │   ├── organizations/
│   │   ├── workspaces/
│   │   ├── documents/
│   │   ├── conversations/
│   │   ├── rag/
│   │   ├── providers/
│   │   ├── agents/
│   │   ├── approvals/
│   │   ├── security/
│   │   ├── evaluation/
│   │   └── usage/
│   ├── ai/
│   │   ├── embeddings/
│   │   ├── retrieval/
│   │   ├── guardrails/
│   │   ├── providers/
│   │   └── workflows/
│   └── workers/
├── migrations/
├── tests/
│   ├── unit/
│   ├── integration/
│   └── security/
├── alembic.ini
├── pyproject.toml
└── Dockerfile
```

## 4. Backend Module Organization

Business modules may contain:

- router.py: HTTP endpoints
- service.py: Business logic
- repository.py: Database operations
- models.py: SQLAlchemy models
- schemas.py: Pydantic schemas
- dependencies.py: Module-specific dependencies

Not every module requires every file.

## 5. Backend Layer Responsibilities

- API layer: Handles HTTP requests and responses.
- Core layer: Provides shared configuration and security.
- Database layer: Manages database infrastructure.
- Modules layer: Implements business capabilities.
- AI layer: Provides reusable AI functionality.
- Workers layer: Processes background tasks.

## 6. Frontend Structure

The frontend uses React, TypeScript, Vite, and Tailwind CSS.

```text
frontend/
├── src/
│   ├── app/
│   ├── components/
│   ├── features/
│   ├── hooks/
│   ├── lib/
│   ├── services/
│   ├── types/
│   └── assets/
├── public/
├── package.json
├── tsconfig.json
└── Dockerfile
```

Frontend features include:

- Authentication
- Dashboard
- Organizations
- Workspaces
- Documents
- Conversations
- Agents
- Approvals
- Settings

## 7. Testing Strategy

Backend testing is divided into:

- Unit tests
- Integration tests
- Security tests

Frontend and end-to-end tests will be added
as the corresponding functionality develops.

## 8. Configuration Management

- Use environment variables for configuration.
- Maintain .env.example as a safe template.
- Never commit actual secrets.
- Use .gitignore to exclude local configuration.
- Protect user-provided provider credentials.

## 9. Development Principles

1. Keep business modules independent.
2. Avoid circular dependencies.
3. Separate API handling from business logic.
4. Keep database access behind repositories.
5. Reuse shared AI infrastructure.
6. Test modules independently.
7. Introduce abstractions when they provide real value.
8. Avoid premature microservices and unnecessary complexity.

## 10. Implementation Status

This is the planned repository structure.

Directories and modules will be introduced progressively
as their implementation begins.