# Public username lookup CLI

Checks one user-supplied GitHub username through GitHub's public user API. Returns the public profile URL, public repository count, and creation timestamp when available. It does not search other sites or identify a person.

~~~bash
python -m pip install -r requirements.txt
python search.py octocat
python search.py octocat --json
python search.py --version
~~~

A 404 is reported as not found; 403/429 is blocked or rate limited; a timeout is unknown, not proof of absence. Use only for a legitimate purpose and follow current API terms/rate limits. Do not automate mass profiling or evade access controls. Tests use mocked HTTP responses only.
