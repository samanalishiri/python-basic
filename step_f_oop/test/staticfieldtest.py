from unittest import TestCase

from step_f_oop.staticfield import StaticField


class StaticFieldTest(TestCase):
    def test_static_field(self):
        instance_1 = StaticField()
        instance_2 = StaticField()

        self.assertEqual(StaticField.number_of_instance, 2)
