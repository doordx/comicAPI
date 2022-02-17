import unittest
from src.utils import RandomNumberGenerator
from src.config import FETCH_RECORD_THRESHHOLD


class TestUtils(unittest.TestCase):
    def test_random_number_generator(self):
        self.assertIsNotNone(RandomNumberGenerator(1, 5).get_random_number())
    
    def test_random_number_generated_list(self):
        self.assertEqual(len(RandomNumberGenerator(1, 5).get_random_generated_list()), FETCH_RECORD_THRESHHOLD)


if __name__ == '__main__':
    unittest.main()
