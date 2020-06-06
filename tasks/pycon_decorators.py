import functools
import time
from typing import Dict, Any

REGISTERED: Dict[str, Any] = dict()


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
    """Show the trace of function calls"""

    # This only happens once, instead of every time
    name = func.__name__

    @functools.wraps(func)
    def _trace(*args, **kwargs):
        """The trace function replacing the original function"""
        args_repr = [repr(a) for a in args]
        # kwargs_repr = [f"{k}={repr(v)}" for k, v in kwargs.items()]
        kwargs_repr = [
            f"{k}={v!r}" for k, v in kwargs.items()
        ]  # this !r is a shortcut for repr()
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {name}({signature})")
        value = func(*args, **kwargs)
        print(f"{name} returned {value!r}")
        return value

    return _trace


def my_orig_trace(func):
    """Show the trace of function calls"""

    @functools.wraps(func)
    def _wrapper(*args, **kwargs):
        """The wrapper function replacing the original"""
        args_str = ""
        for arg in args:
            if isinstance(arg, str):
                args_str += "'" + arg + "', "
            else:
                args_str += str(arg) + ", "

        for k, v in kwargs.items():
            args_str += str(k) + f"='{v}', "

        args_str = args_str.rstrip(", ")
        # args_str = args_str.rstrip(',')
        print(f"Calling {func.__name__}({args_str})")
        value = func(*args, **kwargs)
        print(f"{func.__name__} returned '{value}'")
        return value

    return _wrapper


def register(func):
    """Register a function"""
    REGISTERED[func.__name__] = func
    return func


def count_calls(func):
    """Count the number of calls to a function"""

    @functools.wraps(func)
    def _count_calls(*args, **kwargs):
        """The wrapper function replacing the original"""
        _count_calls.num_calls += 1
        return func(*args, **kwargs)

    _count_calls.num_calls = 0
    return _count_calls


class CountCalls:
    """Count the number of calls to a function"""

    def __init__(self, func):
        self.func = func
        self.num_calls = 0
        functools.update_wrapper(self, func)

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        return self.func(*args, **kwargs)
