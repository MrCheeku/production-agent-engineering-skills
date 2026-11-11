---
name: performance-optimization
description: "Improve latency, throughput, memory, and cost using measurements, workload models, and regression budgets."
version: "1.0.0"
---

# Performance Optimization

## Purpose

Optimize the bottleneck that matters to users without sacrificing correctness or maintainability.

## Activation

### Activate when

A measurable latency, throughput, resource, bundle-size, or infrastructure-cost concern exists.

### Do not activate when

No performance objective or symptom has been identified.

## Required tools and inputs

Workload, user-facing SLO, baseline metrics, representative data, runtime limits, and cost constraints.

Select language-native tools and verify current official documentation for external SDKs and services before relying on a specific API.

## Recommended architecture

Instrument request boundaries, DB calls, queues, caches, and resources. Keep optimization changes local to measured hot paths.

## Implementation workflow

1. Define the user-visible metric. 2. Capture baseline. 3. Profile CPU/memory/I/O/network. 4. Identify bottleneck. 5. Form measurable hypothesis. 6. Change one factor. 7. Benchmark comparably. 8. Add regression budget and monitor.

## Coding standards

Prefer algorithmic improvements before premature caching/concurrency. Bound queues and payloads. Document cache invalidation and consistency.

## Security requirements

Do not weaken authorization, validation, encryption, or audit logging for speed. Avoid untrusted cache keys and cross-tenant leaks.

## Error handling and observability

Use timeouts, backpressure, bounded concurrency, and graceful degradation. Avoid resource-exhaustion retry storms.

## Testing requirements

Benchmark representative inputs and repeat runs. Include cold/warm behavior where relevant. Test invalidation, concurrency, worst-case input, and memory growth.

## Practical example

~~~python
from time import perf_counter
start = perf_counter()
result = expensive_operation()
elapsed_ms = (perf_counter() - start) * 1000
~~~

## Common mistakes and remedies

Do not trust one noisy run. Do not cache without invalidation rules. Do not raise worker counts without checking downstream capacity.

## Expected outputs

Baseline, profiler evidence, targeted change, benchmark comparison, and monitoring thresholds.

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

Metric is defined. Baseline is repeatable. Bottleneck is evidenced. Correctness is preserved. Regression is monitored.
