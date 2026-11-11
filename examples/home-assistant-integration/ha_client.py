from __future__ import annotations

from dataclasses import dataclass
from urllib.parse import urlparse

import httpx

ALLOWED_SERVICES = {"light": {"turn_on", "turn_off"}}


@dataclass
class HomeAssistantClient:
    base_url: str
    token: str
    allowed_entities: frozenset[str]
    timeout: float = 8.0
    transport: httpx.BaseTransport | None = None

    def __post_init__(self) -> None:
        parsed = urlparse(self.base_url)
        if parsed.scheme not in {"http", "https"} or not parsed.netloc:
            raise ValueError("base_url must be an absolute HTTP(S) URL")
        if not self.token.strip():
            raise ValueError("A Home Assistant token is required")
        self.base_url = self.base_url.rstrip("/")

    def _client(self) -> httpx.Client:
        return httpx.Client(
            base_url=self.base_url,
            headers={"Authorization": f"Bearer {self.token}", "Content-Type": "application/json"},
            timeout=self.timeout,
            transport=self.transport,
        )

    def list_entities(self) -> list[dict[str, str]]:
        with self._client() as client:
            response = client.get("/api/states")
            response.raise_for_status()
            payload = response.json()
        if not isinstance(payload, list):
            raise RuntimeError("Unexpected response from Home Assistant")
        return [
            {"entity_id": item["entity_id"], "state": str(item.get("state", "unknown"))}
            for item in payload
            if isinstance(item, dict) and item.get("entity_id") in self.allowed_entities
        ]

    def call_service(self, entity_id: str, service: str, *, confirmed: bool = False) -> dict[str, object]:
        if entity_id not in self.allowed_entities:
            raise PermissionError("Entity is not allowlisted")
        domain = entity_id.split(".", maxsplit=1)[0]
        if service not in ALLOWED_SERVICES.get(domain, set()):
            raise PermissionError("Service is not allowlisted for this entity domain")
        if not confirmed:
            raise PermissionError("Explicit user confirmation is required")
        with self._client() as client:
            response = client.post(
                f"/api/services/{domain}/{service}",
                json={"entity_id": entity_id},
            )
            response.raise_for_status()
            payload = response.json()
        return {"success": True, "result_count": len(payload) if isinstance(payload, list) else 0}
