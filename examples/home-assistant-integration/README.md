# Home Assistant integration example

This client filters reads to an entity allowlist and only permits two light services. State changes require an explicit confirmation flag from the calling application.

Install and run offline tests:

~~~bash
python -m pip install -r requirements.txt
pytest -q
~~~

Create the client with the base URL, a dedicated token, and a small list of allowed entity IDs. HTTP is supported for local network use; use HTTPS or a trusted private network and configure TLS for untrusted paths.

This demo intentionally excludes locks, alarms, garage doors, cameras, and arbitrary services. The boolean confirmation is not a substitute for a real authenticated approval workflow.
