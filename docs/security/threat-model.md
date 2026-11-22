
# Threat Model — HONEST DIMENSIONS

## 1. Purpose

Identify security threats affecting HONEST DIMENSIONS and define
the controls required to protect users, organizations, data,
AI workflows, and external integrations.

## 2. Security Scope

This threat model covers:

- Authentication and authorization
- Organization and workspace isolation
- Document uploads and processing
- RAG and vector retrieval
- LLM provider integrations
- AI agents and tool execution
- API security
- Secrets and credentials
- Audit logs and usage tracking

## 3. Protected Assets

- User credentials and access tokens
- Organization documents and extracted content
- Document chunks and vector embeddings
- Conversations and message history
- LLM provider API keys
- Agent tools and execution permissions
- Approval records and audit logs
- Database credentials and application secrets

## 4. Threat Actors

- Unauthenticated external attackers
- Malicious authenticated users
- Malicious organization members
- Users attempting cross-tenant access
- Malicious document authors
- Compromised third-party services or dependencies
- Abusive or misconfigured AI agents

## 5. Trust Boundaries

- Browser to FastAPI backend
- Backend to PostgreSQL
- Organization A to Organization B
- Uploaded files to document processing workers
- Backend to external LLM providers
- AI agents to external tools
- Background workers to shared application resources

## 6. STRIDE Analysis

| Category | Example | Security Control |
|---|---|---|
| Spoofing | Stolen user token | Token security and revocation |
| Tampering | Modified document metadata | Authorization and integrity checks |
| Repudiation | Denying an approved action | Audit logging |
| Information Disclosure | Cross-tenant retrieval | Tenant isolation and RLS |
| Denial of Service | Excessive AI requests | Rate limits and quotas |
| Elevation of Privilege | Employee accessing admin features | RBAC and server-side authorization |

## 7. Initial Threat Register

| ID | Threat | Impact | Planned Mitigation |
|---|---|---|---|
| TH-01 | Stolen access token | Account takeover | Secure token lifecycle |
| TH-02 | Cross-tenant access | Data leakage | Tenant authorization and RLS |
| TH-03 | Malicious uploaded file | Parser compromise | File validation and isolation |
| TH-04 | Direct prompt injection | Manipulated AI behavior | Input handling and action restrictions |
| TH-05 | Indirect prompt injection | Malicious document influences agents | Untrusted-content handling |
| TH-06 | RAG poisoning | Manipulated retrieval results | Provenance and ingestion controls |
| TH-07 | API key leakage | Unauthorized provider usage | Encryption and secret redaction |
| TH-08 | Agent tool abuse | Unauthorized actions | Tool allowlists and human approval |
| TH-09 | Unsafe model output | Downstream injection | Schema validation and output encoding |
| TH-10 | Unbounded AI consumption | Service and cost exhaustion | Rate limits and execution limits |

## 8. Core Security Principles

1. Zero trust: authenticate and authorize every protected operation.
2. Least privilege: grant only necessary permissions.
3. Defense in depth: use multiple independent security controls.
4. Secure by default: deny unauthorized operations.
5. Auditability: record important security events.

## 9. AI-Specific Security Requirements

- Treat user prompts and retrieved documents as untrusted input.
- Never rely on system prompts for access control.
- Enforce tenant authorization before retrieving documents.
- Restrict agent tools using explicit allowlists.
- Validate tool arguments before execution.
- Require human approval for sensitive actions.
- Never expose provider credentials in prompts or logs.
- Validate model outputs before downstream processing.
- Apply request, token, time, and execution limits.
- Maintain provenance for retrieved documents and AI responses.

## 10. Validation Strategy

Every identified threat must eventually have a security test.

Examples:

- Verify Organization B cannot retrieve Organization A's documents.
- Verify unauthorized users cannot execute administrative operations.
- Verify malicious document instructions cannot authorize tool execution.
- Verify an agent cannot call tools outside its permission list.
- Verify API keys never appear in application logs.
- Verify request limits prevent excessive AI consumption.

## 11. Status

Initial threat model drafted.

Threat mitigations are architectural requirements,
not proof that the controls have already been implemented.

This document will evolve as the application architecture
and implementation develop.