from math import ceil
import numpy as np
from matplotlib import pyplot as plt

def TDMA(a, b, c, d):
    n = len(d)
    w= np.zeros(n-1,float)
    g= np.zeros(n, float)
    p = np.zeros(n,float)
    
    w[0] = c[0]/b[0]
    g[0] = d[0]/b[0]

    for i in range(1,n-1):
        w[i] = c[i]/(b[i] - a[i-1]*w[i-1])
    for i in range(1,n):
        g[i] = (d[i] - a[i-1]*g[i-1])/(b[i] - a[i-1]*w[i-1])
    p[n-1] = g[n-1]
    for i in range(n-1,0,-1):
        p[i-1] = g[i-1] - w[i-1]*p[i]
    return p

def u(x):
    return x**2 - x

def solve(h):
    # c lower
    # a middle
    # b upper

    N = ceil(1 / h)

    b_1 = [1] ##
    b_i = [1 + (i*h) * h for i in range(1,N)] #

    a_1 = [2*h**2 - 1] ##
    a_i = [-2 - 4 * h**2 for i in range(1, N)] #
    a_N = [1 + 2 *h +4*h**2]

    c_i = [1 - (i*h)*h for i in range(1, N)] #
    c_N = [-1]
    
    f_1 = [-h+h**2] ##
    f_i = [(2*(i*h) + 2) * h**2 for i in range(1, N)] #
    f_N = [h-h**2]

    ys = TDMA(
        c_i + c_N,
        a_1 + a_i + a_N,
        b_1 + b_i,
        f_1 + f_i + f_N,
    )

    xs = [i * h for i in range(N+1)]
    plt.plot(xs, ys, "ro", xs, [u(x) for x in xs], "b")
    plt.legend(["$y(x)$", "$u(x)$"])
    plt.show()

    print(ys)
    print(max([u(x) - y for (x,y) in zip(xs, ys)]))
    return ys



y1 = solve(0.02)
y2 = solve(0.01)
print(max([abs(y2[2*i] - y1[i]) for i in range(ceil(1 / 0.02))]))


