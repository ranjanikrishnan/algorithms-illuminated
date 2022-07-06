from typing import List


def recursive_matrix_multiplication(x: List[List[int]], y: List[List[int]]) -> List[List[int]]:
    n = len(x)
    z = [[0 for _ in range(n)] for _ in range(n)]

    if n == 1:
        z[0][0] = x[0][0] * y[0][0]
        return z

    a, b, c, d = get_submatrices(x, n)
    e, f, g, h = get_submatrices(y, n)

    p1 = recursive_matrix_multiplication(a, e)
    p2 = recursive_matrix_multiplication(b, g)
    p3 = recursive_matrix_multiplication(a, f)
    p4 = recursive_matrix_multiplication(b, h)
    p5 = recursive_matrix_multiplication(c, e)
    p6 = recursive_matrix_multiplication(d, g)
    p7 = recursive_matrix_multiplication(c, f)
    p8 = recursive_matrix_multiplication(d, h)

    term_1 = add_matrix(p1, p2)
    term_2 = add_matrix(p3, p4)
    term_3 = add_matrix(p5, p6)
    term_4 = add_matrix(p7, p8)

    z = combine_submatrices(term_1, term_2, term_3, term_4, n, z)
    return z


def get_submatrices(x, n):
    a = [x[i][:n//2] for i in range(n//2)]
    b = [x[i][n//2:] for i in range(n//2)]
    c = [x[i][:n//2] for i in range(n//2, n)]
    d = [x[i][n//2:] for i in range(n//2, n)]

    return a, b, c, d


def add_matrix(a1, a2):
    added = []
    for i in range(len(a1)):
        result = []
        for j in range(len(a1[0])):
            result.append(a1[i][j]+a2[i][j])
        added.append(result)
    return added


def combine_submatrices(term_1, term_2, term_3, term_4, n, z):
    for i in range(n//2):
        for j in range(n//2):
            z[i][j] = term_1[i][j]

    for i in range(n//2):
        for j in range(n//2, n):
            z[i][j] = term_2[i][j-n//2]

    for i in range(n//2, n):
        for j in range(n//2):
            z[i][j] = term_3[i-n//2][j]

    for i in range(n//2, n):
        for j in range(n//2, n):
            z[i][j] = term_4[i-n//2][j-n//2]

    return z
