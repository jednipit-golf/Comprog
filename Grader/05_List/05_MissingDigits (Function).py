def missing_digits(t):
    OOO = []
    A = len(t)
    c = ['0','1','2','3','4','5','6','7','8','9']
    k = []
    s = []
    ans = ''
    for i in range(A):
        if t[i] == '0':k.append('0')
        elif t[i] == '1':k.append('1')
        elif t[i] == '2':k.append('2')
        elif t[i] == '3':k.append('3')
        elif t[i] == '4':k.append('4')
        elif t[i] == '5':k.append('5')
        elif t[i] == '6':k.append('6')
        elif t[i] == '7':k.append('7')
        elif t[i] == '8':k.append('8')
        elif t[i] == '9':k.append('9')
    k.sort()
    K = len(k)
    if K != 0:
        x = k[0]
        s.append(x)
        for i in range(1,K-1):
            if x == k[i]:pass
            elif x != k[i]:
                s.append(k[i])
                x = k[i]
        if len(s) == 10:return OOO
        else:
            for i in s:
                c.remove(i)
            C = len(c)
            for i in range(C):
                OOO.append(int(c[i]))
            return (OOO)
    else:
       return [0,1,2,3,4,5,6,7,8,9]
    
exec(input()) 