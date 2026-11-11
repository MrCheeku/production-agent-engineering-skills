# Production Agent Engineering Skills

> Reusable, production-oriented engineering skills, workflows, tools, and examples for modern AI coding agents.

**Maintainer:** [Mr.Cheeku](https://github.com/MrCheeku)  
**License:** MIT · **Python:** 3.11+

This repository is a practical engineering playbook for AI coding agents and the developers who direct them. It combines actionable skill instructions with reference implementations, validation scripts, and CI examples.

The project takes architectural inspiration from public work such as [Claude Quickstarts](https://github.com/anthropics/claude-quickstarts), [Home Assistant MCP](https://github.com/homeassistant-ai/ha-mcp), [Sherlock](https://github.com/sherlock-project/sherlock), and [Meta Astryx](https://github.com/meta/astryx). It does **not** copy their source code, branding, or documentation.

## Included

- 18 engineering skills: architecture, Python, AI applications, MCP, agent tools, APIs, automation, public username lookup, frontend, design systems, databases, testing, debugging, security, performance, DevOps, documentation, and code review.
- Reference examples for an Anthropic API call, MCP tools, Home Assistant access, public GitHub username lookup, and a responsive design system.
- Templates for Python, FastAPI, MCP, AI-agent, and frontend projects.
- Validators for skill metadata/sections and local Markdown links.
- GitHub Actions for tests, lint, dependency auditing, and Markdown linting.

## Quick start

~~~bash
git clone https://github.com/MrCheeku/production-agent-engineering-skills.git
cd production-agent-engineering-skills
python -m venv .venv
# Windows PowerShell: .venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
python -m pip install -e ".[dev]"
python scripts/validate_skills.py
python scripts/check_links.py
pytest
ruff check .
~~~

## Use a skill with an AI coding agent

1. Choose a task and open the relevant complete file under [skills/](skills/INDEX.md).
2. Provide the file to your coding agent or add it to its project context.
3. Ask the agent to follow the workflow and report assumptions, files changed, commands executed, test results, and unresolved risks.
4. Review generated changes and run checks yourself.

Example instruction:

> Read skills/security-engineering/SKILL.md. Review this repository's authentication flow. Map trust boundaries and report prioritized findings with file references. Do not modify files until I approve the plan.

Skill files are portable Markdown. Automatic discovery and invocation varies by agent and must be configured or verified for the specific agent.

## Skills

See [skills/INDEX.md](skills/INDEX.md) for the complete catalogue.

| Category | Skills |
|---|---|
| Architecture | Software architecture |
| Backend | Python engineering, database engineering, API integration |
| AI systems | AI application development, MCP server development, tool calling and agents |
| Automation & research | Home automation, public username lookup |
| UI | Frontend engineering, design systems |
| Quality | Testing and quality, debugging, code review |
| Operations | Security engineering, performance optimization, DevOps and deployment |
| Knowledge | Documentation |

## Examples

| Example | Purpose |
|---|---|
| [Claude API](examples/claude-api-example/README.md) | Environment-configured Messages API call |
| [MCP tools](examples/mcp-tool-example/README.md) | Bounded arithmetic and text-statistics tools |
| [Home Assistant](examples/home-assistant-integration/README.md) | Entity-filtered reads and confirmed allowlisted light actions |
| [Username CLI](examples/username-search-cli/README.md) | One supplied GitHub username through its public API |
| [Design system](examples/customizable-design-system/README.md) | Responsive accessible UI, tokens, and themes |

Examples are educational starting points, not audited production products. Configure real authentication, access controls, deployment hardening, and monitoring for your environment.

## Validation

~~~bash
python scripts/validate_skills.py
python scripts/check_links.py
python scripts/generate_index.py
pytest
ruff check .
~~~

Read [getting started](docs/getting-started.md), [architecture](docs/architecture.md), and [contribution guidance](CONTRIBUTING.md).

## Security and privacy

Read [SECURITY.md](SECURITY.md). Never commit API keys, Home Assistant tokens, private profile data, or production records. The username example queries only GitHub's public user API and is not an identity-verification tool. It does not bypass controls or evade rate limits.

## Compatibility

These are portable Markdown skills and reference examples. Agent compatibility depends on each tool's current context and skill-discovery conventions. See [agent compatibility](docs/agent-compatibility.md).

## Contributing and license

Contributions are welcome; start with [CONTRIBUTING.md](CONTRIBUTING.md). The project is distributed under the [MIT License](LICENSE).
