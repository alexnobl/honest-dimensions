
# AI Security Architecture — HONEST DIMENSIONS

## 1. Purpose

Define security mechanisms for protecting AI interactions,
RAG pipelines, agent workflows, external integrations,
and organization data.

## 2. Security Architecture Principles

- Never treat LLM output as trusted.
- Never rely on prompts for authorization.
- Enforce permissions in backend code.
- Apply least privilege to users, agents, and tools.
- Isolate organization data.
- Require approval for sensitive operations.
- Record security-relevant events.

## 3. Prompt Injection Defense

### Direct Prompt Injection

Malicious instructions supplied through user prompts.

### Indirect Prompt Injection

Malicious instructions embedded in retrieved documents,
web content, tool results, or other external sources.

### Controls

- Separate trusted instructions from untrusted content.
- Clearly identify retrieved content as untrusted.
- Do not place secrets in prompts.
- Validate model-generated actions outside the LLM.
- Apply input and output security checks.
- Perform adversarial security testing.

Prompt filtering is a defense layer, not a complete solution.

## 4. RAG Security

- Resolve organization context from authenticated membership.
- Apply tenant filters before vector retrieval.
- Validate document-level permissions.
- Use PostgreSQL RLS as defense in depth.
- Scope caches and background jobs by tenant.
- Protect document downloads and conversation history.
- Maintain document provenance and access records.

## 5. AI Guardrails

### Input Guardrails

- Input size and format validation.
- Suspicious content detection.
- Untrusted context identification.

### Output Guardrails

- Structured output validation.
- Sensitive information checks.
- Citation and source validation.
- Safe downstream rendering.

### Action Guardrails

- Tool allowlists.
- Permission validation.
- Argument validation.
- Action risk classification.
- Human approval for sensitive operations.

Deterministic controls must enforce security decisions.
Model-based classifiers provide additional detection.

## 6. Agent Tool Security

- Agents cannot directly access unrestricted system resources.
- Every tool has an explicit permission policy.
- Tool arguments are validated using typed schemas.
- Authorization uses the initiating user's identity and tenant.
- Tools receive only the permissions required for their task.
- Sensitive operations require approval.
- Execution has timeout and iteration limits.
- Every tool execution is audited.

## 7. Human-in-the-Loop

Approval is required for configured high-risk actions.

Approval records must include:

- Organization and requesting user.
- Agent execution reference.
- Action type and exact arguments.
- Approval status.
- Reviewer identity and timestamp.
- Expiration information.

Revalidate permissions and action integrity before execution.
Expired, rejected, or modified actions must not execute
under an earlier approval.

## 8. Security Monitoring

Record security-relevant events:

- Authentication failures.
- Authorization failures.
- Cross-tenant access attempts.
- Suspicious prompt injection signals.
- Rejected tool executions.
- Approval decisions.
- Provider errors.
- Rate-limit events.

Never log passwords, tokens, API keys, or unnecessary
sensitive document contents.

## 9. Security Testing Requirements

- Test direct prompt injection.
- Test indirect injection in uploaded documents.
- Test cross-tenant RAG retrieval.
- Test unauthorized tool execution.
- Test malformed tool arguments.
- Test approval expiration and replay.
- Test sensitive output leakage.
- Test provider credential redaction.
- Test rate limits and agent execution limits.

## 10. Implementation Status

This document describes the intended security architecture.

The controls are design requirements and must be implemented,
tested, and reviewed before being considered effective.