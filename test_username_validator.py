import unittest
from username_validator import validate_username

class TestUsernameValidator(unittest.TestCase):
    def test_valid_username(self):
        self.assertTrue(validate_username("user1"))

    def test_too_short(self):
        self.assertFalse(validate_username("user"))

if __name__ == '__main__':
    unittest.main()