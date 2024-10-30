d = input().split()
D = len(d)
n = D//2
action = input()
A = len(action)
for i in range(A):
    if action[i] == 'C':
        d = d[n:2*n]+d[0:n]
    if action[i] == 'S':
        for k in range(n):
            d.append(d[k])
            d.append(d[k+n])
        d=d[D:2*D]
    else:
        pass
ans = ''
for i in range(D):
    ans += d[i]
    ans += ' '
print(ans[:-1:])
    