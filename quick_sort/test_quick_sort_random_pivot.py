import unittest

from quick_sort_random_pivot import partition, quick_sort


class TestQuickSortRandomPivot(unittest.TestCase):
    def test_partition(self):
        a = [3, 8, 2, 5, 1, 4, 7, 6]

        expected = 2
        actual = partition(a, 0, 7)
        self.assertEqual(expected, actual)

    def test_quick_sort(self):
        a = [3, 8, 2, 5, 1, 4, 7, 6]
        quick_sort(a, 0, len(a))
        expected = [1, 2, 3, 4, 5, 6, 7, 8]
        self.assertEqual(expected, a)

