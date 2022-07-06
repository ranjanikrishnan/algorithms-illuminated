from typing import List, Tuple


def strassens_matrix_multiplication(x: List[List[int]], y: List[List[int]], n: int) -> List[List[int]]:
    if n == 1:
        z = [[0 for _ in range(n)] for _ in range(n)]
        z[0][0] = x[0][0] * y[0][0]
        return z

    a, b, c, d = get_submatrices(x, n)
    e, f, g, h = get_submatrices(y, n)

    fh = subtract_matrices(f, h, n//2)
    p1 = strassens_matrix_multiplication(a, fh, n//2)
    ab = add_matrices(a, b, n//2)
    p2 = strassens_matrix_multiplication(ab, h, n//2)
    cd = add_matrices(c, d, n//2)
    p3 = strassens_matrix_multiplication(cd, e, n//2)
    ge = subtract_matrices(g, e, n//2)
    p4 = strassens_matrix_multiplication(d, ge, n//2)
    ad = add_matrices(a, d, n//2)
    eh = add_matrices(e, h, n//2)
    p5 = strassens_matrix_multiplication(ad, eh, n//2)
    bd = subtract_matrices(b, d, n//2)
    gh = add_matrices(g, h, n//2)
    p6 = strassens_matrix_multiplication(bd, gh, n//2)
    ac = subtract_matrices(a, c, n//2)
    ef = add_matrices(e, f, n//2)
    p7 = strassens_matrix_multiplication(ac, ef, n//2)

    term_1_a = add_matrices(p5, p4, n//2)
    term_1_b = add_matrices(term_1_a, p6, n//2)
    term_1 = subtract_matrices(term_1_b, p2, n//2)

    term_2 = add_matrices(p1, p2, n//2)
    term_3 = add_matrices(p3, p4, n//2)

    term_4_a = add_matrices(p1, p5, n//2)
    term_4_b = subtract_matrices(term_4_a, p7, n//2)
    term_4 = subtract_matrices(term_4_b, p3, n//2)

    z = combine_submatrices(term_1, term_2, term_3, term_4, n)
    return z


def get_submatrices(x: List[List[int]], n: int) -> Tuple[List[List[int]], List[List[int]], List[List[int]], List[List[int]]]:
    a = [x[i][:n//2] for i in range(n//2)]
    b = [x[i][n//2:] for i in range(n//2)]
    c = [x[i][:n//2] for i in range(n//2, n)]
    d = [x[i][n//2:] for i in range(n//2, n)]

    return a, b, c, d


def subtract_matrices(a: List[List[int]], b: List[List[int]], n: int) -> List[List[int]]:
    c = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            c[i][j] = a[i][j] - b[i][j]
    return c


def add_matrices(a: List[List[int]], b: List[List[int]], n: int) -> List[List[int]]:
    c = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            c[i][j] = a[i][j] + b[i][j]
    return c


def combine_submatrices(term_1, term_2, term_3, term_4, n):
    z = [[0 for _ in range(n)] for _ in range(n)]
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
