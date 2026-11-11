---
name: frontend-engineering
description: "Build responsive, accessible, maintainable frontend experiences with clear state boundaries and performance budgets."
version: "1.0.0"
---

# Frontend Engineering

## Purpose

Deliver interfaces that work across devices, assistive technologies, slow networks, and changing requirements.

## Activation

### Activate when

Building/refactoring pages, components, client workflows, or frontend architecture.

### Do not activate when

Backend-only changes have no UI impact.

## Required tools and inputs

User journeys, supported browsers, viewport needs, design references, accessibility target, loading states, and performance budget.

Select language-native tools and verify current official documentation for external SDKs and services before relying on a specific API.

## Recommended architecture

Separate page composition, reusable components, view models, API adapters, and state. Prefer server rendering/static output when it improves product performance.

## Implementation workflow

1. Map journeys and empty/loading/error states. 2. Define semantic structure. 3. Establish tokens and component contracts. 4. Implement mobile-first layouts. 5. Add accessible interactions. 6. Integrate typed API states. 7. Measure bundle/render/interaction performance. 8. Verify target browsers and screen readers.

## Coding standards

Use semantic HTML, labels, visible focus, meaningful headings, responsive units, and reusable components. Avoid excess global state and one-off CSS. Prefer progressive enhancement.

## Security requirements

Escape untrusted content, avoid unsafe HTML injection, validate navigation targets, protect routes on the server, and keep secrets out of client bundles.

## Error handling and observability

Represent loading, empty, stale, success, and error states explicitly. Provide actionable recovery and do not discard unsaved work silently.

## Testing requirements

Test behavior using component/browser tests. Cover keyboard-only usage, responsive breakpoints, form validation, loading/error states, and screen-reader semantics.

## Practical example

~~~html
<label for="email">Email address</label>
<input id="email" name="email" type="email" autocomplete="email" required>
<button type="submit">Continue</button>
~~~

## Common mistakes and remedies

Do not use clickable divs when a button or link is appropriate. Do not communicate state with color alone. Do not ship unbounded animation or huge bundles.

## Expected outputs

Responsive pages, reusable components, typed UI states, accessibility checks, and measured performance.

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

Keyboard works. Inputs have labels. Narrow layouts work. Errors are visible. Secrets are server-side. Performance is measured.
