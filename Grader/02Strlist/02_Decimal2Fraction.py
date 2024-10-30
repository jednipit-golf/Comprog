import math
a,b,c = input().split(",")
B1 = int(a+b+c)
B2 = int(a+b)
a = B1-B2
b = (10**len(b+c))-(10**len(b))

gcd = math.gcd(a,b)
print(a//gcd,"/",b//gcd)