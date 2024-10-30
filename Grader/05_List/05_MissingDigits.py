a = input().strip()
A = len(a)
c = ['0','1','2','3','4','5','6','7','8','9']
k = []
s = []
ans = ''
for i in range(A):
    if a[i] == '0':k.append('0')
    elif a[i] == '1':k.append('1')
    elif a[i] == '2':k.append('2')
    elif a[i] == '3':k.append('3')
    elif a[i] == '4':k.append('4')
    elif a[i] == '5':k.append('5')
    elif a[i] == '6':k.append('6')
    elif a[i] == '7':k.append('7')
    elif a[i] == '8':k.append('8')
    elif a[i] == '9':k.append('9')
k.sort()
K = len(k)
if K != 0:
    x = k[0]
    s.append(x)
    for i in range(1,K-1):
        if x == k[i]:pass
        elif x != k[i]:
            s.append(k[i])
            x = k[i]
    if len(s) == 10:print('None')
    else:
        for i in s:
            c.remove(i)
        C = len(c)
        for i in range(C):
            ans += c[i]+','
        print(ans[:-1])
else:
    print('1,2,3,4,5,6,7,8,9')
    