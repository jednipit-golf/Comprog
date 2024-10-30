def peaks(x):
    c = len(x)
    k = []
    for i in range(1,c-1):
        if x[i-1] < x[i] and x[i] > x[i+1]:
            k.append(i)
    return k
exec(input()) 