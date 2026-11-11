.PHONY: install test lint validate links index check

install:
	python -m pip install -e ".[dev]"

test:
	pytest

lint:
	ruff check .

validate:
	python scripts/validate_skills.py

links:
	python scripts/check_links.py

index:
	python scripts/generate_index.py

check: validate links lint test
