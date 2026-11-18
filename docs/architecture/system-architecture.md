
# HONEST DIMENSIONS
# System Architecture

**Version:** 1.0
**Architecture Style:** Layered Modular Monolith
**Status:** Initial Design

---

## 1. Overview

HONEST DIMENSIONS follows a layered modular monolith architecture with independently organized frontend and backend applications.

The system combines enterprise document management, Retrieval-Augmented Generation, LLM integrations, agentic workflows and AI security.

The architecture prioritizes maintainability, security, modularity and future scalability.

## 2. Architecture Style

### Selected: Modular Monolith

The backend will initially run as one deployable FastAPI application containing logically separated modules.

Each module will have defined responsibilities and interfaces.

This avoids unnecessary microservice infrastructure while maintaining separation of concerns.

Individual components may be extracted into independent services if future requirements justify it.

## 3. Application Layers

### 3.1 Presentation Layer

Technology: React, TypeScript, Vite and Tailwind CSS.

Responsibilities:
- User interface.
- Authentication screens.
- Document management.
- AI chat.
- Agent workflow interface.
- Approval interface.
- Usage analytics.

### 3.2 API Layer

Technology: FastAPI.

Responsibilities:
- HTTP request handling.
- Request validation.
- Authentication.
- Authorization.
- API response formatting.
- Error handling.

### 3.3 Business Logic Layer

Responsibilities:
- Organization management.
- User management.
- Document management.
- Conversation management.
- Workflow management.
- Usage tracking.

### 3.4 AI Engineering Layer

Responsibilities:
- Document ingestion.
- Embedding generation.
- RAG pipeline.
- Hybrid retrieval.
- LLM provider management.
- LangGraph workflows.
- MCP integration.
- AI guardrails.
- AI evaluation.

### 3.5 Data Layer

Technology: PostgreSQL and pgvector.

Responsibilities:
- Persistent relational data.
- Document metadata.
- Conversation history.
- Document chunks.
- Vector embeddings.
- Agent execution records.
- Audit information.

Original files will be stored separately using an interchangeable storage interface.

## 4. High-Level Request Flow

1. User interacts with the React frontend.
2. Frontend sends a request to FastAPI.
3. Authentication validates the user's identity.
4. Authorization resolves organization and workspace permissions.
5. Relevant business service processes the request.
6. AI services execute retrieval or agent workflows when required.
7. Data access is restricted to authorized resources.
8. Generated results undergo validation.
9. Backend returns the response.
10. Frontend displays the result.

## 5. Document Ingestion Architecture

Document ingestion follows these stages:

1. File upload.
2. File validation.
3. Original file storage.
4. Text extraction.
5. Text cleaning.
6. Document chunking.
7. Embedding generation.
8. Vector persistence.
9. Processing status update.

Uploaded content must be treated as untrusted data.

## 6. RAG Architecture

The RAG pipeline consists of:

1. User query.
2. Query embedding.
3. Permission-filtered retrieval.
4. Semantic and keyword search.
5. Result ranking.
6. Context construction.
7. LLM generation.
8. Output validation.
9. Citation generation.
10. Response delivery.

The retrieval layer must enforce organization and document-level access permissions.

## 7. Agent Architecture

LangGraph will manage multi-step agent workflows.

The initial research agent will:

1. Receive a research request.
2. Identify relevant documents.
3. Retrieve supporting information.
4. Analyze retrieved content.
5. Generate a structured report.
6. Validate sources.
7. Return the result.

Agent tools must use explicit permissions and validated arguments.

Sensitive actions require human approval.

## 8. AI Security Architecture

Security controls include:

- JWT authentication.
- Role-based authorization.
- Tenant isolation.
- Document access control.
- Input validation.
- Prompt injection risk mitigation.
- Untrusted document handling.
- Output validation.
- PII detection and redaction.
- Restricted tool execution.
- Human approval.
- Audit logging.

Security enforcement must not depend exclusively on LLM instructions.

## 9. Infrastructure

Initial infrastructure:

- FastAPI backend.
- React frontend.
- PostgreSQL.
- pgvector.
- Local or S3-compatible document storage.
- Configured external or local LLM providers.

Redis and background workers will be introduced when asynchronous processing requirements justify them.

Docker Compose will provide reproducible local execution.

## 10. Architectural Decisions

| Area | Decision |
|---|---|
| Architecture | Modular monolith |
| Backend | FastAPI |
| Frontend | React + TypeScript |
| Database | PostgreSQL |
| Vector search | pgvector |
| AI workflows | LangGraph |
| AI integrations | Provider abstraction |
| Deployment | Docker Compose |

## 11. Future Scalability

Potential future improvements:

- Independent background processing workers.
- Dedicated retrieval service.
- Distributed task processing.
- Separate AI inference services.
- Object storage integration.
- Advanced observability.
- Independent microservices where justified.

These are not mandatory MVP requirements.

## 12. Architecture Status

This document represents the initial architecture.

Architectural changes must be documented through Architecture Decision Records.