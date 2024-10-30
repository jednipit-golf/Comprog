D = input().strip().upper()
d = len(D)
O = input()
c = [0,0,0,0]
C = 0
k = 0
ans = ''
for i in D:
    if i not in  'ATCG':
        k += 1
if k == 0:
    if O == 'R':
        for i in D:
            if i == 'A':
                ans += 'T'
            elif i == 'T':
                ans += 'A'
            elif i == 'C':
                ans += 'G'
            elif i == 'G':
                ans += 'C'
        print(ans[::-1])
    elif O == 'F':
        for i in D:
            if i == 'A':
                c[0] += 1
            elif i == 'T':
                c[1] += 1
            elif i == 'C':
                c[2] += 1
            elif i == 'G':
                c[3] += 1
        print('A='+str(c[0])+', '+'T='+str(c[1])+', '+'G='+str(c[3])+', '+'C='+str(c[2]))
    elif O == 'D':
        pp = input()
        for i in range(len(D)-1):
            if pp == D[i:i+2]:
                C += 1
        print(C)
else:
    print('Invalid DNA')