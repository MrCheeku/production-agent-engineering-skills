# Contributing

Thank you for helping improve this engineering resource.

## Before opening a change

- Search existing skills/examples to avoid duplication.
- Read the relevant skill and preserve safety/privacy principles.
- Verify current official documentation for SDK-specific guidance.
- Keep examples runnable and free of real credentials.

## Skill requirements

Every new or materially revised skill must include YAML frontmatter and all headings validated by scripts/validate_skills.py. Include concrete steps, domain-specific security rules, failure handling, tests, and expected outputs. Avoid generic advice that could be copied unchanged into unrelated skills.

## Code and documentation

- Python code targets 3.11+ unless a template says otherwise.
- Use type hints and clear exceptions.
- Add/update tests for behavior changes.
- Keep examples independent and document optional credentials.
- Use repository-relative links for internal resources.
- Never commit .env files, tokens, private data, or generated caches.

## Local checks

~~~bash
python -m pip install -e ".[dev]"
python scripts/validate_skills.py
python scripts/check_links.py
pytest
ruff check .
~~~

Describe the problem, intended change, tests run, security/privacy impact, and known limitations in pull requests. Do not claim that a check passed unless it was run.
