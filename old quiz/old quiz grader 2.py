a = [int(e) for e in input().split()]
a = sorted(a)
A = len(a)
ans = []
A = A//2
if len(a)%2 == 0:
    Q1 = a[0:A]
    Q3 = a[A:]
else:
    Q1 = a[0:A]
    Q3 = a[A+1:]
for i in range(len(Q1)):
    if len(Q1)%2 == 0:
        x = len(Q1)//2
        q1 = (Q1[x] + Q1[x-1])/2
    else:
        x = len(Q1)//2
        q1 = Q1[x] 
for i in range(len(Q3)):
    if len(Q3)%2 == 0:
        x = len(Q3)//2
        q3 = (Q3[x] + Q3[x-1])/2
    else:
        x = len(Q1)//2
        q3 = Q3[x]
IQR = q3-q1
l = q1 - 1.5*IQR
u = q3 + 1.5*IQR
for i in a:
    if i < l:
        ans.append(i)
    elif i > u:
        ans.append(i)
if len(ans) == 0:
    print('L = '+str(l)+' '+'U = '+str(u))
    print('Not found')
else:
    ans = [str(i) for i in ans]
    print('L = '+str(l)+' '+'U = '+str(u))
    print(' '.join(ans))
        
    
#else:
    