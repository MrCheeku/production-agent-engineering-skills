---
name: software-architecture
description: "Design modular, testable systems with explicit boundaries, documented decisions, and operational constraints."
version: "1.0.0"
---

# Software Architecture

## Purpose

Turn ambiguous product requests into system designs that can be implemented, tested, operated, and changed safely. Prefer understandable boundaries over unnecessary infrastructure.

## Activation

### Activate when

A new product is being designed, a feature crosses modules, service boundaries are changing, or an unfamiliar codebase needs structural review.

### Do not activate when

A small isolated bug fix or local refactor does not change module contracts.

## Required tools and inputs

User journeys, functional requirements, quality attributes, data sensitivity, scale assumptions, ownership, deployment model, and failure requirements.

Select language-native tools and verify current official documentation for external SDKs and services before relying on a specific API.

## Recommended architecture

Prefer a modular monolith until independent deployment, scaling, ownership, or reliability needs justify services. Separate domain rules, application orchestration, adapters, and delivery interfaces. Define dependency direction and data ownership.

## Implementation workflow

1. Clarify actors, use cases, constraints, and failure conditions. 2. Record functional and non-functional requirements. 3. Draw a context and container diagram. 4. Identify domain boundaries and data ownership. 5. Define interfaces and error contracts. 6. Compare options and record consequential decisions as ADRs. 7. Build one vertical slice. 8. Validate boundaries against real change requests.

## Coding standards

Prefer explicit interfaces, cohesive modules, dependency inversion, stable contracts, and boring technology. Document invariants. Avoid abstractions with only one trivial implementation. Make migrations and compatibility changes explicit.

## Security requirements

Map trust boundaries and sensitive data flows. Apply least privilege, tenant isolation, secrets management, and threat modeling. Do not treat internal networks as trusted by default.

## Error handling and observability

Define errors at boundaries and translate low-level failures into stable domain errors. Set remote timeouts; use bounded retries only for safe operations. Design degraded behavior for optional dependencies. Use correlation IDs without logging secrets.

## Testing requirements

Test domain rules without infrastructure, adapter contracts with fakes or containers, and critical user journeys end-to-end. Add architecture tests for meaningful dependency constraints.

## Practical example

~~~text
A billing module owns invoice state transitions. A payment-provider adapter implements capture/refund interfaces. HTTP handlers validate requests and map results; they do not implement billing rules.
~~~

## Common mistakes and remedies

Do not split services just because a diagram looks cleaner. Do not share database tables across purported service boundaries. Do not let controllers become the domain layer.

## Expected outputs

Context/container diagrams, module map, interface contracts, ADRs, dependency plan, and a testable vertical slice.

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

Every module has a clear reason to change. Data ownership is explicit. Trust boundaries are documented. Failure modes are designed. Trade-offs are recorded.
