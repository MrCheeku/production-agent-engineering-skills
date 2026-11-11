# Getting started

1. Open the [skill index](../skills/INDEX.md) and choose the smallest relevant skill set.
2. Provide the complete SKILL.md to your coding agent or add it to its supported project context.
3. Ask the agent to inspect the repository and state its plan before broad changes.
4. Require a report of files changed, assumptions, commands run, test results, risks, and gaps.
5. Review the patch and run checks in the target environment.

~~~bash
python -m pip install -e ".[dev]"
python scripts/validate_skills.py
python scripts/check_links.py
pytest
ruff check .
~~~

A generated patch is not production-ready until reviewed and tested in the target environment.
