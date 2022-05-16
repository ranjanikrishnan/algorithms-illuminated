def matrix_multiplication(x, y):
    n = len(x)
    z = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            z[i][j] = 0
            for k in range(n):
                z[i][j] = z[i][j] + x[i][k] * y[k][j]
    return z
