# Production Agent Engineering Skills

> A collection of reusable, production-grade engineering skills, workflows, tools, and instructions for modern AI coding agents.

[![CI](https://github.com/MrCheeku/production-agent-engineering-skills/actions/workflows/ci.yml/badge.svg)](https://github.com/MrCheeku/production-agent-engineering-skills/actions/workflows/ci.yml)

**Maintainer:** [Mr.Cheeku](https://github.com/MrCheeku) · **License:** [MIT](LICENSE) · **Python:** 3.11+

Production Agent Engineering Skills is a practical engineering playbook for AI coding agents and the developers who direct them. It pairs task-oriented Markdown skills with runnable reference examples, project templates, and repository checks. The goal is to support thoughtful, testable engineering—not to replace human review or claim that generated changes are automatically production-ready.

The repository is independently written and takes architectural inspiration from public projects such as [Claude Quickstarts](https://github.com/anthropics/claude-quickstarts), [Home Assistant MCP](https://github.com/homeassistant-ai/ha-mcp), [Sherlock](https://github.com/sherlock-project/sherlock), and [Meta Astryx](https://github.com/meta/astryx). It does not include their source code, branding, or assets.

## What’s inside

- **18 engineering skills** covering architecture, Python, AI applications, MCP, APIs, automation, UI, data, quality, security, operations, documentation, and review.
- **Runnable examples** for an Anthropic API integration, MCP tools, permission-controlled Home Assistant operations, a public GitHub username lookup CLI, and a responsive design system.
- **Starter templates** for Python, FastAPI, MCP, AI-agent, and frontend projects.
- **Validation tools and tests** for skill metadata and structure, documentation links, and project behavior.
- **GitHub Actions** for automated validation, lint, tests, and security-related checks.

## Skills

Browse the full [skill index](skills/INDEX.md). Each skill explains when to use it, recommended workflows, coding and security requirements, testing expectations, examples, and readiness checklists.

| Category | Skills |
|---|---|
| Architecture | [Software architecture](skills/software-architecture/SKILL.md) |
| Backend | [Python engineering](skills/python-engineering/SKILL.md), [Database engineering](skills/database-engineering/SKILL.md), [API integration](skills/api-integration/SKILL.md) |
| AI systems | [AI application development](skills/ai-application-development/SKILL.md), [MCP server development](skills/mcp-server-development/SKILL.md), [Tool calling and agents](skills/tool-calling-and-agents/SKILL.md) |
| Automation & research | [Home automation](skills/home-automation/SKILL.md), [Public username search](skills/osint-public-username-search/SKILL.md) |
| UI | [Frontend engineering](skills/frontend-engineering/SKILL.md), [Design systems](skills/design-systems/SKILL.md) |
| Quality | [Testing and quality](skills/testing-and-quality/SKILL.md), [Debugging](skills/debugging/SKILL.md), [Code review](skills/code-review/SKILL.md) |
| Operations | [Security engineering](skills/security-engineering/SKILL.md), [Performance optimization](skills/performance-optimization/SKILL.md), [DevOps and deployment](skills/devops-and-deployment/SKILL.md) |
| Knowledge | [Documentation](skills/documentation/SKILL.md) |

## Quick start

Clone the repository and install its development dependencies in a virtual environment:

~~~bash
git clone https://github.com/MrCheeku/production-agent-engineering-skills.git
cd production-agent-engineering-skills
python -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -e ".[dev]"
~~~

Run the repository checks:

~~~bash
python scripts/validate_skills.py
python scripts/check_links.py
pytest
ruff check .
~~~

See [Getting started](docs/getting-started.md), [Installation](docs/installation.md), and [Architecture](docs/architecture.md) for additional guidance.

## Use a skill with a coding agent

1. Select the smallest relevant skill set from the [skill index](skills/INDEX.md).
2. Give your coding agent the complete `SKILL.md` file(s), or configure them in the agent’s supported project context.
3. Ask the agent to inspect the codebase first, state assumptions and a plan, then make a focused change.
4. Review the resulting diff and run relevant checks in your own environment.
5. Ask for a report of files changed, commands actually run, test results, unresolved risks, and work not completed.

Example request:

> Read `skills/security-engineering/SKILL.md`. Review this repository’s authentication flow. Map the trust boundaries and report prioritized findings with file references. Do not modify files until I approve the proposed changes.

Skills are portable Markdown guidance. Automatic discovery, invocation, and compatibility vary by agent; see [Agent compatibility](docs/agent-compatibility.md) and verify your chosen agent’s current conventions.

## Reference examples

| Example | What it demonstrates | Guide |
|---|---|---|
| Anthropic API | Environment-based configuration and a Python API call | [Run instructions](examples/claude-api-example/README.md) |
| MCP tools | A small server with bounded, validated tools | [Run instructions](examples/mcp-tool-example/README.md) |
| Home Assistant | Entity-scoped reads and explicitly authorized allowlisted actions | [Run instructions](examples/home-assistant-integration/README.md) |
| Username lookup CLI | A narrow lookup against GitHub’s public user API | [Run instructions](examples/username-search-cli/README.md) |
| Design system | Reusable responsive UI, design tokens, and themes | [Run instructions](examples/customizable-design-system/README.md) |

Examples are educational reference implementations, not audited production services. Follow each example’s setup guide, protect credentials, and add environment-specific access controls, monitoring, and tests before deploying.

## Security and privacy

Security is part of every skill. The examples avoid embedded credentials and bound potentially sensitive operations. The username lookup is limited to publicly accessible GitHub profile information; it is not a general-purpose people-search system. Respect service terms, applicable law, rate limits, privacy, and consent. Read [SECURITY.md](SECURITY.md) for safe development and vulnerability-reporting guidance. Never commit API keys, access tokens, private profile data, or production records.

## Contributing

Contributions are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md), follow the repository’s `AGENTS.md` guidance, and run the relevant checks before opening a pull request. The [roadmap](ROADMAP.md) describes areas for future improvement.

## License

This project is distributed under the [MIT License](LICENSE).
