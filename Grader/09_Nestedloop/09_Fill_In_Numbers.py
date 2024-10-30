def pattern1(nrows, ncols):
    x = [[0]*n for i in range(nrows)]
    i = 1
    for r in range(nrows):
        for c in range(ncols):
            x[r][c] = i
            i +=1
    return x
def pattern2(nrows, ncols):
    c = []
    a = nrows * ncols
    n = []
    for i in range(1,nrows+1):
        for j in range(i,a+1,nrows):
            n.append(j)
        c.append(n)
        n = []
    return c
def pattern3(n):
    x = [[0]*n for i in range(n)]
    i = 1
    for r in range(n):
        for c in range(r,n):
            x[r][c] = i
            i +=1
    return x 
def pattern4(n):
    x = [[0]*n for i in range(n)]
    i = 1
    for c in range(n):
        for r in range(c,-1,-1):
            x[r][c] = i
            i+= 1
    return x
def pattern5(n):
    x = [[0]*n for i in range(n)]
    i = 1
    for d in range(n):
        for r in range(0,n-d):
            c = r+d
            x[r][c] = i
            i +=1
    return x
def pattern6(n):
    x = [[0]*n for i in range(n)]
    i = 1
    for d in range(n):
        if d%2 == 0:
            for r in range(0,n-d):
                c = r + d
                x[r][c] = i
                i += 1
        else:
            for r in range(n-d-1,-1,-1):
                c = r + d
                x[r][c] = i
                i += 1
    return x 
exec(input().strip()) 