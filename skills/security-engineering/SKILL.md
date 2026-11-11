---
name: security-engineering
description: "Apply threat modeling, secure defaults, dependency hygiene, least privilege, and defensive testing."
version: "1.0.0"
---

# Security Engineering

## Purpose

Reduce attack surface and prevent common implementation flaws before they reach production.

## Activation

### Activate when

Public interfaces, sensitive data, authentication, automation, dependencies, or release preparation.

### Do not activate when

No software behavior or security posture is involved.

## Required tools and inputs

Assets, trust boundaries, threat actors, data classification, user roles, topology, dependencies, and compliance constraints.

Select language-native tools and verify current official documentation for external SDKs and services before relying on a specific API.

## Recommended architecture

Use defense in depth: secure defaults, identity, authorization, validation, isolation, observability, and recovery. Threat-model data flows before high-risk features.

## Implementation workflow

1. Inventory assets/data. 2. Draw trust boundaries. 3. Identify abuse cases. 4. Prioritize threats. 5. Apply least privilege and validation. 6. Add security tests/scanning. 7. Review secrets and build provenance. 8. Document residual risk and response.

## Coding standards

Use parameterized queries, safe serialization, secure cookies, modern TLS, dependency constraints, and explicit authorization. Fail closed for protected actions.

## Security requirements

Never commit credentials. Never bypass authentication or rate limits. Validate paths, URLs, and subprocess args. Address injection, SSRF, traversal, CSRF, XSS, and unsafe deserialization where relevant. Rotate exposed secrets.

## Error handling and observability

Return generic external errors with sanitized diagnostics. Avoid traces/tokens in user-facing output. Alert on suspicious authorization/automation patterns.

## Testing requirements

Test authentication/authorization, tenant isolation, input edge cases, dependency audit, secret scanning, and secure defaults. Review high-risk changes manually.

## Practical example

~~~python
from pathlib import Path

def resolve_under(root: Path, user_path: str) -> Path:
    base = root.resolve()
    target = (base / user_path).resolve()
    if target != base and base not in target.parents:
        raise ValueError("Path escapes the allowed directory")
    return target
~~~

## Common mistakes and remedies

Do not rely on obscurity, client checks, or model instructions for security. Do not log bearer tokens. Do not suppress findings without owner and rationale.

## Expected outputs

Threat model, secure checklist, automated checks, prioritized findings, and residual-risk notes.

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

Trust boundaries are identified. Secrets are absent. Authorization is server-side. Inputs are constrained. Dependencies are reviewed. Errors are sanitized.
