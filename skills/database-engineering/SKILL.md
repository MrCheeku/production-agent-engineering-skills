---
name: database-engineering
description: "Design reliable schemas, migrations, transactions, queries, indexes, and backup strategies."
version: "1.0.0"
---

# Database Engineering

## Purpose

Protect data correctness and make persistence observable, evolvable, and recoverable.

## Activation

### Activate when

Creating schemas, writing queries, changing migrations, optimizing DB workloads, or implementing persistence.

### Do not activate when

No storage or query behavior changes.

## Required tools and inputs

Entities/invariants, access patterns, data volume, consistency needs, retention rules, engine, and recovery objectives.

Select language-native tools and verify current official documentation for external SDKs and services before relying on a specific API.

## Recommended architecture

Model authoritative ownership clearly. Keep DB access behind repositories/query services where useful. Migrations are the versioned source of schema truth.

## Implementation workflow

1. Identify entities, relations, and invariants. 2. Choose types/constraints. 3. Design migration/rollback. 4. Use parameterized queries and explicit transactions. 5. Add indexes based on query plans. 6. Test concurrency and migrations. 7. Define backups and restore drills. 8. Monitor latency, locks, and growth.

## Coding standards

Use foreign keys, uniqueness, not-null, and check constraints for invariants. Use UTC timestamps. Avoid derived values unless consistency rules are clear. Keep migrations small.

## Security requirements

Use least-privilege DB accounts, encrypted connections, parameterized queries, tenant scoping, and encrypted backups. Do not log sensitive rows.

## Error handling and observability

Handle rollback, deadlocks, pool exhaustion, constraint failures, and unavailable replicas distinctly. Retry only safe transactions.

## Testing requirements

Test constraints, migrations, rollback, concurrent writes, pagination stability, and critical query plans.

## Practical example

~~~python
cursor.execute("SELECT id, email FROM users WHERE id = %s", (user_id,))
~~~

## Common mistakes and remedies

Do not interpolate user values into SQL. Do not rely only on application validation for invariants. Do not add indexes without considering write/storage cost.

## Expected outputs

ER diagram, migrations, query notes, access layer, backup/restore procedure, and integrity tests.

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

Constraints protect invariants. Queries are parameterized. Migrations are tested. Transactions are bounded. Backups can be restored.
