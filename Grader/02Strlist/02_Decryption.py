a = input()
X = ['J','A','B','C','D','E','F','G','H','I','J']
b = a[3::7]
c = a[7::5]
d = str(int(b)+int(c)+10000)
e = d[-4:-1]
f = str(int(e[0])+int(e[1])+int(e[2]))
f_check = (int(e[0])+int(e[1])+int(e[2])+1)%10
ANS_1 = e+X[f_check]
print(ANS_1)
