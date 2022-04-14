from math import cos, exp
import numpy as np
from matplotlib import pyplot as plt
h = 0.1
a = -2
b =  2
f = lambda x: exp(cos(x))
def build(n):
    k = int((b-a) / h) + 1
    xs = [a + h * i for i in range(k)]
    ys = [f(x) for x in xs]
    ss = np.array([[sum([x ** (i+j) for x in xs]) for j in range(n+1)] for i in range(n+1)])
    ms = np.array([sum([x**i * y for (x, y) in zip(xs, ys)]) for i in range(n+1)])
    cs = np.linalg.solve(ss, ms)
    q = lambda x: sum([c*(x**i) for (c,i) in zip(cs, range(n+1))])
    ds = [a + i * (b-a)/100 for i in range(101)]
    print(sum([(f(x) - q(x))**2 for x in xs]))
    plt.plot(xs, ys, "ro", ds, [q(x) for x in ds], "b")
    plt.legend(["$e^{\\cos x}$", "$q(x)$"])
    plt.show()
build(3)
build(6)