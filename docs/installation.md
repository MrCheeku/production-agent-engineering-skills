# Installation

The skills are Markdown files and can be used without installing this Python project.

## Use skills directly

Clone or download the repository and provide the required complete file under skills/ to your coding agent or add it to its supported project context.

## Install validation tools

Python 3.11 or later is required.

~~~bash
python -m venv .venv
python -m pip install -e ".[dev]"
~~~

## Optional examples

~~~bash
python -m pip install -e ".[ai-example]"
python -m pip install -e ".[mcp-example]"
python -m pip install -e ".[home-assistant-example]"
python -m pip install -e ".[username-cli]"
~~~

Each example has a README. Supply credentials/endpoints locally; never commit them.
