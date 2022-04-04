from math import exp, cos, sin
import numpy as np
from matplotlib import pyplot as plt

a = -2
b = 2
N = 10
h = (b-a) / N
f = lambda x: exp(cos(x))
dfdx = lambda x: -sin(x) * exp(cos(x))
# f = lambda x: abs(x)
# dfdx = lambda x: -1 if x== -2 else 1
xss = [a + i*h for i in range(0, N+1)]
yss = [f(x) for x in xss]

def TDMA(a, b, c, d):
    n = len(d)
    w=  [.0] * (n-1)
    g= [.0] * n
    p= [.0] * n
    
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

css = []
ass = []
bss = []
dss = []
for i in range(0, N+1):
    if i== 0:
        ass.append(h/3)
        bss.append(h/6)
        dss.append((yss[1] - yss[0])/h - dfdx(a))
    elif i== N:
        css.append(h/6)
        ass.append(h/3)
        dss.append(dfdx(b) - (yss[N] - yss[N-1])/h)
    else:
        css.append(h/6)
        ass.append(2*h/3)
        bss.append(h/6)
        dss.append((yss[i+1] - yss[i])/h - (yss[i] - yss[i-1])/h)

mss = TDMA(css,ass,bss,dss)
sss = []

def wrap(i):
    def s(x): 
        return (xss[i] - x)**3 * mss[i-1] / (6*h)  + (x-xss[i-1])**3 * mss[i] / (6*h) + (yss[i-1] - mss[i-1]*h*h/6)*(xss[i] - x)/h + (yss[i] - mss[i] *h*h /6)*(x-xss[i-1])/h
    return s

for i in range(1, N+1):
    sss.append(wrap(i))

def S(x):
    i  = int((x - a)/h)
    if i == 10:
        i = 9
    return sss[i](x)

def compare(n):
    d = (b-a)/n
    xs = [a + i * d for i in range(n+1)]
    plt.plot(
            xs, [S(x) for x in xs], "b",
            xs, [f(x) for x in xs],  "r",
            xss, [f(x) for x in xss], "ro",
    )
    plt.legend(["S(x)", "f(x)"])
    plt.show()

def error():
    d = (b-a)/100
    xs = [a + i * d for i in range(101)]
    return max([abs(f(x) - S(x)) for x in xs])

print(error())

compare(100)