from fibonacci import get_fibonacci_list, get_fibonacci_xrange, fibonacci, fibonacci_generator


def test_fibonacci():
    assert fibonacci(0) == 0

    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8

    assert fibonacci(-1) == 1
    assert fibonacci(-2) == -1
    assert fibonacci(-3) == 2
    assert fibonacci(-4) == -3
    assert fibonacci(-5) == 5
    assert fibonacci(-6) == -8


def test_positive_fibonacci_generator():
    fg = fibonacci_generator()
    assert fg.next() == 0
    assert fg.next() == 1
    assert fg.next() == 1
    assert fg.next() == 2
    assert fg.next() == 3
    assert fg.next() == 5
    assert fg.next() == 8


def test_negative_fibonacci_generator():
    fg = fibonacci_generator(negative=True)
    assert fg.next() == 0
    assert fg.next() == 1
    assert fg.next() == -1
    assert fg.next() == 2
    assert fg.next() == -3
    assert fg.next() == 5
    assert fg.next() == -8


def test_positive_fibonacci_list():
    assert get_fibonacci_list(0) == [0]
    assert get_fibonacci_list(1) == [0, 1]
    assert get_fibonacci_list(2) == [0, 1, 1]
    assert get_fibonacci_list(3) == [0, 1, 1, 2]
    assert get_fibonacci_list(4) == [0, 1, 1, 2, 3]
    assert get_fibonacci_list(5) == [0, 1, 1, 2, 3, 5]
    assert get_fibonacci_list(6) == [0, 1, 1, 2, 3, 5, 8]


def test_negative_fibonacci_list():
    assert get_fibonacci_list(0) == [0]
    assert get_fibonacci_list(-1) == [1, 0]
    assert get_fibonacci_list(-2) == [-1, 1, 0]
    assert get_fibonacci_list(-3) == [2, -1, 1, 0]
    assert get_fibonacci_list(-4) == [-3, 2, -1, 1, 0]
    assert get_fibonacci_list(-5) == [5, -3, 2, -1, 1, 0]
    assert get_fibonacci_list(-6) == [-8, 5, -3, 2, -1, 1, 0]


def test_positive_fibonacci_xrange():
    assert get_fibonacci_xrange(0) == [0]
    assert get_fibonacci_xrange(1) == [0, 1]
    assert get_fibonacci_xrange(2) == [0, 1, 1]
    assert get_fibonacci_xrange(3) == [0, 1, 1, 2]
    assert get_fibonacci_xrange(4) == [0, 1, 1, 2, 3]
    assert get_fibonacci_xrange(5) == [0, 1, 1, 2, 3, 5]
    assert get_fibonacci_xrange(6) == [0, 1, 1, 2, 3, 5, 8]


def test_negative_fibonacci_xrange():
    assert get_fibonacci_xrange(0) == [0]
    assert get_fibonacci_xrange(-1) == [1, 0]
    assert get_fibonacci_xrange(-2) == [-1, 1, 0]
    assert get_fibonacci_xrange(-3) == [2, -1, 1, 0]
    assert get_fibonacci_xrange(-4) == [-3, 2, -1, 1, 0]
    assert get_fibonacci_xrange(-5) == [5, -3, 2, -1, 1, 0]
    assert get_fibonacci_xrange(-6) == [-8, 5, -3, 2, -1, 1, 0]
