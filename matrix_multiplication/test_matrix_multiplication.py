import unittest

from matrix_multiplication import matrix_multiplication


class TestMatrixMultiplication(unittest.TestCase):
    def test_matrix_multiplication(self):
        x = [[3, 4], [2, 1]]
        y = [[1, 5], [3, 7]]
        expected = [[15, 43], [5, 17]]
        actual = matrix_multiplication(x, y)
        self.assertEqual(expected, actual)
