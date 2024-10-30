import numpy as np
def sum_2_rows(M):
    a = M[::2]+M[1::2]
    return a

def sum_left_right(M):
    s = (M.shape[1])//2
    a = M[::,0:s]+M[::,s:]
    return a

def sum_upper_lower(M):
    s = (M.shape[0])//2
    a = M[0:s]+M[s:]
    return a
def sum_4_quadrants(M):
    x = (M.shape[0])//2
    y = (M.shape[1])//2
    a1 = M[0:x,0:y];a2 = M[0:x,y:];a3 = M[x:,0:y];a4 = M[x:,y:]
    i = a1+a2+a3+a4
    return i
def sum_4_cells(M):
    k = []
    x = (M.shape[0])//2
    y = (M.shape[1])//2
    for i in range(x):
        for j in range(y):
            a = M[0+2*i:2+2*i,0+2*j:2+2*j]
            k.append(np.sum(a))
    i = np.array(k).reshape(x,y)
    return i
def count_leap_years(years):
    years = years-543 
    a=np.sum((years%400==0) | (years%4==0) &(years%100!=0))
    return a

exec(input().strip())
