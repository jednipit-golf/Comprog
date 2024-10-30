w = input().strip()
if w[-1] == 's' or w[-1] == 'x':
    w +='es'
elif w[-1] == 'h' and w[-2] == 'c':
     w +='es'
elif w[-1] == 'y':
    if w[-2] != 'a' and w[-2] != 'e' and w[-2] != 'i' and w[-2] != 'o' and w[-2] != 'u':
        w = w[:-1:] 
        w += 'ies'
    else:
        w += 's'   
else:
    w += 's'
print(w)