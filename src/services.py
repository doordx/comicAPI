import requests


class ComicService(object):
    def get(self, url):
        res = requests.get(url)
        if res.status_code == 200:
            res = res.json()
        return res
