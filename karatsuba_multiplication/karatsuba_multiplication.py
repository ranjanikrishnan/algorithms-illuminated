from typing import Tuple


def karatsuba_multiplication(x: int, y: int) -> int:
    n = get_number_of_digits(x)
    if n == 1:
        return x*y
    a, b = split_number_into_two(x, n)
    c, d = split_number_into_two(y, n)
    p = a + b
    q = c + d
    pq = p * q
    ac = karatsuba_multiplication(a, c)
    bd = karatsuba_multiplication(b, d)
    adbc = pq - ac - bd
    return pow(10, n) * ac + pow(10, n/2) * adbc + bd


def get_number_of_digits(num: int) -> int:
    return len(str(num))


def split_number_into_two(num: int, number_length: int) -> Tuple[int, int]:
    i = pow(10, number_length/2)
    first_half = int(num // i)
    second_half = int(num % i)
    return first_half, second_half
