def add_poly(p1, p2):
    p = dict([(e,c) for c,e in p2])
    for c,e in p1:
        if e in p:
            p[e] += c
        else:
            p[e] = c
    return [(p[e],e) for e in sorted(p)[::-1] if p[e] != 0]  
def mult_poly(p1, p2):
    p = {}
    for c1,e1 in p1:
        for c2,e2 in p2:
            e = e1 + e2
            c = c1 * c2
            if e in p:
                p[e] += c
            else:
                p[e] = c
    return [(p[e],e) for e in sorted(p)[::-1] if p[e] != 0]
for i in range(3):
    exec(input().strip())