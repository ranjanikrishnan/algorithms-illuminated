from typing import Tuple


def recursive_integer_multiplication(x: int, y: int) -> int:
    n = get_number_of_digits(x)
    if n == 1:
        return x*y

    a, b = split_number_into_two(x, n)
    c, d = split_number_into_two(y, n)
    ac = recursive_integer_multiplication(a, c)
    ad = recursive_integer_multiplication(a, d)
    bc = recursive_integer_multiplication(b, c)
    bd = recursive_integer_multiplication(b, d)
    return pow(10, len(str(x)))*ac + pow(10, len(str(x))/2)*(ad+bc) + bd


def get_number_of_digits(num: int) -> int:
    return len(str(num))


def split_number_into_two(num: int, num_length) -> Tuple[int, int]:
    i = pow(10, num_length/2)
    first_half = int(num // i)
    second_half = int(num % i)
    return first_half, second_half
