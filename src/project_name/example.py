"""Example module — replace with your own code."""


def hello(name: str = "world") -> str:
    """Return a greeting string."""
    return f"Hello, {name}!"

name = input("What's your name? ")
print(hello(name))