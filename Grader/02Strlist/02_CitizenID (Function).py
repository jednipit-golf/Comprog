def check_digit(n):
    a = int(n[0])*13
    b = int(n[1])*12
    c = int(n[2])*11
    d = int(n[3])*10
    e = int(n[4])*9
    f = int(n[5])*8
    g = int(n[6])*7
    h = int(n[7])*6
    i = int(n[8])*5
    j = int(n[9])*4
    k = int(n[10])*3
    l = int(n[11])*2
    Z = (a+b+c+d+e+f+g+h+i+j+k+l)%11
    X=(11-Z)%10
    #n12 = (11 - (13*n[0]+12*n[1]+11*n[2]+10*n[3]+9*n[4]+8*n[5]+7*n[6]+6*n[7]+5*n[8]+4*n[9]+3*n[10]+2*n[11])%11)%10
    return X

exec(input())