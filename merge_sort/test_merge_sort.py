import unittest
from merge_sort import merge_sort


class TestMergeSort(unittest.TestCase):
    def test_merge_sort(self):
        result = merge_sort([5, 4, 1, 8, 7, 2, 6, 3])
        self.assertEqual(result, [1, 2, 3, 4, 5, 6, 7, 8])

        result = merge_sort([5, 4, 1, 8, 7, 2, 6])
        self.assertEqual(result, [1, 2, 4, 5, 6, 7, 8])
