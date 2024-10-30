sol = input()
ans = input()
A = len(sol)
B = len(ans)
c = 0
if A-B == 0:
    for i in range(len(sol)):
        if sol[i]==ans[i]:
            c +=1
    print(c)
else:
    print('Incomplete answer')