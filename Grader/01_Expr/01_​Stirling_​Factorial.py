import math
x = int(input())

a = (2*math.pi)**0.5
b = x**(x+0.5)
c = (math.e)**(-x+1/((12*x)+1))
d = (math.e)**(-x+1/(12*x))

underbound = a*b*c
upperbound = a*b*d
print(underbound)
print(upperbound)