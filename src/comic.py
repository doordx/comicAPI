import json


class Comic(object):
    def __init__(self, **comic_obj):
        self.name = comic_obj.get('title')
        self.alt_text = comic_obj.get('alt')
        self.num = comic_obj.get('num')
        self.link = comic_obj.get('link')
        self.image = comic_obj.get('img').split("/")[-1]
        self.image_link = comic_obj.get('img')

    def __str__(self):
        obj = dict()
        obj['name'] = self.name
        obj['alt_text'] = self.alt_text
        obj['num'] = self.num
        obj['link'] = self.link
        obj['image'] = self.image
        obj['image_link'] = self.image_link
        return json.dumps(obj)

    def get_serialized_tuple(self):
        data = [self.name, self.num, self.alt_text, self.image_link]
        return tuple(data)


