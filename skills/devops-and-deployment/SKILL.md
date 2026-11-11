---
name: devops-and-deployment
description: "Package, configure, deploy, observe, and roll back applications through repeatable, secure workflows."
version: "1.0.0"
---

# Devops And Deployment

## Purpose

Make releases predictable and recoverable from development through production.

## Activation

### Activate when

Creating CI/CD, containers, deployment manifests, release automation, environments, or runbooks.

### Do not activate when

No deployment/runtime impact.

## Required tools and inputs

Runtime, environments, secrets provider, target, health checks, scaling model, SLOs, and rollback requirements.

Select language-native tools and verify current official documentation for external SDKs and services before relying on a specific API.

## Recommended architecture

Build immutable artifacts once and promote them across environments. Keep config external to images. Separate readiness and liveness checks.

## Implementation workflow

1. Define build/runtime requirements. 2. Create reproducible build. 3. Add lint/tests/security/artifact checks to CI. 4. Scan dependencies/images. 5. Deploy staging. 6. Run smoke/migration checks. 7. Promote controlled rollout. 8. Verify health/metrics. 9. Roll back using tested procedure.

## Coding standards

Use least-privilege CI permissions, pinned action versions or immutable SHAs, short-lived credentials, timeouts, and immutable image tags.

## Security requirements

Do not expose CI secrets to untrusted PR code. Restrict environments and approvals. Generate provenance where practical. Protect registries and production credentials.

## Error handling and observability

Fail fast on invalid config. Make deployment idempotent. Separate rollback from irreversible data migration. Document degraded mode and escalation.

## Testing requirements

Validate workflow syntax, build reproducibility, container health, migration compatibility, secret absence, and rollback in non-production.

## Practical example

~~~dockerfile
FROM python:3.12-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir .
USER 10001
CMD ["python", "-m", "your_package"]
~~~

## Common mistakes and remedies

Do not use latest as a production tag. Do not deploy unreviewed branches. A green build does not prove runtime health.

## Expected outputs

CI pipeline, deployment config, env contract, health checks, release checklist, and rollback runbook.

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

Artifacts are reproducible. CI permissions are minimal. Secrets are external. Health checks exist. Rollback is tested.
