import functools
import time


def wrapper(func):
    """Template for decorators"""

    @functools.wraps(func)
    def _wrapper(*args, **kwargs):
        """The wrapper function replacing the original"""
        # Do something before calling the function
        value = func(*args, **kwargs)
        # Do something after calling the function
        return value

    return _wrapper


def timer(func):
    """Measure the time taken to execute the function."""

    @functools.wraps(func)
    def _wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        f = func(*args, **kwargs)
        finish_time = time.perf_counter()
        print(f"Elapsed time: {finish_time - start_time:.5f}")
        return f

    return _wrapper


def trace(func):
    """Template for decorators"""

    @functools.wraps(func)
    def _wrapper(*args, **kwargs):
        """The wrapper function replacing the original"""
        # Do something before calling the function
        value = func(*args, **kwargs)
        # Do something after calling the function
        return value

    return _wrapper
