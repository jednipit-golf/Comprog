n = int(input())
if n == 0:
    print(0)
    print(0)
else:
    su = set([int(i) for i in input().split()])
    si = set(su)
    for i in range(n-1):
        s = set([int(i) for i in input().split()])
        su |= s
        si &= s
    print(len(su))
    print(len(si))

        
