import numpy as np
import math
def p(x):
    a = x[::,0]
    b = x[::,1]
    logit = (-3.98 + 0.1*a + 0.5*b)*-1
    f = (1+(math.e)**(logit))**(-1)
    return f
   
exec(input().strip())