n = int(input())
p = []
c = 0
list_poweruse = []
for i in range(n):
    x = [int(e)for e in input().split()]
    p += x
power = int(input())
power_use = 0
for i in range(n-1):
    x = abs(p[(2*i)+2]-p[2*i])+abs(p[(2*i)+3]-p[(2*i)+1])
    if x > power:
        break
    else:
        power_use += x
        list_poweruse += [power_use]
        power -= x
        x = 0
        c += 1
ans = '1 '
for i in range(c):
    A = str(list_poweruse[i])
    I = str(i+2)
    H = '-> '+I+'['+A+']'
    ans += H
print(ans)