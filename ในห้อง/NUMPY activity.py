import numpy as np
def f1(M, c):
    A = M*c
    return A
def f2(U, V):
    return np.dot(U,V)
def f3(M):
    t =  np.transpose(M)
    return t
def f4(x, y, dx, dy, k, R):
    d = (x-x[k])**2 + (y-y[k])**2 
    mask = d <= R**2
    sx, sy = np.sum(dx[mask]), np.sum(dy[mask])
    t = np.arctan2(sy, sx)
    return np.cos(t), np.sin(t)

for k in range(int(input())):
    exec(input().strip())