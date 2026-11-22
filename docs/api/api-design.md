
# API Design and Contract — HONEST DIMENSIONS

## 1. Purpose

Define the REST API structure, endpoint conventions,
request and response contracts, authentication,
authorization, error handling, and API versioning.

## 2. API Technology

- Backend: FastAPI
- Validation: Pydantic
- API Style: REST
- API Format: JSON
- API Version: v1
- Documentation: OpenAPI

Base path: /api/v1/

## 3. API Conventions

- Use resource-oriented URLs.
- Use standard HTTP methods.
- Use UUIDs for resource identifiers.
- Use JSON for ordinary request and response bodies.
- Use multipart/form-data for file uploads.
- Use UTC timestamps in ISO 8601 format.
- Validate all incoming data.
- Apply authentication and authorization to protected endpoints.

## 4. Authentication

| Method | Endpoint | Purpose |
|---|---|---|
| POST | /auth/register | Register |
| POST | /auth/login | Login |
| POST | /auth/refresh | Refresh token |
| POST | /auth/logout | Logout |
| GET | /users/me | Current user |

Protected requests use:

Authorization: Bearer <access_token>

Organization selection may use an X-Organization-ID header.
The backend must verify membership and permissions.
The header is never proof of authorization.

## 5. Organization and Workspace APIs

| Method | Endpoint | Purpose |
|---|---|---|
| GET | /organizations | List organizations |
| POST | /organizations | Create organization |
| GET | /organizations/{id} | Get organization |
| GET | /organizations/{id}/members | List members |
| POST | /organizations/{id}/members | Add or invite member |
| GET | /workspaces | List workspaces |
| POST | /workspaces | Create workspace |
| PATCH | /workspaces/{id} | Update workspace |
| DELETE | /workspaces/{id} | Delete workspace |

## 6. Document APIs

| Method | Endpoint | Purpose |
|---|---|---|
| POST | /documents | Upload document |
| GET | /documents | List documents |
| GET | /documents/{id} | Document details |
| GET | /documents/{id}/status | Processing status |
| GET | /documents/{id}/download | Download document |
| DELETE | /documents/{id} | Delete document |

Document processing is asynchronous.
Uploads return an accepted response and document identifier.
The frontend checks processing status separately.

## 7. Conversation and RAG APIs

| Method | Endpoint | Purpose |
|---|---|---|
| POST | /conversations | Create conversation |
| GET | /conversations | List conversations |
| GET | /conversations/{id} | Conversation details |
| POST | /conversations/{id}/messages | Send message |
| GET | /conversations/{id}/messages | Retrieve messages |
| DELETE | /conversations/{id} | Delete conversation |

## 8. Agent and Approval APIs

| Method | Endpoint | Purpose |
|---|---|---|
| GET | /agents | List agents |
| POST | /agents/{id}/executions | Start execution |
| GET | /agents/executions/{id} | Execution status |
| GET | /approvals | List approvals |
| POST | /approvals/{id}/approve | Approve action |
| POST | /approvals/{id}/reject | Reject action |

Sensitive agent actions require backend-enforced approval.
Approval must be bound to the exact action and arguments.

## 9. Provider and Usage APIs

| Method | Endpoint | Purpose |
|---|---|---|
| GET | /providers | Supported providers |
| GET | /provider-configurations | List configurations |
| POST | /provider-configurations | Configure provider |
| PATCH | /provider-configurations/{id} | Update configuration |
| DELETE | /provider-configurations/{id} | Remove configuration |
| GET | /usage | Usage information |

Provider credentials must never be returned in API responses.

## 10. Response Conventions

Successful responses use appropriate HTTP status codes.

Errors use a consistent structure:

{
  "error": {
    "code": "RESOURCE_NOT_FOUND",
    "message": "The requested resource was not found.",
    "request_id": "request-id"
  }
}

## 11. HTTP Status Codes

- 200: Successful retrieval or operation
- 201: Resource created
- 202: Asynchronous operation accepted
- 204: Successful operation without response body
- 400: Invalid request
- 401: Authentication required
- 403: Permission denied
- 404: Resource not found or concealed
- 409: Conflict
- 413: Payload too large
- 422: Validation failure
- 429: Rate limit exceeded
- 500: Internal server error
- 503: Service unavailable

## 12. Pagination and Filtering

List endpoints support pagination.

Example:

GET /api/v1/documents?page=1&page_size=20

Filtering and sorting use validated query parameters.

## 13. Reliability

- Use idempotency keys for operations where retries
  could create duplicate effects.
- Apply request and execution timeouts.
- Use rate limits and quotas.
- Support asynchronous processing for long-running tasks.
- Keep background jobs tenant-aware.
- Avoid exposing internal exceptions to clients.

## 14. OpenAPI Documentation

FastAPI generates OpenAPI documentation.

- /docs
- /redoc
- /openapi.json

Request and response schemas will be defined using Pydantic.

## 15. Security Requirements

- Authenticate protected requests.
- Enforce organization membership.
- Apply resource-level authorization.
- Never trust client-provided tenant identifiers.
- Validate file uploads and request bodies.
- Protect provider credentials.
- Scope database operations by tenant.
- Apply rate limits and execution limits.
- Record security-relevant events.

## 16. Implementation Status

This document defines the proposed API contract.

Endpoints, schemas, and response formats must be
implemented and tested before they are considered complete.