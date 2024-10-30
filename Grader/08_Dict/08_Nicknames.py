n = int(input())
c = {}
c_r = {}
dd = []
ans = []
for i in range(n):
    a,b = input().split()
    c[a] = b
    c_r[b] = a
m = int(input())
for i in range(m):
    k = input()
    dd.append(k)
for i in dd:
    if i in c:
        ans.append(c[i])
    elif i in c_r:
        ans.append(c_r[i])
    else:
        ans.append('Not found')
for i in range(len(ans)):
    print(ans[i])