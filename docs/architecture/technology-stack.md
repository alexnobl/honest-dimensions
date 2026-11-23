
# Technology Stack — HONEST DIMENSIONS

## 1. Purpose

Document the technologies selected or proposed for
HONEST DIMENSIONS and explain their responsibilities.

## 2. Backend

| Technology | Purpose |
|---|---|
| Python | Main backend language |
| FastAPI | REST API framework |
| Pydantic | Validation and schemas |
| SQLAlchemy | ORM and database access |
| Alembic | Database migrations |
| Uvicorn | ASGI server |
| HTTPX | HTTP client |

## 3. Database

| Technology | Purpose |
|---|---|
| PostgreSQL | Relational database |
| pgvector | Vector similarity search |
| Psycopg | PostgreSQL driver |

## 4. AI Engineering

| Technology | Purpose |
|---|---|
| LangChain | LLM integrations and components |
| LangGraph | Stateful agent workflows |
| Sentence Transformers | Local embeddings |
| Gemini | Cloud LLM provider |
| Groq | Cloud inference provider |
| Ollama | Local LLM runtime |
| PyPDF | PDF text extraction |

## 5. Frontend

| Technology | Purpose |
|---|---|
| React | UI framework |
| TypeScript | Static typing |
| Vite | Development and build tooling |
| Tailwind CSS | Styling |

## 6. Infrastructure

| Technology | Purpose |
|---|---|
| Docker | Containerization |
| Docker Compose | Local multi-container environment |
| Git | Version control |
| GitHub | Repository and collaboration |
| GitHub Actions | CI automation |

## 7. Development and Testing

| Technology | Purpose |
|---|---|
| Pytest | Backend testing |
| Ruff | Python linting and formatting |
| HTTPX | API testing |
| npm | Frontend package management |

## 8. Initial LLM Provider Strategy

The application will support a provider abstraction.

Initial provider targets:

- Google Gemini
- Groq
- Ollama

The provider manager will eventually support:

- Provider selection
- Model capability handling
- Credential management
- Quota and rate-limit handling
- Retry and fallback policies
- Usage tracking

## 9. Dependency Strategy

Dependencies will be introduced progressively.

Essential dependencies will be installed during
backend and frontend foundation work.

AI integrations will be added when their modules
are implemented.

Optional infrastructure such as Redis and Celery
will only be introduced when justified by actual needs.

## 10. Security Considerations

- Keep credentials outside source code.
- Never commit .env files.
- Validate external API responses.
- Protect provider credentials.
- Track provider usage and failures.
- Use supported package versions.
- Review dependencies for maintenance and security.

## 11. Cost Strategy

Prefer local development and free or low-cost options.

- PostgreSQL and pgvector locally.
- Ollama where hardware permits.
- Free-tier cloud LLM providers where available.
- Mock providers for automated tests.
- Avoid unnecessary paid infrastructure.

Provider quotas and pricing must be verified
when integrations are implemented.

## 12. Decision Status

Accepted foundational decisions:

- FastAPI
- PostgreSQL and pgvector
- Modular monolith
- LangGraph for complex stateful workflows

Other technologies remain proposed until evaluated
and formally accepted where necessary.

## 13. Implementation Status

This document describes the planned technology stack.

Dependencies will be installed progressively,
not all at once.