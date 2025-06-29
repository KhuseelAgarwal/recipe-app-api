"""
Sample tests
"""

from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):
    """ test the calc module"""

    def test_add_numbers(self):
        """Test adding numbers together"""
        res = calc.add(5,6)

        self.assertEqual(res,12)

    def test_subtract_numbers(self):

        res = calc.subtract(5,6)

        self.assertEqual(res,1)