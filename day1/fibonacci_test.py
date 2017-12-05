import unittest
from fibonacci import fibonacci


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


if __name__ == '__main__':
    unittest.main()
