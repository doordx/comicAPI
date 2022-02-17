import unittest
from src.utils import RandomNumberGenerator
from src.app import App


class TestApp(unittest.TestCase):
    def test_run(self):
        App.run()


if __name__ == '__main__':
    unittest.main()
