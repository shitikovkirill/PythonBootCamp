import unittest
from fibonacci import *


class TestFibonacci(unittest.TestCase):

    def test_fibonacci(self):
        self.assertEquals(0, fibonacci(0))
        self.assertEquals(1, fibonacci(1))
        self.assertEquals(1, fibonacci(2))
        self.assertEquals(2, fibonacci(3))
        self.assertEquals(3, fibonacci(4))
        self.assertEquals(5, fibonacci(5))
        self.assertEquals(8, fibonacci(6))
        self.assertEquals(13, fibonacci(7))

    def test_negative_fibonacci(self):
        self.assertEquals(1, fibonacci(-1))
        self.assertEquals(-1, fibonacci(-2))
        self.assertEquals(2, fibonacci(-3))
        self.assertEquals(-3, fibonacci(-4))
        self.assertEquals(5, fibonacci(-5))
        self.assertEquals(-8, fibonacci(-6))
        self.assertEquals(13, fibonacci(-7))

    def test_get_fibonacci_range(self):
        fib_13_poz = get_fibonacci_range(13)
        self.assertEquals([0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144], fib_13_poz)
        self.assertEquals(13, len(fib_13_poz))
        self.assertIn(144, fib_13_poz)

        fib_13_neg = get_fibonacci_range(-13)
        self.assertEquals([-144, 89, -55, 34, -21, 13, -8, 5, -3, 2, -1, 1, 0], fib_13_neg)
        self.assertEquals(13, len(fib_13_neg))
        self.assertIn(-144, fib_13_neg)


if __name__ == '__main__':
    unittest.main()
