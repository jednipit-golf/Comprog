a = input().strip().lower()
c = []
for i in a:
    if i == ' ':
        pass
    else:
        c.append(i)
c.sort()
b = input().strip().lower()
d = []
for i in b:
    if i == ' ':
        pass
    else:
        d.append(i)
d.sort()
k = 0
if len(c) == len(d):
    for i in range(len(c)):
        if c[i] != d[i]:
            k+= 1
    if k == 0:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
    