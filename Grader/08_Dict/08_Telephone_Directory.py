n = int(input())
c = {}
j = []
ans = []
for i in range(n):
    x,y,z = input().strip().split()
    name = x+' '+y
    c[name] = z
    c[z] = name
k = int(input())
for i in range(k):
    a = input().strip()
    j.append(a)
for i in j:
    if i in c:
        ans.append([i,c[i]])
    else:
        ans.append([i,'Not found'])
for i in ans:
    k = i[0]+' --> '+i[1]
    print(k)
