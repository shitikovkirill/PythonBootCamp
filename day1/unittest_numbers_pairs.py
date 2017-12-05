import unittest
from numbers_pairs import contain_10


class TestContain10(unittest.TestCase):

    def test_1(self):
        test_1 = contain_10(5, 5, 6, 7, 2, 3, 2, 3)
        self.assertEquals([(3, 7), (5, 5)], test_1)
        self.assertEquals(2, len(test_1))
        self.assertIn((3, 7), test_1)
        self.assertIsNotNone(test_1)

        test_2 = contain_10(1, 2, 3, 4, 5, 5, 6)
        self.assertEquals([(4, 6), (5, 5)], test_2)
        self.assertEquals(2, len(test_1))
        self.assertIn((4, 6), test_1)
        self.assertIsNotNone(test_2)


if __name__ == '__main__':
    unittest.main()
