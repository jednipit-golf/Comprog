def row_number(t, e):
    rA = len(t)
    cA = len(t[0])
    for i in range(rA):
        for j in t[i]:
            if j == e:
                return i  
def flatten(t):
    c = []
    for i in t:
        for j in i:
            if j == 0:
                pass
            else:
                c.append(j)
    return c
def inversions(t):
    c = 0
    if type(t[0]) == list:
        x = flatten(t)
        for i in range(len(x)):
            for j in range(i,len(x)):
                if x[i] > x[j]:
                    c += 1
    elif type(t[0]) == int:
        for i in range(len(t)):
            for j in range(i,len(t)):
                if t[i] > t[j]:
                    c += 1
    return c
def solvable(t):
    if len(t)%2 == 1:
        if inversions(t)%2 == 0:
            return True
        else:
            return False     
    else:
        if inversions(t)%2 == 1:
            if row_number(t,0)%2 == 0:
                return True
            else:
                return False
        else:
            if row_number(t,0)%2 == 1:
                return True
            else:
                return False
exec(input().strip()) 