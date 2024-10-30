import numpy as np
def get_column_from_bottom_to_top(A,c):
    a = A[::-1,c]
    return a
def get_odd_rows(A):
    a = A[1::2,]
    return a
def get_even_column_last_row(A):
    a = A[-1,::2]
    return a
def get_diagonal1(A):
    z = []
    a = A.shape[0]
    for i in range(a):
        k = A[i,i]
        z.append(k)
    c = np.array(z)
    return c
def get_diagonal2(A):
    z = []
    a = A.shape[0]
    for i in range(a):
        k = A[i,a-(1+i)]
        z.append(k)
    c = np.array(z)
    return c

exec(input().strip()) 