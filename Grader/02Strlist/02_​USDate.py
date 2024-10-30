a = input()
A = a.split("/")
M = int(A[1])-1 ; y = ['January','February','March','April','May','June','July','August','September','October','November','December']
Z = y[M]
print(Z+' '+A[0]+', '+A[2])