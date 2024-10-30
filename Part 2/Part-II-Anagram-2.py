w1 = input()
w2 = input()
a = w1.strip().lower()
b = w2.strip().lower()
A = {}
B = {}
k1 = []
k2 = []
for i in a:
    if 'a' <= i <= 'z':
        if i not in A:
            A[i] = 1
        else:
            A[i] += 1
for i in b:
    if 'a' <= i <= 'z':
        if i not in B:
            B[i] = 1
        else:
            B[i] += 1
for i in A:
    k1.append([i,A[i]])
for i in B:
    k2.append([i,B[i]])
Ar = {}
Br = {}
for i in A.keys():
    for k in B.keys():
        if i in B:
            if A[i] == B[i]:
                Ar[i] = 0
                Br[i] = 0
            elif A[i] > B[i]:
                Ar[i] = A[i] - B[i]               
            elif B[i] > A[i]:
                Br[i] = B[i] - A[i]
        if i not in B:
            Ar[i] = A[i]
        if k not in A:
            Br[k] = B[k]
a = sorted(Ar)
b = sorted(Br)
ca = 0;cb = 0
for i in Ar:
    ca += Ar[i]
for i in Br:
    cb += Br[i]
if ca == 0:
    print(w1)
    print(' - None')
else:
    print(w1)
    for i in a:
        if Ar[i] == 1:
            print(' - remove '+'1 '+i)
        elif Ar[i] > 1:
            print(' - remove '+str(Ar[i])+' '+i+"'s")
if cb == 0:
    print(w2)
    print(' - None')
else:
    print(w2)
    for i in b:
        if Br[i] == 1:
            print(' - remove '+'1 '+i)
        elif Br[i] > 1:
            print(' - remove '+str(Br[i])+' '+i+"'s")

            


        
