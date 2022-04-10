import unittest
from karatsuba_multiplication import karatsuba_multiplication, split_number_into_two, get_number_of_digits


class TestKaratsubaMultiplication(unittest.TestCase):
    def test_karatsuba_multiplication(self):
        result = karatsuba_multiplication(1234, 5678)
        self.assertEqual(result, 7006652)
        
        result = karatsuba_multiplication(11, 11)
        self.assertEqual(result, 121)

    def test_split_number_into_two(self):
        result_1, result_2 = split_number_into_two(1234, 4)
        self.assertEqual(result_1, 12)
        self.assertEqual(result_2, 34)

    def test_get_number_of_digits(self):
        result = get_number_of_digits(1234)
        self.assertEqual(result, 4)

        result = get_number_of_digits(56)
        self.assertEqual(result, 2)
