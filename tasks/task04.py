from pycon_decorators import count_calls
from pycon_decorators import CountCalls

# @count_calls
@CountCalls
def fibonacci(number: int):
    """Calculate Fibonacci numbers fib_n

    The Fibonacci numbers are 1, 2, 3, 5, 8, 13, 21, ...

    fib_n = fib_n-1 + fib_n-2
    """
    if number < 2:
        return 1

    return fibonacci(number - 1) + fibonacci(number - 2)


if __name__ == "__main__":
    print(fibonacci.__name__)
    print('fibonacci.num_calls:', fibonacci.num_calls)
    print(fibonacci(7))
    print('fibonacci.num_calls:', fibonacci.num_calls)
    print(fibonacci(32))
    print('fibonacci.num_calls:', fibonacci.num_calls)