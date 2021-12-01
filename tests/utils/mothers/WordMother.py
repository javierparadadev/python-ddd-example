import string
import random


class WordMother:

    @staticmethod
    def random() -> str:
        letters = string.ascii_lowercase
        random_str = ''.join(random.choice(letters) for i in range(10))
        return random_str
