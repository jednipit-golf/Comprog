a = input().lower()
z = ''
c = {}
ans = []
for i in a:
    if 'a' <= i <= 'z':
        z += i
for i in z:
    if not i in c.keys():
        c[i] = 1
    else:
        c[i] = c[i]+1
for i in c.keys():
    ans.append([-c[i],i])
ans.sort()
for i in ans:
    k = i[1]+' -> '+str(-i[0])
    print(k)