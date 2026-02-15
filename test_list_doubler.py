import unittest
from list_doubler import double_elements

class TestListDoubler(unittest.TestCase):
    def test_zero_element(self):
        self.assertEqual(double_elements([]), [])

if __name__ == '__main__':
    unittest.main()