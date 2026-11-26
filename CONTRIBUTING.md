# Contributing

Thanks for contributing to Production Agent Engineering Skills.

## Local development

Use Python 3.11 or newer. Install the development tools and run the same checks used in CI:

```bash
python -m pip install -e ".[dev]"
python scripts/validate_skills.py
python scripts/check_links.py
ruff check .
pytest
```

## Skill authoring

- Keep each skill in `skills/<skill-name>/SKILL.md`.
- Use the required YAML frontmatter and section structure described in the existing skills.
- Keep guidance provider-aware, testable, and explicit about permissions and approval boundaries.
- Do not present a tool description as authorization to access an account, device, filesystem, or network.
- Include error handling, privacy, security, and testing guidance.
- Update `skills/INDEX.md` by running `python scripts/generate_index.py` when adding a skill.

## Pull requests

Describe the problem, solution, validation performed, and any remaining limitations. Never include real credentials, API keys, private personal data, or working exploit secrets in examples.
