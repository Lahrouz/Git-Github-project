import unittest
from addition import add_numbers

class TestAdditionInvalid(unittest.TestCase):
    def test_add_numbers_invalid(self):
        with self.assertRaises(TypeError):
            add_numbers("1", 2)

if __name__ == '__main__':
    unittest.main()