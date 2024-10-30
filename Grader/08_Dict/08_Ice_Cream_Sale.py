n = int(input())
k = {}
ans = []
ANS = {}
x = []
ts = []
total = 0
for i in range(n):
    a,b = input().split()
    k[a] = int(b)
s = int(input())
for i in range(s):
    c,d = input().split()
    if c in k.keys():
        ans.append([c,d])
if len(ans) == 0:
    print('No ice cream sales')
else:
    for i in ans:
        if i[0] not in ANS.keys():
            ANS[i[0]] = int(i[1])
        else:
            ANS[i[0]] += int(i[1])
    for i in ANS.keys():
        if i in k.keys():
            ANS[i] = ANS[i]*int(k[i])
    for i in ANS:
        x.append([ANS[i],i])
    xc = max(x)[0]
    for s,ic in x:
        if s == xc:
            ts.append(ic)
    ts.sort()
    for i in ANS:
        total += ANS[i]
        TS = ''
    for i in ts:
        TS += ' '+i+','
    TS = TS[1:-1:]
    print('Total ice cream sales: '+str(float(total)))
    print('Top sales: '+TS)

    