from functools import reduce
from random import randint
from copy import deepcopy

n = 10
e = 10 ** -7
k_max = 1000

# Random matrix
matrix = [[randint(-100, 100) * 1.0 for _ in range(n)] for _ in range(n)]

# Filling upper triangle
for i in range(n):
    for j in range(i + 1, n):
        matrix[i][j] = matrix[j][i]
s = sum(
    [sum([abs(matrix[i][j]) for j in range(n)]) - abs(matrix[i][i]) for i in range(n)]
)
for i in range(n):
    matrix[i][i] = s + randint(1, 10)

# Exact solution
xs = [i for i in range(1, n + 1)]

# Right part
f = [
    reduce((lambda x, y: x + y), [x * a for (x, a) in zip(xs, matrix[i])])
    for i in range(n)
]

# x^k and x^(k+1)
x_old = deepcopy(f)
x_new = [0.0] * n

# Jacobi method
q = 0
while True:
    x_new = [
        (
            f[i]
            - (
                reduce(
                    (lambda x, y: x + y), [x * a for (x, a) in zip(x_old, matrix[i])]
                )
                - matrix[i][i] * x_old[i]
            )
        )
        / matrix[i][i]
        for i in range(n)
    ]
    q += 1
    error = max([abs(x - y) for (x, y) in zip(x_old, x_new)])
    if q > k_max:
        print("Превышено число итераций")
        break
    if error <= e:
        print(f"max |x^q_i - x^(q-1)_i| = {error}")
        break
    x_old = deepcopy(x_new)


def pretty_print(matrix):
    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = "\t".join("{{:{}}}".format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print("\n".join(table))


print("Матрица:")
pretty_print(matrix)
print("Точное решение:")
print(xs)
print("Правая часть:")
print(f)
print("Начальное приближение:")
print(f)

print("==============================Якоби================================")
print("Номер итерации для метода Якоби:")
print(q)
print("Численное решение для метода Якоби")
print(x_new)
print("Абсолютная погрешность")
print(max([abs(x_new[i] - xs[i]) for i in range(n)]))
print("===================================================================")

print("==============================Релаксация===========================")
omegas = [0.2, 0.5, 0.8, 1.0, 1.3, 1.5, 1.8]

for omega in omegas:
    q = 0
    x_old = deepcopy(f)
    # Relaxation with different parameters
    while True:
        for i in range(n):
            base = (1 - omega) * x_old[i]
            old = 0
            new = f[i]
            for j in range(0, i - 1):
                new -= matrix[i][j] * x_new[j]
            for j in range(i + 1, n):
                new -= matrix[i][j] * x_old[j]
            x_new[i] = base + new * omega / matrix[i][i] + old

        q += 1
        error = max([abs(x - y) for (x, y) in zip(x_old, x_new)])
        if q > k_max:
            print("Превышено число итераций")
            break
        if error <= e:
            print(f"Параметр релаксации равный {omega}")
            print(f"Число итераций {q}")
            print(f"max |x^q_i - x^(q-1)_i| = {error}")
            print(
                f"Абсолютная погрешность {max([abs(x_new[i] - xs[i]) for i in range(n)])}"
            )
            break
        x_old = deepcopy(x_new)
print("==============================Релаксация===========================")
