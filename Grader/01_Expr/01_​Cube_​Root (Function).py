import math
def sqrt_n_times(x, n):
    a = x**(1/(2**n))
    return a
    
def cube_root(y):
    a = sqrt_n_times(y,2)
    b = sqrt_n_times(a,2)*a
    c = sqrt_n_times(b,4)*b
    d = sqrt_n_times(c,8)*c
    e = sqrt_n_times(d,16)*d
    f = sqrt_n_times(e,32)*e
    g = a*b*c*d*e*f
    result_cube_root = f
    return result_cube_root

def main():
    q = float(input())
    print(cube_root(q))

exec(input()) 