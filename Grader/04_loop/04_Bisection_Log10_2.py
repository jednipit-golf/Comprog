import math
a = float(input())
L = 0
U = 0
a0 = a
while a0 > 0:
    a0//=10
    U+=1
x = (L+U)/2
print(U)
while not math.isclose(a,10**x):
    if 10**x>a:
        U = x
    elif 10**x<a:
        L = x
    x = (U+L)/2
    
print(round(x,6))