import pytest
from app import build_messages


def test_build_messages_strips_prompt() -> None:
    assert build_messages("  Hello  ") == [{"role": "user", "content": "Hello"}]


def test_build_messages_rejects_empty_prompt() -> None:
    with pytest.raises(ValueError):
        build_messages("   ")


def test_build_messages_rejects_oversized_prompt() -> None:
    with pytest.raises(ValueError):
        build_messages("x" * 20_001)
