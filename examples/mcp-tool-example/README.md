# MCP tools example

Uses the MCP Python SDK v2 API. It exposes bounded arithmetic evaluation with an AST allowlist and text statistics.

~~~bash
python -m pip install -r requirements.txt
python server.py
~~~

The server uses the SDK's default local stdio transport. Configure it in an MCP host using that host's current documentation. Do not run it with arbitrary elevated permissions.

Run tests with pytest -q. The arithmetic tool does not use eval or execute Python. Extend only with narrow capabilities, server-side authorization, and tests. Verify SDK v2 docs before upgrading or changing transports.
