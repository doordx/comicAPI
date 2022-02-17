from utils import RandomNumberGenerator
from config import BASE_API_URL, IS_DATABASE_CONNECTED, FETCH_RECORD_THRESHHOLD
from services import ComicService
from comic import Comic
from dao import Dao
import json


class App(object):
    @staticmethod
    def run():
        rg = RandomNumberGenerator(1, 87)
        if FETCH_RECORD_THRESHHOLD < 1 or FETCH_RECORD_THRESHHOLD > 87:
            print("Please check Threshhold in config. It should be between 1 to 87")
            exit()
        num_list = rg.get_random_generated_list()
        comic_service = ComicService()
        comics = list()
        db_rows = list()
        for num in num_list:
            url = BASE_API_URL + "{}/info.0.json".format(num)
            comic_obj = comic_service.get(url)
            comic = Comic(**comic_obj)
            comics.append(comic)
            db_rows.append(comic.get_serialized_tuple())
        if IS_DATABASE_CONNECTED:
            dao = Dao()
            dao.bulk_insert(db_rows)
        for comic in comics:
            print(comic)


if __name__ == "__main__":
    App.run()
