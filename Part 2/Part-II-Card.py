c = input().strip()
k = []
v = {'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10,'J':11,'Q':12,'K':13}
vv = {'C':1,'D':2,'H':3,'S':4}
ans = ''
for i in range(len(c)//2):
    w = c[i*2:i*2+2]
    k.append(w)
for i in range(len(k)-1):
    s = i+1
    d = v[str(k[i][0])] - v[str(k[s][0])]
    if d > 0:
        ans += '+'+str(d)
    elif d < 0:
        ans += str(d)
    elif d == 0:
            y = vv[str(k[i][1])] - vv[str(k[s][1])]
            if y > 0:
                ans += '+'+str(y)
            elif y < 0:
                ans += str(y)
            elif y == 0:
                ans += '0'
print(ans)
    
      

    