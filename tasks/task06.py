import logging
import random

from pycon_decorators import supertrace

GREETINGS = ["Heisann", "Hi there", "Ni!"]


@supertrace
def greet(name: str, greeting: str = "Hello") -> str:
    return f"{greeting} {name}"


@supertrace(logger=logging.warning)
def random_greet(name: str = "Emily") -> str:
    greeting = random.choice(GREETINGS)
    return greet(name, greeting=greeting)


@supertrace()
def hello():
    return "Hello"


if __name__ == "__main__":
    random.seed(2020)
    print(greet("world"))
    print("-" * 50)
    print(random_greet())
    print("-" * 50)
    print(hello())