---
name: home-automation
description: "Connect AI assistants to home devices using explicit entity allowlists, user confirmation, and least-privilege credentials."
version: "1.0.0"
---

# Home Automation

## Purpose

Make automation useful without permitting arbitrary device changes, hidden monitoring, or unsafe physical actions.

## Activation

### Activate when

Connecting assistants or services to Home Assistant or another smart-home platform.

### Do not activate when

Only a static UI mock or non-device data transform is needed.

## Required tools and inputs

Platform URL, limited token, allowed entities/services, device criticality, network model, and approval policy.

Select language-native tools and verify current official documentation for external SDKs and services before relying on a specific API.

## Recommended architecture

Separate Home Assistant client, policy/allowlist layer, MCP/application adapter, and UI confirmation flow. Distinguish reads from state-changing actions.

## Implementation workflow

1. Inventory needed entities and minimum scopes. 2. Validate URL/token config. 3. Expose read-only status first. 4. Add strict domain/service/entity allowlists. 5. Require confirmation for writes. 6. Set timeouts and audit actions. 7. Test denied entities and unsafe combinations. 8. Roll out to non-critical devices first.

## Coding standards

Use stable entity IDs, explicit schemas, and clear device labels. Report uncertainty rather than inferring state. Never expose every entity by default.

## Security requirements

Use a dedicated least-privilege token. Protect it. Do not expose locks, alarms, garage doors, cameras, or safety-critical controls without separate threat review. Keep approval outside model control.

## Error handling and observability

Treat unreachable devices, stale state, and rejected services distinctly. Do not claim success until the API confirms it. Include sanitized timestamps and entity identifiers in logs.

## Testing requirements

Mock HTTP responses. Verify allowlists, domain matching, missing confirmation, expired tokens, timeouts, and service failures. Never test real household devices in CI.

## Practical example

~~~python
def may_control(entity_id: str, service: str, approved: bool) -> bool:
    allowed = {"light.desk_lamp": {"turn_on", "turn_off"}}
    return approved and service in allowed.get(entity_id, set())
~~~

## Common mistakes and remedies

Do not expose a generic service-call tool. Do not assume all listed entities are safe. Do not enable cameras or locks without separate approval.

## Expected outputs

Scoped API client, entity/service policy, approval flow, audit events, and mocked tests.

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

Only allowlisted entities are available. Writes require approval. Tokens are protected. Timeouts exist. Unsafe control is off by default.
