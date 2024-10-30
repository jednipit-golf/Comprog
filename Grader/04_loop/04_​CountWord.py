w = input()
t = input()
c = 0
T = ''
for n in t:
    if n in ['"', '(' , ')', ',', '.', "'"]:
        T +=' '
    else:
        T += n
for i in T.split():
    if i == w:
        c+=1      
print(c)