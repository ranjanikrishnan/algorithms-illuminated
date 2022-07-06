import unittest

from strassens_matrix_multiplication import strassens_matrix_multiplication


class TestRecursiveMatrixMultiplication(unittest.TestCase):
    def test_recursive_matrix_multiplication(self):
        x = [[1, 2], [3, 4]]
        y = [[2, 0], [1, 2]]

        expected = [[4, 4], [10, 8]]
        actual = strassens_matrix_multiplication(x, y, len(x))
        self.assertEqual(expected, actual)

        x = [[1, 2, 3, 4], [3, 4, 5, 6], [5, 6, 7, 8], [7, 8, 9, 10]]
        y = [[1, 2, 3, 4], [3, 4, 5, 6], [5, 6, 7, 8], [7, 8, 9, 10]]
        expected = [[50, 60, 70, 80], [82, 100, 118, 136], [114, 140, 166, 192], [146, 180, 214, 248]]
        actual = strassens_matrix_multiplication(x, y, len(x))
        self.assertEqual(expected, actual)
