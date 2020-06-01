import random
from typing import Any


def wrapper(func: Any):
    """Wrapping the outer function at runtime"""

    def _wrapper():
        print(f"Before {func.__name__}")
        func()
        print(f"After {func.__name__}")

    return _wrapper


@wrapper
def dice_roll():
    return random.randint(1, 6)


print(dice_roll())
print(dice_roll.__name__)