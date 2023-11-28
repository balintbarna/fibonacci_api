from functools import cache


@cache
def get_fibonacci_value(index: int) -> int:
    """
    Calculate the fibonacci value at the specified index.
    The starting values are 0 and 1.
    Caching is enabled on the function.
    """
    if not isinstance(index, int):
        raise TypeError
    if index < 0:
        raise IndexError
    try:
        return [0, 1][index]
    except IndexError:
        return get_fibonacci_value(index - 1) + get_fibonacci_value(index - 2)
