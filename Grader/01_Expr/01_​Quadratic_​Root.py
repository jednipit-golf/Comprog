a  = float(input())
b  = float(input())
c  = float(input())
import math
A1 = -b
A2 = ((b**2)-(4*a*c))**0.5
A3 = 2*a

x1 = (A1-A2)/A3
x2 = (A1+A2)/A3

print(round(x1,3),round(x2,3))


import math
a = float(input())
b = float(input())
c = float(input())

x1 = (-b-(math.sqrt(b2-(4ac))))/ (2*a)
x2 = (-b+(math.sqrt(b2-(4ac))))/ (2*a)

print(round(x1,3),round(x2,3))