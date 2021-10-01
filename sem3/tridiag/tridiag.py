from random import randint


def find_error(x):
    y = [i + 1.0 for i in range(len(x))]
    error = max([abs(a - b) for (a, b) in zip(x, y)])
    max_y = max([abs(a) for a in y])
    return error / max_y
n = 3
k = 1
r = lambda: randint(-10, 10) * 1.00
a = [r() for _ in range(n - 1)]
b = [r() for _ in range(n - 1)]
y = [i + 1.0 for i in range(n)]
c = (
    [abs(b[0]) + 3 / 2 * k]
    + [abs(a[i - 1]) + abs(b[i]) + 3 / 2 * k for i in range(1, n - 1)]
    + [abs(a[n - 2]) + 3 / 2 * k]
)
f = (
    [c[0] * y[0] + -b[0] * y[1]]
    + [-a[i - 1] * y[i - 1] + c[i] * y[i] + -b[i] * y[i + 1] for i in range(1, n - 1)]
    + [-a[n - 2] * y[n - 2] + c[n - 1] * y[n - 1]]
)


# alpha = [0.0] * 2*n
# beta = [0.0] * 2*n
# x = [0.0] * n

# x[n-1] = f[n-1] - a[n-2] * beta[n-1]

def thomas(a,b,c,d):
    # a= [1,3,1.5,4.5,4.5]
    # b= [-6,-4.5,-7.5,-7.5,-4.5] 
    # c= [3,3,3,3,3]
    # d= [0,0,100,0,0]
    n = len(b)
    c.append(0.0)
    p = []; q= [] 
    p.append(c[0]/b[0]); q.append(d[0]/b[0])
    for j in range(1,n):
        pj = c[j]/(b[j] - a[j-1]* p[j-1])
        qj = (d[j] - a[j-1]*q[j-1])/(b[j] - a[j-1]* p[j-1])
        p.append(pj); q.append(qj)
    x = []; x.append(q[n-1])
    for j in range(n-2,-1,-1):
        xj = q[j] - p[j]*x[0] # Value holder
        x.insert(0,xj) # Building the list backwards
    return x    
print(a)
print(c)
print(b)
print(f)
print(thomas(a, c, b, f))