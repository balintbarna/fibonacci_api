from pytest import raises
from fibonacci import get_fibonacci_value


def test_invalid_fibonacci_indexes():
    with raises(TypeError):
        get_fibonacci_value("hello")
    with raises(IndexError):
        get_fibonacci_value(-5)


KNOWN_RESULTS = {
    0: 0,
    1: 1,
    2: 1,
    3: 2,
    4: 3,
    5: 5,
    6: 8,
    13: 233,
    19: 4181,
}


def test_known_fibonacci_results():
    for k, v in KNOWN_RESULTS.items():
        assert v == get_fibonacci_value(k)
