nexts = {}
while True:
    a = input().split()
    if len(a) == 1:
        break
    b2,b1 = a
    if b1 not in nexts:nexts[b1] = set()
    if b2 not in nexts:nexts[b2] = set()
    nexts[b1].add(b2)
    nexts[b2].add(b1)
q = a[0]
if q in nexts:
    results = set(nexts[q])
    for s in nexts[q]:
        results |= nexts[s]
    print('\n'.join(sorted(results)))
else:
    print(q)