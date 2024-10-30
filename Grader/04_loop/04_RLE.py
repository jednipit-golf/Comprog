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
    
