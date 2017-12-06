from fibonacci import get_fibonacci_list, get_fibonacci_xrange, fibonacci, fibonacci_generator
import pytest


@pytest.mark.parametrize("number,fibonacci_number", [
    (0, 0),
    (1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (6, 8),
    (-1, 1), (-2, -1), (-3, 2), (-4, -3), (-5, 5), (-6, -8),
])
def test_fibonacci(number, fibonacci_number):
    assert fibonacci(number) == fibonacci_number


@pytest.mark.fibonacci_generator
def test_positive_fibonacci_generator():
    fg = fibonacci_generator()
    assert fg.next() == 0
    assert fg.next() == 1
    assert fg.next() == 1
    assert fg.next() == 2
    assert fg.next() == 3
    assert fg.next() == 5
    assert fg.next() == 8


@pytest.mark.fibonacci_generator
def test_negative_fibonacci_generator():
    fg = fibonacci_generator(negative=True)
    assert fg.next() == 0
    assert fg.next() == 1
    assert fg.next() == -1
    assert fg.next() == 2
    assert fg.next() == -3
    assert fg.next() == 5
    assert fg.next() == -8


POSITIVE_FIBONACCI = [
    (0, [0]),
    (1, [0, 1]),
    (2, [0, 1, 1]),
    (3, [0, 1, 1, 2]),
    (4, [0, 1, 1, 2, 3]),
    (5, [0, 1, 1, 2, 3, 5]),
    (6, [0, 1, 1, 2, 3, 5, 8]),
]


@pytest.mark.parametrize("number,fibonacci_list", POSITIVE_FIBONACCI)
def test_positive_fibonacci_list(number, fibonacci_list):
    assert get_fibonacci_list(number) == fibonacci_list


NEGATIVE_FIBONACCI = [
    (0, [0]),
    (-1, [1, 0]),
    (-2, [-1, 1, 0]),
    (-3, [2, -1, 1, 0]),
    (-4, [-3, 2, -1, 1, 0]),
    (-5, [5, -3, 2, -1, 1, 0]),
    (-6, [-8, 5, -3, 2, -1, 1, 0]),
]


@pytest.mark.parametrize("number,fibonacci_list", NEGATIVE_FIBONACCI)
def test_negative_fibonacci_list(number, fibonacci_list):
    assert get_fibonacci_list(number) == fibonacci_list


@pytest.mark.fibonacci_generator
@pytest.mark.parametrize("number,fibonacci_list", POSITIVE_FIBONACCI)
def test_positive_fibonacci_xrange(number, fibonacci_list):
    assert get_fibonacci_xrange(number) == fibonacci_list


@pytest.mark.fibonacci_generator
@pytest.mark.parametrize("number,fibonacci_list", NEGATIVE_FIBONACCI)
def test_negative_fibonacci_xrange(number, fibonacci_list):
    assert get_fibonacci_xrange(number) == fibonacci_list
