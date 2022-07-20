import unittest
from rselect import rselect


class TestRSelect(unittest.TestCase):
    def test_rselect(self):
        a = [6, 8, 9, 2]

        expected = 6
        actual = rselect(a, 2)
        self.assertEqual(expected, actual)