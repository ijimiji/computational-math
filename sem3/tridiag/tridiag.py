from random import randint

N = 9
k = 1


def find_error(x):
    y = [i + 1.0 for i in range(len(x))]
    error = max([abs(a - b) for (a, b) in zip(x, y)])
    max_y = max([abs(a) for a in y])
    return error / max_y


r = lambda: randint(-10, 10) * 1.00

# Задаем вектора, которые стоят на главной диагонали, под и над ней
a = [0.0] + [r() for _ in range(1, N + 1)]
b = [r() for _ in range(0, N)]
c = (
    [abs(b[0]) + 1.5 * k]
    + [abs(a[i]) + abs(b[i]) + 1.5 * k for i in range(1, N)]
    + [abs(a[N]) + 1.5 * k]
)
# Задаем точное решение и резервируем ресурсы для численного решения
y = [i + 1.0 for i in range(N + 1)]
x = [0.0] * (N + 1)

# Задаем вектор правой части
f = [0.0] * (N + 1)
f = (
    [c[0] * y[0] + -b[0] * y[1]]
    + [-a[i] * y[i - 1] + c[i] * y[i] + -b[i] * y[i + 1] for i in range(1, N)]
    + [-a[N] * y[N - 1] + c[N] * y[N]]
)

# Прямой ход
alpha = [0.0]
beta = [0.0]
alpha.append(b[0] / c[0])
beta.append(f[0] / c[0])
for i in range(1, N):
    product = c[i] - a[i] * alpha[i]
    alpha.append(b[i] / product)
    beta.append((f[i] + a[i] * beta[i]) / product)
beta.append((f[N] + a[N] * beta[N]) / (c[N] - a[N] * alpha[N]))

# Обратный ход
x[N] = beta[N + 1]
for i in reversed(range(N)):
    x[i] = alpha[i + 1] * x[i + 1] + beta[i + 1]

# Выводим результаты
print(f"a ={a}")
print(f"b ={b}")
print(f"c ={c}")
print(f"f ={f}")
print(f"y*={x}")
print(f"y ={y}")

print(f"Погрешность {find_error(x)}")
