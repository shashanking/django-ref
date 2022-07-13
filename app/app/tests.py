"""
Sample test
"""

from django.test import SimpleTestCase
from . import calc


class CalcTest(SimpleTestCase):
    """Test class to test calc"""

    def test_add(self):
        """test adding x and y together"""
        res = calc.add(4, 6)
        self.assertEqual(res, 10)

    def test_subtract(self):
        """test subtracting numbers"""
        res = calc.subtract(10, 15)
        self.assertEqual(res, 5)
