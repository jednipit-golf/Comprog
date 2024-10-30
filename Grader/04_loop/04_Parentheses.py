A = input()
t = ''
for i in A:
    if i == '(':
        t += '['
    elif i =='[':
        t += '('
    elif i == ')':
            t += ']'
        elif i == ']':
            t += ')'
        else:
            t += i
    print(t)
