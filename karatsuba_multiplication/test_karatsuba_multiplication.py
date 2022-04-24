import unittest
from karatsuba_multiplication import karatsuba_multiplication


class TestKaratsubaMultiplication(unittest.TestCase):
    def test_recursive_integer_multiplication(self):
        result = karatsuba_multiplication(1234, 5678)
        self.assertEqual(result, 7006652)

        result = karatsuba_multiplication(11, 11)
        self.assertEqual(result, 121)

        x = 3141592653589793238462643383279502884197169399375105820974944592
        y = 2718281828459045235360287471352662497757247093699959574966967627
        expected = 8.539734222673566e+126
        result = karatsuba_multiplication(x, y)
        self.assertEqual(result, expected)
