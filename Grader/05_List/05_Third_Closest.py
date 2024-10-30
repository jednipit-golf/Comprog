import math
n = int(input())
x = []
y = []
d = []
c = []
for i in range(n):
    a = input().split()
    x.append(float(a[0]))
    y.append(float(a[1]))
for i in range(n):
    D = math.sqrt((x[i]**2)+(y[i]**2))
    d.append(D)
for i in range(n):
    o = [d[i],x[i],y[i],i+1]
    c.append(o)
c.sort()
ans = c[2]
r = ''
r += '#'+str(ans[3])+': ('+str(ans[1])+', '+str(ans[2])+')'
print(r)
