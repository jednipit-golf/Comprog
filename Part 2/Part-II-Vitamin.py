n = int(input())
k = []
for i in range(n):
    a = input().split()
    k.append(a)   
c = input().split(' ')
if c[0] == 'show' :
    for i in k:
        print(' '.join(i))
elif c[0] == 'max' :
    h = {}
    a = int(c[1])
    for i in k:
        if float(i[a]) not in h:
            h[float(i[a])] = [i[0]]
        else:
            h[float(i[a])] += [i[0]]
    k = sorted(h)[::-1][0]
    s = h[k]
    ans = min(s)
    for i,b in h.items():
        if ans in b:
            print(ans+' '+str(i))
elif c[0] == 'avg' :
    h = 0
    a = int(c[1])
    for i in k:
        h += float(i[a])
    h = h/len(k)
    print(round(h,4))
elif c[0] == 'get' :
    s = 0
    for i in k:
        if c[1] == i[0]:
            print(' '.join(i))
            s = 1
            break
    if s == 0:
        print(c[1]+' not found')

elif c[0] == 'sort' :
    h = {}
    ans = []
    kk = []
    a = int(c[1])
    for i in k:
        if float(i[a]) not in h:
            h[float(i[a])] = [i[0]]
        else:
            h[float(i[a])] += [i[0]]
    for lion in h.keys():
        h[lion] = sorted(h[lion])
    k = sorted(h)
    for i in k:
        ans = ans + h[i]
    print(' '.join(ans))
