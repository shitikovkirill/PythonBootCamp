from pbc.tools.fibonacci import fibonacci_list
import pytest

POSITIVE_FIBONACCI_NUMBER = [
    0, 1, 1, 2, 3, 5, 8,
]

NEGATIVE_FIBONACCI_NUMBER = [
    0, 1, -1, 2, -3, 5, -8,
]


@pytest.mark.fibonacci
@pytest.mark.fibonacci_generator
@pytest.mark.parametrize("number", POSITIVE_FIBONACCI_NUMBER)
def test_positive_fibonacci_generator(fib_generator, number):
    assert fib_generator.next() == number


@pytest.mark.fibonacci
@pytest.mark.fibonacci_generator
@pytest.mark.parametrize("number", NEGATIVE_FIBONACCI_NUMBER)
def test_negative_fibonacci_generator(negative_fib_generator, number):
    assert negative_fib_generator.next() == number


POSITIVE_FIBONACCI_LIST = [
    (0, [0]),
    (1, [0, 1]),
    (2, [0, 1, 1]),
    (3, [0, 1, 1, 2]),
    (4, [0, 1, 1, 2, 3]),
    (5, [0, 1, 1, 2, 3, 5]),
    (6, [0, 1, 1, 2, 3, 5, 8]),
]

NEGATIVE_FIBONACCI_LIST = [
    (0, [0]),
    (-1, [1, 0]),
    (-2, [-1, 1, 0]),
    (-3, [2, -1, 1, 0]),
    (-4, [-3, 2, -1, 1, 0]),
    (-5, [5, -3, 2, -1, 1, 0]),
    (-6, [-8, 5, -3, 2, -1, 1, 0]),
]


@pytest.mark.fibonacci
@pytest.mark.fibonacci_list
@pytest.mark.parametrize("number,fibonacci_list_value", POSITIVE_FIBONACCI_LIST)
def test_positive_fibonacci_list(number, fibonacci_list_value):
    assert fibonacci_list(number) == fibonacci_list_value


@pytest.mark.fibonacci
@pytest.mark.fibonacci_list
@pytest.mark.parametrize("number,fibonacci_list_value", NEGATIVE_FIBONACCI_LIST)
def test_negative_fibonacci_list(number, fibonacci_list_value):
    assert fibonacci_list(number) == fibonacci_list_value
