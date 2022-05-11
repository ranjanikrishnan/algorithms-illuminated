import unittest
from counting_inversions import counting_inversions


class TestCountingInversions(unittest.TestCase):
    def test_counting_inversions(self):
        input_array = [1, 3, 5, 2, 4, 6]
        expected = 3
        actual = counting_inversions(input_array)
        self.assertEqual(expected, actual)
