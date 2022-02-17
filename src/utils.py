import random
from config import FETCH_RECORD_THRESHHOLD


class RandomNumberGenerator(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def get_random_number(self):
        return random.randint(self.start, self.end)

    def get_random_generated_list(self):
        generated = list()
        while len(generated) != FETCH_RECORD_THRESHHOLD:
            num = self.get_random_number()
            if num in generated:
                continue
            generated.append(num)
        return generated
