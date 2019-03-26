import json
from collections import defaultdict


# Saman Alishiri samanalishiri@gmail.com
class DictionaryList:

    def __init__(self):
        self.__dictionary = defaultdict(list)

    def append(self, key, n):
        if key not in self.__dictionary:
            self.__dictionary[key] = []

        self.__dictionary[key].append(n)

    def to_string(self):
        return json.dumps(self.__dictionary)
