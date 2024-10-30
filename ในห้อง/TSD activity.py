n = int(input())
z = {}
for i in range(n):
    a = input()
    k = a.split(',')
    k[0] = k[0].split()
    z[k[0][0]] = [k[0][1]]+k[1:]
while True:
    a = set()
    b = set()
    name = input()
    if name == 'q':
        break
    j = name.split()
    k1 = z[j[0]]
    k2 = z[j[1]]
    for i in k1:
        a.add(i)
    for j in k2:
        b.add(j)
    c = a.intersection(b)
    print(sorted(c))