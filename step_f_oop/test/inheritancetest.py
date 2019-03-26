from unittest import TestCase

from step_f_oop.inheritance import JavaProgrammer


class InheritanceTest(TestCase):
    def test_java_spring(self):
        programmer = JavaProgrammer('Spring')
        self.assertEqual(programmer.__str__(), "Java:Spring")
