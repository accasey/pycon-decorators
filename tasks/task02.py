import random

from pycon_decorators import trace, timer


GREETINGS = ["Heisann", "Hi there", "Ni!", "Wassup", "Naber", "Merhaba"]


@trace
def greet(name: str, greeting: str ="Hello"):
    return f"{greeting} {name}"


@timer
@trace
def random_greet(name: str ="Emily"):
    greeting = random.choice(GREETINGS)
    return greet(name, greeting=greeting)


@trace
def greet_many(number: int):
    return [random_greet() for _ in range(number)]


if __name__ == "__main__":
    # greet("Andrew")
    # greet("Andrew", greeting="Naber")
    # greet(name="Andrew", greeting="Naber")
    # random_greet()
    # greet_many(3)
    random.seed(2020)
    greet("world")
    print("-" * 50)
    greet(name="world", greeting="def")
    print("-" * 50)
    random_greet()
    print("-" * 50)
    greet_many(3)
