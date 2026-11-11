---
name: design-systems
description: "Create scalable, accessible design systems with tokens, documented components, variants, and themes."
version: "1.0.0"
---

# Design Systems

## Purpose

Make visual consistency measurable without forcing every surface into an inflexible component library.

## Activation

### Activate when

Creating a design language, shared components, tokens, themes, or design-to-code workflow.

### Do not activate when

A disposable prototype does not need reusable constraints.

## Required tools and inputs

Brand principles, current UI inventory, platform targets, accessibility needs, theme needs, and design source of truth.

Select language-native tools and verify current official documentation for external SDKs and services before relying on a specific API.

## Recommended architecture

Organize foundations, semantic tokens, component tokens, primitives, patterns, and documentation. Keep raw palette values separate from semantic roles.

## Implementation workflow

1. Audit existing UI. 2. Define token naming and semantic roles. 3. Establish type/color/spacing/radius/elevation/motion scales. 4. Build accessible primitives. 5. Document variants and states. 6. Support themes without duplicating components. 7. Add visual examples. 8. Publish versioning and migrations.

## Coding standards

Prefer semantic tokens such as surface, text-primary, border-muted, and action-primary. Define APIs around use cases. Include focus, disabled, hover, active, and invalid states.

## Security requirements

Do not embed secrets in theme/build config. Validate remote assets. Keep font/icon licenses and attribution.

## Error handling and observability

Provide visual fallbacks for missing tokens/assets. Deprecate tokens with migration paths instead of silently changing semantics.

## Testing requirements

Test token completeness, contrast, keyboard behavior, component variants, responsive rendering, and theme parity. Snapshot representative states.

## Practical example

~~~css
:root { --surface: #fff; --text: #172033; --action: #2457d6; --space-2: .5rem; }
[data-theme="dark"] { --surface: #111827; --text: #f4f6fb; }
~~~

## Common mistakes and remedies

Do not expose raw palette names as semantic roles. Do not make a variant for every tiny difference. Do not ignore contrast and focus rings.

## Expected outputs

Token definitions, component APIs, theme examples, design docs, visual tests, and version guidance.

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

Tokens are semantic. Contrast is checked. States are documented. Themes share component structure. Changes have migration notes.
