def reverse(d):
    c = {}
    for i in d.keys():
        b = d[i]
        c[b] = i
    return c

def keys(d, v):
    c = []
    for i in d.keys():
        b = d[i]
        if b == v:
            c.append(i)
    return c
   
exec(input().strip())