import unittest
from counting_inversions_improved import sort_and_count_inversions


class TestCountingInversionsImproved(unittest.TestCase):
    def test_counting_inversions_improved(self):
        input_array = [1, 3, 5, 2, 4, 6]
        expected = 3
        actual_1, actual_2 = sort_and_count_inversions(input_array)
        self.assertEqual(expected, actual_2)
