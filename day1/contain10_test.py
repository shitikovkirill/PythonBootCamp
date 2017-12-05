import unittest
from contain10 import contain_10


class TestFibonacci(unittest.TestCase):

    def test_1(self):
        self.assertEquals([5, 5], contain_10(5, 5))