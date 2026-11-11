---
name: osint-public-username-search
description: "Conduct narrow public username lookups against approved endpoints while documenting uncertainty and respecting privacy."
version: "1.0.0"
---

# Osint Public Username Search

## Purpose

Provide limited public-profile discovery for a supplied username. A match is a lead, not proof that accounts belong to one person.

## Activation

### Activate when

A user explicitly asks to check a supplied username against public profiles or approved public APIs.

### Do not activate when

The objective is to identify an anonymous person, obtain private data, bypass controls, stalk, harass, or compile a sensitive dossier.

## Required tools and inputs

User-supplied handle, approved endpoints, legitimate purpose, applicable terms/law, request budget, and retention policy.

Select language-native tools and verify current official documentation for external SDKs and services before relying on a specific API.

## Recommended architecture

Use an allowlist of public endpoints, one adapter per platform, bounded HTTP client, and normalized result containing URL, status, retrieval time, and confidence.

## Implementation workflow

1. Confirm legitimate purpose and exact handle. 2. Select approved public endpoints only. 3. Normalize input without guessing variants. 4. Send bounded requests through documented APIs/permitted pages. 5. Distinguish found, absent, blocked, rate-limited, and unknown. 6. Record source URLs and timestamps. 7. Explain false-positive risk. 8. Delete transient data when no longer needed.

## Coding standards

Use platform allowlists and conservative request budgets. Do not infer identity from matching handles. Avoid collecting unnecessary profile fields.

## Security requirements

Do not access private accounts, bypass login, evade CAPTCHAs, rotate proxies to evade limits, or scrape sensitive data. Respect terms and law. Do not publish dossiers.

## Error handling and observability

403/429/CAPTCHA/bot detection means blocked or rate-limited; stop instead of bypassing. Timeout is unknown, not absent. Preserve timestamps and source references.

## Testing requirements

Use mocked responses. Test 200, 404, 403, 429, timeout, malformed JSON, redirects, and input validation. CI must not query real social networks.

## Practical example

~~~python
from dataclasses import dataclass

@dataclass(frozen=True)
class PublicLookup:
    platform: str
    profile_url: str
    status: str  # found, absent, blocked, or unknown
    checked_at: str
~~~

## Common mistakes and remedies

Do not claim confirmed identity. Do not scan private surfaces. Do not evade limits. Do not retain or publish unnecessary personal information.

## Expected outputs

A bounded public lookup result with source URLs, timestamps, limitations, and retention decision.

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

Purpose is legitimate. Endpoints are allowlisted. Requests are limited. Blocks are not bypassed. Findings are qualified, not identity proof.
