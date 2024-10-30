def zzip(x,y):
    ans = []
    X = len(x)
    Y = len(y)
    if X == Y:
        for i in range(X):
            ans.append(x[i])
            ans.append(y[i])
        return ans
    elif X > Y:
        for i in range(Y):
            ans.append(x[i])
            ans.append(y[i])
        for i in range(Y,X):
             ans.append(x[i])
        return ans
    elif X < Y:
        for i in range(X):
            ans.append(x[i])
            ans.append(y[i])
        for i in range(X,Y):
             ans.append(y[i])
        return ans
    
def reverse_digits(t):
    numbers = ''
    for e in t:
        if '0' <= e <= '9':
            numbers += e
    ans = ''
    for e in t:
        if '0' <= e <= '9':
            ans += numbers[-1]
            n = len(numbers)
            numbers = numbers[:n-1:]
        else:
            ans += e
    return ans
    

    
    
    
    
    
    
