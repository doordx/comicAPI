import unittest
from src.services import ComicService
from src.config import BASE_API_URL


class TestComicService(unittest.TestCase):
    def test_getService(self):
        url = BASE_API_URL + "{}/info.0.json".format(1)
        self.assertIsNotNone(ComicService().get(url))


if __name__ == '__main__':
    unittest.main()
