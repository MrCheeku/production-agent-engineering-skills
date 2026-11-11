---
name: testing-and-quality
description: "Build layered automated tests and quality gates that detect regressions without brittle feedback."
version: "1.0.0"
---

# Testing And Quality

## Purpose

Turn product behavior and risk assumptions into fast, repeatable evidence.

## Activation

### Activate when

Adding features, fixing bugs, changing interfaces, releasing software, or improving CI.

### Do not activate when

Pure explanation or content edit with no behavior change.

## Required tools and inputs

Acceptance criteria, risk ranking, architecture boundaries, supported environments, and critical user journeys.

Select language-native tools and verify current official documentation for external SDKs and services before relying on a specific API.

## Recommended architecture

Use a testing pyramid: many focused unit tests, fewer integration tests, and a small critical E2E set. Keep fixtures deterministic and data isolated.

## Implementation workflow

1. Translate criteria into assertions. 2. Identify risk and boundary cases. 3. Test pure logic. 4. Add adapter/contract tests. 5. Add critical E2E. 6. Run lint/type/security checks. 7. Make CI failures actionable. 8. Track flaky tests.

## Coding standards

Test behavior, not internals. Use descriptive names and arrange-act-assert. Keep tests independent, deterministic, and readable.

## Security requirements

Never put production secrets or customer data in fixtures. Test authorization denials and tenant isolation. Gate high-risk changes.

## Error handling and observability

Preserve useful failure logs without secrets. Quarantine flaky tests only with an owner and expiry.

## Testing requirements

Cover happy paths, boundaries, invalid inputs, permission failures, concurrency, timeouts, and recovery. Coverage is a signal, not proof.

## Practical example

~~~python
def test_rejects_empty_username():
    import pytest
    from app.validation import normalize_username
    with pytest.raises(ValueError):
        normalize_username("   ")
~~~

## Common mistakes and remedies

Do not assert private call counts without contract need. Do not sleep for async work. Do not depend on test order or live third parties.

## Expected outputs

Risk-based test plan, deterministic suites, CI gates, reproducible failure reports, and known gaps.

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

Acceptance criteria are tested. Tests are deterministic. Critical boundaries are covered. CI mirrors local checks. Flaky tests are owned.
