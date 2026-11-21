
# ADR-005: Use LangGraph for Stateful AI Workflows

- Status: Accepted
- Date: 2026-11-21

## 1. Context

HONEST DIMENSIONS requires AI workflows for document
analysis, knowledge retrieval, risk identification,
and multi-step agent operations.

Some workflows require conditional execution, state
management, retries, persistence, and human approval.

Simple LLM calls and sequential chains are sufficient
for basic tasks, but more complex workflows require
a dedicated orchestration mechanism.

## 2. Decision

We propose using LangGraph for complex, stateful AI workflows.

LangGraph workflows will use:

- State to maintain execution context.
- Nodes to represent individual operations.
- Edges to connect workflow operations.
- Conditional edges for dynamic routing.
- Checkpointing for workflow persistence.
- Human-in-the-loop mechanisms for approval-based operations.

LangChain components may be used where appropriate,
but LangChain will not be mandatory for every workflow.

## 3. Alternatives Considered

### Option A: Direct LLM Calls

Advantages:
- Simple implementation.
- Minimal orchestration overhead.

Disadvantages:
- Not suitable for complex multi-step execution.
- Requires additional application logic for state management.

### Option B: Sequential Chains

Advantages:
- Easy to understand.
- Suitable for predictable workflows.

Disadvantages:
- Limited flexibility for conditional branching and loops.
- More complex pause-and-resume behavior requires additional logic.

### Option C: LangGraph

Advantages:
- Stateful workflow orchestration.
- Conditional routing and cycles.
- Persistence and checkpointing.
- Human-in-the-loop workflows.
- Suitable for complex agent execution.

Disadvantages:
- Additional learning and implementation complexity.
- Requires careful state and checkpoint management.
- Workflow behavior needs thorough testing.

## 4. Consequences

Positive:
- Better control over multi-step AI workflows.
- Support for conditional execution.
- Ability to pause and resume workflows.
- Structured human approval processes.
- Clearer separation of workflow operations.

Negative:
- Additional orchestration complexity.
- Requires persistence and execution management.
- Agents need strict permissions and execution limits.

## 5. Security Considerations

- Treat retrieved documents as untrusted input.
- Restrict agent access through tool allowlists.
- Enforce authorization outside the LLM.
- Require approval for sensitive operations.
- Limit execution steps, retries, and resource usage.
- Audit important workflow actions.
- Protect checkpoint data and approval records.

## 6. Future Considerations

Evaluate additional agent patterns as requirements evolve.

Use direct LLM calls or simpler pipelines for tasks
that do not require graph-based orchestration.

## 7. References

- docs/architecture/system-architecture.md
- docs/requirements/project-requirements.md
- https://docs.langchain.com/oss/python/langgraph/overview