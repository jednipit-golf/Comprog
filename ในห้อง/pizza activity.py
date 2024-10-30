c = {}
pizza = {'PZ871':265.25,'PZ953':246.5,'Z1983':256.5,'Z2853':272.5,'LC673':309.25}
n = int(input())
ans = []
for i in range(n):
    a = input().split(',')
    C = (len(a)-1)//2
    p = {}
    if a[0] not in c:
        c[a[0]] = 0
    for k in range(C):
        count = 0
        if a[2*k+1] in pizza:
            count += pizza[a[2*k+1]]*int(a[2*k+2])
            if a[0] in c:
                c[a[0]] += count
s = len(c)
for i in c:
    ans.append([i,c[i]])
ans.sort()
for i in range(s):
    KK = ans[i][0]+' -> '+str(ans[i][1])
    print(KK)

                
            
        