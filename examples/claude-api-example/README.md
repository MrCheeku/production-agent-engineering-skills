# Claude API example

A minimal Python example using the official Anthropic SDK. Credentials and model selection come from environment variables.

## Run

~~~bash
python -m pip install -r requirements.txt
# Set ANTHROPIC_API_KEY and ANTHROPIC_MODEL in your shell.
python app.py
~~~

Offline tests:

~~~bash
python -m pip install pytest
pytest -q
~~~

The model must be available to your account. Verify current SDK/API documentation before changing request parameters. Do not print or commit your API key.
