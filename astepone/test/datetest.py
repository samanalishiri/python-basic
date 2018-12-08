from unittest import TestCase

import astepone.utils.date as date


class DateTest(TestCase):

    def test_date(self):
        d = date.Date(2018, 11, 22)
        self.assertEqual(format(d), '2018-11-22', 'DateTest.test_date is failed')
