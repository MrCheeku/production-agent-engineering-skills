import httpx
import pytest
from ha_client import HomeAssistantClient


def build_client(handler) -> HomeAssistantClient:
    return HomeAssistantClient(
        "http://homeassistant.local:8123",
        "test-token",
        frozenset({"light.desk"}),
        transport=httpx.MockTransport(handler),
    )


def test_list_entities_filters_unapproved_entities() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, json=[
            {"entity_id": "light.desk", "state": "on"},
            {"entity_id": "lock.front_door", "state": "locked"},
        ])
    assert build_client(handler).list_entities() == [{"entity_id": "light.desk", "state": "on"}]


def test_write_requires_confirmation() -> None:
    client = build_client(lambda request: httpx.Response(200, json=[]))
    with pytest.raises(PermissionError):
        client.call_service("light.desk", "turn_off")


def test_write_rejects_unapproved_entity() -> None:
    client = build_client(lambda request: httpx.Response(200, json=[]))
    with pytest.raises(PermissionError):
        client.call_service("lock.front_door", "unlock", confirmed=True)


def test_allowlisted_confirmed_write() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        assert request.url.path == "/api/services/light/turn_off"
        assert request.headers["Authorization"] == "Bearer test-token"
        return httpx.Response(200, json=[])
    assert build_client(handler).call_service("light.desk", "turn_off", confirmed=True)["success"]
