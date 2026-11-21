
# ADR-006: Adopt a Layered Multi-Tenant Security Strategy

- Status: Proposed
- Date: 2026-11-21

## 1. Context

HONEST DIMENSIONS is designed to support multiple organizations
using a shared application.

Each organization may have multiple users, workspaces,
documents, conversations, AI workflows, and provider
configurations.

The platform must prevent unauthorized access to data
belonging to other organizations.

Tenant isolation must apply consistently across APIs,
database queries, vector retrieval, background jobs,
caches, file storage, and AI agent tools.

## 2. Decision

We propose a shared PostgreSQL database and shared schema
with organization-level tenant isolation.

Tenant-owned records will contain an organization_id.
Workspace-specific records will also contain a workspace_id
where appropriate.

The security architecture will use multiple layers:

- Authentication to identify users.
- Organization memberships to verify tenant access.
- Role-Based Access Control (RBAC).
- Application-level tenant authorization.
- Database constraints to preserve tenant relationships.
- PostgreSQL Row-Level Security (RLS) as an additional
  database protection layer.
- Tenant-scoped vector retrieval.
- Authorization checks for AI agent tools.

## 3. Alternatives Considered

### Option A: Separate Database per Organization

Advantages:
- Strong physical data separation.
- Independent database configuration.
- Suitable for specialized enterprise requirements.

Disadvantages:
- More infrastructure.
- Complex database provisioning and migrations.
- Higher operational overhead.

### Option B: Separate Schema per Organization

Advantages:
- Logical separation of database objects.
- Shared database infrastructure.

Disadvantages:
- Complex schema management.
- More difficult migrations as tenant count grows.

### Option C: Shared Database and Shared Schema

Advantages:
- Lower infrastructure complexity.
- Easier migrations.
- Efficient resource utilization.
- Suitable for the initial MVP.

Disadvantages:
- Requires strict tenant filtering.
- A missing authorization check could expose data.
- Requires careful database policy design.

## 4. Consequences

Positive:
- Cost-effective initial architecture.
- Centralized database management.
- Consistent tenant authorization.
- Additional database-level protection through RLS.
- Supports multiple organizations and workspaces.

Negative:
- Requires careful authorization implementation.
- RLS configuration and connection pooling require attention.
- Tenant isolation must be tested across every data path.

## 5. Security Requirements

- Never trust organization IDs supplied by clients.
- Derive tenant context from authenticated membership.
- Verify workspace membership and permissions.
- Apply tenant filters to all relevant database queries.
- Apply tenant filters before vector search results are returned.
- Protect background jobs and cached data.
- Enforce permissions on every AI agent tool execution.
- Restrict access to organization-specific audit logs.
- Use database constraints to prevent invalid
  cross-organization relationships.
- Test for cross-tenant access vulnerabilities.

## 6. Database Security

PostgreSQL Row-Level Security will provide an additional
database-level protection layer.

RLS policies must use trusted transaction-scoped tenant
context and a restricted database role.

Connection pooling, background workers, administrative
operations, and database ownership privileges must be
handled carefully.

RLS does not replace application-level authorization.

## 7. Future Considerations

Evaluate separate databases or schemas for organizations
that require stronger physical isolation or specialized
enterprise deployment arrangements.

Review tenant isolation through security testing,
including API authorization tests, vector retrieval tests,
and background job tests.

## 8. References

- docs/architecture/database-design.md
- docs/architecture/system-architecture.md
- docs/requirements/project-requirements.md