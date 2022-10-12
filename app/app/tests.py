"""
Sample Tests

"""
from django.test import SimpleTestCase

from app import calc


class CalcTest(SimpleTestCase):
    def test_add_numbers(self):
        """ Test the add module """

        res = calc.add(5, 10)
        self.assertEqual(res, 15)

    def test_subtract_numbers(self):
        """ Test the subtract module """

        res = calc.subtract(5, 10)
        self.assertEqual(res, 5)
