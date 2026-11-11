---
name: debugging
description: "Diagnose defects systematically using reproduction, evidence, hypotheses, and regression prevention."
version: "1.0.0"
---

# Debugging

## Purpose

Find root causes without masking symptoms or making unrelated changes.

## Activation

### Activate when

Bug, crash, unexpected result, performance regression, or environment-specific failure.

### Do not activate when

Greenfield design with no observed failure.

## Required tools and inputs

Expected/actual behavior, reproduction steps, logs, recent changes, environment, versions, and impact.

Select language-native tools and verify current official documentation for external SDKs and services before relying on a specific API.

## Recommended architecture

Trace input, state, domain logic, dependencies, persistence, and output. Use correlation IDs and structured events where available.

## Implementation workflow

1. Reproduce with smallest case. 2. Confirm impact/scope. 3. Collect logs/runtime facts. 4. Form one testable hypothesis at a time. 5. Change one variable. 6. Identify root cause. 7. Add regression test. 8. Verify adjacent paths and document.

## Coding standards

Preserve evidence before changes. Record exact versions and commands. Avoid speculative broad refactors during incident repair. Keep fixes minimal.

## Security requirements

Redact secrets/personal data from logs and reports. Never request production credentials or copy sensitive dumps into tickets. Start with read-only diagnostics.

## Error handling and observability

Distinguish original errors from secondary failures. Preserve stack traces internally. Avoid swallowing exceptions. Use rollback or feature flags for severe impact.

## Testing requirements

Create a failing test or reproducer before the fix when practical. Verify fix and adjacent boundaries. Add monitoring if the failure was invisible.

## Practical example

~~~text
Symptom: intermittent HTTP timeouts.
Hypothesis: connection pool exhausted.
Evidence: pool wait rises while upstream latency stays flat.
Experiment: compare a bounded pool change in staging.
Regression: load test verifies bounded wait under peak load.
~~~

## Common mistakes and remedies

Do not change several subsystems at once. Do not assume the last changed file caused the bug. Do not fix flakiness with arbitrary sleeps.

## Expected outputs

Reproduction, evidence log, validated cause, minimal patch, regression test, and operational follow-up.

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

Issue reproduces. Hypotheses were tested. Root cause is evidenced. Regression coverage exists. Sensitive logs are redacted.
