t = input().lower()
s = ''
for e in t:
    if '0' <= e <= '9' or \
       'a' <= e <= 'z':
        s += e
    else:
        s += ' '
w = s.split()
camel = w[0]
for e in w[1:]:
    camel += e[0].upper() + e[1:]
print(camel)