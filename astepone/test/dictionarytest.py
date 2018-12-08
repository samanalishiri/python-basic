from unittest import TestCase

from astepone.datastructure.dictionarylist import DictionaryList


class DictionaryTest(TestCase):
    def test_dictionary_list(self):
        dictionary = DictionaryList()
        dictionary.append('key-1', 0)
        dictionary.append('key-1', 2)
        dictionary.append('key-2', 1)
        self.assertEqual(dictionary.to_string(),
                         '{"key-1": [0, 2], "key-2": [1]}',
                         'DictionaryTest.test_dictionary_list is failed'
                         )
