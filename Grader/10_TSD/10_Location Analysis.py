n = int(input())
ans = {}
ss = []
c = []
p = []
for i in range(n):
    ids,c = input().strip().split(':')
    for j in c.split(','):
        p.append(j.strip())
    ans[ids] = p
    p = []
f = input()
if f in ans:
    d = ans[f]
for i,b in ans.items():
    if i == f:
        pass
    else:
        for l in b:
            if l in d:
                ss.append(i)
                break
if ss == []:
    print('Not Found')
else:
    for i in ss:
        print(i)
        