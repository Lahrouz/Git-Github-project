import unittest
from addition import add_numbers

class TestAddition(unittest.TestCase):
    def test_add_numbers(self):
        result = add_numbers(2, 3)
        self.assertEqual(result, 5)

    def test_add_numbers_negative(self):
        result = add_numbers(-2, 2)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()