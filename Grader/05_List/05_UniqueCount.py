x = [int(e) for e in input().split()]
x.sort()
if len(x)>0:
    s = x[0]
    a = [s]
    c = 1
    for i in range(1,len(x)):
        if x[i] == s:
            c+=1
        elif x[i] != s and c >0:
            a.append(x[i])
            c = 1
            s = x[i]
print(len(a))
if len(a)>10:
    a = a[:10]
print(a)
        