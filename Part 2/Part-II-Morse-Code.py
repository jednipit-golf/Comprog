def T2M(a):
    data = []
    for i in pattern:
        if 'A' <= i <= 'Z':
            data.append(i)
    morse = ''
    for e in a:
        if e in data:
            j = pattern.find('[' + e + ']')
            j += 3
            k = pattern.find('[',j)
            morse += pattern[j:k] + ' '
        else:
            morse = 'Invalid : '+a
            break
    return morse  
def M2T(a):
    f = ' '.join(a)
    text = ''
    morse = []
    m = ''
    for i in pattern:
        if 'A' <= i <= 'Z':pass
        elif i == '[':
            morse.append(m)
            m = ''
        elif i == ']':pass
        else:
            m+= i      
    A = len(a)
    for i in range(A):
        if a[i] in morse:
            p = pattern.find(']' + a[i] + '[')
            p -= 1
            text += pattern[p]
        else:
            text = 'Invalid : '+f
            break
    return text
filename = input().strip()
f1 = open(filename,'r')
code = f1.readline().strip()
pattern = f1.readline().strip()
if code == 'T2M':
    for i in f1:
        a = i.strip()
        print(T2M(a))
elif code == 'M2T':
    for i in f1:
        a = i.strip().split()
        print(M2T(a))
else:
    print('Invalid code')
f1.close()
