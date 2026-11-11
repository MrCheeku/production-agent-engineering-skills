---
name: ai-application-development
description: "Engineer reliable model-powered applications with schemas, streaming, provider adapters, and measurable quality."
version: "1.0.0"
---

# Ai Application Development

## Purpose

Integrate model capabilities as one dependency in a product instead of spreading provider-specific request code throughout the application.

## Activation

### Activate when

Adding model inference, chat, extraction, summarization, retrieval, streaming, structured output, or a model-backed workflow.

### Do not activate when

A deterministic rule or ordinary database query fully solves the requirement.

## Required tools and inputs

Task definition, provider constraints, allowed data, model access, latency/cost budgets, output contract, eval examples, and fallback requirements.

Select language-native tools and verify current official documentation for external SDKs and services before relying on a specific API.

## Recommended architecture

Use an application-level model interface with provider adapters. Keep prompts and schemas versioned. Separate orchestration, provider transport, tool execution, persistence, and evaluation.

## Implementation workflow

1. Define success metrics and representative evals. 2. Choose a model using quality, latency, cost, and data policy. 3. Define input/output schemas. 4. Implement an adapter with timeouts and retries. 5. Add streaming only when useful. 6. Validate structured output. 7. Add refusal, fallback, and human-review paths. 8. Measure quality, latency, tokens, and cost.

## Coding standards

Keep system instructions separate from user data. Treat model output as untrusted. Prefer constrained schemas. Version prompts and evaluate changes. Make requests idempotent where possible.

## Security requirements

Minimize sensitive data sent to providers, redact telemetry, restrict tool availability, defend against prompt injection, and enforce authorization outside the model. Model claims of authorization are never sufficient.

## Error handling and observability

Handle auth, rate limits, timeouts, overload, invalid requests, truncation, refusal, and schema failures distinctly. Use bounded exponential backoff with jitter only for retryable failures. Never blindly retry non-idempotent actions.

## Testing requirements

Use deterministic tests with mocked adapters, provider contract tests, and offline eval fixtures. Test malformed output, prompt injection, refusal, long context, and empty responses.

## Practical example

~~~python
from typing import Protocol

class TextGenerator(Protocol):
    def generate(self, prompt: str) -> str: ...

def extract_title(generator: TextGenerator, document: str) -> str:
    title = generator.generate("Return one concise title:\\n" + document).strip()
    if not title or len(title) > 120:
        raise ValueError("Invalid model title")
    return title
~~~

## Common mistakes and remedies

Do not use a model for authorization or exact arithmetic. Do not trust free-form output as JSON. Do not hide cost, retries, or model changes. Do not send unnecessary data.

## Expected outputs

Provider-neutral boundary, provider adapter, prompt/schema versions, eval set, telemetry plan, and failure/review paths.

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

Inputs are minimized. Outputs are validated. Costs and latency are measured. Provider errors are mapped. Tool permissions are enforced in application code.
