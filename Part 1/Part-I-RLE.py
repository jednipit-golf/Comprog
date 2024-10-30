b = input()
if b == 'str2RLE':
    A = input()
    a = A[0]
    ans = []
    p = ''
    for i in range(len(A)-1):
        if a[0] == A[i+1]:
            a += A[i+1]
        elif a[0] != A[i+1]:
            ans += [a]
            a = A[i+1]
    ans += [a]
    y = len(ans)
    for i in range(y):
        word = ans[i]
        c = str(len(word))
        pp = word[0]+' '+c+' '
        p += pp
    print(p)
elif b == 'RLE2str':
    a = input().split()
    A = len(a)
    ans = ''
    for i in range(A//2):
        ans += a[2*i]*int(a[2*i+1])
    print(ans)
else:
    print('Error')
    
