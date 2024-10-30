n = int(input())
d1 = {}
d2 = {}
ans = []
for i in range(n):
    f,c = input().split()
    d1[f] = int(c)
h = int(input())
for i in range(h):
    ids,s,f1,f2,f3,f4 = input().split()
    s = float(s)
    d2[s] = [ids,f1,f2,f3,f4]
a = sorted(d2)[::-1]
for i in a:
    k = d2[i][1:]
    for j in k:
        if d1[j] != 0:
            d1[j] -= 1
            break
    ans.append([d2[i][0],j])
for i in sorted(ans):
    print(' '.join(i))