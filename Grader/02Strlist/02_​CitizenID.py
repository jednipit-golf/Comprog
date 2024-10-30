n = input()
a1 = 13*int(n[0])
a2 = 12*int(n[1])
a3 = 11*int(n[2])
a4 = 10*int(n[3])
a5 = 9*int(n[4])
a6 = 8*int(n[5])
a7 = 7*int(n[6])
a8 = 6*int(n[7])
a9 = 5*int(n[8])
a10 = 4*int(n[9])
a11 = 3*int(n[10])
a12 = 2*int(n[11])
A = (11-((a1+a2+a3+a4+a5+a6+a7+a8+a9+a10+a11+a12)%11))%10
print(n[0]+" "+n[1:5:1]+" "+n[5:10:1]+" "+n[10:12:1]+" "+str(A))
    


