import pytest
from pbc.tools.fibonacci import fibonacci_generator


@pytest.fixture(scope='module')
def fib_generator():
    return fibonacci_generator()


@pytest.fixture(scope='module')
def negative_fib_generator():
    return fibonacci_generator(negative=True)
