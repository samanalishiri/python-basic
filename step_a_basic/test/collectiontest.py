from unittest import TestCase

from step_a_basic.datastructure.filterlist import FilterList, event_number_filter


class CollectionTest(TestCase):
    def setUp(self):
        self.original_list = [1, 4, -5, 10, -7, 2, 3, -1]

    def test_filter_list(self):
        filter_list = FilterList(self.original_list, event_number_filter)
        self.assertListEqual([n for n in self.original_list if n % 2 == 0],
                             filter_list.get_filtered_list(),
                             'FilterList.test_filter_list is failed')
