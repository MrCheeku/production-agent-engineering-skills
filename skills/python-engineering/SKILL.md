---
name: python-engineering
description: "Build maintainable Python packages, services, and CLIs with typing, packaging, testing, and observability."
version: "1.0.0"
---

# Python Engineering

## Purpose

Produce Python that is predictable across developer machines, CI, and production.

## Activation

### Activate when

Creating Python packages, APIs, automation tools, CLIs, background jobs, or Python integrations.

### Do not activate when

The task does not involve Python or only needs a disposable short snippet.

## Required tools and inputs

Supported Python versions, target OS, runtime model, dependencies, CLI/API contract, deployment environment, and input constraints.

Select language-native tools and verify current official documentation for external SDKs and services before relying on a specific API.

## Recommended architecture

Use a src/ package layout for distributable code, keep CLI entry points thin, isolate I/O behind adapters, and put business logic in ordinary functions/classes. Declare build metadata and optional extras in pyproject.toml.

## Implementation workflow

1. Confirm supported Python versions. 2. Create pyproject.toml and src layout. 3. Add type annotations and config parsing. 4. Separate pure logic from I/O. 5. Add structured logging and explicit exceptions. 6. Test normal, boundary, and failure cases. 7. Run lint/type/package checks. 8. Verify installation in a clean environment.

## Coding standards

Use descriptive names, pathlib, context managers, explicit public return types, and typed models. Avoid mutable defaults, broad except clauses, hidden global state, and import-time side effects.

## Security requirements

Read secrets from environment or a secret manager. Validate paths and input. Never use eval on user input. Avoid shell=True; pass argument arrays and set timeouts. Audit dependencies.

## Error handling and observability

Raise domain-specific exceptions with actionable context. Catch only errors that can be handled at the current layer. Preserve causes with raise from. Keep machine-readable stdout clean and send diagnostics to stderr.

## Testing requirements

Use pytest. Test pure functions first, then adapters with fakes/mock transports. Cover invalid input, timeouts, permission errors, and supported platforms. Avoid live internet and real credentials in CI.

## Practical example

~~~python
from pathlib import Path

def load_text(path: Path) -> str:
    if not path.is_file():
        raise FileNotFoundError(path)
    return path.read_text(encoding="utf-8")
~~~

## Common mistakes and remedies

Do not put all logic in __main__.py. Do not catch Exception and continue silently. Do not commit virtual environments or .env files. Do not claim type safety without running a checker.

## Expected outputs

Documented package layout, pyproject, typed implementation, entry point, tests, and reproducible commands.

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

Clean install works. Public functions are typed. Inputs are validated. Exceptions are intentional. Tests run offline. Logs contain no secrets.
