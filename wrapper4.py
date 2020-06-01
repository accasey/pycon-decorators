import random
from typing import Any
import functools


def wrapper(func: Any):
    """Wrapping the outer function at runtime"""

    @functools.wraps(func)
    def _wrapper(*args, **kwargs):
        print(f"Before {func.__name__}")
        value = func(*args, **kwargs)
        print(f"After {func.__name__}")
        return value

    return _wrapper


@wrapper
def say_hello(name: str):
    print(f"Hello {name}")


@wrapper
def dice_roll():
    """Roll a six-sided dice"""
    return random.randint(1, 6)


say_hello("world")
print(dice_roll())
print(dice_roll.__name__)
print(dice_roll.__doc__)
# help(dice_roll)