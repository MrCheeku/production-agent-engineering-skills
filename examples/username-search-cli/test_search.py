import httpx
import pytest
from search import lookup_github_username


def test_returns_public_profile_fields() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, json={
            "login": "octocat",
            "html_url": "https://github.com/octocat",
            "public_repos": 8,
            "created_at": "2011-01-25T18:44:36Z",
        })
    with httpx.Client(transport=httpx.MockTransport(handler)) as client:
        result = lookup_github_username("octocat", client)
    assert result.status == "found"
    assert result.profile_url == "https://github.com/octocat"


def test_not_found_is_not_an_error() -> None:
    with httpx.Client(transport=httpx.MockTransport(lambda request: httpx.Response(404))) as client:
        assert lookup_github_username("unknown-user", client).status == "not_found"


def test_invalid_username_is_rejected() -> None:
    with pytest.raises(ValueError):
        lookup_github_username("bad username")


def test_rate_limit_is_reported() -> None:
    with httpx.Client(transport=httpx.MockTransport(lambda request: httpx.Response(429))) as client:
        assert lookup_github_username("octocat", client).status == "blocked_or_rate_limited"
