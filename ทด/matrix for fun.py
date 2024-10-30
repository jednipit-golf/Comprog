def print_matrix(m):
    if len(m) == 1:
        print(m)
    else:
        print('[' + str(m[0]))
        for i in range(1,len(m)-1):
            print(' ' + str(m[i]))
        print(' ' + str(m[-1]) + ']' )
def read_matrix():
    m = []
    nrows = int(input())
    for k in range(nrows):
        x = input().split()
        r = []
        for e in x:
            r.append(float(e))
        m.append(r)
    f = print_matrix(m)
    return f
def add_matrix(a,b):
    c = []
    nrows = len(a)
    ncols = len(a[0])
    for i in range(nrows):
        c.append([0.0]*ncols)
        for j in range(ncols):
            c[i][j] = a[i][j] +b[i][j]
    return print_matrix(c)
            
            
            
            
