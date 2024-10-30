n = int(input())
f = {}
z = []
for i in range(n):
    n,a,w,t = input().split(',')
    m,s = [int(e) for e in t.split(':')]
    if w not in f:
        f[w] = (m*60)+s
    elif w in f:
        f[w] = f[w]+((m*60)+s)
for i in f:
    z.append([f[i],i])
z.sort()
z = z[::-1]
if len(z) < 3:
    for i in range(len(z)):
        m = str(z[i][0]//60)
        s = z[i][0]%60
        if s < 10:
            s = '0'+str(s)
        else:
            s = str(s)
        print(z[i][1].strip(),'--> '+m+':'+s)
if len(z) >=3:
    for i in range(3):
        m = str(z[i][0]//60)
        s = z[i][0]%60
        if s < 10:
            s = '0'+str(s)
        else:
            s = str(s)
        print(z[i][1].strip(),' --> '+m+':'+s)