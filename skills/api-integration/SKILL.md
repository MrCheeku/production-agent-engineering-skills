---
name: api-integration
description: "Build resilient external HTTP integrations with explicit contracts, timeouts, retries, pagination, and observability."
version: "1.0.0"
---

# Api Integration

## Purpose

Make remote services predictable dependencies with documented failure behavior and isolated provider-specific details.

## Activation

### Activate when

Connecting SaaS APIs, web services, payment gateways, identity providers, or internal HTTP services.

### Do not activate when

No remote service is involved.

## Required tools and inputs

API docs/version, authentication, rate limits, pagination, data contract, availability objectives, and sandbox credentials.

Select language-native tools and verify current official documentation for external SDKs and services before relying on a specific API.

## Recommended architecture

Wrap each API in a typed client. Keep DTOs and provider error mapping inside the adapter. Expose application-specific methods rather than raw HTTP responses.

## Implementation workflow

1. Verify official docs and API version. 2. Define request/response models. 3. Centralize auth and base URL. 4. Set connect/read/total timeouts. 5. Add rate-limit-aware bounded retries for safe methods. 6. Implement pagination and cursor validation. 7. Redact logs. 8. Test success, malformed responses, 4xx/5xx, throttling, and network failures.

## Coding standards

Use HTTPS outside controlled local development. Set request IDs where appropriate. Validate status and response size. Avoid leaking provider payloads across domain boundaries.

## Security requirements

Store credentials in a secret manager. Use least-privilege scopes. Prevent SSRF by controlling base URLs and redirects. Validate webhook signatures and replay protection.

## Error handling and observability

Map provider errors to typed outcomes. Honor Retry-After. Retry only idempotent operations or writes with provider idempotency keys. Use circuit breakers only when justified.

## Testing requirements

Use mock transports or sanitized fixtures. Test pagination loops, cursor tampering, timeout, auth failures, rate limiting, and schema drift.

## Practical example

~~~python
import httpx

with httpx.Client(timeout=httpx.Timeout(10.0, connect=3.0)) as client:
    response = client.get("https://api.example.test/v1/status")
    response.raise_for_status()
    payload = response.json()
~~~

## Common mistakes and remedies

Do not use unbounded retries. Do not log Authorization headers. Do not assume every 429/5xx is safe to retry. Do not follow user-controlled URLs without SSRF defenses.

## Expected outputs

Typed API adapter, config schema, error mapping, timeout/retry policy, mock tests, and operational notes.

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

API version is known. Requests time out. Retries are bounded. Credentials are protected. Pagination terminates. Errors are observable.
