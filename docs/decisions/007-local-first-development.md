
# ADR-007: Adopt a Local-First Development Strategy

- Status: Accepted
- Date: 2026-11-21

## 1. Context

HONEST DIMENSIONS requires multiple infrastructure
components, including a frontend, backend, database,
vector search, document storage, and LLM providers.

Development should remain cost-effective and reproducible
without requiring paid cloud infrastructure for every task.

The project should also support both local language models
and external cloud-based LLM providers.

## 2. Decision

We propose a local-first development strategy.

The development environment will use:

- React and Vite for the frontend.
- FastAPI for the backend.
- PostgreSQL with pgvector for persistence and vector search.
- Local file storage during development.
- Docker and Docker Compose for managing infrastructure.
- Ollama as an optional local LLM provider.
- Gemini and Groq as optional cloud LLM integrations.

The frontend and backend may run directly on the host
machine or in containers, depending on development needs.

## 3. Alternatives Considered

### Option A: Cloud-First Development

Advantages:
- Similar infrastructure to production.
- Managed infrastructure.
- Easier access to hosted services.

Disadvantages:
- Potential infrastructure costs.
- Internet dependency.
- More complicated local experimentation.

### Option B: Local-First Development

Advantages:
- Lower development costs.
- Greater control over the environment.
- Easier local debugging.
- Supports offline development for local services.
- Reproducible infrastructure using Docker Compose.

Disadvantages:
- Depends on local hardware resources.
- Developers must maintain local infrastructure.
- Local model performance may be limited.

### Option C: Hybrid Development

Advantages:
- Combines local infrastructure with cloud services.
- Flexible model testing.
- Can resemble production infrastructure.

Disadvantages:
- Requires additional configuration.
- Cloud services may introduce costs and external dependencies.

## 4. Consequences

Positive:
- Lower initial infrastructure costs.
- More reproducible development.
- Support for local and cloud AI providers.
- Easier development and testing without mandatory paid APIs.

Negative:
- Local hardware limitations.
- Additional configuration and maintenance.
- Development and production environments may differ.

## 5. Security Considerations

- Never commit real credentials.
- Maintain an .env.example template.
- Exclude local environment files from Git.
- Use secure credential storage in production.
- Avoid sending confidential data to external providers
  without appropriate authorization.
- Use isolated test data and mocked providers where possible.

## 6. Future Considerations

Evaluate cloud infrastructure when deployment,
availability, scalability, or operational requirements
justify the additional cost.

Local development should remain reproducible even
if production infrastructure changes.

## 7. References

- docs/architecture/system-architecture.md
- docs/requirements/project-requirements.md