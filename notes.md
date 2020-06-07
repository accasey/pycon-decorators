# Introduction to Decorators: Power up your Python Code
Geir Arne Hjelle:  @gahjelle
https://github.com/gahjelle/decorators_tutorial

## Decorators Hall of Fame
From the standard library:
* `@property`
* `@classmethod`
* `@staticmethod`
* `@functools.wraps`
* `@dataclasses.dataclass`
* `@contextlib.contextmanager`

Some notable third party packages:
* Numba: `@jit`
* Flask: `@app.route`
* Click: `@command`, `@argument`, `@option`

Further resources:
* [Real Python article](https://realpython.com/primer-on-python-decorators)
* [Decorator package](https://pypi.org/project/decorator)
* [Python cookbook (chapter 9)](https://github.com/dabeaz/python-cookbook/tree/master/src/9)
* [PEP 318](https://www.python.org/dev/peps/pep-0318)
* [PEP 614](https://www.python.org/dev/peps/pep-0614)


## Functions as first class objects
Functions can be passed into other functions as an argument.
* Similar to JavaScript.


## Decorator key take aways
A *decorator* is any function that accepts a function and returns a function.
* I think it is more accurate to say an object that is callable.

```python
@wrapper
def function
    pass

```

This is just *syntactic sugar* for:
```python
def function():
    pass

function = wrapper(function)
```

So you could even do this for delivered functions, e.g. math.factorial.
```python
math.factorial = wrapper(math.factorial)
```
As you cannot redefine the factorial function itself using the decorator syntax.
```python
@wrapper
def math.factorial:
    pass
```


Issues so far:
1. The wrapping will change the name of the `__name__` variable.
    * You can get around this by assigning the `__name__` variable directly.
    * You can use functools.update_wrapper; this updates/fixes more than just `__name__`.
    * Even better you can use the decorator factory functools.wraps
        * This is applied against the inner function within the 'wrapper'/'decorator' function.
2. The wrapping doesn't work with an argument, e.g. `say_hello("world)`
    * Use `*args` and `**kwargs` to get around this. They are collected in a `list` and a `dict`.
3. The return value from the decorated function, e.g. `dice_roll()` is being *eaten*.
    * You need to 'save' the function, rather than invoking it, to a variable and then return it.



## Advanced Decorators

### Keeping State
Caching, Lookups.
You can implement the state in the inner function.
And initialise it just before the call to return the outer function in the decorator.


### Decorating Classes
The class needs to be callable, i.e. it needs to implement the special `__call__` method.

You can decorate a class with a function decorator. But then this changes the class into a function.
* This means you would lose the type, so `isinstance` will not work.
* The decorator needs to return the same class, so the decorator needs to take in the class and return it.

Something about a [data class decorator](https://docs.python.org/3/library/dataclasses.html) introduced in Python 3.7.

### Adding Arguments
Uses a decorator factory pattern.

### Optional Arguments
Decorators can also optionally use arguments. In this case, the decorator factory needs to return either a
decorator or a wrapper function, depending on how it is called.
* See task 6 and `supertrace`.


