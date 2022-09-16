from math import ceil, exp, log
from matplotlib import pyplot as plt

a = 1.
b = 2.
initial = exp(a)
f = lambda x, y: y * log(y) / x
u = lambda x: exp(x)
dudu = lambda x, y: (log(y) + 1) / x
eps = 0.000001

def runge(h, ass, alpha, beta):
    q = len(ass)
    n = ceil((b - a) / h) + 1
    ys = [initial]
    xs = [a + i * h for i in range(n)]
    for i in range(n-1):
        integral = 0.
        phi = [f(xs[i], ys[i])]
        for k in range(q):
            if k != 0:
                phi.append(f(xs[i] + h * alpha[k-1], ys[i] + h * sum([beta[k-1][j] * phi[j] for j in range(k)])))
            integral += ass[k] * phi[k]
        ys.append(ys[i] + h * integral)

    norm = max([abs(ys[i] - u(xs[i])) for i in range(n-1)])
    plt.plot(xs, ys, "ro", xs, [u(x) for x in xs], "b")
    plt.legend(["$y(x)$", "$e^x$"])
    plt.title(f"$q = {q}$, $h = {h}$, norm = ${norm}$")
    plt.show()
    print(f"q = {q}, h = {h}, norm = {norm}")

def euler(h):
    n = ceil((b - a) / h)
    ys = [initial]
    xs = [a + i * h for i in range(n)]
    for i in range(n-1): 
        last = ys[-1]
        while True:
            current = last - (last - ys[-1] - 0.5 * h * (f(xs[i], ys[-1]) + f(xs[i+1], last)))/(1 - 0.5 * h * dudu(xs[i+1], last))
            if abs(last - current) < eps:
                ys.append(current)
                break
            last = current
    norm = max([abs(y - u(x)) for (x, y) in zip(xs, ys)])
    plt.plot(xs, ys, "ro", xs, [u(x) for x in xs], "b")
    plt.legend(["$y(x)$", "$e^x$"])
    plt.title(f"Euler $h = {h}$, norm = ${norm}$")
    plt.show()
    print(f"Euler h = {h}, norm = {norm}")

euler(0.1)
euler(0.05)

runge(0.1,[0, 1], [0.5], [[0.5]])
runge(0.05,[0, 1], [0.5], [[0.5]])
runge(0.1,[1./6, 2./6, 2./6, 1./6], [0.5, 0.5, 1], [[0.5, 0., 0.], [0, 0.5, 0], [0, 0, 1]] )
runge(0.05,[1./6, 2./6, 2./6, 1./6], [0.5, 0.5, 1], [[0.5, 0., 0], [0, 0.5, 0], [0, 0, 1]] )

