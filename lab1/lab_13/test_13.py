import unittest
from src import peut_diviser_en_trois

class TestSovenirs(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(peut_diviser_en_trois([3, 3, 3, 3]), 0)  # Impossible
        self.assertEqual(peut_diviser_en_trois([40]), 0)  # Impossible
        self.assertEqual(peut_diviser_en_trois([17, 59, 34, 57, 17, 23, 67, 1, 18, 2, 59]), 1)  # Possible
        self.assertEqual(peut_diviser_en_trois([1, 2, 3, 4, 5, 5, 7, 7, 8, 10, 12, 19, 25]), 1)  # Possible
        self.assertEqual(peut_diviser_en_trois([1, 1, 1, 1, 1, 1]), 1)  # Impossible

if __name__ == "__main__":
    unittest.main()
