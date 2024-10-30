def factor(n):
    ans = []
    k = 2
    while n>= k:
        c = 0
        while n%k == 0:
            n = n//k
            c += 1
        if c != 0:
            ans.append([k,c])
        k += 1
        c = 0
    return ans    
exec(input().strip())