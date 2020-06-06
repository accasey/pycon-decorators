# Introduction to Decorators: Power up your Python Code
Geir Arne Hjelle:  @gahjelle
https://github.com/gahjelle/decorators_tutorial

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


