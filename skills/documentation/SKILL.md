---
name: documentation
description: "Write accurate, task-oriented documentation for installation, operation, troubleshooting, and contribution."
version: "1.0.0"
---

# Documentation

## Purpose

Keep documentation aligned with actual behavior so readers can complete tasks without guessing.

## Activation

### Activate when

Creating/changing README, API reference, runbooks, architecture docs, onboarding, or release notes.

### Do not activate when

No documentation contract is affected.

## Required tools and inputs

Actual code behavior, supported environments, commands, config, audience, terminology, and limitations.

Select language-native tools and verify current official documentation for external SDKs and services before relying on a specific API.

## Recommended architecture

Organize docs by task: quick start, concepts, reference, operations, troubleshooting, contributions. Keep examples near features and link to one source of truth.

## Implementation workflow

1. Identify reader/task. 2. Verify behavior from source or execution. 3. Write prerequisites/copyable steps. 4. Include expected output/troubleshooting. 5. Link related topics. 6. Check links/snippets. 7. Review stale claims after changes.

## Coding standards

Use direct language, consistent terms, runnable examples, explicit versions, and warnings. Distinguish required from optional. Avoid unverified support claims.

## Security requirements

Never include working credentials, personal data, internal endpoints, or sensitive logs. Use fake placeholders and explain secret handling.

## Error handling and observability

Document common errors with cause, evidence, and safe remediation. Do not recommend disabling security as a general workaround.

## Testing requirements

Run documented commands in a clean environment where practical. Validate internal links and snippets. Compare install steps with package metadata.

## Practical example

~~~bash
python -m venv .venv
python -m pip install -e ".[dev]"
python scripts/validate_skills.py
~~~

## Common mistakes and remedies

Do not present a plan as implemented. Do not list untested commands as verified. Remove obsolete screenshots and version claims.

## Expected outputs

Task-oriented docs, accurate examples, link checks, troubleshooting, and changelog entries.

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

Audience is clear. Commands are verified. Limitations are stated. Links resolve. No secrets appear.
