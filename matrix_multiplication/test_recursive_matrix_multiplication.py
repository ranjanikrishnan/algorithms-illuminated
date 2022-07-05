import unittest

from recursive_matrix_multiplication import recursive_matrix_multiplication


class TestRecursiveMatrixMultiplication(unittest.TestCase):
    def test_recursive_matrix_multiplication(self):
        x = [[3, 4], [2, 1]]
        y = [[1, 5], [3, 7]]

        expected = [[15, 43], [5, 17]]
        actual = recursive_matrix_multiplication(x, y)
        self.assertEqual(expected, actual)

        x = [[1, 2, 3, 4], [3, 4, 5, 6], [5, 6, 7, 8], [7, 8, 9, 10]]
        y = [[1, 2, 3, 4], [3, 4, 5, 6], [5, 6, 7, 8], [7, 8, 9, 10]]
        expected = [[50, 60, 70, 80], [82, 100, 118, 136], [114, 140, 166, 192], [146, 180, 214, 248]]
        actual = recursive_matrix_multiplication(x, y)
        self.assertEqual(expected, actual)
