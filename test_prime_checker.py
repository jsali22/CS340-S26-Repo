import unittest
from prime_checker import is_prime

class TestPrimeChecker(unittest.TestCase):
    def test_prime_seven(self):
        self.assertTrue(is_prime(7))

    def test_composite_four(self):
        self.assertFalse(is_prime(4))

if __name__ == '__main__':
    unittest.main()