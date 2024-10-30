dm=[0,31,28,31,30,31,30,31,31,30,31,30,31]
mo=[0,1,2,3,4,5,6,7,8,9,10,11,12]
tp={'E':1,'Q':3,'N':7,'F':14}
order = []
while True:
    n = input().split()
    if n == ['END']:
        break
    ids = n[0]
    t = n[1]
    d = int(n[2])
    m = int(n[3])
    y = int(n[4])
    y -= 543
    if (y%400==0) or (y%4==0 and y%100!=0):
        dm[2] = 29
    else:
        dm[2] = 28
    y += 543
    if y < 2558:
        print('Error: '+ids+' '+t+' '+str(d)+' '+str(m)+' '+str(y)+' --> Invalid year')
    elif not m in mo or m == 0:
        print('Error: '+ids+' '+t+' '+str(d)+' '+str(m)+' '+str(y)+' --> Invalid month')
    elif d >  dm[m] or d == 0:
        print('Error: '+ids+' '+t+' '+str(d)+' '+str(m)+' '+str(y)+' --> Invalid date')
    elif t not in 'EQFN':
        print('Error: '+ids+' '+t+' '+str(d)+' '+str(m)+' '+str(y)+' --> Invalid delivery type')
    else:
        d += tp[t]
        if d > dm[m]:
            d-= dm[m]
            m+= 1
        if m > 12:
            m-=12
            y+=1
        order.append([[y,m,d],ids])
order.sort()
for e in order:
    print(e[-1]+': delivered on '+str(e[0][-1])+'/'+str(e[0][-2])+'/'+str(e[0][-3]))

        
        

