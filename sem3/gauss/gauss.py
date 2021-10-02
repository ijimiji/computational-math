from random import randint
from functools import reduce
from copy import deepcopy


def id_matrix(n):
    matrix = [[0] * (n) for i in range(n)]
    for i in range(n):
        matrix[i][i] = 1.0
    return matrix


def hilbert_matrix(n):
    matrix = [[0] * (n + 1) for i in range(n)]
    xs = [i + 1 for i in range(n)]
    for i in range(n):
        for j in range(n):
            matrix[i][j] = 1.0 / (i + j + 1)
        matrix[i][n] = reduce(
            (lambda x, y: x + y),
            [x * a for (x, a) in zip(xs, [matrix[i][j] for j in range(n)])],
        )
    return matrix


def random_matrix(n):
    matrix = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            matrix[i][j] = randint(-100, 100) * 1.0
    return matrix


def random_matrix_with_b(n):
    matrix = [[0] * (n + 1) for i in range(n)]
    xs = [i + 1 for i in range(n)]
    for i in range(n):
        for j in range(n):
            matrix[i][j] = randint(-100, 100) * 1.0
        matrix[i][n] = reduce(
            (lambda x, y: x + y),
            [x * a for (x, a) in zip(xs, [matrix[i][j] for j in range(n)])],
        )
    return matrix


def mult(X, Y):
    return [
        [sum(a * b for a, b in zip(X_row, Y_col)) for Y_col in zip(*Y)] for X_row in X
    ]


def pretty_print(matrix):
    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = "\t".join("{{:{}}}".format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print("\n".join(table))


def find_error(x):
    ys = [i + 1 for i in range(len(x))]
    error = [abs(x - y) for (x, y) in zip(x, ys)]
    mes_error = max(error)
    mes_y = max([abs(y) for y in ys])
    return mes_error * 1.0 / mes_y


def gauss(A):
    A = deepcopy(A)
    m = len(A)
    n = m + 1
    for k in range(m):
        pivots = [abs(A[i][k]) for i in range(k, m)]
        i_max = pivots.index(max(pivots)) + k
        assert A[i_max][k] != 0, "Zero on main diag"
        A[k], A[i_max] = A[i_max], A[k]
        for i in range(k + 1, m):
            f = A[i][k] / A[k][k]
            for j in range(k + 1, n):
                A[i][j] -= A[k][j] * f
            A[i][k] = 0
    x = []
    for i in range(m - 1, -1, -1):
        x.insert(0, A[i][m] / A[i][i])
        for k in range(i - 1, -1, -1):
            A[k][m] -= A[k][i] * x[0]
    return x


def inverse(A):
    A = deepcopy(A)
    n = len(A)
    E = id_matrix(n)
    for i in range(n):
        pivots = [abs(A[z][i]) for z in range(i, n)]
        i_max = pivots.index(max(pivots)) + i
        assert A[i_max][i] != 0, "Zero on main diag"
        A[i], A[i_max] = A[i_max], A[i]
        E[i], E[i_max] = E[i_max], E[i]
        for k in range(i + 1, n):
            f = A[k][i] / A[i][i]
            for j in range(n):
                A[k][j] -= A[i][j] * f
                E[k][j] -= E[i][j] * f
    for i in range(n - 1, -1, -1):
        for k in range(i - 1, -1, -1):
            f = A[k][i] / A[i][i]
            for j in range(n):
                E[k][j] -= E[i][j] * f
    for i in range(n):
        for j in range(n):
            E[i][j] /= A[i][i]
    return E


H = hilbert_matrix(40)
y = gauss(H)
print(y)
print(f"Hilbert: error = {find_error(y)}")
