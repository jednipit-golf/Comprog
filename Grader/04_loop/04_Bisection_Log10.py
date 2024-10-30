import math
a = float(input())
L = 0
U = a
x = (L+U)/2
while not math.isclose(a,10**x):
    print('x = ', x )
    if 10**x>a:
        U = x
    elif 10**x<a:
        L = x
    x = (U+L)/2
    
print(round(x,6))