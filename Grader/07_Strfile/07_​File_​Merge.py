def less(sid1,sid2):
    if sid1[-2:] < sid2[-2:]:
        return True
    elif sid1[-2:] > sid2[-2:]:
        return False
    else:
        return sid1 < sid2

def read_next(f):
    t = f.readline()
    if len(t) == 0:
        return ['','']
    return t.strip().split()

fn1, fn2 = input().split()
f1 = open(fn1, 'r')
f2 = open(fn2, 'r')
sid1, g1 = read_next(f1)
sid2, g2 = read_next(f2)

while sid1 != '' and sid2 != '':
    if less(sid1,sid2):
        print(sid1, g1)
        sid1, g1 = read_next(f1)
    else:
        print(sid2, g2)
        sid2, g2 = read_next(f2)
while sid1 != '':
    print(sid1, g1)
    sid1, g1 = read_next(f1)
while sid2 != '':
    print(sid2, g2)
    sid2, g2 = read_next(f2)
f1.close()
f2.close()
