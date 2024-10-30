def grade_mcq(sol, ans):
    A = len(sol)
    B = len(ans)
    c = 0
    if A-B == 0:
        for i in range(len(sol)):
            if sol[i]==ans[i]:
                c +=1
        return c
    else:
        return -1
    
exec(input())