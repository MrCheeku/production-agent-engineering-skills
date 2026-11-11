---
name: code-review
description: "Review changes for correctness, security, maintainability, coverage, compatibility, and operational risk."
version: "1.0.0"
---

# Code Review

## Purpose

Provide specific evidence-based feedback that makes a change safer without bikeshedding.

## Activation

### Activate when

Reviewing a PR, patch, generated code, or high-impact planned change.

### Do not activate when

No code or technical change is available.

## Required tools and inputs

Diff, requirements, surrounding code, supported versions, test results, security context, and deployment impact.

Select language-native tools and verify current official documentation for external SDKs and services before relying on a specific API.

## Recommended architecture

Review in context: callers, contracts, data ownership, trust boundaries, migrations, and operations. Prioritize defects over style.

## Implementation workflow

1. Read requirements and diff. 2. Trace changed code through callers. 3. Check correctness/edge cases. 4. Review security/auth. 5. Inspect tests/failure handling. 6. Consider performance/compatibility. 7. Run focused checks if available. 8. Report severity, location, impact, and fix.

## Coding standards

Findings must be actionable and tied to changed lines or behavior. Separate blockers from suggestions. State missing evidence. Avoid speculative issues.

## Security requirements

Prioritize exploitable trust-boundary failures, secret exposure, authorization gaps, injection, unsafe deserialization, and supply-chain risks.

## Error handling and observability

Check state preservation, resource cleanup, propagation, duplicate side effects, silent exception handling, and unbounded retries.

## Testing requirements

Check changed behavior, boundaries, authorization denials, and regression paths. Note unexecuted tests explicitly. Never invent CI outcomes.

## Practical example

~~~text
Severity: High
Location: api/orders.py:84
Issue: Order lookup does not scope by authenticated tenant.
Impact: A user may read another tenant's order.
Fix: Scope by tenant and add a cross-tenant denial test.
~~~

## Common mistakes and remedies

Do not report formatting preferences as bugs. Trace inputs to plausible impact. Do not claim tests pass when they were not run.

## Expected outputs

Prioritized review with file/line references, impact, fixes, test gaps, and approval/blocking summary.

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

Requirements are checked. Security boundaries are traced. Findings are actionable. Test status is factual. Severity matches impact.
