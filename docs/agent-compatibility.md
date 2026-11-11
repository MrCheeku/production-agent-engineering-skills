# Agent compatibility

## Format

Every skill is plain Markdown with YAML frontmatter fields name, description, and version.

## Using skills

An agent can use a skill when it can read repository files or when the user includes the skill in context. Provide the complete relevant file for each task.

## Automatic discovery

Automatic discovery differs by agent and changes over time. This repository does not claim native support for a specific agent. If an agent documents a skill-directory convention, verify its current official documentation and create a reviewed adapter for that exact convention.

## Suggested instruction

"Read skills/api-integration/SKILL.md before changing the payment-provider adapter. Follow its workflow, inspect existing conventions, and report assumptions and test results. Do not expose secrets or perform a live transaction."
