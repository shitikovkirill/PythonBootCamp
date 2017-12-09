from pbc_app.fibonacci import fibonacci_list,  fibonacci_generator
import pytest


@pytest.mark.fibonacci
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


@pytest.mark.fibonacci
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

NEGATIVE_FIBONACCI = [
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
@pytest.mark.parametrize("number,fibonacci_list_value", POSITIVE_FIBONACCI)
def test_positive_fibonacci_list(number, fibonacci_list_value):
    assert fibonacci_list(number) == fibonacci_list_value


@pytest.mark.fibonacci
@pytest.mark.fibonacci_list
@pytest.mark.parametrize("number,fibonacci_list_value", NEGATIVE_FIBONACCI)
def test_negative_fibonacci_list(number, fibonacci_list_value):
    assert fibonacci_list(number) == fibonacci_list_value
