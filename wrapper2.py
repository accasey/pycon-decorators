from typing import Any


def wrapper(func: Any):
    """Wrapping the outer function at runtime"""

    def _wrapper():
        print(f"Before {func.__name__}")
        func()
        print(f"After {func.__name__}")

    return _wrapper


@wrapper
def outer():
    """
    Now this is a decorated function!
    And you can see the 'before' and 'after' print statements as well as the statements
    from within the function passed in as an argument to wrapper.
    """
    print("Inside the outer function")
    pycon = 2020

    def inner():
        print("Inside the inner function")
        print(f"PyCon is in {pycon}")

    inner()
    return inner


outer()

# the decorator syntax is the syntactic sugar for:
# outer = wrapper(outer)