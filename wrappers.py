from typing import Any


def wrapper(func: Any):
    """Wrapping the outer function at runtime"""
    def _wrapper():
        print(f"Before {func.__name__}")
        func()
        print(f"After {func.__name__}")
    return _wrapper


def outer():
    print("Inside the outer function")
    pycon = 2020
    def inner():
        print("Inside the inner function")
        print(f"PyCon is in {pycon}")

    inner()
    return inner


wrapper(outer)
# Just returns the function:
# <function wrapper.<locals>._wrapper at 0x7fb40993fee0>

# Assign the function to a variable
new_outer = wrapper(outer) # The wrapping happens only once.
# Now the function has been 'wrapped', and each time it is called
# the function will print the before and after.
new_outer()


# print(outer)
# <function outer at 0x7f2e441d8e50>

# Now the function has been decorated
outer = wrapper(outer)
# print(outer)
# <function wrapper.<locals>._wrapper at 0x7fd2cfc5af70>