"""
Many examples of passing in a function as the 'logger'.
Make sure that you 'pass' the function without the parenthesis.
- Otherwise print() will not work - as print() returns None and this is not callable.
"""
import logging
from typing import Any


def say_hello(name: str, logger: Any):
    logger(f"Hello {name}")


def reversed_print(text: str):
    print(text[::-1].capitalize())


say_hello("World", print)
say_hello("logger", logging.warning)

# with open("say_hello.txt", "w") as f:
#     say_hello("files", f.write)


say_hello("nocyp", reversed_print)
