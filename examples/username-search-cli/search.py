from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict, dataclass

import httpx

VERSION = "0.1.0"
API_ROOT = "https://api.github.com"


@dataclass(frozen=True)
class LookupResult:
    username: str
    status: str
    profile_url: str | None = None
    public_repos: int | None = None
    created_at: str | None = None
    message: str | None = None


def lookup_github_username(username: str, client: httpx.Client | None = None) -> LookupResult:
    value = username.strip()
    if not value or len(value) > 39 or not value.replace("-", "").isalnum():
        raise ValueError("Provide a valid GitHub username")
    owns_client = client is None
    active = client or httpx.Client(
        base_url=API_ROOT,
        headers={"Accept": "application/vnd.github+json", "User-Agent": "public-username-lookup"},
        timeout=httpx.Timeout(8.0, connect=3.0),
        follow_redirects=False,
    )
    try:
        response = active.get(f"/users/{value}")
        if response.status_code == 404:
            return LookupResult(value, "not_found")
        if response.status_code in {403, 429}:
            return LookupResult(value, "blocked_or_rate_limited", message="Public API denied or rate-limited this request")
        response.raise_for_status()
        data = response.json()
        return LookupResult(
            username=str(data.get("login", value)),
            status="found",
            profile_url=data.get("html_url"),
            public_repos=data.get("public_repos"),
            created_at=data.get("created_at"),
        )
    finally:
        if owns_client:
            active.close()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Check one supplied username using GitHub's public API.")
    parser.add_argument("username", nargs="?")
    parser.add_argument("--json", action="store_true", help="Print JSON")
    parser.add_argument("--version", action="version", version=VERSION)
    args = parser.parse_args(argv)
    if not args.username:
        parser.error("username is required")
    try:
        result = lookup_github_username(args.username)
    except (ValueError, httpx.HTTPError) as exc:
        print(f"lookup failed: {exc}", file=sys.stderr)
        return 1
    if args.json:
        print(json.dumps(asdict(result), indent=2))
    else:
        print(f"Username: {result.username}")
        print(f"Status: {result.status}")
        if result.profile_url:
            print(f"Public profile: {result.profile_url}")
        if result.message:
            print(result.message)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
