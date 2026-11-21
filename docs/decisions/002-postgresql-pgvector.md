# ADR-002: Use PostgreSQL with pgvector

- Status: Proposed
- Date: 2026-11-21

## 1. Context

HONEST DIMENSIONS requires persistent storage for structured
application data and vector embeddings.

Structured data includes users, organizations, workspaces,
documents, conversations, permissions, and audit logs.

Vector data is required for semantic search and Retrieval
Augmented Generation (RAG).

We need a database strategy that supports both requirements
without introducing unnecessary infrastructure complexity.

## 2. Decision

We propose PostgreSQL as the primary relational database
and pgvector as its vector search extension.

PostgreSQL will store application entities and metadata.

pgvector will store document chunk embeddings and support
similarity searches during RAG retrieval.

## 3. Alternatives Considered

### Option A: PostgreSQL without pgvector

Advantages:
- Strong relational database capabilities.
- Simple structured data management.

Disadvantages:
- Requires another solution for vector similarity search.

### Option B: PostgreSQL with pgvector

Advantages:
- Structured and vector data in one database.
- Transactional consistency.
- Reduced infrastructure complexity.
- Supports vector similarity search.

Disadvantages:
- Vector workloads share database resources.
- Performance must be evaluated for large datasets.

### Option C: Dedicated Vector Database

Examples:
- Qdrant
- Milvus

Advantages:
- Specialized vector search capabilities.
- Potentially better scaling for large vector workloads.

Disadvantages:
- Additional infrastructure.
- More operational complexity.
- Data synchronization between databases may be required.

## 4. Consequences

Positive:
- One primary database for the MVP.
- Simpler deployment and maintenance.
- Easier integration between document metadata and embeddings.

Negative:
- Database performance must be monitored as vector workloads grow.
- A dedicated vector database may become necessary in the future.

## 5. Future Considerations

Evaluate dedicated vector databases if measured retrieval
latency, dataset size, or workload requirements exceed
the capabilities of the current PostgreSQL setup.

Embedding dimensions and vector indexes must match the
selected embedding model.

## 6. References

- docs/architecture/database-design.md
- docs/architecture/system-architecture.md