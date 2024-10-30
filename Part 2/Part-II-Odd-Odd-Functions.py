def is_odd(n):
    if n%2 == 1:
        return True
    else:
        return False

def has_odds(x):
    a = False
    for i in x:
        if i %2 == 1:
            a = True
    return a
def all_odds(x):
    a = True
    for i in x:
        if i %2 == 0:
            a = False
    return a

def no_odds(x):
    a = True
    for i in x:
        if i %2 == 1:
            a = False
    return a

def get_odds(x):
    a = []
    for i in x:
        if i%2 == 1:
            a.append(i)
    return a
        
def zip_odds(a, b):
    A = []
    B = []
    ANS = []
    for i in a:
        if i%2 == 1:
            A.append(i)
    for i in b:
        if i%2 == 1:
            B.append(i)
    c = min(len(A),len(B))
    for i in range(c):
        ANS.append(A[i])
        ANS.append(B[i])
    if len(A) > len(B):
        for i in range(c,len(A)):
            ANS.append(A[i])
    elif len(A) < len(B):
        for i in range(c,len(B)):
            ANS.append(B[i])
    return ANS     

exec(input().strip()) 