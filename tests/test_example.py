"""Example tests — replace with your own tests."""

from usoar_edm.example import hello


def test_hello_default() -> None:
    assert hello() == "Hello, world!"


def test_hello_name() -> None:
    assert hello("Alice") == "Hello, Alice!"
