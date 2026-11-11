import pytest
from safety import safe_calculate


def test_safe_arithmetic() -> None:
    assert safe_calculate("(2 + 3) * 4") == 20


def test_rejects_python_calls() -> None:
    with pytest.raises(ValueError):
        safe_calculate("__import__('os').system('whoami')")


def test_rejects_large_exponent() -> None:
    with pytest.raises(ValueError):
        safe_calculate("2 ** 99")


def test_rejects_long_expression() -> None:
    with pytest.raises(ValueError):
        safe_calculate("1" * 201)
