---
name: tool-calling-and-agents
description: "Build bounded agent loops with typed tools, authorization checks, budgets, idempotency, and traceable execution."
version: "1.0.0"
---

# Tool Calling And Agents

## Purpose

Allow a model to request application actions while policy, validation, and side effects remain under deterministic application control.

## Activation

### Activate when

Implementing function calling, multi-step agents, planners, tool registries, or model-directed task execution.

### Do not activate when

A single model response without external actions is enough.

## Required tools and inputs

Tool inventory, user permissions, task boundaries, max steps, cost/time budgets, state model, and approval requirements.

Select language-native tools and verify current official documentation for external SDKs and services before relying on a specific API.

## Recommended architecture

Separate planner/model adapter, tool registry, policy engine, execution layer, state store, and audit trail. The model proposes; deterministic code validates and decides.

## Implementation workflow

1. Define tools with small schemas and side-effect labels. 2. Resolve identity and permissions outside the model. 3. Validate and normalize arguments. 4. Check policy and approval requirements. 5. Execute with deadline and idempotency key. 6. Return minimal structured results. 7. Enforce max turns, calls, tokens, and elapsed time. 8. Stop on ambiguity or repeated failure.

## Coding standards

Use allowlisted tool names, strict schemas, bounded loops, deterministic validation, idempotent writes, and typed outcomes. Keep authoritative state separate from model history.

## Security requirements

Never let generated shell commands or URLs bypass policy. Defend against prompt injection in retrieved content. Check ownership and tenant boundaries on every call. Require approval for destructive, financial, privacy-sensitive, or external communications actions.

## Error handling and observability

Use typed outcomes: success, denied, invalid, retryable, failed. Retry only known-safe operations. Detect repeated calls and loops. Redact secrets from audit context.

## Testing requirements

Test schema rejection, permission denial, injected instructions, duplicate calls, retries, loop exhaustion, cancellation, and partial completion. Assert policy is consulted for every tool call.

## Practical example

~~~python
def authorize(tool: str, scopes: set[str]) -> bool:
    required = {"read_status": "status:read", "set_mode": "device:write"}
    scope = required.get(tool)
    return scope is not None and scope in scopes
~~~

## Common mistakes and remedies

Do not let the model decide resource ownership. Do not run unlimited loops. Do not treat retrieved text as instructions. Do not retry writes without idempotency.

## Expected outputs

Typed tool registry, policy checks, bounded orchestrator, audit events, approval flow, and adversarial tests.

## Production-readiness checklist

- Requirements and constraints are recorded.
- Boundaries and ownership are explicit.
- Inputs and outputs have documented contracts.
- Failure and recovery behavior is defined.
- Security controls are enforced outside untrusted model output.
- Tests cover normal, boundary, denied, and failing cases.
- Logs and metrics are useful and contain no secrets.
- Operational and compatibility limitations are documented.

## Quality-assurance checklist

Every tool is allowlisted. Permissions are checked at execution. Budgets are enforced. Writes are idempotent. High-impact actions need approval.
