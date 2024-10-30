k = 0
A = []
while k == 0:
    a =input()
    if a == "q":
        break
    else:
        A += [float(a)]
if len(A) == 0:
    print('No Data')
else:    
    X = sum(A)/len(A)
    print(round(X,2))
    
    