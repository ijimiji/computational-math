from math import exp, cos, pi
import matplotlib.pyplot as plt

a = -2
b =  2

f_1 = lambda x: exp(cos(x))
f_2 = lambda x: abs(x * abs(x) - 1)

x_ch = lambda k, n: (a+b)/2  + (b-a) / 2 * cos((2*k + 1)*pi / (2*n +2))
x_ = lambda i, n: a + i*(b-a)/n

def newton(x, y, n):
    xss = [x(i, n) for i in range(n)]
    yss = [y(xss[i]) for i in range(n)]
    coefficients = [xss, yss]
    for i in range(1, n):
        prev = coefficients[i]
        diff = []
        for j in range(0, n-i):
            d = (prev[j] - prev[j+1]) / (xss[j] - xss[j+i])
            diff.append(d)
        coefficients.append(diff)
    return coefficients

def calc(x, c):
    ans = 0
    factor = 1
    n = len(c[0])
    for i in range(n):
        ans = ans + c[i+1][0] * factor
        factor = factor * (x-c[0][i])
    return ans

def compare(f, n):
    c = newton(x_, f, n)
    c_ch = newton(x_ch, f, n)
    m = 100
    xss = [x_(i, m) for i in range(m)]
    print(n)
    print(f"Ordinary error: {max(f, c)}")
    print(f"Chebyshev error: {max(f, c_ch)}")
    print()

    plt.plot(
            xss, [calc(x,c) for x in xss], "b",
            xss, [calc(x,c_ch) for x in xss],  "r",
            xss, [f(x) for x in xss], "g",

            c_ch[0], [f(x) for x in c_ch[0]], "ro",
            c[0], [f(x) for x in c[0]], "bo")
    plt.show()

def max(f, c):
    n = 101
    m = abs(calc(x_(0, n), c)  - f(x_(0, n)))
    for i in range(n):
        temp = abs(calc(x_(i, n), c)  - f(x_(i, n)))
        if temp > m:
            m = temp
    return m

print("f_1")
for i in [5, 10, 15, 20]:
    compare(f_1, i)

print("f_2")
for i in [5, 10, 15, 20]:
    compare(f_2, i)
    
