# Repository architecture

- skills/: agent-readable engineering workflows.
- templates/: starting points for common project types.
- examples/: small implementations illustrating selected skills.
- scripts/: maintenance and validation commands.
- src/agent_skills/: reusable validation logic.
- tests/: offline tests for validators and pure example behavior.
- docs/: onboarding, architecture, and compatibility guidance.
- .github/: automated quality checks and contribution templates.

The core package has no runtime dependencies. Optional example dependencies are declared as extras. Skill files guide agents but do not grant permissions. Authorization, confirmation, and policy enforcement belong in deterministic application code. Tool outputs and external content are untrusted data.
