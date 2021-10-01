from random import randint


def find_error(x):
    y = [i + 1.0 for i in range(len(x))]
    error = max([abs(a - b) for (a, b) in zip(x, y)])
    max_y = max([abs(a) for a in y])
    return error / max_y


n = 2
k = 1
r = lambda: randint(-100, 100) * 1.00
a = [r() for _ in range(n - 1)]
b = [r() for _ in range(n - 1)]
y = [i + 1.0 for i in range(n)]
c = (
    [abs(b[0]) + 3 / 2 * k]
    + [abs(a[i - 1]) + abs(b[i]) + 3 / 2 * k for i in range(1, n - 1)]
    + [abs(a[n - 2]) + 3 / 2 * k]
)
f = (
    [c[0] * y[0] + b[0] * y[1]]
    + [a[i - 1] * y[i - 1] + c[i] * y[i] + b[i] * y[i + 1] for i in range(1, n - 1)]
    + [a[n - 2] * y[n - 2] + c[n - 1] * y[n - 1]]
)

print(a)
print(b)
print(c)
print(f)
# alpha = [0.0] * n
# beta = [0.0] * (n + 1)
# y_ = [0.0] * n

# alpha[0] = b[0] / c[0]
# beta[0] = f[0] / c[0]
# for i in range(1, n):
#     product = c[i] - a[i - 1] * alpha[i - 1]
#     alpha[i] = b[i] / product
#     beta[i] = (f[i] + a[i - 1] * beta[i - 1]) / product

# beta[n] = (f[n - 1] + a[n - 1] * beta[n - 2]) / (c[n - 2] - a[n - 2] * alpha[n - 2])

# y_[n - 1] = beta[n - 1]
# for i in range(n - 2, -1):
#     y_[i] = alpha[i] * y_[i + 1] + beta[i]
# m = 10

