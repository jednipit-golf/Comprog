import numpy as np
def toCelsius(f):
    return (f-32)*(5/9)
def BMI(wh):
    weight = wh[::,0]
    height = wh[::,1]
    BMI = weight/((height/100)**2)
    return BMI
def distanceTo(p,Points):
    x = Points[::,0]
    y = Points[::,1]
    c = p[0]
    k = p[1]
    distance = ((x-c)**2 + (y-k)**2)**0.5
    return distance

exec(input().strip()) 